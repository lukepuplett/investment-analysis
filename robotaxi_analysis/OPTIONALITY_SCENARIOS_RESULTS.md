# Optionality Scenarios: 2035 Valuation Results

## Summary

This document presents 2035 terminal valuations for the three optionality scenarios (Conservative, Infrastructure, Natural Monopoly) based on model simulations. The results show how different market structure assumptions and behavior change inflections affect robotaxi company valuations.

---

## Waymo (Google) - 2035 Terminal Valuation by Scenario

| Metric | Conservative (Transport) | Infrastructure Layer | Natural Monopoly |
|--------|--------------------------|----------------------|------------------|
| **Fleet Operating** | **144,000 vehicles** | **165,000 vehicles** | **190,000 vehicles** |
| Gross Annual Revenue | $13.0B | $16.5B | $21.0B |
| **Platform Revenue** | **$4.56B** | **$6.10B** | **$8.20B** |
| Terminal Multiple | 17-18x | 28-32x | 40-45x |
| **Terminal Value (2035)** | **$77.5B** | **$169B** | **$328B** |
| **Discounted PV (10% WACC)** | **$30.0B** | **$65.2B** | **$126.6B** |
| **% of GOOGL Market Cap** | **0.64%** | **1.39%** | **2.71%** |
| **Per Share Impact** | **+$2.48/share** | **+$5.41/share** | **+$10.51/share** |

**Key Drivers:**
- Conservative: Fixed demand (1.35x induced), transport multiples (17-8x), no behavior change
- Infrastructure: 2x induced demand from 2028 onward, infrastructure multiples (32-15x), city OS value
- Monopoly: 1.5x induced demand from 2030, platform multiples (45-20x), moat compounding

---

## Tesla - 2035 Terminal Valuation by Scenario

| Metric | Conservative (Transport) | Infrastructure Layer | Natural Monopoly |
|--------|--------------------------|----------------------|------------------|
| **Fleet Operating** | **180,000 vehicles** | **220,000 vehicles** | **280,000 vehicles** |
| Gross Annual Revenue | $2.1B | $2.8B | $3.9B |
| **Platform Revenue** | **$0.42B** | **$0.58B** | **$0.85B** |
| Terminal Multiple | 9.8x | 15-18x | 20-25x |
| **Terminal Value (2035)** | **$4.1B** | **$9.1B** | **$18.5B** |
| **Discounted PV (10% WACC)** | **$1.6B** | **$3.5B** | **$7.1B** |
| **% of TSLA Market Cap** | **0.10%** | **0.22%** | **0.44%** |
| **Per Share Impact** | **+$0.40/share** | **+$0.88/share** | **+$1.78/share** |

**Key Drivers:**
- Conservative: Tier 3 suburban dominance, lower utilization (55%), tight margins (18% take-rate)
- Infrastructure: Behavior change enables slightly higher fleet, logistics revenue potential
- Monopoly: Reflects winner-take-most dynamics IF autonomy proven, but still limited by market structure

**Critical Insight:** Tesla's option value is much smaller than Waymo's because:
1. Suburban market is intrinsically lower-margin (15-18% take-rate vs 25-32% premium)
2. Manufacturing scale isn't binding; regulatory approval is
3. Behavior change in Tier 3 is limited (Tesla already captures price-sensitive users)

---

## Probability-Weighted Valuations

### Waymo Expected Value

Assuming scenario probabilities (Conservative 40%, Infrastructure 40%, Monopoly 20%):

```
Expected PV = (0.40 × $30.0B) + (0.40 × $65.2B) + (0.20 × $126.6B)
            = $12.0B + $26.1B + $25.3B
            = $63.4B
```

**Per share impact: +$5.26**

Range: +$2.48/share (conservative) to +$10.51/share (monopoly)

### Tesla Expected Value

Assuming scenario probabilities (Conservative 50%, Infrastructure 35%, Bear 15%):

```
Expected PV = (0.50 × $1.6B) + (0.35 × $3.5B) + (0.15 × $0B)
            = $0.8B + $1.2B + $0B
            = $2.0B
```

**Per share impact: +$0.50**

Range: $0/share (bear) to +$1.78/share (monopoly)

---

## Key Differences: Why Waymo Scales Better

### 1. **Premium Market Structure**
- **Waymo:** 25-32% take-rate → higher margin layers, willingness-to-pay for infrastructure
- **Tesla:** 15-18% take-rate → commodity pricing, limited ability to extract infrastructure value

### 2. **Regulatory Moat Compounds in Waymo's Favor**
- **Waymo:** Safety advantage → faster Tier 2 expansion → more revenue to reinvest → better moat
- **Tesla:** Safety must prove (all-or-nothing), then cost advantage becomes competitive not moat

### 3. **Behavior Change Impacts Differently**
- **Waymo:** More land use shift in premium metros (people trade car ownership for convenience)
- **Tesla:** Already in Tier 3 where people own cars; behavior change limited to fewer second cars

