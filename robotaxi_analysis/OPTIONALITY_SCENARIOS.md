# Optionality Scenarios: 2035 Terminal Valuations

Four mutually exclusive scenarios spanning the full range of robotaxi outcomes. Numbers from model run June 2026.

---

## Scenario Definitions

| Scenario | Fleet Waymo / Tesla | Car Substitution | Asset Layer | Adoption | Terminal Multiple (T1/T2/T3) |
|----------|--------------------|--------------------|-------------|----------|-------------------------------|
| **Conservative (Transport)** | 120k / 200k | 8% | 1.0x | Linear | 17x / 11x / 8x |
| **Infrastructure Layer** | 2M / 5M | 20% | 1.2x | Linear (inflects 2028) | 32x / 22x / 15x |
| **Natural Monopoly** | 5M / 15M | 35% | 1.4x | Linear (inflects 2030) | 45x / 30x / 20x |
| **Ownership Disruption** | 10M / 30M | 60% | 1.6x | S-curve (inflects 2029) | 50x / 35x / 25x |

---

## 2035 Terminal Outcomes: Waymo (Alphabet / GOOGL)

| Scenario | Fleet | Rides Revenue | Asset Layer | Total Revenue | Terminal Value | PV @ 10% WACC |
|----------|-------|--------------|-------------|---------------|----------------|----------------|
| Conservative | 120,000 | $7.9B | $0.0B | $7.9B | $135B | **$52B** |
| Infrastructure | 2,000,000 | $132.0B | $26.4B | $158.4B | $5,068B | **$1,956B** |
| Natural Monopoly | 3,872,000* | $255.4B | $102.2B | $357.5B | $16,089B | **$6,210B** |
| Ownership Disruption | 10,000,000 | $653.2B | $391.9B | $1,045.1B | $52,254B | **$20,170B** |

\*Ramp-limited by 2035; terminal target 5M reached beyond model horizon.

## 2035 Terminal Outcomes: Tesla (TSLA)

| Scenario | Fleet | Rides Revenue | Asset Layer | Total Revenue | Terminal Value | PV @ 10% WACC |
|----------|-------|--------------|-------------|---------------|----------------|----------------|
| Conservative | 200,000 | $4.9B | $0.0B | $4.9B | $84B | **$32B** |
| Infrastructure | 5,000,000 | $123.2B | $24.6B | $147.8B | $4,729B | **$1,825B** |
| Natural Monopoly | 8,899,000* | $218.8B | $87.5B | $306.3B | $13,782B | **$5,320B** |
| Ownership Disruption | 30,000,000† | $58.0B | $34.8B | $92.8B | $4,639B | **$1,791B** |

\*Ramp-limited; terminal target 15M reached beyond model horizon.  
†At 30M US vehicles, Tesla hits network congestion limit (6,200 vehicles/100k vs 5,000/100k inflection). Ownership Disruption requires global deployment for Tesla at this fleet scale.

---

## Stockholder Value Impact

**Alphabet (GOOGL) — $4.68T market cap · $388/share · 12.06B shares**

| Scenario | PV | % of Market Cap | Per Share |
|----------|----|-----------------|-----------|
| Conservative | $52B | 1.1% | +$4.31 |
| Infrastructure | $1,956B | 41.8% | +$162.19 |
| Natural Monopoly | $6,210B | 132.7% | +$514.96 |
| Ownership Disruption | $20,170B | 430.9% | +$1,672.47 |

**Tesla (TSLA) — $1.60T market cap · $399/share · 4.0B shares**

| Scenario | PV | % of Market Cap | Per Share |
|----------|----|-----------------|-----------|
| Conservative | $32B | 2.0% | +$8.09 |
| Infrastructure | $1,825B | 114.1% | +$456.35 |
| Natural Monopoly | $5,320B | 332.5% | +$1,329.99 |
| Ownership Disruption | $1,791B | 111.9% | +$447.62 |

---

## Notes

- PV = Terminal Value × 0.386 (10% WACC, 10-year discount)
- Terminal Value = Total Platform Revenue × Terminal Multiple
- Asset layer (multiplier > 1.0) covers logistics, data, advertising, subscriptions on top of core rides
- Scenarios are all-or-nothing packages — assumptions are internally coupled; see `REGIME_COHERENCE_CONSTRAINTS.md`
- Which scenario is materializing: see `REGIME_INDICATORS.md` and `REGIME_TRANSITIONS.md`
- Run model: `python3 run_optionality_scenarios.py`
