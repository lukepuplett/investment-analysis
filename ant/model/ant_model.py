"""
Anthropic ($ANT) analyst-style model built from the S-1/A No.1 (filed 2 Nov 2026).
Units: $ millions and millions of shares unless stated. Page refs = S-1/A page numbers.
Every input lives in ASSUMPTIONS / FILING below; each item carries its source or 'ASSUMPTION'.
Run:  python3 ant_model.py   -> writes output.md and PNG charts in this folder.
"""
import os, math, copy
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# 1. INPUTS — FILING DATA (S-1/A) and ASSUMPTIONS. (value, source)
# =============================================================================
FILING = {
    # --- basic shares outstanding, 30 Sep 2026 (post 10-for-1 split) ---
    "class_a_outstanding":   (2168.788, "F-7 balance sheet: 2,168,788k Class A issued & outstanding"),
    "class_n_outstanding":   (30.643,   "F-7 balance sheet: 30,643k Class N issued & outstanding"),
    # --- preferred, shares outstanding (thousands->millions) and conversion ratio, F-47 ---
    # (series, shares_m, ratio, holder_group). Ratios: 10:1 except D-1 10.6, D-2 10.4, D-3 10.6 (F-47/48).
    "preferred": ([
        ("A",   48.574, 10.0, "voting"),  ("B",   87.430, 10.0, "nonvoting_other"),
        ("C-1", 26.397, 10.0, "voting"),  ("C-2", 13.362, 10.0, "nonvoting_other"),
        ("D-1", 35.013, 10.6, "voting"),  ("D-2",  4.444, 10.4, "voting"),
        ("D-3",  4.999, 10.6, "nonvoting_other"),
        ("E-1", 63.610, 10.0, "voting"),  ("E-2", 95.282, 10.0, "amazon"),
        ("E-3", 12.664, 10.0, "google"),  ("E-4", 15.343, 10.0, "google"),
        ("E-5", 24.244, 10.0, "google"),
        ("F-1", 92.220, 10.0, "voting"),  ("F-2", 20.740, 10.0, "amazon"),
        ("G-1", 90.510, 10.0, "voting"),
        ("G-2/Google", 38.6, 10.0, "google"), ("G-2/Amazon", 19.3, 10.0, "amazon"),
        ("G-2/undisclosed", 83.929 - 38.6 - 19.3, 10.0, "nonvoting_other"),
        ("G-3", 20.563, 10.0, "amazon"),  ("G-4",  3.322, 10.0, "google"),
        ("H-1", 77.638, 10.0, "voting"),
        ("H-2/Google", 10000 / 589.0095, 10.0, "google"),
        ("H-2/Amazon",  5000 / 589.0095, 10.0, "amazon"),
        ("H-2/undisclosed", 33.110 - 10000/589.0095 - 5000/589.0095, 10.0, "nonvoting_other"),
    ], "F-47 preferred table; attribution: E-2/F-2/G-3 = Amazon note conversions (F-41/42), "
       "E-3/E-4/E-5/G-4 = Google note conversions (F-40/41), G-2 38.6m Google + 19.3m Amazon (F-32), "
       "Series H: Google $10.0bn, Amazon $5.0bn (F-41/42). Other series' holders NOT disclosed."),
    "preferred_asconverted_check": (8558.869, "F-59 anti-dilutive table: 8,558,869k as-converted"),
    "series_h_price_pref":   (589.0095, "F-47: Series H-1/H-2 at $589.0095 per preferred share"),
    "pref_conversion_ratio": (10.0,     "F-47/48: conversion ratio 10:1 (except D series)"),
    # --- Amazon rollover notes outstanding (p.168) ---
    "amazon_2023_principal": (2186.0, "p.168 table"), "amazon_2023_conv": (2.0928, "p.168: lower of $2.0928 and IPO price"),
    "amazon_2024_principal": (4017.0, "p.168 table"), "amazon_2024_conv": (5.0478, "p.168: lower of $5.0478 and IPO price"),
    "amazon_note_shares_check": (1840.445, "p.168: 1,840,444,962 Class N issuable (ignoring cap)"),
    "amazon_cap": (0.12,  "p.168: Amazon cap 12% of capitalization (as-converted incl. awards), waivable"),
    "google_cap": (0.1499,"p.172: Google cap 14.99% post-money as-converted"),
    # --- equity awards ---
    "options_outstanding":   (1774.343, "p.21 / F-52: 1,774,342,693 options"),
    "options_waep":          (2.91,     "p.21: weighted-average exercise price $2.91"),
    "rsus_outstanding":      (1127.994, "F-53: 1,127,994k RSUs (all double-trigger, settle on IPO / vesting)"),
    "rsas_unvested":         (13.736,   "F-59: RSAs 13,736k (already issued & outstanding -> not added)"),
    "donation_match_shares": (27.992,   "F-59: donation matching program liability 27,992k shares"),
    "holdback_shares":       (1.590,    "F-59: acquisition holdback liability 1,590k shares"),
    "post_q3_acq_class_n":   (0.849,    "p.21: 848,882 Class N issued after 30 Sep for acquisitions (Class A count left blank)"),
    "public_benefit_fund":   (846.84096,"p.146: 846,840,960 Class N to Anthropic Public Benefit Fund (=5% of FD at 30 Jun 26)"),
    "safes":    (0.0, "F-32: 'All SAFEs have been converted as of December 31, 2024'"),
    "warrants_issued_by_ant": (0.0, "No ANT-issued warrants found; F-31 warrant rights are an ASSET (warrants in a private co.)"),
    # --- undrawn financing facilities (p.168-172, p.167) settled in Class N stock ---
    "google_npa":   (20000.0, "p.169: Google 2026 NPA $20.0bn available (shares at 30-day VWAP post-IPO)"),
    "amazon_npa":   (15000.0, "p.169: Amazon 2026 NPA $15.0bn (shares at 30-day VWAP, in $5bn milestones)"),
    "broadcom_npa": (42000.0, "p.169/171: Infrastructure Partner 2026 NPA $42.0bn notes"),
    "broadcom_conv_normal":  (0.90, "p.171: converts at 90% of 30-day VWAP"),
    "broadcom_conv_penalty": (0.85, "p.171 fn4: 85% if revenue conditions not met"),
    "broadcom_rate_normal":  (0.09, "p.171: 9.00% PIK"),
    "broadcom_rate_penalty": (0.13, "p.171 fn4: 13.00% PIK"),
    "amd_put":      (5000.0,  "p.167-168: AMD commits to buy up to $5.0bn Class N at 30-day VWAP"),
    "google_ipo_pp_option": (10000.0, "p.172: Google option to buy up to $10bn at IPO price; REDUCES Google NPA 1:1 (no extra shares)"),
    # --- financials ---
    "q_revenue": ({"1Q25":376,"2Q25":787,"3Q25":1382,"4Q25":2040,"1Q26":4731,"2Q26":11555,"3Q26":16956}, "p.161 quarterly table"),
    "q_compute": ({"1Q25":944,"2Q25":1390,"3Q25":2047,"4Q25":2945,"1Q26":3387,"2Q26":5558,"3Q26":9863}, "p.161"),
    "fy_revenue": ({2023:41, 2024:386, 2025:4585}, "p.24"),
    "rev_9m26": (33242.0, "p.24"), "compute_9m26": (18808.0, "p.24"),
    "cor_9m26": (4812.0, "F-40 functional table: cost of revenue (substantially all serving compute)"),
    "rnd_9m26": (19240.0, "F-40"), "sm_func_9m26": (6619.0, "F-40"), "ga_func_9m26": (3831.0, "F-40"),
    "personnel_9m26": (4863.0, "p.24 (incl. SBC)"), "smp_9m26": (5529.0, "p.24 sales, marketing & partnerships"),
    "other_opadmin_9m26": (5302.0, "p.24 (incl. donation match)"),
    "sbc_9m26": (3255.0, "p.159"), "donation_9m26": (2086.0, "p.159 non-cash charitable contributions"),
    "op_loss_9m26": (-1260.0, "p.24"), "interest_income_9m26": (2359.0, "p.24"),
    "cash_sti_sep26": (131845.0, "p.26: cash, equivalents & short-term investments"),
    "rsu_cum_sbc_at_ipo": (8200.0, "F-53: $8.2bn cumulative RSU SBC would be recognised when performance condition met (IPO)"),
    "rsu_unrec_sbc": (24100.0, "F-53: $24.1bn unrecognised RSU cost, ~2.0 yrs"),
    "option_unrec_sbc": (1800.0, "F-52: $1.8bn unrecognised option cost, ~1.2 yrs"),
    "capex_9m26": (925.0 + 1955.0, "F-13: PP&E $925m + prepayments for leased assets $1,955m"),
    "commit_total": (895400.0, "p.140: aggregate committed spend ~$895.4bn"),
    "commit_to_2030": (447500.0, "p.140: ~$447.5bn before 31 Dec 2030"),
    "commit_next12m": (69800.0, "p.140: ~$69.8bn in 12 months after 30 Sep 2026"),
    "contract_table": ({2026:5231, 2027:29165, 2028:44357, 2029:47752, 2030:45070}, "p.174 contractual obligations table (subset of the $447.5bn)"),
    "founders_record_shares": (237.81308+238.31954+241.34814+239.44694+239.52627+240.55895+240.05752,
                               "p.295 footnotes: Class A held of record by the 7 co-founders"),
}

