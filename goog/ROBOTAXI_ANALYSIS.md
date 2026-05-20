# Waymo vs. Tesla Robotaxi Analysis (Shared Model)

**Out-of-band quantitative analysis** — separate from standard CLAUDE.md investment analysis documents.

**Location:** Shared analysis at `/robotaxi_analysis/` (repo root) — also referenced in [`tsla/`](../tsla/ROBOTAXI_ANALYSIS.md).

## BLUF (Bottom Line Up Front)

**Waymo's robotaxi competitive advantage is structural and survives infrastructure constraints: despite both Waymo and Tesla being capped at ~70k vehicles (2035) by charging bottleneck, Waymo generates 2.6× higher platform revenue ($4.28B vs Tesla's $1.65B) from identical fleet size via 35% take-rate, $1.90/mile fares, and superior utilization. Charging infrastructure (not vehicle demand or manufacturing) is the binding constraint through 2035; winner is determined by charger buildout velocity, not autonomous capability. Robotaxi emerges as a regulated utility network with $3.5–4.4B annual revenue (Waymo), not a $100B+ platform. For Alphabet investors: Waymo represents optionality on a utility-scale business with structural margin dominance, regulatory moat, and infrastructure partnership leverage, rather than winner-take-most platform upside.**

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

### Base Case (2035 Terminal, Enhanced Model with Infrastructure Constraints)

| Company | Fleet | Gross Revenue/Year | Platform Revenue/Year | Bottleneck | Unit Economics |
|---------|-------|-------------------|----------------------|------------|-----------------|
| **Tesla**   | **70k** | **$5.8B** | **$1.65B** | Charging | $1.10 fare, 28% take-rate, $0.42 opex |
| **Waymo**   | **70k** | **$12.2B** | **$4.28B** | Charging | $1.90 fare, 35% take-rate, $0.68 opex |

**Critical Finding (All Figures Annual)**:
- **Identical fleet sizes** (70k each) due to shared charging infrastructure bottleneck (~500k chargers needed, limits both to ~70k vehicles)
- **Waymo's 2.6× revenue advantage** ($4.28B vs $1.65B) comes entirely from pricing power and take-rate structure, not fleet scale
- **Infrastructure is binding constraint**, not demand or manufacturing. Both companies could deploy 200k+ vehicles if charging existed; neither can scale beyond 70k by 2035
- **Margin structure matters more than cost efficiency** in constrained regime. Tesla's $0.42/mile cost advantage is immaterial (~$22M savings on $1.65B revenue)

### Scenario Spread (2035 Annual Platform Revenue, Enhanced Model)

| Scenario | Tesla Fleet | Waymo Fleet | Tesla Revenue | Waymo Revenue | Waymo Advantage | Notes |
|----------|------------|------------|----------------|----------------|-----------------|-------|
| Slow     | 70k | 70k | $1.54B | $3.55B | 2.3× | Slower charging buildout, but same bottleneck |
| Base     | 70k | 70k | $1.65B | $4.28B | 2.6× | Reference case |
| Hypergrowth | 70k | 70k | $1.67B | $4.41B | 2.6× | Faster regulatory approval; charger still binding |
| Platform Dominance | 70k | 70k | $1.67B | $4.37B | 2.6× | Winner-take-most; but still capped by chargers |

**Critical Finding**: Scenario variation **does not move fleet size**. All scenarios converge to identical 70k vehicle caps because all hit the same charging infrastructure bottleneck. Waymo's 2.3–2.6× advantage is structural, not scenario-dependent. The real upside/downside is infrastructure buildout velocity (who deploys chargers faster post-2035), not vehicle manufacturing or regulatory velocity (both immaterial when chargers are binding).

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
