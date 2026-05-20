# Tesla Robotaxi Competitive Analysis (Shared Model)

**Out-of-band quantitative analysis** — competitive modeling for Tesla vs. Waymo autonomous networks.

**Location:** Shared analysis at `/robotaxi_analysis/` (repo root) — also referenced in [`goog/`](../goog/ROBOTAXI_ANALYSIS.md).

## BLUF (Bottom Line Up Front)

**Tesla's robotaxi strategy faces structural profitability constraints vs Waymo: while Tesla's $0.42/mile cost advantage is real, lower take-rate (28% vs 35%) and lower fares ($1.10 vs $1.90/mile) cap annual platform revenue at $18.18B (2035 base case) vs Waymo's $21.18B—a 14% disadvantage despite Tesla's 130% larger fleet. Cost advantage alone cannot offset Waymo's margin dominance; Tesla would need fare power increase (+35% to $1.50+) or take-rate expansion (+25% to 35%) to achieve parity. Robotaxi optionality for Tesla is real but secondary to core business; Waymo's unit economics suggest it will be the more profitable autonomous network operator. (All figures are annual, not quarterly.)**

## Overview

Tesla's robotaxi strategy competes directly with **Waymo** (Google's autonomous vehicle subsidiary). This shared model compares:

- **Tesla**: Mass-market swarm thesis (lower fares, broader geographic coverage, supply-constrained growth)
- **Waymo**: Premium regulated network thesis (higher fares, tighter geographic focus, better unit economics)

## What This Tells You About Tesla

### Tesla's Competitive Positioning

**Advantages:**
- **Coverage breadth** — 88% effective coverage vs Waymo's 55% across base case 2035
- **Fleet scale** — 1.25M vehicles vs Waymo's 807k (55% larger fleet)
- **Lower fares** — $1.10/mile vs $1.90 signals mass-market disruption potential
- **Supply ramp velocity** — 22% annual cap vs Waymo's 12% (faster deployment)
- **Lower cost structure** — $0.42/mile vs $0.68 indicates operational efficiency advantage

**Challenges:**
- **Lower margins** — 28% take-rate vs Waymo's 35% means Tesla captures less of each dollar
- **Supply-constrained model** — Fleet ramp is intentionally capped, not demand-driven
- **Economic coverage gap** — Only 78% of reachable population is economically viable (vs Waymo's tighter 55% but better unit economics)
- **Platform revenue upside capped** — Lower fares × lower take-rate = limited monetization per vehicle

### Base Case Terminal (2035, Annual Revenue)

| Metric | Tesla | Waymo | Delta |
|--------|-------|-------|-------|
| Fleet Operating | 922.1k | 401.1k | Tesla +130% |
| Reachable Population | 370.3M | 283.4M | Tesla +31% |
| Effective Coverage | 288.8M (78%) | 155.8M (55%) | Tesla +85% |
| **Gross Annual Revenue** | **$64.92B** | **$60.51B** | Tesla +7% |
| **Platform Annual Revenue** | **$18.18B** | **$21.18B** | **Waymo +16%** |
| Annual Revenue/Vehicle | $19.7k | $52.8k | Waymo 2.7× |

**Key Insight (All Figures Annual):** Tesla's mass-market strategy (130% more vehicles, lower fares, wider coverage) generates *less* annual platform revenue than Waymo's premium approach. Despite 56% fewer vehicles, Waymo earns 16% more platform revenue annually. This suggests **Waymo has better long-term economics**.

### Scenario Sensitivity (Annual Platform Revenue, 2035)

| Scenario | Tesla/Year | Waymo/Year | Winner |
|----------|-----------|-----------|--------|
| Slow | $8.56B | $9.97B | Waymo |
| Base | $18.18B | $21.18B | Waymo |
| Hypergrowth | $42.04B | $48.97B | Waymo |
| Platform Dominance | $52.26B | $60.88B | Waymo |

**Implication:** Waymo's profitability advantage persists across *all scenarios*, even when total market size varies 2–3×.

## What Tesla Needs for Competitive Parity

1. **Fare power increase** — Move from $1.10 to $1.50+/mile while maintaining volume (requires reduced competition or strong brand)
2. **Take-rate expansion** — Move from 28% to 35%+ (requires owned fleet vs contractor-backed)
3. **Economic coverage improvement** — Move from 78% to 85%+ (requires better unit economics or lower cost structure)
4. **Supply discipline** — Intentional scarcity to maintain pricing power (counterintuitive for Tesla's abundance thesis)

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
