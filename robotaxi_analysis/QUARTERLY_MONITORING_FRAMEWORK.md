# Quarterly Monitoring Framework: Regime Determination

## Overview

This document defines the operational monitoring process for determining which robotaxi regime (A/B/C) is materializing. Replaces scenario probability weighting with hard regime transitions.

**Goal:** Quarterly KPI tracking determines observable shifts toward Regime A, B, or C. Hard triggers force regime transitions (not gradual probability shifts).

**Current Probability (May 2026):** A 50%, B 35%, C 15%  
**First Checkpoint:** Q4 2027 (hard data distinguishes regimes)

---

## Regime Definitions at a Glance

| Aspect | **Regime A** | **Regime B** | **Regime C** |
|--------|-----------|-----------|-----------|
| **Ownership Substitution** | <5% | 15–30% | 50%+ |
| **Fleet Size (2035)** | 120–300k | 500k–2M | 10–50M |
| **Take-Rate** | 18–32% | 25–40% | 40–65% |
| **Regulatory Approval** | 3–6%/year | 5–8%/year S-curve | >10%/year exponential |
| **Non-Ride Use** | <5% miles | 10–25% miles | 30%+ miles |
| **2035 Waymo Revenue** | $3–5B | $15–30B | $50–150B |
| **Terminal Value** | $30–90B | $150–400B | $2–10T |
| **Multiple** | 9–18x | 25–50x | 50–150x |

---

## Quarterly KPI Monitoring Scorecard

**Track each KPI. Hard threshold breached = regime transition triggered.**

### Key Metrics by Regime

| KPI | Regime A | Regime B | Regime C | A→B Trigger | B→C Trigger | B→A Collapse |
|-----|----------|----------|----------|------------|------------|-------------|
| **Ownership %** | <5% | 15–30% | 50%+ | 10%+ | 35%+ | <10% |
| **Approval %/yr** | 3–6% | 5–8% | >10% | 8%+ | 10%+ | 2% |
| **Non-Ride % miles** | <5% | 10–25% | 30%+ | 10%+ | 30%+ | <5% |
| **Take-Rate** | 18–32% | 25–40% | 40–65% | 30%+ | 40%+ | <18% |
| **Fleet Size** | <300k | 500k–2M | 10M+ | 500k | 5M | <300k |
| **Intervention Rate** | Improving | Improving 20%+/yr | Improving 30%+/yr | — | — | Flat 4Q |
| **Winner Share** | <70% | <70% | >70% | — | 75%+ | — |

**Data Sources:** Earnings calls, 10-Q MD&A, investor presentations, press releases

---

## Regime-Breaking Events (Trigger Regime Transition)

**If ANY observed, regime transition is FORCED (not probability-weighted).**

| Event | Regime Shift | Action |
|-------|-------------|--------|
| **Ownership <10% after 3+ years availability (Waymo/Tesla combined)** | B→A | Collapse to Regime A; demand insufficient for ownership replacement |
| **Approval <2%/year sustained 2+ years** | B→A | Regulatory environment unchanged; not civilization-scale |
| **Take-rate <18% sustained (Waymo Tier 1)** | B→A | Uber re-enters; margin collapse to commodity |
| **Intervention rate flat 4+ quarters** | B→A or C→B | Autonomy stalled; fragility evident |
| **One player captures >75% share in any tier** | A→B or B→C | Software scaling evident; winner consolidation |
| **Approval >8%/year (Waymo)** | A→B | Regulatory environment accelerating |
| **Ownership >35% in major metro** | B→C | Ownership replacement structural |
| **Non-ride >30% of miles** | B→C | Platform layer exceeds core ride |
| **Cost decline >30%/year sustained** | B→C | Software scaling compounding |
| **Major incident (fatality, crash)** | →A | Safety narrative reversed |
| **Regulatory approval reversed** | →A | Pilot closure; policy flip |

---

## Quarterly Data Collection (Due 30 Days Post-Earnings)

| Source | Extract | Waymo (GOOGL) | Tesla (TSLA) |
|--------|---------|---|---|
| **10-Q + MD&A** | Deployment plans, guidance, risks | Fleet guidance, utilization plan | FSD timeline, Robotaxi capex |
| **Earnings Call** | Management tone on approval, autonomy progress | Approval pace, intervention rate | FSD improvement rate, tier expansion |
| **Investor Presentation** | Roadmap, new use cases | Non-ride monetization signals | Cost structure, manufacturing trends |
| **Press Release** | Fleet size, metro expansion | Ownership behavior signals | Regulatory wins, competitive positioning |

---

## Regime Determination Rules

**If KPI hits hard trigger threshold, regime transition is FORCED.**

