"""
SpaceX orbital AI data centre — bottom-up physics, BOM, launch & development cost model.
Units: USD (M or B noted in output), metric tonnes, kW/MW/GW unless stated.
Legend on each input: HARD | PROXY | GUESS — see INPUTS table in README.md.
Run:  python3 spcx/orbital/orbital_dc_model.py  → output.md + charts/*.png
Do not edit spcx/model/ (terrestrial model is separate).
"""
from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(HERE, "charts")

# =============================================================================
# INPUTS — low / base / high where ranges apply; single value if fixed (HARD).
# Tuple: (low, base, high, tag, source)
# =============================================================================

SIGMA_SB = 5.670374419e-8  # W/m²/K⁴ — HARD (CODATA)

INPUTS: Dict[str, Tuple] = {
    # --- orbit & sun ---
    "orbit_altitude_km": (600, 650, 800, "PROXY", "Suncatcher illustrative cluster 650 km; SSO band"),
    "orbit_type": ("SSO dawn-dusk", "SSO dawn-dusk", "SSO dawn-dusk", "PROXY", "Suncatcher / Google blog 2025"),
    "solar_constant_wm2": (1361, 1361, 1361, "HARD", "AM0 solar constant"),
    "eclipse_fraction": (0.00, 0.02, 0.08, "GUESS", "Dawn-dusk SSO ~0; PSAO/LEO alternative"),
    "cell_efficiency_bol": (0.20, 0.28, 0.32, "PROXY", "Suncatcher ~22–32%; Starlink-class CIGS/silicon"),
    "cell_degradation_per_yr": (0.015, 0.02, 0.03, "PROXY", "GEO-style LEO literature"),
    "array_packing_factor": (0.75, 0.85, 0.92, "GUESS", "Deployable array gap fill"),
    "pe_efficiency": (0.92, 0.95, 0.97, "GUESS", "DC bus power electronics"),
    # --- compute definition (1 GW = IT load) ---
    "it_load_gw": (1.0, 1.0, 1.0, "HARD", "Model definition: 1 GW IT (accelerator) load"),
    "space_pue": (1.25, 1.45, 1.75, "GUESS", "Bus power / IT; no chillers; solar+rad losses"),
    "kw_per_accelerator": (1.0, 1.2, 1.7, "PROXY", "COLOSSUS ~210 MW / 110k GPU ≈ 1.9 kW; GB200 rack 120 kW/72"),
    "accelerator_cost_usd_k": (25, 35, 50, "PROXY", "Baker $35B IT / GW; H100/B200 ASP ranges"),
    "accelerators_replacement_yr": (3, 4, 6, "GUESS", "Brief + Suncatcher 5 yr TID vs terrestrial 3–5 yr"),
    "ecc_shielding_premium_it_pct": (0.05, 0.12, 0.25, "GUESS", "Rad-tolerant packaging / derating"),
    # --- thermal (Stefan–Boltzmann); two-sided radiators ---
    "radiator_temp_k": (300, 330, 360, "GUESS", "Aerospace reject temp vs COTS limit"),
    "radiator_emissivity": (0.85, 0.90, 0.95, "PROXY", "Coated OSR / deployable films"),
    "radiator_view_factor_space": (0.75, 0.85, 0.92, "GUESS", "Earth IR + albedo occlusion in LEO"),
    "radiator_areal_mass_kg_m2": (2.0, 3.5, 6.0, "GUESS", "Deployable fins; ISS P6 ~order 3–5"),
    "fluid_loop_kg_per_mw": (50, 120, 250, "GUESS", "Pumps/loop per rejected MW"),
    # --- radiation ---
    "tid_krad_yr": (10, 15, 25, "PROXY", "Suncatcher ~150 rad(Si)/yr ≈ 1.5 krad/yr with shielding quote"),
    "shielding_kg_per_m2_10mm_al": (27, 27, 27, "HARD", "10 mm Al ≈ 27 kg/m² area equiv."),
    "shielded_envelope_fraction": (0.10, 0.20, 0.40, "GUESS", "Fraction of bus needing heavy shielding"),
    # --- mass anchors (tonnes per GW IT) — bottom-up cross-check ---
    "mass_it_hardware_t": (1500, 2200, 3200, "PROXY", "Starcloud 100 t / 40 MW → 2500 t; lighter modular"),
    "mass_solar_t": (800, 1400, 2500, "GUESS", "km²-scale arrays; kg/kW 2–7"),
    "mass_radiator_t": (600, 1200, 2200, "GUESS", "From physics + areal mass"),
    "mass_structure_bus_t": (400, 800, 1500, "GUESS", "Starlink V2 bus scale-up"),
    "mass_power_electronics_t": (150, 300, 500, "GUESS", "DCDC, battery (eclipse), PMAD"),
    "mass_comms_isl_t": (100, 250, 600, "PROXY", "Starlink laser mesh; training bisection BW"),
    "mass_propulsion_prop_t": (80, 150, 300, "PROXY", "Hall thrusters + prop for 10–15 yr station-keeping"),
    "mass_integration_margin_pct": (0.10, 0.15, 0.25, "GUESS", "I&T, tools, secondary structure"),
  # Total mass cap (Starcloud ~2k t/GW modular vs physics-upper ~15k t) — low/base/high
    "mass_total_cap_t": (2800, 6500, 15000, "GUESS", "Starcloud 100t/40MW×25 + rad; physics upper ~15k t"),
    # --- $/kg launch (marginal internal SpaceX scenarios) ---
    "launch_usd_per_kg": (10, 50, 200, "GUESS", "Brief $10–200/kg; Suncatcher Starship $15–250"),
    "launch_usd_per_kg_f9_proxy": (1500, 2200, 3000, "PROXY", "Falcon 9 ~$2–3M / ~10–15 t commercial"),
    "starship_payload_t": (40, 100, 150, "GUESS", "Brief 100–150 t reusable; Flight 14 suborbital deploy test"),
    # --- non-launch hardware $/GW (ex-IT); compare to Baker $25B avoided power/cooling ---
    "cost_it_usd_b": (32, 35, 42, "PROXY", "Baker $35B IT / GW; Epoch ~$27–41B IT share"),
    "cost_orbital_power_thermal_usd_b": (6, 12, 22, "GUESS", "Solar+rad+batteries vs $25B terrestrial avoided"),
    "cost_spacecraft_bus_usd_b": (2, 5, 10, "GUESS", "Bus + structure per GW constellation"),
    "cost_comms_usd_b": (1, 3, 8, "GUESS", "ISL + ground stations amortized"),
    "cost_ops_insurance_lifecycle_usd_b": (2, 6, 18, "GUESS", "Ground stations, insurance, SSA; NOT FOUND filed tariff"),
    "lifecycle_chip_replacement_usd_b": (5, 12, 28, "GUESS", "1–2 accelerator generations in mission life"),
    "launch_cost_usd_b_direct": (0.5, 5.0, 12.0, "GUESS", "Bottom-up $/kg vs Baker $5B/GW at Starship reuse (PROXY)"),
    "mission_life_yr": (10, 12, 15, "GUESS", "Replacement vs disposal"),
    # --- development programme (amortized $/GW at scale) ---
    "dev_orbital_platform_usd_b": (15, 30, 60, "GUESS", "Starlink dev comp; no filed orbital DC budget"),
    "dev_starship_to_full_reuse_usd_b": (5, 15, 30, "GUESS", "Cumulative Starship spend proxy; sunk for SpaceX"),
    "dev_headcount_peak": (2000, 5000, 12000, "GUESS", "Platform + ops engineering"),
    "dev_cost_per_head_usd_k_yr": (250, 350, 500, "PROXY", "SpaceX blended engineer $"),
    "dev_timeline_first_gw_yr": (2030, 2032, 2035, "GUESS", "424B4 orbital AI “as early as 2028”; 1 GW later"),
    "gw_cumulative_at_dev_amort": (10, 25, 100, "GUESS", "GW over which to spread dev"),
    # --- terrestrial comparator (Baker / filings) ---
    "terrestrial_all_in_usd_b_gw": (50, 60, 70, "PROXY", "Baker $60B; Orennia ~$60B; Epoch ~$38B low"),
    "terrestrial_it_only_usd_b": (35, 38, 42, "PROXY", "Baker $35B IT; Orennia ~70% IT"),
    "terrestrial_power_cooling_usd_b": (18, 25, 30, "PROXY", "Baker $25B avoided in orbit narrative"),
    # --- cadence physics ---
    "starship_launches_per_day_max": (0.5, 1.0, 3.0, "GUESS", "Starcloud “3/day” aspiration; pads limit"),
    "active_pads": (2, 3, 5, "PROXY", "Starbase, LC-39A, SLC-37, future offshore"),
}

