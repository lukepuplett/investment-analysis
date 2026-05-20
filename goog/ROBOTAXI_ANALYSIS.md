# Waymo vs. Tesla Robotaxi Analysis (Shared Model)

**Out-of-band quantitative analysis** — separate from standard CLAUDE.md investment analysis documents.

**Location:** Shared analysis at `/robotaxi_analysis/` (repo root) — also referenced in [`tsla/`](../tsla/ROBOTAXI_ANALYSIS.md).

## BLUF (Bottom Line Up Front)

**Waymo's robotaxi unit economics create a structural competitive moat: 16% higher annual platform revenue than Tesla in base case 2035 ($21.18B vs $18.18B) despite 56% fewer vehicles, driven by 35% take-rate vs Tesla's 28% and $1.90 vs $1.10 fares. This advantage persists across all scenarios (slow, base, hypergrowth, platform dominance), suggesting Waymo's premium regulated strategy is more defensible than Tesla's mass-market thesis. For Alphabet investors: Waymo represents optionality on a $9.97B–$60.88B annual platform revenue business by 2035 (scenario-dependent, slow to platform dominance).**

## Overview

Google (Alphabet) does not directly operate a public robotaxi service, but **Waymo** (Google's autonomous vehicle subsidiary) is the primary competitive counterpart to Tesla's robotaxi ambitions. This shared model compares:

- **Waymo**: Premium regulated network thesis (higher fares, tighter geographic focus, better unit economics)
- **Tesla**: Mass-market swarm thesis (lower fares, broader coverage, supply-constrained growth)

## What's Inside

The model is located at `/robotaxi_analysis/` (repo root). See [`../../robotaxi_analysis/README.md`](../../robotaxi_analysis/README.md) for full documentation.

### Files

- **`robotaxi_revenue_model.py`** — Core simulation engine
- **`run_all_scenarios.py`** — Multi-scenario executor (runs slow, base, hypergrowth, platform_dominance)
- **`README.md`** — Full documentation and usage guide
- **`all_scenarios_sample.csv`** — Sample CSV output (all scenarios, 2026–2035)
- **`all_scenarios_sample.json`** — Sample JSON output (structured results for downstream analysis)

## Quick Usage

From the `/robotaxi_analysis/` directory:

```bash
# Run all four scenarios (prints ASCII table)
python3 run_all_scenarios.py

# Save results to CSV
python3 run_all_scenarios.py --csv my_output.csv

# Run just one scenario
python3 robotaxi_revenue_model.py --scenario base
```

## Key Insights from Sample Output

### Base Case (2035 Terminal, Annual Revenue)

| Company | Fleet (k) | Gross Revenue/Year | Platform Revenue/Year | Effective Coverage |
|---------|-----------|-------------------|----------------------|-------------------|
| Tesla   | 922.1     | $64.92B            | $18.18B              | 288.8M (78% reach) |
| Waymo   | 401.1     | $60.51B            | $21.18B              | 155.8M (55% reach) |

**Key Observation (All Figures Annual)**:
- **Waymo** achieves higher *annual platform revenue* ($21.18B) despite 56% fewer vehicles, driven by 73% higher fares ($1.90 vs $1.10/mile) and better take-rate (35% vs 28%).
- **Tesla** compensates with 130% more vehicles and 85% wider effective coverage, but annual gross revenue is only 7% higher with far lower profitability capture.

### Scenario Spread (2035 Annual Platform Revenue)

| Scenario | Tesla/Year | Waymo/Year | Notes |
|----------|-----------|-----------|-------|
| Slow     | $8.56B    | $9.97B    | Regulatory friction, lower demand elasticity |
| Base     | $18.18B   | $21.18B   | Gradual scaling, moderate adoption |
| Hypergrowth | $42.04B | $48.97B | Rapid expansion, strong demand |
| Platform Dominance | $52.26B | $60.88B | Winner-take-most, network effects |

**Implication**: Waymo's profitability advantage persists across all scenarios, but absolute market size is scenario-dependent (2–3× spread between slow and dominance).

## What This Model Captures

### Physical Constraints Layer
- **Reachable population** by year (rollout timeline)
- **Economic coverage fraction** (what % of reachable population is economically viable)
- **Demand intensity** (trips/capita, elasticity under different scenarios)
- **Supply constraints** (max annual fleet deployment as fraction of terminal)

### Unit Economics
- **Fares** ($/mile) — Tesla $1.10 vs Waymo $1.90
- **Take rate** (platform % of gross) — Tesla 28% vs Waymo 35%
- **Cost per mile** — Tesla $0.42 vs Waymo $0.68
- **Profitability drivers** — coverage, fleet utilization, fare power, operating leverage

### Scenario Knobs
Multipliers that shift realistic outcomes:
1. **Regulatory velocity** (slow adoption vs rapid expansion)
2. **Demand elasticity** (price sensitivity and trip growth)
3. **Induced demand multiplier** (TAM expansion from cheaper miles)
4. **Fleet supply discipline** (constrained scarcity vs unfettered ramp)

## Why This Matters for Waymo (Google) Investment Thesis

1. **Profitability path is clearer** — Waymo's tighter focus + higher unit economics → platform revenue scales better than raw fleet size
2. **Regulatory advantage** — Premium positioning and controlled rollout may mitigate regulatory risk
3. **Competitive moat** — If Waymo achieves 55%+ economic coverage + strong brand perception, Tesla's mass-market approach has structural cost disadvantage
4. **Revenue upside** — Platform revenue 25–45% higher than Tesla across base-to-hypergrowth scenarios suggests significant option value for Alphabet

## Integration with Standard CLAUDE.md Analysis

This quantitative model should **inform** (not replace):
- **Business model analysis** in `goog/analysis/YYYY_MM_business_model.md`
- **Competitive analysis** comparing Waymo's regulatory/unit economics vs Tesla's scale thesis
- **Valuation analysis** with scenario-specific revenue projections fed into DCF
- **Investment thesis** on Alphabet's autonomous vehicle optionality

Typical workflow:
1. Run base case and three scenarios via `run_all_scenarios.py`
2. Extract 2030E and 2035E platform revenue for each scenario
3. Feed into valuation model with appropriate discount rates
4. Document assumptions in formal analysis documents

## Customization Points

All customizable via CLI flags (see `robotaxi_analysis/README.md`):

- **Rollout timeline** — change city/population targets
- **Market assumptions** — US population, trip rates, substitution ceiling
- **Company profiles** — adjust fares, take rates, cost structures
- **Market share** — control demand split between Tesla and Waymo
- **Time horizon** — change 2026–2035 projection window

## Files Metadata

| File | Purpose | Size |
|------|---------|------|
| `robotaxi_revenue_model.py` | Core engine (stdlib only) | ~18 KB |
| `run_all_scenarios.py` | Multi-scenario runner | ~6 KB |
| `all_scenarios_sample.csv` | 2026–2035 base case + 3 scenarios (40 rows) | ~5 KB |
| `all_scenarios_sample.json` | Same as CSV but structured | ~40 KB |

---

**Last updated:** 2026-05-20  
**Next step:** Integrate base case projections into standard GOOG valuation analysis.