ASSUMPTIONS = {
    "ipo_primary_raise":   (25000.0, "ASSUMPTION: gross primary raise (S-1/A leaves size blank)"),
    "ipo_fee":             (0.03,    "ASSUMPTION: underwriting + expenses"),
    "rsu_net_withholding": (0.0,     "ASSUMPTION: RSUs counted gross (S-1/A says net settlement; rate left blank)"),
    "facility_price_mode": ("ipo",   "Per brief: facility shares issued at the IPO price (filing: 30-day VWAP at draw)"),
    "market_caps":         ([1.0e6, 1.5e6, 2.0e6], "Brief: $1.0tn/$1.5tn/$2.0tn"),
    "headline_cap":        (1.5e6,   "Brief: $1.5tn"),
    # --- operating model (2026E-2030E) ---
    # quarterly QoQ revenue growth for 4Q26 = g0, decays by d each quarter, floored at f
    "scenarios": ({
        "Bear":  dict(g0=0.10, d=0.75, f=0.015),
        "Base":  dict(g0=0.22, d=0.85, f=0.025),
        "Bull":  dict(g0=0.30, d=0.88, f=0.035),
    }, "ASSUMPTION: decelerating QoQ paths anchored on 3Q26 $16,956m (actual QoQ: +132%, +144%, +47%)"),
    "thread_path": ({2027: 2.45, 2028: 1.69, 2029: 1.30, 2030: 1.20},
                    "@TechFundies thread: revenue +145% (2027), +69% (2028); 2029/30 = ASSUMPTION"),
    "thread_4q26_from": ("Base", "ASSUMPTION: thread scenario uses Base 4Q26"),
    # cost lines as % of revenue: start = 9M26 actual, linear glide to 2030 target
    "cost_targets_2030": ({
        #           COR   train  pers  S&M   G&A   SBCnew don
        "Bear":   dict(cor=0.20, train=0.40, pers=0.050, sm=0.16, ga=0.08, sbc=0.05, don=0.02),
        "Base":   dict(cor=0.17, train=0.30, pers=0.045, sm=0.13, ga=0.06, sbc=0.04, don=0.015),
        "Bull":   dict(cor=0.14, train=0.22, pers=0.040, sm=0.11, ga=0.05, sbc=0.03, don=0.01),
        "Thread": dict(cor=0.17, train=0.30, pers=0.045, sm=0.13, ga=0.06, sbc=0.04, don=0.015),
    }, "ASSUMPTION"),
    # yearly compute+infra cash floor from commitments ($m). Sums to $447.5bn incl 4Q26 (p.140).
    "commit_schedule": ({2026: 14000, 2027: 74000, 2028: 106000, 2029: 120000, 2030: 133500},
                        "ASSUMPTION allocation of p.140 $447.5bn to 2030 (4Q26+0.75x2027 ~= $69.8bn next-12m)"),
    "commit_passthrough": ({"Bear": 1 - 213.8/895.4, "Base": 1.0, "Thread": 1.0, "Bull": 1.0},
                           "ASSUMPTION: share of committed spend expensed in-year. Bear walks away from the $213.8bn "
                           "contingent/terminable portion (p.174) -> 76%; others 100%"),
    "broadcom_draws": ({
        "Bear":   dict(amount=42000, rate="penalty"),
        "Base":   dict(amount=21000, rate="normal"),
        "Bull":   dict(amount=0,     rate="normal"),
        "Thread": dict(amount=21000, rate="normal"),
    }, "ASSUMPTION: drawn evenly 2027-2030 to fund lease rent"),
    "facility_draw_years": ([2027, 2028, 2029, 2030], "ASSUMPTION: Google/Amazon/AMD drawn evenly 2027-2030"),
    "cash_yield": (0.035, "ASSUMPTION (9M26 interest income $2.36bn on rising balance)"),
    "tax_rate":   (0.21,  "ASSUMPTION"),
    "nol_start":  (15000.0,"ASSUMPTION: usable NOLs ~ cumulative cash operating losses (not disclosed)"),
    "capex_pct":  (0.05,  "ASSUMPTION: capex outside commitments, % revenue (9M26 actual ~8.7% incl. lease prepayments)"),
    "fv_changes_post_ipo": (0.0, "ASSUMPTION: fair-value marks on notes/NPAs not forecast (they were -$104.6bn in 9M26)"),
    # --- valuation ---
    "exit_pe":       (25.0, "Brief: 25x 2030 P/E exit"),
    "discount_rate": (0.12, "Brief: 12%"),
    "hold_years":    (4.0,  "ASSUMPTION: buy at IPO ~end-2026, exit end-2030"),
    "sens_compute":  ([0.40, 0.50, 0.60, 0.70, 0.80], "Sensitivity grid: total compute % of revenue in 2028"),
}

