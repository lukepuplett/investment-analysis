# Quarterly Monitoring Framework: Robotaxi Scenarios

## Overview

This document defines the operational monitoring process for the three optionality scenarios (Conservative, Infrastructure, Natural Monopoly). It translates scenario theory into quarterly data collection, trend analysis, and repricing triggers for Waymo (GOOGL) and Tesla (TSLA).

**Goal:** Detect early which scenario is unfolding and adjust probability weights (and valuations) before the market reprices.

---

## Framework Structure

### 1. Quarterly Data Collection (Due 30 days post-earnings)
- **Source:** Earnings call, 10-Q MD&A, investor presentations, SEC filings
- **Metric groups:** Operational (deployment, utilization), Financial (take-rate, margins), Strategic (behavior change signals, infrastructure layers)
- **Output:** Populated monitoring scorecard (see Section 5)

### 2. Scenario Path Assessment (Due 45 days post-earnings)
- **Process:** Compare actual metrics vs. scenario projections for that quarter
- **Decision rules:** If metric deviates >1.5 sigma from scenario path, flag
- **Output:** Scenario probability adjustment (see Section 6)

### 3. Repricing Trigger (Automatic)
- **Condition:** Any scenario shifts >10 percentage points in cumulative probability
- **Action:** Recalculate terminal valuations and per-share impact; update investment thesis

### 4. Annual Deep Dive (Q4 only)
- **Review:** Full-year actuals vs. forward guidance for next 2 years
- **Assess:** Which scenario's assumptions are holding; which are breaking
- **Reforecast:** Update 2035 terminal fleet, revenue, multiples if needed

---

## Section 1: Scenario Definition at a Glance

| Aspect | Conservative | Infrastructure | Natural Monopoly |
|--------|--------------|-----------------|------------------|
| **Behavior Inflection** | Never | 2028 | 2030 |
| **Key Value Driver** | Ride-hailing only | Infrastructure layers | Moat compounding |
| **Demand Multiplier** | 1.35x (fixed) | 2.0x by 2035 | 1.5x by 2035 |
| **Terminal Multiples** | 17-8x | 32-15x | 45-20x |
| **2035 Waymo Platform Revenue** | $4.56B | $6.10B | $8.20B |
| **2035 Waymo PV (10% WACC)** | $30.0B | $65.2B | $126.6B |
| **Per GOOGL Share** | +$2.48 | +$5.41 | +$10.51 |
| **Probability Weight (Illustrative)** | 40% | 40% | 20% |

---

## Section 2: Quarterly KPI Monitoring Scorecard

**Instructions:** Populate after each earnings call. Score each metric 0–10 (10 = scenario confirmed, 0 = scenario contradicted).

### Waymo (GOOGL) — Quarterly Tracking

| KPI | Scenario Path | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Confidence |
|-----|---------------|---------|---------|---------|---------|------------|
| **Tier 2 Expansion** | | | | | | |
| - Conservative Target | 1 new metro/year | | | | | |
| - Infrastructure Target | 1.5 new metros/year | | | | | |
| - Monopoly Target | 2+ metros/year by 2029 | | | | | |
| **Waymo Intervention Rate** | | | | | | |
| - Conservative Path | Stalls at 18k mi/intervention | | | | | |
| - Infrastructure Path | Reaches 25-28k by 2028-29 | | | | | |
| - Monopoly Path | Reaches 35k+ by 2030 | | | | | |
| **Utilization Efficiency (SF, Tier 1)** | | | | | | |
| - Conservative Path | Stable 80-85% | | | | | |
| - Infrastructure Path | Accelerates to 88-92% | | | | | |
| - Monopoly Path | Reaches 94%+ by 2030 | | | | | |
| **Take-Rate in Tier 2** | | | | | | |
| - Conservative Path | 20-22% (pricing pressure) | | | | | |
| - Infrastructure Path | 24-26% (infrastructure premium) | | | | | |
| - Monopoly Path | 28%+ (moat premium) | | | | | |
| **City Integration Depth** | | | | | | |
| - Conservative Signal | Traffic management only | | | | | |
| - Infrastructure Signal | Traffic + parking + emergency | | | | | |
| - Monopoly Signal | Full mobility OS (energy, logistics, delivery) | | | | | |
| **FSD Safety Progress (Tesla Comparison)** | | | | | | |
| - Conservative Path | Tesla narrows gap; Waymo lead erodes | | | | | |
| - Infrastructure Path | Waymo gap widens | | | | | |
| - Monopoly Path | Waymo gap becomes structural moat | | | | | |

