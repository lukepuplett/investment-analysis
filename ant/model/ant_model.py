"""
Anthropic ($ANT) analyst-style model. Base case = S-1/A No.2 (price-range amendment, filed 10 Nov 2026,
accession 0001628280-26-072484). Earlier version (9 Nov 2026) used S-1/A No.1 with an ASSUMED $25bn raise.
Units: $ millions and millions of shares unless stated.
Page refs: "A2 p.x" = S-1/A No.2 page; un-prefixed "p.x"/"F-x" = S-1/A No.1 (financial statements carried over unchanged).
Every input lives in FILING / ASSUMPTIONS below; each item carries its source or 'ASSUMPTION'.
Run:  python3 ant_model.py   -> writes output.md and PNG charts in this folder.
"""
import os, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# 1. INPUTS — FILING DATA and ASSUMPTIONS. (value, source)
# =============================================================================
FILING = {
    # --- deal terms (S-1/A No.2) ---
    "price_low": (70.0, "A2 cover: estimated IPO price between $70.00 and $78.00"),
    "price_high": (78.0, "A2 cover"),
    "price_mid": (74.0, "A2 p.20: assumed IPO price $74.00 (midpoint)"),
    "ipo_primary_shares": (801.351354, "A2 cover / p.20: 801,351,354 Class A sold by the company"),
    "ipo_secondary_shares": (23.648646, "A2 cover / p.20: 23,648,646 Class A sold by selling stockholders (7 co-founders x 3,378,378, A2 p.301)"),
    "greenshoe_shares": (123.75, "A2 cover: underwriters' option, 123,750,000 Class A from the company only"),
    "pipe_total": (26000.0, "A2 cover / p.20: $26.0bn Class N concurrent private placement at the IPO price"),
    "pipe": ({  # $m, shares at $74 per A2 p.20
        "Google LLC": (10000.0, 135.135135), "NVIDIA": (10000.0, 135.135135), "AMD": (2500.0, 33.783783),
        "Broadcom": (1000.0, 13.513513), "Micron": (1000.0, 13.513513), "Microsoft": (1000.0, 13.513513),
        "TSMC Partners": (500.0, 6.756756)}, "A2 p.20: purchasers, $ and shares at the $74 midpoint (351,351,348 total)"),
    "pipe_shares_at_mid": (351.351348, "A2 p.25 / p.348: 351,351,348 Class N at $74"),
    "insider_iois": (303.0, "A2 cover / p.22: board-affiliated IOIs up to $303m IN this offering (Hastings DAF up to $300m, Liddell trust up to $3m, A2 p.301); part of the 825m, not extra"),
    "net_proceeds_mid": (84600.0, "A2 p.21 / p.128: ~$84.6bn net (IPO primary + PIPE) at $74"),
    "net_proceeds_mid_shoe": (93700.0, "A2 p.21: ~$93.7bn with the option exercised in full"),
    "net_proceeds_per_1": (793.0, "A2 p.128: +/- $793m net proceeds per $1.00 change in price"),
    "cash_sti_proforma_adj": (212684.0, "A2 p.131 capitalization: pro forma as adjusted cash + STI at $74 (after RSU tax withholding)"),
    "conv_notes_fv_proforma": (110873.0, "A2 p.131: convertible notes payable, pro forma as adjusted (Amazon rollover notes at fair value)"),
    # --- post-deal outstanding at $74, no shoe (A2 p.21, p.25) ---
    "class_a_post": (7427.991791, "A2 p.21: 7,427,991,791 Class A after the offering + PIPE (7,551,741,791 with shoe)"),
    "class_n_post": (5658.680800, "A2 p.21: 5,658,680,800 Class N (includes 846,840,960 Public Benefit Fund shares)"),
    "class_t_e_f": (2e-6, "A2 p.21: 1 Class T, 0 Class E, 1 Class F (no economic rights)"),
    "outstanding_post": (13086.672593, "A2 p.21: 13,086,672,593 total (13,210,422,593 with shoe)"),
    "public_benefit_fund": (846.84096, "A2 p.24-25: Initial Public Benefit Issuance 846,840,960 Class N (legally outstanding)"),
    "pref_to_class_a": (4408.097245, "A2 p.23: Preferred Stock Conversion -> 4,408,097,245 Class A"),
    "pref_to_class_n": (4153.017914, "A2 p.23: -> 4,153,017,914 Class N"),
    "rsu_settlement_net": (49.754965, "A2 p.23: net RSU Settlement 49,754,965 Class A (51,578,975 withheld at 50.90%)"),
    # --- excluded from outstanding (A2 p.23-25) ---
    "options_outstanding": (1774.342693, "A2 p.23: options, WAEP $2.91"),
    "options_waep": (2.91, "A2 p.23"),
    "options_tsm_buyback_mid": (69.774828, "A2 p.25 fn1: TSM reduction at $74 (~$5.2bn exercise proceeds)"),
    "rsus_unvested": (1026.660010, "A2 p.23: RSUs whose service condition is not met by 19 Nov 2026"),
    "rsus_post_sep": (47.041287, "A2 p.23: RSUs granted after 30 Sep 2026"),
    "acq_class_a": (0.561963, "A2 p.24: Class A issued after 30 Sep for acquisitions"),
    "acq_class_n": (0.848882, "A2 p.24: Class N issued after 30 Sep for acquisitions"),
    "holdback": (1.590190, "A2 p.25: acquisition holdback shares"),
    "matching_issuance": (27.991850, "A2 p.24: Class N issued after 30 Sep to match employee donations"),
    "vested_matching_obligation": (553.441297, "A2 p.24: max matching shares on pledges over vested awards"),
    "plan_2026_reserve": (1920.580692, "A2 p.24: 2026 Equity Incentive Plan reserve (plus rolled-over 2021 Plan shares, not quantified)"),
    "espp_reserve": (128.038713, "A2 p.24: 2026 ESPP reserve"),
    "filing_fd_total_mid": (18012.993381, "A2 p.25 'Additional Adjustments' total: Class A 7,430,143,944 + Class N 7,804,580,273 + options (TSM) 1,704,567,865 + RSUs 1,073,701,297 + 2"),
    # --- Amazon notes (A2 p.172-173) ---
    "amazon_2023_principal": (2186.0, "A2 p.173 table"), "amazon_2023_conv": (2.0928, "A2 p.173"),
    "amazon_2024_principal": (4017.0, "A2 p.173 table"), "amazon_2024_conv": (5.0478, "A2 p.173"),
    "amazon_note_shares_full": (1840.444962, "A2 p.173: 1,840,444,962 Class N ignoring the cap"),
    "amazon_ipo_conv_principal": (579.3, "A2 p.23: $579.3m converts at IPO"),
    "amazon_ipo_conv_shares": (276.827518, "A2 p.23: 276,827,518 Class N = max without exceeding the cap (Amazon did NOT waive)"),
    "amazon_rollover_shares": (1563.617444, "A2 p.25 / p.121: 1,563,617,444 Class N issuable later on rollover notes"),
    "amazon_cap": (0.12, "A2 p.172: 12% of capitalization incl. equity awards and convertibles ('Note Capitalization', as of 31 Oct 26 pro forma)"),
    "notes_pct_class_n": (0.255, "A2 p.62: outstanding notes = ~25.5% of Class N, 12.6% of total common, fully converted, ignoring cap"),
    "notes_pct_total": (0.126, "A2 p.62"),
    "amazon_class_n_post": (1920.511218, "A2 p.120-121: Amazon holds 1,920,511,218 Class N after the offering"),
    "google_class_n_pre": (1654.463134, "A2 p.120: Google 1,654,463,134 Class N before the PIPE"),
    "google_class_n_post": (1789.598269, "A2 p.121: Google 1,789,598,269 Class N after the PIPE"),
    "google_cap": (0.1499, "A2 p.176: Google 2026 NPA cap 14.99% post-money as-converted"),
    # --- remaining facilities after the deal ---
    "google_npa": (10000.0, "A2 p.173 fn1: Google 2026 NPA cut from $20.0bn to $10.0bn on PIPE closing; post-IPO draws: agreed note terms or shares at 30-day VWAP (A2 p.176)"),
    "amazon_npa": (15000.0, "A2 p.174: $15.0bn, none expected pre-IPO; shares at 30-day VWAP, $5bn milestones, subject to cap"),
    "broadcom_npa": (42000.0, "A2 p.62 / p.173: Infrastructure Partner 2026 NPA $42.0bn"),
    "broadcom_conv_normal": (0.90, "A2 p.175: 90% of 30-day VWAP"), "broadcom_conv_penalty": (0.85, "A2 p.175: 85% if revenue conditions not met"),
    "broadcom_rate_normal": (0.09, "A2 p.175: 9.00% PIK"), "broadcom_rate_penalty": (0.13, "A2 p.175: 13.00% PIK"),
    "amd_remaining": (2500.0, "A2 p.172: AMD $5.0bn commitment less $2.5bn PIPE = up to $2.5bn left; first milestones 2027; 30-day VWAP"),
    # --- operating metrics ---
    "arr_oct26": (81000.0, "A2 p.203: Run-Rate Revenue ~$81bn at 31 Oct 2026, up $10bn from 30 Sep 2026"),
    "arr_sep26": (71000.0, "Derived: $81bn - $10bn (A2 p.203)"),
    "nrr": (9.0, "A2 p.12: Net Revenue Retention ~900%"),
    # --- historical (carried over from S-1/A No.1 model) ---
    "series_h_price_pref": (589.0095, "No.1 F-47: Series H at $589.0095 per preferred share"),
    "pref_conversion_ratio": (10.0, "No.1 F-47/48: 10:1"),
    "basic_sep26": (2168.788227 + 30.643060, "A2 p.25: 2,168,788,227 Class A + 30,643,060 Class N at 30 Sep 26"),
    "founders_record_shares": (237.81308+238.31954+241.34814+239.44694+239.52627+240.55895+240.05752,
                               "No.1 p.295: Class A of record, 7 co-founders (before selling 3,378,378 each)"),
    # --- financials ---
    "q_revenue": ({"1Q25":376,"2Q25":787,"3Q25":1382,"4Q25":2040,"1Q26":4731,"2Q26":11555,"3Q26":16956}, "p.161 quarterly table"),
    "q_compute": ({"1Q25":944,"2Q25":1390,"3Q25":2047,"4Q25":2945,"1Q26":3387,"2Q26":5558,"3Q26":9863}, "p.161"),
    "fy_revenue": ({2023:41, 2024:386, 2025:4585}, "p.24"),
    "rev_9m26": (33242.0, "p.24"), "compute_9m26": (18808.0, "p.24"),
    "cor_9m26": (4812.0, "F-40 functional table: cost of revenue"),
    "rnd_9m26": (19240.0, "F-40"),
    "personnel_9m26": (4863.0, "p.24 (incl. SBC)"), "smp_9m26": (5529.0, "p.24 sales, marketing & partnerships"),
    "other_opadmin_9m26": (5302.0, "p.24 (incl. donation match)"),
    "sbc_9m26": (3255.0, "p.159"), "donation_9m26": (2086.0, "p.159 non-cash charitable contributions"),
    "interest_income_9m26": (2359.0, "p.24"),
    "cash_sti_sep26": (131845.0, "A2 p.131: cash, equivalents & short-term investments, actual"),
    "rsu_cum_sbc_at_ipo": (8200.0, "F-53: $8.2bn cumulative RSU SBC recognised at IPO"),
    "rsu_unrec_sbc": (24100.0, "F-53: $24.1bn unrecognised RSU cost, ~2.0 yrs"),
    "option_unrec_sbc": (1800.0, "F-52: $1.8bn unrecognised option cost, ~1.2 yrs"),
    # commitments: UPDATED in No.2 (No.1: $895.4bn / $447.5bn / $69.8bn / $213.8bn)
    "commit_total": (900900.0, "A2 p.144 / p.178: ~$900.9bn aggregate committed spend"),
    "commit_to_2030": (451600.0, "A2 p.144: ~$451.6bn before 31 Dec 2030"),
    "commit_next12m": (70700.0, "A2 p.144 / p.179: ~$70.7bn in the 12 months after 30 Sep 2026"),
    "commit_contingent": (186200.0, "A2 p.178: ~$186.2bn subject to termination rights or contingent conditions"),
    "contract_table": ({2026:5231, 2027:29165, 2028:44357, 2029:47752, 2030:45070}, "A2 p.178 contractual obligations table (unchanged)"),
}

