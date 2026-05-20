# Model Architecture: Transport vs. Platform

Original model assumes **transport business**. Market prices **platform outcome**. These require different assumptions in every dimension.

---

## 1. Demand Modeling

| Aspect | **Transport Model (Regime A)** | **Platform Model (Regime C)** |
|--------|------|------|
| **Trip Origin** | Fixed pool (rideshare users, ~5% of miles) | Ownership replacement pool (50%+ of miles) |
| **Elasticity** | Modest 1.35–2.25x | Massive 10–25x (new categories: kids, elderly, delivery, subsidy-dependent) |
| **Induced Demand** | "Rideshare available → I use it more" | "Own car ↔ robotaxi → life rewires (no commute, urban sprawl collapse, logistics reimagined)" |
| **New Use Cases** | None (rides only) | Logistics (30%+ of miles), delivery, ads, subsidized transport |
| **Geography** | Dense metro + affluent suburbs | Urban density + rural accessibility (ownership collapse enables sparse deployment) |

**Model Implication:**
- Transport: Trips/capita 12–45 (anchored to rideshare behavior)
- Platform: Trips/capita 150–300+ (ownership replacement unlocks new categories)

---

## 2. Geography & Deployment

| Aspect | **Transport Model** | **Platform Model** |
|--------|---|---|
| **Approval Path** | Metro-by-metro + local politics | S-curve inflection (stalled → sudden exponential) |
| **Geofence Model** | Heavy (strict service area per metro) | Minimal (stack scales across regions, geofences optional) |
| **Cross-Metro Leverage** | Zero (SF approval ≠ Phoenix approval) | High (FSD/Waymo improvements in SF scale to Phoenix, LA, etc.) |
| **Regulatory Timeline** | 3–6%/year linear (1–2 metros/year for 15 years) | <10 years to 50%+ approval (S-curve inflection 2028–2030) |

**Model Implication:**
- Transport: Expansion is capital-limited and regulatory-gated
- Platform: Expansion is software-limited; capital scales with software

---

## 3. Unit Economics

| Aspect | **Transport Model** | **Platform Model** |
|--------|---|---|
| **Capex/Vehicle** | Stable (~$40–60k per vehicle) | Declining 20–30%+/year (stack generalization reduces per-vehicle capex) |
| **Opex/Mile** | Stable by metro | Declining 30%+/year (autonomy cost collapse, software scaling) |
| **Take-Rate** | 18–32% (Uber/Lyft competitive pressure) | 40–65% (ownership replacement justifies premium; network effects lock in) |
| **Fleet Economics** | Per-vehicle FCF determined by local utilization | Fleet-wide FCF improves with scale (cost decline compounds) |
| **Scaling Economics** | Linear (each metro adds marginal revenue equal to marginal cost) | Exponential (cost decline + approval acceleration → higher utilization → lower unit cost → more deployment) |

**Model Implication:**
- Transport: Profitability tied to utilization; margins constant or declining
- Platform: Profitability improves with scale; margins expand (cost collapse)

---

## 4. Competitive Dynamics

