"""
Moderna (MRNA) toy projection: income statement, free cash flow and balance-sheet items, FY2026E-FY2030E.
FY2026 is built from management's FY2026 guidance (as recorded in mrna/analysis/2026_11_q3_delta_analysis.md) and the
Q3 2026 10-Q. FY2027-30 are ASSUMPTIONS in three scenarios. A toy, not a forecast, and not a recommendation.
Units: $ millions and millions of shares unless stated. Every input is in OFFICIAL, ASSUMPTIONS or SCENARIOS with a source.
Run:  python3 mrna_projection.py   -> writes output.md and cash_and_fcf.png in this folder.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
TENQ = "Q3 2026 10-Q (acc. 0001682852-26-000197)"
DELTA = "mrna/analysis/2026_11_q3_delta_analysis.md (FY2026 framework from the 6 Nov 2026 8-K)"
NOTE = "mrna/analysis/2026_11_23_profitability_and_intismeran_timing.md"
YEARS = (2026, 2027, 2028, 2029, 2030)

# =============================================================================
# 1. OFFICIAL INPUTS (value, source)
# =============================================================================
OFFICIAL = {
    "fy25_revenue": (1944, "DERIVED: TTM 2,525 - 9M26 1,847 + 9M25 1,266 (10-Q facts)"),
    "m9_revenue": (1847, TENQ), "m9_net_income": (-1963, TENQ), "m9_operating_income": (-2073, TENQ),
    "m9_interest_income": (201, TENQ + ": InvestmentIncomeInterest"), "m9_sbc": (351, TENQ), "m9_da": (173, TENQ),
    "m9_financing_cash_flow": (2776, TENQ + ": financing activities, mainly net convertible proceeds"),
    "begin_cash": (8135, TENQ + ": cash, equivalents and investments at 31 Dec 2025"),
    "cash_30sep": (7976, TENQ + ": cash 1,195 + investments 3,976 + non-current 2,805"),
    "equity_30sep": (6837, TENQ), "shares_cover": (404.62, "10-Q cover, 30 Oct 2026 (millions)"),
    "fy26_growth_low": (0.15, DELTA), "fy26_growth_high": (0.25, DELTA),
    "fy26_rd": (2700, DELTA + ": R&D about $2.7bn"), "fy26_sga": (1000, DELTA + ": SG&A about $1.0bn"),
    "fy26_cogs": (1700, DELTA + ": cost of sales about $1.7bn including about $0.9bn settlement charge"),
    "fy26_capex": (200, DELTA), "fy26_ye_cash_low": (8100, DELTA), "fy26_ye_cash_high": (8300, DELTA),
    "term_loan": (600, TENQ + ": senior secured, SOFR + 5.50% (9.23% at 30 Sep), due 24 Nov 2030, no amortisation"),
    "term_loan_rate": (0.0923, TENQ),
    "converts": (3000, TENQ + ": 0.00% convertible senior notes due 1 Mar 2032; conversion price about $210, cap about $392"),
    "convert_conv_price": (210.0, TENQ),
    "leases": (680, TENQ + ": operating and finance lease liabilities"),
    "ddtl_undrawn": (900, TENQ + ": $400m (to Nov 2027) + $500m (to Nov 2028, needs regulatory milestones); undrawn"),
    "price": (210.72, "Yahoo close, 23 Nov 2026"),
    "mgmt_cash_breakeven_year": (2028, NOTE + " (management target; not verified against the call)"),
}

def O(k):
    return OFFICIAL[k][0]

# =============================================================================
# 2. GLOBAL ASSUMPTIONS (value, source)
# =============================================================================
ASSUMPTIONS = {
    "growth_fy26": (0.20, "ASSUMPTION: midpoint of the 15-25% FY2026 revenue growth guide"),
    "ye26_cash": (8200, "midpoint of the $8.1-8.3bn year-end 2026 cash guide"),
    "cash_yield": (0.035, "ASSUMPTION: yield on opening cash; 9M26 interest income of 201 on about 8.0bn is about 3.4% annualised"),
    "interest_fees": (15, "ASSUMPTION: commitment fees on undrawn DDTLs and other, $m a year"),
    "other_nonop": (-60, "ASSUMPTION: other non-operating, $m a year (9M26: -58)"),
    "tax": (45, "ASSUMPTION: cash and book tax, $m a year (9M26: 33); losses carried forward, so no tax on any profit before 2031"),
    "da": (240, "ASSUMPTION: depreciation and amortisation, $m (9M26: 173)"),
    "sbc": (470, "ASSUMPTION: stock compensation, $m (9M26: 351), added back to cash flow and to equity"),
    "capex": (200, "ASSUMPTION: held at the FY2026 guide"),
    "wc_drag": (0.15, "ASSUMPTION: working capital absorbed per $1 of extra revenue (receivables about 10%, inventory about 5%)"),
    "sga_growth": (0.03, "ASSUMPTION: SG&A growth a year after 2027"),
    "share_creep": (0.015, "ASSUMPTION: share count growth a year from stock compensation; converts treated as debt"),
    "ar_pct": (0.10, "ASSUMPTION: year-end receivables as a share of annual revenue (Dec 2025: 184 on 1,944)"),
    "inv_pct": (0.10, "ASSUMPTION: year-end inventory as a share of annual revenue (Dec 2025: 153; Sep 2026: 313)"),
    "term_loan_repaid": (2030, "ASSUMPTION: the $600m term loan is repaid from cash at maturity in Nov 2030, not refinanced"),
}

def A(k):
    return ASSUMPTIONS[k][0]

# =============================================================================
# 3. SCENARIOS (2027-2030) — ASSUMPTIONS, illustrative
# =============================================================================
SCENARIOS = {
    "Bear": {
        "vax_growth": (-0.05, 0.00, 0.02, 0.02), "onc_revenue": (0, 0, 100, 400), "rd": (2700, 2700, 2600, 2600),
        "sga_2027": 1000, "vax_cogs": 0.40,
        "why": "Respiratory sales keep shrinking, oncology approval slips to 2029, R&D stays at the 2026 level to fund the oncology trials.",
    },
    "Base": {
        "vax_growth": (0.08, 0.08, 0.06, 0.06), "onc_revenue": (0, 150, 600, 1200), "rd": (2450, 2350, 2350, 2400),
        "sga_2027": 1000, "vax_cogs": 0.36,
        "why": "A full 2027-28 flu season and combo-vaccine approvals offset COVID decline; oncology approved around early 2028 with Moderna's share of revenue ramping; R&D trimmed about 9% then held.",
    },
    "Bull": {
        "vax_growth": (0.15, 0.12, 0.10, 0.08), "onc_revenue": (100, 700, 1800, 3000), "rd": (2300, 2150, 2100, 2100),
        "sga_2027": 1000, "vax_cogs": 0.33,
        "why": "Oncology approved in H2 2027 and launches fast; respiratory products grow; R&D cut about 15% by 2029.",
    },
}
ONC_COGS = 0.40  # ASSUMPTION: oncology cost of sales as a share of Moderna's oncology revenue (collaboration economics are shared with Merck)

# =============================================================================
# 4. ENGINE
# =============================================================================
def project(sc):
    rows = []
    rev26 = O("fy25_revenue") * (1 + A("growth_fy26"))
    oi26 = rev26 - O("fy26_cogs") - O("fy26_rd") - O("fy26_sga")
    int_inc26 = O("m9_interest_income") + A("cash_yield") * O("cash_30sep") / 4
    int_exp26 = O("term_loan") * O("term_loan_rate")
    ni26 = oi26 + int_inc26 - int_exp26 + A("other_nonop") - A("tax") - A("interest_fees")
    cash26 = A("ye26_cash")
    fcf26 = cash26 - O("begin_cash") - O("m9_financing_cash_flow")  # plug from the year-end cash guide
    eq26 = O("equity_30sep") + (ni26 - O("m9_net_income")) + (A("sbc") - O("m9_sbc"))
    rows.append(dict(year=2026, vax=rev26, onc=0.0, revenue=rev26, cogs=O("fy26_cogs"), rd=O("fy26_rd"), sga=O("fy26_sga"),
                     oi=oi26, int_inc=int_inc26, int_exp=int_exp26, ni=ni26, fcf=fcf26, financing=O("m9_financing_cash_flow"),
                     cash=cash26, term_loan=O("term_loan"), converts=O("converts"), leases=O("leases"),
                     ar=A("ar_pct") * rev26, inv=A("inv_pct") * rev26, equity=eq26, shares=O("shares_cover")))
    sga = sc["sga_2027"]
    for i, y in enumerate(YEARS[1:]):
        prev = rows[-1]
        vax = prev["vax"] * (1 + sc["vax_growth"][i]); onc = sc["onc_revenue"][i]; rev = vax + onc
        cogs = sc["vax_cogs"] * vax + ONC_COGS * onc
        if i > 0:
            sga = sga * (1 + A("sga_growth"))
        rd = sc["rd"][i]
        oi = rev - cogs - rd - sga
        int_inc = A("cash_yield") * prev["cash"]
        repaid = (y == A("term_loan_repaid"))
        int_exp = O("term_loan") * O("term_loan_rate") * (11 / 12 if repaid else 1.0) + A("interest_fees")
        ni = oi + int_inc - int_exp + A("other_nonop") - A("tax")
        wc = -A("wc_drag") * (rev - prev["revenue"])
        fcf = ni + A("da") + A("sbc") + wc - A("capex")
        financing = -O("term_loan") if repaid else 0.0
        cash = prev["cash"] + fcf + financing
        rows.append(dict(year=y, vax=vax, onc=onc, revenue=rev, cogs=cogs, rd=rd, sga=sga, oi=oi, int_inc=int_inc, int_exp=int_exp, ni=ni,
                         fcf=fcf, financing=financing, cash=cash, term_loan=0.0 if y >= A("term_loan_repaid") else O("term_loan"),
                         converts=O("converts"), leases=O("leases"), ar=A("ar_pct") * rev, inv=A("inv_pct") * rev,
                         equity=prev["equity"] + ni + A("sbc"), shares=prev["shares"] * (1 + A("share_creep"))))
    return rows

def required_revenue(sc_rows, year, rd, sga, cogs_pct):
    """Revenue needed for FCF = 0 in `year`, given R&D and SG&A, using the Base-case prior-year revenue and opening cash."""
    prev = next(r for r in sc_rows if r["year"] == year - 1)
    int_inc = A("cash_yield") * prev["cash"]
    int_exp = O("term_loan") * O("term_loan_rate") + A("interest_fees")
    k = 1 - cogs_pct - A("wc_drag")
    rhs = rd + sga - int_inc + int_exp - A("other_nonop") + A("tax") - A("da") - A("sbc") + A("capex") - A("wc_drag") * prev["revenue"]
    return rhs / k

# =============================================================================
# 5. OUTPUT
# =============================================================================
def f0(x): return f"{x:,.0f}"
def table(headers, rows):
    s = "| " + " | ".join(headers) + " |\n|" + "|".join(["---"] + ["---:"] * (len(headers) - 1)) + "|\n"
    for r in rows: s += "| " + " | ".join(str(c) for c in r) + " |\n"
    return s

def first_year(rows, key):
    return next((r["year"] for r in rows if r[key] > 0), None)

def main():
    res = {n: project(sc) for n, sc in SCENARIOS.items()}
    L = ["# Moderna (MRNA) — toy projection of income, free cash flow and balance sheet, FY2026E-FY2030E\n"]
    L.append("*A toy, not a forecast and not a recommendation. FY2026 is from management's guidance and the Q3 10-Q; FY2027-30 are labelled assumptions in three scenarios. $ millions. Built 23 Nov 2026 from the Q3 2026 10-Q and the repo's Q3 delta note; the 2028 cash break-even target and the oncology timeline are from the repo's 23 Nov note and are not verified against the call.*\n")
    base = res["Base"]; bear = res["Bear"]; bull = res["Bull"]
    L.append("## Punchline\n")
    L.append(f"- **FY2026E** (guidance midpoint): revenue {f0(base[0]['revenue'])}, operating loss {f0(base[0]['oi'])}, net loss {f0(base[0]['ni'])}, free cash flow about {f0(base[0]['fcf'])}, year-end cash and investments {f0(base[0]['cash'])}.")
    for n in ("Bear", "Base", "Bull"):
        r = res[n]
        L.append(f"- **{n}:** operating break-even {first_year(r, 'oi') or 'not by 2030'}; free cash flow positive {first_year(r, 'fcf') or 'not by 2030'}; cumulative free cash flow 2027-30 {f0(sum(x['fcf'] for x in r[1:]))}; year-end 2030 cash and investments {f0(r[-1]['cash'])}, lowest year-end {f0(min(x['cash'] for x in r))}.")
    rr = {(rd, y): required_revenue(base, y, rd, base[y - 2026]['sga'], 0.36) for rd in (2400, 2000, 1600) for y in (2028, 2029)}
    L.append(f"- **Management's target is cash break-even in 2028.** None of the three scenarios reaches it. For free cash flow to be zero in 2028 on Base assumptions, revenue would need to be about {rr[(2400,2028)]/1000:.1f}bn with R&D at $2.4bn, {rr[(2000,2028)]/1000:.1f}bn at $2.0bn, or {rr[(1600,2028)]/1000:.1f}bn at $1.6bn (against about {base[0]['revenue']/1000:.1f}bn in 2026). The target therefore needs a big revenue step-up, deep cost cuts, or both.")
    L.append(f"- **Funding:** in Base cash ends 2030 at {f0(base[-1]['cash'])} and in Bull at {f0(bull[-1]['cash'])}. In **Bear** it falls to {f0(bear[-1]['cash'])} at end-2030 after repaying the $600m term loan (cash was {f0(bear[-2]['cash'])} a year earlier), close to the $500m minimum-cash covenant, which only applies if its market cap is below $5bn. The model adds no new financing, so Bear would in practice need to raise money, draw the delayed-draw loans or cut costs before then. The $3.0bn convertible falls due in Mar 2032, beyond the horizon.\n")
    for n in ("Bear", "Base", "Bull"):
        r = res[n]; sc = SCENARIOS[n]
        L.append(f"## {n} case\n\n*{sc['why']}*\n")
        hdr = ["$m"] + [f"FY{y}{'E' if y else ''}" for y in YEARS]
        lines = [("Vaccine and respiratory revenue", "vax"), ("Oncology revenue (Moderna's share)", "onc"), ("Total revenue", "revenue"),
                 ("Cost of sales", "cogs"), ("R&D", "rd"), ("SG&A", "sga"), ("Operating income", "oi"), ("Interest income", "int_inc"),
                 ("Interest expense", "int_exp"), ("Net income", "ni"), ("Free cash flow (after capex)", "fcf"), ("Financing (FY26 convert and loan flows; 2030 loan repayment)", "financing"),
                 ("Cash and investments (year-end)", "cash"), ("Term loan", "term_loan"), ("Convertible notes", "converts"), ("Lease liabilities", "leases"),
                 ("Receivables", "ar"), ("Inventory", "inv"), ("Stockholders' equity", "equity")]
        rows = [[lab] + [f0(x[k]) for x in r] for lab, k in lines]
        rows.append(["Net cash (cash less loan, converts and leases)"] + [f0(x["cash"] - x["term_loan"] - x["converts"] - x["leases"]) for x in r])
        rows.append(["Operating margin"] + [f"{x['oi']/x['revenue']*100:.0f}%" for x in r])
        rows.append(["Shares (m, basic, creeping)"] + [f"{x['shares']:.0f}" for x in r])
        rows.append(["Net income per share ($)"] + [f"{x['ni']/x['shares']:.2f}" for x in r])
        L.append(table(hdr, rows))
    L.append("## What would have to be true for 2028 cash break-even (Base cost structure)\n")
    rows = []
    for rd in (2400, 2000, 1600):
        rows.append([f"R&D ${rd/1000:.1f}bn", f"{rr[(rd,2028)]/1000:.1f}bn", f"{rr[(rd,2028)]/base[0]['revenue']:.1f}x", f"{rr[(rd,2029)]/1000:.1f}bn"])
    L.append(table(["2028 R&D (SG&A about $1.0bn)", "Revenue needed in 2028", "Multiple of FY2026E", "Revenue needed in 2029 (R&D unchanged)"], rows))
    L.append("*Arithmetic from the model's cash bridge (gross margin 64%, working capital 15% of extra revenue, interest income on the Base-case cash). It shows the size of the gap, not a forecast.*\n")
    mc = O("price") * O("shares_cover")
    L.append("## Market context (not a valuation)\n")
    L.append(table(["", "Bear", "Base", "Bull"], [
        ["Market cap at $210.72 (404.6m shares), $bn", f"{mc/1000:.0f}", f"{mc/1000:.0f}", f"{mc/1000:.0f}"],
        ["Market cap / FY2028E revenue", *[f"{mc/res[n][2]['revenue']:.0f}x" for n in ('Bear', 'Base', 'Bull')]],
        ["Market cap / FY2030E revenue", *[f"{mc/res[n][4]['revenue']:.0f}x" for n in ('Bear', 'Base', 'Bull')]],
        ["FY2030E operating margin", *[f"{res[n][4]['oi']/res[n][4]['revenue']*100:.0f}%" for n in ('Bear', 'Base', 'Bull')]],
    ]))
    L.append("## Inputs\n\n### OFFICIAL\n")
    L.append(table(["Key", "Value", "Source"], [(k, str(v[0]), v[1]) for k, v in OFFICIAL.items()]).replace("---:", "---"))
    L.append("### ASSUMPTIONS\n")
    L.append(table(["Key", "Value", "Source"], [(k, str(v[0]), v[1]) for k, v in ASSUMPTIONS.items()]).replace("---:", "---"))
    L.append("### SCENARIOS (2027, 2028, 2029, 2030)\n")
    L.append(table(["Scenario", "Vaccine growth", "Oncology revenue $m", "R&D $m", "Vaccine cost of sales %"],
                   [(n, str(s["vax_growth"]), str(s["onc_revenue"]), str(s["rd"]), f"{s['vax_cogs']*100:.0f}%") for n, s in SCENARIOS.items()]).replace("---:", "---"))
    L.append(f"*Oncology cost of sales is {ONC_COGS*100:.0f}% of oncology revenue in every scenario. All scenario numbers are ASSUMPTIONS for illustration; oncology revenue in particular is not guided.*\n")
    L.append("## What would change the answer\n")
    for s in ["**Oncology timing and economics:** BLA filing by end-2026, approval date, label, Moderna's share of revenue and profit with Merck, and survival data.",
              "**Respiratory revenue:** COVID decline, RSV, a full flu season, US approval of the flu and COVID combination.",
              "**Cost cuts:** how much of the R&D reduction is sustained against the cancer trials and platform spending.",
              "**Receivables and Q4 cash:** the $1.2bn build in Q3 and its collection; the FY2026 cash guide is the anchor for the whole bridge.",
              "**Financing:** the $0.9bn of undrawn delayed-draw loans, a refinancing of the 2030 term loan, and what happens to the $3.0bn convertible with the stock at about its $210 conversion price.",
              "**Tax and interest:** loss carryforwards and the yield on a large cash pile."]:
        L.append("- " + s)
    L.append("")
    open(os.path.join(HERE, "output.md"), "w").write("\n".join(L))
    # chart
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2)); colors = {"Bear": "#c0392b", "Base": "#1f5fbf", "Bull": "#2f8f5b"}
    for n, r in res.items():
        ax[0].plot(YEARS, [x["cash"] / 1000 for x in r], marker="o", color=colors[n], label=n)
        ax[1].plot(YEARS, [x["fcf"] / 1000 for x in r], marker="o", color=colors[n], label=n)
    ax[0].set_title("Cash and investments, year-end ($bn)"); ax[1].set_title("Free cash flow after capex ($bn)")
    ax[1].axhline(0, color="k", lw=0.8); ax[0].legend(); fig.tight_layout(); fig.savefig(os.path.join(HERE, "cash_and_fcf.png"), dpi=130); plt.close(fig)
    for n, r in res.items():
        print(n, " ".join(f"{x['year']}: rev {x['revenue']:.0f} oi {x['oi']:.0f} ni {x['ni']:.0f} fcf {x['fcf']:.0f} cash {x['cash']:.0f}" for x in r))

if __name__ == "__main__":
    main()
