# Robotaxi Revenue Model — Reframed (May 2026)

**Regulatory approval as primary constraint. Charging bottleneck is superseded.**

This directory contains a reframed revenue projection model for autonomous ride-hailing services, comparing Tesla and Waymo under four scenario frameworks. The model reveals that **charging infrastructure is elastic capital** ($500/vehicle/year, 0.5% of fleet cost), while **regulatory approval by metro tier** is the primary binding constraint.

## ⚠️ IMPORTANT: Model Reframed

**The old model (with "2 chargers per vehicle" bottleneck) has been superseded.** See [`REFRAME_ANALYSIS.md`](REFRAME_ANALYSIS.md) for the complete reframe explaining:

- Why charging is NOT a constraint
- Why regulatory approval is the real bottleneck
- How metro-tier framework changes the analysis
- 2035 terminal outcomes: Waymo 17.3x multiple (premium), Tesla 9.8x (suburban)

**Old files archived in `.backup/` with deprecation notice.**

---

## BLUF (Bottom Line Up Front)

**Waymo dominates premium metros (Tier 1: SF, Phoenix, LA) with regulatory trust + high utilization → $3.5B platform revenue from 120k vehicles at 17.3x valuation multiple. Tesla's path is suburban Tier 3 dominance (if vision autonomy works) → 200k vehicles, $4.2B revenue, 9.8x multiple. Charging is $500/vehicle/year capex (trivial); regulatory approval gates fleet expansion, not infrastructure. Both companies' fleets scale with metro approval velocity, not charger availability.**

---

## Quick Start

### Essential Concepts

1. **Metro Tier Framework**:
   - **Tier 1**: Premium dense cores (SF, Phoenix, LA) — Waymo-favored, 2.25x regulatory velocity
   - **Tier 2**: Secondary metros (Austin, Denver) — balanced deployment, 1.0x velocity
   - **Tier 3**: Suburban rings (DFW, LA suburbs) — Tesla-favored, 0.94-1.4x velocity
   - **Tier 4**: Rural — no deployment expected

2. **Primary Constraints**:
   - **Regulatory approval** (primary) — gates deployment by metro tier
   - **Manufacturing capacity** (secondary) — rarely binds before 2035
   - **Battery supply** (tertiary) — global growth 30%/year, rarely binds
   - **Charging** (NOT a constraint) — $500/vehicle/year, solved with capital

3. **Terminal Economics**:
   - **Waymo in Tier 1**: 89.7% utilization, $1.90/mile, 32% take-rate → 17.3x multiple
   - **Tesla in Tier 3**: 55% utilization, $1.10/mile, 18% take-rate → 9.8x multiple

### Run the Model

```bash
cd robotaxi_analysis

# Import and run (Python 3.10+)
python3 -c "
from robotaxi_revenue_model_enhanced import *

# Run base case
results = run_projection(
    years=list(range(2026, 2036)),
    scenario_name=ScenarioName.BASE,
    profiles=default_profiles(),
    active={'tesla', 'waymo'},
    market=MarketPriors(),
    rollout_grid=default_rollout_grid(),
    theoretical_us_fleet_terminal=3_000_000,
    market_share={'tesla': 0.45, 'waymo': 0.55},
    supply_constraints=SupplyConstraints(),
    use_enhancements=True
)

# Print key results
for r in [res for res in results if res.year == 2035]:
    print(f'{r.company}: {r.fleet_operating:,.0f} vehicles, \${r.net_platform_revenue/1e9:.2f}B revenue')
"
```

---

## Model Architecture

### Core Components

**1. Metro-Tier Framework**
```python
from robotaxi_revenue_model_enhanced import default_metros

metros = default_metros()
# Returns 8 illustrative metros (SF, Phoenix, LA, Austin, Denver, DFW, LA suburbs)
# Covers ~31.8M of 280M US metro population (illustrative, not exhaustive)
```

**2. Regulatory Velocity by Company & Metro**
```python
from robotaxi_revenue_model_enhanced import regulatory_approval_velocity_by_tier_and_company

velocity = regulatory_approval_velocity_by_tier_and_company(
    tier=MetroTier.TIER_1,
    company="waymo",
    years_in_market=5,
    cumulative_autonomy_miles=50e6
)
# Waymo in Tier 1 after 5 years: 2.25x base velocity
```

**3. Utilization Efficiency by Operational Maturity**
```python
from robotaxi_revenue_model_enhanced import utilization_efficiency_by_company_metro

efficiency = utilization_efficiency_by_company_metro(
    company="waymo",
    metro=sf_metro,
    years_in_market=5,
    miles_per_intervention=35000
)
# Waymo in SF after 5 years: 0.897 (89.7% utilization)
```

**4. Charging Cost Model (Not a Bottleneck)**
```python
from robotaxi_revenue_model_enhanced import ChargingCostModel, calculate_charging_capex_per_vehicle

model = ChargingCostModel()
costs = calculate_charging_capex_per_vehicle(model)
# Annual cost per vehicle: $500 (0.5% of fleet capex)
# Charger ratio: 1 per 20 vehicles (fleet ops vs. consumer EV)
```