V = lambda d, k: d[k][0]
F = {k: v[0] for k, v in FILING.items()}
A = {k: v[0] for k, v in ASSUMPTIONS.items()}

# =============================================================================
# 2. SHARE BRIDGE
# =============================================================================
def pref_rows():
    return [(s, sh, r, g, sh * r) for s, sh, r, g in F["preferred"]]

def amazon_note_shares(price):
    p23 = min(F["amazon_2023_conv"], price); p24 = min(F["amazon_2024_conv"], price)
    return F["amazon_2023_principal"] / p23 + F["amazon_2024_principal"] / p24

def tsm_options(price):
    n, k = F["options_outstanding"], F["options_waep"]
    return max(0.0, n * (1 - k / price)) if price > k else 0.0

def bridge(price, include_ipo=True, broadcom_case="normal"):
    """Returns ordered list of (label, shares_m, source) and totals at a given price."""
    pref = sum(r[4] for r in pref_rows())
    rsu = F["rsus_outstanding"] * (1 - A["rsu_net_withholding"])
    items = [
        ("Basic: Class A + Class N", F["class_a_outstanding"] + F["class_n_outstanding"], "F-7"),
        ("Preferred -> common (10:1; D-series 10.4-10.6)", pref, "F-47"),
        ("Amazon rollover notes ($6.2bn @ $2.09/$5.05)", amazon_note_shares(price), "p.168"),
        ("Options (treasury stock method)", tsm_options(price), "F-52 / p.21"),
        ("RSUs (1,128m, counted gross)", rsu, "F-53"),
        ("Public Benefit Fund (Class N)", F["public_benefit_fund"], "p.146"),
        ("Donation match + holdback + post-Q3 acq.", F["donation_match_shares"] + F["holdback_shares"] + F["post_q3_acq_class_n"], "F-59 / p.21"),
        ("SAFEs / ANT warrants", F["safes"] + F["warrants_issued_by_ant"], "F-32 / F-31"),
    ]
    fd_pre = sum(x[1] for x in items)
    ipo = (A["ipo_primary_raise"] / price) if include_ipo else 0.0
    conv_b = F["broadcom_conv_penalty"] if broadcom_case == "penalty" else F["broadcom_conv_normal"]
    fac = [
        ("IPO primary (ASSUMPTION $25bn)", ipo, "ASSUMPTION"),
        ("Google 2026 NPA $20bn", F["google_npa"] / price, "p.169"),
        ("Amazon 2026 NPA $15bn", F["amazon_npa"] / price, "p.169"),
        (f"Broadcom NPA $42bn @ {int(conv_b*100)}% of price (principal only)", F["broadcom_npa"] / (conv_b * price), "p.171"),
        ("AMD put $5bn", F["amd_put"] / price, "p.167"),
    ]
    return items, fac

