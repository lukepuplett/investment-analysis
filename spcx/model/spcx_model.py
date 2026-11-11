#!/usr/bin/env python3
"""
SpaceX (SPCX) — terrestrial-only scenario model.
Orbital compute is EXCLUDED from revenue/EBIT/DCF; residual option value shown separately.

Run: python3 spcx_model.py  -> output.md + PNG charts in this directory.
Sources: spcx/analysis/2026_11_model_inputs.md, 2026_11_valuation_snapshot.md
"""
from __future__ import annotations

import math
import os
import copy

import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
YEARS = [2026, 2027, 2028, 2029, 2030]

# fmt: off
# =============================================================================
# 1. FILING (HARD) — see spcx/analysis/2026_11_model_inputs.md
# =============================================================================
F = dict(
    price_mkt=(141.30, "HARD: valuation_snapshot / Yahoo 11 Nov 2026"),
    shares_out=(13_581.0, "HARD: Q3 10-Q cover 15 Oct 2026 (millions)"),
    cash=(51_294, "HARD: 10-Q 30 Sep 2026"),
    debt=(38_006, "HARD: 10-Q Note 9 excl. finance leases"),
    apollo_lease_commit=(40_000, "HARD: 8-K GPU master lease 26 Oct 2026 aggregate principal"),
    rev_q3=(14_575, "HARD: 10-Q Note 3 Q3 2026"),
    rev_9m=(27_083, "HARD: 10-Q Note 3 9M 2026"),
    space_q3=(1_767, "HARD: 10-Q segment Q3"),
    conn_q3=(5_248, "HARD: 10-Q segment Q3"),
    si_q3=(7_560, "HARD: 10-Q segment Q3"),
    conn_consumer_q3=(3_121, "HARD: 10-Q disaggregation Q3"),
    conn_eg_q3=(2_127, "HARD: 10-Q disaggregation Q3"),
    si_infra_q3=(7_022, "HARD: 10-Q disaggregation Q3"),
    si_ads_q3=(538, "HARD: 10-Q disaggregation Q3 — xAI/X ads; not separately modeled"),
    space_9m=(3_348, "HARD: 10-Q 9M"),
    conn_9m=(12_796, "HARD: 10-Q 9M"),
    si_9m=(10_939, "HARD: 10-Q 9M"),
    opinc_q3=(2_791, "HARD: 10-Q consolidated Q3"),
    opinc_space_q3=(-7, "HARD: 10-Q segment Q3"),
    opinc_conn_q3=(2_367, "HARD: 10-Q segment Q3"),
    opinc_si_q3=(431, "HARD: 10-Q segment Q3"),
    adj_ebitda_q3=(8_809, "HARD: Q3 press release non-GAAP"),
    ni_q3=(4_404, "HARD: 10-Q Q3"),
    starlink_subs=(13.6, "HARD: Q3 press release 30 Sep 2026 (millions)"),
    starlink_arpu=(69, "HARD: Q3 press release USD/mo"),
    gw_nameplate=(1.7, "HARD: Q3 press release nameplate GW 30 Sep 2026"),
    google_fee_mo=(920, "HARD: Google FWP USD M/mo at ramp Oct 2026–Jun 2029"),
    google_gpus=(110_000, "HARD: Google FWP GPU count"),
    google_mw_proxy=(210, "HARD: 424B4 COLOSSUS II ~210 MW narrative"),
    anthropic_cap=(120_500, "HARD: Anthropic S-1/A cumulative spend cap through 2029 USD M"),
    anthropic_fee_mo_full=(3_100, "HARD: Anthropic S-1/A at full delivery USD M/mo"),
    rpo=(62_959, "HARD: 10-Q RPO 30 Sep 2026"),
    cust_a_pct=(0.166, "HARD: 10-Q concentration Q3"),
    cust_b_pct=(0.345, "HARD: 10-Q concentration Q3"),
    capex_9m=(48_069, "HARD: 10-Q cash flow PP&E 9M"),
    capex_space_q3=(1_606, "HARD: Q3 press release"),
    capex_conn_q3=(1_543, "HARD: Q3 press release"),
    capex_si_q3=(16_444, "HARD: Q3 press release"),
    ocf_9m=(13_097, "HARD: 10-Q 9M operating cash flow"),
)