ASSUMPTIONS = {
    "market_caps": ([1.0e6, 1.5e6, 2.0e6], "Luke's earlier guesses: $1.0tn (~Series H) / $1.5tn / $2.0tn"),
    "rsu_tax_withholding_scales": (False, "ASSUMPTION: pro forma cash moves only with the $793m/$1 sensitivity; RSU withholding cash held at the $74 figure"),
    "scenarios": ({
        "Bear":  dict(g0=0.10, d=0.75, f=0.015),
        "Base":  dict(g0=0.22, d=0.85, f=0.025),
        "Bull":  dict(g0=0.30, d=0.88, f=0.035),
    }, "ASSUMPTION: decelerating QoQ paths anchored on 3Q26 $16,956m (actual QoQ: +132%, +144%, +47%); unchanged from 9 Nov"),
    "thread_path": ({2027: 2.45, 2028: 1.69, 2029: 1.30, 2030: 1.20},
                    "@TechFundies thread: revenue +145% (2027), +69% (2028); 2029/30 = ASSUMPTION"),
    "thread_4q26_from": ("Base", "ASSUMPTION: thread scenario uses Base 4Q26"),
    "cost_targets_2030": ({
        "Bear":   dict(cor=0.20, train=0.40, pers=0.050, sm=0.16, ga=0.08, sbc=0.05, don=0.02),
        "Base":   dict(cor=0.17, train=0.30, pers=0.045, sm=0.13, ga=0.06, sbc=0.04, don=0.015),
        "Bull":   dict(cor=0.14, train=0.22, pers=0.040, sm=0.11, ga=0.05, sbc=0.03, don=0.01),
        "Thread": dict(cor=0.17, train=0.30, pers=0.045, sm=0.13, ga=0.06, sbc=0.04, don=0.015),
    }, "ASSUMPTION"),
    # yearly compute+infra floor ($m); sums to No.2's $451.6bn incl 4Q26; 4Q26 + 0.75x2027 = $70.5bn ~ $70.7bn next-12m
    "commit_schedule": ({2026: 15000, 2027: 74000, 2028: 106000, 2029: 120000, 2030: 136600},
                        "ASSUMPTION allocation of A2 p.144 $451.6bn to 2030"),
    "commit_passthrough": ({"Bear": 1 - 186.2/900.9, "Base": 1.0, "Thread": 1.0, "Bull": 1.0},
                           "ASSUMPTION: Bear walks away from the $186.2bn contingent/terminable portion (A2 p.178) -> 79%"),
    "broadcom_draws": ({
        "Bear":   dict(amount=42000, rate="penalty"),
        "Base":   dict(amount=21000, rate="normal"),
        "Bull":   dict(amount=0,     rate="normal"),
        "Thread": dict(amount=21000, rate="normal"),
    }, "ASSUMPTION: drawn evenly 2027-2030 to fund lease rent"),
    "facility_draw_years": ([2027, 2028, 2029, 2030], "ASSUMPTION: Google/Amazon/AMD remaining facilities drawn evenly 2027-2030"),
    "facility_price_mode": ("ipo", "ASSUMPTION: facility shares issued at the IPO price (filing: 30-day VWAP at draw)"),
    "cash_yield": (0.035, "ASSUMPTION"),
    "tax_rate":   (0.21,  "ASSUMPTION"),
    "nol_start":  (15000.0,"ASSUMPTION: usable NOLs (not disclosed)"),
    "capex_pct":  (0.05,  "ASSUMPTION: capex outside commitments, % revenue"),
    "fv_changes_post_ipo": (0.0, "ASSUMPTION: fair-value marks on rollover notes/NPAs not forecast"),
    "drip_other_issuance_q": (60.0, "ASSUMPTION: non-Amazon Note Capitalization growth per quarter (m shares) from new RSU grants, donation match, PBF top-ups, facility draws to others"),
    "exit_pe":       (25.0, "25x 2030 P/E exit (unchanged from 9 Nov brief)"),
    "discount_rate": (0.12, "12% (unchanged)"),
    "hold_years":    (4.0,  "ASSUMPTION: buy at IPO ~end-2026, exit end-2030"),
    "sens_compute":  ([0.40, 0.50, 0.60, 0.70, 0.80], "Sensitivity grid: total compute % of revenue in 2028"),
}

