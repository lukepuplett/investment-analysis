"""
CoreWeave (CRWV) toy model of the EQUITY RESIDUAL CLAIM, built on the Q3 2026 results pack (10 Nov 2026).
Question: not whether demand is real, but what is left for equity after lenders, lessors, depreciation, cash capex, dilution.
This is a toy, not a production DCF. To be updated when the Q3 2026 Form 10-Q is filed (it was NOT on EDGAR on 11 Nov 2026).
Units: $ millions and millions of shares unless stated. Presentation capex ("pres capex") and cash purchases of PPE are
DIFFERENT series and are never swapped silently: pres capex = additions to PPE incl. finance-lease assets less change in CIP
(slide 8 footnote 2); cash capex = "Purchases of property and equipment" in the cash-flow statement (Exhibit 99.1).
Every input lives in OFFICIAL / ASSUMPTIONS / SCENARIOS below, each tagged with a source string or "ASSUMPTION".
Run:  python3 crwv_residual_model.py   -> writes output.md and PNG charts in this folder.
"""
import os, copy
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
PACK_DIRS = [os.path.join(HERE, "..", "quarterly")]  # Q3 pack filed as quarterly/2026_Q3_*
PRESS_RELEASE_NAMES = ["2026_Q3_press_release.txt"]

X99 = "Ex.99.1"   # Exhibit 99.1 to the 8-K of 10 Nov 2026 (acc. 0001769628-26-000461)
PRES = "Presentation"  # CoreWeave-3Q26-Earnings-Presentation-Final.pdf
CALL = "Call"          # CoreWeave-3Q26-Transcript.pdf (commentary, NOT a financial statement)

# =============================================================================
# 1. OFFICIAL INPUTS  (value, source)
# =============================================================================
OFFICIAL = {
    # --- Q3 2026 income statement ---
    "q3_revenue": (3661, X99 + " income statement, Q3 2026"),
    "q3_opex": (3454, X99),
    "q3_gaap_oi": (207, X99),
    "q3_interest": (846, X99 + ": interest expense, net"),
    "q3_other_income": (13, X99),
    "q3_net_loss": (-709, X99),
    "q3_adj_ebitda": (2256, X99 + " non-GAAP reconciliation"),
    "q3_adj_oi": (379, X99 + " non-GAAP reconciliation"),
    "q3_da": (1889, X99 + " cash-flow statement"),
    "q3_sbc": (160, X99 + " cash-flow statement"),
    "q3_ocf": (1975, X99 + " cash-flow statement"),
    "q3_cash_ppe": (9441, X99 + ": purchases of property and equipment (cash)"),
    "q3_pres_capex": (14500, PRES + " slide 8/14: $14.5bn capex (pres definition)"),
    "q3_wtd_shares": (559, X99 + ": weighted-average shares, basic and diluted (NOT a period-end FD count)"),
    "q2_revenue": (2575, "Prior official release (Q2 2026), not this exhibit"),
    # --- nine months ---
    "m9_revenue": (8314, X99),
    "m9_gaap_oi": (14, X99),
    "m9_interest": (2022, X99),
    "m9_adj_ebitda": (4923, X99),
    "m9_adj_oi": (528, X99),
    "m9_ocf": (5638, X99),
    "m9_cash_ppe": (23558, X99),
    "m9_da": (4429, X99),
    "m9_sbc": (478, X99),
    "m9_debt_discount_amort": (143, X99 + " cash-flow statement: amortization of debt discounts, issuance costs"),
    "m9_deferred_revenue_cf": (3492, X99 + " cash-flow statement: change in deferred revenue (net, 9M)"),
    "m9_capped_calls": (1058, X99),
    "m9_private_placements": (2982, X99),
    "pres_capex_q1_26": (8200, PRES + " capex chart"), "pres_capex_q2_26": (9400, PRES), "pres_capex_q3_26": (14500, PRES),
    "q3_debt_proceeds": (10301, X99), "q3_debt_repay": (2344, X99), "q3_capped_calls": (566, X99),
    "cip_q3_26": (9300, PRES + ": CIP fell to $9.3bn from $11.9bn in Q2"),
    # --- balance sheet 30 Sep 2026 ---
    "cash": (4122, X99 + " balance sheet"), "restricted_cash_cur": (1405, X99), "restricted_cash_noncur": (877, X99),
    "marketable_securities": (62, X99), "receivables": (4280, X99), "ppe_net": (56778, X99),
    "op_lease_rou": (18922, X99), "total_assets": (91481, X99),
    "recourse_debt_cur": (9183, X99), "recourse_debt_noncur": (32417, X99),
    "nonrecourse_debt_cur": (1389, X99), "nonrecourse_debt_noncur": (3884, X99),
    "deferred_rev_cur": (2269, X99), "deferred_rev_noncur": (7733, X99),
    "op_lease_liab_cur": (668, X99), "op_lease_liab_noncur": (18029, X99),
    "fin_lease_liab_cur": (296, X99), "fin_lease_liab_noncur": (353, X99),
    "total_liabilities": (87456, X99), "equity": (4025, X99),
    "total_cash_like_call": (6500, CALL + ": ~$6.5bn cash, equivalents, restricted cash and marketable securities"),
    # --- outlook (10 Nov 2026) ---
    "fy_rev_low": (13000, X99 + " outlook (prior Aug range $12.4-13.2bn; older $12-13bn)"), "fy_rev_high": (13300, X99),
    "fy_adj_oi_low": (1275, X99 + " outlook (Aug range $960m-1.15bn)"), "fy_adj_oi_high": (1375, X99),
    "fy_capex_low": (37000, X99 + " outlook, pres definition (prior $35-39bn)"), "fy_capex_high": (39000, X99),
    "q4_interest_low": (1050, X99 + " outlook"), "q4_interest_high": (1150, X99),
    "exit_arr_low": (20000, X99 + ": exit-2026 annualised run-rate revenue (last month x12); Aug guide $18.5-19.5bn"),
    "exit_arr_high": (21000, X99),
    "active_power_gw_ye": (1.85, X99 + ": >1.85 GW active power at year-end"),
    "prepay_next_3m": (9000, X99 + ": ~$9bn prepayments and deposits next three months; >$3bn is recontracting existing infrastructure (" + CALL + ")"),
    "convert_raise": (4200, X99 + ": ~$4.2bn upsized convertible senior notes (terms NOT in pack)"),
    "atm_shares_max": (35.0, X99 + ": inaugural ATM, up to 35m Class A (take-up NOT disclosed)"),
    "ddtl_55": (2600, X99 + ": $2.6bn DDTL 5.5 closed"),
    "undrawn_ddtl": (5000, CALL + ": nearly $5bn undrawn under committed DDTLs"),
    "parent_raise_through_2027_max": (5000, CALL + ": expect <$5bn incremental parent-level capital through 2027"),
    # --- backlog ---
    "backlog": (132500, X99 + " / " + PRES + " slide 13"),
    "backlog_rpo": (132300, PRES + " backlog table"), "backlog_other": (200, PRES + " backlog table"),
    "backlog_prior_year": (55600, PRES + " slide 13"),
    "backlog_pct_le24m": (0.36, PRES + " slide 13 CHART (read from the PDF image: dark-blue bottom bar = <24 months)"),
    "backlog_pct_25_48m": (0.38, PRES + " slide 13 chart: mid bar = 25-48 months"),
    "backlog_pct_gt48m": (0.26, PRES + " slide 13 chart: top light bar = >48 months"),
    "backlog_commence_by_ye26": (0.50, CALL + ": >50% of backlog on contracts where delivery commences by end 2026 (commencement, not recognition)"),
    # --- management commentary (claims, not facts) ---
    "wacd": (0.079, CALL + ": weighted-average cost of debt 7.9% at end Q3 (-250bp YoY). A claim"),
    "ddtl_financing_range": ((0.70, 1.00), CALL + ": DDTLs finance 70%-100% of associated capex"),
    "ddtl_spread_bp": ((225, 550), CALL + ": priced SOFR+225 to +550bp since IPO; <10% at the high end today"),
    "new_ig_ddtl_yield": ((0.07, 0.075), CALL + ": next IG DDTL implied 7%-7.5%, >90% of capex"),
    "ig_enterprise_share_committed_capex": (0.75, CALL + ": >75% of committed capex tied to IG/enterprise customers"),
    "debt_paid_down_via_contracts": (4000, CALL + ": >$4bn paid down through contract cash flow"),
    "gpus_off_contract_2027": (130000, CALL), "gpus_off_contract_2028": (170000, CALL),
    "renewal_arr_2027": (4000, CALL + ": 2027 renewals ~ approaching $4bn incremental annualised revenue, no new capex (claim)"),
    "renewal_arr_through_2028": (10000, CALL + ": ~nearly $10bn cumulative incl. 2028 renewals (claim)"),
    "price_close_10nov": (48.73, "README / Yahoo regular close 10 Nov 2026 (prior close 48.98)"),
}