# =============================================================================
# 2. ASSUMPTIONS — tagged PROXY / GUESS; scenarios Bear | Base | Bull
# =============================================================================
A = dict(
  # --- market bridge ---
  mkt_cap=(F["price_mkt"][0] * F["shares_out"][0], "HARD: price × shares (USD M; shares in millions)"),
  discount_rate=(0.11, "GUESS: terrestrial WACC; no beta filed post-IPO"),
  terminal_growth=(0.03, "GUESS: terminal FCF growth post-2030"),
  exit_pe=(25, "PROXY: valuation_snapshot reverse test ~$75B NI @ 25×"),
  stub_years=(0.25, "DERIVED: 30 Sep 2026 balance-sheet date to 31 Dec 2026; DCF/exit discounting runs from the 30 Sep net-debt date"),
  new_debt_rate=(0.07, "GUESS: cost of newly raised GPU-backed debt (same as lease_rate)"),
  funding_debt_share=(0.70, "GUESS: share of the funding need left after lease financing that is raised as debt; the rest is equity"),
  equity_issue_price=(F["price_mkt"][0], "ASSUMPTION: new equity issued at the 11 Nov 2026 price (no re-rating); dilutes the exit lens"),
  lease_finance_share=(0.35, "GUESS: share of new-GW SI capex lease-financed, like the Apollo programme"),
  lease_amort_share=(0.12, "GUESS: principal repaid in the year as a share of that year's lease draw"),
  lease_drawn_at_valuation_share=(0.15, "GUESS: share of the $40bn Apollo commitment drawn at the valuation date and by YE2026"),
  dev_share_of_space=(0.36, "PROXY: development contracts ~637/1,767 of Q3 Space revenue"),
  other_da_pct_rev=(0.04, "GUESS: Connectivity + Space D&A as % of revenue"),
  cash_yield_growth=(0.05, "GUESS: growth per year in the cash balance earning the yield"),
  terminal_capex_to_da=(1.10, "GUESS: steady-state capex / D&A used for the normalised terminal free cash flow"),
  q4_si_capex_uplift=(1.00, "GUESS: Q4 2026 SI capex as a multiple of Q3 ($16.4bn); capex leads GW"),
  si_capex_9m=(F["capex_9m"][0] - (F["capex_space_q3"][0] + F["capex_conn_q3"][0]) * 3, "PROXY: 9M capex less Q3 Space+Connectivity capex x3; opening base for SI depreciation (not HARD)"),
  tax_rate=(0.21, "GUESS: US blended statutory"),
  debt_rate=(0.055, "GUESS: weighted avg on $25B notes + other financings"),
  lease_rate=(0.07, "GUESS: Apollo GPU master lease — rate not in 8-K summary"),
  cash_yield=(0.04, "GUESS: on $51B cash"),
  corp_overhead_pct=(0.025, "GUESS: unallocated HQ; 9M SI SBC/R&D not in segments"),
  # --- capex per incremental SI GW (USD M per GW) ---
  capex_per_gw_bear=(55_000, "PROXY: Orennia ~$60B/GW top; Baker $35B IT + power"),
  capex_per_gw_base=(45_000, "PROXY: mid Orennia/Epoch range; inputs register"),
  capex_per_gw_bull=(38_000, "PROXY: Epoch ~$38B/GW grid GB200 stylized"),
  dep_years_si=(5, "GUESS: AI server depreciation vs 3–5yr industry"),
  capex_space_conn_growth=(0.08, "GUESS: non-SI capex grows with segment revenue"),
  # --- SI merchant (uncontracted) economics ---
  rev_per_gw_merchant_bear=(8_000, "PROXY: neocloud floor ~$8M/MW-yr"),
  rev_per_gw_merchant_base=(14_000, "PROXY: CoreWeave ~$6.9–8.2M/MW annualized mid-high"),
  rev_per_gw_merchant_bull=(22_000, "PROXY: short-dated CRWV ~$40M/MW upper bound scaled"),
  util_bear=(0.65, "GUESS: ramp + merchant fill lag"),
  util_base=(0.80, "GUESS: hyperscaler-style utilization"),
  util_bull=(0.88, "GUESS: tight GPU market"),
  gw_contracted_google=(0.25, "GUESS: ~210MW / 0.21GW rounded; FWP GPU count"),
  gw_contracted_anthropic_full=(1.35, "GUESS: $37.2B/yr ÷ ~$27.5B/GW implied blended contract yield"),
  # --- contracted revenue paths (USD M annual) ---
  google_annual_full=(F["google_fee_mo"][0] * 12, "HARD: 920M/mo × 12"),
  scenarios=dict(
    Bear=dict(
      sub_growth=(0.12, "GUESS: Starlink saturation / competition"),
      arpu_growth=(0.02, "GUESS: pricing pressure"),
      eg_growth=(0.10, "GUESS: enterprise/gov vs consumer"),
      conn_margin_2030=(0.42, "GUESS: glide from Q3 ~45%"),
      launches_2030=(95, "GUESS: Falcon/Starship cadence"),
      rev_per_launch=(65, "GUESS: USD M blended commercial"),
      dev_contract_growth=(0.05, "GUESS: NASA/DoD dev"),
      space_margin_2030=(0.01, "GUESS: near breakeven"),
      gw_eoy=(1.7, 2.2, 3.0, 4.0, 5.0),
      google_revenue=(11_040, 6_000, 0, 0, 0),  # cancel after 2027
      anthropic_revenue=(18_000, 22_000, 20_000, 15_000, 12_000),  # partial ramp then cut
      ads_growth=(0.12, "GUESS: xAI/X folded in SI"),
      si_margin_2030=(0.06, "GUESS: low merchant + contract cuts"),
      si_merchant_rev_gw=(8_000, "PROXY: bear merchant $/GW-yr"),
      util=(0.65, "GUESS"),
      capex_per_gw=(55_000, "PROXY"),
    ),
    Base=dict(
      sub_growth=(0.20, "GUESS: press KPI trend"),
      arpu_growth=(0.04, "GUESS: tier mix"),
      eg_growth=(0.16, "GUESS"),
      conn_margin_2030=(0.46, "GUESS"),
      launches_2030=(130, "GUESS"),
      rev_per_launch=(72, "GUESS"),
      dev_contract_growth=(0.08, "GUESS"),
      space_margin_2030=(0.03, "GUESS"),
      gw_eoy=(1.7, 3.5, 6.0, 9.0, 12.0),
      google_revenue=(11_040, 11_040, 11_040, 8_000, 0),  # thru Jun 2029 then lapse
      anthropic_revenue=(20_000, 28_000, 35_000, 37_200, 37_200),  # ramp to filed run-rate
      ads_growth=(0.22, "GUESS"),
      si_margin_2030=(0.16, "GUESS: scale + RPO recognition"),
      si_merchant_rev_gw=(14_000, "PROXY"),
      util=(0.80, "GUESS"),
      capex_per_gw=(45_000, "PROXY"),
    ),
    Bull=dict(
      sub_growth=(0.28, "GUESS: global penetration"),
      arpu_growth=(0.06, "GUESS: premium tiers"),
      eg_growth=(0.22, "GUESS"),
      conn_margin_2030=(0.48, "GUESS"),
      launches_2030=(165, "GUESS: Starship commercial"),
      rev_per_launch=(80, "GUESS"),
      dev_contract_growth=(0.10, "GUESS"),
      space_margin_2030=(0.05, "GUESS"),
      gw_eoy=(1.7, 5.0, 10.0, 18.0, 28.0),
      google_revenue=(11_040, 11_040, 11_040, 11_040, 11_040),  # extend ASSUMPTION
      anthropic_revenue=(22_000, 32_000, 37_200, 37_200, 40_000),  # cap + modest upside
      ads_growth=(0.35, "GUESS"),
      si_margin_2030=(0.24, "GUESS: merchant + util"),
      si_merchant_rev_gw=(22_000, "PROXY"),
      util=(0.88, "GUESS"),
      capex_per_gw=(38_000, "PROXY"),
    ),
  ),
  # FY2026 Q4 bridge (shared): 9M actual + modelled Q4
  q4_si_uplift=(1.00, "GUESS: Q4 SI ~ Q3 run-rate after ramp"),
  q4_conn_uplift=(1.03, "GUESS: holiday subscriber adds"),
  q4_space_uplift=(1.05, "GUESS: launch cadence"),
)