STELLAR_SOURCE_NOTE = (
    "Starship reuse (Nov 2026): Super Heavy caught 3×; Ship splashdown until Flight 15 "
    "(target 13 Nov 2026) first ship catch attempt — SpaceX updates / Flight 15 page (PROXY)."
)


@dataclass
class Scenario:
    name: str
    idx: int  # 0=low(bull orbit), 1=base, 2=high(bear orbit)


def pick(key: str, sc: Scenario) -> float:
    lo, base, hi, *_ = INPUTS[key]
    return (lo, base, hi)[sc.idx]


def bus_power_kw(sc: Scenario) -> float:
    return pick("it_load_gw", sc) * 1e6 * pick("space_pue", sc)


def radiator_area_m2(waste_kw: float, sc: Scenario) -> float:
    t = pick("radiator_temp_k", sc)
    eps = pick("radiator_emissivity", sc)
    vf = pick("radiator_view_factor_space", sc)
    q_area = 2.0 * eps * SIGMA_SB * (t**4) * vf  # W/m² two-sided
    return (waste_kw * 1000.0) / q_area


def solar_array_area_m2(bus_kw: float, sc: Scenario) -> float:
    eff = pick("cell_efficiency_bol", sc) * pick("array_packing_factor", sc) * pick("pe_efficiency", sc)
    eclipse = pick("eclipse_fraction", sc)
    # Size for average insolation; battery covers eclipse energy (mass in battery sizing)
    insolation = pick("solar_constant_wm2", sc) * (1.0 - 0.5 * eclipse)
    return (bus_kw * 1000.0) / (insolation * eff)


