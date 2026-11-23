---
name: fetch-quarterly
description: Snapshot a company's latest 10-Q or 10-K from SEC EDGAR into the repo with provenance. Saves the filing, a facts TSV and TTM/share/price ratio inputs under <ticker>/quarterly/. Use when asked to fetch, refresh, pull or update quarterly data, or to check a P/S, P/E or market-cap figure against filings.
argument-hint: <TICKER> [period YYYY-MM-DD]
allowed-tools: Bash(python3 *) Bash(curl *) Read Grep
---

# Fetch a filing snapshot from EDGAR

Target: **$ARGUMENTS**

EDGAR is the only authority for financials. One tested script does the work: `scripts/edgar_snapshot.py`. Do not hand-roll curl calls or use third-party financial APIs for the numbers; they can disagree with the filing.

## Before you run

- `SEC_USER_AGENT` must be set in the environment to a descriptive string with a contact (the SEC blocks requests without one; a generic agent got HTTP 403). If it is not set, stop and tell the user. Never put the user's email, or any contact you invented, in a request header on your own.
- Ticker and "latest" are enough; don't ask questions in the obvious case. Ask only if there is no ticker, or the ticker folder doesn't exist (folder names don't always match, e.g. NET is `cloudflare/`; pass `--outdir`).

## Run

```bash
python3 scripts/edgar_snapshot.py TICKER --price            # latest 10-Q or 10-K, into <ticker>/quarterly/
python3 scripts/edgar_snapshot.py TICKER --period 2026-09-30 --outdir some/quarterly
```

It writes, with the repo's `YYYY_Q#_` names (fiscal labels from the filing's cover tags, `YYYY_FY_10k` for a 10-K), and refuses to overwrite without `--force`:

| File | Content |
|---|---|
| `YYYY_Q#_10q.htm` | the primary iXBRL document |
| `YYYY_Q#_10q_facts.tsv` | every numeric fact with period, segments, accession number and filed date |
| `YYYY_Q#_10q_ratio_inputs.json` | TTM revenue and net income (with the rows used), cover-page shares by class, diluted weighted shares, cash, equity, debt candidates, and with `--price` the close, market cap, P/S and P/E on both share bases |

## What the script already guards, and what you must still check

- **Period guard:** it aborts if page one of the document doesn't match the period EDGAR lists. (Once a Q2 10-Q was mistaken for the Q3 one.)
- **TTM** = latest fiscal year − prior-year YTD + current YTD, from facts deduplicated by period with the latest filing winning (later filings restate and re-round, so a figure can move by 1m). Q4 is never a reported quarter.
- **Shares:** the cover-page count is per class and is absent from the `companyfacts` feed for multi-class companies, so the script reads it from the document. Report both bases (cover total and diluted weighted average) and say which one a figure uses. They can differ a lot (SMCI: 659m vs 749m).
- **You must still:** read the balance sheet for debt and lease balances (tag names vary; the JSON lists candidates, and the maturity ladder is in the facts TSV), and compute EV/Sales from them with the working shown. P/S alone flatters leveraged companies (CRWV: P/S 2.2x, EV/Sales about 6.4x).
- **Stock splits:** Yahoo prices are split-adjusted but filing share counts are not, so the script scales shares by any split dated after the cover date (cover shares) or the filing date (diluted shares) and prints a WARNING when it does. SNDK's 8-for-1 split on 20 Nov 2026 made the unadjusted P/E 0.7.
- **Negative earnings:** P/E is `n/m`, never a negative number.

## Other kinds of company

- **20-F filers** (foreign private issuers on EDGAR, e.g. ASML) are supported on an **annual basis only**. The output states the basis and how many days old it is (ASML: 326 days). Their quarterly and half-year numbers come as 6-K press releases with no structured data, so TTM cannot be built from EDGAR: treat the ratio as stale and, if a current one is needed, use the manual route below. If the financials are in a different currency from the price (ASML: EUR vs USD), the script skips the ratios; convert before comparing.
- **Not an SEC registrant** (DRO.AX, ENR.DE, RYCEY) or a **6-K / 40-F only** filer: the script says so. Don't fall back to a guess. Copy `scripts/manual_inputs_template.json` to `<ticker>/quarterly/YYYY_Q#_manual_inputs.json`, fill every number from the company's own report with its source, use `null` for anything not found, then run `python3 scripts/edgar_snapshot.py --ratios-from <file>`. It computes market cap, P/S, P/E and, if debt and cash are given, EV/Sales, and refuses on missing values or a currency mismatch.
- **8-K results (Item 2.02) and press releases:** list filings from `https://data.sec.gov/submissions/CIK{cik}.json` with the same User-Agent, save the 8-K as `YYYY_Q#_8k.htm` and the Exhibit 99.1 text as `YYYY_Q#_press_release.txt`.

## After

Show the summary and the file list. Do not commit unless asked. If you changed a number that a diary table or model quotes, say which one.