| Aspect | **Transport Model** | **Platform Model** |
|--------|---|---|
| **Market Structure** | Duopoly/oligopoly (Waymo + Tesla coexist) | Winner-take-most or rapid bifurcation |
| **Moat Source** | Regulatory approval parity (both approved in same metros) | Software scaling (cost decline compounds, second player can't catch up) |
| **Competitive Lever** | Price (take-rate competition) | Cost curve + network effects (first player's advantage compounds) |
| **Survival Condition** | Both scale at similar pace in assigned geographies | One player reaches 70%+ concentration; second player trapped in low-volume, low-utilization hellscape |
| **Path to Victory** | Waymo (regulatory + safety lead); Tesla (cost + manufacturing) | FSD generalizes (Tesla wins) OR Waymo's regulatory lead creates insurmountable advantage (Waymo wins) |

**Model Implication:**
- Transport: Waymo ~$30–60B, Tesla ~$15–40B (both survive)
- Platform: Winner ~$2–5T, Loser ~$0–500B (massive variance)

---

## 5. Valuation Multiple

| Aspect | **Transport Model** | **Platform Model** |
|---|---|---|
| **Comparable Valuation** | Uber (8x EV/Revenue), transportation/logistics (9–18x) | Salesforce/ServiceNow (15–50x), Google Maps/Waze (50–100x+) |
| **What You're Pricing** | Rideshare operator with labor cost advantage (Waymo/Tesla) | Compounding software monopoly with network effects |
| **Success Case Multiple** | 12–18x (commodity with moat) | 50–150x (software with lock-in) |
| **Failure Case Multiple** | 5–9x (regulated utility, if model breaks) | 0–3x (destroyed by competition or regulated) |
| **Terminal Value 2035** | $30–90B (Waymo) × 9–18x multiple | $2–10T (Waymo) × 50–150x multiple |

**Model Implication:**
- Transport: Waymo per-share value +$2–8
- Platform: Waymo per-share value +$165–830

---

## 6. Scaling Behavior

| Aspect | **Transport Model** | **Platform Model** |
|---|---|---|
| **Deployment Curve** | Linear (each metro independently approved, deployed, optimized, cash-generating) | Nonlinear (cost decline + approval acceleration + utilization improvement compound) |
| **Feedback Loops** | Weak (one metro success doesn't accelerate another metro approval) | Strong (cost decline in SF enables aggressive deployment in Phoenix; utilization improvements prove safety → faster approval) |
| **Learning Transfer** | Minimal (per-metro optimization doesn't transfer across regions) | Maximum (FSD/Waymo stack generalization enables knowledge transfer) |
| **Network Effects** | None (Waymo network in SF doesn't improve Waymo SF quality) | Strong (more vehicles → more miles → better stack → faster improvement → lower costs) |

**Model Implication:**
- Transport: 300k vehicles in year 10
- Platform: 10–50M vehicles in year 10 (scale-driven cost decline makes deployment exponential)

---

## 7. Labor & Externalities

| Aspect | **Transport Model** | **Platform Model** |
|---|---|---|
| **Driver Elimination** | Risk (regulatory/political backlash; driver lobby resistance) | Core thesis (driver elimination is value creation; enables 40%+ take-rates + customer acceptance) |
| **Public Messaging** | "Safer than humans; complement to transit" | "Transportation workforce transition; redistribution policy needed" |
| **Political Path** | Defensive (minimize driver impact; gradual replacement) | Offensive (safety argument; network effects argument; congestion relief argument) |
| **Regulatory Risk** | Moderate (anti-displacement rules; worker retraining mandates) | Extreme (either full support or full opposition; no middle ground) |

**Model Implication:**
- Transport: Modest regulatory friction over driver impact
- Platform: Binary outcome (regulatory approval S-curve or regulatory collapse)

---

## 8. Regulatory Assumptions

| Aspect | **Transport Model** | **Platform Model** |
|---|---|---|
| **Approval Path** | Linear 3–6%/year (local politics + bureaucracy + incremental learning) | S-curve + exponential (safety advantage flips narrative from "caution" to "human driving is dangerous") |
| **Inflection Condition** | None (linear forever) | Undeniable safety gap (Waymo 30k mi/intervention vs. human 150k mi/crashes) |
| **Timeline to Full Approval** | 15–25 years (300k vehicles in year 20) | 10 years total, with 8 years at linear then 2 years exponential (50%+ approval by 2035) |
| **Reversal Risk** | Low (linear approval only stalls, not reverses) | High (major incident reverses narrative; approval collapses) |

**Model Implication:**
- Transport: Approval pace is constant structural parameter
- Platform: Approval pace is threshold-dependent (linear until inflection, then exponential)

---

## 9. Success Conditions

| Aspect | **Transport Model** | **Platform Model** |
|---|---|---|
| **What Wins** | Waymo + Tesla both capture regional advantage (Waymo premium metros, Tesla suburbs) | One player dominates 70%+, second player in niche OR market bifurcates (premium/commodity) |
| **Industry Outcome** | Stable duopoly / oligopoly (~50/50 or 60/40 split) | Winner-take-most or rapid bifurcation (70/30 or 80/20 or 90/10) |
| **Value Capture** | Shared between Waymo and Tesla | Highly concentrated (winner captures 70–80% of platform value) |
| **Is Model Right?** | Both players profitable, market stable, 300k–500k vehicles by 2035 | Ownership >50%, approval >10%/year, non-ride >30%, one player 70%+ by 2030 |

**Model Implication:**
- Transport: Success = both Waymo and Tesla survive and scale
- Platform: Success = one player dominates; other dies or occupies niche

---

## 10. Hidden Assumption Coupling

**Transport Model:**
```
Ownership <5% 
  ↓ (locks)
Approval 3–6%/year
  ↓ (locks)
Take-rate 18–32% (Uber competition)
  ↓ (locks)
Fleet <300k (5% rideshare TAM)
  ↓ (locks)
Take-rate <32% (no margin expansion)
  ↓ (locks)
Waymo + Tesla coexist (no winner-take-most)
```

**Platform Model:**
```
Ownership 50%+
  ↓ (locks)
Take-rate 40–65% (necessity + lock-in)
  ↓ (locks)
Fleet 10–50M (ownership replacement requires scale)
  ↓ (locks)
Approval exponential (safety narrative flips)
  ↓ (locks)
Software scaling 30%+/year (cost decline compounds)
  ↓ (locks)
One player 70%+ (winner-take-most from cost advantage)
```

**Cannot mix:** If ownership truly replaced (50%+), you CANNOT stay in transport economics (9x multiple, $30–90B value). You MUST shift to platform economics (50–150x multiple, $2–10T value).

---

## Summary: Why Model Matters

**Transport Model Cost:** Leaves $2–9.9T of Waymo value on table (pricing 5% of potential)

**Platform Model Cost:** Overprices if ownership <30% (buys $2–10T value for something worth $150B)

**Decision:** Track ownership substitution % through 2027. If <10% by Q4 2027, accept transport model. If >15%, shift to platform model. If 30%+, accept full platform model.
