# Reframing: Transport Model vs. Platform Model

Original model was architected as a **transport business** while the market prices a **platform outcome**. These are discontinuous economic structures that require different assumption packages.

---

## Three Mutually Exclusive Worlds

| Aspect | **Regime A: Utility** | **Regime B: Infrastructure** | **Regime C: Platform** |
|--------|------------------|------------------------|------------------|
| **Competes With** | Uber/Lyft | Transit + suburban cars | Car ownership (50%+) |
| **TAM** | $5–10B (rideshare) | $50–100B (partial replace) | $2–5T (total transport) |
| **Economics** | Transport commodity | Essential infrastructure | Computing monopoly |
| **Moat** | None (margin compression) | Regulatory + convenience | Winner-take-most software |
| **Scaling Model** | Linear (capital constrained) | Sigmoid (S-curve approval) | Exponential (software) |
| **Regulatory Path** | Bureaucratic linear 3–6%/year | S-curve inflection 2028–2030 | Exponential post-inflection |
| **Fleet Size 2035** | 120–300k | 500k–2M | 10–50M |
| **2035 Revenue** | $3–5B | $15–30B | $50–150B |
| **Terminal Multiple** | 9–18x (auto/transport) | 25–50x (infrastructure) | 50–150x (software) |
| **Waymo Terminal Value** | $30–90B | $150–400B | $2–10T |
| **Core Assumption** | Ownership stays universal <5% | Ownership shifts 20–30% | Ownership collapses 50%+ |

---

## Architectural Critique: Why Original Model Fails

**Original model embedded these assumptions:**
- Fleet 120–300k (signals <5% ownership substitution)
- Take-rate 18–32% (Uber/Lyft competitive pressure)
- Approval 3–6%/year (bureaucratic, linear)
- No asset-layer monetization (<5% non-ride)
- Induced demand 1.35–2.25x (modest elasticity)
- Terminal multiple 9–18x (transport commodity)

**Result:** Model locked into Regime A economics. Cannot escape because every variable is interdependent. Ownership assumption drives fleet size, which drives utilization, which drives take-rate, which drives regulatory narrative, which drives approval pace.

**The problem:** Market prices Regime C (platform outcome with 50%+ ownership replacement, $2–10T value). Model prices Regime A (niche rideshare, $30–90B value). **85–90% of potential upside is excluded by architecture.**

---

## Hidden Variables That Drive World Determination

**Seven variables lock the regime:**

1. **Ownership Substitution %**
   - Regime A: <5% (people keep cars)
   - Regime B: 15–30% (meaningful shift in metros)
   - Regime C: 50%+ (majority adoption)
   - Why it matters: Sets TAM and customer lock-in dynamics. If ownership truly replaced, customers accept 40%+ take-rates (necessity). If ownership <5%, Uber competes at 15%, margins collapse.

2. **Regulatory Approval Pace**
   - Regime A: 3–6%/year linear (local bureaucracy)
   - Regime B: 5–8%/year S-curve (inflection 2028–2030)
   - Regime C: >10%/year exponential (safety narrative flipped)
   - Why it matters: Approval pace must match autonomy robustness. If approval exponential but autonomy stalls, narrative breaks.

3. **Non-Ride Revenue Mix**
   - Regime A: <5% of miles (pure rideshare)
   - Regime B: 10–25% of miles (logistics, delivery, ads emerging)
   - Regime C: 30%+ of miles (platform layer exceeds core ride)
   - Why it matters: Asset leverage. Can justify 10M+ fleet only if non-ride revenue >30%.

4. **Take-Rate Sustainability**
   - Regime A: 18–32% (Uber pressure keeps rates low)
   - Regime B: 25–40% (convenience premium, no Uber at scale)
   - Regime C: 40–65% (lock-in + network effects)
   - Why it matters: If ownership truly replaced, customers have no choice—rates stay high. If ownership <5%, Uber re-enters—rates compress.

5. **Fleet Guidance**
   - Regime A: <300k (serves 5% rideshare demand)
   - Regime B: 500k–2M (covers ownership replacement in metros)
   - Regime C: 10M+ (5–20% of 290M US car fleet)
   - Why it matters: Fleet size reveals TAM assumption. If company guides >500k, they're modeling ownership replacement, not rideshare niche.

6. **Software Scaling Rate (Marginal Cost Decline)**
   - Regime A: Flat or <10%/year (hardware-gated, not software)
   - Regime B: 15–25%/year (steady but not exponential)
   - Regime C: 30%+/year (autonomy stack generalizing, cost toward zero)
   - Why it matters: If cost decline stays <15%, second player can match leader—bifurcated market. If >30%, first player compounds advantage infinitely—monopoly.

