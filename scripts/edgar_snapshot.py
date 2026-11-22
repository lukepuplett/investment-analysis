#!/usr/bin/env python3
"""
Take a reproducible snapshot of a company's latest 10-Q / 10-K from SEC EDGAR.

Writes into <ticker>/quarterly/ (repo convention, never overwritten without --force):
  YYYY_Q#_10q.htm (or YYYY_FY_10k.htm)   the primary iXBRL document
  YYYY_Q#_10q_facts.tsv                   numeric facts with provenance (accession, filed date)
  YYYY_Q#_10q_ratio_inputs.json           TTM revenue / net income, shares, cash, equity, provenance
and prints a short summary. Optional --price adds the last regular close (Yahoo chart API) and P/S, P/E.

Needs: Python 3, ixbrlparse (scripts/requirements-ixbrl.txt). Set SEC_USER_AGENT to a descriptive
string with a contact, as the SEC asks, e.g.  export SEC_USER_AGENT="YourOrg research you@example.com".
The script never embeds a contact of its own.

20-F filers (foreign private issuers that file inline XBRL, e.g. ASML) are supported on an ANNUAL basis only:
facts use the ifrs-full taxonomy, the TTM figure is the latest fiscal year, and the output says how stale it is.
Their quarterly and half-year numbers arrive as 6-K press releases with no structured data, so they are not read.
Companies that are not SEC registrants are reported as unsupported; for those, fill a manual inputs file
(scripts/manual_inputs_template.json) and compute ratios with --ratios-from.

Examples:
  python3 scripts/edgar_snapshot.py CRWV --price
  python3 scripts/edgar_snapshot.py NET --outdir cloudflare/quarterly
  python3 scripts/edgar_snapshot.py DDOG --period 2026-09-30 --outdir /tmp/ddog
  python3 scripts/edgar_snapshot.py ASML --price                 # 20-F, annual basis
  python3 scripts/edgar_snapshot.py --ratios-from enr/quarterly/2026_FY_manual_inputs.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import warnings
import urllib.error
import urllib.request
from pathlib import Path

warnings.filterwarnings("ignore", module="ixbrlparse")  # unimplemented ixt formats on non-numeric text facts
REPO = Path(__file__).resolve().parent.parent
FORMS = ("10-Q", "10-K", "20-F")
TAGS = {  # taxonomy -> metric -> candidate tags, in order of preference
    "us-gaap": {
        "revenue": ("Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                    "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"),
        "net_income": ("NetIncomeLoss", "ProfitLoss"),
        "diluted_shares": ("WeightedAverageNumberOfDilutedSharesOutstanding",),
        "cash": ("CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"),
        "equity": ("StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"),
    },
    "ifrs-full": {
        "revenue": ("Revenue", "RevenueFromContractsWithCustomers"),
        "net_income": ("ProfitLossAttributableToOwnersOfParent", "ProfitLoss"),
        "diluted_shares": ("AdjustedWeightedAverageShares", "WeightedAverageShares"),
        "cash": ("CashAndCashEquivalents",),
        "equity": ("EquityAttributableToOwnersOfParent", "Equity"),
    },
}
DEBT_NAME = re.compile(r"Debt|Notes|Borrowings|Loan|Lease", re.I)
DAY = dt.timedelta(days=1)


class SnapshotError(Exception):
    pass


def user_agent() -> str:
    ua = os.environ.get("SEC_USER_AGENT", "").strip()
    if not ua:
        raise SnapshotError("Unable to call SEC EDGAR. SEC_USER_AGENT is not set; export a descriptive "
                            "string with a contact, e.g. export SEC_USER_AGENT=\"YourOrg research you@example.com\".")
    return ua


def get(url: str, ua: str, tries: int = 4) -> bytes:
    last = None
    for i in range(tries):
        time.sleep(0.2)  # stay well under the SEC's 10 requests/second
        req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept-Encoding": "identity"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (403, 429, 500, 502, 503):
                time.sleep(2 * (i + 1))
                continue
            raise SnapshotError(f"Unable to fetch {url}. HTTP {e.code}.")
        except urllib.error.URLError as e:
            last = e
            time.sleep(2 * (i + 1))
    raise SnapshotError(f"Unable to fetch {url}. {last}")


def resolve_cik(ticker: str, ua: str) -> tuple[int, str]:
    data = json.loads(get("https://www.sec.gov/files/company_tickers.json", ua))
    for row in data.values():
        if row["ticker"].upper() == ticker.upper():
            return int(row["cik_str"]), row["title"]
    raise SnapshotError(f"Unable to find {ticker} in the SEC ticker list. It is probably not an SEC registrant "
                        "(for example a non-US listing); use the company's own reports instead.")


def pick_filing(subs: dict, period: str | None) -> dict:
    r = subs["filings"]["recent"]
    rows = [dict(form=r["form"][i], filed=r["filingDate"][i], report=r["reportDate"][i],
                 accn=r["accessionNumber"][i], doc=r["primaryDocument"][i]) for i in range(len(r["form"]))]
    cands = [x for x in rows if x["form"] in FORMS and (period is None or x["report"] == period)]
    if not cands:
        other = sorted({x["form"] for x in rows if x["form"] in ("40-F", "6-K")})
        hint = f" It files {', '.join(other)} instead; this script does not support those." if other else ""
        raise SnapshotError("Unable to find a 10-Q or 10-K" + (f" for period {period}" if period else "") + f".{hint}")
    return max(cands, key=lambda x: (x["report"], x["filed"]))


def facts_from_doc(path: Path):
    from ixbrlparse import IXBRL
    with open(path, "rb") as f:
        return IXBRL(f)


def ctx_period(ctx) -> str:
    if ctx is None:
        return ""
    if getattr(ctx, "instant", None):
        return f"instant={ctx.instant}"
    return f"duration={ctx.startdate}..{ctx.enddate}"


def ctx_segments(ctx) -> str:
    if ctx is None or not getattr(ctx, "segments", None):
        return ""
    return "; ".join(f"{s.get('dimension')}={s.get('value')}" for s in ctx.segments)


def dei_text(ix, name: str) -> str | None:
    for v in ix.nonnumeric:
        if v.name == name and v.schema == "dei":
            return " ".join(str(v.value).split())
    return None


def cover_shares(ix) -> dict:
    by_class, asof = {}, None
    for v in ix.numeric:
        if v.name == "EntityCommonStockSharesOutstanding" and v.schema == "dei":
            seg = ctx_segments(v.context) or "(single class)"
            by_class[seg] = float(v.value)
            asof = str(getattr(v.context, "instant", "")) or asof
    basis = "cover page"
    if not by_class:  # 20-F filers often have no cover count; fall back to the period-end balance
        for v in ix.numeric:
            if v.name in ("NumberOfSharesOutstanding", "SharesOutstanding") and not ctx_segments(v.context) and getattr(v.context, "instant", None):
                by_class["(period-end, no class split)"] = float(v.value)
                asof = str(v.context.instant)
        basis = "period-end balance (no cover-page count found)"
    return {"as_of": asof, "basis": basis, "by_class": by_class, "total": sum(by_class.values()) if by_class else None}


def parse_d(s: str) -> dt.date:
    return dt.date.fromisoformat(s)


def doc_period_iso(text: str | None) -> str | None:
    if not text:
        return None
    for fmt in ("%B %d, %Y", "%Y-%m-%d", "%d %B %Y", "%b %d, %Y"):
        try:
            return dt.datetime.strptime(text.strip(), fmt).date().isoformat()
        except ValueError:
            pass
    return None


def dedupe_durations(rows: list[dict]) -> list[dict]:
    """One row per (start, end): the latest filing wins, because later filings restate and re-round."""
    best = {}
    for r in rows:
        if "start" not in r:
            continue
        k = (r["start"], r["end"])
        if k not in best or r["filed"] > best[k]["filed"]:
            best[k] = r
    return list(best.values())


def duration_days(r: dict) -> int:
    return (parse_d(r["end"]) - parse_d(r["start"])).days + 1


def near(a: dt.date, b: dt.date, tol: int = 7) -> bool:
    return abs((a - b).days) <= tol


def pick_unit(facts: dict, tags: tuple) -> str | None:
    """The unit with the most rows for the first tag that has any (USD, EUR, ...; never shares or pure)."""
    for tag in tags:
        units = {u: rs for u, rs in facts.get(tag, {}).get("units", {}).items() if "/" not in u and u not in ("shares", "pure")}
        if units:
            return max(units, key=lambda u: len(units[u]))
    return None


def ttm_for(facts: dict, tags: tuple, period_end: str, unit: str | None = None) -> dict:
    """TTM ending at period_end from deduped duration facts: FY(prior) + YTD(current) - YTD(prior year)."""
    end = parse_d(period_end)
    unit = unit or pick_unit(facts, tags) or "USD"
    for tag in tags:
        rows = dedupe_durations([dict(r, tag=tag) for r in facts.get(tag, {}).get("units", {}).get(unit, [])])
        cur = [r for r in rows if parse_d(r["end"]) == end and duration_days(r) >= 80]
        if not cur:
            continue
        cur = max(cur, key=duration_days)
        used = [cur]
        if duration_days(cur) >= 350:
            return {"tag": tag, "value": cur["val"], "unit": unit, "method": "latest fiscal year", "rows": used}
        cstart = parse_d(cur["start"])
        fy = [r for r in rows if duration_days(r) >= 350 and near(parse_d(r["end"]), cstart - DAY)]
        py = [r for r in rows if near(parse_d(r["start"]), cstart.replace(year=cstart.year - 1))
              and near(parse_d(r["end"]), end.replace(year=end.year - 1)) and abs(duration_days(r) - duration_days(cur)) <= 7]
        if not fy or not py:
            return {"tag": tag, "value": None, "unit": unit, "method": "missing prior fiscal year or prior-year YTD", "rows": used}
        fy, py = max(fy, key=lambda r: r["end"]), max(py, key=lambda r: r["filed"])
        used += [fy, py]
        return {"tag": tag, "value": fy["val"] + cur["val"] - py["val"], "unit": unit,
                "method": "FY(prior) + YTD(current) - YTD(prior year)", "rows": used}
    return {"tag": None, "value": None, "method": "no matching tag at the period end", "rows": []}


def instant_value(facts: dict, tags: tuple, period_end: str, unit: str | None = None) -> dict:
    unit = unit or pick_unit(facts, tags) or "USD"
    for tag in tags:
        rows = [r for r in facts.get(tag, {}).get("units", {}).get(unit, []) if r["end"] == period_end and "start" not in r]
        if rows:
            r = max(rows, key=lambda r: r["filed"])
            return {"tag": tag, "value": r["val"], "unit": unit, "filed": r["filed"], "accn": r["accn"]}
    return {"tag": None, "value": None}


def latest_quarter_shares(facts: dict, tags: tuple, period_end: str) -> dict:
    end = parse_d(period_end)
    for tag in tags:
        rows = dedupe_durations([r for r in facts.get(tag, {}).get("units", {}).get("shares", [])])
        q = [r for r in rows if parse_d(r["end"]) == end and 80 <= duration_days(r) <= 100]
        if not q:
            q = [r for r in rows if parse_d(r["end"]) == end]
        if q:
            r = min(q, key=duration_days)
            return {"tag": tag, "value": r["val"], "start": r["start"], "end": r["end"], "accn": r["accn"]}
    return {"value": None}


def yahoo_close(ticker: str) -> dict:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=5d&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        res = json.load(r)["chart"]["result"][0]
    closes = [(t, c) for t, c in zip(res["timestamp"], res["indicators"]["quote"][0]["close"]) if c is not None]
    t, c = closes[-1]
    return {"price": c, "date": dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%d"),
            "source": "Yahoo Finance chart API, last regular close", "currency": res["meta"].get("currency")}


def label(ix, filing: dict) -> tuple[str, str]:
    fp = (dei_text(ix, "DocumentFiscalPeriodFocus") or "").upper()
    fy = dei_text(ix, "DocumentFiscalYearFocus") or filing["report"][:4]
    if filing["form"] == "20-F":
        return f"{fy}_FY", "20f"
    if filing["form"] == "10-K" or fp == "FY":
        return f"{fy}_FY", "10k"
    return f"{fy}_{fp}", "10q"


def ratios_from_manual(path: Path) -> int:
    """Compute market cap, P/S, P/E and EV/Sales from a hand-filled inputs file (see manual_inputs_template.json)."""
    d = json.loads(path.read_text(encoding="utf-8"))
    need = {"ttm_revenue": d.get("ttm_revenue", {}).get("value"), "shares": d.get("shares", {}).get("value"),
            "price": d.get("price", {}).get("value")}
    missing = [k for k, v in need.items() if not v]
    if missing:
        print(f"ERROR: Unable to compute ratios. Missing values: {', '.join(missing)}.", file=sys.stderr)
        return 1
    cur, pcur = d.get("currency"), d["price"].get("currency")
    if cur and pcur and cur != pcur:
        print(f"ERROR: Unable to compute ratios. Financials are in {cur} but the price is in {pcur}; convert first.", file=sys.stderr)
        return 1
    mc = need["shares"] * need["price"]
    ni = d.get("ttm_net_income", {}).get("value")
    out = {"market_cap": mc, "price_to_sales": mc / need["ttm_revenue"],
           "price_to_earnings": (mc / ni) if ni and ni > 0 else "n/m"}
    debt, cash = d.get("debt", {}).get("value"), d.get("cash", {}).get("value")
    if debt is not None and cash is not None:
        ev = mc + debt + (d.get("leases", {}).get("value") or 0) - cash
        out["enterprise_value"], out["ev_to_sales"] = ev, ev / need["ttm_revenue"]
    d["ratios"] = out
    d["ratios_computed"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    path.write_text(json.dumps(d, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"{d.get('ticker')} ({cur}): market cap {mc:,.0f}  P/S {out['price_to_sales']:.2f}  P/E {out['price_to_earnings']}"
          + (f"  EV/Sales {out['ev_to_sales']:.2f}" if "ev_to_sales" in out else "  (no debt/cash given: EV skipped)"))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker", nargs="?")
    ap.add_argument("--ratios-from", type=Path, help="compute ratios from a manual inputs JSON (no EDGAR call)")
    ap.add_argument("--period", help="period end date YYYY-MM-DD (default: latest 10-Q or 10-K)")
    ap.add_argument("--outdir", type=Path, help="default: <repo>/<ticker lowercase>/quarterly")
    ap.add_argument("--price", action="store_true", help="add the last close and P/S, P/E")
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    a = ap.parse_args()
    if a.ratios_from:
        return ratios_from_manual(a.ratios_from)
    if not a.ticker:
        ap.error("ticker is required unless --ratios-from is given")
    try:
        ua = user_agent()
        cik, title = resolve_cik(a.ticker, ua)
        outdir = a.outdir or REPO / a.ticker.lower() / "quarterly"
        if not outdir.is_dir():
            raise SnapshotError(f"Unable to save to {outdir}. The folder does not exist; pass --outdir.")
        subs = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", ua))
        f = pick_filing(subs, a.period)
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{f['accn'].replace('-', '')}/{f['doc']}"
        tmp = outdir / f".{f['accn']}.download"
        tmp.write_bytes(get(url, ua))
        ix = facts_from_doc(tmp)
        # guard: the document on page one must be the period we asked EDGAR for
        doc_end = dei_text(ix, "DocumentPeriodEndDate")
        doc_end_iso = doc_period_iso(doc_end)
        if doc_end_iso != f["report"]:
            tmp.unlink()
            raise SnapshotError(f"Unable to verify the filing. Page one says period {doc_end}, EDGAR says {f['report']}.")
        stem, kind = label(ix, f)
        paths = {"doc": outdir / f"{stem}_{kind}.htm", "facts": outdir / f"{stem}_{kind}_facts.tsv",
                 "inputs": outdir / f"{stem}_{kind}_ratio_inputs.json"}
        existing = [p.name for p in paths.values() if p.exists()]
        if existing and not a.force:
            tmp.unlink()
            raise SnapshotError(f"Unable to save. Already exists: {', '.join(existing)}. Use --force to overwrite.")
        tmp.replace(paths["doc"])
        # facts with provenance
        with open(paths["facts"], "w", encoding="utf-8") as out:
            out.write("concept\tvalue\tunit\tperiod\tsegments\taccession\tfiled\n")
            rows = [(f"{v.schema}:{v.name}", str(v.value), str(getattr(v, 'unit', '') or ''), ctx_period(v.context), ctx_segments(v.context))
                    for v in ix.numeric]
            for r in sorted(rows):
                out.write("\t".join(r) + f"\t{f['accn']}\t{f['filed']}\n")
        # structured inputs
        all_facts = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", ua))["facts"]
        end = f["report"]
        ns = next((n for n in TAGS if ttm_for(all_facts.get(n, {}), TAGS[n]["revenue"], end)["tag"]), "us-gaap")
        facts, tg = all_facts.get(ns, {}), TAGS[ns]
        rev, ni = ttm_for(facts, tg["revenue"], end), ttm_for(facts, tg["net_income"], end)
        cover, wa = cover_shares(ix), latest_quarter_shares(facts, tg["diluted_shares"], end)
        age = (dt.date.today() - parse_d(end)).days
        debt = sorted({(v.name, float(v.value)) for v in ix.numeric
                       if not ctx_segments(v.context) and getattr(v.context, "instant", None) and str(v.context.instant) == end
                       and DEBT_NAME.search(v.name) and v.schema in ("us-gaap", "ifrs-full")})
        inputs = {
            "ticker": a.ticker.upper(), "company": title, "cik": cik, "form": f["form"], "period_end": end,
            "fiscal_label": stem, "accession": f["accn"], "filed": f["filed"], "source_url": url,
            "taxonomy": ns, "currency": rev.get("unit"), "basis": ("annual only: fiscal year ended %s, %d days before this snapshot" % (end, age)) if f["form"] == "20-F" else ("TTM to %s" % end),
            "ttm_revenue": rev, "ttm_net_income": ni, "cover_shares": cover, "diluted_weighted_shares": wa,
            "cash": instant_value(facts, tg["cash"], end), "equity": instant_value(facts, tg["equity"], end),
            "debt_candidates_review_balance_sheet": [{"concept": n, "value": v} for n, v in debt],
            "notes": ["Debt tags vary by company: confirm debt and lease balances on the balance sheet before computing EV.",
                      "Values from companyfacts are deduplicated by period, latest filing wins (later filings re-round)."],
            "snapshot_taken": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        }
        if a.price:
            px = yahoo_close(a.ticker)
            inputs["price"] = px
            shares = {"cover_total": cover["total"], "diluted_weighted": wa.get("value")}
            ratios = {}
            if px.get("currency") and rev.get("unit") and px["currency"] != rev["unit"]:
                inputs["ratios_skipped"] = f"currency mismatch: financials in {rev['unit']}, price in {px['currency']}; convert before computing ratios"
                shares = {}
            for name, sh in shares.items():
                if sh and rev["value"]:
                    mc = sh * px["price"]
                    ratios[name] = {"shares": sh, "market_cap": mc, "price_to_sales": mc / rev["value"],
                                    "price_to_earnings": (mc / ni["value"]) if ni["value"] and ni["value"] > 0 else "n/m"}
            inputs["ratios"] = ratios
        paths["inputs"].write_text(json.dumps(inputs, indent=2, default=str) + "\n", encoding="utf-8")
    except SnapshotError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print(f"{inputs['ticker']} {inputs['company']}: {f['form']} period {end}, filed {f['filed']}, accession {f['accn']}")
    for p in paths.values():
        print("  wrote", p)
    print(f"  basis          {inputs['basis']}  | taxonomy {ns}, currency {rev.get('unit')}")
    print(f"  TTM revenue    {rev['value']}  ({rev['method']}, tag {rev['tag']})")
    print(f"  TTM net income {ni['value']}  ({ni['method']}, tag {ni['tag']})")
    print(f"  cover shares   {cover['total']}  as of {cover['as_of']}  {cover['by_class']}")
    print(f"  diluted WASO   {wa.get('value')}")
    if a.price:
        print(f"  price {inputs['price']['price']} on {inputs['price']['date']}")
        if "ratios_skipped" in inputs:
            print("  ratios skipped:", inputs["ratios_skipped"])
        for k, v in inputs["ratios"].items():
            print(f"  [{k}] mcap {v['market_cap']:,.0f}  P/S {v['price_to_sales']:.2f}  P/E {v['price_to_earnings']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
