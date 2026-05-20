# Tesla Robotaxi Competitive Analysis (Shared Model)

**Out-of-band quantitative analysis** — competitive modeling for Tesla vs. Waymo autonomous networks.

**Location:** Shared analysis at `/robotaxi_analysis/` (repo root) — also referenced in [`goog/`](../goog/ROBOTAXI_ANALYSIS.md).

## BLUF (Bottom Line Up Front)

**Tesla's robotaxi strategy is bottlenecked by charging infrastructure, not market demand or vehicle manufacturing. Both Tesla and Waymo are capped at ~70k vehicles by 2035 due to ~500k charger constraint (2 chargers/vehicle at scale). In this infrastructure-constrained regime, Waymo's superior unit economics ($4.28B platform revenue vs Tesla's $1.65B on identical fleet size) reflect structural advantages: 35% take-rate vs Tesla's 28%, and $1.90/mile fares vs $1.10/mile. Tesla's cost advantage ($0.42/mile vs Waymo's $0.68/mile) is real but insufficient to overcome margin structurally when both face the same charging bottleneck. Winner is determined by infrastructure buildout velocity, not vehicle production. Robotaxi emerges as a regulated utility network, not a mass-market rideshare platform. (All figures annual, 2035 base case; revenue-constrained at ~$1.6-4.3B scale, not the $100B+ platform narrative.)**

## Overview

Tesla's robotaxi strategy competes directly with **Waymo** (Google's autonomous vehicle subsidiary). This shared model compares:

- **Tesla**: Mass-market swarm thesis (lower fares, broader geographic coverage, supply-constrained growth)
- **Waymo**: Premium regulated network thesis (higher fares, tighter geographic focus, better unit economics)

## What This Tells You About Tesla

### Tesla's Competitive Positioning (Infrastructure-Constrained Regime)

**Advantages:**
- **Lower cost structure** — $0.42/mile vs Waymo's $0.68/mile (38% opex advantage)
- **Market ambition** — 22% annual deployment cap vs Waymo's 12% (willing to build faster if constraints permit)
- **Broader geographic intent** — ~88% reachable population vs Waymo's 55% (if infrastructure weren't binding)

**Challenges (all binding):**
- **Charging infrastructure bottleneck** — Both capped at ~70k vehicles by 2035, limited by ~500k charger buildout (2 chargers/vehicle required at scale)
- **Margin structurally lower** — 28% take-rate vs Waymo's 35% + lower fares ($1.10 vs $1.90/mile) = 2.6× less platform revenue on identical fleet size
- **Cost advantage insufficient** — Even with $0.26/mile cost gap, cannot overcome structural margin disadvantage when both hit same infrastructure ceiling
- **Terminal revenue modest** — At 70k vehicles, platform revenue only $1.65B annually (not $18B+); this is a utility-scale business (10-15x earnings multiple), not a platform (25x+ multiple)

### Base Case Terminal (2035, Enhanced Model with Infrastructure Constraints)

| Metric | Tesla | Waymo | Delta | Notes |
|--------|-------|-------|-------|-------|
| **Fleet Operating** | **70k** | **70k** | Identical | Both capped by charging infrastructure (~500k chargers needed) |
| Reachable Population | 370.3M | 283.4M | Tesla +31% | Regulatory approval differs; doesn't increase fleet |
| Revenue Miles/Day | 209.8 | 251.8 | Waymo +20% | Higher utilization from better unit economics |
| **Gross Annual Revenue** | **$5.8B** | **$12.2B** | Waymo +2.1× | Waymo's fares ($1.90) vs Tesla's ($1.10) |
| **Platform Annual Revenue** | **$1.65B** | **$4.28B** | **Waymo +2.6×** | Take-rate gap (28% vs 35%) amplifies at $12B gross |
| Annual Revenue/Vehicle | $23.6k | $61.1k | Waymo 2.6× | Superior unit economics despite identical fleet |
| Terminal Structure | Utility | Utility | Both | ~10-15x earnings multiple (not platform) |
| Bottleneck | Charging | Charging | Binding | 500k charger constraint caps both players |

**Critical Insight:** Infrastructure emergence, not market competition, determines outcomes. Both companies deploy identical 70k fleets because both hit the same charging bottleneck. Waymo's 2.6× revenue advantage reflects structural pricing power and take-rate superiority, not fleet scale. In a utility-constrained regime, **margin structure determines winner**, not manufacturing or roadmap ambition. Tesla's cost advantage is immaterial when both are infrastructure-limited.

