# Optionality Scenarios: Transportation vs. Infrastructure Analysis

## Overview

The enhanced model now supports three distinct market structure assumptions for robotaxis:

1. **Conservative (Transportation Market)** — baseline model
2. **Infrastructure Layer** — city OS + logistics + data value
3. **Natural Monopoly** — winner-take-most with compounding moats

This framework explores the user's core critique: **the model may be treating a civilization-scale technology as a niche transportation market.**

---

## Three Scenarios Explained

### 1. Conservative (Transport Market)
**Current baseline model. Robotaxis are premium rideshare.**

| Parameter | Value |
|-----------|-------|
| Behavior Change | Never (fixed demand) |
| Market Structure | Transport economics |
| Induced Demand Multiplier | 1.35x |
| Terminal Multiples | Tier 1: 17x, Tier 2: 11x, Tier 3: 8x |
| Waymo 2035 Platform Revenue | $3.5B |
| Waymo Discounted Value (PV) | **$23.4B** |
| % of GOOGL Market Cap | **0.50%** |

**Assumptions:**
- Trips/capita fixed at market baseline
- Substitution of existing taxi/rideshare only
- Margins compress with competition
- Multiple reflects transport commodity economics

**Risk:** Likely **too conservative** if robotaxis enable phase-change behaviors.

---

### 2. Infrastructure Layer
**Robotaxis become urban operating systems with multiple value streams.**

| Parameter | Value |
|-----------|-------|
| Behavior Change | Starts 2028 (land use shifts accelerate) |
| Induced Demand Multiplier | 1.75x (2x baseline by 2035) |
| Market Structure | Infrastructure + network effects |
| Terminal Multiples | Tier 1: 32x, Tier 2: 22x, Tier 3: 15x |
| Waymo 2035 Platform Revenue | $6.5B+ (ride + logistics + data + city OS) |
| Waymo Discounted Value (PV) | **$50–100B** |
| % of GOOGL Market Cap | **1.1–2.1%** |

**Value Layers:**
- **Ride-hailing:** $3.5B (current model)
- **Logistics:** $1.5B (autonomous delivery, warehouse-to-retail)
- **City Integration:** $0.8B (traffic management, emergency services, parking)
- **Data Monetization:** $0.5B (movement patterns, congestion prediction, city optimization)
- **Insurance/Risk Pooling:** $0.2B (fleet safety data commands premium rates)

**Behavior Changes Assumed:**
- Land use shifts: People move farther out → 2-3x commute distance
- Second-car elimination: Freed capital reduces ownership → +induced demand
- New user cohorts: Elderly, non-drivers gain mobility → new trips
- Mobile work/leisure: Commute time becomes productive → longer trips
- Net effect: Passenger miles 1.75x baseline by 2035

**Regulatory Flip:**
- 2026–2028: Regulation is **drag** (approval gating fleet)
- 2028+: Regulation becomes **moat** (competitor barriers increase)

**Key Insight:** AWS-like inflection. Waymo's ride revenue is the least important layer; infrastructure value dominates.

---

### 3. Natural Monopoly
**One network becomes clearly safer. Regulatory preference + city lock-in create quasi-monopoly.**

| Parameter | Value |
|-----------|-------|
| Behavior Change | Starts 2030 (inflection later, more dramatic) |
| Induced Demand Multiplier | 1.50x |
| Market Structure | Platform monopoly + moats |
| Terminal Multiples | Tier 1: 45x, Tier 2: 30x, Tier 3: 20x |
| Waymo 2035 Platform Revenue | $8–15B (winner takes most) |
| Waymo Discounted Value (PV) | **$100–300B** |
| % of GOOGL Market Cap | **2.1–6.4%** |

**Moat Compounding Effects:**
1. **Safety datasets compound:** More miles → safer system → faster approval → more miles
2. **Regulator preference compounds:** One proven winner beats competitors → approved faster in new metros
3. **City integration deepens:** Once embedded in traffic system, replacement cost becomes prohibitive
4. **Insurance pools compound:** Scale reduces per-mile risk → undercut competitor pricing

**Inflection Timing:**
- 2026–2030: Duopoly (Waymo vs Tesla, possibly one other)
- 2030+: Clear winner emerges (likely Waymo on safety + regulatory trust)
- 2030–2035: Rapid centralization → Waymo 90%+ of Tier 1/2, Tesla limited to Tier 3

**Terminal Market Structure:**
- Waymo becomes infrastructure (like air traffic control, electricity grids)
- Tesla either absorbed, forced into niche, or exits
- Passenger vehicle usage becomes platform-mediated (analogous to app stores)

**Key Insight:** Regulation flips from gating to moat-enhancing. Winner extracts platform leverage.

---

## How to Use in Python

### Run Standard Scenarios (Baseline Model)

