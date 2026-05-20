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

## Geographic Scope

**Analysis covers USA market only.** The model includes 11 metropolitan areas:

**Explicitly Modeled (8 metros):**
- **Tier 1 (Premium):** SF/East Bay (7.7M), Phoenix (5.0M), LA Downtown (3.5M)
- **Tier 2 (Secondary):** Austin (2.4M), Denver (3.2M)
- **Tier 3 (Suburban):** DFW Suburbs (4.0M), LA Suburbs (6.0M)
- **Aggregate tier buckets (3):** Tier 1 Other (7.8M: NYC, Boston, Seattle, DC), Tier 2 Other (32.7M: Chicago, Atlanta, rest of secondary), Tier 3 Other (206.2M: remaining suburban/exurban US)

**Total coverage:** 278.5M of 280M US metro population (99.5%)

**Note:** Defined metros (8) cover 31.8M explicitly; aggregates cover remaining 246.7M at tier-level characteristics. For 2035 projections, model uses national rollout grid with tier-specific regulatory velocities and company-specific approval rates.

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

## Valuation Anchor (2035 Terminal)

### Bull Case: $40B Option Value

**IF Tesla vision autonomy matures:** Tesla dominates suburban Tier 3 with 200k vehicles, 18% take-rate, $4.2B platform revenue at 9.8x multiple.

**Tesla robotaxi valuation:**
- Fleet: 200k vehicles, 75% in Tier 3 (DFW suburbs, LA suburbs, rest of suburban US)
- Take rate: 18% (cost-sensitive suburban markets, <$1.20/mile pricing)
- Utilization: 55.4% efficiency (year 2-3 operational maturity; lower density markets)
- Gross annual revenue: $23.4B; platform net: $4.2B

**Valuation multiple: 9.8x** (commodity business, lower margin, volume-dependent)
- **Formula:** $4.2B annual platform revenue × 9.8x = $41.16B terminal value
- **Rationale:** Suburban mass-market robotaxi ≈ scaled Uber/Lyft model, not premium utility. Margins ~8-10% vs Waymo's 28%+. Multiple reflects commodity ride-hailing (8-10x) with regulatory moat (adds 1-2x premium)
- **Comparable:** Uber/Lyft trade 4-8x revenue; Tesla at 9.8x reflects profitable, autonomous-marginal-cost advantage

**Present value (discounted 2026–2035 at 10% WACC):**
- Terminal value (2035): $41.16B
- PV factor (10 years, 10% discount): 0.386
- **Discounted value: ~$15.9B** (bull case optionality)
- BUT: This assumes autonomy succeeds. Probability-weighted = bullish scenario value

### Bear Case: <$5B Option Value

**IF Tesla vision autonomy fails in long-tail edge cases:**
- Fleet: <10k vehicles (pilot programs only)
- Take rate: N/A (service not scalable)
- Platform revenue: ~$0
- Valuation: **~$0–5B** (sunk costs, residual value of development IP, Tesla brand value from attempt)

### Scenario Range

| Scenario | Autonomy Maturity | 2035 Fleet | 2035 Platform Revenue | Terminal Multiple | Terminal Value | PV @ 10% WACC | Key Assumption |
|----------|-------------------|-----------|----------------------|------------------|-----------------|---------------|-----------------|
| **Bear** | Fails (stuck 12k mi/int) | <10k | ~$0 | — | ~$0 | ~$0 | Vision edge cases don't solve; remote ops costs unsustainable |
| **Slow** | Marginal (18k mi/int) | 150k | $3.2B | 8.5x | $27.2B | $10.5B | Autonomy progresses slowly; Tier 3 expansion delayed |
| **Base** | Proven (30k mi/int) | 200k | $4.2B | 9.8x | $41.2B | $15.9B | Autonomy targets hit; standard Tier 3 deployment |
| **Hypergrowth** | Advanced (40k+ mi/int) | 300k | $5.8B | 10.5x | $60.9B | $23.5B | FSD breakthrough; rapid Tier 2/3 expansion; cost advantage sustained |

**Key insight:** Tesla's entire valuation range ($(0–24B) is driven by one variable: **autonomy maturity**. Regulatory approval, manufacturing, pricing all matter only IF autonomy works.

### Sensitivity to Autonomy Milestone (Critical Drivers)

| Milestone | Date | Impact on Terminal Value | Bear Case Risk | Bull Case Upside |
|-----------|------|-------------------------|-----------------|------------------|
| **Intervention rate: 12k → 20k mi/int** | 2027 | +$5B (credibility) | Stalls here → full bear | On track |
| **5B cumulative safety miles** | 2028-2029 | +$10B (Tier 3 approval) | Delayed → revenue push to 2033+ | On track |
| **30k mi/int baseline (vs Waymo 35k)** | 2029 | +$8B (parity viability) | Stalls <25k → margins unsustainable | At risk |
| **Tier 3 expansion +1 metro/quarter** | 2030-2032 | +$12B (scale validation) | <2 new metros/year → capped at 150k fleet | On track |
| **Remote ops cost <$0.10/mile** | 2031 | +$3B (unit economics) | Stays >$0.15/mile → profitability breaks | Critical |

