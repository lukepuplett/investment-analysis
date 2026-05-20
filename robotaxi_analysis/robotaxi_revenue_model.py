#!/usr/bin/env python3
"""
Enhanced robotaxi revenue model with:
1. Dynamic utilization (network effects + congestion penalty)
2. Supply constraints (manufacturing, charging, service, regulatory, battery)
3. Congestion feedback on demand elasticity
4. Terminal state classification (structure + valuation multiple)

All original functionality preserved; enhancements are layered on top.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Iterable, Mapping

# ---------------------------------------------------------------------------
# ENHANCEMENT 1: Supply Constraints
# ---------------------------------------------------------------------------

@dataclass
class SupplyConstraints:
    """Physical bottlenecks on fleet deployment."""
    manufacturing_capacity_2026: float = 500_000
    charging_points_2026: float = 100_000
    service_centers_2026: int = 100
    battery_supply_lfp_annual_2026: float = 500_000_000  # kWh/year
    robotaxi_battery_share_2026: float = 0.05


def project_supply_constraints(
    year: int,
    scenario_name: str,
    constraints: SupplyConstraints
) -> dict[str, float]:
    """
    Project physical supply constraints on fleet deployment.
    Returns the bottleneck (minimum constraint).
    """

    years = max(0, year - 2026)

    # 1. MANUFACTURING CAPACITY
    # Tesla baseline: 500k/year, grows to 750k over 5 years with capex
    mfg_growth_factor = 1.0 + 0.5 * min(years / 5.0, 1.0)
    manufacturing_cap = constraints.manufacturing_capacity_2026 * mfg_growth_factor

    # 2. CHARGING INFRASTRUCTURE
    # 100k → 500k chargers over 7 years (grid upgrade bottleneck)
    # Assume 2 chargers per vehicle at scale
    chargers_available = constraints.charging_points_2026 * (1.0 + 0.4 * min(years / 7.0, 1.0))
    vehicles_supported_by_charging = chargers_available / 2.0

    # 3. SERVICE/MAINTENANCE NETWORK
    # 100 → 2,000 centers over 7 years
    service_centers = constraints.service_centers_2026 * (1.0 + 0.5 * min(years / 7.0, 1.0))
    vehicles_supported_by_service = service_centers * 500

    # 4. REGULATORY APPROVAL
    # Varies by scenario: % of US metro population approved per year
    if scenario_name == "slow":
        new_approval_rate = 0.03  # 3% per year
    elif scenario_name == "base":
        new_approval_rate = 0.06
    elif scenario_name == "hypergrowth":
        new_approval_rate = 0.12
    else:  # platform_dominance
        new_approval_rate = 0.15

    approved_population = 280_000_000 * min(1.0, new_approval_rate * years)
    # Assume ~500 vehicles per 100k population at terminal
    vehicles_supported_by_regulation = approved_population * 0.005

    # 5. BATTERY SUPPLY
    # Global LFP: 500M kWh/year, growing 30%/year
    # Robotaxi gets 5-10% (starts at 5%, ramps to 10%)
    global_lfp = constraints.battery_supply_lfp_annual_2026 * (1.3 ** years)
    robotaxi_share = constraints.robotaxi_battery_share_2026 + 0.05 * min(years / 5.0, 1.0)
    battery_supply_capacity = (global_lfp * robotaxi_share) / 60.0  # 60 kWh per vehicle

    return {
        "manufacturing": manufacturing_cap,
        "charging": vehicles_supported_by_charging,
        "service": vehicles_supported_by_service,
        "regulatory": vehicles_supported_by_regulation,
        "battery": battery_supply_capacity,
        "bottleneck": min(
            manufacturing_cap,
            vehicles_supported_by_charging,
            vehicles_supported_by_service,
            vehicles_supported_by_regulation,
            battery_supply_capacity
        )
    }


# ---------------------------------------------------------------------------
# ENHANCEMENT 2: Dynamic Utilization with Congestion
# ---------------------------------------------------------------------------

def calculate_utilization(
    year: int,
    profile: CompanyProfile,
    fleet_operating: float,
    reachable_pop: float,
    scenario: ScenarioKnobs
) -> tuple[float, float, float]:
    """
    Calculate dynamic utilization with network effects and congestion penalty.

    Returns: (effective_miles_per_day, network_gain, congestion_penalty)
    """

    years_in_market = max(0, year - 2026)

    # 1. Network effect: +5% per year, capping at +25%
    network_gain = min(0.25, 0.05 * years_in_market)

    # 2. Congestion penalty: logistic curve based on vehicles per 100k population
    # Threshold: 50 vehicles/100k = start of material congestion
    # Steepness: 10 = moderate slope
    vehicles_per_100k = (fleet_operating / max(reachable_pop, 1.0)) * 100_000
    congestion_penalty = 1.0 / (1.0 + math.exp(-(vehicles_per_100k - 50.0) / 10.0))

    # 3. Friction still applies
    friction_discount = 1.0 - 0.03 * profile.readiness_friction()

    # 4. Combine effects
    base_miles = profile.paid_miles_per_vehicle_day
    effective_miles = base_miles * friction_discount * (1.0 + network_gain) * (1.0 - congestion_penalty)

    return effective_miles, network_gain, congestion_penalty


# ---------------------------------------------------------------------------
# ENHANCEMENT 3: Congestion Feedback on Demand
# ---------------------------------------------------------------------------

def apply_congestion_feedback(
    fleet_operating: float,
    reachable_pop: float,
    scenario: ScenarioKnobs
) -> ScenarioKnobs:
    """
    High vehicle density → congestion → slower trips → lower demand elasticity.
    Returns modified scenario with reduced demand_elasticity.
    """

    vehicles_per_100k = (fleet_operating / max(reachable_pop, 1.0)) * 100_000

    # Elasticity factor decreases as density increases
    # At 50 vehicles/100k: factor = 1.0 (no change)
    # At 80 vehicles/100k: factor ≈ 0.60 (40% reduction)
    congestion_elasticity_factor = 1.0 / (1.0 + 0.01 * max(0, vehicles_per_100k - 50))

    adjusted_scenario = ScenarioKnobs(
        label=scenario.label,
        regulatory_velocity=scenario.regulatory_velocity,
        demand_elasticity=scenario.demand_elasticity * congestion_elasticity_factor,
        induced_demand_multiplier=scenario.induced_demand_multiplier,
        fleet_supply_discipline=scenario.fleet_supply_discipline
    )

    return adjusted_scenario


# ---------------------------------------------------------------------------
# ENHANCEMENT 4: Terminal State Classification
# ---------------------------------------------------------------------------

@dataclass
class TerminalState:
    """Classification of terminal market structure and implied valuation."""
    vehicles: float
    average_fare: float
    take_rate: float
    platform_revenue: float
    structure: str
    implied_multiple: int
    gross_margin: float


def classify_terminal_2035(result: YearResult, profile: CompanyProfile) -> TerminalState:
    """
    Classify 2035 terminal state based on economics.
    Maps platform_margin to market structure.
    """

    vehicles = result.fleet_operating
    annual_miles = vehicles * result.revenue_miles_per_vehicle_day * 365.0

    fare_per_mile = result.gross_passenger_revenue / max(annual_miles, 1.0)
    take_rate = result.net_platform_revenue / max(result.gross_passenger_revenue, 1.0)

    # Estimate gross margin
    cost_per_mile = 0.42 if profile.slug == "tesla" else 0.68
    gross_costs = annual_miles * cost_per_mile
    gross_margin = (result.gross_passenger_revenue - gross_costs) / max(result.gross_passenger_revenue, 1.0)

    # Classify by take_rate (platform margin)
    if take_rate <= 0.05:
        structure = "REGULATED UTILITY (3-5% target margin)"
        multiple = 10
    elif take_rate <= 0.15:
        structure = "COMPETITIVE OLIGOPOLY (10-15% margin)"
        multiple = 15
    elif take_rate <= 0.25:
        structure = "STRONG OLIGOPOLY (20-25% margin)"
        multiple = 20
    else:
        structure = "PLATFORM/DUOPOLY (30%+ margin)"
        multiple = 25

    return TerminalState(
        vehicles=vehicles,
        average_fare=fare_per_mile * 8.0,  # Assume 8 mi/trip
        take_rate=take_rate,
        platform_revenue=result.net_platform_revenue,
        structure=structure,
        implied_multiple=multiple,
        gross_margin=gross_margin
    )


# ---------------------------------------------------------------------------
# Original Model Code (with enhancements integrated)
# ---------------------------------------------------------------------------

class ScenarioName(str, Enum):
    SLOW = "slow"
    BASE = "base"
    HYPERGROWTH = "hypergrowth"
    PLATFORM_DOMINANCE = "platform_dominance"


@dataclass(frozen=True)
class ScenarioKnobs:
    label: str
    regulatory_velocity: float
    demand_elasticity: float
    induced_demand_multiplier: float
    fleet_supply_discipline: float


def scenario_library() -> dict[ScenarioName, ScenarioKnobs]:
    return {
        ScenarioName.SLOW: ScenarioKnobs(
            label="Slow adoption — regulatory drag, setbacks",
            regulatory_velocity=0.65,
            demand_elasticity=0.85,
            induced_demand_multiplier=1.15,
            fleet_supply_discipline=0.9,
        ),
        ScenarioName.BASE: ScenarioKnobs(
            label="Base case — gradual scaling",
            regulatory_velocity=1.0,
            demand_elasticity=1.0,
            induced_demand_multiplier=1.35,
            fleet_supply_discipline=1.0,
        ),
        ScenarioName.HYPERGROWTH: ScenarioKnobs(
            label="Hypergrowth — trust + economics win quickly",
            regulatory_velocity=1.25,
            demand_elasticity=1.35,
            induced_demand_multiplier=1.85,
            fleet_supply_discipline=1.0,
        ),
        ScenarioName.PLATFORM_DOMINANCE: ScenarioKnobs(
            label="Platform dominance — winner-take-most dynamics",
            regulatory_velocity=1.15,
            demand_elasticity=1.5,
            induced_demand_multiplier=2.25,
            fleet_supply_discipline=1.05,
        ),
    }


@dataclass(frozen=True)
class CompanyProfile:
    slug: str
    display_name: str
    economic_coverage_fraction: float
    paid_miles_per_vehicle_day: float
    fare_per_mile_usd: float
    active_hours_per_day: float
    take_rate: float
    annual_supply_ramp_cap_fraction: float
    rollout_pace_vs_baseline: float
    miles_per_intervention: float
    cost_per_autonomous_mile_usd: float

    def readiness_friction(self) -> float:
        x = self.miles_per_intervention / 10_000.0
        return 1.0 / (1.0 + math.exp(x - 3.0))


def default_profiles() -> dict[str, CompanyProfile]:
    return {
        "tesla": CompanyProfile(
            slug="tesla",
            display_name="Tesla (mass-market swarm thesis)",
            economic_coverage_fraction=0.78,
            paid_miles_per_vehicle_day=180.0,
            fare_per_mile_usd=1.10,
            active_hours_per_day=18.0,
            take_rate=0.28,
            annual_supply_ramp_cap_fraction=0.22,
            rollout_pace_vs_baseline=1.15,
            miles_per_intervention=12_000.0,
            cost_per_autonomous_mile_usd=0.42,
        ),
        "waymo": CompanyProfile(
            slug="waymo",
            display_name="Waymo (premium regulated network thesis)",
            economic_coverage_fraction=0.55,
            paid_miles_per_vehicle_day=220.0,
            fare_per_mile_usd=1.90,
            active_hours_per_day=20.0,
            take_rate=0.35,
            annual_supply_ramp_cap_fraction=0.12,
            rollout_pace_vs_baseline=0.88,
            miles_per_intervention=35_000.0,
            cost_per_autonomous_mile_usd=0.68,
        ),
    }


@dataclass
class MarketPriors:
    us_metro_population_full: float = 280e6
    baseline_rideshare_trips_per_capita_year: float = 18.0
    baseline_taxi_trips_per_capita_year: float = 4.0
    avg_trip_miles_substitute: float = 8.0
    private_car_trip_pool_per_capita_year: float = 220.0
    private_car_substitution_fraction_terminal: float = 0.08


@dataclass(frozen=True)
class RolloutYear:
    year: int
    cities: int
    reachable_population_millions: float


def default_rollout_grid() -> list[RolloutYear]:
    return [
        RolloutYear(2026, 10, 25),
        RolloutYear(2027, 25, 80),
        RolloutYear(2028, 60, 180),
        RolloutYear(2029, 90, 230),
        RolloutYear(2030, 120, 280),
        RolloutYear(2031, 140, 295),
        RolloutYear(2032, 155, 305),
        RolloutYear(2033, 165, 312),
        RolloutYear(2034, 172, 318),
        RolloutYear(2035, 178, 322),
    ]


def interpolate_reachable_pop(
    years: Iterable[int],
    grid: list[RolloutYear],
) -> dict[int, float]:
    anchors = {r.year: r.reachable_population_millions * 1e6 for r in grid}
    sorted_years = sorted(anchors)
    if not sorted_years:
        return {}

    def pop_at(y: int) -> float:
        if y <= sorted_years[0]:
            return anchors[sorted_years[0]]
        if y >= sorted_years[-1]:
            return anchors[sorted_years[-1]]
        for y0, y1 in zip(sorted_years, sorted_years[1:]):
            if y0 <= y <= y1:
                p0, p1 = anchors[y0], anchors[y1]
                t = (y - y0) / (y1 - y0)
                return p0 + t * (p1 - p0)
        return anchors[sorted_years[-1]]

    return {y: pop_at(y) for y in years}


@dataclass
class YearResult:
    year: int
    scenario: str
    scenario_label: str
    company: str
    reachable_pop: float
    effective_covered_pop: float
    trip_intensity_per_capita: float
    annual_ride_miles_demand: float
    fleet_demand: float
    fleet_supply_cap: float
    fleet_operating: float
    gross_passenger_revenue: float
    net_platform_revenue: float
    revenue_miles_per_vehicle_day: float
    readiness_friction: float
    # NEW: Utilization details
    utilization_efficiency: float = 0.0  # network_gain - congestion_penalty
    congestion_penalty: float = 0.0
    vehicles_per_100k: float = 0.0
    # NEW: Supply constraint bottleneck
    supply_constraints: dict[str, float] = field(default_factory=dict)
    bottleneck_name: str = "none"
    # NEW: Terminal classification
    terminal_structure: str = ""
    terminal_implied_multiple: int = 0


def _terminal_year_index(year: int, start_year: int) -> int:
    return max(0, year - start_year)


def simulate_company_year(
    year: int,
    *,
    scenario_key: str,
    profile: CompanyProfile,
    scenario: ScenarioKnobs,
    market: MarketPriors,
    base_reachable_pop: float,
    start_year: int,
    theoretical_us_fleet_terminal: float,
    market_share_of_robotaxi: float,
    supply_constraints: SupplyConstraints | None = None,
    use_enhancements: bool = True,
) -> YearResult:
    """One company-year with optional enhancements."""

    reg_vel = scenario.regulatory_velocity * profile.rollout_pace_vs_baseline
    adjusted_reachable = base_reachable_pop * reg_vel
    effective_pop = adjusted_reachable * profile.economic_coverage_fraction

    years_elapsed = _terminal_year_index(year, start_year)
    supply_ramp_index = max(1, year - start_year + 1)
    substitution_ramp = min(1.0, years_elapsed / 10.0)

    private_shift = (
        market.private_car_trip_pool_per_capita_year
        * market.private_car_substitution_fraction_terminal
        * substitution_ramp
    )

    base_trips_pc = (
        market.baseline_rideshare_trips_per_capita_year
        + market.baseline_taxi_trips_per_capita_year
    )

    # ENHANCEMENT 3: Apply congestion feedback to demand elasticity
    active_scenario = scenario
    temp_fleet = 0.0
    if use_enhancements:
        # First pass: estimate fleet for congestion feedback
        trips_pc_base = (base_trips_pc + private_shift) * scenario.demand_elasticity * scenario.induced_demand_multiplier
        temp_fleet = (effective_pop * trips_pc_base * market_share_of_robotaxi) / max(profile.paid_miles_per_vehicle_day * 365.0, 1e-6)
        active_scenario = apply_congestion_feedback(temp_fleet, adjusted_reachable, scenario)

    trips_pc = (
        (base_trips_pc + private_shift)
        * active_scenario.demand_elasticity
        * active_scenario.induced_demand_multiplier
    )
    annual_miles_per_capita = trips_pc * market.avg_trip_miles_substitute

    total_demand_miles = effective_pop * annual_miles_per_capita * market_share_of_robotaxi

    # ENHANCEMENT 1: Dynamic utilization instead of static
    if use_enhancements:
        paid_per_vehicle_day, network_gain, congestion_penalty = calculate_utilization(
            year, profile, temp_fleet, adjusted_reachable, active_scenario
        )
        vehicles_per_100k = (temp_fleet / max(adjusted_reachable, 1.0)) * 100_000
    else:
        paid_per_vehicle_day = profile.paid_miles_per_vehicle_day * (1.0 - 0.03 * profile.readiness_friction())
        network_gain = 0.0
        congestion_penalty = 0.0
        vehicles_per_100k = 0.0

    fleet_demand = total_demand_miles / max(paid_per_vehicle_day * 365.0, 1e-6)

    # ENHANCEMENT 2: Supply constraints instead of simple ramp
    if use_enhancements and supply_constraints:
        supply_dict = project_supply_constraints(year, scenario_key, supply_constraints)
        supply_cap = supply_dict["bottleneck"]

        # Find which constraint is binding
        bottleneck_name = min(
            [("manufacturing", supply_dict["manufacturing"]),
             ("charging", supply_dict["charging"]),
             ("service", supply_dict["service"]),
             ("regulatory", supply_dict["regulatory"]),
             ("battery", supply_dict["battery"])],
            key=lambda x: x[1]
        )[0]
    else:
        terminal_fraction = min(1.0, adjusted_reachable / max(market.us_metro_population_full, 1.0))
        supply_cap = (
            theoretical_us_fleet_terminal
            * terminal_fraction
            * profile.annual_supply_ramp_cap_fraction
            * supply_ramp_index
            * active_scenario.fleet_supply_discipline
        )
        supply_dict = {}
        bottleneck_name = "legacy_ramp"

    fleet_op = max(0.0, min(fleet_demand, supply_cap))

    # Recalculate utilization with actual fleet
    if use_enhancements:
        paid_per_vehicle_day, network_gain, congestion_penalty = calculate_utilization(
            year, profile, fleet_op, adjusted_reachable, active_scenario
        )
        vehicles_per_100k = (fleet_op / max(adjusted_reachable, 1.0)) * 100_000

    gross_rev = fleet_op * paid_per_vehicle_day * 365.0 * profile.fare_per_mile_usd
    net_rev = gross_rev * profile.take_rate

    result = YearResult(
        year=year,
        scenario=scenario_key,
        scenario_label=scenario.label,
        company=profile.slug,
        reachable_pop=adjusted_reachable,
        effective_covered_pop=effective_pop,
        trip_intensity_per_capita=trips_pc,
        annual_ride_miles_demand=total_demand_miles,
        fleet_demand=fleet_demand,
        fleet_supply_cap=supply_cap,
        fleet_operating=fleet_op,
        gross_passenger_revenue=gross_rev,
        net_platform_revenue=net_rev,
        revenue_miles_per_vehicle_day=paid_per_vehicle_day,
        readiness_friction=profile.readiness_friction(),
        utilization_efficiency=network_gain - congestion_penalty,
        congestion_penalty=congestion_penalty,
        vehicles_per_100k=vehicles_per_100k,
        supply_constraints=supply_dict,
        bottleneck_name=bottleneck_name,
    )

    # ENHANCEMENT 4: Terminal classification (for 2035)
    if year == 2035:
        terminal = classify_terminal_2035(result, profile)
        result.terminal_structure = terminal.structure
        result.terminal_implied_multiple = terminal.implied_multiple

    return result


def run_projection(
    *,
    years: list[int],
    scenario_name: ScenarioName,
    profiles: dict[str, CompanyProfile],
    active: set[str],
    market: MarketPriors,
    rollout_grid: list[RolloutYear],
    theoretical_us_fleet_terminal: float,
    market_share: dict[str, float],
    supply_constraints: SupplyConstraints | None = None,
    use_enhancements: bool = True,
) -> list[YearResult]:
    scen = scenario_library()[scenario_name]
    pop_by_year = interpolate_reachable_pop(years, rollout_grid)
    start_year = min(years)
    out: list[YearResult] = []
    for y in years:
        for slug in active:
            pr = profiles[slug]
            share = market_share.get(slug, 1.0 / max(len(active), 1))
            out.append(
                simulate_company_year(
                    y,
                    scenario_key=scenario_name.value,
                    profile=pr,
                    scenario=scen,
                    market=market,
                    base_reachable_pop=pop_by_year[y],
                    start_year=start_year,
                    theoretical_us_fleet_terminal=theoretical_us_fleet_terminal,
                    market_share_of_robotaxi=share,
                    supply_constraints=supply_constraints,
                    use_enhancements=use_enhancements,
                )
            )
    return out


def results_to_rows(results: list[YearResult]) -> list[dict[str, Any]]:
    return [asdict(r) for r in results]


def write_csv(results: list[YearResult], path: str) -> None:
    if not results:
        return
    fieldnames = list(asdict(results[0]).keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in results:
            w.writerow(asdict(r))


def _load_json_optional(path: str | None) -> Any:
    if not path:
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _apply_market_overlay(market: MarketPriors, data: Mapping[str, Any]) -> MarketPriors:
    m = asdict(market)
    for k, v in data.items():
        if k in m:
            m[k] = v
    return MarketPriors(**m)


def _parse_rollout_json(data: list[dict[str, Any]]) -> list[RolloutYear]:
    out: list[RolloutYear] = []
    for row in data:
        out.append(
            RolloutYear(
                year=int(row["year"]),
                cities=int(row.get("cities", 0)),
                reachable_population_millions=float(row["reachable_population_millions"]),
            )
        )
    return sorted(out, key=lambda r: r.year)
