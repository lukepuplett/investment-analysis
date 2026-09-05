# CSCO — Cisco Systems, Inc.

**Sector:** Technology / Networking Hardware & Software
**Exchange:** NASDAQ: CSCO
**Fiscal Year End:** Last Saturday in July (Cisco's FY2026 ended ~July 25, 2026)
**Coverage initiated:** 2026-08-13

---

## Executive Summary (BLUF — Bottom Line Up Front)

**Overall: Cisco is in the middle of a genuine, broad-based networking demand cycle — not just an AI infrastructure order spike — evidenced by accelerating quarterly revenue growth (7.5%→17.6% YoY through FY2026) and double-digit order growth across every geography and customer segment. Operating leverage is excellent (GAAP operating margin +350bps FY2026) and the balance sheet is sound, but the market has already re-rated the stock meaningfully (trailing P/E 25x→41x over the past year) ahead of full delivery on FY2027 guidance, leaving thin margin for error. Initial stance: constructive on business quality, valuation-aware on entry price — a starter position with room to add on weakness, not a full-conviction buy at $113.47.**

### By Analysis Area

- **[Financial](analysis/2026_08_financial_analysis.md):** Cisco closed FY2026 with record revenue of $63.3B (+12% YoY) and accelerating quarterly growth, driven almost entirely by Networking (+22% FY, now 55% of revenue) on AI infrastructure orders. Operating leverage was excellent (opex +1.8% vs. revenue +12%) but gross margin compressed ~40bps YoY, and the balance sheet shows a real working-capital cost of the AI ramp (inventories +80%, current ratio to 0.93).
- **[Market](analysis/2026_08_market_analysis.md):** Growth is broad-based — enterprise orders +21%, public sector +30%, service provider/cloud +95%, all geographies double-digit. Management's "networking super cycle" framing rests on four concurrent drivers (AI/hyperscale, telco scale-across, enterprise refresh, emerging "Mythos"/LDOS catalyst); AI infrastructure itself is only ~10% of guided FY2027 revenue, so durability of the other 90% is the real question.
- **[Competitive](analysis/2026_08_competitive_analysis.md):** Moat strengthened via concrete displacement wins (a 1,000-switch bank deal displacing two named-category competitors) and rebuilt hyperscaler relationships built over ~6 years. Moat is uneven: strong in networking/optics/platform-integration (4-5/5), weaker in security (2/5) where growth lagged most of FY2026.
- **[Technical](analysis/2026_08_technical_analysis.md):** Differentiation rests on Silicon One (P200/G200/G300), Acacia optics, and a flexible silicon/systems/software commercial model. Near-term catalyst is "scale-across" (inter-data-center AI networking, ~14x legacy DCI traffic) with 3 hyperscaler design wins on the P200. Full Silicon One rollout across the portfolio targeted by FY2029 — a multi-year execution commitment to track.
- **[Risk](analysis/2026_08_risk_assessment.md):** No red flag currently meets severity≥8/mitigant≤5, but hyperscaler/AI order concentration (severity 7, mitigant 6) is the risk most likely to re-rate the stock if it deteriorates. Gross margin compression, working-capital cost of the inventory build, and a large unitemized non-operating income swing (+$1,245M FY2026) are secondary items to watch.
- **[Investment Thesis](analysis/2026_08_investment_thesis.md):** 4 of 6 thesis pillars are positive (super cycle breadth, operating leverage, moat, balance sheet); 2 are weak (AI revenue delivery risk, valuation). Overall thesis confidence 6.5/10, weighted toward business quality but discounted for entry price. Q1 FY2027 results (~Nov 12, 2026) are the next explicit checkpoint.
- **[Valuation](analysis/2026_08_valuation_analysis.md):** Trailing P/E 40.9x (vs. 25.3x a year ago), EV/EBITDA 27.5x. The 8.4% post-earnings drop reads as a partial unwind of a gradual, multi-quarter re-rating rather than a fundamentals miss. PEG of 1.21 suggests growth-adjusted pricing is reasonable *if* guidance is delivered, but risk/reward is asymmetric toward disappointment at these levels.

---

## Revenue Breakdown & Growth Drivers Analysis

### Jargon Glossary

| Term | Meaning |
|------|---------|
| **Networking super cycle** | Management's framing for the current multi-year, multi-billion-dollar demand upswing across campus, data center, and AI infrastructure networking simultaneously |
| **Scale-out** | Networking GPUs/accelerators *within* a single data center or cluster |
| **Scale-across** | Networking GPU clusters *between* data centers/facilities due to power/physical constraints — ~14x the traffic of legacy data-center-interconnect (DCI), per management |
| **Silicon One** | Cisco's proprietary programmable networking silicon architecture; chip families include P200, G200, G300 |
| **Acacia** | Cisco's coherent optical/pluggable optics business (acquired 2021) |
| **Open line system / multi-rail optical systems** | Cisco optical-networking technology enabling third-party equipment to use Cisco's coherent optics directly |
| **Mythos / LDOS (Last Day of Support)** | An infrastructure-modernization urgency driver: customers auditing which equipment (Cisco's or competitors') is past end-of-support and can't be patched, creating refresh + competitive-displacement demand |
| **Cisco Cloud Control / AI Canvas / Cisco IQ** | Unified management plane, agentic troubleshooting assistant, and infrastructure-assessment tooling launched June 2026 |
| **RPO / ARR** | Remaining Performance Obligations / Annual Recurring Revenue — subscription/backlog metrics ($46.7B RPO, $32.1B ARR at FY2026 year-end) |
| **Non-GAAP** | Adjusted results excluding share-based comp, amortization of purchased intangibles, restructuring, and certain other items; Cisco reports both GAAP and non-GAAP each quarter |

### FY2026 Revenue Breakdown (Current State)

```
FY2026 Revenue: $63,325M
├── Networking (Product) — $34,668M, 54.8% [+22% YoY]
│   ├── AI Infrastructure (hyperscalers) — ~$4,000M revenue (from $9,300M in orders)
│   ├── Enterprise/Campus switching, routing, wireless — majority of remainder
│   └── Acacia optics — >$1,000M in orders in Q4 alone (embedded in Networking)
├── Security (Product) — $8,232M, 13.0% [+2% YoY]
│   ├── Splunk (observability + security integration)
│   ├── Firewalls (+30%+ order growth, 2 consecutive quarters)
│   └── SASE / XDR / Secure Access / AI Defense
├── Collaboration (Product) — $4,300M, 6.8% [+4% YoY]
│   └── Webex, video devices (+40% YoY), contact center
├── Observability (Product) — $1,095M, 1.7% [+4% YoY]
└── Services — $15,030M, 23.7% [flat YoY]
    └── Support, maintenance, subscription services (48% of total revenue is subscription)

FY2027E Guidance: $72.2B–$73.4B total (+15% at midpoint)
├── AI Infrastructure revenue: $7.5B (+88% vs. FY2026's ~$4B)
├── "Core" (ex-AI) business: ~10% growth (per CFO), decelerating toward
│   the long-term 4–6% algorithm as FY2026 comps normalize through the year
└── Security: guided to high-single-digit growth (vs. +2% FY2026)
```

### Growth Driver Impact Table

| Driver | Segment | FY2026 | FY2027E | Impact | Mechanism |
|--------|---------|--------|---------|--------|-----------|
| AI Infrastructure Hyperscaler Ramp | Networking | ~$4.0B | $7.5B | **+$3.5B** | Silicon One P200/G200 systems + Acacia optics sold into hyperscaler scale-out and scale-across (inter-data-center) buildouts; backed by $9.3B FY2026 order backlog |
| Core Enterprise/Campus Refresh | Networking | Base | Elevated | **Meaningful, embedded in ~10% core growth** | LDOS/Mythos-driven infrastructure audits, Wi-Fi 7 upgrade cycle (>50% of wireless orders), enterprise data-center switching (+35%+ orders) |
| Telco Scale-Across Build-out | Networking (Service Provider) | Emerging | Growing off small base | Orders +30%+ in Q4 | Telcos building capacity for AI-driven data-center-interconnect traffic estimated at ~14x historical DCI levels |
| Security Recovery | Security | $8.2B (+2%) | High-single-digit growth guide | **+$500–700M** | Splunk integration maturing (6,400+ net-new customers since launch), firewall share gains, AI Defense/Guardrails adoption for agentic-AI security |
| Price Increases (component cost passthrough) | Networking (hardware-heavy SKUs) | ~4–5pts of FY26 revenue growth | Front-loaded to H1 FY27, lapping in H2 | Embedded in total revenue growth | Single-digit price increases on memory-intensive hardware, offset partially by ~30 internal memory-efficiency programs (e.g., Wi-Fi 7 memory use cut 50% in ~90 days) |
| Services Stabilization | Services | Flat ($15.0B) | Low-single-digit growth guide | **+$150–450M** | Subscription mix shift, AI-driven customer-experience tooling improving renewal rates (145,000 support cases resolved entirely by AI in FY2026) |

### Translation Examples

**Example 1: Scale-Across & the P200 (Networking / AI Infrastructure)**
- **Jargon:** "Three scale-across design wins for the P200... traffic 14x what it was historically."
- **Translation:** Hyperscalers can no longer fit all the compute for a single AI model in one data center due to power constraints, so they connect multiple facilities together as if they were one giant cluster. This inter-facility traffic is Cisco's estimate of ~14x the traffic volume of pre-AI data-center-interconnect. Cisco's Silicon One P200 chip, paired with Acacia optics and open line systems, is the product bet on this specific, newly-large networking problem.
- **Financial:** Three hyperscalers already ordered against these design wins in Q4 FY2026, contributing to the $9.3B FY2026 AI order total; this is one of the mechanisms behind the $7.5B FY2027 AI infrastructure revenue guide (up from ~$4B FY2026).

**Example 2: Mythos / LDOS (Enterprise Networking Refresh)**
- **Jargon:** "Customers doing analysis right now on their LDOS... last day of support footprint."
- **Translation:** Enterprises are auditing their installed networking/security gear (Cisco's *and* competitors') to find equipment that can no longer receive security patches. This is being treated with the same urgency as cybersecurity spend over the past 3–5 years — not optional, and increasingly funded by shifting budget from other IT line items rather than by new incremental budget.
- **Financial:** Management has not yet seen this show up materially in booked revenue (it's still "pipeline"), but it's cited as a contributor to the >20% campus networking order growth and explicitly enables *competitive displacement* — the manufacturing-customer anecdote in the Q4 call involved replacing a competitor's past-end-of-support gear, not just refreshing Cisco's own installed base.

**Example 3: Price Increases & Memory Costs (Margin Mechanics)**
- **Jargon:** "Price increases... about five points in terms of top-line revenue growth... memory utilization programs."
- **Translation:** Component (especially memory) cost inflation is squeezing gross margin industry-wide. Cisco's response is a mix of single-digit price increases (targeted specifically at higher-memory-utilization hardware SKUs, not blanket increases, and not applied to software) and ~30 internal engineering programs to reduce memory usage per unit — e.g., a 90-day effort cut Wi-Fi 7 memory utilization by 50%.
- **Financial:** Price increases added ~4–5 points to FY2026 revenue growth, front-loaded into H2 FY2026, meaning FY2027 will "lap" much of this benefit in H1 and see less incremental lift in H2 — a partial explanation for the CFO's guided sequential deceleration through FY2027.

### Long-Term Opportunities (3–5 Year Horizon)

- **Silicon One full-portfolio rollout (by FY2029):** If achieved, gives Cisco end-to-end control of its silicon supply chain and innovation pipeline (dealing directly with TSMC, no merchant-silicon middleman) — a structural cost and differentiation opportunity beyond the current AI infrastructure narrow window.
- **Post-Quantum Cryptography (PQC) readiness:** Early-stage but positioned as a multi-year differentiator for regulated-industry customers as quantum-computing risk becomes a board-level concern industry-wide.
- **Cisco Cloud Control / agentic AI tooling (AI Canvas, Cisco IQ):** ~4,500 enterprises signed up since June 2026 launch; not yet quantified as a standalone revenue driver, but a potential platform-stickiness and cross-sell lever once GA (imminent as of Aug 2026).
- **Neocloud/sovereign AI infrastructure:** Currently >$1B FY2026 orders (small relative to hyperscaler's $9.3B) but a distinct, earlier-stage customer category that could diversify AI infrastructure revenue away from the "four top hyperscalers" concentration flagged in the risk assessment.

---

## Data Status (as of 2026-08-13)

| Period | Status | Source |
|--------|--------|--------|
| FY2026 Q1 (period end 10/25/2025) | ✅ 10-Q saved | `quarterly/2026_Q1_10q.htm` |
| FY2026 Q2 (period end 1/24/2026) | ✅ 10-Q saved | `quarterly/2026_Q2_10q.htm` |
| FY2026 Q3 (period end 4/25/2026) | ✅ 10-Q saved | `quarterly/2026_Q3_10q.htm` |
| FY2026 Q4 (period end ~7/25/2026) | ✅ 8-K press release saved — includes full unaudited income statement, balance sheet, and cash flow statement | `quarterly/2026_Q4_press_release.htm` |
| FY2026 Q4 earnings call | ✅ Transcript saved | `quarterly/2026_Q4_earnings_call.txt` |
| FY2026 10-K (full year, audited) | ⏳ **Pending** — expected early Sept 2026 | Not yet filed |
| Stock metrics | ✅ Saved (pasted from Yahoo Finance, 8/13/2026) | `financials/2026_08/yahoo_stats.md` |
| Analysis documents (7 required + this README) | ✅ Complete (initial coverage round) | `analysis/2026_08_*.md` |

**Note on Q4:** Cisco does not file a 10-Q for its fiscal fourth quarter (only three 10-Qs per fiscal year, since Q4 = fiscal year-end). The 8-K press release (filed 2026-08-12) turned out to include full condensed consolidated financial statements (income statement, balance sheet, cash flow), not just headline figures — sufficient for this round of analysis. The FY2026 10-K, once filed, will add audited certification, full footnotes, MD&A narrative, and segment/customer-concentration detail not present in the press release.

---

## Directory Structure

```
csco/
├── README.md                    # This file
├── analysis/                    # 7 required analysis documents (2026_08_*.md)
├── financials/2026_08/          # yahoo_stats.md
├── quarterly/                   # Primary source documents
│   ├── 2026_Q1_10q.htm          # FY2026 Q1 10-Q (period end 10/25/2025)
│   ├── 2026_Q2_10q.htm          # FY2026 Q2 10-Q (period end 1/24/2026)
│   ├── 2026_Q3_10q.htm          # FY2026 Q3 10-Q (period end 4/25/2026)
│   ├── 2026_Q4_press_release.htm # FY2026 Q4/FY 8-K press release (filed 8/12/2026)
│   └── 2026_Q4_earnings_call.txt # FY2026 Q4 earnings call transcript (8/12/2026)
└── question_answers/            # (pending) Q&A documentation
```

## Next Steps

1. Fetch FY2026 10-K once filed (~early Sept 2026) for audited Q4 financials, full footnotes (esp. "Other income, net" composition and customer concentration disclosures), and MD&A — revisit the financial analysis and risk assessment documents at that point.
2. Add lightweight peer valuation/competitive data (Arista Networks at minimum, given closest business-model overlap; Nvidia/Broadcom for AI-networking-silicon competitive context) — currently a data gap flagged in both the competitive and valuation analyses.
3. Build a `CSCO_MONITORING_SCHEDULE.md` covering the run-up to Q1 FY2027 earnings (~Nov 12, 2026) with explicit red-flag/green-light thresholds tied to the AI infrastructure revenue guide and core growth durability.
4. Consider a formal multi-year DCF once a longer post-10-K financial history is available in the repo (flagged as a gap in the valuation analysis).