def O(k):
    return OFFICIAL[k][0]

# =============================================================================
# 2. GLOBAL ASSUMPTIONS (value, source) — not official; every one is a judgement
# =============================================================================
ASSUMPTIONS = {
    "ebitda_margin": (0.62, "ASSUMPTION: held at Q3 2026 adj. EBITDA margin (Ex.99.1 62%)"),
    "rev_yield": (0.27, "ASSUMPTION: annualised revenue per $1 of pres capex placed in service. Cross-check: Q4'26 annualised revenue minus Q3'25 annualised revenue / last four quarters' pres capex = ~0.35 before CIP lag; 0.27 is deliberately lower"),
    "inyear_factor": (0.5, "ASSUMPTION: new capacity contributes half a year of revenue in the year it is placed in service"),
    "sbc_annual": (640, "ASSUMPTION: Q3 SBC $160m x 4"),
    "other_income_annual": (52, "ASSUMPTION: Q3 other income $13m x 4"),
    "other_adj_per_year": (48, "ASSUMPTION: Q3 adj OI -> GAAP OI bridge: 379 - 160 SBC - 207 = $12m/qtr other, x4"),
    "adj_oi_bridge_per_year": (48, "ASSUMPTION: Q3 adj. OI minus (adj. EBITDA - D&A) = 379 - 367 = $12m/qtr, x4"),
    "tax_rate": (0.21, "ASSUMPTION: US statutory rate on positive pre-tax income; NOLs and deferred tax ignored"),
    "cash_floor": (3000, "ASSUMPTION: minimum usable cash (cash + securities); Dec-25 usable cash was $3.1bn"),
    "cash_ratio_q4": (1.00, "ASSUMPTION: Q4 cash capex = pres capex (Q3 deliveries pulled forward; payables unwind). 9M history 0.73, Q3 0.65"),
    "cash_ratio_fwd": (0.90, "ASSUMPTION: cash capex / pres capex in 2027-28; the rest is OEM/vendor/finance-lease financed and added to debt. 9M26 actual 0.73"),
    "amort_rate_debt": (None, "DERIVED from balance sheet: current debt / total debt (set below)"),
    "amort_rate_lease": (None, "DERIVED: current operating lease liability / total (set below)"),
    "noncash_interest_share": (None, "DERIVED: 9M debt-discount amortisation / 9M interest = 143/2,022 (set below)"),
    "ar_ratio": (None, "DERIVED: receivables / Q3 annualised revenue (set below)"),
    "da_rate": (None, "DERIVED: Q3 D&A x4 / in-service net PPE (PPE net - CIP) (set below)"),
    "rate_ddtl_new": (0.085, "ASSUMPTION: new asset-level debt; mgmt: <10% at high end, 7-7.5% for IG; 8.5% blended"),
    "rate_parent_new": (0.10, "ASSUMPTION: new limited parent raise (converts/secured/term) at ~10%"),
    "rate_parent_stress": (0.15, "STRESS RATE ONLY: unverified mid-Oct press report of ~15% yield on 2032 unsecured; not an official input"),
    "release_rate_annual": (0.30, "ASSUMPTION: share of (opening deferred revenue + half of receipts) earned into revenue per year"),
    "receipt_rate_new": (0.30, "ASSUMPTION: customer prepayments received per $1 of pres capex; calibrated so net deferred-revenue inflow ~ 9M26 pace ($3.5bn)"),
    "q4_ddtl_share": (0.75, "ASSUMPTION: share of Q4 cash capex funded by asset-level debt (mgmt 70-100%)"),
    "q4_undrawn_check": (None, "see OFFICIAL undrawn_ddtl"),
    "atm_fee": (0.015, "ASSUMPTION: ATM commission/fees"),
    "convert_conv_price": (75.0, "ASSUMPTION placeholder: $4.2bn converts at ~55% premium to $48.73; terms not in pack"),
    "convert_in_debt_already": (True, "ASSUMPTION: the $4.2bn is inside the 30 Sep debt (Q3 capped-call purchase $566m suggests Q3 closing); if it settled in Q4, Q4 debt is $4.2bn higher"),
    # terminal / residual
    "useful_life_yrs": (6.0, "ASSUMPTION: GPU fleet economic life; not in the pack"),
    "residual_value_pct": (0.10, "ASSUMPTION: used-GPU resale as % of cost at end of life; not in the pack"),
    "gross_up": (1.35, "ASSUMPTION: gross / net PPE for a young fleet (about a quarter depreciated)"),
    "maintenance_pct_net_ppe": (0.10, "ASSUMPTION: harvest-case maintenance pres capex as % of opening in-service net PPE; steady-state replacement is 1/life = 16.7%"),
    "ev_ebitda_multiples": ((4.0, 6.0, 8.0), "ASSUMPTION: EV / terminal adj. EBITDA range for a capital-intensive GPU lessor; not market data"),
    "owner_cap_rate": (0.12, "ASSUMPTION: capitalisation rate on steady-state owner earnings"),
    "atm_price_normal": (48.73, "Official 10 Nov close, used as issue price"),
    "atm_price_stress": (34.0, "ASSUMPTION: ~30% below 10 Nov close for the stress case"),
    "q4_recontract_note": (None, ""),
}

def _derive(A):
    """Fill derived assumptions from OFFICIAL (kept out of the calculation functions)."""
    debt = O("recourse_debt_cur") + O("recourse_debt_noncur") + O("nonrecourse_debt_cur") + O("nonrecourse_debt_noncur")
    cur = O("recourse_debt_cur") + O("nonrecourse_debt_cur")
    A["amort_rate_debt"] = (cur / debt, "DERIVED: current debt $%s m / total debt $%s m at 30 Sep 2026 (Ex.99.1)" % (f"{cur:,}", f"{debt:,}"))
    ol = O("op_lease_liab_cur") + O("op_lease_liab_noncur")
    A["amort_rate_lease"] = (O("op_lease_liab_cur") / ol, "DERIVED: current / total operating lease liability (Ex.99.1)")
    A["noncash_interest_share"] = (O("m9_debt_discount_amort") / O("m9_interest"), "DERIVED: 143/2,022 (Ex.99.1)")
    A["ar_ratio"] = (O("receivables") / (4 * O("q3_revenue")), "DERIVED: receivables / (Q3 revenue x4) (Ex.99.1)")
    A["da_rate"] = (4 * O("q3_da") / (O("ppe_net") - O("cip_q3_26")), "DERIVED: Q3 D&A x4 / (PPE net - CIP $9.3bn)")
    return A

ASSUMPTIONS = _derive(ASSUMPTIONS)

def a(A, k):
    return A[k][0]