def mass_from_physics(sc: Scenario) -> Dict[str, float]:
    bus_kw = bus_power_kw(sc)
    rad_m2 = radiator_area_m2(bus_kw, sc)
    sol_m2 = solar_array_area_m2(bus_kw, sc)
    rad_mass = rad_m2 * pick("radiator_areal_mass_kg_m2", sc) / 1000.0  # tonnes
    # solar mass: use kg/kW heuristic
    kg_per_kw = (2.5, 4.0, 7.0)[sc.idx]
    sol_mass = bus_kw * kg_per_kw / 1000.0
    return {
        "radiator_area_km2": rad_m2 / 1e6,
        "solar_array_area_km2": sol_m2 / 1e6,
        "radiator_mass_t_physics": rad_mass,
        "solar_mass_t_physics": sol_mass,
        "waste_heat_mw": bus_kw / 1000.0,
        "bus_power_mw": bus_kw / 1000.0,
    }


def total_mass_t(sc: Scenario) -> Tuple[float, Dict[str, float]]:
    phys = mass_from_physics(sc)
    components = {
        "it_hardware": pick("mass_it_hardware_t", sc),
        "solar_arrays": max(pick("mass_solar_t", sc), phys["solar_mass_t_physics"] * 0.85),
        "radiators_thermal": max(pick("mass_radiator_t", sc), phys["radiator_mass_t_physics"] * 0.85),
        "structure_bus": pick("mass_structure_bus_t", sc),
        "power_electronics_batteries": pick("mass_power_electronics_t", sc),
        "comms_isl": pick("mass_comms_isl_t", sc),
        "propulsion_propellant": pick("mass_propulsion_prop_t", sc),
    }
    shield = (
        pick("shielding_kg_per_m2_10mm_al", sc)
        * pick("shielded_envelope_fraction", sc)
        * 20000  # m² proxy shielded area per GW — GUESS
        / 1000.0
    )
    components["radiation_shielding"] = shield
    subtotal = sum(components.values())
    margin = subtotal * pick("mass_integration_margin_pct", sc)
    physics_total = subtotal + margin
    cap = pick("mass_total_cap_t", sc)
    # Use physics-informed sum capped by architecture scenario (Starcloud-style vs upper physics)
    if sc.idx == 0:
        total = min(physics_total, cap)
    elif sc.idx == 1:
        total = cap
    else:
        total = max(physics_total, cap)
    components["integration_margin"] = margin
    components["physics_mass_t"] = physics_total
    components["total"] = total
    return total, {**components, **phys}


def hardware_cost_usd_b(sc: Scenario) -> Dict[str, float]:
    it = pick("cost_it_usd_b", sc) * (1 + pick("ecc_shielding_premium_it_pct", sc))
    other = {
        "orbital_power_thermal": pick("cost_orbital_power_thermal_usd_b", sc),
        "spacecraft_bus": pick("cost_spacecraft_bus_usd_b", sc),
        "comms_ground": pick("cost_comms_usd_b", sc),
    }
    out = {"it_stack": it, **other}
    out["hardware_subtotal"] = sum(out.values())
    return out


