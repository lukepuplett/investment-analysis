# Orbital AI data centre — physics and cost model (Nov 2026)

## Executive summary

**BLUF: Dawn–dusk SSO can supply ~1.45 GW bus power for 1 GW IT with ~5 km² solar and ~1.4 km² two-sided radiators, but a GW cluster is **~6.5 kt** (modular cap) to **~15 kt** (physics roll-up) per year of hardware — **65–150+ Starship-class flights per GW**. Lifecycle $/GW is **$52B / $84B / $150B** (bull/base/bear) against terrestrial **$50–60B**; first-install breakeven vs $60B terrestrial is ~**$123/kg** at base mass. Baker’s public **$30B/GW** orbit figure double-counts avoided power or understates IT+launch; **$40B** is the internally consistent split.**

## Baker arithmetic (cross-check)

From [2026_11_model_inputs.md](../../analysis/2026_11_model_inputs.md) and [diary](../../diary/2026-11.md):

- Terrestrial: **$35B IT + $25B power/cooling = $60B/GW** (PROXY — Gavin Baker, TBPN 15 Jun 2026).
- Stated orbit: **$30B/GW** with **$5B/GW** launch at Starship reuse.
- **Consistent sum:** $35B IT + $5B launch = **$40B**; or $60B − $25B avoided + $5B launch = **$40B**.
- **$30B** requires an extra **$10B** omission not named on the podcast.

## Radiator physics worked example (base)

- Waste heat ≈ **1.45 GW** (IT × PUE 1.45).
- \(T = 330\) K, \(\varepsilon = 0.9\), \(f_{\mathrm{view}} = 0.85\), \(\sigma = 5.67\times10^{-8}\).
- \(q'' = 2 \varepsilon \sigma T^4 f_{\mathrm{view}} \approx 1.03\) MW/m².
- \(A \approx 1.41\) km² (matches `orbital_dc_model.py`).

At **1750 MW** bear bus power, physics radiator area crosses **1 km²** with higher temperature cap — still consistent with **Starcloud 4 km × 4 km** visual for **5 GW** (PROXY — NVIDIA blog).

## Mass, flights, cadence

See [output.md](../output.md). Base **100 t** Starship payload → **65 flights/GW**.

Scaling to Musk award narrative (**100 TW-year** non-Earth compute per 424B4) is **eight orders of magnitude** above **1.7 GW** nameplate today (HARD — input register); this model only sizes **1 GW**.

## Development capex and timeline

| Milestone | Timing | Tag |
|-----------|--------|-----|
| Orbital AI compute “as early as 2028” | 424B4 glossary | HARD |
| First **1 GW** operational | 2030–2035 | GUESS — model |
| Starship Ship reuse demonstrated | Flight 15 target Nov 2026 | PROXY |

**Cumulative Starship spend / Starlink R&D** as precedent: **NOT FOUND** audited orbital-DC line item in SPCX 10-Q.

## Sensitivity — what moves $/GW most

| Driver | Base | ±10% impact (directional) | Tag |
|--------|------|---------------------------|-----|
| IT stack $/GW | $39.2B | ±$3.9B | PROXY |
| Orbital power/thermal | $12B | ±$1.2B | GUESS |
| Launch ($5B floor vs $/kg) | $5B | dominant in bull/bear | GUESS |
| Mass cap (6.5 kt vs 15 kt physics) | 65 vs 150 flights | cadence | GUESS |

## Chart index

Generated in [../charts/](../charts/): cost waterfall, orbital vs terrestrial, breakeven $/kg, mass stack, radiator physics, cadence.

*Model: `python3 spcx/orbital/orbital_dc_model.py`.*