```python
from robotaxi_revenue_model_enhanced import (
    ScenarioName, 
    run_projection, 
    default_profiles, 
    MarketPriors,
    default_rollout_grid,
    SupplyConstraints
)

# Run base case (transport market)
results = run_projection(
    years=list(range(2026, 2036)),
    scenario_name=ScenarioName.BASE,
    profiles=default_profiles(),
    active={'waymo'},
    market=MarketPriors(),
    rollout_grid=default_rollout_grid(),
    theoretical_us_fleet_terminal=3_000_000,
    market_share={'waymo': 1.0},
    supply_constraints=SupplyConstraints(),
    use_enhancements=True,
)

# Extract 2035 results
for r in results:
    if r.year == 2035:
        print(f"Waymo 2035 Fleet: {r.fleet_operating:,.0f} vehicles")
        print(f"Platform Revenue: ${r.net_platform_revenue/1e9:.2f}B")
        print(f"Terminal Multiple: {r.terminal_implied_multiple}x")
```

### Run Infrastructure/Monopoly Scenarios

```python
from robotaxi_revenue_model_enhanced import (
    optionality_scenarios,
    run_projection,
    default_profiles,
    MarketPriors,
    default_rollout_grid,
    SupplyConstraints,
)

# Load extended scenarios
opt_scen = optionality_scenarios()

# Run infrastructure scenario for Waymo
infra_scenario = opt_scen['infrastructure_layer']
results_infra = run_projection(
    years=list(range(2026, 2036)),
    scenario_name='optionality_infrastructure',  # Custom name
    profiles=default_profiles(),
    active={'waymo'},
    market=MarketPriors(),
    rollout_grid=default_rollout_grid(),
    theoretical_us_fleet_terminal=3_000_000,
    market_share={'waymo': 1.0},
    supply_constraints=SupplyConstraints(),
    scenario=infra_scenario,  # Pass custom scenario
    use_enhancements=True,
)

# Run monopoly scenario
monopoly_scenario = opt_scen['natural_monopoly']
results_monopoly = run_projection(
    years=list(range(2026, 2036)),
    scenario_name='optionality_monopoly',
    profiles=default_profiles(),
    active={'waymo'},
    market=MarketPriors(),
    rollout_grid=default_rollout_grid(),
    theoretical_us_fleet_terminal=3_000_000,
    market_share={'waymo': 1.0},
    supply_constraints=SupplyConstraints(),
    scenario=monopoly_scenario,
    use_enhancements=True,
)

# Compare valuations
def extract_2035_value(results):
    for r in results:
        if r.year == 2035:
            terminal_value = r.net_platform_revenue * r.terminal_implied_multiple
            pv = terminal_value * 0.386  # PV factor at 10% WACC
            return {
                'fleet': r.fleet_operating,
                'revenue': r.net_platform_revenue,
                'multiple': r.terminal_implied_multiple,
                'terminal_value': terminal_value,
                'pv': pv,
            }

conservative = extract_2035_value(results)
infrastructure = extract_2035_value(results_infra)
monopoly = extract_2035_value(results_monopoly)

print(f"Conservative:     ${conservative['pv']/1e9:.1f}B PV")
print(f"Infrastructure:   ${infrastructure['pv']/1e9:.1f}B PV")
print(f"Natural Monopoly: ${monopoly['pv']/1e9:.1f}B PV")
```

---

## Valuation Summary

| Case | Fleet | Platform Revenue | Multiple | Terminal Value | Discounted PV | Per GOOGL Share |
|------|-------|-----------------|----------|-----------------|---------------|-----------------|
| **Conservative** | 120k | $3.5B | 17.3x | $60.5B | **$23.4B** | +$1.94 |
| **Infrastructure** | 150k | $6.5B | 28x | $182B | **$70.3B** | +$5.83 |
| **Natural Monopoly** | 180k | $10B | 35x | $350B | **$135B** | +$11.20 |

**Probability Weighting (Illustrative):**
- Conservative: 40% × $23.4B = $9.4B
- Infrastructure: 40% × $70.3B = $28.1B
- Monopoly: 20% × $135B = $27.0B
- **Expected Value: $64.5B** (vs $23.4B conservative case)

---

## Key Takeaway

The model's "conservative" stance may reflect:
- ✅ **Correct:** Uncertain regulatory approval, Tesla competitive threat
- ❌ **Too narrow:** Only priced rides, not infrastructure/logistics/data
- ❌ **Premature maturity:** Assumed 2035 is mature state; moat compounding may accelerate after 2030

The optionality framework lets you explore: **What if the user's critique is right?**

---

## References

- Main model: `robotaxi_revenue_model_enhanced.py`
- Analysis docs: `goog/ROBOTAXI_ANALYSIS.md` and `tsla/ROBOTAXI_ANALYSIS.md`
- Full reframe: `REFRAME_ANALYSIS.md`
