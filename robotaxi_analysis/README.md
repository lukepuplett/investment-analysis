# Waymo vs. Tesla Robotaxi Revenue Projection Model

**Out-of-band analysis for Google/Waymo investment thesis.**

This directory contains a probabilistic revenue model for autonomous ride-hailing services, comparing Tesla and Waymo under four scenario frameworks. The model translates physical network constraints (reachable population → effective coverage → demand → fleet utilization) into financial outcomes (gross platform revenue and take-rate capture).

## BLUF (Bottom Line Up Front)

**Waymo's premium unit economics ($1.90 fare, 35% take-rate) generate 16% higher annual platform revenue than Tesla's mass-market model ($1.10 fare, 28% take-rate) across all scenarios despite 56% smaller fleet size. Base case 2035 (annual): Waymo $21.18B platform revenue (401.1k fleet) vs Tesla $18.18B (922.1k fleet). Cost advantage alone ($0.42 vs $0.68/mile) does not overcome Tesla's margin disadvantage; unit economics favor Waymo's regulated premium network thesis over Tesla's abundance strategy. Robotaxi platform TAM scales from $9.97B/year (slow) to $60.88B/year (platform dominance), but Waymo wins profitability in all scenarios.**

## Quick Start

### Basic Usage

Run the model across all four scenarios:

```bash
python3 run_all_scenarios.py
```

Output: consolidated ASCII table with scenario, year, company, and key metrics.

### Save to CSV or JSON

```bash
python3 run_all_scenarios.py --csv all_scenarios.csv
python3 run_all_scenarios.py --json all_scenarios.json
```

### Single Scenario

To run just one scenario (e.g., base case):

```bash
python3 robotaxi_revenue_model.py --scenario base
```

## Model Architecture

### Simulation Layers

1. **Market Priors** — US metro population (280M), baseline trip rates (rideshare + taxi), private vehicle substitution ceiling
2. **Rollout Grid** — City count and reachable population by year (default: 2026–2035)
3. **Company Profiles** — Tesla (mass-market, lower fare) vs Waymo (premium regulated, higher fare)
4. **Scenarios** — Four storylines with knob variations:
   - **Slow**: regulatory drag, 0.65× velocity, 0.85× demand elasticity
   - **Base**: gradual scaling, 1.0× velocity, 1.0× elasticity
   - **Hypergrowth**: rapid adoption, 1.25× velocity, 1.35× elasticity
   - **Platform Dominance**: winner-take-most, 1.15× velocity, 1.5× elasticity, network effects

### Key Parameters

**Company Profile** (Tesla vs Waymo):

| Parameter | Tesla | Waymo | Meaning |
|-----------|-------|-------|---------|
| Economic Coverage Fraction | 0.78 | 0.55 | Fraction of reachable pop economically viable |
| Paid Miles/Vehicle/Day | 180 | 220 | Revenue-generating miles per vehicle |
| Fare/Mile | $1.10 | $1.90 | Passenger-facing price per mile |
| Take Rate | 0.28 | 0.35 | Platform's % cut of gross revenue |
| Supply Ramp Cap | 0.22 | 0.12 | Max annual % of terminal fleet deployed |
| Cost/Autonomous Mile | $0.42 | $0.68 | Operating cost per mile (fuel, maintenance, ops) |

**Market Priors**:
- US metro population: 280M
- Baseline rideshare trips/capita/year: 18
- Baseline taxi trips/capita/year: 4
- Average trip miles: 8
- Private car substitution pool: 220 trips/capita/year at terminal
- Terminal substitution fraction: 8% (80-90M annual rides captured)

## Output Columns

```
scenario       | Scenario name (slow, base, hypergrowth, platform_dominance)
year           | Calendar year
company        | Tesla or Waymo
reach_pop_m    | Reachable population (millions)
eff_cov_m      | Effectively covered population (millions)
fleet_k        | Operating fleet size (thousands of vehicles)
gross_b        | Gross passenger revenue (billions USD, annual)
plat_b         | Net platform revenue after take-rate (billions USD, annual)
```

**All revenue figures are annualized for the given calendar year (not quarterly or monthly).**

## Customization

### Change Market Assumptions

Overlay market priors as JSON:

```bash
python3 run_all_scenarios.py --market-json '{"us_metro_population_full": 300000000}'
```

### Adjust Rollout Timeline

Replace the rollout grid with custom city/population targets:

```bash
python3 run_all_scenarios.py --rollout-json rollout_custom.json
```

JSON format:
```json
[
  {"year": 2026, "cities": 10, "reachable_population_millions": 25},
  {"year": 2027, "cities": 25, "reachable_population_millions": 80},
  ...
]
```

### Set Market Share

Control demand split between Tesla and Waymo:

```bash
python3 run_all_scenarios.py --market-share-json '{"tesla":0.6,"waymo":0.4}'
```

## Interpreting Results

### Example (Base Case, 2035, Annual Revenue)

| Company | Reach_pop_m | Eff_cov_m | Fleet_k | Gross_b/year | Plat_b/year |
|---------|-------------|-----------|---------|--------------|-------------|
| Tesla   | 370.3       | 288.8     | 922.1   | $64.92       | $18.18      |
| Waymo   | 283.4       | 155.8     | 401.1   | $60.51       | $21.18      |

**Interpretation (Annual Figures):**
- **Tesla**: Reaches 370.3M metro population with 288.8M economically viable (78% effective coverage). Operates 922.1k vehicles, generating $64.92B annual gross passenger revenue and retaining $18.18B annual platform revenue (28% take-rate).
- **Waymo**: Smaller reachable market (283.4M) yields 155.8M economically viable (55% effective coverage). Leaner fleet (401.1k vehicles) with higher fares ($1.90/mi) and better take-rate (35%) generates $60.51B annual gross on $21.18B annual platform revenue—16% higher platform revenue despite 56% fewer vehicles.

### Key Insights

1. **Coverage vs Economics**: Tesla's wider geographic coverage (78%) is offset by lower unit economics. Waymo's tighter focus (55%) achieves better profitability per vehicle.
2. **Supply Discipline**: Tesla can ramp fleet faster (22% annual cap) but hits demand ceilings. Waymo's constrained ramp (12%) suggests intentional scarcity or regulatory limits.
3. **Revenue Scaling**: Platform revenue = `fleet × paid_miles_day × 365 × fare × take_rate`. Doubling fleet does NOT double platform revenue due to demand elasticity and supply constraints.
4. **Scenario Spread**: Hypergrowth (1.5B vehicles) vs Slow (800k vehicles) diverges dramatically by 2035, especially for Waymo (platform revenue ranges $200M → $2.0B+).

## Files

- `robotaxi_revenue_model.py` — Core simulation engine; run single scenario with `--scenario` flag
- `run_all_scenarios.py` — Runner that executes all four scenarios and consolidates results
- `README.md` — This file

## Notes

- **No external dependencies** — stdlib only (argparse, csv, json, dataclasses, enum)
- **Defaults to 2026–2035** — Change with `--start-year` and `--end-year`
- **Market share normalization** — If shares don't sum to 1.0, they're auto-normalized to preserve ratio
- **Readiness friction** — Accounts for autonomous system maturity via `miles_per_intervention` (lower = more interventions = higher friction)

## Roadmap for Expansion

Potential enhancements (not implemented):
- Ride-pooling dynamics (shared vs solo rides)
- Cannibalization of existing rideshare (Uber/Lyft)
- International rollout (Europe, Asia)
- Integration with freight/delivery revenue streams
- Competitive pricing endgame (race to lowest fare)
- Fleet ownership models (owned vs contractor-backed)