def totals(price, broadcom_case="normal"):
    items, fac = bridge(price, broadcom_case=broadcom_case)
    basic = items[0][1]
    fd_pre = sum(x[1] for x in items)
    fd_ipo = fd_pre + fac[0][1]
    post = fd_ipo + sum(x[1] for x in fac[1:])
    return dict(basic=basic, fd_pre=fd_pre, fd_ipo=fd_ipo, post=post)

def solve_price(mcap, basis, broadcom_case="normal"):
    """Fixed point: price = mcap / shares(price). basis in basic|fd_ipo|post."""
    p = 60.0
    for _ in range(200):
        s = totals(p, broadcom_case)[basis]
        p_new = mcap / s
        if abs(p_new - p) < 1e-9: break
        p = p_new
    return p, totals(p, broadcom_case)[basis]

def ownership(price, broadcom_case="normal"):
    items, fac = bridge(price, broadcom_case=broadcom_case)
    groups = {}
    for s, sh, r, g, conv in pref_rows():
        groups[g] = groups.get(g, 0) + conv
    founders = F["founders_record_shares"]
    other_common = F["class_a_outstanding"] + F["class_n_outstanding"] - founders
    t = totals(price, broadcom_case)
    am_notes = amazon_note_shares(price)
    rows_today = {
        "Co-founders (7, Class A of record)": founders,
        "Other common holders (employees, ex-employees, others)": other_common,
        "Employee options (TSM) + RSUs": tsm_options(price) + F["rsus_outstanding"],
        "Voting preferred holders (A,C-1,D-1,D-2,E-1,F-1,G-1,H-1) - venture/financial proxy": groups["voting"],
        "Amazon (identified preferred + rollover notes)": groups["amazon"] + am_notes,
        "Google (identified preferred)": groups["google"],
        "Non-voting preferred, holder not disclosed (B, C-2, D-3, part G-2/H-2)": groups["nonvoting_other"],
        "Public Benefit Fund": F["public_benefit_fund"],
        "Other (donation match, holdback, acq.)": F["donation_match_shares"] + F["holdback_shares"] + F["post_q3_acq_class_n"],
        "IPO investors (ASSUMPTION $25bn)": fac[0][1],
    }
    post = dict(rows_today)
    post["Amazon (identified preferred + rollover notes)"] += fac[2][1]
    post["Google (identified preferred)"] += fac[1][1]
    post["Broadcom / assignee (notes)"] = fac[3][1]
    post["AMD (put)"] = fac[4][1]
    return rows_today, post, t

# =============================================================================
# 3. OPERATING MODEL
# =============================================================================
YEARS = [2026, 2027, 2028, 2029, 2030]

def revenue_path(name):
    q = F["q_revenue"]
    last = q["3Q26"]
    if name == "Thread":
        base = revenue_path(A["thread_4q26_from"])
        out = {2026: base["annual"][2026]}
        for y in [2027, 2028, 2029, 2030]:
            out[y] = out[y-1] * A["thread_path"][y]
        return dict(annual=out, quarterly=None, q4=base["quarterly"][0])
    sc = A["scenarios"][name]
    qs = []; r = last
    for t in range(17):  # 4Q26 .. 4Q30
        g = max(sc["f"], sc["g0"] * sc["d"] ** t)
        r = r * (1 + g); qs.append(r)
    ann = {2026: F["rev_9m26"] + qs[0]}
    for i, y in enumerate([2027, 2028, 2029, 2030]):
        ann[y] = sum(qs[1 + 4*i: 5 + 4*i])
    return dict(annual=ann, quarterly=qs, q4=qs[0])

def lin(start, end, i, n=4):  # i: 0 for 2026 ... 4 for 2030
    return start + (end - start) * i / n

