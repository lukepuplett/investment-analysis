#!/usr/bin/env python3
"""
Run optionality scenarios (Conservative/Infrastructure/Monopoly) for Waymo and Tesla.
Extracts 2035 terminal valuations and sensitivity analysis.

Usage:
  python3 run_optionality_scenarios.py
"""

import json
from robotaxi_revenue_model_enhanced import (
    optionality_scenarios,
    scenario_library,
    run_projection,
    simulate_company_year,
    interpolate_reachable_pop,
    default_profiles,
    MarketPriors,
    default_rollout_grid,
    SupplyConstraints,
    ScenarioName,
)


def run_projection_custom_scenario(
    *,
    years: list[int],
    scenario_obj,  # Custom ScenarioKnobs
    scenario_name_label: str,
    profiles: dict,
    active: set,
    market,
    rollout_grid: list,
    theoretical_us_fleet_terminal: float,
    market_share: dict,
    supply_constraints=None,
    use_enhancements: bool = True,
) -> list:
    """Run projection with custom scenario object (not from ScenarioName enum)."""
    if supply_constraints is None:
        supply_constraints = SupplyConstraints()

    pop_by_year = interpolate_reachable_pop(years, rollout_grid)
    start_year = min(years)
    out = []

    for y in years:
        for slug in active:
            pr = profiles[slug]
            share = market_share.get(slug, 1.0 / max(len(active), 1))

            result = simulate_company_year(
                y,
                scenario_key=scenario_name_label,
                profile=pr,
                scenario=scenario_obj,  # Use custom scenario
                market=market,
                base_reachable_pop=pop_by_year[y],
                start_year=start_year,
                theoretical_us_fleet_terminal=theoretical_us_fleet_terminal,
                market_share_of_robotaxi=share,
                supply_constraints=supply_constraints,
                use_enhancements=use_enhancements,
            )
            out.append(result)

    return out


def extract_2035_metrics(results, scenario_name):
    """Extract 2035 terminal metrics from results."""
    for r in results:
        if r.year == 2035:
            return {
                'year': 2035,
                'scenario': scenario_name,
                'company': r.company,
                'fleet_operating': int(r.fleet_operating),
                'gross_passenger_revenue': r.gross_passenger_revenue / 1e9,  # Billions
                'net_platform_revenue': r.net_platform_revenue / 1e9,  # Billions
                'revenue_miles_per_vehicle_day': r.revenue_miles_per_vehicle_day,
                'utilization_efficiency': r.utilization_efficiency,
                'terminal_multiple': r.terminal_implied_multiple,
                'terminal_value_billions': (r.net_platform_revenue * r.terminal_implied_multiple) / 1e9,
                'pv_at_10pct_wacc_billions': (r.net_platform_revenue * r.terminal_implied_multiple * 0.386) / 1e9,
            }
    return None