# =============================================================================
# 3. SCENARIOS — per-year inputs. Q4 2026 is common to all (official guide basis).
# =============================================================================
SCENARIOS = {
    "1A Keep building (committed backlog only)": {
        "short": "1A Keep building",
        "capex_pres": {2027: 38000, 2028: 38000},   # mgmt: committed-backlog-only -> 2027 capex in line with 2026 (FY26 guide mid $38bn)
        "capex_src": "2027: Call - capex 'in line with 2026' if only committed backlog (FY26 mid $38bn). 2028: ASSUMPTION flat",
        "renewal_arr_add": {2027: 0, 2028: 0},       # committed-only: no repricing credit
        "recontract_prepay": {2027: 3000, 2028: 3000},
        "lease_adds": {2027: 6000, 2028: 5000},
        "ddtl_share": {2027: 0.75, 2028: 0.75}, "ddtl_cap": {2027: None, 2028: None},
        "parent_raise": {2027: (4000, "rate_parent_new"), 2028: (2000, "rate_parent_new")},
        "atm_price": "atm_price_normal", "capex_flex": False, "arr_share": 1.0, "cip_completion": {},
    },
    "1B Keep building (optional growth, higher capex + renewals)": {
        "short": "1B Growth capex",
        "capex_pres": {2027: 50000, 2028: 50000},
        "capex_src": "ASSUMPTION: optional higher-capex growth case ($12bn above committed-only)",
        "renewal_arr_add": {2027: 4000, 2028: 6000},  # Call claim: ~$4bn 2027, ~$10bn cumulative incl. 2028 (claim, not contracted)
        "recontract_prepay": {2027: 3000, 2028: 3000},
        "lease_adds": {2027: 10000, 2028: 10000},
        "ddtl_share": {2027: 0.75, 2028: 0.75}, "ddtl_cap": {2027: None, 2028: None},
        "parent_raise": {2027: (5000, "rate_parent_new"), 2028: (3000, "rate_parent_new")},
        "atm_price": "atm_price_normal", "capex_flex": False, "arr_share": 1.0, "cip_completion": {},
    },
    "2 Harvest (capex falls to maintenance)": {
        "short": "2 Harvest",
        "capex_pres": {2027: "maintenance", 2028: "maintenance"},
        "capex_src": "ASSUMPTION: maintenance = maintenance_pct_net_ppe x opening in-service net PPE, adds no revenue; the $9.3bn already in CIP is completed in 2027 with no further cash (ASSUMPTION) and does add revenue",
        "renewal_arr_add": {2027: 0, 2028: 0},
        "recontract_prepay": {2027: 3000, 2028: 3000},
        "lease_adds": {2027: 0, 2028: 0},
        "ddtl_share": {2027: 0.0, 2028: 0.0}, "ddtl_cap": {2027: 0, 2028: 0},
        "parent_raise": {2027: (0, "rate_parent_new"), 2028: (0, "rate_parent_new")},
        "atm_price": "atm_price_normal", "capex_flex": False, "arr_share": 0.0,
        "cip_completion": {2027: 9300},   # CIP at 30 Sep ($9.3bn, Presentation) finishes and is placed in service; cash already paid
    },
    "3 Funding stress (no parent unsecured; capex flexes to funding)": {
        "short": "3 Funding stress",
        "capex_pres": {2027: 38000, 2028: 38000},
        "capex_src": "Plan = committed-only $38bn; capex is cut until funded (bisection)",
        "renewal_arr_add": {2027: 0, 2028: 0},
        "recontract_prepay": {2027: 3000, 2028: 3000},
        "lease_adds": {2027: 3000, 2028: 2000},
        "ddtl_share": {2027: 0.55, 2028: 0.55},
        "ddtl_cap": {2027: 13000, 2028: 10000},     # ASSUMPTION: lender appetite; $5bn undrawn (Call) + new facilities
        "parent_raise": {2027: (1500, "rate_parent_stress"), 2028: (1000, "rate_parent_stress")},
        "atm_price": "atm_price_stress", "capex_flex": True, "arr_share": 1.0, "cip_completion": {},
    },
}

# =============================================================================
# 4. CORE ENGINE
# =============================================================================
def opening_state(A):
    debt = O("recourse_debt_cur") + O("recourse_debt_noncur") + O("nonrecourse_debt_cur") + O("nonrecourse_debt_noncur")
    return {
        "legacy": debt, "ddtl": 0.0, "parent": 0.0,
        "op_lease": O("op_lease_liab_cur") + O("op_lease_liab_noncur"),
        "fin_lease": O("fin_lease_liab_cur") + O("fin_lease_liab_noncur"),
        "equity": O("equity"),
        "liquidity": O("cash") + O("marketable_securities"),
        "deferred": O("deferred_rev_cur") + O("deferred_rev_noncur"),
        "ppe_in": O("ppe_net") - O("cip_q3_26"),
        "arr": 4 * O("q3_revenue"),
        "shares": O("q3_wtd_shares"),
        "atm_shares_left": O("atm_shares_max"),
        "r_legacy": None,
    }

def period_step(A, st, P):
    """One period. P: dict of period inputs (years, capex_plan, ...). Returns (new_state, metrics)."""
    def attempt(scale):
        yrs = P["years"]
        capex_pres = scale * P["capex_plan"]
        cash_ratio = P["cash_ratio"]
        cash_capex = capex_pres * cash_ratio
        oem = capex_pres - cash_capex
        # --- revenue / earnings ---
        if P.get("revenue_override") is not None:
            revenue = P["revenue_override"]; arr_exit = P["arr_exit_override"]
            ebitda = revenue * a(A, "ebitda_margin")
            adj_oi = P["adj_oi_override"]
            da = ebitda - adj_oi + a(A, "adj_oi_bridge_per_year") * yrs
        else:
            inserv = capex_pres + P["cip_completion"]
            new_arr = (capex_pres * P["arr_share"] + P["cip_completion"]) * a(A, "rev_yield")
            arr_exit = st["arr"] + new_arr + P["renewal_arr_add"]
            revenue = (st["arr"] + a(A, "inyear_factor") * (new_arr + P["renewal_arr_add"])) * yrs
            ebitda = revenue * a(A, "ebitda_margin")
            r = a(A, "da_rate")
            da = r * (st["ppe_in"] + inserv / 2.0) / (1 + r / 2.0) * yrs
            adj_oi = ebitda - da + a(A, "adj_oi_bridge_per_year") * yrs
        inserv = capex_pres + P["cip_completion"]
        sbc = a(A, "sbc_annual") * yrs
        gaap_oi = adj_oi - sbc - a(A, "other_adj_per_year") * yrs
        # --- debt roll ---
        leg_am = a(A, "amort_rate_debt") * yrs * st["legacy"]
        ddtl_am = a(A, "amort_rate_debt") * yrs * st["ddtl"]
        ddtl_draw = P["ddtl_share"] * cash_capex
        if P["ddtl_cap"] is not None:
            ddtl_draw = min(ddtl_draw, P["ddtl_cap"])
        parent_draw, parent_rate = P["parent_raise"]
        leg_close = st["legacy"] - leg_am
        ddtl_close = st["ddtl"] - ddtl_am + ddtl_draw + oem
        par_close = st["parent"] + parent_draw
        rate_ddtl = a(A, "rate_ddtl_new"); rate_par = a(A, parent_rate)
        other_int = (rate_ddtl * (st["ddtl"] + ddtl_close) / 2 + rate_par * (st["parent"] + par_close) / 2) * yrs
        if P.get("interest_target") is not None:      # Q4: calibrate the effective legacy rate to the official guide
            interest = P["interest_target"]
            r_leg = (interest - other_int) / (yrs * (st["legacy"] + leg_close) / 2)
        else:
            r_leg = st["r_legacy"]
            interest = r_leg * yrs * (st["legacy"] + leg_close) / 2 + other_int
        cash_interest = interest * (1 - a(A, "noncash_interest_share"))
        pretax = gaap_oi - interest + a(A, "other_income_annual") * yrs
        tax = a(A, "tax_rate") * max(0.0, pretax)
        net_income = pretax - tax
        # --- working capital ---
        d_ar = a(A, "ar_ratio") * (arr_exit - st["arr"])
        receipts = P["receipts_fixed"] + P["receipt_rate"] * capex_pres
        release = min(st["deferred"] + receipts, a(A, "release_rate_annual") * yrs * (st["deferred"] + 0.5 * receipts))
        net_prepay = receipts - release
        ocf_ex = ebitda - cash_interest - tax - d_ar
        ocf = ocf_ex + net_prepay
        # --- sources and uses ---
        repay = leg_am + ddtl_am
        capped = P["capped_calls"]
        uses = cash_capex + repay + capped
        sources = ocf + ddtl_draw + parent_draw
        gap0 = uses - sources
        cushion = max(0.0, st["liquidity"] - a(A, "cash_floor"))
        from_cash = min(max(gap0, 0.0), cushion)
        gap1 = gap0 - from_cash
        atm_price = P["atm_price"]
        atm_cap_dollars = st["atm_shares_left"] * atm_price * (1 - a(A, "atm_fee"))
        atm_amt = min(max(gap1, 0.0), atm_cap_dollars)
        atm_sh = atm_amt / (atm_price * (1 - a(A, "atm_fee"))) if atm_amt > 0 else 0.0
        unfunded = max(gap1, 0.0) - atm_amt
        liq_close = st["liquidity"] - from_cash + atm_amt + max(0.0, -gap0)
        ns = dict(st)
        ns.update({
            "legacy": leg_close, "ddtl": ddtl_close, "parent": par_close,
            "op_lease": st["op_lease"] + P["lease_adds"] - a(A, "amort_rate_lease") * yrs * st["op_lease"],
            "equity": st["equity"] + net_income + sbc + atm_amt - capped,
            "liquidity": liq_close,
            "deferred": st["deferred"] + receipts - release,
            "ppe_in": st["ppe_in"] + inserv - da,
            "arr": arr_exit,
            "shares": st["shares"] + atm_sh + sbc / atm_price,
            "atm_shares_left": st["atm_shares_left"] - atm_sh,
            "r_legacy": r_leg,
        })
        debt_close = leg_close + ddtl_close + par_close
        m = {
            "revenue": revenue, "arr_exit": arr_exit, "ebitda": ebitda, "da": da, "adj_oi": adj_oi, "sbc": sbc,
            "gaap_oi": gaap_oi, "interest": interest, "cash_interest": cash_interest, "net_income": net_income,
            "capex_pres": capex_pres, "cash_capex": cash_capex, "oem_financed": oem,
            "d_ar": d_ar, "receipts": receipts, "release": release, "net_prepay": net_prepay,
            "ocf_ex": ocf_ex, "ocf": ocf, "fcf_ex": ocf_ex - cash_capex, "fcf_incl": ocf - cash_capex,
            "repay": repay, "capped": capped, "ddtl_draw": ddtl_draw, "parent_draw": parent_draw,
            "from_cash": from_cash, "atm_amt": atm_amt, "atm_shares": atm_sh, "unfunded": unfunded,
            "uses": uses, "surplus": max(0.0, -gap0),
            "debt": debt_close, "debt_like": debt_close + st["fin_lease"], "op_lease": ns["op_lease"],
            "debt_leases": debt_close + st["fin_lease"] + ns["op_lease"],
            "equity": ns["equity"], "shares": ns["shares"], "liquidity": liq_close, "deferred": ns["deferred"],
            "r_legacy": r_leg, "scale": scale,
            "cov_ebitda": ebitda / interest, "cov_gaap_oi": gaap_oi / interest,
            "dscr_ex": ocf_ex / (cash_interest + repay),
        }
        return ns, m, unfunded
    ns, m, unf = attempt(1.0)
    if P["flex"] and unf > 1.0:
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            _, _, u = attempt(mid)
            if u > 1.0: hi = mid
            else: lo = mid
        ns, m, unf = attempt(lo)
    return ns, m