def op_model(name, price_post, shares_post, shares_fd, compute_override_2028=None):
    rv = revenue_path(name)["annual"]
    T = A["cost_targets_2030"][name]
    r9 = F["rev_9m26"]
    start = dict(cor=F["cor_9m26"]/r9, train=(F["compute_9m26"]-F["cor_9m26"])/r9,
                 pers=(F["personnel_9m26"]-F["sbc_9m26"])/r9, sm=F["smp_9m26"]/r9,
                 ga=(F["other_opadmin_9m26"]-F["donation_9m26"])/r9,
                 sbc=F["sbc_9m26"]/r9, don=F["donation_9m26"]/r9)
    bd = A["broadcom_draws"][name]
    rate = F["broadcom_rate_penalty"] if bd["rate"] == "penalty" else F["broadcom_rate_normal"]
    draw_years = A["facility_draw_years"]
    cash = F["cash_sti_sep26"]; nol = A["nol_start"]; bnotes = 0.0
    rows = []
    for i, y in enumerate(YEARS):
        R = rv[y]
        # 2026: actual 9M + modelled 4Q at 9M ratios (start); later years glide
        pct = {k: lin(start[k], T[k], i) for k in start}
        compute_pct_model = pct["cor"] + pct["train"]
        if compute_override_2028 is not None and y == 2028:
            compute = compute_override_2028 * R; floor_binds = False
        else:
            compute_model = compute_pct_model * R
            if y == 2026:  # 9M actual + 4Q
                q4 = R - r9
                compute_model = F["compute_9m26"] + compute_pct_model * q4
                floor = F["compute_9m26"] + A["commit_schedule"][2026] * A["commit_passthrough"][name]
            else:
                floor = A["commit_schedule"][y] * A["commit_passthrough"][name]
            compute = max(compute_model, floor); floor_binds = floor > compute_model
        cor = min(compute, pct["cor"] * R); train = compute - cor
        pers = pct["pers"] * R; sm = pct["sm"] * R; ga = pct["ga"] * R; don = pct["don"] * R
        # SBC: new grants % rev + unrecognised schedule + one-off RSU catch-up at IPO
        sbc = pct["sbc"] * R
        if y == 2026:
            sbc = F["sbc_9m26"] + start["sbc"] * (R - r9) + F["rsu_cum_sbc_at_ipo"]
            don = F["donation_9m26"] + start["don"] * (R - r9)
        if y in (2027, 2028):
            sbc += F["rsu_unrec_sbc"] / 2.0
        if y == 2027:
            sbc += F["option_unrec_sbc"]
        opex = compute + pers + sm + ga + sbc + don
        ebit = R - opex
        # Broadcom notes: drawn evenly over 2027-30, PIK interest (non-cash)
        draw = bd["amount"] / 4 if y in draw_years else 0.0
        b_int = (bnotes + draw / 2) * rate
        bnotes += draw + b_int
        int_inc = cash * A["cash_yield"] if y > 2026 else F["interest_income_9m26"] + cash * A["cash_yield"] / 4
        pbt = ebit + int_inc - b_int + A["fv_changes_post_ipo"]
        use = min(nol, max(0.0, pbt)); nol -= use
        tax = max(0.0, pbt - use) * A["tax_rate"]
        ni = pbt - tax
        capex = A["capex_pct"] * R
        fcf = ni + sbc + don + b_int - capex       # SBC, donation (stock) and PIK are non-cash
        equity_draws = (F["google_npa"] + F["amazon_npa"] + F["amd_put"]) / 4 if y in draw_years else 0.0
        ipo_cash = A["ipo_primary_raise"] * (1 - A["ipo_fee"]) if y == 2026 else 0.0
        cash = cash + (fcf if y > 2026 else 0.0) + draw + equity_draws + ipo_cash
        rows.append(dict(year=y, revenue=R, compute=compute, compute_pct=compute / R, floor_binds=floor_binds,
                         cor=cor, train=train, pers=pers, sm=sm, ga=ga, sbc=sbc, don=don,
                         ebit=ebit, ebit_m=ebit / R, int_inc=int_inc, b_int=b_int, tax=tax, ni=ni,
                         eps_post=ni / shares_post, eps_fd=ni / shares_fd, fcf=fcf, cash=cash,
                         adj_ebit=ebit + sbc + don))
    return rows

# =============================================================================
# 4. RUN + OUTPUTS
# =============================================================================
def md_table(headers, rows):
    s = "| " + " | ".join(headers) + " |\n|" + "|".join(["---"] * len(headers)) + "|\n"
    for r in rows: s += "| " + " | ".join(str(x) for x in r) + " |\n"
    return s

fm = lambda x: f"{x:,.0f}"
fb = lambda x: f"{x/1000:,.1f}"
fp = lambda x: f"{x*100:.1f}%"