# fmt: on


def lin(start: float, end: float, i: int, n: int = 4) -> float:
    return start + (end - start) * i / n


def connectivity_annual(sc: dict, year: int, subs: float, arpu: float, eg_annual: float) -> tuple[float, float, float, float]:
    """Returns revenue, ebit, subs, arpu (end of year state)."""
    if year == 2026:
        q4_c = F["conn_consumer_q3"][0] * A["q4_conn_uplift"][0]
        q4_e = F["conn_eg_q3"][0] * A["q4_conn_uplift"][0]
        rev = F["conn_9m"][0] + q4_c + q4_e
        ebit = F["opinc_conn_q3"][0] * (rev / (F["conn_q3"][0] * 4))  # scale Q3 margin
    else:
        subs = subs * (1 + sc["sub_growth"][0])
        arpu = arpu * (1 + sc["arpu_growth"][0])
        consumer = subs * arpu * 12  # $M: subs in millions
        eg_annual = eg_annual * (1 + sc["eg_growth"][0])
        rev = consumer + eg_annual
        m0 = F["opinc_conn_q3"][0] / F["conn_q3"][0]
        m = lin(m0, sc["conn_margin_2030"][0], year - 2026)
        ebit = rev * m
    return rev, ebit, subs, arpu


def space_annual(sc: dict, year: int, dev_base: float) -> tuple[float, float, float]:
    if year == 2026:
        rev = F["space_9m"][0] + F["space_q3"][0] * A["q4_space_uplift"][0]
        ebit = F["opinc_space_q3"][0] * (rev / (F["space_q3"][0] * 4))
        dev_base = F["space_q3"][0] * A["dev_share_of_space"][0]
    else:
        launches = lin(F["space_q3"][0] * 0.64 / sc["rev_per_launch"][0], sc["launches_2030"][0], year - 2026)
        launch_rev = launches * sc["rev_per_launch"][0]
        dev_rev = F["space_q3"][0] * A["dev_share_of_space"][0] * 4 * (1 + sc["dev_contract_growth"][0]) ** (year - 2026)
        rev = launch_rev + dev_rev
        m0 = F["opinc_space_q3"][0] / F["space_q3"][0]
        m = lin(m0, sc["space_margin_2030"][0], year - 2026)
        ebit = rev * m
    return rev, ebit, dev_base