### Scenario Sensitivity (Annual Platform Revenue, 2035, Enhanced Model)

| Scenario | Tesla Fleet | Waymo Fleet | Tesla Revenue | Waymo Revenue | Waymo Advantage |
|----------|-------------|-------------|----------------|----------------|-----------------|
| Slow | 70k | 70k | $1.54B | $3.55B | 2.3× |
| **Base** | **70k** | **70k** | **$1.65B** | **$4.28B** | **2.6×** |
| Hypergrowth | 70k | 70k | $1.67B | $4.41B | 2.6× |
| Platform Dominance | 70k | 70k | $1.67B | $4.37B | 2.6× |

**Critical Finding:** Scenario optimism is *eliminated* by infrastructure constraints. All scenarios converge to identical fleet sizes (70k vehicles) because all hit the same charging bottleneck. Waymo's 2.3–2.6× revenue advantage is not dependent on market size—it reflects structural unit economics (pricing, take-rate, utilization). Scenario variation becomes irrelevant when infrastructure binding constraint dominates. **The real risk/reward is infrastructure buildout velocity, not vehicle demand.**

## What Tesla Actually Faces (Infrastructure-Constrained Regime)

In a bottleneck-constrained market (charging infrastructure binding at ~70k vehicles), traditional competitive levers become irrelevant:

1. **Charging infrastructure investment** — Primary lever; whoever builds chargers 20%+ faster than Waymo captures upside. This is not Tesla's historical advantage; Waymo (Google/Alphabet) has infrastructure deployment experience.

2. **Regulatory approval momentum** — Geographic expansion is frozen by charging, not regulation. Regulatory velocity matters only post-charger availability.

3. **Pricing power is locked** — At 70k vehicle scale ($1.5-4.3B platform revenue), pricing is constrained by regulatory tolls and customer willingness-to-pay, not Tesla's brand. Take-rate increase from 28% to 35% requires owned fleet and payment infrastructure (both capital-intensive moves).

4. **Cost advantage becomes moot** — $0.42/mile vs $0.68/mile on 70k vehicles = ~$22M annual opex advantage on $1.65B revenue. Immaterial. Infrastructure capex dominates.

**Reality:** Robotaxi becomes a regulated utility, not a competitive market. Winner is determined by infrastructure partnership strategy and regulatory relationships, not vehicle manufacturing or software. Tesla's play must be charging network ownership + fleet (capital-intensive) or pure software licensing to fleet operators (lower margin).

## Integration with Standard CLAUDE.md Analysis

This quantitative model should **inform**:
- **Business model analysis** in `tsla/analysis/YYYY_MM_business_model.md` — robotaxi revenue stream assumptions
- **Competitive analysis** comparing Tesla's scale thesis vs Waymo's unit economics dominance
- **Valuation analysis** with scenario-specific revenue projections fed into DCF
- **Investment thesis** on Tesla's autonomous vehicle optionality and profitability path

Typical workflow:
1. Run base case and three scenarios via `/robotaxi_analysis/run_all_scenarios.py`
2. Extract 2030E and 2035E platform revenue for each scenario
3. Assess whether Tesla's cost advantage ($0.42 vs $0.68/mile) can offset Waymo's margin advantage
4. Document assumptions and sensitivity in formal analysis documents

## Accessing the Shared Model

See [`robotaxi_analysis/README.md`](../../robotaxi_analysis/README.md) for:
- Full model documentation
- All customization options (rollout timeline, market share, assumptions)
- CLI usage and export formats (CSV, JSON)
- Scenario definitions and knob explanations

### Quick Start

From `/robotaxi_analysis/` directory:

```bash
# View all scenarios
python3 run_all_scenarios.py

# Export to CSV for analysis
python3 run_all_scenarios.py --csv tesla_waymo_comparison.csv

# Adjust Tesla vs Waymo market share
python3 run_all_scenarios.py --market-share-json '{"tesla":0.6,"waymo":0.4}'

# Run single scenario with custom assumptions
python3 robotaxi_revenue_model.py --scenario hypergrowth --market-json '{"us_metro_population_full": 300000000}'
```

---

**Last updated:** 2026-05-20  
**Key Question:** Does Tesla's cost advantage ($0.42/mile) materialize fast enough to defend against Waymo's structural margin advantage?