def launch_cost_usd_b(mass_t: float, sc: Scenario) -> float:
    bottom_up = mass_t * 1000.0 * pick("launch_usd_per_kg", sc) / 1e9
    return max(bottom_up, pick("launch_cost_usd_b_direct", sc) * (0.85 if sc.idx == 2 else 1.0))


def dev_cost_per_gw_usd_b(sc: Scenario) -> float:
    platform = pick("dev_orbital_platform_usd_b", sc)
    starship = pick("dev_starship_to_full_reuse_usd_b", sc) * 0.3  # marginal attribution GUESS
    hc = pick("dev_headcount_peak", sc) * pick("dev_cost_per_head_usd_k_yr", sc) / 1e6
    timeline = pick("dev_timeline_first_gw_yr", sc) - 2026
    program = platform + starship + hc * timeline * 0.5
    return program / pick("gw_cumulative_at_dev_amort", sc)


def ops_lifecycle_usd_b(sc: Scenario) -> float:
    return pick("cost_ops_insurance_lifecycle_usd_b", sc)


def total_cost_per_gw(sc: Scenario) -> Dict[str, float]:
    mass, _ = total_mass_t(sc)
    hw = hardware_cost_usd_b(sc)
    launch = launch_cost_usd_b(mass, sc)
    dev = dev_cost_per_gw_usd_b(sc)
    ops = ops_lifecycle_usd_b(sc)
    chip_refresh = pick("lifecycle_chip_replacement_usd_b", sc)
    install = hw["hardware_subtotal"] + launch
    total = install + dev + ops + chip_refresh
    return {
        "mass_t": mass,
        "flights_per_gw": mass / pick("starship_payload_t", sc),
        **hw,
        "launch": launch,
        "development_amort": dev,
        "ops_lifecycle": ops,
        "chip_refresh_lifecycle": chip_refresh,
        "capex_install_usd_b": install,
        "total_usd_b": total,
    }


def breakeven_launch_usd_kg(sc: Scenario, terrestrial_usd_b: float, lifecycle: bool = False) -> float:
    """Solve $/kg where orbital hardware + launch equals terrestrial benchmark."""
    mass, _ = total_mass_t(sc)
    c = total_cost_per_gw(sc)
    if lifecycle:
        non_launch = c["total_usd_b"] - c["launch"]
    else:
        non_launch = c["capex_install_usd_b"] - c["launch"]
    if mass <= 0:
        return float("nan")
    need_launch_b = terrestrial_usd_b - non_launch
    if need_launch_b <= 0:
        return 0.0
    return need_launch_b * 1e9 / (mass * 1000.0)


def cadence_rows() -> List[Dict]:
    sc = Scenario("base", 1)
    mass, _ = total_mass_t(sc)
    flights_per_gw = mass / pick("starship_payload_t", sc)
    rows = []
    for gw_yr in (1, 10, 100):
        flights = flights_per_gw * gw_yr
        launches_day = flights / 365.0
        pad_days = launches_day / pick("starship_launches_per_day_max", sc) / pick("active_pads", sc)
        rows.append(
            {
                "gw_per_yr": gw_yr,
                "mass_t_yr": mass * gw_yr,
                "flights_yr": flights,
                "flights_per_day": launches_day,
                "min_pads_at_max_cadence": pad_days,
            }
        )
    return rows