def si_annual(sc: dict, year: int, ads: float) -> tuple[float, float, float, float]:
    """SI revenue = contracted + merchant + ads (xAI/X). Returns rev, ebit, gw, ads."""
    ix = year - 2026
    gw = sc["gw_eoy"][ix] if ix < len(sc["gw_eoy"]) else sc["gw_eoy"][-1]
    google = sc["google_revenue"][ix] if ix < len(sc["google_revenue"]) else 0
    anthropic = sc["anthropic_revenue"][ix] if ix < len(sc["anthropic_revenue"]) else 0
    contracted_gw = min(gw, A["gw_contracted_google"][0] + A["gw_contracted_anthropic_full"][0])
    merchant_gw = max(0.0, gw - contracted_gw)
    merchant_rev = merchant_gw * sc["util"][0] * sc["si_merchant_rev_gw"][0]
    if year == 2026:
        q4 = (F["si_q3"][0] * A["q4_si_uplift"][0])
        rev = F["si_9m"][0] + q4
        # reconcile: don't double-count — use actual 9M+Q4 path
        ebit = F["opinc_si_q3"][0] * (rev / (F["si_q3"][0] * 4))
        ads = F["si_ads_q3"][0] * 4
    else:
        ads = ads * (1 + sc["ads_growth"][0])
        rev = google + anthropic + merchant_rev + ads
        m0 = F["opinc_si_q3"][0] / F["si_q3"][0]
        m = lin(m0, sc["si_margin_2030"][0], year - 2026)
        ebit = rev * m
    return rev, ebit, gw, ads


def net_debt_at_valuation() -> float:
    """Existing claims at the 30 Sep 2026 balance-sheet date: debt + Apollo lease drawn - cash.
    The undrawn lease commitment is future financing of capex that the DCF already charges, so it is not subtracted."""
    return F["debt"][0] + F["apollo_lease_commit"][0] * A["lease_drawn_at_valuation_share"][0] - F["cash"][0]


