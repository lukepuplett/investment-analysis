#!/usr/bin/env python3
"""
Simple scenario runner for optionality analysis.
Extracts 2035 valuation for each scenario.
"""

from robotaxi_revenue_model_enhanced import (
    optionality_scenarios,
    simulate_company_year,
    interpolate_reachable_pop,
    default_profiles,
    MarketPriors,
    default_rollout_grid,
    SupplyConstraints,
)

# Scenario configurations
opt_scen = optionality_scenarios()
scenarios = {
    'Conservative (Transport)': opt_scen['conservative_transport'],
    'Infrastructure Layer': opt_scen['infrastructure_layer'],
    'Natural Monopoly': opt_scen['natural_monopoly'],
}

# Common parameters
years = list(range(2026, 2036))
profiles = default_profiles()
market = MarketPriors()
rollout_grid = default_rollout_grid()
pop_by_year = interpolate_reachable_pop(years, rollout_grid)

# Realistic terminal fleet sizes
TERMINAL_FLEETS = {'waymo': 120_000, 'tesla': 200_000}

print("=" * 110)
print("OPTIONALITY SCENARIOS: 2035 TERMINAL VALUATIONS")
print("=" * 110)

results_all = {}

for scenario_name, scenario_obj in scenarios.items():
    print(f"\n{'='*110}")
    print(f"SCENARIO: {scenario_name}")
    print(f"Inflection Year: {scenario_obj.behavior_change_inflection_year} | "
          f"Market Structure: {scenario_obj.market_structure} | "
          f"Multiples: {scenario_obj.terminal_multiple_tier1:.0f}x/{scenario_obj.terminal_multiple_tier2:.0f}x/{scenario_obj.terminal_multiple_tier3:.0f}x")
    print("=" * 110)

    results_all[scenario_name] = {}

    for company in ['waymo', 'tesla']:
        profile = profiles[company]
        terminal_fleet = TERMINAL_FLEETS[company]

        result = simulate_company_year(
            2035,
            scenario_key=scenario_name,
            profile=profile,
            scenario=scenario_obj,
            market=market,
            base_reachable_pop=pop_by_year[2035],
            start_year=2026,
            theoretical_us_fleet_terminal=terminal_fleet,
            market_share_of_robotaxi=1.0,
            supply_constraints=SupplyConstraints(),
            use_enhancements=True,
        )

        terminal_value = result.net_platform_revenue * result.terminal_implied_multiple
        pv_value = terminal_value * 0.386

        results_all[scenario_name][company] = {
            'fleet': result.fleet_operating,
            'gross_revenue': result.gross_passenger_revenue / 1e9,
            'platform_revenue': result.net_platform_revenue / 1e9,
            'multiple': result.terminal_implied_multiple,
            'terminal_value': terminal_value / 1e9,
            'pv_value': pv_value / 1e9,
        }

        print(f"\n{company.upper():>10}   Fleet: {result.fleet_operating:>8,.0f} | "
              f"Gross Rev: ${result.gross_passenger_revenue/1e9:>6.2f}B | "
              f"Platform Rev: ${result.net_platform_revenue/1e9:>6.2f}B | "
              f"Multiple: {result.terminal_implied_multiple:>5.1f}x | "
              f"Terminal Value: ${terminal_value/1e9:>7.1f}B | "
              f"PV (10% WACC): ${pv_value/1e9:>7.1f}B")

# Summary table
print(f"\n\n{'='*110}")
print("SUMMARY: WAYMO 2035 VALUATION BY SCENARIO")
print("=" * 110)
print(f"{'Metric':<35} {'Conservative':<25} {'Infrastructure':<25} {'Monopoly':<25}")
print("-" * 110)