def main():
    out = []
    out.append("# ANT model output (S-1/A No.1, 2 Nov 2026)\n\nAll $ in millions unless stated; shares in millions. "
               "Run `python3 ant_model.py`. Assumptions are listed in README.md and at the top of ant_model.py.\n")
    # ---- headline price at $1.5tn on FD incl IPO ----
    cap = A["headline_cap"]
    p_fd, s_fd = solve_price(cap, "fd_ipo")
    p_post, _s = solve_price(cap, "post")
    s_post = totals(p_fd)["post"]   # facility shares issued at the IPO price (brief)
    p_post_pen, s_post_pen = solve_price(cap, "post", "penalty")
    p_basic, s_basic = solve_price(cap, "basic")
    items, fac = bridge(p_fd)
    # preferred check
    pref_sum = sum(r[4] for r in pref_rows())
    out.append("## 1. Share bridge / dilution waterfall\n")
    out.append(f"Priced at the **$1.5tn fully-diluted IPO price of ${p_fd:,.2f}** (solved as a fixed point: price = $1.5tn / FD shares incl. IPO primary).\n")
    rows = []; cum = 0
    for lbl, sh, src in items:
        cum += sh; rows.append([lbl, fm(sh), fm(cum), src])
    rows.append(["**= Fully diluted, pre-IPO**", "", f"**{fm(cum)}**", ""])
    for lbl, sh, src in fac:
        cum += sh; rows.append([lbl, fm(sh), fm(cum), src])
        if lbl.startswith("IPO"):
            rows.append(["**= Fully diluted incl. IPO primary**", "", f"**{fm(cum)}**", ""])
    rows.append(["**= Post-facility (all committed facilities drawn)**", "", f"**{fm(cum)}**", ""])
    out.append(md_table(["Step", "Shares (m)", "Cumulative (m)", "Source"], rows))
    t = totals(p_fd); tpen = totals(p_fd, "penalty")
    out.append(f"\n- Preferred as-converted from series table: {fm(pref_sum)}m vs F-59 anti-dilutive figure {fm(F['preferred_asconverted_check'])}m (D-series ratios explain the gap vs a flat 10:1 = {fm(853.394*10)}m).")
    out.append(f"- Amazon notes check: {fm(amazon_note_shares(p_fd))}m vs filing {fm(F['amazon_note_shares_check'])}m. Fixed conversion prices ($2.09/$5.05) are far below any plausible IPO price, so the IPO price does not change this count. Most of it is likely blocked at IPO by Amazon's 12% cap (see ownership), and the remainder rolls over and converts quarterly. It is counted in full here.")
    out.append(f"- Options via TSM at ${p_fd:,.2f}: {fm(tsm_options(p_fd))}m net of {fm(F['options_outstanding'])}m gross (strike $2.91 is trivial vs price).")
    out.append(f"- **Dilution vs basic ({fm(t['basic'])}m):** FD pre-IPO {fm(t['fd_pre'])}m = **{t['fd_pre']/t['basic']:.1f}x basic (+{(t['fd_pre']/t['basic']-1)*100:,.0f}%)**; FD incl. IPO {fm(t['fd_ipo'])}m; post-facility {fm(t['post'])}m (+{(t['post']/t['fd_ipo']-1)*100:.1f}% vs FD incl. IPO); penalty Broadcom case {fm(tpen['post'])}m.")
    out.append("- Note: the large 'basic -> FD' step is mostly **preferred conversion**: venture money that is already invested and is not new dilution at IPO. The genuinely *new* dilution after IPO is the facilities (+{:.1f}%) plus ongoing SBC and Public Benefit Fund top-ups (up to 2% per +50% share-price milestone, p.146; not modelled).\n".format((t['post']/t['fd_ipo']-1)*100))

    # ---- ownership ----
    today, post, _ = ownership(p_fd)
    tot_today = sum(today.values()); tot_post = sum(post.values())
    rows = []
    for k in post:
        a = today.get(k, 0.0)
        rows.append([k, fm(a), fp(a / tot_today), fm(post[k]), fp(post[k] / tot_post)])
    rows.append(["**Total**", fm(tot_today), "100%", fm(tot_post), "100%"])
    out.append("### Ownership (economic, as-converted)\n")
    out.append(md_table(["Holder group", "FD incl. IPO (m)", "%", "Post-facility (m)", "%"], rows))
    am_id = sum(r[4] for r in pref_rows() if r[3] == "amazon")
    go_id = sum(r[4] for r in pref_rows() if r[3] == "google")
    T0 = tot_today - amazon_note_shares(p_fd)
    x_cap = max(0.0, (F["amazon_cap"] * T0 - am_id) / (1 - F["amazon_cap"]))
    out.append(f"\n- **What can and can't be derived:** Amazon and Google holdings are a *floor*: only the series the filing ties to them (note conversions, G-2 tranche, Series H amounts). The principal-stockholders table (p.294) lists only voting holders, so Amazon/Google (non-voting Class N) are not shown with %. "
               "Holders of the other non-voting series (B, C-2, D-3, the rest of G-2/H-2) are not disclosed. 'Voting preferred' is a proxy for venture/financial investors and may include strategics. **A precise venture-vs-strategic split can't be derived from the filing.**")
    out.append(f"- Amazon identified preferred = {fm(am_id)}m; with all notes converted it would hold {fp((am_id+amazon_note_shares(p_fd))/tot_today)}. The 12% cap would allow only about {fm(x_cap)}m of the {fm(amazon_note_shares(p_fd))}m note shares to convert at IPO (if Amazon holds nothing else and does not waive the cap). The rest stays as rollover notes.")
    out.append(f"- Google identified preferred = {fm(go_id)}m ({fp(go_id/tot_today)}); 14.99% cap applies to NPA draws.\n")

    # ---- prices ----
    out.append("## 2. Price per share at market cap\n")
    rows = []
    for c in A["market_caps"]:
        pb, _ = solve_price(c, "basic"); pf, _ = solve_price(c, "fd_ipo"); pp, _ = solve_price(c, "post"); ppp, _ = solve_price(c, "post", "penalty")
        rows.append([f"${c/1e6:.1f}tn", f"${pb:,.2f}", f"${pf:,.2f}", f"${pp:,.2f}", f"${ppp:,.2f}"])
    out.append(md_table(["Market cap", "Basic shares", "FD incl. IPO", "Post-facility (Broadcom 90%)", "Post-facility (Broadcom 85%)"], rows))
    sh_per_common = F["series_h_price_pref"] / F["pref_conversion_ratio"]
    sh_val_fd = sh_per_common * totals(sh_per_common)["fd_pre"]
    out.append(f"\n- **Series H:** ${F['series_h_price_pref']:.4f} per preferred share / 10:1 conversion (F-47, ratio verified) = **${sh_per_common:.2f} per common share**. At that price, FD pre-IPO shares imply roughly **${sh_val_fd/1e6:.2f}tn** (post-money ~ $1.0tn). The $1.5tn FD price of ${p_fd:,.2f} is {p_fd/sh_per_common-1:+.0%} vs Series H.")
    out.append("- Holding market cap fixed while adding facility shares understates value slightly, because those shares are issued for cash ($82bn) that stays on the balance sheet.\n")

    # ---- operating model ----
    out.append("## 3. Operating model 2026E–2030E (GAAP)\n")
    out.append(f"EPS uses post-facility diluted shares ({fm(s_post)}m: all facilities issued at the $1.5tn FD/IPO price). 2026E = 9M actual + modelled 4Q. 2026 SBC includes the one-off $8.2bn RSU catch-up at IPO.\n")
    scen = ["Bear", "Base", "Thread", "Bull"]
    results = {}
    for sname in scen:
        rows_ = op_model(sname, p_post, s_post, s_fd); results[sname] = rows_
        tbl = []
        keys = [("Revenue", "revenue", fb), ("  growth", None, None), ("Compute+infra", "compute", fb), ("  % rev", "compute_pct", fp),
                ("  commitment floor binds?", "floor_binds", lambda b: "yes" if b else "no"),
                ("  of which cost of revenue", "cor", fb), ("  of which training/other", "train", fb),
                ("Personnel (cash, R&D-ex-compute proxy)", "pers", fb), ("S&M & partnerships", "sm", fb), ("G&A / other (ex donation)", "ga", fb),
                ("SBC", "sbc", fb), ("Donation match (non-cash)", "don", fb),
                ("GAAP operating income", "ebit", fb), ("  margin", "ebit_m", fp), ("Adj. op. income (ex SBC, donation)", "adj_ebit", fb),
                ("Interest income", "int_inc", fb), ("Broadcom note PIK interest", "b_int", fb), ("Tax", "tax", fb),
                ("Net income", "ni", fb), ("EPS (post-facility, $)", "eps_post", lambda x: f"{x:.2f}"),
                ("FCF", "fcf", fb), ("Year-end cash (incl. IPO & facility draws)", "cash", fb)]
        prev = {2026: F["fy_revenue"][2025]}
        for lbl, k, f in keys:
            if k is None:
                vals = []
                for r in rows_:
                    p = prev.get(r["year"], None) if r["year"] == 2026 else rows_[r["year"]-2027]["revenue"]
                    vals.append(fp(r["revenue"] / p - 1))
                tbl.append([lbl] + vals); continue
            tbl.append([lbl] + [f(r[k]) for r in rows_])
        out.append(f"### {sname} ($bn unless %)\n")
        out.append(md_table(["Line"] + [f"{y}E" for y in YEARS], tbl) + "\n")
    out.append("Commitment check: the modelled compute line is floored at the assumed annual commitment schedule "
               f"({', '.join(f'{y}: ${v/1000:.0f}bn' for y, v in A['commit_schedule'].items())}; total $447.5bn to 2030 per p.140, allocation = ASSUMPTION). "
               "Where 'floor binds = yes', fixed commitments, not demand, set compute cost.\n")

    # ---- valuation ----
    out.append("## 4. Valuation at $1.5tn\n")
    net_cash_ipo = F["cash_sti_sep26"] + A["ipo_primary_raise"] * (1 - A["ipo_fee"])
    ev = cap - net_cash_ipo
    rows = []
    for sname in scen:
        r = {x["year"]: x for x in results[sname]}
        eps30 = r[2030]["eps_post"]
        exit_px = A["exit_pe"] * eps30
        pv = exit_px / (1 + A["discount_rate"]) ** A["hold_years"]
        irr = (exit_px / p_fd) ** (1 / A["hold_years"]) - 1 if exit_px > 0 else float("nan")
        pe = lambda y: (p_fd / r[y]["eps_post"]) if r[y]["ni"] > 0 else float("nan")
        rows.append([sname, f"{ev / r[2027]['revenue']:.1f}x", f"{ev / r[2028]['revenue']:.1f}x",
                     "n/m" if math.isnan(pe(2027)) else f"{pe(2027):.0f}x", "n/m" if math.isnan(pe(2028)) else f"{pe(2028):.0f}x",
                     f"${eps30:.2f}", f"${exit_px:,.0f}", f"${pv:,.0f}", "n/m" if math.isnan(irr) else f"{irr*100:.1f}%"])
    out.append(f"EV = $1.5tn - cash ${fb(net_cash_ipo)}bn (Sep-26 cash + net IPO proceeds) = ${fb(ev)}bn. P/E = IPO price ${p_fd:,.2f} / post-facility EPS. "
               f"IRR for an IPO buyer at the FD price ${p_fd:,.2f}, exit at {A['exit_pe']:.0f}x 2030E EPS after {A['hold_years']:.0f} yrs; PV discounted at {A['discount_rate']*100:.0f}%.\n")
    out.append(md_table(["Scenario", "EV/Sales 27E", "EV/Sales 28E", "P/E 27E", "P/E 28E", "EPS 30E", "Exit price", "PV today", "IRR"], rows))

    # ---- sensitivity ----
    out.append("\n## 5. Sensitivity: 2028E EPS ($, post-facility) vs revenue path x total compute % of revenue\n")
    hdr = ["Path (2028E rev)"] + [f"compute {int(c*100)}%" for c in A["sens_compute"]] + ["modelled"]
    rows = []
    for sname in scen:
        base_rows = results[sname]; r28 = base_rows[2]
        vals = [f"{op_model(sname, p_post, s_post, s_fd, compute_override_2028=c)[2]['eps_post']:.2f}" for c in A["sens_compute"]]
        rows.append([f"{sname} (${fb(r28['revenue'])}bn)"] + vals + [f"{r28['eps_post']:.2f} @ {fp(r28['compute_pct'])}"])
    out.append(md_table(hdr, rows))
    floor28 = A["commit_schedule"][2028]
    out.append(f"\nNote: grid cells ignore the commitment floor. The assumed 2028 floor is ${floor28/1000:.0f}bn, i.e. {floor28/results['Base'][2]['revenue']*100:.0f}% of Base and {floor28/results['Bear'][2]['revenue']*100:.0f}% of Bear 2028 revenue, so the low-compute cells are not reachable on lower revenue paths without renegotiating or cancelling commitments.\n")

    open(os.path.join(HERE, "output.md"), "w").write("\n".join(out))

    # ---- charts ----
    charts(p_fd, results)
    print("\n".join(out))