def project_scenario(name: str, sc: dict | None = None) -> list[dict]:
    sc = sc or A["scenarios"][name]
    subs, arpu = F["starlink_subs"][0], F["starlink_arpu"][0]
    eg_annual = F["conn_eg_q3"][0] * 4
    dev_base = F["space_q3"][0] * A["dev_share_of_space"][0]
    ads = F["si_ads_q3"][0] * 4
    gw_prev = F["gw_nameplate"][0]
    si_capex_cum = A["si_capex_9m"][0]
    lease_bal = F["apollo_lease_commit"][0] * A["lease_drawn_at_valuation_share"][0]
    new_debt = 0.0
    shares = F["shares_out"][0]
    rows = []
    for i, y in enumerate(YEARS):
        c_rev, c_ebit, subs, arpu = connectivity_annual(sc, y, subs, arpu, eg_annual)
        eg_annual = F["conn_eg_q3"][0] * 4 * (1 + sc["eg_growth"][0]) ** max(0, y - 2026)
        s_rev, s_ebit, dev_base = space_annual(sc, y, dev_base)
        si_rev, si_ebit, gw, ads = si_annual(sc, y, ads)
        rev = c_rev + s_rev + si_rev
        corp = rev * A["corp_overhead_pct"][0]
        ebit = c_ebit + s_ebit + si_ebit - corp
        new_gw = max(0.0, gw - gw_prev)
        si_capex = new_gw * sc["capex_per_gw"][0]
        other_capex = (F["capex_space_q3"][0] + F["capex_conn_q3"][0]) * (1 + A["capex_space_conn_growth"][0]) ** i * 4
        q4_si_capex = F["capex_si_q3"][0] * A["q4_si_capex_uplift"][0] if y == 2026 else 0.0
        if y == 2026:
            q4_capex = q4_si_capex + other_capex * 0.25
            capex = F["capex_9m"][0] + si_capex + q4_capex
        else:
            q4_capex = None
            capex = si_capex + other_capex
        da = (si_capex_cum / A["dep_years_si"][0]) + rev * A["other_da_pct_rev"][0]
        int_inc = F["cash"][0] * A["cash_yield"][0] * (1 + A["cash_yield_growth"][0] * i)
        lease_draw = si_capex * A["lease_finance_share"][0]
        lease_repay = lease_draw * A["lease_amort_share"][0]
        lease_net = lease_draw - lease_repay
        # interest depends on in-year debt draws, which depend on the funding need: iterate to a fixed point
        draw_debt = 0.0
        for _ in range(100):
            int_exp = (F["debt"][0] * A["debt_rate"][0]
                       + (new_debt + 0.5 * draw_debt) * A["new_debt_rate"][0]
                       + (lease_bal + 0.5 * lease_net) * A["lease_rate"][0])
            pbt = ebit + int_inc - int_exp
            tax = max(0.0, pbt) * A["tax_rate"][0]
            ni = pbt - tax
            fcf = ni + da - capex
            # 2026: the 9M spend was funded before the valuation date; only Q4 needs new financing
            fcf_to_fund = (ni + da) * 0.25 - q4_capex if y == 2026 else fcf
            need = max(0.0, -fcf_to_fund - lease_net)
            new_draw = A["funding_debt_share"][0] * need
            if abs(new_draw - draw_debt) < 1e-6:
                break
            draw_debt = new_draw
        equity_raised = need - draw_debt
        shares += equity_raised / A["equity_issue_price"][0]
        new_debt += draw_debt
        lease_bal += lease_net
        si_capex_cum += si_capex + q4_si_capex
        nopat = ebit - max(0.0, ebit) * A["tax_rate"][0]
        ufcf = nopat + da - capex
        q4_ufcf = (nopat + da) * 0.25 - q4_capex if y == 2026 else None
        rows.append(dict(
            year=y, revenue=rev, conn_rev=c_rev, space_rev=s_rev, si_rev=si_rev,
            ebit=ebit, ebit_m=ebit / rev if rev else 0, da=da, ni=ni, capex=capex, fcf=fcf,
            ufcf=ufcf, q4_ufcf=q4_ufcf, funding_need=need, debt_raised=draw_debt, equity_raised=equity_raised,
            new_debt_cum=new_debt, shares_eoy=shares, gw=gw, int_exp=int_exp, tax=tax,
        ))
        gw_prev = gw
    return rows


def years_to_exit() -> float:
    return A["stub_years"][0] + (YEARS[-1] - 2026)


def terrestrial_ev_dcf(rows: list[dict]) -> float:
    """Unlevered DCF at the 30 Sep 2026 balance-sheet date: Q4'26 stub, FY27-30 mid-year, normalised terminal value."""
    r, g = A["discount_rate"][0], A["terminal_growth"][0]
    if r <= g:
        raise ValueError("Unable to run the DCF. discount_rate must exceed terminal_growth.")
    stub = A["stub_years"][0]
    pv = rows[0]["q4_ufcf"] / (1 + r) ** (stub / 2)
    for row in rows[1:]:
        pv += row["ufcf"] / (1 + r) ** (stub + (row["year"] - 2027) + 0.5)
    last = rows[-1]
    nopat = last["ebit"] - max(0.0, last["ebit"]) * A["tax_rate"][0]
    ufcf_norm = nopat + last["da"] * (1 - A["terminal_capex_to_da"][0])
    tv = ufcf_norm * (1 + g) / (r - g)
    return pv + tv / (1 + r) ** years_to_exit()


def terrestrial_equity_value(rows: list[dict]) -> tuple[float, float, float]:
    """Returns (dcf_equity, exit_pv_equity, blend), USD M attributable to today's shareholders.
    DCF: unlevered EV less net debt at the valuation date. Exit: 2030 NI (after all interest) x P/E, discounted,
    scaled for shares issued to fund the gap. Neither lens subtracts debt twice."""
    dcf_equity = terrestrial_ev_dcf(rows) - net_debt_at_valuation()
    last = rows[-1]
    exit_mcap = max(0.0, last["ni"]) * A["exit_pe"][0]
    exit_pv = exit_mcap / (1 + A["discount_rate"][0]) ** years_to_exit() * (F["shares_out"][0] / last["shares_eoy"])
    return dcf_equity, exit_pv, 0.5 * dcf_equity + 0.5 * exit_pv