F = {k: v[0] for k, v in FILING.items()}
A = {k: v[0] for k, v in ASSUMPTIONS.items()}

# =============================================================================
# 2. SHARE BASES (S-1/A No.2)
# =============================================================================
def pipe_shares(price):
    """PIPE is a fixed $26.0bn, so the share count moves inversely with the IPO price."""
    return F["pipe_total"] / price

def outstanding(price, shoe=False):
    """Post-deal outstanding. The filing count is at $74; only the PIPE shares are re-struck at other prices
    (RSU-settlement withholding and the Amazon cap conversion also move slightly; not modelled)."""
    s = F["outstanding_post"] - F["pipe_shares_at_mid"] + pipe_shares(price)
    return s + (F["greenshoe_shares"] if shoe else 0.0)

def tsm_options(price):
    n, k = F["options_outstanding"], F["options_waep"]
    return max(0.0, n * (1 - k / price))

def layers(price):
    """Ordered additions on top of outstanding. Returns list of (label, shares_m, source, tier)."""
    return [
        ("Options (gross; TSM nets out only ~3.9%)", F["options_outstanding"], "A2 p.23", "tight"),
        ("Unvested RSUs at 30 Sep", F["rsus_unvested"], "A2 p.23", "tight"),
        ("RSUs granted after 30 Sep", F["rsus_post_sep"], "A2 p.23", "tight"),
        ("Post-30-Sep acquisition shares (A+N)", F["acq_class_a"] + F["acq_class_n"], "A2 p.24", "tight"),
        ("Matching Issuance (donation match, issued)", F["matching_issuance"], "A2 p.24", "tight"),
        ("Vested Matching Obligation + holdback", F["vested_matching_obligation"] + F["holdback"], "A2 p.24-25", "vmo"),
        ("Amazon rollover notes (the drip)", F["amazon_rollover_shares"], "A2 p.25 / p.173", "filing"),
        ("Less: options TSM buyback", -(F["options_outstanding"] - tsm_options(price)), "A2 p.25 fn1", "filing"),
        ("Unused 2026 Plan + ESPP reserves", F["plan_2026_reserve"] + F["espp_reserve"], "A2 p.24", "overhang"),
    ]

