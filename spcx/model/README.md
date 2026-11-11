# SPCX terrestrial scenario model (Nov 2026)

`python3 spcx_model.py` writes **`output.md`** and four charts:

| Chart | Description |
|-------|-------------|
| `revenue_scenarios.png` | Bear / Base / Bull terrestrial revenue 2026–2030 |
| `valuation_per_share.png` | Blended terrestrial value vs $141.30 market |
| `sensitivity_gw_rev.png` | 2030 exit value per share vs $/GW-yr × GW |
| `orbital_residual.png` | Market cap split: terrestrial vs implied orbital/option |

All inputs are in **`FILING`** (HARD, with source tags) and **`ASSUMPTIONS`** (PROXY/GUESS) at the top of **`spcx_model.py`**, cross-walked to [../analysis/2026_11_model_inputs.md](../analysis/2026_11_model_inputs.md). Units: **USD millions**; Starlink subscribers in **millions**; GW nameplate for Super Intelligence.

## Scope

**On Earth only:** Connectivity (Starlink consumer × ARPU + enterprise/government), Space (launch count × price + development contracts), and **terrestrial** Super Intelligence (contracted Google/Anthropic revenue + merchant GW × $/GW-yr + advertising). **Orbital compute is excluded** from revenue, EBIT, capex, and DCF. The model reports:

> **Implied value left for orbital/option = market cap − terrestrial blended equity**

per [valuation snapshot](../analysis/2026_11_valuation_snapshot.md) framing.

**xAI / X:** Q3 SI advertising **$538M/qtr** (HARD) grows inside SI. Grok subscriptions are not segment-disclosed in the 10-Q and are folded into SI with a note—not modeled separately.

## What is HARD in the script

- Q3 / 9M segment revenue and operating income; 1.7 GW nameplate; Starlink 13.6M subs @ $69 ARPU.
- Google **$920M/mo**; Anthropic **~$3.1B/mo** at full delivery; RPO **$62.96B**; debt/cash; Apollo **~$40B** lease commitment (8-K).
- Market reference **$141.30**, **13.581B** shares (~**$1.92T** cap).

## Scenario structure

| Segment | Bear | Base | Bull |
|---------|------|------|------|
| Starlink | Slower subs/ARPU; margin 42% by 2030 | KPI-linked growth; 46% margin | Aggressive penetration; 48% margin |
| Space | ~95 launches/2030; ~breakeven | 130 launches; low positive margin | 165 launches; Starship-scale |
| SI GW (EOY) | 1.7→5.0 | 1.7→12.0 | 1.7→28.0 |
| Contracts | Google cancels 2028+; Anthropic trimmed | Google thru Jun 2029; Anthropic to $37.2B/yr | Full contracts + renewals |
| Capex/GW | $55B (PROXY high) | $45B | $38B (PROXY low) |

FY**2026** = **9M actual** (HARD) + modelled **Q4** (GUESS uplifts on Q3 run-rates).

## Valuation method

1. **DCF** — unlevered free cash flow (EBIT after tax + D&A − capex), valued at the **30 Sep 2026** balance-sheet date: a Q4'26 stub, FY27–30 at mid-year, and a terminal value on a **normalised** 2030 cash flow (capex = 1.1× D&A, 3% growth), discounted at 11% (GUESS WACC).
2. **Exit multiple** — **25×** 2030 NI (after all interest, including interest on funding raised), PV'd 4.25 years at 11%, scaled for shares issued to fund the gap.
3. **Net debt (DCF only)** — debt + the *drawn* part of the Apollo lease (GUESS 15%) − cash. The undrawn lease is future financing of capex the DCF already charges, so it is not subtracted. The exit lens is already after interest and is not reduced by net debt.
4. **Funding gap** — after lease financing (35% of new-GW capex), the remaining need is raised 70% as debt at 7% and 30% as equity at $141.30; interest and dilution flow into net income and the share count. For 2026 only Q4 needs new financing.
5. **Blended** — 50% DCF equity + 50% exit PV, per current share (13.581B).

Terrestrial DCF is heavily negative in early years because SI capex is modeled gross per GW (HARD 9M capex pace + PROXY $/GW). Treat the blend as **scenario equity for filed-Earth businesses**, not a price target.

## Sensitivity

Section 4 of `output.md`: exit-lens value per current share from a **full Base-case run** per cell, with 2030 **GW deployed** and **merchant revenue per GW-year** overridden (GW ramps linearly from 1.7), so funding cost and dilution are included.

## Caveats (read before quoting numbers)

- **Customer A/B** unnamed in 10-Q; Google and Anthropic mapped from FWPs / Anthropic S-1 (PROXY identity).
- **GW per contract** is GUESS; Anthropic dollars do not disclose MW/GW at full run-rate.
- **Apollo lease** rate and draw schedule are GUESS; 8-K only states aggregate principal.
- **No orbital revenue or capex** — residual is a plug vs $141.30, not a priced orbital DCF.
- Musk **$100B Dec ARR** / **$500B–$1T 2027** guides: **NOT FOUND** in saved primaries (per inputs register); not used.
- DCF and FCF omit working capital, exact lease amortization, and SBC (material in 9M NI).
- Q4 2026 SI capex is set to the Q3 level ($16.4bn, GUESS); the 9M SI capex base for depreciation is a proxy (9M capex less Space/Connectivity), not a filed figure.
- All formerly in-function constants (lease split, D&A %, development share, etc.) now live in `ASSUMPTIONS`.

## Related files

- [../analysis/2026_11_model_inputs.md](../analysis/2026_11_model_inputs.md) — input register
- [../analysis/2026_11_valuation_snapshot.md](../analysis/2026_11_valuation_snapshot.md) — market multiples and reverse test
- Template style: [../../ant/model/README.md](../../ant/model/README.md)