def write_output_md(results: Dict) -> None:
    path = os.path.join(HERE, "output.md")
    bear = results["bear"]  # high cost
    base = results["base"]
    bull = results["bull"]
    be = results["breakeven_kg_base_vs_60b"]
    lines = [
        "# Orbital AI data centre — model output",
        "",
        f"*Generated by `orbital_dc_model.py`. {STELLAR_SOURCE_NOTE}*",
        "",
        "## BLUF",
        "",
        f"**At 1 GW IT load, all-in orbital capex is ~**${bull['total_usd_b']:.0f}B** (bull) / "
        f"**${base['total_usd_b']:.0f}B** (base) / **${bear['total_usd_b']:.0f}B** (bear) vs "
        f"terrestrial **$50–60B/GW** (Baker/Orennia). Launch is **${base['launch']:.1f}B** "
        f"({base['launch']/base['total_usd_b']*100:.0f}% of base) at "
        f"**{pick('launch_usd_per_kg', Scenario('base',1)):.0f} $/kg** and "
        f"**{base['mass_t']:.0f} t/GW**.",
        "",
        f"First-install capex (ex-dev/ops/refresh): **${base['capex_install_usd_b']:.1f}B** (base).",
        "",
        f"Breakeven launch **${be:.0f}/kg** (base install, vs **$60B** terrestrial all-in).",
        "",
        f"**{base['flights_per_gw']:.0f} Starship flights/GW** at **{pick('starship_payload_t', Scenario('base',1)):.0f} t** payload.",
        "",
        "## $/GW summary (USD B)",
        "",
        "| Component | Bull (low $) | Base | Bear (high $) |",
        "|-----------|-------------:|-----:|--------------:|",
    ]
    for key in ["it_stack", "orbital_power_thermal", "spacecraft_bus", "comms_ground", "launch",
                "capex_install_usd_b", "development_amort", "ops_lifecycle", "chip_refresh_lifecycle", "total_usd_b"]:
        label = key.replace("_", " ").title()
        lines.append(
            f"| {label} | {bull[key]:.2f} | {base[key]:.2f} | {bear[key]:.2f} |"
        )
    lines.extend(["", "## Mass & flights (per GW IT)", ""])
    for name, sc_i, label in [("bull", 0, "Bull"), ("base", 1, "Base"), ("bear", 2, "Bear")]:
        mass, comp = total_mass_t(Scenario(name, sc_i))
        lines.append(f"### {label}: **{mass:.0f} t**")
        for k, v in comp.items():
            if k.endswith("_km2") or k.endswith("_mw"):
                lines.append(f"- {k}: {v:.3f}")
            elif isinstance(v, float) and k != "total":
                lines.append(f"- {k}: {v:.0f} t")
        lines.append("")

    lines.append("## Deployment cadence (base case)")
    lines.append("")
    lines.append("| GW/yr | Mass/yr (kt) | Flights/yr | Flights/day | Implied pad load |")
    lines.append("|------:|-------------:|-----------:|------------:|-----------------:|")
    for row in cadence_rows():
        lines.append(
            f"| {row['gw_per_yr']} | {row['mass_t_yr']/1000:.1f} | {row['flights_yr']:.0f} | "
            f"{row['flights_per_day']:.2f} | {row['min_pads_at_max_cadence']:.1f}× max cadence |"
        )
    lines.append("")
    lines.append("## Charts")
    lines.append("")
    for fn in sorted(os.listdir(CHARTS)):
        if fn.endswith(".png"):
            lines.append(f"![{fn}](charts/{fn})")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def make_charts(results: Dict) -> None:
    os.makedirs(CHARTS, exist_ok=True)
    labels = ["Bull", "Base", "Bear"]
    totals = [results["bull"]["total_usd_b"], results["base"]["total_usd_b"], results["bear"]["total_usd_b"]]
    earth = pick("terrestrial_all_in_usd_b_gw", Scenario("base", 1))

    # 1) Stacked cost waterfall (base)
    b = results["base"]
    cats = ["IT", "Power+thermal", "Bus", "Comms", "Launch", "Dev", "Ops", "Refresh"]
    vals = [
        b["it_stack"], b["orbital_power_thermal"], b["spacecraft_bus"], b["comms_ground"],
        b["launch"], b["development_amort"], b["ops_lifecycle"], b["chip_refresh_lifecycle"],
    ]
    fig, ax = plt.subplots(figsize=(9, 5))
    bottom = 0
    colors = plt.cm.viridis(np.linspace(0.15, 0.85, len(cats)))
    for c, v, col in zip(cats, vals, colors):
        ax.bar("Orbital base", v, bottom=bottom, label=c, color=col)
        bottom += v
    ax.axhline(earth, color="crimson", linestyle="--", linewidth=2, label=f"Terrestrial ${earth:.0f}B")
    ax.set_ylabel("USD B per GW IT")
    ax.set_title("Orbital $/GW (base) vs terrestrial comparator")
    ax.legend(loc="upper left", fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "cost_per_gw_waterfall.png"), dpi=150)
    plt.close(fig)

    # 2) Scenario comparison
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(len(labels))
    ax.bar(x, totals, color=["#2ecc71", "#3498db", "#e74c3c"])
    ax.axhline(earth, color="k", linestyle="--", label=f"Terrestrial ${earth:.0f}B")
    ax.axhline(pick("terrestrial_it_only_usd_b", Scenario("base", 1)), color="gray", linestyle=":",
               label="Terrestrial IT only")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("USD B / GW")
    ax.set_title("Orbital all-in capex scenarios")
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "orbital_vs_terrestrial.png"), dpi=150)
    plt.close(fig)

    # 3) Breakeven $/kg curve (base mass, vary $/kg)
    sc = Scenario("base", 1)
    mass, _ = total_mass_t(sc)
    c0 = total_cost_per_gw(sc)
    non_launch = c0["capex_install_usd_b"] - c0["launch"]
    kg = np.linspace(5, 300, 100)
    orbital = non_launch + mass * 1000 * kg / 1e9
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(kg, orbital, label="Orbital all-in")
    for ter, lbl in [(60, "$60B Baker"), (50, "$50B mid"), (38, "$38B Epoch low")]:
        ax.axhline(ter, linestyle="--", alpha=0.7, label=f"Terrestrial {lbl}")
    be = breakeven_launch_usd_kg(Scenario("base", 1), 60.0, lifecycle=False)
    ax.axvline(be, color="orange", linestyle=":", label=f"Breakeven vs $60B: ${be:.0f}/kg")
    ax.set_xlabel("Launch $/kg")
    ax.set_ylabel("USD B / GW")
    ax.set_title("Breakeven launch cost (base hardware)")
    ax.legend(fontsize=7)
    ax.set_xlim(0, 300)
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "breakeven_launch_kg.png"), dpi=150)
    plt.close(fig)

    # 4) Mass breakdown (base)
    _, comp = total_mass_t(Scenario("base", 1))
    mass_keys = [k for k in comp if k not in ("total",) and not k.endswith("_km2") and not k.endswith("_mw")
                 and not k.startswith("radiator_mass") and not k.startswith("solar_mass")]
    mvals = [comp[k] for k in mass_keys]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(mass_keys, mvals, color="#5dade2")
    ax.set_xlabel("Tonnes per GW IT")
    ax.set_title("Mass stack (base)")
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "mass_per_gw.png"), dpi=150)
    plt.close(fig)

    # 5) Radiator area vs IT load (physics)
    loads = np.linspace(0.1, 2.0, 40)
    areas = [radiator_area_m2(l * 1e6 * pick("space_pue", Scenario("base", 1)), Scenario("base", 1)) / 1e6
             for l in loads]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(loads, areas, color="#8e44ad")
    ax.set_xlabel("IT load (GW)")
    ax.set_ylabel("Radiator area (km²)")
    ax.set_title("Heat rejection area (Stefan–Boltzmann, base ε,T,vf)")
    ax.axvline(1.0, color="gray", linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "radiator_area_physics.png"), dpi=150)
    plt.close(fig)

    # 6) Cadence
    rows = cadence_rows()
    fig, ax = plt.subplots(figsize=(7, 4))
    gw = [r["gw_per_yr"] for r in rows]
    fpd = [r["flights_per_day"] for r in rows]
    ax.bar([str(g) for g in gw], fpd, color="#e67e22")
    ax.set_ylabel("Starship flights / day")
    ax.set_xlabel("GW deployed per year")
    ax.set_title("Launch cadence demand (base mass & payload)")
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "cadence_flights_per_day.png"), dpi=150)
    plt.close(fig)


def main() -> Dict:
    # Bull orbit = low total cost (idx 0); Bear = high cost (idx 2)
    results = {
        "bull": total_cost_per_gw(Scenario("low", 0)),
        "base": total_cost_per_gw(Scenario("base", 1)),
        "bear": total_cost_per_gw(Scenario("high", 2)),
    }
    results["breakeven_kg_base_vs_60b"] = breakeven_launch_usd_kg(
        Scenario("base", 1), 60.0, lifecycle=False
    )
    results["breakeven_kg_base_vs_40b_baker"] = breakeven_launch_usd_kg(
        Scenario("base", 1), 40.0, lifecycle=False
    )
    make_charts(results)
    write_output_md(results)
    return results


if __name__ == "__main__":
    r = main()
    print("bear/base/bull $/GW (B):", r["bear"]["total_usd_b"], r["base"]["total_usd_b"], r["bull"]["total_usd_b"])
    print("breakeven $/kg vs $60B:", r["breakeven_kg_base_vs_60b"])
    print("flights/GW (base):", r["base"]["flights_per_gw"])
