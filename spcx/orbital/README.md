# SpaceX orbital AI data centre — physics, BOM, and $/GW model

**Assembled:** 11/11/2026  
**Scope:** Bottom-up model for **1 GW IT load** (accelerator power, matching [Baker / TBPN](../analysis/2026_11_model_inputs.md#executive-notes) and terrestrial comps).  
**Runnable model:** `python3 spcx/orbital/orbital_dc_model.py` → [output.md](output.md) and [charts/](charts/).  
**Do not edit** [spcx/model/](../model/) (terrestrial scenario model is maintained separately).

**Legend:** HARD = physical constant or filing; PROXY = cited third-party; GUESS = scenario range; NOT FOUND = no primary source.

## Executive summary

**BLUF: A 1 GW orbital AI data centre is physically plausible in dawn–dusk SSO at multi‑km² solar/radiator scale, but Baker’s ~$30B/GW orbit quote is inconsistent with his own $35B IT + $5B launch (= $40B) unless avoided terrestrial power/cooling is booked twice. This model’s base case lands at ~$64B first-install and ~$84B lifecycle vs ~$60B terrestrial all-in — orbit only wins the Baker arithmetic ($40B consistent) in the bull case (~$45B install) with Starship marginal launch near ~$50/kg and modular Starcloud-style mass (~6.5 kt/GW). The binding constraint is not launch price alone: deploying 100 GW/year implies ~18 Starship flights per day (650 kt), far beyond pad factory capacity.**

| Metric | Bull | Base | Bear |
|--------|-----:|-----:|-----:|
| **Lifecycle $/GW** | $52B | $84B | $150B |
| **First-install $/GW** | ~$45B | ~$64B | ~$122B |
| **Mass / GW** | 2.8 kt | 6.5 kt | 27.6 kt (physics-upper) |
| **Starship flights / GW** | 28 | 65 | 276 |
| vs **$60B** terrestrial | competitive | breakeven launch ~**$123/kg** | never at modeled $/kg |

Sources: model output 11/11/2026; compares to [Orennia](https://orennia.com/insights/what-it-actually-costs-to-build-a-1-gw-data-center), [Epoch AI](https://epoch.ai/data-insights/ai-datacenter-cost-breakdown), [diary Baker entry](../../diary/2026-11.md).

## 1. Physics

### Orbit choice

| Option | Sun | Eclipse | Latency | Notes | Tag |
|--------|-----|---------|---------|-------|-----|
| **Dawn–dusk SSO ~650 km** (base) | Near-continuous | ~0–2% | Higher ground latency to some sites | Google Suncatcher illustrative orbit; constant solar | PROXY |
| Conventional LEO 400–550 km | Good | 30–40% eclipse | Lower | Heavy batteries; Starlink-style | PROXY |
| GEO | Continuous (mostly) | Small | ~240 ms RTT | Huge link budgets for training | GUESS |

**Choice in model:** dawn–dusk sun-synchronous LEO at **650 km** ([Suncatcher paper](https://angadh.com/assets/papers/suncatcher_paper.pdf); [Google blog](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/)).

### Power

| Input | Low | Base | High | Tag | Source |
|-------|-----|------|------|-----|--------|
| Solar constant | 1361 W/m² | 1361 | 1361 | HARD | AM0 |
| Cell efficiency (BOL) | 20% | 28% | 32% | PROXY | Suncatcher table (~22–32%) |
| Eclipse fraction | 0% | 2% | 8% | GUESS | SSO vs generic LEO |
| Space PUE (bus / IT) | 1.25 | 1.45 | 1.75 | GUESS | No chillers; conversion + thermal pumps |

For **1 GW IT**, base **bus power ≈ 1.45 GW** → solar array area **~4.8 km²** (model physics).

### Heat rejection (Stefan–Boltzmann)

Two-sided radiators: \(Q = 2 \,\varepsilon \,\sigma \,A\, T^4 \,f_{\mathrm{view}}\).

| Input | Low | Base | High | Tag |
|-------|-----|------|------|-----|
| Radiator temperature | 300 K | 330 K | 360 K | GUESS |
| Emissivity ε | 0.85 | 0.90 | 0.95 | PROXY |
| View factor to space | 0.75 | 0.85 | 0.92 | GUESS |

Base: **~1.4 km² radiator** rejects **~1.45 GW** waste heat (~3.4 kg/m² deployable mass → **~4.2 kt** radiator mass class before caps). ISS P6-scale deployable radiators used as order-of-magnitude only (NOT FOUND exact NASA $/m² for GW-class farms).

### Radiation

| Item | Value | Tag | Source |
|------|-------|-----|--------|
| Dose rate (shielded LEO) | ~1.5 krad(Si)/yr equivalent | PROXY | Suncatcher §2.3 |
| TPU / accelerator tests | 5 yr TID without hard fail | PROXY | Suncatcher Trillium tests |
| Mitigation | ECC, derate, periodic refresh | GUESS | — |
| Shielding mass | 10–20% envelope @ 10 mm Al equiv. | GUESS | Mass model |

**Chip life:** **3–6 yr** replacement vs **10–15 yr** mission; drives lifecycle $ in model.

### Links

| Link | Training | Inference | Tag |
|------|----------|-----------|-----|
| FSO inter-satellite | Required TB/s bisection within cluster | Same | PROXY — Suncatcher |
| Ground downlink | Bottleneck for large checkpoint sync | Smaller payloads tolerable | PROXY — TBIRD 200 Gbps demo (NASA, 2023) |
| Latency | SSO dawn–dusk penalizes some ground sites | Acceptable for batch inference | PROXY |

**NOT FOUND:** filed SpaceX orbital compute bandwidth tariff.

### Debris, station-keeping

| Item | Base assumption | Tag |
|------|-----------------|-----|
| Propulsion | Hall effect (Starlink heritage) | PROXY |
| Propellant reserve | 80–300 t/GW constellation | GUESS |
| Orbit maintenance | SSO drag lower than 400 km | PROXY |

### Lifetime & replacement

Mission life **12 yr** (GUESS); accelerators refreshed **every 4 yr** (base) → **$12B/GW** lifecycle chip line in model.

## 2. Bill of materials per GW IT

| Line | Base mass (t) | Base hardware ($B) | Tag |
|------|-------------:|-------------------:|-----|
| IT stack (GPUs, memory, network) | 2,200 | 39.2 | PROXY — Baker $35B + rad premium |
| Orbital power + thermal (solar, rad, PE, eclipse battery) | 4,930 + 4,193 (physics split) | 12.0 | GUESS — vs **$25B** terrestrial power/cooling avoided |
| Spacecraft bus / structure | 800 | 5.0 | GUESS |
| Comms (ISL + ground segment share) | 250 | 3.0 | GUESS |
| **Architecture total used** | **6,500** (cap) | **59.2** | — |
| Physics-only upper (no cap) | **14,870** | NOT USED in base $ | GUESS |

**Tonnes/GW summary:** bull **2.8 kt** (Starcloud-styled cap), base **6.5 kt**, bear **27.6 kt** (physics-heavy).

**Comparators**

| Source | Scale | Tag |
|--------|-------|-----|
| [Project Suncatcher](https://angadh.com/assets/papers/suncatcher_paper.pdf) | 81 sats × ~28 kW → **2.26 MW** demo cluster | PROXY |
| [Starcloud white paper](https://starcloudinc.github.io/wp.pdf) | **100 t** / **~40 MW** per Starship launch | PROXY |
| Starlink V2 Mini | **575–800 kg**; ~20–35 kW class (est.) | PROXY |
| SPCX COLOSSUS | 110k GPUs / **210 MW** nameplate | HARD — 424B4 / Q3 PR |

## 3. Launch

| Input | Low | Base | High | Tag |
|-------|-----|------|------|-----|
| Starship payload to SSO (t) | 40 | 100 | 150 | GUESS — brief / Starcloud |
| Marginal $/kg (internal) | 10 | 50 | 200 | GUESS |
| Baker headline **$/GW** launch | — | **5** | — | PROXY — TBPN, reusable Starship |
| Falcon 9 proxy $/kg | 1,500 | 2,200 | 3,000 | PROXY |

**Flights per GW (base):** **65** (= 6,500 t / 100 t).

**$/kg scenarios (base mass 6.5 kt):**

| $/kg | Launch $/GW |
|------|------------:|
| 10 | $0.07B |
| 50 | $0.33B |
| 200 | $1.3B |

Model uses **max(bottom-up, Baker $5B)** in base (PROXY ceiling for allocated internal launch).

### Cadence (base)

| Deploy rate | Mass/yr | Flights/yr | Flights/day |
|------------|--------|-----------|------------:|
| 1 GW/yr | 6.5 kt | 65 | 0.18 |
| 10 GW/yr | 65 kt | 650 | 1.78 |
| 100 GW/yr | 650 kt | **6,500** | **17.8** |

**Pads / factories (PROXY):** Starbase, LC-39A, SLC-37; Starship Flight **15** (13 Nov 2026) targets first **Ship** tower catch — Ship had been ocean splashdown ([SpaceX Flight 15](https://www.spacex.com/launches/starship-flight-15)). Super Heavy caught **3×** before Flight 15 (PROXY). **Raptor production rate:** NOT FOUND audited public number; industry commentary often cites hundreds/year aspirations (GUESS).

## 4. Development programme

| Item | Low | Base | High | Tag |
|------|-----|------|------|-----|
| Orbital DC platform R&D | $15B | $30B | $60B | GUESS — no filing |
| Starship reuse attribution | $5B | $15B | $30B | GUESS — sunk / marginal |
| Peak headcount | 2k | 5k | 12k | GUESS |
| $/head-year | $250k | $350k | $500k | PROXY |
| First **1 GW** online | 2030 | 2032 | 2035 | GUESS — 424B4 “as early as 2028” for orbital AI |
| GW over which R&D amortized | 10 | 25 | 100 | GUESS |

**Amortized dev/GW (base):** ~**$1.6B**.

## 5. Operations

| Item | Base | Tag |
|------|-----|-----|
| Lifecycle ops + insurance + ground | $6B/GW | GUESS — NOT FOUND SpaceX orbital opex |
| Servicing vs disposal | Mostly replace constellation; no filed on-orbit GPU swap plan | NOT FOUND |
| Ground stations | Shared with Starlink laser/RF estate (GUESS synergy) | GUESS |

## Terrestrial comparison

| Case | $/GW | Source |
|------|-----:|--------|
| Baker all-in | 60 | PROXY — TBPN |
| Baker IT only | 35 | PROXY |
| Baker avoided power/cooling | 25 | PROXY |
| Baker orbit (stated) | 30 | PROXY — **arithmetically inconsistent** with $35+$5 |
| Consistent Baker-style orbit | **40** | = $60 − $25 + $5 (per input register) |
| Orennia all-in | ~60 | PROXY |
| Epoch stylized | ~38 | PROXY |

## Breakeven launch $/kg

**vs $60B terrestrial all-in (base hardware, 6.5 kt/GW): ~$123/kg.** Below that, first-install orbital beats $60B even if power/cooling savings are booked; above it, terrestrial wins on capex.

**vs Baker-consistent $40B orbit target:** base install ~$64B → requires lower mass, cheaper orbital power/thermal, or sub-$50/kg **and** sub-$5B allocated launch — bull case only.

## Physics constraints that could kill it

1. **Launch cadence at GW scale** — 100 GW/yr needs **~18 flights/day** (base), exceeding plausible Starship pad throughput (GUESS).
2. **Heat rejection area / occlusion** — km² radiators with formation flight can block IR view factors (Suncatcher §formation flight).
3. **Training network** — bisection bandwidth and ground checkpoint sync at GW scale (NOT FOUND operational architecture).
4. **Accelerator refresh** — radiation + thermal cycling shortens useful life vs terrestrial; lifecycle $ rivals power savings.
5. **Regulation / licensing** — large SSO compute constellations NOT FOUND in ITU/FCC public bundle for SpaceX orbital DC.

## Verdict

Orbit is **not** a near-term capex halving versus $60B/GW terrestrial **unless** Starship reaches **very low marginal $/kg**, **modular mass/GW** stays near **Starcloud-class (~3–7 kt)**, and **orbital power/thermal** stays **below the ~$25B** terrestrial bucket Baker removes. **Launch price alone is insufficient** at GW scale: **mass × flights** dominates the schedule. SpaceX is the only operator that can test this path (Starship + Starlink bus + internal launch), but the **physics-first GW deployment** stresses **radiator area and global launch cadence** more than the podcast-friendly **$5B/GW** line item.

## Files

| Path | Description |
|------|-------------|
| [orbital_dc_model.py](orbital_dc_model.py) | Inputs + physics + cost engine |
| [output.md](output.md) | Latest model run |
| [charts/](charts/) | PNG figures |
| [analysis/2026_11_orbital_physics_cost_model.md](analysis/2026_11_orbital_physics_cost_model.md) | Long-form narrative |

## Related

- [2026_11_model_inputs.md](../analysis/2026_11_model_inputs.md)
- [2026_11_valuation_snapshot.md](../analysis/2026_11_valuation_snapshot.md)
- [diary — stark0xbt / Baker](../../diary/2026-11.md) (2026-11-11 entry)
