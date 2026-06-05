# Robotaxi Regimes: A, B, C

Three mutually exclusive economic structures. Regime is determined by observing real-world data, not chosen by analysts. Assumptions within each regime are coupled — see `REGIME_COHERENCE_CONSTRAINTS.md`.

---

## Regime A: Utility Transport

**Core thesis:** Robotaxis compete with Uber/Lyft. Car ownership stays near-universal.

| Parameter | Value |
|-----------|-------|
| Car substitution | <5% |
| Fleet size (2035) | 120–300k |
| Trip intensity | 12–45 trips/capita/yr |
| Take-rate | 18–32% |
| Regulatory approval | 3–6%/year linear |
| Non-ride revenue | <5% of miles |
| Terminal multiple | 9–18x |
| Waymo 2035 PV | $52B |
| Tesla 2035 PV | $32B |

**What must hold simultaneously:** Ownership stays universal · Approval stays bureaucratic · No software scaling · Uber/Lyft compete on price · No asset-layer monetization

**Exit to B if:** Ownership >10% in any metro · Approval >8%/year sustained · Non-ride >10% of miles · Take-rate >30% without competitive pressure  
**Collapse to A if:** Autonomy stalls (intervention rate flat 4+ quarters)

---

## Regime B: Infrastructure Layer

**Core thesis:** Robotaxis capture 20–30% car ownership. Essential mobility layer. Partial TAM shift.

| Parameter | Value |
|-----------|-------|
| Car substitution | 15–30% |
| Fleet size (2035) | 500k–2M |
| Trip intensity | 50–120 trips/capita/yr |
| Take-rate | 25–40% |
| Regulatory approval | S-curve inflection 2028–2030 |
| Non-ride revenue | 10–25% of miles |
| Terminal multiple | 25–50x |
| Waymo 2035 PV | ~$1,956B |
| Tesla 2035 PV | ~$1,825B |

**What must hold simultaneously:** Ownership drops 20–30% in major metros · Regulatory S-curve inflects · Kids/elderly become primary users · Logistics/delivery 10–25% of miles · Adjacent monetization emerges

**Fall back to A if:** Ownership stays <5% despite availability · Approval stays <3%/year · Take-rates compress <15% · Intervention rate plateaus  
**Escalate to C if:** Ownership >30% · Approval >10%/year · Non-ride >30% · Fleet guidance >2M

---

## Regime C: Platform Monopoly

**Core thesis:** Robotaxis replace 50%+ car ownership. Foundational coordination layer. Winner-take-most.

| Parameter | Value |
|-----------|-------|
| Car substitution | 50%+ |
| Fleet size (2035) | 10–50M |
| Trip intensity | 150–300+ trips/capita/yr |
| Take-rate | 40–65% |
| Regulatory approval | Exponential post-inflection |
| Non-ride revenue | 30%+ of miles |
| Terminal multiple | 50–150x |
| Waymo 2035 PV | $6,210B–$20,170B |
| Tesla 2035 PV | $5,320B (if winner) or ~$0 (if loser) |

**What must hold simultaneously:** Autonomy truly robust · Ownership drops 50%+ in metros · Regulatory S-curve inflects then goes exponential · Stack generalizes cross-region · Marginal costs decline 30%+/year · Winner achieves 70%+ share

**Fall to B if:** Ownership tops out <30% · Second player scales competitively · Take-rates compress <30% · Cost decline <15%/year  
**Collapse to A if:** Major safety incident · Regulatory reversal · Autonomy stalls completely

---

## Monitoring: Which Regime Are We In?

| Metric | Regime A | Regime B | Regime C | Frequency |
|--------|----------|----------|----------|-----------|
| Car substitution % | <5% | 15–30% ↑ | >35% ↑ | Quarterly |
| Regulatory approval pace | 2–6%/yr | 5–8%/yr ↑ | >10%/yr exp. | Quarterly |
| Non-ride revenue mix | <5% miles | 10–25% | >30% | Quarterly |
| Take-rate | 18–32% w/pressure | 25–40% stable | 40%+ resilient | Quarterly |
| Fleet guidance | <300k | 500k–2M | >5M | Annual |
| Intervention rate | Improving | Improving | Improving | Quarterly |

**Rule:** Regime shifts are discontinuous. If any Tier 1–2 metric breaks its ceiling, the regime is dead — shift immediately. See `REGIME_INDICATORS.md` for full decision rules.