def md_table(headers, rows):
    s = "| " + " | ".join(headers) + " |\n|" + "|".join(["---"] * len(headers)) + "|\n"
    for r in rows:
        s += "| " + " | ".join(str(x) for x in r) + " |\n"
    return s


fb = lambda x: f"{x/1000:,.1f}"
fp = lambda x: f"{x*100:.1f}%"
fm = lambda x: f"{x:,.0f}"
ft = lambda x: f"${x/1e6:,.2f}tn" if x >= 1e6 else f"${x/1e3:,.0f}bn"


def sensitivity_2030_value(rev_per_gw: float, gw: float) -> float:
    """Exit-lens PV per current share (USD) from a full Base-case run with merchant $/GW-yr and 2030 GW overridden.
    GW ramps linearly from nameplate to the 2030 level; funding cost and dilution are included."""
    sc = copy.deepcopy(A["scenarios"]["Base"])
    gw0 = F["gw_nameplate"][0]
    n = len(YEARS) - 1
    sc["gw_eoy"] = tuple(gw0 + (gw - gw0) * i / n for i in range(len(YEARS)))
    sc["si_merchant_rev_gw"] = (rev_per_gw, "sensitivity override")
    _, exit_pv, _ = terrestrial_equity_value(project_scenario("Base", sc))
    return exit_pv / F["shares_out"][0]