| KPI Trend | Regime A | Regime B | Regime C | Decision |
|-----------|----------|----------|----------|----------|
| **Ownership grows 5→10%** | Challenged | Threshold hit | — | A→B forced |
| **Approval accelerates to 8%+/year** | Challenged | Threshold hit | — | A→B forced |
| **Non-ride climbs to 10% of miles** | Challenged | Threshold hit | — | A→B forced |
| **Take-rate sustains >30%** | Challenged | Threshold hit | — | A→B forced |
| **Fleet guidance exceeds 500k** | Challenged | Threshold hit | — | A→B forced |
| **Ownership grows 30→35%** | — | Challenged | Threshold hit | B→C forced |
| **Approval accelerates to 10%+/year** | — | Challenged | Threshold hit | B→C forced |
| **Non-ride climbs to 30% of miles** | — | Challenged | Threshold hit | B→C forced |
| **One player >75% of market** | — | Challenged | Threshold hit | B→C forced |
| **Ownership stalls <10% (after 3yr)** | Confirmed | — | — | B→A collapse |
| **Approval stalls <2%/year** | Confirmed | — | — | B→A collapse |
| **Take-rate drops <18%** | Confirmed | — | — | B→A collapse |
| **Intervention rate flat 4+ quarters** | Confirmed | Challenged | — | C→B or B→A |

---

## Annual Deep Dive (Q4 Only)

**Within 30 days of Q4 earnings; determines if regime assumptions still hold for 2027+.**

- [ ] Full-year intervention rate trend (did company hit improvement targets?)
- [ ] Take-rate by tier YTD (any compression signals?)
- [ ] Fleet expansion actual vs. guidance (on track for regime's fleet size targets?)
- [ ] Non-ride revenue mix (emerging or flat?)
- [ ] Ownership substitution signals (market data, insurance, public transit ridership)
- [ ] Competitive gap (Waymo vs. Tesla intervention rate delta widening/narrowing?)
- [ ] If regime threshold hit: Update GOOG/TSLA investment thesis with new regime valuation

---

## When a Hard Trigger is Hit

**If any KPI reaches regime threshold, regime transition is FORCED.**

**Immediate Actions (within 5 business days):**
1. Confirm threshold breach (cross-validate with multiple data sources)
2. Recalculate terminal valuations using new regime economics
3. Update per-share impact (valuation drops/spikes discontinuously)
4. Update GOOG/TSLA investment thesis documents
5. Document which KPI(s) forced the regime shift

**Example: Q2 2026 A→B Trigger**
- Waymo ownership substitution measured at 12% (vs. Regime A max 5%)
- **Trigger:** Hard threshold A→B breached
- **Action:** Regime A model ($30–90B Waymo valuation) → Regime B model ($150–400B)
- **Valuation jump:** Discontinuous, not gradual
- **Thesis update:** Publish revised per-share impact; recommend position increase

---

## Monitoring Timeline

| Timing | Deliverable | KPI Check |
|--------|-------------|-----------|
| **T+30 days post-earnings** | Quarterly KPI tracking | Which KPIs moved toward regime thresholds? |
| **T+45 days post-earnings** | Regime assessment | Did any hard trigger breach? |
| **Q4 only (T+60 days)** | Annual deep dive | Do regime assumptions still hold for 2027+? |

**Key Checkpoints:**
- **Q4 2027:** First major checkpoint (A confirm, B trigger evident, or C signals)
- **Q4 2028:** Second checkpoint (B escalate to C, or fallback to A)
- **Q4 2030:** Final regime determination

---

## Regime Transition Timeline (Baseline Expectations)

| Event | Regime A Path | Regime B Path | Regime C Path |
|-------|---|---|---|
| **Q1–Q3 2026** | Confirmation or first A→B signals | Early signals (approval >6%, ownership 5–10%) | Unlikely (pre-B threshold) |
| **Q4 2026** | Confirm A or hit A→B trigger | Progress toward B (ownership 10–15%, approval 7%) | Unlikely |
| **Q2 2027** | If A: Hold through 2027 | Ownership 15–20%, approval 7–8%, evidence of B dynamics | Unlikely |
| **Q4 2027** | Final confirmation A (50%+ prob remains) | Ownership 20–25%, approval 8%+, first B→C signals visible | Early signals (ownership 30%+, approval 9%+) |
| **Q4 2028** | Very unlikely to shift further | Ownership 25–30%, still in S-curve | Ownership 35–45%, approval 10%+, B→C trigger possible |

**Last Updated:** May 20, 2026  
**Monitoring Interval:** Quarterly  
**Status:** Ready for H2 2026 monitoring cycle