---

## Critical Autonomy Milestones (Quarterly Monitoring)

**Tesla's robotaxi thesis is gated by four autonomy & regulatory milestones. Miss any → entire thesis reprices downward.**

### Gate 1: FSD Intervention Rate (2027–2028)

**Target:** Improve intervention rate from ~12k miles/intervention (current) → 20k by end of 2027 → 30k by end of 2028

| Metric | 2025E | 2026E | 2027E | 2028E | Thesis Status | Miss Threshold |
|--------|-------|-------|-------|-------|----------------|-----------------|
| Miles per intervention | 12k | 15k | 20k | 30k | Improving 25%+ YoY | <15% YoY |
| Cumulative safety miles (billions) | 5B | 8B | 12B | 18B | On path to 5B gate | Delayed >12 months |
| Data collection (edge cases solved/wk) | Unknown | Known | Tracking | Validated | Required validation | Regressing >1 quarter |

**Monitoring:** Quarterly from Investor Day presentations, 10-K filings, Elon commentary
- ✅ **On track:** 20%+ YoY intervention rate improvement → implies Gate 1 clear by Q4 2027
- ⚠️ **At risk:** 10-15% YoY improvement → slipping toward 2028 gate
- ❌ **Broken:** Flat intervention rate or regression → autonomy thesis fails, fleet <50k by 2035

---

### Gate 2: Cumulative Safety Miles (5B Milestone, 2028–2029)

**Target:** 5 billion cumulative miles by end of 2028 = regulatory credibility for Tier 3 expansion

| Metric | 2025E | 2026E | 2027E | 2028E | Gate Requirement |
|--------|-------|-------|-------|-------|----------|
| Annual miles (billions) | 1.5B | 2.5B | 4.0B | 5.0B | ≥5B cumulative = "proven safe" |
| Fleet size (vehicles) | 500 | 2k | 10k | 20k | Supports 5B mile run |
| Miles per vehicle per day | 150 | 400 | 600 | 800 | Utilization scaling |

**Monitoring:** Tesla 10-K (miles driven by fleet), shareholder letters, regulatory communications
- ✅ **On track:** Hit 5B cumulative by Q4 2028 → unlocks aggressive Tier 3 approvals 2029+
- ⚠️ **At risk:** Delayed to Q2 2029 → Tier 3 expansion slips 6 months, revenue pull-forward lost
- ❌ **Broken:** Stuck <3B by end 2029 → regulator skepticism, fleet capped at Tier 1 pilot size (~5k)

---

### Gate 3: Tier 3 Regulatory Approvals (2029–2032)

**Target:** Achieve 50%+ approval probability in Tier 3 metros by 2030; 80%+ by 2032

| Metric | 2028 | 2030 | 2032 | 2035 | Fleet Impact |
|--------|------|------|------|------|--------------|
| Tier 3 approval probability (base) | 8% | 35% | 65% | 85% | Drives fleet allocation |
| Operating metros in Tier 3 | 0 | 3–4 | 8–10 | 20+ | Revenue scale |
| Vehicles deployed in Tier 3 | 0 | 20k | 80k | 150k | 75% of Tesla fleet |

**Monitoring:** State regulatory filings, Waymo competitive approvals, incident reports
- ✅ **On track:** 1 new Tier 3 metro approval per quarter starting Q4 2028 → fleet reaches 200k by 2035
- ⚠️ **At risk:** Slower than 1 new metro/quarter → fleet capped at 150k, revenue $3.2B (Slow scenario)
- ❌ **Broken:** No new Tier 3 approvals past 2030 → fleet stuck <50k, revenue drops to Bear case ($0)

---

### Gate 4: Unit Economics Sustainability (Remote Ops Cost Scaling, 2029–2030)

**Target:** Remote ops cost < $0.10/mile by 2030; decline to <$0.05/mile by 2035

| Metric | 2026 | 2027 | 2028 | 2029 | 2030 | 2035 | Margin Impact |
|--------|------|------|------|------|------|------|---------------|
| Remote ops cost ($/mile) | $0.20 | $0.17 | $0.14 | $0.11 | $0.10 | $0.05 | Most critical |
| Intervention rate required | 12k | 16k | 20k | 25k | 30k | 40k+ | Gate 1 linkage |
| Total opex ($/mile) | $0.62 | $0.59 | $0.56 | $0.53 | $0.52 | $0.47 | Enables profitability |
| Take-rate required for breakeven | 22% | 20% | 18% | 17% | 16% | 14% | Achievable in Tier 3 |