def facilities(price, broadcom_case="normal"):
    conv_b = F["broadcom_conv_penalty"] if broadcom_case == "penalty" else F["broadcom_conv_normal"]
    return [
        ("Google 2026 NPA remaining $10bn", F["google_npa"] / price, "A2 p.173"),
        ("Amazon 2026 NPA $15bn", F["amazon_npa"] / price, "A2 p.174"),
        (f"Broadcom NPA $42bn @ {int(conv_b*100)}% (principal only)", F["broadcom_npa"] / (conv_b * price), "A2 p.175"),
        ("AMD commitment remaining $2.5bn", F["amd_remaining"] / price, "A2 p.172"),
    ]

def bases(price, broadcom_case="normal"):
    out = outstanding(price)
    L = layers(price)
    tight = out + sum(s for _, s, _, t in L if t == "tight")
    vmo = tight + sum(s for _, s, _, t in L if t == "vmo")
    filing = vmo + sum(s for _, s, _, t in L if t == "filing")
    overhang = filing + sum(s for _, s, _, t in L if t == "overhang")
    post = filing + sum(s for _, s, _ in facilities(price, broadcom_case))
    return dict(outstanding=out, tight=tight, vmo=vmo, filing=filing, overhang=overhang, post=post)

BASIS_LABEL = {"outstanding": "Outstanding after deal", "tight": "Tighter FD", "vmo": "Tighter FD + vested match",
               "filing": "Filing FD (A2 p.25)", "overhang": "Filing FD + plan reserves", "post": "Filing FD + facilities"}

def solve_price(mcap, basis, broadcom_case="normal"):
    p = 70.0
    for _ in range(300):
        p_new = mcap / bases(p, broadcom_case)[basis]
        if abs(p_new - p) < 1e-10: break
        p = p_new
    return p

def net_proceeds(price, shoe=False):
    n = F["net_proceeds_mid"] + F["net_proceeds_per_1"] * (price - F["price_mid"])
    if shoe:
        n += (F["net_proceeds_mid_shoe"] - F["net_proceeds_mid"]) * price / F["price_mid"]
    return n

def proforma_cash(price):
    return F["cash_sti_proforma_adj"] + F["net_proceeds_per_1"] * (price - F["price_mid"])

def amazon_drip(quarters=16, other_issuance_q=None):
    """Rollover-note conversion under the 12% cap. Amazon is AT the cap after the IPO conversion, so each quarter it can
    convert only 12/88 of whatever non-Amazon capitalization was added. Note Capitalization implied = Amazon / 12%."""
    g = A["drip_other_issuance_q"] if other_issuance_q is None else other_issuance_q
    left = F["amazon_rollover_shares"]; rows = []
    for q in range(1, quarters + 1):
        conv = min(left, g * F["amazon_cap"] / (1 - F["amazon_cap"]))
        left -= conv; rows.append((q, conv, left))
    return rows

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

def op_model(name, price, shares_post, shares_fd, compute_override_2028=None):
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
        equity_draws = (F["google_npa"] + F["amazon_npa"] + F["amd_remaining"]) / 4 if y in draw_years else 0.0
        ipo_cash = (proforma_cash(price) - F["cash_sti_sep26"]) if y == 2026 else 0.0  # A2 p.131: net IPO+PIPE less RSU tax withholding
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
ft = lambda x: f"${x/1e6:,.3f}tn" if x >= 1e6 else f"${x/1e3:,.0f}bn"   # x in $m