for metric_key, metric_label in [
    ('platform_revenue', 'Platform Revenue ($B)'),
    ('fleet', 'Fleet (vehicles)'),
    ('multiple', 'Terminal Multiple (x)'),
    ('terminal_value', 'Terminal Value ($B)'),
    ('pv_value', 'Discounted PV ($B)'),
]:
    conservative = results_all['Conservative (Transport)']['waymo'].get(metric_key, 0)
    infrastructure = results_all['Infrastructure Layer']['waymo'].get(metric_key, 0)
    monopoly = results_all['Natural Monopoly']['waymo'].get(metric_key, 0)

    if isinstance(conservative, float) and metric_key != 'fleet':
        c_str = f"${conservative:.2f}B" if 'revenue' in metric_key or 'value' in metric_key else f"{conservative:.1f}x"
        i_str = f"${infrastructure:.2f}B" if 'revenue' in metric_key or 'value' in metric_key else f"{infrastructure:.1f}x"
        m_str = f"${monopoly:.2f}B" if 'revenue' in metric_key or 'value' in metric_key else f"{monopoly:.1f}x"
    else:
        c_str = f"{conservative:,.0f}"
        i_str = f"{infrastructure:,.0f}"
        m_str = f"{monopoly:,.0f}"

    print(f"{metric_label:<35} {c_str:<25} {i_str:<25} {m_str:<25}")

print(f"\n{'='*110}")
print("SUMMARY: TESLA 2035 VALUATION BY SCENARIO")
print("=" * 110)
print(f"{'Metric':<35} {'Conservative':<25} {'Infrastructure':<25} {'Monopoly':<25}")
print("-" * 110)

for metric_key, metric_label in [
    ('platform_revenue', 'Platform Revenue ($B)'),
    ('fleet', 'Fleet (vehicles)'),
    ('multiple', 'Terminal Multiple (x)'),
    ('terminal_value', 'Terminal Value ($B)'),
    ('pv_value', 'Discounted PV ($B)'),
]:
    conservative = results_all['Conservative (Transport)']['tesla'].get(metric_key, 0)
    infrastructure = results_all['Infrastructure Layer']['tesla'].get(metric_key, 0)
    monopoly = results_all['Natural Monopoly']['tesla'].get(metric_key, 0)

    if isinstance(conservative, float) and metric_key != 'fleet':
        c_str = f"${conservative:.2f}B" if 'revenue' in metric_key or 'value' in metric_key else f"{conservative:.1f}x"
        i_str = f"${infrastructure:.2f}B" if 'revenue' in metric_key or 'value' in metric_key else f"{infrastructure:.1f}x"
        m_str = f"${monopoly:.2f}B" if 'revenue' in metric_key or 'value' in metric_key else f"{monopoly:.1f}x"
    else:
        c_str = f"{conservative:,.0f}"
        i_str = f"{infrastructure:,.0f}"
        m_str = f"{monopoly:,.0f}"

    print(f"{metric_label:<35} {c_str:<25} {i_str:<25} {m_str:<25}")

# Stockholder value impact
print(f"\n\n{'='*110}")
print("STOCKHOLDER VALUE IMPACT")
print("=" * 110)
print(f"\nALPHABET (GOOGL): $4.68T market cap | $388/share | 12.06B shares")
print("-" * 110)

for scenario in ['Conservative (Transport)', 'Infrastructure Layer', 'Natural Monopoly']:
    pv = results_all[scenario]['waymo']['pv_value']
    pct = (pv * 1e9) / 4.68e12 * 100
    per_share = (pv * 1e9) / 12.06e9
    print(f"{scenario:<35} ${pv:>7.1f}B PV  ({pct:>5.2f}% cap)  +${per_share:>6.2f}/share")

print(f"\nTESLA (TSLA): $1.60T market cap | $398.87/share | 4.0B shares")
print("-" * 110)

for scenario in ['Conservative (Transport)', 'Infrastructure Layer', 'Natural Monopoly']:
    pv = results_all[scenario]['tesla']['pv_value']
    pct = (pv * 1e9) / 1.60e12 * 100
    per_share = (pv * 1e9) / 4.0e9
    print(f"{scenario:<35} ${pv:>7.1f}B PV  ({pct:>5.2f}% cap)  +${per_share:>6.2f}/share")

print("\n✓ Done")