### Tesla (TSLA) — Quarterly Tracking

| KPI | Scenario Path | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Confidence |
|-----|---------------|---------|---------|---------|---------|------------|
| **FSD Intervention Rate (Autonomy Gate)** | | | | | | |
| - Conservative Path | Stalls at 18k mi/intervention | | | | | |
| - Infrastructure Path | Reaches 25-28k by 2028-29 | | | | | |
| - Monopoly Path | Reaches 35k+ by 2030 | | | | | |
| **Regulatory Approvals (Tier 3/Suburban)** | | | | | | |
| - Conservative Path | 2-3 new metros/year | | | | | |
| - Infrastructure Path | 3-4 new metros/year | | | | | |
| - Monopoly Path | 5+ metros/year (faster than Waymo) | | | | | |
| **Fleet Operating (Waymo+Tesla total in model)** | | | | | | |
| - Conservative Path | 180k Tesla vehicles | | | | | |
| - Infrastructure Path | 220k Tesla vehicles | | | | | |
| - Monopoly Path | 280k Tesla vehicles | | | | | |
| **Take-Rate in Tier 3** | | | | | | |
| - Conservative Path | 15-18% (commodity pricing) | | | | | |
| - Infrastructure Path | 18-20% (behavior change) | | | | | |
| - Monopoly Path | 20-25% (winner-takes-most) | | | | | |
| **Utilization (Suburban Fleet Average)** | | | | | | |
| - Conservative Path | Stable 55-60% | | | | | |
| - Infrastructure Path | Accelerates to 65-70% | | | | | |
| - Monopoly Path | Reaches 75%+ by 2030 | | | | | |
| **Manufacturing Cost/Vehicle (Model 3-based fleet)** | | | | | | |
| - All Scenarios | Should decline ~5-8%/year | | | | | |
| - Flag | If cost deltas vs Waymo reverse (labor arbitrage lost) | | | | | |

---

## Section 3: Red Flag Thresholds (Scenario-Breaking Events)

When you observe ANY of these, escalate to reforecasting within 5 business days.

### Waymo (GOOGL) — Breaking Points

| Event | Impact | Severity | Scenario Breaks | Action |
|-------|--------|----------|-----------------|--------|
| **Tier 1 Utilization Falls Below 75%** | Suggests demand softer than modeled; limits leverage for Infrastructure case | 8/10 | Infrastructure, Monopoly | Recalculate demand curve; check competitive pricing |
| **Intervention Rate Plateau >20k mi (Q1-Q3 2026)** | Safety learning curve flatter than expected; regulatory approval delayed | 7/10 | Infrastructure, Monopoly | Extend 2028 infrastructure inflection to 2030+ |
| **Tier 2 Expansion Stalls (0 new metros 2 consecutive quarters)** | Regulatory approval slower than assumed; moat may not widen | 8/10 | Infrastructure, Monopoly | Shift prob from Infrastructure/Monopoly → Conservative |
| **Take-Rate in Tier 1 Drops Below 20%** | Competitive pressure from Tesla or traditional rideshare; pricing power eroding | 7/10 | All (impacts margin profile) | Recalculate terminal multiple downward |
| **City Integration Not Progressing (MD&A silent on parking/emergency integration Q4 2026)** | Infrastructure layer assumption unfounded | 6/10 | Infrastructure | Shift prob Infrastructure → Conservative |
| **Safety Dataset Not Compounding (FSD improves as fast as Waymo)** | No moat from regulation | 9/10 | Monopoly | Shift prob Monopoly → Conservative/Infrastructure 50/50 |
| **Alphabet Cuts Waymo Budget or Changes Strategic Commitment** | Existential risk | 10/10 | All scenarios null | Abort analysis; reassess from zero |

### Tesla (TSLA) — Breaking Points

| Event | Impact | Severity | Scenario Breaks | Action |
|-------|--------|----------|-----------------|--------|
| **FSD Intervention Rate Deteriorates (>20k by 2027)** | Autonomy not improving; Tier 3 deployment gated indefinitely | 9/10 | All scenarios | Reset to Bear case ($0-5B value) |
| **No Tier 3 Regulatory Approvals by Q4 2026** | Deployment path stalled; regulatory bet lost | 8/10 | Infrastructure, Monopoly | Collapse all to Conservative |
| **Manufacturing Cost Per Vehicle Increases** | Labor cost inflation or capex bloat erodes margin advantage | 7/10 | All (base assumption broken) | Narrow valuation to Conservative downside |
| **Gross Margin (Auto Segment) Compresses Below 20%** | Pricing war or input cost inflation; robotaxi econ unsustainable | 8/10 | All scenarios | Reduce terminal take-rate assumption |
| **Elon Commits Resources to Other Projects (Humanoid, Neuralink)** | Robotaxi deprioritized; funding/mgmt attention diverted | 6/10 | Infrastructure, Monopoly | Shift to Conservative; assume slower deployment |
| **Waymo's Safety Lead Becomes Undeniable (2x better intervention rate)** | Tesla cannot catch up; loses moat race | 9/10 | Monopoly | Shift from Monopoly → Conservative |

