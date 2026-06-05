# Model Architecture: Transport vs. Platform

Original model assumes **transport business**. Market prices **platform outcome**. These require different assumptions in every dimension.

| Dimension | **Transport Model (Regime A)** | **Platform Model (Regime C)** |
|-----------|-------------------------------|-------------------------------|
| **Demand origin** | Fixed rideshare pool (~5% of miles) | Ownership replacement (50%+ of miles) |
| **Elasticity** | 1.35–2.25x | 10–25x (kids, elderly, delivery, logistics) |
| **Trips/capita** | 12–45/yr | 150–300+/yr |
| **Approval path** | Metro-by-metro linear, 3–6%/yr | S-curve inflection → exponential, <10 yrs to 50%+ |
| **Cross-metro leverage** | Zero (SF approval ≠ Phoenix) | High (stack generalizes across regions) |
| **Capex/vehicle** | Stable $40–60k | Declining 20–30%+/yr |
| **Opex/mile** | Stable by metro | Declining 30%+/yr (software scaling) |
| **Take-rate** | 18–32% (Uber competition) | 40–65% (lock-in + necessity) |
| **Fleet economics** | Per-vehicle FCF, local utilization | Fleet-wide FCF improves with scale |
| **Market structure** | Duopoly/oligopoly, both survive | Winner-take-most or rapid bifurcation |
| **Moat source** | Regulatory approval parity | Software scaling, cost curve compounding |
| **Survival condition** | Both scale at similar pace | One player 70%+; second trapped |
| **Valuation comparable** | Uber 8x, transport logistics 9–18x | Salesforce/ServiceNow 15–50x, platform monopoly 50–150x |
| **Terminal value (Waymo)** | $30–90B | $2–10T |
| **Scaling behavior** | Linear (each metro independently) | Exponential (cost decline + approval + utilization compound) |
| **Labor/political risk** | Moderate (driver displacement) | Binary (full support or full opposition) |
| **Success condition** | Both Waymo + Tesla survive and scale | One player dominates; other dies or occupies niche |

**Decision:** Track ownership substitution % through 2027. <10% by Q4 2027 → accept transport model. 15%+ → shift to platform model. See `REGIME_INDICATORS.md`.