**5. Supply Constraints (Regulatory Primary)**
```python
from robotaxi_revenue_model_enhanced import project_supply_constraints

supply = project_supply_constraints(2030, "base", SupplyConstraints())
# Returns: manufacturing, regulatory, battery constraints
# Bottleneck: regulatory (smallest value)
```

---

## Scenarios

Four scenario frameworks with regulatory velocity + demand elasticity knobs:

| Scenario | Regulatory Velocity | Demand Elasticity | Deployment Cap | Use Case |
|----------|-------------------|------------------|-----------------|----------|
| **Slow** | 0.65× | 0.85× | Conservative regulatory drag | Downside case |
| **Base** | 1.0× | 1.0× | Gradual scaling | Reference case |
| **Hypergrowth** | 1.25× | 1.35× | Rapid adoption + network effects | Upside case |
| **Platform Dominance** | 1.15× | 1.5× | Winner-take-most dynamics | Extreme upside |

---

## 2035 Terminal Outcomes

### By Metro Type (Base Scenario)

**Waymo (Premium Network)**:
- Fleet: 120k vehicles (75% in Tier 1)
- Platform Revenue: $3.5B annually
- Take Rate: 32% (premium markets)
- Valuation Multiple: **17.3x** (utility-scale)
- Moat: Regulatory trust, operational competence

**Tesla (Mass-Market Swarm — IF Autonomy Works)**:
- Fleet: 200k vehicles (75% in Tier 3)
- Platform Revenue: $4.2B annually
- Take Rate: 18% (suburban, cost-sensitive)
- Valuation Multiple: **9.8x** (commodity)
- Risk: All-or-nothing on vision autonomy maturity

**Tesla (Bear Case — If Autonomy Fails)**:
- Fleet: <10k vehicles
- Platform Revenue: ~$0
- Valuation: Near-zero

---

## Metro Library (Current)

**Defined Metros** (illustrative, not exhaustive):

| Metro | Tier | Population | Trip Intensity | Company Fit |
|-------|------|-----------|---------------|-----------| 
| SF/East Bay | 1 | 7.7M | 45/capita/yr | Waymo (HQ, best case) |
| Phoenix | 1 | 5.0M | 35/capita/yr | Waymo (mature) |
| LA Downtown | 1 | 3.5M | 40/capita/yr | Waymo (density-driven) |
| Austin | 2 | 2.4M | 28/capita/yr | Mixed |
| Denver | 2 | 3.2M | 22/capita/yr | Mixed |
| DFW Suburbs | 3 | 4.0M | 15/capita/yr | Tesla (cost advantage) |
| LA Suburbs | 3 | 6.0M | 12/capita/yr | Tesla (sprawl) |
| *(Tier 1 Other)* | 1 | 7.8M | 38/capita/yr | NYC, Boston, Seattle, DC |
| *(Tier 2 Other)* | 2 | 32.7M | 22/capita/yr | Chicago, Atlanta, rest of secondary |
| *(Tier 3 Other)* | 3 | 206.2M | 12/capita/yr | Remaining suburban US |

**Note**: Defined metros cover 31.8M (11.4%); "Other" aggregates cover remaining 248.2M. Model currently uses national rollout grid (not metro-specific simulation), so individual metro selection is illustrative. Task #8 will integrate metro-by-metro simulation if granularity is needed.

---

## Key Metrics

### Per-Vehicle Economics

| Metric | Waymo (Tier 1) | Tesla (Tier 3) | Unit |
|--------|---|---|---|
| Miles/Day | 200 | 115 | miles |
| Utilization Efficiency | 89.7% | 55.4% | % of peak |
| Fare | $1.90 | $1.10 | $/mile |
| Take Rate | 32% | 18% | % of gross |
| Opex | $0.68 | $0.42 | $/mile |
| Charging Cost | $500 | $500 | $/vehicle/year |
| Annual Revenue/Vehicle | $29k | $21k | $ |

### Regulatory Velocity (Base Scenario)

| Company | Tier 1 | Tier 2 | Tier 3 | Notes |
|---------|--------|--------|--------|-------|
| **Waymo** | 2.25× | 1.0× | 0.42× | Preferred in premium; slower in mass market |
| **Tesla** | 0.80× | 0.80× | 0.94× | Barriers in premium; strength in suburban |

---

## Customization

All parameters customizable in `robotaxi_revenue_model_enhanced.py`:

- **Metro tiers**: Add/modify metros in `default_metros()`
- **Regulatory velocity**: Adjust per company in `regulatory_approval_velocity_by_tier_and_company()`
- **Utilization efficiency**: Modify by metro/maturity in `utilization_efficiency_by_company_metro()`
- **Charging costs**: Update in `ChargingCostModel` dataclass
- **Market priors**: Change `MarketPriors` (population, trip rates, substitution ceiling)
- **Company profiles**: Adjust fares, take rates, cost structures in `default_profiles()`

