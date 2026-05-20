# Tesla Robotaxi Competitive Analysis (Shared Model)

**Out-of-band quantitative analysis** — competitive modeling for Tesla vs. Waymo autonomous networks.

**Location:** Shared analysis at `/robotaxi_analysis/` (repo root) — also referenced in [`goog/`](../goog/ROBOTAXI_ANALYSIS.md).

## BLUF (Bottom Line Up Front)

**Tesla's robotaxi strategy hinges entirely on vision autonomy survival in long-tail edge cases. Charging bottleneck is a red herring; regulatory approval is the real constraint. If autonomy works: Tesla dominates suburban Tier 3 with 200k+ vehicles, 18% take-rate, $4.2B platform revenue at 9.8x multiple = $40B+ option value. If autonomy fails: near-zero value. The charging model was wrong (elastic capital, $500/vehicle/year, 0.5% of fleet cost). Real risk: remote ops costs don't scale with intervention rate, or vision failures spike after 2030 as edge cases accumulate. For Tesla shareholders: robotaxi is all-or-nothing bet on FSD maturity, not a utility-scale regulated business. Waymo's 17.3x premium metro moat is structural; Tesla's optionality is fragile.**

## ⚠️ MODEL REFRAME (May 2026)

**The original model is SUPERSEDED.** The "charging bottleneck" assumption was incorrect. See [`robotaxi_analysis/REFRAME_ANALYSIS.md`](../robotaxi_analysis/REFRAME_ANALYSIS.md) for complete reframe:

- ✅ **Charging is NOT the bottleneck** — it's elastic capital ($500/vehicle/year, 0.5% of fleet economics)
- ✅ **Regulatory approval is the actual constraint** — gates fleet by metro tier
- ✅ **Tesla's real risk is autonomy fragility** — remote ops costs don't scale if intervention rate doesn't improve with scale
- ✅ **Tesla's real path is Tier 3 dominance** — suburban markets where lower density and cost advantage matter, not mass-market network effects
- ✅ **Different terminal outcomes** — Tesla bull case 9.8x multiple (commodity suburban), bear case near-zero (autonomy fails)

---

## Overview

Tesla's robotaxi strategy competes directly with **Waymo** (Google's autonomous vehicle subsidiary). This shared model compares:

- **Tesla**: Suburban mass-market swarm (Tier 3: DFW, LA suburbs) — cost advantage *IF* vision autonomy survives edge cases
- **Waymo**: Premium metro network (Tier 1: SF, Phoenix, LA) — regulatory trust + high utilization + pricing power

## What This Tells You About Tesla

### Tesla's Competitive Positioning (Regulatory Approval as Primary Constraint)

**Real Advantages (if autonomy works):**
- **Lower cost structure** — $0.42/mile vs Waymo's $0.68/mile (38% opex advantage) enables lower fares in price-sensitive markets
- **Suburban market fit** — Tier 3 metros (DFW, LA suburbs) have lower density, longer distances → cost advantage matters more than in dense urban
- **Manufacturing scale** — Can deploy 200k+ vehicles if regulatory approval accelerates; Tesla capex per vehicle lower than Waymo's
- **Rapid iteration** — Vision autonomy improving at >50% annual intervention rate improvement (claimed); could hit 5B milestone faster than Waymo's 35k mi baseline

**Real Challenges (Regulatory + Operational):**
- **Regulatory barriers in premium metros** — Tier 1 (SF, Phoenix): 0.8x approval velocity vs Waymo's 2.25x. Tesla must prove safety (5B cumulative miles) before tier expansion
- **Intervention rate fragility** — Entire thesis depends on improving from 12k mi/intervention to 35k+ mi/intervention. If it stalls or regresses post-2030, remote ops costs collapse unit economics
- **Tier 3 is lower-margin** — Suburban supports 15-18% take-rate vs Tier 1's 25-32%. Even with cost advantage, net margin may not exceed 8-10%
- **Terminal revenue limited by choice** — At 200k vehicles in Tier 3, platform revenue only $4.2B (not market-sharing failure, but market structure). Waymo gets $3.5B from 120k at higher margins

**Critical Risk:** If vision autonomy underperforms in long-tail urban edge cases (2028-2030), intervention rate stagnates, remote ops costs stay high, and entire Tier 3 expansion becomes unprofitable. This is an **all-or-nothing bet**.

### Base Case Terminal (2035, Regulatory Approval as Primary Constraint)

| Metric | Tesla (Bull) | Waymo | Delta | Notes |
|--------|-------|-------|-------|-------|
| **Fleet Operating** | **200k** | **120k** | Tesla +67% | Different metro focus: Tesla Tier 3, Waymo Tier 1 |
| Metro Focus | Tier 3 (Suburban) | Tier 1 (Premium) | Different markets | Different regulatory approval rates |
| **Take Rate** | **18%** | **32%** | Waymo +14pp | Premium metro pricing power vs suburban cost competition |
| Fares $/Mile | $1.10 | $1.90 | Waymo +73% | Different market structure |
| **Gross Annual Revenue** | **$23.4B** | **$12.2B** | Tesla higher volume | But lower per-vehicle utilization |
| **Platform Annual Revenue** | **$4.2B** | **$3.5B** | Tesla higher | Volume advantage offset by margin disadvantage |
| Annual Revenue/Vehicle | $21k | $29k | Waymo +38% | Better utilization + pricing in premium metros |
| Terminal Multiple | 9.8x | 17.3x | Waymo +76% | Different market structures: commodity vs utility |
| Bottleneck | Regulatory | Regulatory | Both | Regulatory approval gates expansion, not charging |
| Real Risk | Autonomy failure | Regulatory caution | Asymmetric | Tesla loses if vision fails; Waymo has proven ops |