**Monitoring:** Gross margin evolution (10-K), operating leverage commentary, cost per mile tracking
- ✅ **On track:** Remote ops cost declining 8-10% YoY; hit <$0.10 by Q2 2030 → unit economics sustainable
- ⚠️ **At risk:** Cost declining <5% YoY → staying >$0.12 by 2030 → compressed margins, fleet smaller than model
- ❌ **Broken:** Cost flat/regressing (human intervention doesn't scale with fleet) → entire Tier 3 expansion unprofitable

---

## Autonomy Risk Dashboard

**Tesla's robotaxi thesis rides on autonomy execution. These are the failure modes that matter most.**

| Risk | Severity (1-10) | Mitigant | Mitigant Strength (1-10) | Monitoring KPI | Trigger for Repricing |
|------|-----------------|----------|-------------------------|-----------------|--------------------------|
| **FSD edge cases don't improve with scale** | 9 | Fleet driving more miles = more edge case data | 5 | Intervention rate YoY improvement | <10% YoY improvement for 2+ qtrs |
| **Remote ops cost doesn't scale** | 8 | Automation tools, geographic load balancing, routing optimization | 6 | $/mile remote ops cost trend | Cost flat or rising for 2+ qtrs |
| **Regulatory skepticism persists** | 7 | 5B safety milestone achievement; no major incidents; Waymo track record helps calibrate regulator views | 6 | New Tier 3 metro approvals/quarter | <1 new approval per 2 quarters |
| **Waymo accelerates Tier 3 expansion** | 7 | Tesla's cost advantage ($0.42 vs $0.68) defensible; different market positioning | 6 | Waymo Tier 3 approval rate vs Tesla's | Waymo approval rate >2x Tesla's in Tier 3 |
| **Major incident (fatal accident)** | 8 | Full autonomy (no human remote operator liability); extensive testing before expansion | 7 | Cumulative incident tracking; miles between incidents | Major incident involving fatality |
| **Manufacturing capacity proves inadequate** | 4 | Tesla can scale Model Y line; external manufacturing partnerships possible | 8 | Announced production capacity vs fleet targets | Capacity shortfall >20% of plan |

---

## Investment Thesis: Bull vs Bear vs Base Case

### Bull Case Path ($40B+ valuation)
1. **2026–2028:** Intervention rate improves 25%+/year → 20k+ miles/intervention by 2028
2. **2028–2029:** Hit 5B cumulative safety miles → unlock Tier 3 expansion
3. **2029–2032:** Rapid Tier 3 metro approvals (1/quarter) → 200k vehicles by 2032
4. **2030–2035:** Remote ops cost declines to <$0.10/mile → unit economics sustain 16%+ take-rate
5. **Outcome:** 200k fleet, $4.2B platform revenue, 9.8x multiple = $40B+

**Probability: 35%** (requires flawless autonomy execution + regulatory cooperation)

### Base Case Path ($15.9B valuation)
1. **2026–2028:** Intervention rate improves 15–20%/year → 25k miles/intervention by 2029
2. **2029–2030:** Hit 5B safety miles, but regulatory approval slower than optimized
3. **2030–2032:** 2–3 new Tier 3 metros/year → 150–200k vehicles
4. **2035:** $3.2–4.2B platform revenue, 9.2–9.8x multiple = $30–40B
5. **Outcome:** Base case fleet (200k), revenue ($4.2B), value ($40B)

**Probability: 50%** (moderate autonomy success, steady regulatory pace)

### Bear Case Path ($0–5B valuation)
1. **2027–2029:** Intervention rate improvement stalls <15%/year → stuck at 15k miles/intervention
2. **2029:** Unable to convince regulators Tier 3 is safe; stuck in limited Tier 1 pilot
3. **2030+:** Fleet growth ceases at <50k; remote ops costs unsustainable
4. **Outcome:** Pilot program only, near-zero robotaxi revenue, $0–5B sunk value

**Probability: 15%** (autonomy doesn't solve edge cases; regulators prioritize safety)

---

## Next Steps: Quarterly Validation Framework

**This thesis needs quarterly validation against four milestones. Tracking requirements:**

### Q Report Checklist
- [ ] **FSD intervention rate:** Extract from investor day or regulatory filing; calculate YoY improvement %
- [ ] **Cumulative safety miles:** Sum from 10-K or management commentary; track path to 5B by end 2028
- [ ] **Tier 3 approvals:** Monitor state regulatory announcements; track new metro approvals
- [ ] **Remote ops cost:** Estimate from gross margin trends; assess leverage as fleet scales
- [ ] **Competitive moat:** Compare Tesla approval velocity vs Waymo; assess if cost advantage defended

### Escalation Triggers (Thesis Repricing)
- Intervention rate improvement <10% YoY → downgrade to Slow scenario
- 5B safety miles delayed >6 months → downgrade to Bear scenario  
- Remote ops cost flat/rising → full repricing (autonomy thesis breaks)
- Waymo Tier 3 approval >2× Tesla's rate → competitive threat escalates
- Major incident with fatality → immediate repricing to Bear

### Data Sources
- **Quarterly 10-K:** miles, fleet size, capex, gross margin trends
- **Investor Days:** FSD maturity metrics, autonomy targeting, regional strategies
- **Regulatory filings:** State approval timelines, incident reports, company testimonies
- **Competitive:** Waymo approval rates, pricing, fleet expansion pace

---

**Last updated:** 2026-05-20  
**Model version:** Reframed (autonomy maturity as primary risk, regulatory approval as secondary constraint)  
**Status:** Bull case ($40B) feasible if milestones hit; Bear case ($0) if autonomy stalls; Base ($16B PV) most likely outcome