def charts(p_fd, results):
    plt.rcParams.update({"font.size": 11})
    # 1 waterfall
    items, fac = bridge(p_fd)
    steps = [(l, s) for l, s, _ in items if s > 0.5] + [(l, s) for l, s, _ in fac]
    labels = [l.split(" (")[0] for l, _ in steps]
    fig, ax = plt.subplots(figsize=(12, 6.5))
    cum = 0; xs = range(len(steps))
    for i, (l, s) in enumerate(steps):
        color = "#4C72B0" if i == 0 else ("#DD8452" if i < len([x for x in items if x[1] > 0.5]) else "#C44E52")
        ax.bar(i, s, bottom=cum, color=color, edgecolor="black")
        ax.text(i, cum + s + 150, f"{s/1000:.2f}bn", ha="center", fontsize=9)
        cum += s
    ax.bar(len(steps), cum, color="#55A868", edgecolor="black")
    ax.text(len(steps), cum + 150, f"{cum/1000:.1f}bn", ha="center", fontsize=10, fontweight="bold")
    ax.set_xticks(list(xs) + [len(steps)])
    ax.set_xticklabels(labels + ["Post-facility total"], rotation=35, ha="right", fontsize=9)
    ax.set_ylabel("Shares (millions)")
    ax.set_title(f"ANT share bridge at \\${p_fd:.2f}/sh (\\$1.5tn FD): basic -> fully diluted -> post-facility")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color="#4C72B0", label="Basic (Class A+N)"), Patch(color="#DD8452", label="Existing claims (FD)"),
                       Patch(color="#C44E52", label="IPO + future facilities"), Patch(color="#55A868", label="Total")], loc="upper left")
    ax.grid(axis="y", alpha=0.3); fig.tight_layout(); fig.savefig(os.path.join(HERE, "dilution_waterfall.png"), dpi=130); plt.close(fig)
    # 2 revenue scenarios
    fig, ax = plt.subplots(figsize=(10, 6))
    hist_years = [2024, 2025]; hist = [F["fy_revenue"][2024] / 1000, F["fy_revenue"][2025] / 1000]
    colors = {"Bear": "#C44E52", "Base": "#4C72B0", "Thread": "#8172B2", "Bull": "#55A868"}
    for s, rows in results.items():
        ys = [r["revenue"] / 1000 for r in rows]
        ax.plot([2025] + YEARS, [hist[-1]] + ys, marker="o", label=s, color=colors[s], lw=2)
        ax.annotate(f"\\${ys[-1]:.0f}bn", (2030, ys[-1]), textcoords="offset points", xytext=(6, 0), fontsize=9, color=colors[s])
    ax.plot(hist_years, hist, marker="s", color="black", lw=2, label="Actual")
    ax.axhline(F["q_revenue"]["3Q26"] * 4 / 1000, ls="--", color="grey"); ax.text(2024.05, F["q_revenue"]["3Q26"] * 4 / 1000 + 8, "3Q26 annualised \\$67.8bn", color="grey", fontsize=9)
    ax.set_ylabel("Revenue ($bn)"); ax.set_title("ANT revenue scenarios (2026E = 9M actual + modelled 4Q)")
    ax.set_xlim(2023.8, 2030.8); ax.legend(); ax.grid(alpha=0.3); fig.tight_layout()
    fig.savefig(os.path.join(HERE, "revenue_scenarios.png"), dpi=130); plt.close(fig)
    # 3 price per share
    fig, ax = plt.subplots(figsize=(10, 6))
    caps = A["market_caps"]; bases = [("basic", "Basic"), ("fd_ipo", "FD incl. IPO"), ("post", "Post-facility")]
    w = 0.26
    for j, (b, lbl) in enumerate(bases):
        vals = [solve_price(c, b)[0] for c in caps]
        bars = ax.bar(np.arange(len(caps)) + (j - 1) * w, vals, w, label=lbl)
        for bx, v in zip(bars, vals): ax.text(bx.get_x() + bx.get_width() / 2, v + 5, f"\\${v:.0f}", ha="center", fontsize=9)
    sh = F["series_h_price_pref"] / F["pref_conversion_ratio"]
    ax.axhline(sh, color="red", ls="--", label=f"Series H \\${sh:.2f} per common share")
    ax.set_xticks(range(len(caps))); ax.set_xticklabels([f"${c/1e6:.1f}tn" for c in caps])
    ax.set_ylabel("$ per share"); ax.set_title("Implied ANT price per share by share-count basis")
    ax.legend(); ax.grid(axis="y", alpha=0.3); fig.tight_layout(); fig.savefig(os.path.join(HERE, "price_per_share.png"), dpi=130); plt.close(fig)

if __name__ == "__main__":
    main()
