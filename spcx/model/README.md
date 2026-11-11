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

1. **DCF** — discount annual FCF 2027–2030 at 11% (GUESS WACC); terminal on 2030 FCF (Gordon) or **25×** 2030 NI if FCF still negative.
2. **Exit multiple** — **25×** 2030 NI (same anchor as reverse test in valuation snapshot), PV’d four years at 11%.
3. **Blended** — 50% DCF equity + 50% exit PV, both net of **debt + full Apollo lease − cash** (PROXY balance-sheet bridge).
4. **Per share** — blended equity ÷ 13.581B shares.

Terrestrial DCF is heavily negative in early years because SI capex is modeled gross per GW (HARD 9M capex pace + PROXY $/GW). Treat the blend as **scenario equity for filed-Earth businesses**, not a price target.

## Sensitivity

Section 4 of `output.md`: stylized **2030** exit per share vs **merchant revenue per GW-year** and **GW deployed**, holding Base Starlink/Space and full Google/Anthropic contract fees.

## Caveats (read before quoting numbers)

- **Customer A/B** unnamed in 10-Q; Google and Anthropic mapped from FWPs / Anthropic S-1 (PROXY identity).
- **GW per contract** is GUESS; Anthropic dollars do not disclose MW/GW at full run-rate.
- **Apollo lease** rate and draw schedule are GUESS; 8-K only states aggregate principal.
- **No orbital revenue or capex** — residual is a plug vs $141.30, not a priced orbital DCF.
- Musk **$100B Dec ARR** / **$500B–$1T 2027** guides: **NOT FOUND** in saved primaries (per inputs register); not used.
- DCF and FCF omit working capital, exact lease amortization, and SBC (material in 9M NI).

## Related files

- [../analysis/2026_11_model_inputs.md](../analysis/2026_11_model_inputs.md) — input register
- [../analysis/2026_11_valuation_snapshot.md](../analysis/2026_11_valuation_snapshot.md) — market multiples and reverse test
- Template style: [../../ant/model/README.md](../../ant/model/README.md)
