# Regime Coherence Constraints

Each regime is a self-consistent assumption package. Cannot cherry-pick across regimes. Breaking any core assumption forces regime transition.

## Regime A (Utility)

**Core Assumptions (All Must Hold)**

| Assumption | Range | Breaks If |
|-----------|-------|-----------|
| Ownership substitution | <5% | >10% observed |
| Regulatory approval | 3–6%/year | Accelerates >2x baseline |
| Non-ride use | <5% miles | >10% of miles |
| Take-rate | 18–32% | Sustains >25% without erosion |
| Fleet | 120–300k | Jumps to 500k+ |
| Induced demand | 1.35–2.25x | >3x (behavior change signal) |
| Competition | Coexist (both survive) | One player >70% |

**Incoherence Triggers (Force A→B Shift)**
- Fleet >500k = ownership replacement happening
- Take-rate >30% sustained = margins too high for Uber competition
- Non-ride >10% miles = asset monetization emerging
- Approval >8%/year = regulatory environment changed
- One player >70% = software scaling evident


## Regime B (Infrastructure)

**Core Assumptions (All Must Hold)**

| Assumption | Range | Breaks If |
|-----------|-------|-----------|
| Ownership substitution | 15–30% | <10% (→A) or >40% (→C) |
| Regulatory approval | 5–8%/year S-curve | <3%/year linear (→A) or >10%/year (→C) |
| Non-ride use | 10–25% miles | <5% (→A) or >30% (→C) |
| Take-rate | 25–40% | <18% (→A) or >45% sustained (→C) |
| Fleet | 500k–2M | <300k (→A) or >5M (→C) |
| Induced demand | 3–5x | <2x (→A) or >8x (→C) |
| Competition | Winner-leaning, bifurcated | >75% to one player (→C) |

**Incoherence Triggers**
- Ownership <10% despite 3+ years availability → A
- Approval stuck <2%/year → A
- Take-rate <18% (competition re-emerges) → A
- Intervention rate flat 4+ quarters → A
- Ownership >35% in major metro → C
- Approval >10%/year sustained → C
- Non-ride >30% of miles → C
- One player >75% share → C


## Regime C (Platform)

**Core Assumptions (All Must Hold)**

| Assumption | Range | Breaks If |
|-----------|-------|-----------|
| Ownership substitution | 50%+ | <30% (→B) |
| Regulatory approval | >10%/year exponential | <8%/year (→B) or incident reversal (→A) |
| Non-ride use | 30%+ miles | <20% (→B) |
| Take-rate | 40–65% | <30% (→B) |
| Fleet | 10–50M | <2M (→B) |
| Induced demand | 10–25x | <5x (→B) |
| Competition | Winner-take-most | Both >30% share (→B) |
| Cost decline | 30%+/year | <15%/year (→B) |
| Stack generalization | Cross-region transfer | Region-locked (→B) |

**Incoherence Triggers**
- Autonomy stalls (intervention rate flat 4+ quarters) → B
- Second player matches leader growth → B
- Approval inflection fails (stays <8%/year) → B
- Ownership <40% after 5+ years → B
- Take-rate <35% despite fleet scale → B
- Major incident or regulatory reversal → A
- Ownership substitution fails completely → A


## Cross-Regime Logical Errors (Cannot Mix)

**Error 1: Regime C Fleet + Regime A Take-Rate**
- 10M vehicles at 20% take-rate = $10B revenue (doesn't match any regime)
- 10M fleet requires 50%+ ownership substitution. If true, customers demand lock-in (40%+ take-rate), not Uber pricing
- **Rule:** Take-rate is function of ownership substitution, not independent variable

**Error 2: Regime C Approval + Regime A Autonomy**
- Exponential approval (>10%/year) = narrative: "human driving dangerous"
- Flat intervention decline (Regime A) = "autonomy still fragile"
- **Rule:** Regulatory pace must match autonomy robustness or narrative breaks

**Error 3: Regime B Ownership + Regime C Non-Ride Mix**
- 30% non-ride miles requires 10M+ fleet for capital leverage
- Regime B fleet is 500k–2M; non-ride stays 10–25% due to smaller asset base
- **Rule:** Non-ride mix scales with fleet size; cannot mix across regimes

## Why Assumptions Are Coupled

| Variable | Determined By | Cannot Independently Set |
|----------|---------------|------------------------|
| Fleet size | TAM (ownership %) | No—implied by ownership substitution |
| Take-rate | Competition + ownership replacement econ | No—driven by customer lock-in or Uber pressure |
| Approval pace | Autonomy robustness + regulatory narrative | No—must align with proof of safety |
| Non-ride revenue | Fleet size and capital intensity | No—leveraged off asset deployment scale |
| Competitive consolidation | Software scaling rate | No—determined by cost curve compounding |

**To transition regimes: change the full package, not tweaks.** Autonomy stalls → collapse to A. Ownership emerging → shift to B. Software scales + regulation inflects → escalate to C.