def run_all_scenarios():
    """Run Conservative, Infrastructure, and Monopoly scenarios for both companies."""

    print("=" * 100)
    print("OPTIONALITY SCENARIOS: CONSERVATIVE vs INFRASTRUCTURE vs NATURAL MONOPOLY")
    print("=" * 100)

    # Common parameters
    years = list(range(2026, 2036))
    profiles = default_profiles()
    market = MarketPriors()
    rollout_grid = default_rollout_grid()
    supply_constraints = SupplyConstraints()

    # Realistic terminal fleet sizes (from analyses)
    TERMINAL_FLEETS = {
        'waymo': 120_000,   # Conservative case
        'tesla': 200_000,   # Conservative case
    }

    # Scenario configurations
    opt_scen = optionality_scenarios()

    scenarios_to_run = {
        'Conservative (Transport)': opt_scen['conservative_transport'],
        'Infrastructure Layer': opt_scen['infrastructure_layer'],
        'Natural Monopoly': opt_scen['natural_monopoly'],
    }

    results_by_company = {}

    # Run each scenario for each company
    for scenario_label, scenario_obj in scenarios_to_run.items():
        print(f"\n{'=' * 100}")
        print(f"SCENARIO: {scenario_label}")
        print(f"{'=' * 100}")
        print(f"  Behavior Change Inflection: {scenario_obj.behavior_change_inflection_year}")
        print(f"  Market Structure: {scenario_obj.market_structure}")
        print(f"  Tier Multiples: {scenario_obj.terminal_multiple_tier1:.0f}x / {scenario_obj.terminal_multiple_tier2:.0f}x / {scenario_obj.terminal_multiple_tier3:.0f}x")
        print(f"  Induced Demand: {scenario_obj.induced_demand_multiplier:.2f}x")

        for company_slug in ['waymo', 'tesla']:
            print(f"\n  {company_slug.upper()}")
            print("-" * 100)

            results = run_projection_custom_scenario(
                years=years,
                scenario_obj=scenario_obj,
                scenario_name_label=scenario_label,
                profiles=profiles,
                active={company_slug},
                market=market,
                rollout_grid=rollout_grid,
                theoretical_us_fleet_terminal=TERMINAL_FLEETS[company_slug],
                market_share={company_slug: 1.0},
                supply_constraints=supply_constraints,
                use_enhancements=True,
            )

            metrics_2035 = extract_2035_metrics(results, scenario_label)

            if metrics_2035:
                if company_slug not in results_by_company:
                    results_by_company[company_slug] = {}
                results_by_company[company_slug][scenario_label] = metrics_2035

                print(f"    Fleet (2035):               {metrics_2035['fleet_operating']:,} vehicles")
                print(f"    Gross Revenue:             ${metrics_2035['gross_passenger_revenue']:.2f}B")
                print(f"    Platform Revenue:          ${metrics_2035['net_platform_revenue']:.2f}B")
                print(f"    Miles/Vehicle/Day:         {metrics_2035['revenue_miles_per_vehicle_day']:.0f}")
                print(f"    Utilization Efficiency:    {metrics_2035['utilization_efficiency']:.1%}")
                print(f"    Terminal Multiple:         {metrics_2035['terminal_multiple']:.1f}x")
                print(f"    Terminal Value (2035):     ${metrics_2035['terminal_value_billions']:.1f}B")
                print(f"    Discounted Value (PV):     ${metrics_2035['pv_at_10pct_wacc_billions']:.1f}B")

    # Print comparison tables
    print("\n\n" + "=" * 100)
    print("COMPARISON: WAYMO (GOOGL)")
    print("=" * 100)
    print(f"{'Metric':<35} {'Conservative':<20} {'Infrastructure':<20} {'Monopoly':<20}")
    print("-" * 100)

    waymo_data = results_by_company.get('waymo', {})
    metrics_keys = [
        ('fleet_operating', 'Fleet (vehicles)', '{:,.0f}'),
        ('net_platform_revenue', 'Platform Revenue ($B)', '${:.2f}B'),
        ('terminal_multiple', 'Terminal Multiple (x)', '{:.1f}x'),
        ('terminal_value_billions', 'Terminal Value ($B)', '${:.1f}B'),
        ('pv_at_10pct_wacc_billions', 'Discounted PV ($B)', '${:.1f}B'),
    ]

    for key, label, fmt in metrics_keys:
        conservative = waymo_data.get('Conservative (Transport)', {}).get(key, 'N/A')
        infrastructure = waymo_data.get('Infrastructure Layer', {}).get(key, 'N/A')
        monopoly = waymo_data.get('Natural Monopoly', {}).get(key, 'N/A')

        if isinstance(conservative, (int, float)):
            c_str = fmt.format(conservative)
            i_str = fmt.format(infrastructure) if isinstance(infrastructure, (int, float)) else 'N/A'
            m_str = fmt.format(monopoly) if isinstance(monopoly, (int, float)) else 'N/A'
        else:
            c_str = str(conservative)
            i_str = str(infrastructure)
            m_str = str(monopoly)

        print(f"{label:<35} {c_str:<20} {i_str:<20} {m_str:<20}")

    print("\n" + "=" * 100)
    print("COMPARISON: TESLA (TSLA)")
    print("=" * 100)
    print(f"{'Metric':<35} {'Conservative':<20} {'Infrastructure':<20} {'Monopoly':<20}")
    print("-" * 100)

    tesla_data = results_by_company.get('tesla', {})

    for key, label, fmt in metrics_keys:
        conservative = tesla_data.get('Conservative (Transport)', {}).get(key, 'N/A')
        infrastructure = tesla_data.get('Infrastructure Layer', {}).get(key, 'N/A')
        monopoly = tesla_data.get('Natural Monopoly', {}).get(key, 'N/A')

        if isinstance(conservative, (int, float)):
            c_str = fmt.format(conservative)
            i_str = fmt.format(infrastructure) if isinstance(infrastructure, (int, float)) else 'N/A'
            m_str = fmt.format(monopoly) if isinstance(monopoly, (int, float)) else 'N/A'
        else:
            c_str = str(conservative)
            i_str = str(infrastructure)
            m_str = str(monopoly)

        print(f"{label:<35} {c_str:<20} {i_str:<20} {m_str:<20}")

    # Stockholder value impact
    print("\n\n" + "=" * 100)
    print("STOCKHOLDER VALUE IMPACT")
    print("=" * 100)
    print(f"\nALPHABET (GOOGL): $4.68T market cap, $388/share, 12.06B shares")
    print("-" * 100)

    for scenario_label in scenarios_to_run.keys():
        if scenario_label in waymo_data:
            pv = waymo_data[scenario_label]['pv_at_10pct_wacc_billions']
            pct_of_cap = (pv * 1e9) / 4.68e12 * 100
            per_share = pv * 1e9 / 12.06e9
            print(f"{scenario_label:<30} ${pv:>7.1f}B PV  ({pct_of_cap:>4.2f}% of cap)  +${per_share:>5.2f}/share")

    print(f"\nTESLA (TSLA): $1.60T market cap, $398.87/share, 4.0B shares")
    print("-" * 100)

    for scenario_label in scenarios_to_run.keys():
        if scenario_label in tesla_data:
            pv = tesla_data[scenario_label]['pv_at_10pct_wacc_billions']
            pct_of_cap = (pv * 1e9) / 1.60e12 * 100
            per_share = pv * 1e9 / 4.0e9
            print(f"{scenario_label:<30} ${pv:>7.1f}B PV  ({pct_of_cap:>4.2f}% of cap)  +${per_share:>5.2f}/share")

    # Save results as JSON
    print("\n\n" + "=" * 100)
    print("Saving results to optionality_scenarios_results.json...")
    print("=" * 100)

    with open('optionality_scenarios_results.json', 'w') as f:
        json.dump(results_by_company, f, indent=2)
    print("✓ Results saved.")

    return results_by_company


if __name__ == '__main__':
    results = run_all_scenarios()