---

## Section 4: Quarterly Data Collection Checklist

**Due 30 days after quarter-end earnings.**

### Always Capture (All Quarters)

- [ ] **10-Q Filing:** MD&A section, risk factors, forward guidance
- [ ] **Earnings Call Transcript:** Management commentary on deployment, utilization, safety milestones
- [ ] **Investor Presentation:** Product roadmap, geographic expansion plans, technology progress
- [ ] **Press Release:** Fleet size, intervention rate, new metro approvals

### Waymo-Specific (GOOGL)

- [ ] **Fleet Operating:** Current vehicle count across all metros (Tier 1, 2, 3)
- [ ] **Utilization Efficiency:** Revenue per vehicle per day (proxy for demand strength)
- [ ] **Take-Rate by Tier:** If disclosed; otherwise calculate from gross revenue / gross Miles
- [ ] **Intervention Rate:** Miles per intervention or intervention-free miles milestone
- [ ] **New Metro Approvals:** List new cities approved/deployed in quarter
- [ ] **City Integration Signals:** Any MD&A mentions of parking, emergency services, logistics, data partnerships
- [ ] **Capex/Fleet Growth Plans:** Forward guidance on fleet size 2026-2027
- [ ] **Competitive Positioning:** Any commentary on Tesla FSD, Cruise, or other competitors

### Tesla-Specific (TSLA)

- [ ] **FSD Intervention Rate:** Latest miles-per-intervention or improvement trajectory
- [ ] **Robotaxi Fleet Status:** Vehicles deployed, utilization, take-rate if disclosed
- [ ] **Regulatory Approvals:** New Tier 3 metros approved in quarter
- [ ] **Manufacturing Cost Trends:** Gross margin trend; any commentary on vehicle cost
- [ ] **Autonomous Capex:** Capex plans for FSD, fleet infrastructure, computing
- [ ] **Management Commentary on Autonomy:** Elon's tone on "self-driving" progress; timeline realism
- [ ] **Optionality on Other Businesses:** Any changes in Elon's stated priorities (Humanoid, Neuralink, etc.)

---

## Section 5: Scenario Probability Adjustment Rules

**Decision framework for repricing scenarios quarterly.**

### Rule 1: Waymo Tier 2 Expansion Velocity

| Actual Approvals | Conservative (0.25x) | Infrastructure (0.5x) | Monopoly (1.0x) | Guidance |
|-----------------|---------------------|----------------------|-----------------|----------|
| **0 metros Q1-Q2** | Slightly more likely (+5%) | Slightly less likely (-5%) | Much less likely (-10%) | Delay infrastructure inflection to 2029 |
| **1 new metro (expected)** | No change | No change | No change | On track |
| **2+ new metros** | Much less likely (-10%) | Slightly more likely (+5%) | More likely (+10%) | Accelerate inflection; pull forward 2030 milestones |

**Action:** After Q2 and Q3 2026, reweight probabilities based on cumulative metro approvals YTD vs. expected path.

### Rule 2: Utilization Efficiency Trajectory

| Waymo SF Utilization | Conservative | Infrastructure | Monopoly | Note |
|----------------------|--------------|-----------------|----------|------|
| **Falls Below 80%** | Slightly more likely (+3%) | Less likely (-5%) | Much less likely (-8%) | Demand assumptions too high |
| **Stays 80-85%** | No change | No change | No change | On track for all scenarios |
| **Reaches 90%+** | Less likely (-5%) | More likely (+8%) | More likely (+10%) | Demand stronger; infrastructure premium evident |

**Action:** Track quarterly; adjust in Q2-Q4 2026.

### Rule 3: Intervention Rate Progress (Waymo vs. Tesla)

| Rate | Waymo Moat Narrative | Adjustment | Note |
|-----|---------------------|-----------|------|
| **Waymo 18k, Tesla 18k** | No gap; no moat | Monopoly -15%, split to Inf/Cons | Safety learning similar; regulation won't favor one |
| **Waymo 20k, Tesla 16k** | Widening (on path) | Monopoly +5% | Gap compounding; infrastructure scenario more likely |
| **Waymo 22k+, Tesla <14k** | Significant gap | Monopoly +10%, Inf +5% | Clear safety lead; regulatory moat likely |