def main():
    lo_price = F["price_mkt"][0]
    out = []
    out.append("# SPCX terrestrial model output\n\n")
    out.append("**Scope:** Earth-only (Starlink, launch, terrestrial Super Intelligence). ")
    out.append("Orbital compute is **excluded**; residual = market cap minus terrestrial value.\n\n")
    out.append(f"Market reference: **${lo_price:.2f}/share**, {F['shares_out'][0]/1000:.3f}bn shares, ")
    out.append(f"~{ft(F['price_mkt'][0]*F['shares_out'][0])} market cap ([valuation_snapshot](../analysis/2026_11_valuation_snapshot.md)).\n\n")
    out.append("Run `python3 spcx_model.py`. Inputs: `FILING` / `ASSUMPTIONS` at top of script; ")
    out.append("register: [2026_11_model_inputs.md](../analysis/2026_11_model_inputs.md).\n\n")
    out.append("**xAI / X:** SI advertising ($538M/qtr HARD) grows inside SI; Grok subscription not separable in 10-Q — folded into SI ads line.\n\n")

    results = {n: project_scenario(n) for n in A["scenarios"]}

    out.append("## 1. Segment revenue & profit (terrestrial)\n\n")
    for sname, rows in results.items():
        tbl = []
        for key, label, fmt in [
            ("revenue", "Total revenue", fb), ("conn_rev", "  Connectivity", fb),
            ("space_rev", "  Space", fb), ("si_rev", "  Super Intelligence", fb),
            ("ebit", "EBIT (after corp overhead)", fb), ("ebit_m", "  EBIT margin", fp),
            ("capex", "Capex", fb), ("fcf", "FCF", fb), ("ufcf", "Unlevered FCF", fb), ("funding_need", "  Funding need after lease (2026 = Q4 only)", fb),
            ("new_debt_cum", "  New debt outstanding (cum)", fb), ("equity_raised", "  Equity issued", fb),
            ("shares_eoy", "  Shares (m, after issuance)", lambda x: f"{x:,.0f}"),
            ("gw", "SI nameplate GW (EOY)", lambda x: f"{x:.1f}"),
        ]:
            tbl.append([label] + [fmt(r[key]) for r in rows])
        out.append(f"### {sname}\n\n")
        out.append(md_table(["Line"] + [f"{y}E" for y in YEARS], tbl) + "\n")

    out.append("## 2. Contracted vs uncontracted SI (Base)\n\n")
    sc = A["scenarios"]["Base"]
    rows_c = []
    for i, y in enumerate(YEARS):
        ix = i
        g = sc["google_revenue"][ix]
        an = sc["anthropic_revenue"][ix]
        gw = sc["gw_eoy"][ix]
        merch = max(0, gw - 1.6) * sc["util"][0] * sc["si_merchant_rev_gw"][0]
        rows_c.append([y, fm(g), fm(an), fm(merch), f"{gw:.1f}", fm(g + an + merch)])
    out.append(md_table(["Year", "Google (M)", "Anthropic (M)", "Merchant SI (M)", "GW", "Contract+merchant"], rows_c))
    out.append("\nRPO **$62.96B** HARD supports recognition timing; bear case cuts Google after 2027 and trims Anthropic (90-day cancel rights after 2027 — HARD in Anthropic S-1/A / Google FWP).\n\n")

    out.append("## 3. Terrestrial valuation vs $141.30 market\n\n")
    val_rows = []
    orbitals = {}
    mkt_cap = A["mkt_cap"][0]
    for sname, rows in results.items():
        dcf_eq, exit_pv, blend = terrestrial_equity_value(rows)
        sh = F["shares_out"][0]
        px_dcf = dcf_eq / sh
        px_exit = exit_pv / sh
        px_blend = blend / sh
        orbital = mkt_cap - blend
        orbitals[sname] = orbital
        val_rows.append([
            sname, f"${px_dcf:.1f}", f"${px_exit:.1f}", f"${px_blend:.1f}",
            f"${lo_price:.2f}", f"{(px_blend/lo_price-1)*100:+.0f}%",
            ft(orbital) + " implied orbital/option",
        ])
    out.append(md_table(["Scenario", "DCF equity/sh", "Exit 25×2030 NI PV/sh", "Blended 50/50", "Market", "Blended vs mkt", "Orbital residual"], val_rows))
    out.append(f"\n*Method: DCF is unlevered, at the 30 Sep 2026 balance-sheet date (Q4'26 stub, FY27-30 mid-year, normalised terminal), less net debt {fm(net_debt_at_valuation())}M (debt + drawn lease - cash). Exit lens is 2030 NI x {A['exit_pe'][0]}x, discounted {years_to_exit():.2f} years and scaled for shares issued to fund the gap. The funding gap is financed {A['funding_debt_share'][0]*100:.0f}% debt at {A['new_debt_rate'][0]*100:.0f}% and the rest equity at ${A['equity_issue_price'][0]:.2f}.*\n")
    out.append("\n**Implied value left for orbital/option** = market cap − terrestrial blended equity (per scenario). ")
    out.append("Negative terrestrial blended ⇒ market already prices orbital/out-of-model upside in bull segments.\n\n")

    out.append("## 4. Sensitivity — 2030 exit value per share ($) vs revenue/GW-yr × GW deployed\n\n")
    gw_grid = [5, 8, 12, 18, 28]
    rev_grid = [8, 12, 16, 20, 24]
    hdr = ["rev\\GW"] + [f"{g} GW" for g in gw_grid]
    sens = []
    for rv in rev_grid:
        sens.append([f"${rv}B/GW-yr"] + [f"${sensitivity_2030_value(rv*1000, g):.0f}" for g in gw_grid])
    out.append(md_table(hdr, sens))
    out.append("\nCells: exit-lens PV per current share from a full Base-case run (25× 2030 NI, funding cost and dilution included), with 2030 GW and merchant $/GW-yr overridden and GW ramping linearly from 1.7. Merchant GW = deployed − 1.6 contracted.\n\n")

    out.append("## 5. Funding & financing hooks\n\n")
    out.append(f"- **Debt** {fm(F['debt'][0])}M HARD; **cash** {fm(F['cash'][0])}M HARD.\n")
    out.append(f"- **Apollo GPU lease** up to {fm(F['apollo_lease_commit'][0])}M principal HARD (8-K); model assumes gradual draw with SI capex.\n")
    out.append(f"- **9M capex** {fm(F['capex_9m'][0])}M HARD; SI dominated ({fm(F['capex_si_q3'][0])}M/qtr Q3).\n")
    cum_fund = {s: sum(r["funding_need"] for r in results[s]) for s in results}
    cum_debt = {s: sum(r["debt_raised"] for r in results[s]) for s in results}
    out.append("- Cumulative funding need after lease financing, Q4'26 to 2030: " +
               ", ".join(f"{s} ${cum_fund[s]/1000:.0f}bn (debt ${cum_debt[s]/1000:.0f}bn, equity ${(cum_fund[s]-cum_debt[s])/1000:.0f}bn)" for s in results) + " (GUESS capex, lease and debt/equity splits). It carries interest and dilution in the valuation above.\n\n")

    out.append("## 6. Three biggest drivers (terrestrial vs $141.30)\n\n")
    out.append("1. **GW deployed × $/GW-year (merchant + contract utilization)** — filings anchor Google $11B/yr and Anthropic ~$37B/yr at full delivery, but only **1.7 GW** nameplate today (HARD). Bull case needs 10–28 GW terrestrial by 2030 (GUESS) at neocloud-to-hyperscaler yields.\n")
    out.append("2. **Capex per GW and lease/debt funding** — $38–55B/GW proxies (PROXY) × GW delta drives FCF deeply negative; Apollo **~$40B** lease (HARD) not fully on balance sheet yet.\n")
    out.append("3. **Starlink profit vs SI ramp** — Q3 op income is **$2.37B/qtr Connectivity vs $0.43B SI** (HARD); market at ~33× run-rate sales prices SI growth contracts already partially in revenue (Customer A/B 51% of Q3 rev, HARD).\n\n")

    path = os.path.join(HERE, "output.md")
    open(path, "w", encoding="utf-8").write("\n".join(out))
    charts(results, orbitals)
    print("\n".join(out))
    return results, orbitals