### 4. **Infrastructure Layers**
- **Waymo:** Can monetize city integration, logistics, insurance, data at 28-32% premium margins
- **Tesla:** Limited infrastructure value in suburbs (lower density, existing car culture)

---

## Sensitivity: What Breaks Each Scenario?

### Conservative Case Breaks If:
- Regulatory approval faster than expected → Infrastructure case becomes likely
- Behavior change inflection happens earlier than assumed → Monopoly case becomes likely
- Waymo expands to Tier 2 faster → Terminal revenue could be $6B+ instead of $4.56B

### Infrastructure Case Breaks If:
- Behavior change inflection delayed past 2028 → reverts toward Conservative
- City/government doesn't adopt Waymo as essential infrastructure → Monopoly premiums don't materialize
- Tesla autonomy proves competitive → takes suburban Tier 3, limiting Waymo's Monopoly path

### Monopoly Case Breaks If:
- Regulatory consolidation doesn't happen → stays multi-player commodity (Conservative case)
- Safety datasets don't compound strongly → no inflection point, linear growth instead
- Tesla/Uber/others prove autonomous safety equivalent → no winner-take-most

---

## Critical Monitoring Metrics (2026-2030)

To assess which scenario is unfolding:

| Metric | Conservative Path | Infrastructure Path | Monopoly Path |
|--------|-------------------|---------------------|---------------|
| **Waymo Tier 2 Expansion** | Slow (1 new metro/year) | Moderate (1.5/year) | Fast (2+/year by 2029) |
| **Utilization Growth** | Steady 2-3% YoY | Accelerating (3-5% YoY) | Exponential (5%+ YoY) |
| **Take-Rate in Tier 2** | 20-22% (pricing pressure) | 24-26% (infrastructure value) | 28%+ (moat premium) |
| **City Integration Depth** | Traffic mgmt only | Traffic + parking + emergency services | Full mobility OS (energy, logistics, delivery) |
| **Tesla FSD Progress** | Stalls at 18k mi/intervention | Reaches 28k by 2029 | Reaches 35k mi/intervention |
| **Safety Dataset Advantage** | Narrows (Tesla improves) | Widens (Waymo pulls ahead) | Becomes structural moat |

---

## 2026-2035 Revenue Progression (Waymo, Base Scenario)

| Year | Fleet | Trips per Capita | Gross Revenue | Platform Revenue | Annual Multiple Assumption |
|------|-------|-----------------|----------------|------------------|--------------------------|
| 2026 | 2k | 20 | $30M | $10M | 15x (early) |
| 2027 | 8k | 22 | $180M | $65M | 15x |
| 2028 | 18k | 24 | $480M | $180M | 16x |
| 2029 | 32k | 26 | $900M | $350M | 16x (behavior inflection starts) |
| 2030 | 50k | 30 | $1.5B | $570M | 17x |
| 2031 | 70k | 33 | $2.4B | $900M | 17x |
| 2032 | 90k | 36 | $3.4B | $1.2B | 18x |
| 2033 | 110k | 39 | $4.2B | $1.5B | 18x |
| 2034 | 130k | 42 | $5.1B | $1.9B | 18x |
| 2035 | **144k** | **45** | **$13.0B** | **$4.56B** | **17-18x** |

---

## Investment Thesis Implications

### For Alphabet (GOOGL) Shareholders:

**Conservative:** Waymo is a $2.5B/year platform in 2035, worth ~$30B PV. Real but modest.

**Infrastructure:** Waymo becomes a $6B/year city operating system. Worth ~$65B PV. Material optionality.

**Monopoly:** Waymo is a $8B+ platform with compounding moats. Worth >$100B PV. Transformative.

**Probability-weighted: +$5.26/share** — More than 2x conservative case, reflecting infrastructure upside.

### For Tesla (TSLA) Shareholders:

**Conservative:** Robotaxi adds $400M/year revenue, $1.6B value. Negligible for $1.6T company.

**Infrastructure:** Better assumptions (behavior change, city integration) add only modest value. Still <$5B.

**Monopoly:** Only if Tesla wins autonomy AND scales 300k+ vehicles. Even then $7B PV.

**Probability-weighted: +$0.50/share** — Mostly downside risk. Robotaxi is not path to growth.

**Key difference:** Waymo's premium market structure enables infrastructure layers. Tesla's suburban market doesn't.

---

## Next Steps

1. **Quarterly Monitoring:** Use metrics above to track which scenario is unfolding
2. **Scenario Reprice Triggers:** When metrics deviate >2 sigma from scenario path, shift probability weights
3. **Deep Dives:** 
   - Track Waymo Tier 2 regulatory approvals monthly
   - Monitor Tesla FSD intervention rate trajectory quarterly
   - Assess city/government adoption of Waymo as essential infrastructure
4. **Sensitivity Updates:** If behavior change inflection dates shift, recalculate valuations

---

**Last Updated:** May 20, 2026  
**Model Version:** Optionality Scenarios Framework  
**Status:** Ready for quarterly thesis monitoring

