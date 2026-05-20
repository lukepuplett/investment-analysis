#!/usr/bin/env python3
"""
Layered robotaxi / autonomous network revenue model (Tesla vs Waymo framing).

Interprets revenue as emerging from physical constraints first:
reachable population → effective coverage → induced demand → fleet balance → fare × take rate.

No third-party dependencies (stdlib only).
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Iterable, Mapping


# ---------------------------------------------------------------------------
# Scenarios (Step 7) — shift rollout, elasticity, and supply discipline
# ---------------------------------------------------------------------------


class ScenarioName(str, Enum):
    SLOW = "slow"
    BASE = "base"
    HYPERGROWTH = "hypergrowth"
    PLATFORM_DOMINANCE = "platform_dominance"


@dataclass(frozen=True)
class ScenarioKnobs:
    """Multipliers and demand uplift vs base trajectory."""

    label: str
    regulatory_velocity: float  # scales reachable-pop growth
    demand_elasticity: float  # scales rides/mile intensity on covered population
    induced_demand_multiplier: float  # extra TAM from cheap miles (bandwidth analogy)
    fleet_supply_discipline: float  # <1 => intentionally/rationally capacity-constrained


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


# ---------------------------------------------------------------------------
# Company profiles (Steps 2–4, 8) — technical vs economic coverage, utilization
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CompanyProfile:
    slug: str
    display_name: str
    # Step 3: fraction of *technically* launched pops that are *economically* served well
    economic_coverage_fraction: float
    # Utilization / unit economics (Step 4)
    paid_miles_per_vehicle_day: float
    fare_per_mile_usd: float
    active_hours_per_day: float
    # Marketplace vs owned fleet abstraction: fraction of passenger fare kept by platform
    take_rate: float
    # Step 5: supply curve — max fraction of “theoretical US robotaxi fleet” deployable per year
    annual_supply_ramp_cap_fraction: float
    # Rollout curve shape — multiplier on baseline reachable-pop table (Waymo slower, Tesla faster intent)
    rollout_pace_vs_baseline: float
    # Core driver priors (Step 10 — miles per intervention as readiness / scaling friction)
    miles_per_intervention: float
    cost_per_autonomous_mile_usd: float

    def readiness_friction(self) -> float:
        """Maps intervention mileage to 0–1 friction (higher = more friction). """
        # Logistic-ish: 5k mi ≈ still heavy friction, 50k+ ≈ low friction
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


# ---------------------------------------------------------------------------
# Market & rollout priors (Steps 1–2)
# ---------------------------------------------------------------------------


@dataclass
class MarketPriors:
    """US-oriented priors; replace via JSON overlay for custom runs."""

    us_metro_population_full: float = 280e6
    baseline_rideshare_trips_per_capita_year: float = 18.0
    baseline_taxi_trips_per_capita_year: float = 4.0
    avg_trip_miles_substitute: float = 8.0
    # Private-car miles that could shift partially into robotaxi over time (order-of-magnitude prior)
    private_car_trip_pool_per_capita_year: float = 220.0
    private_car_substitution_fraction_terminal: float = 0.08


@dataclass(frozen=True)
class RolloutYear:
    year: int
    cities: int
    reachable_population_millions: float


def default_rollout_grid() -> list[RolloutYear]:
    """Illustrative rollout — edit or pass --rollout-json to replace."""
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
    """Piecewise linear between anchor years; flat extrapolation beyond ends."""
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


# ---------------------------------------------------------------------------
# Core simulation
# ---------------------------------------------------------------------------


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
) -> YearResult:
    """One company-year; market_share splits TAM between players for demand-side competition."""

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
    trips_pc = (
        (base_trips_pc + private_shift)
        * scenario.demand_elasticity
        * scenario.induced_demand_multiplier
    )
    annual_miles_per_capita = trips_pc * market.avg_trip_miles_substitute

    total_demand_miles = effective_pop * annual_miles_per_capita * market_share_of_robotaxi

    paid_per_vehicle_day = profile.paid_miles_per_vehicle_day * (1.0 - 0.03 * profile.readiness_friction())
    fleet_demand = total_demand_miles / max(paid_per_vehicle_day * 365.0, 1e-6)

    terminal_fraction = min(1.0, adjusted_reachable / max(market.us_metro_population_full, 1.0))
    supply_cap = (
        theoretical_us_fleet_terminal
        * terminal_fraction
        * profile.annual_supply_ramp_cap_fraction
        * supply_ramp_index
        * scenario.fleet_supply_discipline
    )
    fleet_op = max(0.0, min(fleet_demand, supply_cap))

    gross_rev = fleet_op * paid_per_vehicle_day * 365.0 * profile.fare_per_mile_usd
    net_rev = gross_rev * profile.take_rate

    return YearResult(
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
    )


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
                )
            )
    return out


# ---------------------------------------------------------------------------
# IO helpers
# ---------------------------------------------------------------------------


def results_to_rows(results: list[YearResult]) -> list[dict[str, Any]]:
    return [asdict(r) for r in results]


def print_table(results: list[YearResult], stream=sys.stdout) -> None:
    headers = [
        "year",
        "company",
        "reachable_pop_m",
        "eff_cov_pop_m",
        "fleet_op_k",
        "gross_rev_b",
        "platform_rev_b",
        "miveh_day",
    ]
    stream.write(" | ".join(f"{h:>14}" for h in headers) + "\n")
    stream.write("-" * (len(headers) * 17) + "\n")
    for r in results:
        row = [
            f"{r.year:>14}",
            f"{r.company:>14}",
            f"{r.reachable_pop / 1e6:>14.1f}",
            f"{r.effective_covered_pop / 1e6:>14.1f}",
            f"{r.fleet_operating / 1e3:>14.1f}",
            f"{r.gross_passenger_revenue / 1e9:>14.2f}",
            f"{r.net_platform_revenue / 1e9:>14.2f}",
            f"{r.revenue_miles_per_vehicle_day:>14.1f}",
        ]
        stream.write(" | ".join(row) + "\n")


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


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--start-year", type=int, default=2026)
    p.add_argument("--end-year", type=int, default=2035)
    p.add_argument(
        "--scenario",
        choices=[s.value for s in ScenarioName],
        default=ScenarioName.BASE.value,
    )
    p.add_argument(
        "--companies",
        default="tesla,waymo",
        help="Comma-separated slugs from the built-in profile table.",
    )
    p.add_argument(
        "--market-share-json",
        default="",
        help='Optional JSON dict, e.g. \'{"tesla":0.45,"waymo":0.2}\' summing to <=1 implies residual untapped.',
    )
    p.add_argument(
        "--theoretical-us-fleet-terminal",
        type=float,
        default=4_500_000.0,
        help="Order-of-magnitude cap: US robotaxi fleet if fully built out.",
    )
    p.add_argument("--market-json", default="", help="Overlay numeric MarketPriors fields.")
    p.add_argument("--rollout-json", default="", help="Replace rollout anchor table.")
    p.add_argument("--csv", default="", help="Write detailed CSV to this path.")
    p.add_argument("--json", default="", help="Write JSON rows to this path.")
    p.add_argument("--quiet", action="store_true", help="Suppress ASCII table.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    profiles = default_profiles()
    active = {s.strip().lower() for s in args.companies.split(",") if s.strip()}
    unknown = active - profiles.keys()
    if unknown:
        print(f"Unknown company slug(s): {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2

    if args.rollout_json:
        loaded = _load_json_optional(args.rollout_json)
        if not isinstance(loaded, list):
            print("--rollout-json must contain a JSON array of rows.", file=sys.stderr)
            return 2
        rollout = _parse_rollout_json(loaded)
    else:
        rollout = default_rollout_grid()

    years = list(range(args.start_year, args.end_year + 1))
    market = MarketPriors()
    market = _apply_market_overlay(market, _load_json_optional(args.market_json))

    share: dict[str, float] = {}
    if args.market_share_json:
        share = json.loads(args.market_share_json)
    else:
        n = max(len(active), 1)
        share = {slug: 0.5 for slug in active} if n == 2 else {slug: 1.0 / n for slug in active}

    s_total = sum(share.get(slug, 0.0) for slug in active)
    if s_total <= 0:
        print("Market shares must sum to > 0 for active companies.", file=sys.stderr)
        return 2
    if s_total > 1.0001:
        print(f"Warning: market shares sum to {s_total:.3f} (>1); scaling down proportionally.", file=sys.stderr)

    if s_total > 1.0:
        normalized = {slug: share.get(slug, 0.0) / s_total for slug in active}
    else:
        normalized = {slug: float(share.get(slug, 0.0)) for slug in active}

    results = run_projection(
        years=years,
        scenario_name=ScenarioName(args.scenario),
        profiles=profiles,
        active=active,
        market=market,
        rollout_grid=rollout,
        theoretical_us_fleet_terminal=args.theoretical_us_fleet_terminal,
        market_share=normalized,
    )
    if not args.quiet:
        print_table(results)
    if args.csv:
        write_csv(results, args.csv)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results_to_rows(results), f, indent=2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
