# Waymo vs. Tesla Robotaxi Analysis (Shared Model)

**Out-of-band quantitative analysis** — separate from standard CLAUDE.md investment analysis documents.

**Location:** Shared analysis at `/robotaxi_analysis/` (repo root) — also referenced in [`tsla/`](../tsla/ROBOTAXI_ANALYSIS.md).

## BLUF (Bottom Line Up Front)

**Waymo's competitive moat is regulatory trust and premium market dominance, NOT charging infrastructure. The original model's "2-charger bottleneck" was a spreadsheet constraint, not a physical law. Reframed analysis reveals: regulatory approval (not chargers) is the primary binding constraint through 2035. Waymo dominates premium metros (Tier 1: SF, Phoenix, LA) with 89.7% utilization and 32% take-rate, generating $3.5B+ platform revenue from 120k vehicles at 17.3x valuation multiple. Tesla's path (IF vision autonomy matures) is suburban Tier 3 dominance (200k vehicles) at 9.8x multiple with 18% take-rate. For Alphabet: Waymo's real advantage is regulatory relationships + operational competence in high-value markets, not charging logistics. Charging is $500/vehicle/year capex (0.5% of fleet economics) — trivial, solved with capital, never a constraint.**

## ⚠️ MODEL REFRAME (May 2026)

**The original model is SUPERSEDED.** The "charging bottleneck" assumption was incorrect. See [`robotaxi_analysis/REFRAME_ANALYSIS.md`](../robotaxi_analysis/REFRAME_ANALYSIS.md) for complete reframe:

- ✅ **Charging is NOT the bottleneck** — it's elastic capital ($500/vehicle/year, 0.5% of fleet economics)
- ✅ **Regulatory approval is the actual constraint** — gates fleet by metro tier
- ✅ **Waymo's advantage is premium market concentration** — Tier 1 metros (SF, Phoenix) not charger density
- ✅ **Tesla's path is suburban dominance** — IF vision autonomy survives edge cases; constrained by regulatory barriers in premium metros
- ✅ **Different terminal structures** — Waymo 17.3x multiple (utility-scale premium market), Tesla 9.8x (commodity suburban)

---

## Overview

Google (Alphabet) does not directly operate a public robotaxi service, but **Waymo** (Google's autonomous vehicle subsidiary) is the primary competitive counterpart to Tesla's robotaxi ambitions. This shared model compares:

- **Waymo**: Premium metro network (Tier 1: SF, Phoenix, LA) — regulatory trust + high utilization + pricing power
- **Tesla**: Suburban/mass-market swarm (Tier 3: DFW, LA suburbs) — cost advantage *IF* vision autonomy works

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

## Key Insights from Reframed Model (May 2026)

### Base Case (2035 Terminal, Regulatory Approval as Primary Constraint)

| Company | Fleet | Take Rate | Fare/Mile | Platform Revenue | Bottleneck | Valuation Multiple |
|---------|-------|-----------|-----------|------------------|------------|-------------------|
| **Tesla** (Tier 3 dominant)   | **200k** | **18%** | **$1.10** | **$4.2B** | Regulatory | **9.8x** (commodity) |
| **Waymo** (Tier 1 dominant)   | **120k** | **32%** | **$1.90** | **$3.5B** | Regulatory | **17.3x** (utility) |

**Critical Findings (Reframed)**:
- **Different fleet sizes by strategy**, not shared constraint — Waymo focuses Tier 1 (premium), Tesla targets Tier 3 (suburban)
- **Waymo's 73% revenue/vehicle advantage** comes from **premium market concentration + regulatory trust**, not from charger density
- **Regulatory approval is the PRIMARY BOTTLENECK**, not charging. Charging is $500/vehicle/year capex (0.5% of fleet economics) — trivial, solved with capital
- **Utilization efficiency varies by metro and company maturity:**
  - Waymo in SF (Tier 1), 5 years: 89.7% utilization
  - Tesla in suburbs (Tier 3), 1 year: 45.7% utilization
- **Margin structure heavily metro-dependent:** Premium metros (Tier 1) support 25-32% take-rate; suburban (Tier 3) supports 15-18%

### Scenario Implications (Base Case + Sensitivity)

| Scenario | Waymo Fleet | Waymo Revenue | Waymo Multiple | Tesla Fleet | Notes |
|----------|------------|----------------|----------------|------------|-------|
| **Slow** | 90k | $2.5B | 16.5x | 150k | Slower approval, but no constraint collapse |
| **Base** | 120k | $3.5B | 17.3x | 200k | Reference case; regulatory gates expansion |
| **Hypergrowth** | 160k | $5.0B | 17.8x | 300k | Fast approval if safety milestones hit |
| **Tesla Bear** | 120k | $3.5B | 17.3x | <10k | Vision autonomy fails in edge cases |

**Critical Finding**: **Fleet size scales with regulatory approval velocity, not infrastructure scarcity.** Waymo's constraint is regulatory caution (focus on Tier 1); Tesla's is regulatory barriers (vision autonomy proof required) + optionality on autonomy maturity. Scenario variation moves fleet size significantly. Charging constraint has been eliminated.

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

### Waymo's Real Moat (Reframed):
1. **Regulatory trust gates expansion** — Waymo's 2.25x approval velocity in premium metros (vs Tesla's 0.8x) is the primary advantage, not charger density
2. **Premium market focus is optimal** — Tier 1 metros (SF, Phoenix, LA) support 28-32% take-rates; suburban (Tier 3) only 15-18%. Waymo's smaller fleet in better markets generates 3-4× more revenue per vehicle
3. **Operational maturity compounds advantage** — 89.7% utilization efficiency in premium metros after 5 years; safety track record (35k mi/intervention) accelerates regulatory expansion
4. **Ceiling is utility-scale, not platform** — $3-5B platform revenue at 17.3x multiple is real value creation, but different from "winner-take-most" narrative

### Waymo's Risks (Reframed):
1. **Tier 2/3 expansion may require 50%+ margin cuts** — Can Waymo maintain 15-20% take-rate in secondary metros without compromising brand?
2. **Regulatory expansion is slow** — Safety milestones (5B, 10B cumulative miles) gate tier upgrades. Revenue scales slower than manufacturing capacity allows
3. **Tesla's optionality in Tier 3** — If vision autonomy matures, Tesla dominates suburban mass market (200k+ vehicles) with cost advantage, even at low margins

### For Alphabet Investors:
- **Valuation anchor:** Waymo at 120k vehicles, $3.5B platform revenue, 17.3x multiple = $60B+ option value (but utility-scale, not platform-scale)
- **Downside scenario:** Regulatory approval stalls in secondary metros; revenue capped at $2.5B (Slow scenario)
- **Upside scenario:** Safety milestones unlock Tier 2 expansion by 2032; revenue reaches $5B+ by 2035 (Hypergrowth)

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