def main():
    lo, mid, hi = F["price_low"], F["price_mid"], F["price_high"]
    out = []
    out.append("# ANT model output (S-1/A No.2, 10 Nov 2026)\n\nAll $ in millions unless stated; shares in millions. "
               "Run `python3 ant_model.py`. Inputs and sources are at the top of ant_model.py; method in README.md. "
               "Base case = the filed $70.00–$78.00 range (midpoint $74.00), no greenshoe.\n")

    # ---- 1. deal ----
    out.append("## 1. The deal (S-1/A No.2)\n")
    rows = [
        ["Class A sold by Anthropic", fm(F["ipo_primary_shares"]), f"${F['ipo_primary_shares']*mid/1000:,.1f}bn gross at $74", "A2 cover"],
        ["Class A sold by 7 co-founders (3.38m each)", fm(F["ipo_secondary_shares"]), f"${F['ipo_secondary_shares']*mid/1000:,.2f}bn to founders, not the company", "A2 cover / p.301"],
        ["**Total IPO**", f"**{fm(F['ipo_primary_shares']+F['ipo_secondary_shares'])}**",
         f"${(F['ipo_primary_shares']+F['ipo_secondary_shares'])*lo/1000:,.1f}bn–${(F['ipo_primary_shares']+F['ipo_secondary_shares'])*hi/1000:,.2f}bn gross", "A2 cover"],
        ["Greenshoe (company only)", fm(F["greenshoe_shares"]), "", "A2 cover"],
    ]
    for k, (usd, sh) in F["pipe"].items():
        rows.append([f"PIPE: {k} (Class N)", f"{sh:,.1f}", f"${usd/1000:,.1f}bn", "A2 p.20"])
    rows.append(["**PIPE total (Class N, at IPO price)**", f"**{fm(F['pipe_shares_at_mid'])}**", f"**${F['pipe_total']/1000:.1f}bn**", "A2 p.20"])
    out.append(md_table(["Piece", "Shares (m) at $74", "$", "Source"], rows))
    out.append(f"\n- **Net proceeds to Anthropic** (IPO primary + PIPE, after fees): ~${F['net_proceeds_mid']/1000:.1f}bn at $74 "
               f"(${net_proceeds(lo)/1000:.1f}bn at $70, ${net_proceeds(hi)/1000:.1f}bn at $78; ±$793m per $1), or ~${F['net_proceeds_mid_shoe']/1000:.1f}bn with the shoe (A2 p.21, p.128).")
    out.append(f"- The press \"up to $64.4bn\" is 825m × $78 = ${(F['ipo_primary_shares']+F['ipo_secondary_shares'])*hi/1000:.2f}bn **gross IPO proceeds including the founders' secondary**, not net to the company. It excludes the $26bn PIPE.")
    out.append(f"- Board-affiliated IOIs of up to ${F['insider_iois']:.0f}m (Hastings DAF $300m, Liddell trust $3m) are to buy **in this offering**, so they sit inside the 825m, not on top (A2 cover, p.301).")
    out.append(f"- Pro forma as adjusted cash and short-term investments: ${F['cash_sti_proforma_adj']/1000:.1f}bn (A2 p.131), after ~$3.8bn of RSU tax withholding (51.6m shares × $74 at a 50.90% rate, A2 p.23).\n")

    # ---- 2. share bases ----
    out.append("## 2. Share count and implied value\n")
    b = bases(mid)
    rows = [["**Outstanding after IPO + PIPE**", "", f"**{fm(b['outstanding'])}**", "A2 p.21 (incl. 847m PBF, 277m Amazon note shares)"]]
    cum = b["outstanding"]
    tiers_done = {"tight": "**= Tighter fully diluted**", "vmo": "**= + vested donation-match obligation**",
                  "filing": "**= Filing's fully diluted table (A2 p.25)**", "overhang": "**= + unused plan reserves (overhang, not day-one)**"}
    L = layers(mid)
    for i, (lbl, sh, src, t) in enumerate(L):
        cum += sh; rows.append([lbl, fm(sh), fm(cum), src])
        if i == len(L) - 1 or L[i + 1][3] != t:
            rows.append([tiers_done[t], "", f"**{fm(cum)}**", ""])
    for lbl, sh, src in facilities(mid):
        cum += sh; rows.append([f"Facility: {lbl}", fm(sh), fm(cum), src])
    out.append(md_table(["Layer (at $74)", "Shares (m)", "Cumulative (m)", "Source"], rows))
    out.append(f"\nFiling check: A2 p.25 totals {fm(F['filing_fd_total_mid'])}m; model {fm(b['filing'])}m. The facility rows stack on the filing FD (excluding plan reserves) and assume issue at the IPO price; the filing says 30-day VWAP at each draw.\n")

    rows = []
    for k in ["outstanding", "tight", "vmo", "filing", "overhang", "post"]:
        vals = [bases(p)[k] * p for p in (lo, mid, hi)]
        rows.append([BASIS_LABEL[k], fm(bases(mid)[k])] + [ft(v) for v in vals] + [f"{vals[1]/F['arr_oct26']:.1f}x"])
    out.append(md_table(["Basis", "Shares at $74 (m)", "Value at $70", "Value at $74", "Value at $78", "Mid / $81bn ARR"], rows))
    fixed = F["outstanding_post"]
    out.append(f"\n- Press headline (Reuters \"up to $1.02tn\") multiplies the fixed $74 share count by the range: {ft(fixed*lo)} / {ft(fixed*mid)} / {ft(fixed*hi)}. "
               f"Re-striking the $26bn PIPE at each price moves the low and high ends by under $2bn.")
    out.append(f"- CNBC's \"$1.405tn\" at $78 = the filing's own p.25 fully diluted table ({fm(F['filing_fd_total_mid'])}m) × $78 = {ft(F['filing_fd_total_mid']*hi)}. "
               "That table includes all 1.56bn Amazon rollover note shares and the 553m vested donation-match obligation, but **not** the unused 2026 Plan/ESPP reserves.")
    out.append(f"- Tighter FD adds only shares already granted or issued: options, RSUs, acquisition and matching shares. It leaves out the rollover notes (blocked by the cap) and contingent donation matches.")
    out.append(f"- Implied Note Capitalization: Amazon's {fm(F['amazon_class_n_post'])}m / 12% ≈ {fm(F['amazon_class_n_post']/F['amazon_cap'])}m, close to the tighter FD count (derived, not stated).")
    out.append(f"- ARR multiples: $81bn at 31 Oct (A2 p.203), up $10bn from 30 Sep. 3Q26 revenue annualised is ${F['q_revenue']['3Q26']*4/1000:.1f}bn, so midpoint outstanding value is {b['outstanding']*mid/(F['q_revenue']['3Q26']*4):.1f}x that.\n")

    # ---- 3. Amazon drip ----
    out.append("## 3. Amazon notes and the 12% cap (the drip)\n")
    r23 = F["amazon_2023_principal"] - F["amazon_ipo_conv_principal"]
    rows = [
        ["2023 NPA", f"${F['amazon_2023_principal']:,.0f}m", f"${F['amazon_2023_conv']}", fm(F['amazon_2023_principal']/F['amazon_2023_conv']),
         f"${F['amazon_ipo_conv_principal']:,.1f}m / {fm(F['amazon_ipo_conv_shares'])}m", f"${r23:,.1f}m / {fm(r23/F['amazon_2023_conv'])}m", "Mar 2034"],
        ["2024 NPA", f"${F['amazon_2024_principal']:,.0f}m", f"${F['amazon_2024_conv']}", fm(F['amazon_2024_principal']/F['amazon_2024_conv']),
         "—", f"${F['amazon_2024_principal']:,.0f}m / {fm(F['amazon_2024_principal']/F['amazon_2024_conv'])}m", "Jan/May/Nov 2035"],
        ["**Total**", f"**${F['amazon_2023_principal']+F['amazon_2024_principal']:,.0f}m**", "", f"**{fm(F['amazon_note_shares_full'])}**",
         f"**${F['amazon_ipo_conv_principal']:,.1f}m / {fm(F['amazon_ipo_conv_shares'])}m**",
         f"**${r23+F['amazon_2024_principal']:,.0f}m / {fm(F['amazon_rollover_shares'])}m**", ""],
    ]
    out.append(md_table(["Notes", "Principal", "Conv. price", "Shares if uncapped (m)", "Converts at IPO", "Left as rollover notes", "Maturity"], rows))
    out.append(f"\n- Amazon **elected not to waive** the 12% cap (A2 p.62, p.172). After the IPO conversion it holds {fm(F['amazon_class_n_post'])}m Class N ({fp(F['amazon_class_n_post']/b['outstanding'])} of outstanding), and Google holds {fm(F['google_class_n_post'])}m ({fp(F['google_class_n_post']/b['outstanding'])}) after its $10bn PIPE (A2 p.120–121).")
    out.append("- The rollover notes are non-interest-bearing. They try to convert at each fiscal quarter-end at the **lowest of the fixed price, the IPO price and the 10-day VWAP**, up to the cap. Anything still unconverted is repaid in cash at maturity, or Amazon can set it off against amounts it owes Anthropic (A2 p.173–174). At any price above $5.05 the fixed prices apply.")
    out.append(f"- Fully converted with no cap, the notes would be {fp(F['notes_pct_total'])} of total common and {fp(F['notes_pct_class_n'])} of Class N after the deal (A2 p.62). At $74 they are worth ~${F['amazon_rollover_shares']*mid/1000:.0f}bn for ~${(r23+F['amazon_2024_principal'])/1000:.2f}bn of principal; the pro forma balance sheet carries them at ${F['conv_notes_fv_proforma']/1000:.1f}bn fair value (A2 p.131).")
    drip = amazon_drip()
    q_yr = [drip[i][2] for i in (3, 7, 11, 15)]
    g = A["drip_other_issuance_q"]
    out.append(f"- **Drip arithmetic (derived):** at the cap, Amazon can convert only ~12–13.6% of any new non-Amazon capitalization (12/88 if the unconverted notes sit outside the cap base, 12% if they are inside it; the filing does not say which, so the model uses 12/88). Clearing all {fm(F['amazon_rollover_shares'])}m would need ~{fm(F['amazon_rollover_shares']/(F['amazon_cap']/(1-F['amazon_cap'])))}m of new shares issued to others. "
               f"At an ASSUMED {g:.0f}m a quarter of other issuance, about {g*F['amazon_cap']/(1-F['amazon_cap']):.1f}m convert per quarter, leaving {fm(q_yr[0])}m / {fm(q_yr[1])}m / {fm(q_yr[2])}m / {fm(q_yr[3])}m after 1/2/3/4 years. "
               "Amazon's own $15bn 2026 NPA draws use the same cap headroom. In practice the notes clear faster only if Amazon sells Class N (which converts to Class A on transfer), the cap base grows faster, or Amazon waives the cap.\n")

    # ---- 4. Prices at Luke's market caps ----
    out.append("## 4. Price per share at $1.0tn / $1.5tn / $2.0tn\n")
    rows = []
    for c in A["market_caps"]:
        rows.append([f"${c/1e6:.1f}tn"] + [f"${solve_price(c, k):,.2f}" for k in ["outstanding", "tight", "filing", "post"]])
    out.append(md_table(["Market cap", "Outstanding", "Tighter FD", "Filing FD", "Filing FD + facilities"], rows))
    sh_px = F["series_h_price_pref"] / F["pref_conversion_ratio"]
    out.append(f"\n- **Series H:** ${F['series_h_price_pref']:.4f} per preferred share / 10 = **${sh_px:.2f} per common share** (S-1/A No.1 F-47). The range is {lo/sh_px-1:+.0%} to {hi/sh_px-1:+.0%} above Series H. "
               f"Series H × the 9 Nov ~16.9bn FD was ≈ $1.0tn, and Series H × today's tighter FD is {ft(sh_px*b['tight'])}.")
    out.append(f"- **Against Luke's earlier view (29 Oct: ~$1.5tn, more likely $2tn, then doubling on day one):** the top of the range is {ft(hi*bases(hi)['outstanding'])} on outstanding and {ft(hi*bases(hi)['tight'])} on tighter FD. "
               f"$1.5tn needs ${solve_price(1.5e6,'outstanding'):.0f} a share on outstanding (${solve_price(1.5e6,'tight'):.0f} on tighter FD), {solve_price(1.5e6,'outstanding')/hi-1:+.0%} above the top of the range. "
               f"$2tn needs ${solve_price(2.0e6,'outstanding'):.0f} ({solve_price(2.0e6,'outstanding')/hi-1:+.0%} vs $78). A day-one double from $74 to $148 would be {ft(148*bases(148)['outstanding'])} on outstanding, so the $2tn idea now rests on the first-day pop, not on the IPO price.\n")

    # ---- 5. operating model ----
    out.append("## 5. Operating model 2026E–2030E (GAAP)\n")
    s_post = bases(mid)["post"]; s_fd = bases(mid)["filing"]
    out.append(f"EPS uses the filing FD plus all remaining facilities issued at $74 ({fm(s_post)}m). 2026E = 9M actual + modelled 4Q, and 2026 cash includes ${(proforma_cash(mid)-F['cash_sti_sep26'])/1000:.1f}bn of net IPO + PIPE proceeds after RSU withholding (A2 p.131). 2026 SBC includes the one-off $8.2bn RSU catch-up at IPO.\n")
    arr_q = F["arr_oct26"] / 4
    out.append(f"ARR check: if revenue simply held at the 31 Oct run-rate, 4Q26 would be ~${arr_q/1000:.1f}bn ({arr_q/F['q_revenue']['3Q26']-1:+.0%} QoQ). "
               + ", ".join(f"{n} 4Q26 = ${revenue_path(n)['q4']/1000:.1f}bn" for n in ["Bear", "Base", "Bull"])
               + ". Bear now sits below a flat October run-rate. The growth paths are unchanged from 9 Nov.\n")
    scen = ["Bear", "Base", "Thread", "Bull"]
    results = {}
    for sname in scen:
        rows_ = op_model(sname, mid, s_post, s_fd); results[sname] = rows_
        tbl = []
        keys = [("Revenue", "revenue", fb), ("  growth", None, None), ("Compute+infra", "compute", fb), ("  % rev", "compute_pct", fp),
                ("  commitment floor binds?", "floor_binds", lambda x: "yes" if x else "no"),
                ("  of which cost of revenue", "cor", fb), ("  of which training/other", "train", fb),
                ("Personnel (cash, R&D-ex-compute proxy)", "pers", fb), ("S&M & partnerships", "sm", fb), ("G&A / other (ex donation)", "ga", fb),
                ("SBC", "sbc", fb), ("Donation match (non-cash)", "don", fb),
                ("GAAP operating income", "ebit", fb), ("  margin", "ebit_m", fp), ("Adj. op. income (ex SBC, donation)", "adj_ebit", fb),
                ("Interest income", "int_inc", fb), ("Broadcom note PIK interest", "b_int", fb), ("Tax", "tax", fb),
                ("Net income", "ni", fb), ("EPS (filing FD + facilities, $)", "eps_post", lambda x: f"{x:.2f}"),
                ("FCF", "fcf", fb), ("Year-end cash (incl. IPO, PIPE & facility draws)", "cash", fb)]
        for lbl, k, f in keys:
            if k is None:
                vals = []
                for r in rows_:
                    p = F["fy_revenue"][2025] if r["year"] == 2026 else rows_[r["year"]-2027]["revenue"]
                    vals.append(fp(r["revenue"] / p - 1))
                tbl.append([lbl] + vals); continue
            tbl.append([lbl] + [f(r[k]) for r in rows_])
        out.append(f"### {sname} ($bn unless %)\n")
        out.append(md_table(["Line"] + [f"{y}E" for y in YEARS], tbl) + "\n")
    out.append("Commitment check: compute is floored at the assumed annual schedule "
               f"({', '.join(f'{y}: ${v/1000:.1f}bn' for y, v in A['commit_schedule'].items())}; total $451.6bn to 2030 per A2 p.144, allocation = ASSUMPTION). "
               "Where 'floor binds = yes', fixed commitments, not demand, set compute cost.\n")

    # ---- 6. valuation ----
    out.append("## 6. Valuation at the IPO range\n")
    rows = []
    for px in (lo, mid, hi):
        mcap = px * bases(px)["outstanding"]; ev = mcap - proforma_cash(px)
        rows.append([f"${px:.0f}", ft(mcap), ft(px * bases(px)["tight"]), ft(ev), f"{mcap/F['arr_oct26']:.1f}x",
                     f"{ev/results['Base'][1]['revenue']:.1f}x", f"{ev/results['Base'][2]['revenue']:.1f}x"])
    out.append(md_table(["IPO price", "Mkt cap (outstanding)", "Tighter FD value", "EV (outstanding less pro forma cash)", "Mkt cap / ARR", "EV / Base 27E sales", "EV / Base 28E sales"], rows))
    out.append("\nEV treats the Amazon rollover notes as equity (they settle in shares), not as the $110.9bn fair-value liability on the pro forma balance sheet.\n")
    rows = []
    for sname in scen:
        r = {x["year"]: x for x in results[sname]}
        eps30 = r[2030]["eps_post"]; exit_px = A["exit_pe"] * eps30
        pv = exit_px / (1 + A["discount_rate"]) ** A["hold_years"]
        irr = (exit_px / mid) ** (1 / A["hold_years"]) - 1 if exit_px > 0 else float("nan")
        pe = lambda y: (mid / r[y]["eps_post"]) if r[y]["ni"] > 0 else float("nan")
        rows.append([sname, "n/m" if math.isnan(pe(2027)) else f"{pe(2027):.0f}x", "n/m" if math.isnan(pe(2028)) else f"{pe(2028):.0f}x",
                     f"${eps30:.2f}", f"${exit_px:,.0f}", f"${pv:,.0f}", "n/m" if math.isnan(irr) else f"{irr*100:.1f}%"])
    out.append(f"IPO buyer at the $74 midpoint; P/E on filing-FD-plus-facilities EPS; exit at {A['exit_pe']:.0f}x 2030E EPS after {A['hold_years']:.0f} years; PV at {A['discount_rate']*100:.0f}%.\n")
    out.append(md_table(["Scenario", "P/E 27E", "P/E 28E", "EPS 30E", "Exit price", "PV today", "IRR from $74"], rows))

    # ---- 7. sensitivity ----
    out.append("\n## 7. Sensitivity: 2028E EPS ($) vs revenue path × total compute % of revenue\n")
    hdr = ["Path (2028E rev)"] + [f"compute {int(c*100)}%" for c in A["sens_compute"]] + ["modelled"]
    rows = []
    for sname in scen:
        r28 = results[sname][2]
        vals = [f"{op_model(sname, mid, s_post, s_fd, compute_override_2028=c)[2]['eps_post']:.2f}" for c in A["sens_compute"]]
        rows.append([f"{sname} (${fb(r28['revenue'])}bn)"] + vals + [f"{r28['eps_post']:.2f} @ {fp(r28['compute_pct'])}"])
    out.append(md_table(hdr, rows))
    floor28 = A["commit_schedule"][2028]
    out.append(f"\nNote: grid cells ignore the commitment floor. The assumed 2028 floor is ${floor28/1000:.0f}bn, i.e. {floor28/results['Base'][2]['revenue']*100:.0f}% of Base and {floor28/results['Bear'][2]['revenue']*100:.0f}% of Bear 2028 revenue.\n")

    open(os.path.join(HERE, "output.md"), "w").write("\n".join(out))
    charts(results)
    print("\n".join(out))