**Critical Insight (Reframed):** Tesla's 200k vehicles vs Waymo's 120k is NOT constrained by charging (elastic capital) but by regulatory approval velocity for Tier 3 expansion. Tesla's lower margins in suburban Tier 3 mean lower valuation multiple (9.8x) despite higher fleet size. **Waymo wins on per-vehicle economics, Tesla wins on volume—but only if vision autonomy matures.** Tesla's real risk: intervention rate stalls, remote ops costs remain high, Tier 3 profitability collapses. If autonomy fails: near-zero deployment (bear case).

### Scenario Sensitivity (Annual Platform Revenue, 2035, Regulatory Constraint)

| Scenario | Tesla Fleet | Tesla Revenue | Waymo Fleet | Waymo Revenue | Notes |
|----------|------------|----------------|------------|----------------|-------|
| Slow | 150k | $3.2B | 90k | $2.5B | Slower regulatory approval; charging not binding |
| **Base** | **200k** | **$4.2B** | **120k** | **$3.5B** | Reference; autonomy works moderately |
| Hypergrowth | 300k | $5.8B | 160k | $5.0B | Fast regulatory approval; Tesla autonomy proven |
| Tesla Bear | <10k | ~$0 | 120k | $3.5B | Vision autonomy fails; Tesla withdraws |

**Critical Finding:** Fleet size now scales with regulatory approval velocity AND autonomy maturity. Tesla's scenarios have wide range ($0–5.8B) depending on whether vision autonomy survives long-tail edge cases. Waymo's scenarios have narrower range ($2.5–5.0B) because regulatory moat is more predictable. **The real upside/downside for Tesla is autonomy trajectory, not vehicle demand or charging.**

## What Tesla Actually Faces (Regulatory Approval + Autonomy Maturity)

In a regulatory-constrained market, Tesla's levers are much narrower than original model suggested:

1. **Autonomy maturity is existential** — Intervention rate must improve from 12k to 30k+ miles per intervention by 2030 to hit 5B cumulative miles safety milestone. If it stalls, Tier 3 expansion fails and remote ops costs remain structural margin drain.

2. **Regulatory approval in Tier 3 comes fast IF autonomy proves** — 0.94x velocity initially, but 1.4x+ after 3 years of safe driving. Tesla can't enter Tier 1 (Waymo's fortress) but can dominate Tier 3 if autonomy holds.

3. **Pricing power in Tier 3 is structurally limited** — Suburban markets support $1.10/mile fares, 15-18% take-rates. Tesla can't raise fares without losing volume (unlike Waymo in premium metros). Cost advantage must be preserved or unit economics break.

4. **Manufacturing scale is real but not binding** — Tesla can make 500k robotaxis/year IF demand exists and regulatory approval comes. But approval comes metro-by-metro, not nationally. Fleet builds slower than Tesla can manufacture.

**Reality (Reframed):** Robotaxi is a utility-scale business with bifurcated markets (Waymo premium, Tesla suburban). Tesla's play is:
- **Bull:** Prove vision autonomy → 200k+ vehicles in Tier 3 by 2035 → $4.2B platform revenue → 9.8x multiple
- **Bear:** Autonomy stalls → <10k vehicles → near-zero valuation
- **Unlikely middle ground:** Partial success doesn't exist (either autonomy works or it doesn't)

Tesla's option value is ALL in autonomy maturity; manufacturing, pricing, and regulatory velocity matter only IF autonomy succeeds.

## Integration with Standard CLAUDE.md Analysis

This quantitative model should **inform**:
- **Business model analysis** in `tsla/analysis/YYYY_MM_business_model.md` — robotaxi revenue stream assumptions
- **Competitive analysis** comparing Tesla's scale thesis vs Waymo's unit economics dominance
- **Valuation analysis** with scenario-specific revenue projections fed into DCF
- **Investment thesis** on Tesla's autonomous vehicle optionality and profitability path

Typical workflow:
1. Run base case and three scenarios via `/robotaxi_analysis/run_all_scenarios.py`
2. Extract 2030E and 2035E platform revenue for each scenario
3. Assess whether Tesla's cost advantage ($0.42 vs $0.68/mile) can offset Waymo's margin advantage
4. Document assumptions and sensitivity in formal analysis documents

## Accessing the Shared Model

See [`robotaxi_analysis/README.md`](../../robotaxi_analysis/README.md) for:
- Full model documentation
- All customization options (rollout timeline, market share, assumptions)
- CLI usage and export formats (CSV, JSON)
- Scenario definitions and knob explanations

### Quick Start

From `/robotaxi_analysis/` directory:

```bash
# View all scenarios
python3 run_all_scenarios.py

# Export to CSV for analysis
python3 run_all_scenarios.py --csv tesla_waymo_comparison.csv

# Adjust Tesla vs Waymo market share
python3 run_all_scenarios.py --market-share-json '{"tesla":0.6,"waymo":0.4}'

# Run single scenario with custom assumptions
python3 robotaxi_revenue_model.py --scenario hypergrowth --market-json '{"us_metro_population_full": 300000000}'
```

---

**Last updated:** 2026-05-20  
**Key Question:** Does Tesla's cost advantage ($0.42/mile) materialize fast enough to defend against Waymo's structural margin advantage?
