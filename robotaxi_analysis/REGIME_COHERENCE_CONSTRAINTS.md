# Regime Coherence Constraints

Each regime is a self-consistent assumption package. Cannot cherry-pick across regimes. Breaking any core assumption forces a transition.

For each regime's full assumption ranges, see `REGIMES.md`.

---

## Coupling Cascades

**Regime A (Utility):**
```
Ownership <5%
  → fleet stays <300k (not enough demand for more)
  → take-rate 18–32% (Uber re-enters above 32%)
  → approval 3–6%/year (no safety narrative shift)
  → non-ride <5% (no asset leverage at small fleet)
  → both players coexist (software not scaling)
```

**Regime B (Infrastructure):**
```
Ownership 15–30%
  → fleet 500k–2M (coverage needed for partial replacement)
  → take-rate 25–40% (convenience premium, Uber absent at scale)
  → approval S-curve 2028–2030 (safety narrative building)
  → non-ride 10–25% (asset base large enough for logistics/data)
  → winner-leaning but bifurcated (not yet monopoly)
```

**Regime C (Platform):**
```
Ownership 50%+
  → fleet 10–50M (full substitution demands scale)
  → take-rate 40–65% (necessity + lock-in; no Uber alternative)
  → approval exponential (human driving framed as dangerous)
  → non-ride 30%+ (platform layer exceeds rides)
  → one player 70%+ (software cost decline compounds → monopoly)
```

---

## Three Cross-Regime Logical Errors

**Error 1: Large fleet + low take-rate**
- 10M vehicles at 20% take-rate is incoherent. A 10M fleet requires 50%+ ownership substitution. When ownership is replaced, customers have no Uber alternative — take-rates must be 40%+. If take-rates are 20%, ownership has NOT been replaced; the fleet cannot be 10M.

**Error 2: Exponential approval + stagnant autonomy**
- Approval going exponential (>10%/year) requires the safety narrative to have flipped ("human driving is dangerous"). That narrative cannot flip while intervention rates are flat. Approval pace and autonomy improvement must co-move.

**Error 3: High non-ride mix + small fleet**
- 30%+ non-ride miles requires capital leverage that only exists at 5M+ fleet. At 500k–2M vehicles (Regime B), non-ride stays 10–25% because the asset base is insufficient for full logistics/data monetization.

---

## Variable Dependency Map

| Variable | Determined By | Cannot Set Independently |
|----------|---------------|--------------------------|
| Fleet size | Ownership substitution % | Fleet follows TAM; TAM follows ownership |
| Take-rate | Ownership replacement + competition | Ownership <5% → Uber competes → rate collapses |
| Approval pace | Autonomy robustness + regulatory narrative | Narrative follows safety proof |
| Non-ride revenue | Fleet size and asset base | Leveraged off scale; tiny at 120k vehicles |
| Competitive structure | Software scaling rate | Coexistence = software not scaling |