---

## Integration with GOOG/TSLA Investment Analyses

This model informs:
- `goog/ROBOTAXI_ANALYSIS.md` — Waymo's premium metro moat
- `tsla/ROBOTAXI_ANALYSIS.md` — Tesla's autonomy-dependent bull/bear cases
- Valuation models with 2030E/2035E platform revenue by scenario
- Risk assessments tied to regulatory approval + intervention rate milestones

---

## Files in This Directory

### Core Regime Economics (May 2026 Framework)

| File | Purpose |
|------|---------|
| [**REGIME_A_UTILITY.md**](REGIME_A_UTILITY.md) | Transport commodity model (fleet 120–300k, take-rate 18–32%, 2035 revenue $3–5B, terminal value $30–90B). Base case if ownership substitution stays <5%. |
| [**REGIME_B_INFRASTRUCTURE.md**](REGIME_B_INFRASTRUCTURE.md) | Infrastructure layer model (fleet 500k–2M, take-rate 25–40%, 2035 revenue $15–30B, terminal value $150–400B). Emerges if ownership substitution 20–30%, regulatory S-curve inflection. |
| [**REGIME_C_PLATFORM.md**](REGIME_C_PLATFORM.md) | Computing platform model (fleet 10–50M, take-rate 40–65%, 2035 revenue $50–150B, terminal value $2–10T). Winner-take-most if ownership substitution 50%+, approval exponential. |

### Valuation & Framework

| File | Purpose |
|------|---------|
| [**REGIME_VALUATION_MASTER.md**](REGIME_VALUATION_MASTER.md) | 2035 outcomes comparison across all three regimes. Waymo: A $30–90B, B $150–400B, C $2–10T. Tesla: A $15–50B, B $80–200B, C $500B–5T (win) or $0 (lose). Probability baseline: A 50%, B 35%, C 15%. Expected value: $368B–1.69T. |
| [**REGIME_COHERENCE_CONSTRAINTS.md**](REGIME_COHERENCE_CONSTRAINTS.md) | Why assumptions are coupled within each regime. Cannot cherry-pick across regimes. Documents seven hidden variables that lock each regime (ownership %, approval pace, non-ride revenue, take-rate, fleet size, software scaling, competitive consolidation). |
| [**REGIME_TRANSITIONS.md**](REGIME_TRANSITIONS.md) | Hard triggers that force regime shifts (A→B, B→C, B→A, C→B, C→A). Soft signals precede hard triggers. Key checkpoint: Q4 2027 (first major data point to distinguish regimes). |

### Monitoring & Indicators

| File | Purpose |
|------|---------|
| [**QUARTERLY_MONITORING_FRAMEWORK.md**](QUARTERLY_MONITORING_FRAMEWORK.md) | Reframed from scenario probability to regime determination. Track KPIs quarterly; hard thresholds force regime transitions (not gradual probability shifts). Includes regime-breaking events, data collection checklist, decision rules. |
| [**REGIME_INDICATORS.md**](REGIME_INDICATORS.md) | Five-tier hierarchy of leading indicators (Tier 1: ownership %, Tier 2: approval pace, Tier 3: non-ride mix, Tier 4: take-rate, Tier 5: fleet size). When any hard trigger hits, regime shift is forced. |

### Architecture & Critique

| File | Purpose |
|------|---------|
| [**REFRAME_WORLD_ANALYSIS.md**](REFRAME_WORLD_ANALYSIS.md) | Architectural critique: original model built as "transport business" while market prices "platform outcome". Explains why original model failed, hidden variables that determine regimes, hinge variable (ownership substitution) that unlocks all others. |
| [**MODEL_ARCHITECTURE_COMPARISON.md**](MODEL_ARCHITECTURE_COMPARISON.md) | Nine-dimension breakdown of transport vs. platform model assumptions: demand, geography, unit economics, competition, valuation, scaling, labor, regulatory, success conditions. Shows why cannot mix regimes. |

### Legacy Files (Reference Only)

| File | Purpose |
|------|---------|
| `robotaxi_revenue_model_enhanced.py` | Main model implementation — reframed with metro-tier + regulatory constraints |
| `robotaxi_revenue_model.py.backup` | Backup of original model (reference only) |
| `.backup/DEPRECATION.md` | Explanation of old model obsolescence |

---

## Next Steps

**Task #8 (Future):** Refactor core simulation to metro-specific parameters, enabling per-metro fleet deployment tracking and regulatory approval gating. Currently uses national rollout grid; metro framework is illustrative.

**Questions for Future Analysis:**
1. Should we expand metro library to 30+ metros or keep aggregated "Tier N Other"?
2. What's the minimum metro granularity for investment decision-making?
3. Do we need quarterly vs. annual metro deployment tracking?

---

**Last updated:** May 20, 2026  
**Model version:** Reframed (regulatory approval primary, charging elastic)  
**Status:** Ready for investment analysis integration
