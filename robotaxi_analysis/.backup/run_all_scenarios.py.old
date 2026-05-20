#!/usr/bin/env python3
"""
Run `robotaxi_revenue_model` for every scenario (slow, base, hypergrowth,
platform_dominance) and print one consolidated ASCII table.

Uses the same priors and flags as the main model where applicable.
"""

from __future__ import annotations

import argparse
import json
import sys

from robotaxi_revenue_model import (
    MarketPriors,
    ScenarioName,
    SupplyConstraints,
    YearResult,
    _apply_market_overlay,
    _load_json_optional,
    _parse_rollout_json,
    default_profiles,
    default_rollout_grid,
    results_to_rows,
    run_projection,
    write_csv,
)


def _parse_companies(raw: str) -> set[str]:
    return {s.strip().lower() for s in raw.split(",") if s.strip()}


def _resolve_market_shares(active: set[str], market_share_json: str) -> dict[str, float]:
    if market_share_json:
        share = json.loads(market_share_json)
    else:
        n = max(len(active), 1)
        share = {slug: 0.5 for slug in active} if n == 2 else {slug: 1.0 / n for slug in active}

    s_total = sum(share.get(slug, 0.0) for slug in active)
    if s_total <= 0:
        raise ValueError("Market shares must sum to > 0 for active companies.")
    if s_total > 1.0001:
        print(
            f"Warning: market shares sum to {s_total:.3f} (>1); scaling down proportionally.",
            file=sys.stderr,
        )

    if s_total > 1.0:
        return {slug: share.get(slug, 0.0) / s_total for slug in active}
    return {slug: float(share.get(slug, 0.0)) for slug in active}


def _print_consolidated_table(results: list[YearResult], stream=sys.stdout) -> None:
    headers = (
        "scenario",
        "year",
        "company",
        "reach_pop_m",
        "eff_cov_m",
        "fleet_k",
        "gross_b",
        "plat_b",
    )
    widths = (22, 4, 7, 10, 10, 10, 10, 10)
    stream.write(" | ".join(f"{h:>{widths[i]}}" for i, h in enumerate(headers)) + "\n")
    stream.write("-" * (sum(widths) + 3 * (len(headers) - 1)) + "\n")

    company_order = {"tesla": 0, "waymo": 1}
    scenario_order = {s.value: i for i, s in enumerate(ScenarioName)}
    sorted_rows = sorted(
        results,
        key=lambda r: (
            scenario_order.get(r.scenario, 99),
            r.year,
            company_order.get(r.company, 99),
        ),
    )

    for r in sorted_rows:
        parts = (
            r.scenario,
            f"{r.year}",
            r.company,
            f"{r.reachable_pop / 1e6:.1f}",
            f"{r.effective_covered_pop / 1e6:.1f}",
            f"{r.fleet_operating / 1e3:.1f}",
            f"{r.gross_passenger_revenue / 1e9:.2f}",
            f"{r.net_platform_revenue / 1e9:.2f}",
        )
        stream.write(" | ".join(f"{parts[i]:>{widths[i]}}" for i in range(len(headers))) + "\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--start-year", type=int, default=2026)
    p.add_argument("--end-year", type=int, default=2035)
    p.add_argument(
        "--companies",
        default="tesla,waymo",
        help="Comma-separated slugs (tesla, waymo).",
    )
    p.add_argument(
        "--market-share-json",
        default="",
        help='Optional JSON dict, e.g. \'{"tesla":0.45,"waymo":0.2}\'',
    )
    p.add_argument(
        "--theoretical-us-fleet-terminal",
        type=float,
        default=4_500_000.0,
    )
    p.add_argument("--market-json", default="", help="Overlay numeric MarketPriors fields.")
    p.add_argument("--rollout-json", default="", help="Replace rollout anchor table (JSON array).")
    p.add_argument("--csv", default="", help="Write all rows to this CSV path.")
    p.add_argument("--json", default="", help="Write all rows to this JSON path.")
    p.add_argument("--quiet", action="store_true", help="Suppress ASCII table.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    profiles = default_profiles()
    active = _parse_companies(args.companies)
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

    if args.start_year > args.end_year:
        print("--start-year must be <= --end-year.", file=sys.stderr)
        return 2

    years = list(range(args.start_year, args.end_year + 1))
    market = MarketPriors()
    market = _apply_market_overlay(market, _load_json_optional(args.market_json))

    try:
        normalized = _resolve_market_shares(active, args.market_share_json)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 2

    all_results: list[YearResult] = []
    supply_constraints = SupplyConstraints()
    for scenario_name in ScenarioName:
        all_results.extend(
            run_projection(
                years=years,
                scenario_name=scenario_name,
                profiles=profiles,
                active=active,
                market=market,
                rollout_grid=rollout,
                theoretical_us_fleet_terminal=args.theoretical_us_fleet_terminal,
                market_share=normalized,
                supply_constraints=supply_constraints,
                use_enhancements=True,
            )
        )

    if not args.quiet:
        _print_consolidated_table(all_results)
    if args.csv:
        write_csv(all_results, args.csv)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results_to_rows(all_results), f, indent=2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