**Action:** Quarterly comparison; adjust Monopoly probability based on gap widening/narrowing.

### Rule 4: City Integration Signals (Infrastructure Case Validator)

| Evidence | Probability Shift | Reason |
|----------|------------------|--------|
| **Zero mentions of parking/emergency integration in MD&A** | Infrastructure -10%, Conservative +10% | Infrastructure value layer assumption broken |
| **One city (SF) integrates with emergency services OR parking system** | Infrastructure +5%, Monopoly +3% | Value layer proof-of-concept; scales to other metros |
| **Two+ cities adopt Waymo as city OS (traffic, parking, emergency)** | Infrastructure +10%, Monopoly +8% | Infrastructure case confirmed; natural monopoly path opened |

**Action:** Qualitative check each quarter; milestone-based repricing.

### Rule 5: Collective Probability Shift (Annual Decision)

**When cumulative adjustments exceed 10 percentage points in any scenario:**

1. **Recalculate terminal valuations** using updated scenario probabilities
2. **Recalculate per-share impact** (impact = probability × per-scenario-per-share-value)
3. **Update GOOGL/TSLA investment thesis** with new probability-weighted valuation
4. **Communicate repricing:** Document which KPI shifts drove the change

**Example:**
- Original: Conservative 40%, Infrastructure 40%, Monopoly 20%
- Q2 2026 actual: Waymo hits 2x metro approvals, FSD stalls, utilization 92%
- Adjusted: Conservative 25%, Infrastructure 50%, Monopoly 25% (Monopoly +5%, Infrastructure +10%, Conservative -15%)
- **Repricing trigger:** Yes, shift >10 points
- **New Waymo PV:** (0.25 × $30B) + (0.50 × $65.2B) + (0.25 × $126.6B) = $7.5B + $32.6B + $31.7B = **$71.8B** (vs. $63.4B before)
- **Per-share impact:** +$5.96 (vs. +$5.26 before)

---

## Section 6: Annual Deep Dive Checklist (Q4 Only)

**Due within 30 days of Q4 earnings release; informs 2027 guidance and thesis update.**

### Full-Year Assessment

- [ ] **Cumulative Interval Rate Progress:** How far did Waymo/Tesla move toward next 5B-mile safety milestone?
- [ ] **Full-Year Take-Rate by Tier:** Gross revenue / gross miles for each tier; any compression signals?
- [ ] **Fleet Composition:** Split of Tier 1 vs. Tier 2 vs. Tier 3; is expansion on expected path?
- [ ] **Capex Efficiency:** Total capex / fleet size; is manufacturing cost declining as expected?
- [ ] **Geographic Concentration:** % of revenue from top 3 metros; diversification progress?
- [ ] **Forward Guidance Reality Check:** Did company hit 2026 targets stated in 2025? What are 2027 guidance?

### Scenario Reforecast (If Material Changes)

- [ ] **Demand Inflection:** Any evidence behavior change is accelerating or delaying?
- [ ] **Margin Architecture:** Is infrastructure layer monetization visible, or still transactional?
- [ ] **Competitive Dynamics:** Has Waymo's lead widened or narrowed vs. Tesla, Cruise, others?
- [ ] **2035 Terminal Assumptions:** Do 2035 fleet size / revenue / multiple assumptions still hold?

### Update Investment Thesis

- [ ] **Revise per-company probabilities** if annual data suggests major shift
- [ ] **Update 2028-2035 projections** if inflection years need to move
- [ ] **Recalculate terminal values** with any updated assumptions
- [ ] **Publish updated investment thesis documents** (goog/ROBOTAXI_ANALYSIS.md, tsla/ROBOTAXI_ANALYSIS.md)

---

## Section 7: Repricing Trigger & Valuation Update Process

**When to act and how.**

### Automatic Repricing Condition

**Any scenario's cumulative probability shifts by >10 percentage points from prior quarter.**

### Repricing Workflow

1. **Data Collection (Days 1-2):** Populate quarterly scorecard (Section 2)
2. **Flag Assessment (Day 3):** Check against red flag thresholds (Section 3)
3. **Probability Adjustment (Day 4):** Apply decision rules (Section 5); calculate new weights
4. **Valuation Recalculation (Day 5):**
   ```
   New Waymo PV = (Conservative% × $30B) + (Infrastructure% × $65.2B) + (Monopoly% × $126.6B)
   New Tesla PV = (Conservative% × $1.6B) + (Infrastructure% × $3.5B) + (Monopoly% × $7.1B)
   New GOOGL Per-Share = Waymo PV / 12.06B shares
   New TSLA Per-Share = Tesla PV / 4.0B shares
   ```