7. **Competitive Consolidation**
   - Regime A: Both players coexist (Waymo + Tesla <70% each)
   - Regime B: Winner-leaning but bifurcated (one player <70%)
   - Regime C: Winner-take-most (one player 70%+)
   - Why it matters: Coexistence requires software NOT scaling. Consolidation requires software scaling (cost leadership compounds). These are mutually exclusive.

---

## What Broke the Original Model

**Three fundamental errors:**

**1. Linear Sensitivity Instead of Regime Discipline**
- Model treated variables independently
- "If take-rate goes to 35%, value increases X%"
- Reality: Take-rate is function of ownership substitution. If true, it MUST jump to 40%+. If not, it COLLAPSES to 18%.
- Variables are coupled, not independent

**2. Hidden Assumption Stack**
- Model assumed: "Robotaxis will compete with Uber, stay niche, extract modest value"
- This assumption package only coherent if ownership <5%, approval stays bureaucratic, software doesn't scale
- Model couldn't model ownership replacement without contradicting take-rate and fleet assumptions simultaneously
- Had to rebuild entire model to allow ownership substitution to be core variable

**3. Valuation Multiplier Trap**
- If robotaxis truly replace 50%+ ownership, they're not "transport business" (9–18x multiple)
- They're computing platform (50–150x multiple)
- Modal player changes from "transportation commodity" to "software monopoly"
- Original model pricing 9x on what market prices 100x

---

## How Regime Framework Fixed This

**Old approach:** One model with linear sensitivity, scenario weightings.
- Conservative: Low ownership, low revenue, low multiple
- Infrastructure: Medium ownership, medium revenue, medium multiple
- Monopoly: High ownership, high revenue, high multiple

**New approach:** Three independent regime packages, hard transitions.
- Regime A: Transport economics (if ownership <5%, approval linear, software flat)
- Regime B: Infrastructure economics (if ownership 15–30%, approval S-curve, software 15–25%/year)
- Regime C: Platform economics (if ownership 50%+, approval exponential, software 30%+/year)

**Key difference:** Regimes are internally coherent but mutually exclusive. Cannot partially mix. Hard triggers force regime shifts (not gradual probability moves).

---

## Monitoring for World Determination

**By 2028, data will clearly indicate which world is materializing:**

| Metric | Confirms A | Confirms B | Confirms C |
|--------|-----------|-----------|-----------|
| **Ownership %** | Flat <5% | 15–30% trending up | 35–50% trending up |
| **Approval %/yr** | 3–6% linear | 5–8% S-curve | 10%+ exponential |
| **Non-ride % miles** | <5% flat | 10–25% | 30%+ |
| **Fleet size** | <300k | 500k–2M | 5M–10M |
| **Take-rate** | 18–32%, pressure | 25–40%, stable | 40%+, resilient |

**If none of these trends materialize by Q4 2028, collapse to Regime A and reset valuation.**

---

## Probability Weighted Expected Values (May 2026)

| Regime | Probability | Waymo Terminal | Waymo PV | Per GOOGL Share |
|--------|------------|------------------|----------|-----------------|
| **A (Utility)** | 50% | $30–90B | $15–45B | +$1.24–3.73 |
| **B (Infrastructure)** | 35% | $150–400B | $52.5–140B | +$4.35–11.62 |
| **C (Platform)** | 15% | $2–10T | $300B–1.5T | +$24.88–124.38 |
| **Expected Value** | 100% | — | $368B–1.69T | +$30.47–139.73 |

**vs. old model ($30–70B range):** Regime framework reveals 5–50x upside optionality depending on which world materializes.

---

## Critical Insight

**Transport business has moat of zero.** Uber enters at 15% margin, compresses rates, takes market. Robotaxis left competing on cost and convenience, not defensibility.

**Platform monopoly has moat of infinity.** First player costs decline 30%+/year, second player can't catch up. Winner extracts 50%+ revenue margin, owns 70%+ market share, trades at 100x+ revenue multiples.

**Ownership substitution is the hinge variable.** If <10% ownership shift by 2028, Regime A confirmed—accept $30–90B Waymo value. If 15–30%, Regime B likely—model $150–400B. If >30%, Regime C possible—price in $2–10T option.

All other variables (approval pace, fleet size, take-rate, non-ride mix, software scaling) are determined by ownership substitution. It's the keystone assumption that unlocks the rest.