def q4_inputs(A, mode="mid"):
    f = {"low": 0.0, "mid": 0.5, "high": 1.0}[mode]
    lerp = lambda lo, hi: O(lo) + f * (O(hi) - O(lo))
    fy_rev = lerp("fy_rev_low", "fy_rev_high"); fy_oi = lerp("fy_adj_oi_low", "fy_adj_oi_high")
    fy_capex = lerp("fy_capex_low", "fy_capex_high")
    pres9 = O("pres_capex_q1_26") + O("pres_capex_q2_26") + O("pres_capex_q3_26")
    return {
        "years": 0.25, "revenue_override": fy_rev - O("m9_revenue"), "adj_oi_override": fy_oi - O("m9_adj_oi"),
        "arr_exit_override": lerp("exit_arr_low", "exit_arr_high"),
        "capex_plan": fy_capex - pres9, "cash_ratio": a(A, "cash_ratio_q4"),
        "interest_target": lerp("q4_interest_low", "q4_interest_high"),
        "ddtl_share": a(A, "q4_ddtl_share"), "ddtl_cap": O("undrawn_ddtl"), "parent_raise": (0.0, "rate_parent_new"),
        "receipts_fixed": O("prepay_next_3m"), "receipt_rate": 0.0, "arr_share": 1.0, "cip_completion": 0.0, "renewal_arr_add": 0.0, "lease_adds": 0.0, "capped_calls": 0.0,
        "atm_price": a(A, "atm_price_normal"), "flex": False,
    }

def year_inputs(A, scn, yr, st):
    c = scn["capex_pres"][yr]
    if c == "maintenance":
        c = a(A, "maintenance_pct_net_ppe") * st["ppe_in"]
    rc_amt, rc_rate = scn["parent_raise"][yr]
    return {
        "years": 1.0, "capex_plan": c, "cash_ratio": a(A, "cash_ratio_fwd"), "renewal_arr_add": scn["renewal_arr_add"][yr],
        "ddtl_share": scn["ddtl_share"][yr], "ddtl_cap": scn["ddtl_cap"][yr], "parent_raise": (rc_amt, rc_rate),
        "receipts_fixed": scn["recontract_prepay"][yr], "receipt_rate": a(A, "receipt_rate_new"), "arr_share": scn["arr_share"], "cip_completion": scn["cip_completion"].get(yr, 0.0), "lease_adds": scn["lease_adds"][yr], "capped_calls": 0.0,
        "atm_price": a(A, scn["atm_price"]), "flex": scn["capex_flex"],
    }

def terminal(A, st, m_last):
    """Steady-state at the exit-2028 run-rate: replace the fleet, pay interest, then see what equity gets."""
    ebitda_t = st["arr"] * a(A, "ebitda_margin")
    fleet_cost = st["ppe_in"] * a(A, "gross_up")
    dep_t = fleet_cost / a(A, "useful_life_yrs")
    repl = dep_t * (1 - a(A, "residual_value_pct"))
    rate_ddtl = a(A, "rate_ddtl_new")
    interest_t = st["r_legacy"] * st["legacy"] + rate_ddtl * st["ddtl"] + m_last["parent_rate_used"] * st["parent"]
    sbc = a(A, "sbc_annual")
    taxable = ebitda_t - dep_t - interest_t - sbc
    tax = a(A, "tax_rate") * max(0.0, taxable)
    owner = ebitda_t - repl - interest_t - tax - sbc
    deferred_cost = st["deferred"] * (1 - a(A, "ebitda_margin"))
    debt = st["legacy"] + st["ddtl"] + st["parent"]
    out = {"ebitda_t": ebitda_t, "repl": repl, "dep_t": dep_t, "interest_t": interest_t, "tax_t": tax, "owner": owner,
           "debt": debt, "fin_lease": st["fin_lease"], "liquidity": st["liquidity"], "deferred_cost": deferred_cost,
           "shares": st["shares"], "equity_book": st["equity"]}
    out["owner_cap_value"] = owner / a(A, "owner_cap_rate")
    out["owner_cap_equity"] = out["owner_cap_value"]  # owner earnings are already after interest => equity value
    eq = {}
    for mult in a(A, "ev_ebitda_multiples"):
        ev = ebitda_t * mult
        eq[mult] = ev - debt - st["fin_lease"] + st["liquidity"] - deferred_cost
    out["equity_at_mult"] = eq
    out["per_share_at_mult"] = {k: v / st["shares"] for k, v in eq.items()}
    out["owner_cap_per_share"] = out["owner_cap_equity"] / st["shares"]
    out["interest_cover_t"] = ebitda_t / interest_t if interest_t else float("inf")
    out["repl_cover_t"] = (ebitda_t - repl) / interest_t if interest_t else float("inf")
    return out

def run_all(A=None, only=None):
    A = A or ASSUMPTIONS
    res = {}
    base = opening_state(A)
    # Q4 2026 (common): range table on the official guide, model on the midpoint
    st_q4, m_q4 = period_step(A, base, q4_inputs(A, "mid"))
    q4_range = {}
    for mode in ("low", "mid", "high"):
        _, mm = period_step(A, base, q4_inputs(A, mode))
        q4_range[mode] = mm
    for name, scn in SCENARIOS.items():
        if only and name != only: continue
        st = copy.deepcopy(st_q4); periods = {"Q4'26": m_q4}
        for yr in (2027, 2028):
            P = year_inputs(A, scn, yr, st)
            st, m = period_step(A, st, P)
            m["parent_rate_used"] = a(A, scn["parent_raise"][yr][1]); m["capex_plan"] = P["capex_plan"]
            periods["FY%d" % (yr % 100)] = m
        res[name] = {"periods": periods, "end_state": st, "terminal": terminal(A, st, m)}
    return res, base, st_q4, q4_range