5. **Communication (Day 6):**
   - Document scenario shift and KPI drivers
   - Update GOOGL/TSLA investment thesis files
   - Email alert: "Robotaxi scenarios repriced: [Old PV] → [New PV], +/- $X/share"

### Example: Q2 2026 Repricing

**Scenario:** Waymo approves 2 new Tier 2 metros in Q2 (vs. 1 expected); utilization hits 91% in SF; FSD intervention rate stalls at 16k miles (vs. expected 17k).

**Impact:**
- Tier 2 acceleration (+2 metros): Infrastructure +8%, Monopoly +5%, Conservative -13% → probabilities now 27% / 48% / 25%
- Utilization strength: Infrastructure +3%, Monopoly +2% → 30% / 51% / 19%
- FSD stall relative to Waymo: Monopoly -8% (moat widening is key to this case) → 30% / 51% / 19%
- **Net shift:** Conservative -13%, Infrastructure +11%, Monopoly +2% ✓ Exceeds 10-point threshold

**Waymo Repricing:**
- New Expected PV = (0.30 × $30B) + (0.51 × $65.2B) + (0.19 × $126.6B) = $9.0B + $33.3B + $24.1B = $66.4B
- Per GOOGL share = $66.4B / 12.06B = **+$5.51/share** (vs. +$5.26 before)
- **Implication:** Waymo's optionality worth +$0.25/share more; thesis upgraded to "Infrastructure path likely"

---

## Section 8: Summary — The Monitoring Rhythm

| Timing | Deliverable | Owner | Key Question |
|--------|-------------|-------|--------------|
| **T+30 days post-earnings** | Quarterly scorecard (Section 2) populated | Analyst | What KPIs moved? |
| **T+45 days post-earnings** | Red flag audit (Section 3) + scenario assessment (Section 5) | Analyst | Did any break threshold? |
| **T+50 days post-earnings** | Repricing decision (Section 7) if >10pt shift | Investment Committee | Do we update thesis? |
| **Q4 only (T+60 days)** | Annual deep dive (Section 6) + 2027-2035 reforecast | Analyst | Do 2035 assumptions still hold? |
| **Always (on file)** | Investment thesis docs updated with latest prob-weighted valuations | Analyst | Does market reflect optionality? |

---

## Appendix: 2026-2027 Expected Paths (Baseline Scenario Projections)

### Waymo Expected Milestones (Infrastructure Case)

| Quarter | Fleet | Intervention Rate (mi) | Tier 2 Metros | Utilization (SF) | Signal to Watch |
|---------|-------|----------------------|----------------|------------------|-----------------|
| Q1 2026 | 18k | 17.5k | 5 | 85% | Baseline establishment |
| Q2 2026 | 22k | 18.0k | 6 | 86% | First Tier 2 expansion |
| Q3 2026 | 26k | 18.5k | 7 | 87% | Acceleration signal |
| Q4 2026 | 32k | 19.0k | 8 | 87% | Regulatory velocity confirmed |
| Q2 2027 | 45k | 21.0k | 10 | 89% | Infrastructure premium emerging |
| Q4 2027 | 60k | 23.0k | 12 | 90% | Inflection path on track |

### Tesla Expected Milestones (Infrastructure Case)

| Quarter | Fleet | FSD Intervention (mi) | Tier 3 Metros | Utilization (Suburban Avg) | Signal to Watch |
|---------|-------|----------------------|----------------|----------------------------|-----------------|
| Q1 2026 | 8k | 16k | 6 | 58% | Baseline ops |
| Q2 2026 | 12k | 16.5k | 7 | 59% | Slow FSD progress |
| Q3 2026 | 16k | 17k | 8 | 60% | Regulatory momentum |
| Q4 2026 | 22k | 17.5k | 10 | 61% | Deployment accelerating |
| Q2 2027 | 35k | 19k | 13 | 64% | FSD improvement visible |
| Q4 2027 | 50k | 21k | 16 | 67% | Cost advantage emerging |

**Deviations >1.5 sigma from above paths warrant scenario adjustment.**

---

**Last Updated:** May 20, 2026  
**Monitoring Interval:** Quarterly (post-earnings, within 30 days)  
**Repricing Condition:** >10 percentage-point shift in cumulative scenario probability  
**Status:** Ready for H2 2026 quarterly monitoring cycle
