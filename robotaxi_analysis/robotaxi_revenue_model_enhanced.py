#!/usr/bin/env python3
"""
Enhanced robotaxi revenue model with:
1. Dynamic utilization (network effects + congestion penalty)
2. Supply constraints (manufacturing, charging, service, regulatory, battery)
3. Congestion feedback on demand elasticity
4. Terminal state classification (structure + valuation multiple)
5. Optionality scenarios (infrastructure/monopoly vs transport market) [NEW]

All original functionality preserved; enhancements are layered on top.

## Optionality Scenarios (NEW)

The model now supports three market structure assumptions:

1. **Conservative (Transport Market)**:
   - Fixed trips/capita, limited induced demand
   - Terminal multiples: 8-18x (transport economics)
   - Result: $23.4B PV for Waymo (current baseline)

2. **Infrastructure Layer**:
   - 2x induced demand from behavior change starting 2028
   - City OS, logistics, data monetization value
   - Terminal multiples: 15-32x (infrastructure economics)
   - Result: $50-100B PV for Waymo

3. **Natural Monopoly**:
   - Winner-take-most with compounding moats
   - Safety datasets, regulatory preference, city lock-in
   - Terminal multiples: 20-45x (platform monopoly)
   - Result: $100-300B PV for Waymo

Use optionality_scenarios() to access extended scenarios.
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
    """Physical bottlenecks on fleet deployment (regulatory + manufacturing only)."""
    manufacturing_capacity_2026: float = 500_000
    battery_supply_lfp_annual_2026: float = 500_000_000  # kWh/year
    robotaxi_battery_share_2026: float = 0.05


def project_supply_constraints(
    year: int,
    scenario_name: str,
    constraints: SupplyConstraints
) -> dict[str, float]:
    """
    Project supply constraints on fleet deployment.

    KEY CHANGE: Charging is NOT a constraint—it's elastic capital.
    A 350kW charger can serve 15-30 vehicles in fleet ops with orchestrated charging.
    Charging capex ~$50-75k per charger, amortized ~$200-400/vehicle/year. Solve with capital, not scarcity.

    Real constraints:
    1. REGULATORY approval (primary bottleneck)
    2. MANUFACTURING capacity (rarely binds; Tesla can scale to 1M+ units)
    3. BATTERY supply (global LFP growing 30%/yr; robotaxi is 5-10% of market; rarely binds)

    Service centers and charging infrastructure scale linearly with fleet. Not binding.

    Returns the bottleneck (minimum constraint).
    """

    years = max(0, year - 2026)

    # 1. MANUFACTURING CAPACITY
    # Tesla baseline: 500k/year, grows to 750k over 5 years with capex
    mfg_growth_factor = 1.0 + 0.5 * min(years / 5.0, 1.0)
    manufacturing_cap = constraints.manufacturing_capacity_2026 * mfg_growth_factor

    # 2. REGULATORY APPROVAL (PRIMARY BOTTLENECK)
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

    # 3. BATTERY SUPPLY
    # Global LFP: 500M kWh/year, growing 30%/year
    # Robotaxi gets 5-10% (starts at 5%, ramps to 10%)
    global_lfp = constraints.battery_supply_lfp_annual_2026 * (1.3 ** years)
    robotaxi_share = constraints.robotaxi_battery_share_2026 + 0.05 * min(years / 5.0, 1.0)
    battery_supply_capacity = (global_lfp * robotaxi_share) / 60.0  # 60 kWh per vehicle

    return {
        "manufacturing": manufacturing_cap,
        "regulatory": vehicles_supported_by_regulation,
        "battery": battery_supply_capacity,
        "bottleneck": min(
            manufacturing_cap,
            vehicles_supported_by_regulation,
            battery_supply_capacity
        )
    }


# ---------------------------------------------------------------------------
# CHARGING COST MODEL (Not a bottleneck—elastic capital)
# ---------------------------------------------------------------------------

@dataclass
class ChargingCostModel:
    """
    Charging infrastructure as a cost line item, not a bottleneck.

    Assumptions:
    - 350kW charger: $50-75k capex, serves 15-30 vehicles in fleet ops
    - Amortized cost: ~$200-400 per vehicle per year
    - Fleet can adapt: relocation, battery swapping, solar, dynamic pricing
    - Never the binding constraint if revenue justifies deployment
    """
    charger_capex_dollars: float = 60_000  # $60k per charger
    chargers_per_vehicle_needed: float = 0.05  # 1 charger per 20 vehicles (fleet ops)
    annual_maintenance_per_charger: float = 4_000  # $4k/year
    amortization_years: float = 10.0
    can_relocate_depots: bool = True
    can_oversize_overnight: bool = True
    can_use_solar_storage: bool = True


def calculate_charging_capex_per_vehicle(
    model: ChargingCostModel,
    annual_vehicle_miles: float = 65_700.0,  # 180 mi/day * 365 days
    battery_kwh: float = 60.0
) -> dict[str, float]:
    """
    Calculate annual charging infrastructure cost per vehicle.

    Returns amortized capex + maintenance cost per vehicle.
    Shows charging is ~0.5-1.0% of total fleet capex/opex.
    """
    annual_charge_events = annual_vehicle_miles / 150.0  # charge every 150 miles
    charger_hours_per_vehicle = annual_charge_events * 0.25  # 15 min charge (350kW → full in ~20 min)

    chargers_needed = model.chargers_per_vehicle_needed
    capex_per_charger_annual = model.charger_capex_dollars / model.amortization_years
    capex_per_vehicle = chargers_needed * capex_per_charger_annual

    maintenance_per_vehicle = chargers_needed * model.annual_maintenance_per_charger

    total_annual_per_vehicle = capex_per_vehicle + maintenance_per_vehicle

    return {
        "chargers_per_vehicle": chargers_needed,
        "annual_capex_per_vehicle": capex_per_vehicle,
        "annual_maintenance_per_vehicle": maintenance_per_vehicle,
        "total_annual_charging_cost_per_vehicle": total_annual_per_vehicle,
        "pct_of_fleet_capex": (total_annual_per_vehicle / 4_000.0) * 100.0,  # Assume $4k/vehicle/yr fleet capex
    }


# ---------------------------------------------------------------------------
# METRO-TIER FRAMEWORK (Regulatory approval is the binding constraint)
# ---------------------------------------------------------------------------

class MetroTier(int, Enum):
    """Metro segmentation by market structure and company advantage."""
    TIER_1 = 1  # Premium dense cores (SF, Phoenix, LA downtown) — Waymo-favored
    TIER_2 = 2  # Secondary metros (Austin, Denver, secondary suburbs) — Mixed autonomy
    TIER_3 = 3  # Suburban rings — Tesla's sweet spot if autonomy works
    TIER_4 = 4  # Rural (no deployment expected)


@dataclass(frozen=True)
class Metro:
    """Metro-specific characteristics for regulatory and utilization modeling."""
    name: str
    tier: MetroTier
    population_millions: float
    baseline_trip_intensity_per_capita_annual: float  # rides per person per year
    # Company-specific notes (for analysis, not calculation)
    description: str = ""

    def trips_per_vehicle_per_day(self, vehicles: float, population: float) -> float:
        """
        Estimate average trips per vehicle per day for this metro.
        Utilization efficiency depends on market maturity and density.
        """
        if vehicles == 0:
            return 0.0
        # Vehicles per 100k population
        vehicles_per_100k = (vehicles / max(population, 1.0)) * 100_000
        # Higher density → more available trips per vehicle
        # Capped at ~40 trips/day in dense Tier 1 metros
        return min(40.0, 8.0 + 0.1 * vehicles_per_100k)


def regulatory_approval_velocity_by_tier_and_company(
    tier: MetroTier,
    company: str,
    years_in_market: int,
    cumulative_autonomy_miles: float,
    major_incidents: int = 0,
) -> float:
    """
    Company-specific regulatory velocity multiplier by metro tier.

    Waymo: High trust in Tier 1 (premium dense cores), slower in Tier 2/3.
    Tesla: Lower initial trust (pure vision autonomy), faster approval IF safety record holds.

    Returns multiplier on base regulatory velocity (1.0 = baseline, 2.0 = 2x faster, 0.5 = 2x slower).
    """

    # Base velocity by tier (all companies)
    base_velocity = {
        MetroTier.TIER_1: 1.5,  # Fastest (most valuable markets, regulators active)
        MetroTier.TIER_2: 1.0,  # Baseline
        MetroTier.TIER_3: 0.7,  # Slower (suburban, less regulatory urgency)
        MetroTier.TIER_4: 0.0,  # No deployment
    }[tier]

    # Company-specific adjustment
    if company == "waymo":
        # Waymo: strong trust in Tier 1 (+50%), weaker in Tier 2/3
        company_factor = {
            MetroTier.TIER_1: 1.5,  # Preferred in premium markets
            MetroTier.TIER_2: 1.0,
            MetroTier.TIER_3: 0.6,  # Slower expansion into mass market
            MetroTier.TIER_4: 0.0,
        }[tier]

    elif company == "tesla":
        # Tesla: lower initial trust (vision-only), accelerates with safety record
        years_safety_factor = min(1.0, (years_in_market + cumulative_autonomy_miles / 1e9) / 3.0)
        company_factor = {
            MetroTier.TIER_1: 0.3 + 0.7 * years_safety_factor,  # Barriers high; needs proof
            MetroTier.TIER_2: 0.5 + 0.5 * years_safety_factor,  # Faster in secondary metros
            MetroTier.TIER_3: 1.0 + years_safety_factor,  # Fastest in suburbs if safety holds
            MetroTier.TIER_4: 0.0,
        }[tier]
    else:
        company_factor = 1.0

    # Safety incident penalty (major incident → -50% velocity for 2 years)
    incident_penalty = 1.0
    if major_incidents > 0:
        incident_penalty = 0.5

    return base_velocity * company_factor * incident_penalty


def intervention_impact_on_regulatory_velocity(
    miles_per_intervention: int,
    cumulative_autonomy_miles: float,
    years_in_market: int,
) -> float:
    """
    Safety track record impacts regulatory approval velocity.

    Waymo (35,000 mi/intervention):
      → Can expand to Tier 2/3 quickly after 2+ years + 5B cumulative miles

    Tesla (12,000 mi/intervention):
      → Stuck in Tier 3 until safety record matures (5B cumulative miles)
      → OR breaks through fast if vision autonomy continues to improve

    Returns multiplier on regulatory velocity (1.0 = no impact, 0.5 = halved, 1.5 = accelerated).
    """

    # Safety milestone: 5B cumulative miles triggers tier expansion approval
    safety_milestone_1 = 5e9
    safety_milestone_2 = 10e9

    if cumulative_autonomy_miles < safety_milestone_1:
        # Early phase: safety record being built
        # Higher mi/intervention = faster safety milestone achievement
        progress_ratio = cumulative_autonomy_miles / safety_milestone_1
        return 0.7 + 0.3 * progress_ratio  # Ranges 0.7 to 1.0
    elif cumulative_autonomy_miles < safety_milestone_2:
        # Mid phase: proven safe, ready for expansion
        return 1.3
    else:
        # Late phase: mature safety record, aggressive expansion
        return 1.6


def utilization_efficiency_by_company_metro(
    company: str,
    metro: Metro,
    years_in_market: int,
    miles_per_intervention: int,
    cumulative_autonomy_miles: float = 0.0,
) -> float:
    """
    Calculate utilization efficiency (as fraction of peak) based on:
    1. Metro tier (Tier 1 has higher available trips per vehicle)
    2. Company operational maturity (years in market, safety record)
    3. Intervention rate (safety confidence → less remote ops overhead)

    Returns a utilization efficiency factor (0.5 to 1.0, where 1.0 = peak utilization).

    Example output:
    - Waymo in SF Tier 1, 5 years, 50M cumulative miles: 0.92
    - Tesla in suburbs Tier 3, 1 year, 10M cumulative miles: 0.68
    """

    # Base utilization by metro tier
    tier_base = {
        MetroTier.TIER_1: 0.95,  # Dense cores: high trip availability, 240-280 mi/day
        MetroTier.TIER_2: 0.80,  # Secondary metros: moderate availability, 160-200 mi/day
        MetroTier.TIER_3: 0.65,  # Suburban: lower availability, 100-160 mi/day
        MetroTier.TIER_4: 0.0,   # Rural: no deployment
    }.get(metro.tier, 0.0)

    if tier_base == 0.0:
        return 0.0

    # Operational maturity multiplier: improves with years in market
    # Year 1: 0.70 (learning phase), Year 3+: 0.95+ (optimized)
    maturity_factor = 0.70 + 0.08 * min(years_in_market, 3.0)

    # Safety record impact: better mi/intervention → less remote ops, higher utilization
    # Higher mi/intervention = safer autonomy = less overhead
    # Normalize to 35,000 (Waymo baseline); 12,000 (Tesla) scores lower
    safety_factor = 0.85 + 0.15 * min(miles_per_intervention / 35_000.0, 1.0)

    # Cumulative miles bonus: proven at scale
    # 1B miles: 1.0x, 5B miles: 1.05x, 10B+ miles: 1.10x
    safety_milestone_bonus = min(1.10, 1.0 + (cumulative_autonomy_miles / 1e10))

    combined_efficiency = tier_base * maturity_factor * safety_factor * safety_milestone_bonus

    return min(1.0, combined_efficiency)  # Cap at 1.0


def default_metros() -> dict[str, Metro]:
    """Library of US metros for robotaxi deployment modeling."""
    return {
        # TIER 1: Premium dense cores (Waymo-favored, highest utilization potential)
        "sf_east_bay": Metro(
            name="San Francisco/East Bay",
            tier=MetroTier.TIER_1,
            population_millions=7.7,
            baseline_trip_intensity_per_capita_annual=45.0,
            description="Waymo HQ region; highest trip density, best case deployment"
        ),
        "phoenix": Metro(
            name="Phoenix metro",
            tier=MetroTier.TIER_1,
            population_millions=5.0,
            baseline_trip_intensity_per_capita_annual=35.0,
            description="Waymo's most mature deployment; positive regulatory stance"
        ),
        "la_downtown": Metro(
            name="LA downtown",
            tier=MetroTier.TIER_1,
            population_millions=3.5,
            baseline_trip_intensity_per_capita_annual=40.0,
            description="High density, congestion-driven demand for autonomous rides"
        ),
        # TIER 2: Secondary metros (mixed autonomy, balanced deployment)
        "austin": Metro(
            name="Austin metro",
            tier=MetroTier.TIER_2,
            population_millions=2.4,
            baseline_trip_intensity_per_capita_annual=28.0,
            description="Tech-friendly, growing rideshare demand, emerging autonomous"
        ),
        "denver": Metro(
            name="Denver metro",
            tier=MetroTier.TIER_2,
            population_millions=3.2,
            baseline_trip_intensity_per_capita_annual=22.0,
            description="Moderate density, suburban sprawl, test market potential"
        ),
        # TIER 3: Suburban rings (Tesla's sweet spot if autonomy works)
        "dfw_suburbs": Metro(
            name="Dallas-Fort Worth suburbs",
            tier=MetroTier.TIER_3,
            population_millions=4.0,
            baseline_trip_intensity_per_capita_annual=15.0,
            description="Low density, long distances, cost sensitivity high; Tesla's market"
        ),
        "la_suburbs": Metro(
            name="LA suburbs",
            tier=MetroTier.TIER_3,
            population_millions=6.0,
            baseline_trip_intensity_per_capita_annual=12.0,
            description="Sprawling suburban, car-dependent, price-sensitive riders"
        ),
        # TIER 1: Rest of US (other premium metros not explicitly modeled)
        "tier1_other": Metro(
            name="Tier 1 Other (NYC, Boston, Seattle, DC, Miami, etc.)",
            tier=MetroTier.TIER_1,
            population_millions=7.8,
            baseline_trip_intensity_per_capita_annual=38.0,
            description="Remaining premium dense cores (~8 major metros): high trip density, strong regulatory relationships"
        ),
        # TIER 2: Rest of US (other secondary metros)
        "tier2_other": Metro(
            name="Tier 2 Other (Chicago, Atlanta, Nashville, Portland, etc.)",
            tier=MetroTier.TIER_2,
            population_millions=32.7,
            baseline_trip_intensity_per_capita_annual=22.0,
            description="Remaining secondary metros (~25+ mid-size cities): moderate trip density, mixed regulatory stance"
        ),
        # TIER 3: Rest of US (remaining suburban America)
        "tier3_other": Metro(
            name="Tier 3 Other (remaining suburban US)",
            tier=MetroTier.TIER_3,
            population_millions=206.2,
            baseline_trip_intensity_per_capita_annual=12.0,
            description="Vast suburban and exurban America (~200+ smaller metros): low trip density, cost-sensitive, car-dependent"
        ),
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


@dataclass
class MetroAwareTerminalState:
    """2035 terminal state broken down by metro tier.

    Reveals the market structure bifurcation: Waymo dominates premium metros,
    Tesla competes in suburban IF autonomy matures. Different econ models per tier.
    """
    company: str
    total_vehicles: float
    total_platform_revenue: float
    tier_1_vehicles: float
    tier_1_take_rate: float
    tier_1_revenue: float
    tier_2_vehicles: float
    tier_2_take_rate: float
    tier_2_revenue: float
    tier_3_vehicles: float
    tier_3_take_rate: float
    tier_3_revenue: float
    implied_multiple_weighted: float  # Weighted by revenue


def classify_terminal_by_metro_2035(
    company: str,
    total_vehicles: float,
    total_revenue: float,
    regulatory_velocity: float,
    scenario: ScenarioKnobs | None = None,
) -> MetroAwareTerminalState:
    """
    Classify 2035 terminal state by metro tier distribution.

    Shows that Waymo dominates premium (Tier 1) metros with high margins,
    while Tesla's path depends on capturing suburban (Tier 3) volume.

    Returns breakdown by metro tier with appropriate valuation multiples.
    """

    # Estimate fleet distribution by tier based on company strategy and regulatory velocity
    if company == "waymo":
        # Waymo: focuses on Tier 1 premium metros (75% of fleet)
        # Then expands to Tier 2 only after market matures
        tier_1_fraction = 0.75
        tier_2_fraction = 0.25
        tier_3_fraction = 0.0

        tier_1_take_rate = 0.32  # Premium markets, oligopoly structure
        tier_2_take_rate = 0.20  # Mixed autonomy, more competition
        tier_3_take_rate = 0.0
    else:
        # Tesla: IF autonomy works, dominates Tier 3 (suburban)
        # Low tier 1 penetration (regulatory barriers), moderate tier 2
        tier_1_fraction = 0.05
        tier_2_fraction = 0.20
        tier_3_fraction = 0.75

        tier_1_take_rate = 0.08  # Squeezed out by Waymo
        tier_2_take_rate = 0.15
        tier_3_take_rate = 0.18  # Cost-driven market, Tesla's advantage

    # Calculate vehicles and revenue by tier
    tier_1_vehicles = total_vehicles * tier_1_fraction
    tier_2_vehicles = total_vehicles * tier_2_fraction
    tier_3_vehicles = total_vehicles * tier_3_fraction

    tier_1_revenue = tier_1_vehicles * 180.0 * 365.0 * 1.90 * tier_1_take_rate
    tier_2_revenue = tier_2_vehicles * 160.0 * 365.0 * 1.40 * tier_2_take_rate
    tier_3_revenue = tier_3_vehicles * 100.0 * 365.0 * 1.10 * tier_3_take_rate

    # Valuation multiples by tier — determined by market structure
    # Transport economics: 8-18x (based on take-rate margins)
    # Infrastructure economics: 15-32x (network effects, city OS, logistics)
    # Monopoly economics: 20-45x (compounding moats, natural monopoly)
    if scenario is not None:
        tier_1_multiple = scenario.terminal_multiple_tier1
        tier_2_multiple = scenario.terminal_multiple_tier2
        tier_3_multiple = scenario.terminal_multiple_tier3
    else:
        tier_1_multiple = 18  # Default: utility-like in premium metros
        tier_2_multiple = 12  # Default: oligopoly in secondary metros
        tier_3_multiple = 8   # Default: commodity-like in suburban (tight margins)

    # Weighted average multiple
    total_revenue_check = tier_1_revenue + tier_2_revenue + tier_3_revenue
    implied_multiple = (
        (tier_1_revenue / max(total_revenue_check, 1.0)) * tier_1_multiple +
        (tier_2_revenue / max(total_revenue_check, 1.0)) * tier_2_multiple +
        (tier_3_revenue / max(total_revenue_check, 1.0)) * tier_3_multiple
    )

    return MetroAwareTerminalState(
        company=company,
        total_vehicles=total_vehicles,
        total_platform_revenue=total_revenue,
        tier_1_vehicles=tier_1_vehicles,
        tier_1_take_rate=tier_1_take_rate,
        tier_1_revenue=tier_1_revenue,
        tier_2_vehicles=tier_2_vehicles,
        tier_2_take_rate=tier_2_take_rate,
        tier_2_revenue=tier_2_revenue,
        tier_3_vehicles=tier_3_vehicles,
        tier_3_take_rate=tier_3_take_rate,
        tier_3_revenue=tier_3_revenue,
        implied_multiple_weighted=implied_multiple,
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
    behavior_change_inflection_year: int = 9999  # Year when land use/behavior shifts accelerate (default: never)
    market_structure: str = "transport"  # "transport" | "infrastructure" | "monopoly"
    terminal_multiple_tier1: float = 18.0  # Tier 1 multiple (can vary by structure)
    terminal_multiple_tier2: float = 12.0  # Tier 2 multiple
    terminal_multiple_tier3: float = 8.0   # Tier 3 multiple


def optionality_scenarios() -> dict[str, ScenarioKnobs]:
    """
    Extended scenarios exploring robotaxis as infrastructure (not just transport).

    These scenarios model:
    1. Behavior change (land use shifts, second-car elimination, new user cohorts)
    2. Market structure evolution (transport → infrastructure → monopoly)
    3. Terminal multiples that reflect different market dynamics

    Use alongside scenario_library() for comprehensive optionality analysis.
    """
    return {
        "conservative_transport": ScenarioKnobs(
            label="Conservative: Transport market economics (current model)",
            regulatory_velocity=1.0,
            demand_elasticity=1.0,
            induced_demand_multiplier=1.35,
            fleet_supply_discipline=1.0,
            behavior_change_inflection_year=9999,  # Never
            market_structure="transport",
            terminal_multiple_tier1=17.0,
            terminal_multiple_tier2=11.0,
            terminal_multiple_tier3=8.0,
        ),
        "infrastructure_layer": ScenarioKnobs(
            label="Infrastructure: City OS + logistics + data (medium upside)",
            regulatory_velocity=1.1,
            demand_elasticity=1.15,
            induced_demand_multiplier=1.75,  # 2x baseline by 2035 from behavior change
            fleet_supply_discipline=1.0,
            behavior_change_inflection_year=2028,  # Land use shifts accelerate mid-period
            market_structure="infrastructure",
            terminal_multiple_tier1=32.0,  # Utility-scale + network effects
            terminal_multiple_tier2=22.0,
            terminal_multiple_tier3=15.0,
        ),
        "natural_monopoly": ScenarioKnobs(
            label="Monopoly: Winner-take-most with compounding moats (high upside)",
            regulatory_velocity=1.2,
            demand_elasticity=1.25,
            induced_demand_multiplier=1.50,
            fleet_supply_discipline=1.1,
            behavior_change_inflection_year=2030,  # Inflection later, but more dramatic
            market_structure="monopoly",
            terminal_multiple_tier1=45.0,  # Platform + moat compounding
            terminal_multiple_tier2=30.0,
            terminal_multiple_tier3=20.0,
        ),
    }


def scenario_library() -> dict[ScenarioName, ScenarioKnobs]:
    return {
        ScenarioName.SLOW: ScenarioKnobs(
            label="Slow adoption — regulatory drag, setbacks",
            regulatory_velocity=0.65,
            demand_elasticity=0.85,
            induced_demand_multiplier=1.15,
            fleet_supply_discipline=0.9,
            behavior_change_inflection_year=9999,  # Never
            market_structure="transport",
            terminal_multiple_tier1=16.0,
            terminal_multiple_tier2=11.0,
            terminal_multiple_tier3=7.0,
        ),
        ScenarioName.BASE: ScenarioKnobs(
            label="Base case — gradual scaling",
            regulatory_velocity=1.0,
            demand_elasticity=1.0,
            induced_demand_multiplier=1.35,
            fleet_supply_discipline=1.0,
            behavior_change_inflection_year=9999,  # Never
            market_structure="transport",
            terminal_multiple_tier1=18.0,
            terminal_multiple_tier2=12.0,
            terminal_multiple_tier3=8.0,
        ),
        ScenarioName.HYPERGROWTH: ScenarioKnobs(
            label="Hypergrowth — trust + economics win quickly",
            regulatory_velocity=1.25,
            demand_elasticity=1.35,
            induced_demand_multiplier=1.85,
            fleet_supply_discipline=1.0,
            behavior_change_inflection_year=9999,  # Never
            market_structure="transport",
            terminal_multiple_tier1=20.0,
            terminal_multiple_tier2=13.0,
            terminal_multiple_tier3=9.0,
        ),
        ScenarioName.PLATFORM_DOMINANCE: ScenarioKnobs(
            label="Platform dominance — winner-take-most dynamics",
            regulatory_velocity=1.15,
            demand_elasticity=1.5,
            induced_demand_multiplier=2.25,
            fleet_supply_discipline=1.05,
            behavior_change_inflection_year=9999,  # Never
            market_structure="transport",
            terminal_multiple_tier1=22.0,
            terminal_multiple_tier2=14.0,
            terminal_multiple_tier3=10.0,
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
    regulatory_trust_factor: float = 1.0  # 1.0 = baseline; Waymo > Tesla in Tier 1

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
            regulatory_trust_factor=0.65,  # Lower trust initially; vision-only autonomy unproven
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
            regulatory_trust_factor=1.35,  # Higher trust; proven track record, regulatory relationships
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
    # NEW: Intervention rate tracking for regulatory gating
    cumulative_autonomy_miles: float = 0.0  # Cumulative miles with autonomy enabled
    annual_autonomy_miles: float = 0.0      # Miles this year
    major_incidents: int = 0                 # Count of major incidents
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

    # ENHANCEMENT 4: Behavior change inflection (land use shifts, second-car elimination, new user cohorts)
    # If behavior_change_inflection_year is specified and we've reached it, apply additional multiplier
    # This models phase-change demand growth from land use shifts, reduced second-car ownership, etc.
    if use_enhancements and year >= scenario.behavior_change_inflection_year:
        years_past_inflection = year - scenario.behavior_change_inflection_year
        # Inflection amplification: starts at 1.0x, ramps to full effect by +5 years
        behavior_change_multiplier = 1.0 + (scenario.induced_demand_multiplier - 1.0) * min(years_past_inflection / 5.0, 1.0)
        trips_pc = trips_pc * behavior_change_multiplier

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

        # Find which constraint is binding (charging removed—it's elastic capital)
        bottleneck_name = min(
            [("manufacturing", supply_dict["manufacturing"]),
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

    # ENHANCEMENT 5: Intervention rate tracking for regulatory gating
    annual_autonomy_miles = fleet_op * paid_per_vehicle_day * 365.0
    # Cumulative miles: simple approximation based on years elapsed
    # In a real model, this would be accumulated from prior years
    cumulative_autonomy_miles = annual_autonomy_miles * (years_elapsed + 1.0)
    # Major incidents: placeholder (would be scenario-dependent)
    major_incidents = 0

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
        cumulative_autonomy_miles=cumulative_autonomy_miles,
        annual_autonomy_miles=annual_autonomy_miles,
        major_incidents=major_incidents,
    )

    # ENHANCEMENT 4: Terminal classification (for 2035)
    if year == 2035:
        terminal = classify_terminal_2035(result, profile)
        result.terminal_structure = terminal.structure
        result.terminal_implied_multiple = terminal.implied_multiple

    return result


def simulate_company_metro_year(
    year: int,
    metro: Metro,
    company: str,
    profile: CompanyProfile,
    scenario: ScenarioKnobs,
    market: MarketPriors,
    scenario_key: str,
    start_year: int,
    supply_constraints: SupplyConstraints | None = None,
) -> dict[str, any]:
    """
    Simulate a single company-metro-year combination.

    Returns per-metro results: fleet_allocated, revenue, regulatory_gating, utilization_efficiency.
    Applies company-specific regulatory velocity by metro tier and safety track record.

    This is the foundation for metro-by-metro deployment tracking (Task #8).
    """

    years_elapsed = max(0, year - start_year)

    # 1. REGULATORY VELOCITY (company + metro tier specific)
    # Waymo: 2.25x in Tier 1, 0.42x in Tier 3
    # Tesla: 0.8x in Tier 1, 0.94-1.4x in Tier 3
    reg_velocity = regulatory_approval_velocity_by_tier_and_company(
        metro.tier,
        company,
        years_elapsed,
        cumulative_autonomy_miles=0.0,  # Would be tracked per-company per-metro in full implementation
        major_incidents=0,
    )

    # 2. METRO APPROVAL PROBABILITY (cumulative over years)
    # Tier 1: faster approval (2.25x for Waymo, 0.8x for Tesla)
    # Tier 3: slower (0.42x for Waymo, 0.94x for Tesla)
    base_approval_rate = {
        MetroTier.TIER_1: 0.08,  # 8% of metros approve per year
        MetroTier.TIER_2: 0.06,  # 6% per year
        MetroTier.TIER_3: 0.04,  # 4% per year (many metros, slow approval)
        MetroTier.TIER_4: 0.0,
    }.get(metro.tier, 0.0)

    # Adjust by company regulatory velocity
    approval_rate = base_approval_rate * reg_velocity
    approval_probability = min(1.0, approval_rate * years_elapsed)

    # If not approved, fleet = 0
    if approval_probability < 0.5:  # Require 50%+ certainty
        return {
            "metro": metro.name,
            "tier": metro.tier.value,
            "approved": False,
            "approval_probability": approval_probability,
            "fleet_allocated": 0.0,
            "gross_revenue": 0.0,
            "net_revenue": 0.0,
            "utilization_efficiency": 0.0,
            "regulatory_velocity": reg_velocity,
            "paid_miles_per_day": 0.0,
        }

    # 3. UTILIZATION EFFICIENCY (operational maturity)
    utilization_eff = utilization_efficiency_by_company_metro(
        company=company,
        metro=metro,
        years_in_market=years_elapsed,
        miles_per_intervention=profile.miles_per_intervention,
        cumulative_autonomy_miles=0.0,
    )

    # 4. FLEET ALLOCATION (demand × utilization efficiency)
    # Trip demand in this metro: population × trip_intensity × market_share
    # Fleet needed = demand_miles / (paid_miles_per_vehicle_day × 365 × utilization)
    annual_trip_miles = (
        metro.population_millions * 1e6
        * metro.baseline_trip_intensity_per_capita_annual
        * market.avg_trip_miles_substitute
    )
    paid_miles_per_day = profile.paid_miles_per_vehicle_day * utilization_eff

    fleet_demand = annual_trip_miles / max(paid_miles_per_day * 365.0, 1e-6)

    # Cap by approved deployment (phased rollout by tier)
    # Tier 1: faster ramp (up to 30% of terminal by 2030)
    # Tier 3: slower ramp (up to 10% of terminal by 2030)
    deployment_cap_by_tier = {
        MetroTier.TIER_1: 0.003 * years_elapsed,  # 0.3% per year
        MetroTier.TIER_2: 0.002 * years_elapsed,  # 0.2% per year
        MetroTier.TIER_3: 0.001 * years_elapsed,  # 0.1% per year
        MetroTier.TIER_4: 0.0,
    }.get(metro.tier, 0.0)

    fleet_cap = metro.population_millions * 1e6 * deployment_cap_by_tier
    fleet_allocated = approval_probability * min(fleet_demand, fleet_cap)

    # 5. REVENUE CALCULATION
    gross_revenue = fleet_allocated * paid_miles_per_day * 365.0 * profile.fare_per_mile_usd
    net_revenue = gross_revenue * profile.take_rate

    return {
        "metro": metro.name,
        "tier": metro.tier.value,
        "approved": approval_probability >= 0.5,
        "approval_probability": approval_probability,
        "fleet_allocated": fleet_allocated,
        "utilization_efficiency": utilization_eff,
        "gross_revenue": gross_revenue,
        "net_revenue": net_revenue,
        "regulatory_velocity": reg_velocity,
        "paid_miles_per_day": paid_miles_per_day,
    }


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


def run_projection_metro_aware(
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
    use_metros: bool = True,
) -> tuple[list[YearResult], dict[str, list[dict]]]:
    """
    Run projection with metro-by-metro breakdown.

    Returns:
    - list[YearResult]: Company-level aggregates (for compatibility with existing code)
    - dict[str, list[dict]]: Per-metro breakdowns by company slug
    """

    scen = scenario_library()[scenario_name]
    start_year = min(years)
    metros = default_metros()

    # Aggregate results
    company_results: list[YearResult] = []
    metro_results: dict[str, list[dict]] = {slug: [] for slug in active}

    for y in years:
        for slug in active:
            pr = profiles[slug]
            share = market_share.get(slug, 1.0 / max(len(active), 1))

            if use_metros:
                # Per-metro simulation
                metro_fleet_total = 0.0
                metro_revenue_total = 0.0
                metro_data_by_metro = []

                for metro_key, metro in metros.items():
                    metro_result = simulate_company_metro_year(
                        year=y,
                        metro=metro,
                        company=slug,
                        profile=pr,
                        scenario=scen,
                        market=market,
                        scenario_key=scenario_name.value,
                        start_year=start_year,
                        supply_constraints=supply_constraints,
                    )
                    metro_data_by_metro.append(metro_result)
                    metro_fleet_total += metro_result["fleet_allocated"]
                    metro_revenue_total += metro_result["net_revenue"]

                # Store metro breakdown
                metro_results[slug].append(
                    {
                        "year": y,
                        "metro_breakdown": metro_data_by_metro,
                        "fleet_total": metro_fleet_total,
                        "revenue_total": metro_revenue_total,
                    }
                )

                # Create aggregated YearResult for compatibility
                # (National rollout still used for demand/supply, metros for gating)
                pop_by_year = interpolate_reachable_pop(years, rollout_grid)
                base_reachable_pop = pop_by_year[y]
                reg_vel = scen.regulatory_velocity * pr.rollout_pace_vs_baseline

                result = simulate_company_year(
                    y,
                    scenario_key=scenario_name.value,
                    profile=pr,
                    scenario=scen,
                    market=market,
                    base_reachable_pop=base_reachable_pop,
                    start_year=start_year,
                    theoretical_us_fleet_terminal=theoretical_us_fleet_terminal,
                    market_share_of_robotaxi=share,
                    supply_constraints=supply_constraints,
                    use_enhancements=True,
                )
                company_results.append(result)
            else:
                # Original national-level simulation
                pop_by_year = interpolate_reachable_pop(years, rollout_grid)
                result = simulate_company_year(
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
                    use_enhancements=True,
                )
                company_results.append(result)

    return company_results, metro_results


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