# =============================================================================
# 5. CHECKS AGAINST THE PACK
# =============================================================================
def verify_official():
    out = []
    debt = O("recourse_debt_cur") + O("recourse_debt_noncur") + O("nonrecourse_debt_cur") + O("nonrecourse_debt_noncur")
    rec = O("recourse_debt_cur") + O("recourse_debt_noncur"); nonrec = O("nonrecourse_debt_cur") + O("nonrecourse_debt_noncur")
    opl = O("op_lease_liab_cur") + O("op_lease_liab_noncur"); fl = O("fin_lease_liab_cur") + O("fin_lease_liab_noncur")
    cashlike = O("cash") + O("restricted_cash_cur") + O("restricted_cash_noncur") + O("marketable_securities")
    cashlike_ex_noncur = O("cash") + O("restricted_cash_cur") + O("marketable_securities")
    checks = [
        ("debt = 46,873", debt == 46873), ("recourse 41,600", rec == 41600), ("non-recourse 5,273", nonrec == 5273),
        ("operating lease liabilities 18,697", opl == 18697), ("finance lease liabilities 649", fl == 649),
        ("debt + leases about 66.2bn", abs(debt + opl + fl - 66219) < 1),
        ("cash + restricted (cur+noncur) + securities = 6,466 (call: ~$6.5bn)", cashlike == 6466),
        ("Q3 opex 3,454 - revenue 3,661 => GAAP OI 207", O("q3_revenue") - O("q3_opex") == O("q3_gaap_oi")),
        ("Q3 revenue up > $1bn QoQ", O("q3_revenue") - O("q2_revenue") > 1000),
        ("backlog RPO + other = 132.5bn", O("backlog_rpo") + O("backlog_other") == O("backlog")),
        ("backlog tenor shares sum to 100%", abs(O("backlog_pct_le24m") + O("backlog_pct_25_48m") + O("backlog_pct_gt48m") - 1) < 1e-9),
        ("presentation capex Q3 = $14.5bn vs cash PPE $9.4bn (different series)", O("q3_pres_capex") != O("q3_cash_ppe")),
    ]
    for label, ok in checks: out.append((label, ok))
    # strings present in the press release extract
    txt = None
    for d in PACK_DIRS:
        for n in PRESS_RELEASE_NAMES:
            p = os.path.join(d, n)
            if os.path.exists(p):
                txt = open(p, encoding="utf-8", errors="ignore").read(); break
        if txt: break
    if txt is None:
        out.append(("press-release text extract found for string checks", False))
    else:
        needles = ["3,661", "1,889", "1,975", "9,441", "23,558", "5,638", "10,301", "2,344", "56,778", "91,481", "87,456", "4,025",
                   "13.0", "1.275", "37", "1.05", "20", "132.5", "35 million"]
        for nd in needles:
            out.append(("string '%s' present in Ex.99.1 text extract" % nd, nd in txt))
    return out

# =============================================================================
# 6. FORMATTING + OUTPUT
# =============================================================================
def f0(x): return f"{x:,.0f}"
def fb(x): return f"{x/1000:,.1f}" if abs(x) >= 50 else "~0"
def fx(x): return f"{x:.2f}x"
def fp(x): return f"{x*100:.0f}%"
def fs(x): return f"{x:,.1f}"

def table(headers, rows):
    s = "| " + " | ".join(headers) + " |\n|" + "|".join(["---"] + ["---:"] * (len(headers) - 1)) + "|\n"
    for r in rows: s += "| " + " | ".join(str(c) for c in r) + " |\n"
    return s

def sensitivity(A):
    """Per-share equity at the middle multiple for scenario 1A under +/- changes in single assumptions."""
    mid = a(A, "ev_ebitda_multiples")[1]
    name = list(SCENARIOS)[0]
    def val(A2, scn_override=None):
        saved = None
        if scn_override:
            saved = copy.deepcopy(SCENARIOS[name]); SCENARIOS[name].update(scn_override)
        r, *_ = run_all(A2, only=name)
        if saved is not None: SCENARIOS[name].clear(); SCENARIOS[name].update(saved)
        t = r[name]["terminal"]
        return t["per_share_at_mult"][a(A2, "ev_ebitda_multiples")[1]], t["owner"]
    base_v, base_o = val(A)
    rows = []
    def tweak(label, key, lo, hi):
        vals = []
        for v in (lo, hi):
            A2 = copy.deepcopy(A); A2[key] = (v, "sensitivity")
            vals.append(val(A2))
        rows.append((label, vals[0][0], vals[1][0], vals[0][1], vals[1][1]))
    tweak("Adj. EBITDA margin 60% / 64%", "ebitda_margin", 0.60, 0.64)
    tweak("Revenue per $ capex 0.22 / 0.32", "rev_yield", 0.22, 0.32)
    tweak("Cash capex / pres capex 1.00 / 0.80", "cash_ratio_fwd", 1.00, 0.80)
    tweak("Useful life 5 / 7 years", "useful_life_yrs", 5.0, 7.0)
    tweak("Residual value 0% / 20%", "residual_value_pct", 0.0, 0.20)
    tweak("New DDTL rate 10.5% / 6.5%", "rate_ddtl_new", 0.105, 0.065)
    A2 = copy.deepcopy(A); A2["ev_ebitda_multiples"] = ((4.0, 4.0, 8.0), "s"); lo = val(A2)
    A2["ev_ebitda_multiples"] = ((4.0, 8.0, 8.0), "s"); hi = val(A2)
    rows.append(("EV/EBITDA multiple 4x / 8x", lo[0], hi[0], base_o, base_o))
    return base_v, base_o, rows

def charts(res, base, q4_range, A):
    names = list(res); short = [SCENARIOS[n]["short"] for n in names]
    colors = ["#1f5fbf", "#6aa6e8", "#2f8f5b", "#c0392b"]
    periods = ["Q4'26", "FY27", "FY28"]
    # 1 coverage
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    w = 0.2
    for i, n in enumerate(names):
        ax[0].bar(np.arange(3) + i * w, [res[n]["periods"][p]["cov_gaap_oi"] for p in periods], w, label=short[i], color=colors[i])
        ax[1].bar(np.arange(3) + i * w, [res[n]["periods"][p]["dscr_ex"] for p in periods], w, label=short[i], color=colors[i])
    for x in ax:
        x.set_xticks(np.arange(3) + 1.5 * w); x.set_xticklabels(periods); x.axhline(1, color="k", lw=0.8, ls="--")
    ax[0].set_title("GAAP operating income / net interest (x)"); ax[1].set_title("Op. cash flow ex-prepayments / (cash interest + scheduled principal)")
    ax[0].legend(fontsize=8); fig.tight_layout(); fig.savefig(os.path.join(HERE, "coverage.png"), dpi=130); plt.close(fig)
    # 2 cash after capex
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    for i, n in enumerate(names):
        ax[0].bar(np.arange(3) + i * w, [res[n]["periods"][p]["fcf_ex"] / 1000 for p in periods], w, label=short[i], color=colors[i])
        ax[1].bar(np.arange(3) + i * w, [res[n]["periods"][p]["fcf_incl"] / 1000 for p in periods], w, label=short[i], color=colors[i])
    for x in ax:
        x.set_xticks(np.arange(3) + 1.5 * w); x.set_xticklabels(periods); x.axhline(0, color="k", lw=0.8)
    ax[0].set_title("Cash after interest and cash capex, EXCLUDING net prepayments ($bn)"); ax[1].set_title("... INCLUDING net prepayments ($bn)")
    ax[0].legend(fontsize=8); fig.tight_layout(); fig.savefig(os.path.join(HERE, "cash_after_capex.png"), dpi=130); plt.close(fig)
    # 3 leverage
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    x0 = ["Q3'26"] + periods
    d0 = (base["legacy"] + base["fin_lease"] + base["op_lease"]) / 1000; e0 = base["equity"]
    for i, n in enumerate(names):
        dl = [d0] + [res[n]["periods"][p]["debt_leases"] / 1000 for p in periods]
        eq = [e0] + [res[n]["periods"][p]["equity"] for p in periods]
        ax[0].plot(x0, dl, marker="o", color=colors[i], label=short[i])
        ax[1].plot(x0, [d * 1000 / e if e > 0 else np.nan for d, e in zip(dl, eq)], marker="o", color=colors[i], label=short[i])
    ax[0].set_title("Debt + finance + operating leases ($bn)"); ax[1].set_title("(Debt + leases) / book equity (x; blank if equity <= 0)")
    ax[0].legend(fontsize=8); fig.tight_layout(); fig.savefig(os.path.join(HERE, "leverage.png"), dpi=130); plt.close(fig)
    # 4 residual range per share
    fig, ax = plt.subplots(figsize=(9, 4.6))
    mults = a(A, "ev_ebitda_multiples")
    for i, n in enumerate(names):
        t = res[n]["terminal"]["per_share_at_mult"]; vals = [t[m] for m in mults]
        ax.vlines(i, min(vals), max(vals), color=colors[i], lw=14, alpha=0.55)
        for m, v in zip(mults, vals): ax.text(i + 0.12, v, f"{m:.0f}x: ${v:,.0f}", fontsize=8, va="center")
        ax.plot([i], [res[n]["terminal"]["owner_cap_per_share"]], marker="D", color="k")
    ax.axhline(0, color="k", lw=0.8); ax.axhline(O("price_close_10nov"), color="#888", ls="--", lw=1)
    ax.text(3.45, O("price_close_10nov"), "10 Nov close $48.73", fontsize=8, va="bottom", ha="right", color="#555")
    ax.set_xticks(range(len(names))); ax.set_xticklabels(short, fontsize=8)
    ax.set_title("Residual equity per share at end-2028 (bar = EV/EBITDA %s-%sx; diamond = owner earnings at %s cap rate)" % (f"{mults[0]:.0f}", f"{mults[-1]:.0f}", fp(a(A, 'owner_cap_rate'))), fontsize=9)
    ax.set_ylabel("$ per share (toy; not a target)"); fig.tight_layout(); fig.savefig(os.path.join(HERE, "residual_range.png"), dpi=130); plt.close(fig)

