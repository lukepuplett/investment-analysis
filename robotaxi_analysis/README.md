# Robotaxi Revenue Model

**Primary constraint: regulatory approval by metro tier. Charging is trivial capex ($500/vehicle/year).**

---

## BLUF

Four scenarios span niche rideshare to civilization-scale transport replacement. The regime that materializes is determined by a single hinge variable — **car ownership substitution %** — observable by Q4 2027.

| Scenario | Waymo PV | Tesla PV | Waymo/share | Tesla/share |
|----------|----------|----------|-------------|-------------|
| Conservative (Transport) | $52B | $32B | +$4.31 | +$8.09 |
| Infrastructure Layer | $1,956B | $1,825B | +$162.19 | +$456.35 |
| Natural Monopoly | $6,210B | $5,320B | +$514.96 | +$1,329.99 |
| Ownership Disruption | $20,170B | $1,791B* | +$1,672.47 | +$447.62 |

\*Tesla congestion-limited at US scale in Ownership Disruption; requires global deployment.

GOOGL market cap $4.68T · $388/share · 12.06B shares. TSLA $1.60T · $399/share · 4.0B shares.

---

## Quick Start

```python
python3 run_optionality_scenarios.py
```

Or from code:

```python
from robotaxi_revenue_model_enhanced import (
    optionality_scenarios, run_projection, default_profiles,
    MarketPriors, default_rollout_grid, SupplyConstraints
)

opt = optionality_scenarios()
# Keys: 'conservative_transport', 'infrastructure_layer', 'natural_monopoly', 'ownership_disruption'
```

---

## Scenarios

| Scenario | Fleet Waymo/Tesla | Car Substitution | Asset Layer | Terminal Multiple (T1) |
|----------|------------------|------------------|-------------|------------------------|
| Conservative | 120k / 200k | 8% | 1.0x | 17x |
| Infrastructure | 2M / 5M | 20% | 1.2x | 32x |
| Natural Monopoly | 5M / 15M | 35% | 1.4x | 45x |
| Ownership Disruption | 10M / 30M | 60% | 1.6x | 50x |

Scenarios are internally coupled assumption packages — not points on a continuous axis. See `REGIME_COHERENCE_CONSTRAINTS.md`.

---

## Files

| File | Purpose |
|------|---------|
| `robotaxi_revenue_model_enhanced.py` | Model implementation |
| `run_optionality_scenarios.py` | Run all four scenarios; saves JSON |
| `REGIMES.md` | Regime A/B/C definitions, economics, monitoring tables |
| `REFRAME.md` | Why charging isn't a constraint; three mutually exclusive worlds; 7 hidden variables |
| `MODEL_ARCHITECTURE_COMPARISON.md` | Transport vs. platform model — 18-dimension comparison table |
| `REGIME_COHERENCE_CONSTRAINTS.md` | Why assumptions are coupled; three cross-regime logical errors |
| `REGIME_VALUATION_MASTER.md` | 2035 outcomes, probability-weighted expected values, sensitivity |
| `REGIME_INDICATORS.md` | Five-tier leading indicator hierarchy; stay-if tables per regime |
| `REGIME_TRANSITIONS.md` | Hard triggers for all five possible regime shift directions |
| `QUARTERLY_MONITORING_FRAMEWORK.md` | KPI scorecard; data collection; what to do when trigger hits |
| `OPTIONALITY_SCENARIOS.md` | Full scenario output tables; per-share stockholder impact |

---

## Key Checkpoint

**Q4 2027:** First data point sufficient to distinguish regime. If car substitution <5% in all metros, Regime A confirmed — accept transport economics. If 10–25%, shift probability mass to Regime B. If >30%, model Regime C.

All other variables (approval pace, fleet guidance, take-rate, non-ride mix) follow from ownership substitution. Track that one first.