def charts(results, orbitals):
    plt.rcParams.update({"font.size": 11})
    cols = {"Bear": "#C44E52", "Base": "#4C72B0", "Bull": "#55A868"}
    # revenue scenarios
    fig, ax = plt.subplots(figsize=(10, 6))
    for s, rows in results.items():
        ys = [r["revenue"] / 1000 for r in rows]
        ax.plot(YEARS, ys, marker="o", label=s, color=cols[s], lw=2)
        ax.annotate(f"\\${ys[-1]:.0f}bn", (2030, ys[-1]), textcoords="offset points", xytext=(6, 0), fontsize=9, color=cols[s])
    ax.axhline(F["rev_q3"][0] * 4 / 1000, ls="--", color="grey", label="Q3 × 4 run rate")
    ax.set_ylabel("Revenue ($bn)")
    ax.set_title("SPCX terrestrial revenue scenarios (no orbital)")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "revenue_scenarios.png"), dpi=130)
    plt.close(fig)

    # valuation per share
    fig, ax = plt.subplots(figsize=(9, 6))
    mkt = F["price_mkt"][0]
    names, vals = [], []
    for s, rows in results.items():
        _, _, blend = terrestrial_equity_value(rows)
        px = blend / F["shares_out"][0]
        names.append(s)
        vals.append(px)
    bars = ax.bar(names, vals, color=[cols[n] for n in names], edgecolor="black")
    ax.axhline(mkt, color="black", ls="--", lw=2, label=f"Market ${mkt:.2f}")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 3, f"\\${v:.0f}", ha="center", fontsize=10)
    ax.set_ylabel("$ per share (terrestrial blended)")
    ax.set_title("Terrestrial blended value vs market (50% DCF / 50% exit 25×)")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "valuation_per_share.png"), dpi=130)
    plt.close(fig)

    # sensitivity heatmap
    gw_grid = np.array([5, 8, 12, 18, 28])
    rev_grid = np.array([8, 12, 16, 20, 24])
    Z = np.array([[sensitivity_2030_value(rv * 1000, g) for g in gw_grid] for rv in rev_grid])
    fig, ax = plt.subplots(figsize=(9, 6))
    im = ax.imshow(Z, cmap="YlGnBu", aspect="auto")
    ax.set_xticks(range(len(gw_grid)))
    ax.set_xticklabels([f"{g}" for g in gw_grid])
    ax.set_yticks(range(len(rev_grid)))
    ax.set_yticklabels([f"{r}" for r in rev_grid])
    ax.set_xlabel("GW deployed (2030)")
    ax.set_ylabel("Revenue per GW-yr ($bn)")
    ax.set_title("Sensitivity: stylized 2030 equity value per share ($)")
    for i in range(len(rev_grid)):
        for j in range(len(gw_grid)):
            ax.text(j, i, f"\\${Z[i,j]:.0f}", ha="center", va="center", fontsize=8)
    fig.colorbar(im, ax=ax, label="$/share")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "sensitivity_gw_rev.png"), dpi=130)
    plt.close(fig)

    # orbital residual
    fig, ax = plt.subplots(figsize=(8, 5))
    mkt_cap = A["mkt_cap"][0] / 1000  # $bn
    ter = []
    for s in names:
        _, _, blend = terrestrial_equity_value(results[s])
        ter.append(blend / 1000)
    residual = [mkt_cap - t for t in ter]
    x = np.arange(3)
    w = 0.35
    ax.bar(x - w / 2, ter, w, label="Terrestrial blended", color="#4C72B0")
    ax.bar(x + w / 2, residual, w, label="Implied orbital/option", color="#C44E52")
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.set_ylabel("$ trillions")
    ax.set_title("Market cap split: terrestrial model vs implied orbital residual")
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "orbital_residual.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    main()