def write_output(res, base, st_q4, q4_range, A):
    names = list(res); mults = a(A, "ev_ebitda_multiples"); mid = mults[1]
    periods = ["Q4'26", "FY27", "FY28"]
    L = []
    price = O("price_close_10nov")
    # punchline
    def ps(n, m): return res[n]["terminal"]["per_share_at_mult"][m]
    n1a, n1b, n2, n3 = names
    L.append("# CoreWeave (CRWV) — equity residual toy model (Q3 2026 pack, 10 Nov 2026)\n")
    L.append("*Toy model, not a production DCF and not a recommendation. Written for the Q3 2026 8-K/Ex.99.1, presentation and call. The Q3 10-Q was not on EDGAR on 11 Nov 2026, so debt and lease schedules, coupons, converts and diluted shares are explicit gaps. $ millions unless stated.*\n")
    L.append("## Punchline\n")
    q4 = q4_range["mid"]
    Q4K = "Q4'26"
    q4_rate = '%.1f%%' % (q4['r_legacy'] * 100)
    t1a = res[n1a]["terminal"]; p1a = res[n1a]["periods"]; p2 = res[n2]["periods"]; p3 = res[n3]["periods"]
    per_turn = (t1a["per_share_at_mult"][mults[2]] - t1a["per_share_at_mult"][mults[0]]) / (mults[2] - mults[0])
    L.append(f"**Demand printed. Whether anything reaches equity is decided by funding, replacement capex and the multiple a buyer pays, not by the outlook raise. On the hard measures the claim is tight: in the keep-building path debt + leases rise from about 66bn to {fb(p1a['FY28']['debt_leases'])}bn against {fb(p1a['FY28']['equity'])}bn of book equity, and each 1x of EV/EBITDA moves equity by about ${per_turn:,.0f} a share (toy count), so equity is a levered option on the multiple.**\n")
    L.append(f"- **The Q4 guide does not cover its own interest.** FY adj. OI guide ($1.275-1.375bn) less 9M actual $528m implies Q4 adj. OI of about $747-847m (mid {f0(q4['adj_oi'])}); Q4 net interest is guided at $1.05-1.15bn (mid {f0(q4['interest'])}). Adj. OI minus interest in Q4 is **{f0(q4['adj_oi']-q4['interest'])}** at the midpoint; model GAAP OI is about {f0(q4['gaap_oi'])}, so GAAP OI / interest is **{fx(q4['cov_gaap_oi'])}**.")
    L.append(f"- **Keep building (1A) is funded by lenders, not by operations.** FY27 cash after interest and cash capex excluding prepayments is {fb(p1a['FY27']['fcf_ex'])}bn ({fb(p1a['FY27']['fcf_incl'])}bn with net prepayments), covered by about {fb(p1a['FY27']['ddtl_draw']+p1a['FY27']['parent_draw']+p1a['FY27']['oem_financed'])}bn of new debt-like funding against {fb(O('undrawn_ddtl'))}bn of undrawn DDTLs today. GAAP OI / interest is {fx(p1a['FY27']['cov_gaap_oi'])} in FY27 and {fx(p1a['FY28']['cov_gaap_oi'])} in FY28. At steady state on the exit-2028 run-rate, owner earnings after replacement capex, interest, tax and SBC are {fb(t1a['owner'])}bn.")
    L.append(f"- **Harvest (2) turns cash after capex positive by design ({fb(p2['FY27']['fcf_ex'])}bn FY27, {fb(p2['FY28']['fcf_ex'])}bn FY28 excluding prepayments), but it does not reach equity cleanly.** It still falls {fb(p2['FY27']['unfunded']+p2['FY28']['unfunded'])}bn short of the scheduled-principal proxy over two years (refinancing or ATM; ATM draws {fs(p2['FY27']['atm_shares']+p2['FY28']['atm_shares'])}m shares), prepayments unwind (net {fb(p2['FY27']['net_prepay'])}bn in FY27), its maintenance capex of {fb(p2['FY28']['cash_capex'])}bn is below steady-state fleet replacement of {fb(res[n2]['terminal']['repl'])}bn, and it gives up growth: FY28 revenue {fb(p2['FY28']['revenue'])}bn vs {fb(p1a['FY28']['revenue'])}bn in 1A. Steady-state owner earnings are {fb(res[n2]['terminal']['owner'])}bn.")
    L.append(f"- **Funding stress (3)** has no parent unsecured issuance. Capex flexes down to what can be funded: FY27 pres capex {fb(p3['FY27']['capex_pres'])}bn of {fb(p3['FY27']['capex_plan'])}bn planned and FY28 {fb(p3['FY28']['capex_pres'])}bn. The ATM is needed in FY27 (35.0m shares, about {fb(p3['FY27']['atm_amt'])}bn at the $34 stress price), is then exhausted, and a {fb(p3['FY28']['unfunded'])}bn FY28 shortfall remains even at zero growth capex on the scheduled-principal proxy. Toy end-2028 share count {fs(res[n3]['end_state']['shares'])}m vs {fs(res[n1a]['end_state']['shares'])}m in 1A.")
    L.append(f"- Reference only: 10 Nov close ${price:.2f} x 559m weighted shares = about ${price*O('q3_wtd_shares')/1000:,.1f}bn (not a fully diluted market cap). Debt + all leases at 30 Sep were about $66.2bn against $4.0bn of book equity.")
    L.append("- The residual is a function of a few assumptions that the pack does not give: **(1) useful life and residual GPU value, (2) EV/EBITDA a buyer pays, (3) cash vs presentation capex, (4) what the 10-Q says about debt cost and maturities.** See sensitivity and the closing list.\n")
    # verification
    L.append("## Checks against the pack\n")
    vr = verify_official(); bad = [l for l, ok in vr if not ok]
    L.append(f"{len(vr)-len(bad)} of {len(vr)} arithmetic/provenance checks passed." + ("" if not bad else " **Failed:** " + "; ".join(bad)) + "\n")
    # Q4 guide
    L.append("## Q4 2026 implied by the official guide\n")
    rows = []
    for mode, lab in (("low", "Low end of FY guide"), ("mid", "Midpoint"), ("high", "High end")):
        mm = q4_range[mode]
        rows.append((lab, f0(mm["revenue"]), f0(mm["adj_oi"]), f0(mm["interest"]), f0(mm["adj_oi"] - mm["interest"]), f0(mm["gaap_oi"]), fx(mm["cov_gaap_oi"]), f0(mm["capex_pres"])))
    L.append(table(["Case", "Q4 revenue", "Q4 adj. OI", "Q4 interest", "Adj. OI - interest", "Q4 GAAP OI (model)", "GAAP OI / interest", "Q4 pres capex"], rows))
    L.append(f"*FY less nine months: revenue 13,000-13,300 less {f0(O('m9_revenue'))}; adj. OI 1,275-1,375 less {f0(O('m9_adj_oi'))}; pres capex 37-39bn less 32.1bn (8.2 + 9.4 + 14.5). Low end pairs with the low end of every guide. Q4 GAAP OI = adj. OI - SBC - other adjustments (ASSUMPTION, Q3 bridge). The implied effective rate on existing debt that reproduces the Q4 interest guide is **{q4_rate}**, against management's 7.9% weighted average cost of debt; the gap is lease interest, fees and amortisation, and lower capitalised interest as CIP falls (inference, not disclosed).*\n")
    # scenario tables
    L.append("## Scenarios (all go through to cash after interest, leases, capex)\n")
    L.append("**Where leases enter:** operating lease cost is already inside adj. EBITDA and GAAP OI, so every coverage ratio below is after lease cost. Finance-lease / OEM-financed capex is added to debt and pays interest at the new-asset rate. Operating lease liabilities are added to debt in the leverage lines. Lease additions are ASSUMPTIONS per scenario.\n")
    L.append("Q4 2026 is common to all scenarios (official guide, midpoint). Scenarios diverge from FY27. 2027 'committed backlog only' follows management: capex in line with 2026 and revenue and EBITDA grow significantly; revenue itself is an ASSUMPTION.\n")
    for n in names:
        scn = SCENARIOS[n]; p = res[n]["periods"]
        L.append(f"### {n}\n")
        L.append(f"*Capex basis: {scn['capex_src']}.*\n")
        rows = []
        def row(label, key, fmt=f0): rows.append([label] + [fmt(p[k][key]) for k in periods])
        row("Revenue", "revenue"); row("Exit run-rate revenue (ARR)", "arr_exit"); row("Adj. EBITDA", "ebitda"); row("D&A", "da")
        row("Adj. operating income", "adj_oi"); row("GAAP operating income", "gaap_oi"); row("Net interest expense", "interest")
        row("Net income (toy)", "net_income"); row("Pres capex (placed in service)", "capex_pres"); row("Cash capex", "cash_capex")
        row("  of which OEM/vendor-financed (added to debt)", "oem_financed")
        row("Op. cash flow excl. net prepayments", "ocf_ex"); row("Net prepayments (receipts less released to revenue)", "net_prepay")
        row("Op. cash flow incl. prepayments", "ocf"); row("Cash after interest and capex, excl. prepayments", "fcf_ex")
        row("Cash after interest and capex, incl. prepayments", "fcf_incl")
        rows.append(["Adj. EBITDA / interest"] + [fx(p[k]["cov_ebitda"]) for k in periods])
        rows.append(["GAAP OI / interest"] + [fx(p[k]["cov_gaap_oi"]) for k in periods])
        rows.append(["Op. CF ex-prepay / (cash interest + scheduled principal)"] + [fx(p[k]["dscr_ex"]) for k in periods])
        L.append(table(["$m"] + periods, rows))
        L.append("**Sources and uses** (funding identity: uses = sources + unfunded)\n")
        rows = []
        def srow(label, key, sign=1): rows.append([label] + [f0(sign * p[k][key]) for k in periods])
        srow("Uses: cash capex", "cash_capex"); srow("Uses: scheduled debt principal", "repay"); srow("Uses: capped calls", "capped")
        srow("Uses total", "uses")
        srow("Sources: op. cash flow (incl. net prepayments)", "ocf"); srow("Sources: asset-level debt draws", "ddtl_draw")
        srow("Sources: parent-level raise", "parent_draw"); srow("Sources: cash drawdown to floor", "from_cash")
        srow("Sources: ATM equity", "atm_amt"); srow("UNFUNDED gap", "unfunded")
        srow("Surplus added to cash", "surplus")
        L.append(table(["$m"] + periods, rows))
        rows = []
        rows.append(["Debt (recourse + non-recourse + new)"] + [f0(p[k]["debt"]) for k in periods])
        rows.append(["Finance lease liabilities"] + [f0(O('fin_lease_liab_cur') + O('fin_lease_liab_noncur'))] * 3)
        rows.append(["Operating lease liabilities"] + [f0(p[k]["op_lease"]) for k in periods])
        rows.append(["Debt + all leases"] + [f0(p[k]["debt_leases"]) for k in periods])
        rows.append(["Book equity (toy roll-forward)"] + [f0(p[k]["equity"]) for k in periods])
        rows.append(["(Debt + leases) / book equity"] + [fx(p[k]["debt_leases"] / p[k]["equity"]) if p[k]["equity"] > 0 else "equity <= 0" for k in periods])
        rows.append(["Share count (m): 559 + SBC + ATM"] + [fs(p[k]["shares"]) for k in periods])
        rows.append(["  ATM shares issued in period (m)"] + [fs(p[k]["atm_shares"]) for k in periods])
        rows.append(["Usable cash + securities"] + [f0(p[k]["liquidity"]) for k in periods])
        rows.append(["Deferred revenue balance"] + [f0(p[k]["deferred"]) for k in periods])
        L.append(table(["$m"] + periods, rows))
        if scn["capex_flex"]:
            L.append(f"*Capex flexed to funding: FY27 pres capex delivered {f0(p['FY27']['capex_pres'])} of {f0(p['FY27']['capex_plan'])} planned; FY28 {f0(p['FY28']['capex_pres'])} of {f0(p['FY28']['capex_plan'])}.*\n")
        t = res[n]["terminal"]
        L.append(f"**Terminal (steady state at exit-2028 run-rate {fb(res[n]['end_state']['arr'])}bn):** EBITDA {f0(t['ebitda_t'])}; replacement capex {f0(t['repl'])} (life {a(A,'useful_life_yrs'):.0f}y, residual {fp(a(A,'residual_value_pct'))}); interest {f0(t['interest_t'])}; tax {f0(t['tax_t'])}; SBC {f0(a(A,'sbc_annual'))}; **owner earnings {f0(t['owner'])}**; (EBITDA - replacement) / interest {fx(t['repl_cover_t'])}. Equity bridge: EV - debt {f0(t['debt'])} - finance leases {f0(t['fin_lease'])} + usable cash {f0(t['liquidity'])} - cost to serve deferred revenue {f0(t['deferred_cost'])}.\n")
    # residual table
    L.append("## Residual to equity (end-2028, toy)\n")
    rows = []
    for n in names:
        t = res[n]["terminal"]
        rows.append([SCENARIOS[n]["short"]] + [f"{f0(t['equity_at_mult'][m])} (${t['per_share_at_mult'][m]:,.0f})" for m in mults] + [f"{f0(t['owner_cap_equity'])} (${t['owner_cap_per_share']:,.0f})", fs(t["shares"])])
    L.append(table(["Scenario"] + [f"EV/EBITDA {m:.0f}x: equity $m (per share)" for m in mults] + [f"Owner earnings / {fp(a(A,'owner_cap_rate'))}", "Shares (m)"], rows))
    L.append("*Negative = equity is out of the money under that multiple. Per-share values use the toy share count above (559m + SBC + ATM), not a diluted count. EV/EBITDA multiples and the cap rate are ASSUMPTIONS, not market data. This is a range under stated assumptions, not a price target.*\n")
    # backlog
    L.append("## Backlog cover (diagnostic)\n")
    bl = O("backlog"); le24 = bl * O("backlog_pct_le24m"); m2548 = bl * O("backlog_pct_25_48m"); gt48 = bl * O("backlog_pct_gt48m")
    rows = [["< 24 months", fp(O("backlog_pct_le24m")), fb(le24), f"{fb(le24/2)} per year"], ["25-48 months", fp(O("backlog_pct_25_48m")), fb(m2548), f"{fb(m2548/2)} per year"], ["> 48 months", fp(O("backlog_pct_gt48m")), fb(gt48), "tenor beyond 48 months not given"]]
    L.append(table(["Bucket (slide 13 chart, read from the PDF)", "Share", "$bn", "Average"], rows))
    L.append("*Shares are 'percentage of backlog we expect to recognise in the months following quarter-end'. Backlog is RPO plus 'other amounts', subject to delivery and availability; more than 50% sits on contracts whose delivery commences by end-2026 (commencement, not recognition).*\n")
    rows = []
    for n in names:
        p = res[n]["periods"]
        cum24 = p["Q4'26"]["revenue"] + p["FY27"]["revenue"] + 0.75 * p["FY28"]["revenue"]
        rows.append([SCENARIOS[n]["short"], fb(cum24), fb(le24), f"{cum24/le24:.2f}x", fb(p["FY28"]["arr_exit"]), fb(m2548 / 2)])
    L.append(table(["Scenario", "Modelled revenue Q4'26 to Q3'28 ($bn)", "Backlog < 24m ($bn)", "Revenue / backlog", "Exit-2028 run-rate ($bn)", "Backlog 25-48m avg per year ($bn)"], rows))
    L.append("*A ratio above 1.0x means the scenario needs bookings and renewals beyond today's < 24-month backlog. The 25-48 month bucket averages well below the modelled exit run-rate, so the later years depend on renewals and new contracts. Backlog is not a revenue floor.*\n")
    # sensitivity
    bv, bo, srows = sensitivity(A)
    L.append(f"## Sensitivity (scenario 1A; equity per share at {mid:.0f}x EV/EBITDA, and owner earnings)\n")
    L.append(f"Base: **${bv:,.0f} per share**, owner earnings {f0(bo)}.\n")
    L.append(table(["Change (low / high)", "$/share, first", "$/share, second", "Owner earnings, first", "Owner earnings, second"], [(r[0], f"${r[1]:,.0f}", f"${r[2]:,.0f}", f0(r[3]), f0(r[4])) for r in srows]))
    # dilution
    L.append("## Dilution placeholders\n")
    conv_sh = O("convert_raise") / a(A, "convert_conv_price")
    rows = [["Q3 weighted-average shares (basic and diluted, official)", fs(O("q3_wtd_shares")), "Ex.99.1; a loss quarter, so converts and RSUs are anti-dilutive and excluded"],
            ["ATM, up to", fs(O("atm_shares_max")), f"OFFICIAL cap; take-up unknown; at $48.73 raises up to ${O('atm_shares_max')*price*(1-a(A,'atm_fee'))/1000:,.1f}bn net"],
            ["Convert placeholder if converted", fs(conv_sh), f"ASSUMPTION: $4.2bn / ${a(A,'convert_conv_price'):.0f}; terms not in the pack. Treated as DEBT in the model above"],
            ["Toy count end-2028, scenario 1A", fs(res[n1a]["end_state"]["shares"]), "559 + SBC $/price + ATM drawn"],
            ["Toy count end-2028, scenario 3", fs(res[n3]["end_state"]["shares"]), "stress price $34 for ATM"]]
    L.append(table(["Item", "Shares (m)", "Source / note"], rows))
    t1 = res[n1a]["terminal"]
    conv_alt = (t1["equity_at_mult"][mid] + O("convert_raise")) / (t1["shares"] + conv_sh)
    L.append(f"*If the converts were converted instead of repaid (1A at {mid:.0f}x): equity ${t1['equity_at_mult'][mid]+O('convert_raise'):,.0f}m over {fs(t1['shares']+conv_sh)}m shares = ${conv_alt:,.0f} per share, against ${t1['per_share_at_mult'][mid]:,.0f} with the notes as debt. Placeholder arithmetic only.*\n")
    # inputs
    L.append("## Inputs\n")
    L.append("### OFFICIAL (value, source)\n")
    rows = [(k, str(v[0]), v[1]) for k, v in OFFICIAL.items()]
    L.append(table(["Key", "Value", "Source"], rows).replace("---:", "---"))
    L.append("### ASSUMPTIONS (value, source)\n")
    rows = [(k, (f"{v[0]:.4g}" if isinstance(v[0], float) else str(v[0])), v[1]) for k, v in A.items() if v[0] is not None]
    L.append(table(["Key", "Value", "Source"], rows).replace("---:", "---"))
    L.append("### SCENARIO inputs\n")
    rows = []
    for n, s in SCENARIOS.items():
        rows.append((s["short"], str(s["capex_pres"]), str(s["renewal_arr_add"]), str(s["ddtl_share"]), str(s["ddtl_cap"]), str(s["parent_raise"]), str(s["lease_adds"])))
    L.append(table(["Scenario", "Pres capex", "Renewal ARR add (claim)", "DDTL share of cash capex", "DDTL cap", "Parent raise (amount, rate key)", "Lease additions"], rows).replace("---:", "---"))
    # change the answer
    L.append("## What would change the answer\n")
    for s in [
        "**Q3 10-Q debt and lease schedule**: instrument-level coupons, maturities, secured vs unsecured vs converts, covenants and the true size of 2027 maturities. The model uses current debt / total debt (22.6%) as an amortisation proxy and an effective legacy rate backed out of the Q4 interest guide.",
        "**Current bond prices and yields**: asset-level loans were said to trade near par; the unsecured 2032 yield (mid-October press report of about 15%, unverified) is used only as a stress rate in scenario 3.",
        "**Convertible terms**: conversion price, coupon, maturity, capped-call strike, and whether the $4.2bn is already in the 30 Sep debt.",
        "**Fully diluted share count**: period-end basic, RSUs, options, convert if-converted, and ATM take-up. 559m is a weighted-average placeholder.",
        "**Residual / used-GPU values and depreciation lives**: drive replacement capex and the terminal multiple; the pack gives neither. Management says depreciation 'dissipates' after contracts outlast depreciable lives.",
        "**Backlog conversion by year in dollars, customer concentration, termination rights**, and how much of the 36% < 24-month bucket is already delivering.",
        "**Cash vs presentation capex**: 9M cash PPE was 73% of the presentation series; how much of the gap is payables, finance leases and vendor financing (all debt-like) is not in the pack.",
        "**Capitalised interest**: Q4 interest guided about 30% above Q3 on similar debt suggests less capitalisation as CIP falls; the 10-Q should confirm.",
        "**Whether prepayments recur at the 2026 pace**: they are funding and deferred revenue that must be earned, not residual; the harvest case shows how they unwind.",
        "**Renewal pricing**: the call claims approaching $4bn incremental annualised revenue from 2027 renewals (about $10bn with 2028); only scenario 1B includes it, as a claim."]:
        L.append("- " + s)
    L.append("")
    open(os.path.join(HERE, "output.md"), "w").write("\n".join(L))

def main():
    res, base, st_q4, q4_range = run_all()
    vr = verify_official()
    for label, ok in vr:
        if not ok: print("CHECK FAILED:", label)
    charts(res, base, q4_range, ASSUMPTIONS)
    write_output(res, base, st_q4, q4_range, ASSUMPTIONS)
    print("checks passed: %d/%d" % (sum(ok for _, ok in vr), len(vr)))
    for n in res:
        t = res[n]["terminal"]; p = res[n]["periods"]
        print(n)
        for k in p:
            m = p[k]; print("  %-6s rev %7.0f gaapOI %6.0f int %6.0f ocf_ex %7.0f netprepay %6.0f capex %7.0f fcf_ex %8.0f fcf_incl %8.0f unfunded %6.0f debt %7.0f eq %7.0f" % (k, m["revenue"], m["gaap_oi"], m["interest"], m["ocf_ex"], m["net_prepay"], m["cash_capex"], m["fcf_ex"], m["fcf_incl"], m["unfunded"], m["debt"], m["equity"]))
        print("  owner %.0f; $/sh at 4/6/8x: %s" % (t["owner"], [round(v) for v in t["per_share_at_mult"].values()]))

if __name__ == "__main__":
    main()