def charts(results):
    lo, mid, hi = F["price_low"], F["price_mid"], F["price_high"]
    plt.rcParams.update({"font.size": 11})
    from matplotlib.patches import Patch
    # 1 share bridge at $74
    b = bases(mid)
    steps = [("Outstanding after deal", b["outstanding"], "#4C72B0")]
    colors = {"tight": "#DD8452", "vmo": "#CCB974", "filing": "#8172B2", "overhang": "#937860"}
    for lbl, sh, _, t in layers(mid):
        steps.append((lbl.split(" (")[0], sh, colors[t]))
    for lbl, sh, _ in facilities(mid):
        steps.append((lbl.split(" (")[0].replace(" remaining", ""), sh, "#C44E52"))
    fig, ax = plt.subplots(figsize=(13, 7))
    cum = 0
    for i, (l, s, c) in enumerate(steps):
        bottom = cum if s >= 0 else cum + s
        ax.bar(i, abs(s), bottom=bottom, color=c, edgecolor="black")
        ax.text(i, max(cum, cum + s) + 150, f"{s/1000:+.2f}bn" if i else f"{s/1000:.2f}bn", ha="center", fontsize=8)
        cum += s
    ax.bar(len(steps), cum, color="#55A868", edgecolor="black")
    ax.text(len(steps), cum + 150, f"{cum/1000:.1f}bn", ha="center", fontsize=10, fontweight="bold")
    ax.set_xticks(range(len(steps) + 1))
    ax.set_xticklabels([s[0] for s in steps] + ["Total incl. overhang + facilities"], rotation=35, ha="right", fontsize=8)
    ax.set_ylabel("Shares (millions)")
    ax.set_title("ANT share bridge at the \\$74 midpoint (S-1/A No.2): outstanding -> fully diluted -> overhang -> facilities")
    ax.legend(handles=[Patch(color="#4C72B0", label=f"Outstanding {b['outstanding']/1000:.2f}bn"),
                       Patch(color="#DD8452", label=f"-> tighter FD {b['tight']/1000:.2f}bn"),
                       Patch(color="#CCB974", label=f"-> + vested match {b['vmo']/1000:.2f}bn"),
                       Patch(color="#8172B2", label=f"-> filing FD {b['filing']/1000:.2f}bn"),
                       Patch(color="#937860", label="Plan reserves (overhang)"),
                       Patch(color="#C44E52", label="Remaining facilities at \\$74")], loc="upper left", fontsize=9)
    ax.grid(axis="y", alpha=0.3); fig.tight_layout(); fig.savefig(os.path.join(HERE, "dilution_waterfall.png"), dpi=130); plt.close(fig)
    # 2 revenue scenarios
    fig, ax = plt.subplots(figsize=(10, 6))
    hist = [F["fy_revenue"][2024] / 1000, F["fy_revenue"][2025] / 1000]
    cols = {"Bear": "#C44E52", "Base": "#4C72B0", "Thread": "#8172B2", "Bull": "#55A868"}
    for s, rows in results.items():
        ys = [r["revenue"] / 1000 for r in rows]
        ax.plot([2025] + YEARS, [hist[-1]] + ys, marker="o", label=s, color=cols[s], lw=2)
        ax.annotate(f"\\${ys[-1]:.0f}bn", (2030, ys[-1]), textcoords="offset points", xytext=(6, 0), fontsize=9, color=cols[s])
    ax.plot([2024, 2025], hist, marker="s", color="black", lw=2, label="Actual")
    ax.axhline(F["q_revenue"]["3Q26"] * 4 / 1000, ls="--", color="grey"); ax.text(2024.05, F["q_revenue"]["3Q26"] * 4 / 1000 + 8, "3Q26 annualised \\$67.8bn", color="grey", fontsize=9)
    ax.axhline(F["arr_oct26"] / 1000, ls=":", color="black"); ax.text(2024.05, F["arr_oct26"] / 1000 + 8, "Run-rate revenue 31 Oct 26: \\$81bn", fontsize=9)
    ax.set_ylabel("Revenue ($bn)"); ax.set_title("ANT revenue scenarios (2026E = 9M actual + modelled 4Q)")
    ax.set_xlim(2023.8, 2030.8); ax.legend(); ax.grid(alpha=0.3); fig.tight_layout()
    fig.savefig(os.path.join(HERE, "revenue_scenarios.png"), dpi=130); plt.close(fig)
    # 3 price per share vs market cap, with the filed range
    fig, ax = plt.subplots(figsize=(10, 6))
    caps = A["market_caps"]; bl = [("outstanding", "Outstanding"), ("tight", "Tighter FD"), ("filing", "Filing FD"), ("post", "Filing FD + facilities")]
    w = 0.2
    for j, (k, lbl) in enumerate(bl):
        vals = [solve_price(c, k) for c in caps]
        bars = ax.bar(np.arange(len(caps)) + (j - 1.5) * w, vals, w, label=lbl)
        for bx, v in zip(bars, vals): ax.text(bx.get_x() + bx.get_width() / 2, v + 2, f"\\${v:.0f}", ha="center", fontsize=8)
    ax.axhspan(lo, hi, color="orange", alpha=0.25, label="Filed range \\$70-\\$78")
    sh = F["series_h_price_pref"] / F["pref_conversion_ratio"]
    ax.axhline(sh, color="red", ls="--", label=f"Series H \\${sh:.2f}")
    ax.set_xticks(range(len(caps))); ax.set_xticklabels([f"${c/1e6:.1f}tn" for c in caps])
    ax.set_ylabel("$ per share"); ax.set_title("Implied ANT price per share by share-count basis vs the filed range")
    ax.legend(fontsize=9); ax.grid(axis="y", alpha=0.3); fig.tight_layout(); fig.savefig(os.path.join(HERE, "price_per_share.png"), dpi=130); plt.close(fig)

if __name__ == "__main__":
    main()
