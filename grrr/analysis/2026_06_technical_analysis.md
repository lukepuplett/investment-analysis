# GRRR – Technical Analysis (Q1 2026)

## Executive Summary

GRRR's technical roadmap is ambitious but executable. Three major projects are on track: (1) Yotta India GPU deployments (first delivery July; revenue Sep–Nov 2026), (2) NeutraDC co-location (online Q3/Q4 2026), (3) Korat 200-MW data center campus (construction Q3/Q4 2026; revenue 2027+). GPU supply chain remains the key risk—NVIDIA allocations are secure via Supermicro partnership, but memory/storage shortages are creating 2–4 week delays. Project financing term sheets ($500M–$800M) are in advanced discussions; closure expected by end of Q3 2026. No catastrophic technical risks identified; execution risk is primarily organizational (hiring ramp, procurement complexity, contractor coordination).

---

## Yotta India GPU Deployment (Largest Near-term Driver)

### Contract Value: $3.2B (3 phases)

| Phase          | Deployment    | Revenue Timing   | Status                           |
|----------------|---------------|------------------|---------------------------------|
| **Phase 1**    | July 2026     | Sep–Nov 2026     | POs placed; Supermicro confirms delivery |
| **Phase 2**    | Aug–Sep 2026  | Oct–Dec 2026     | In manufacturing; on schedule   |
| **Phase 3**    | Oct–Nov 2026  | Dec 2026–Jan 2027 | Planned; supply chain watchpoint |

### Technical Execution Plan
1. **GPU provisioning:** B300 servers (Supermicro OEM); ~1000 servers for Phase 1
   - Unit cost: ~$500k per B300 server + networking/storage
   - **Supply risk:** Memory (HBM) and storage (NVMe) constrained globally; 2–4 week delays reported
   - **GRRR mitigation:** Direct integration with Supermicro co-founder Charles Liang; weekly sync calls to prioritize allocation

2. **Infrastructure readiness:** Co-location facility already secured (lease signed)
   - Power: 10–15 MW available from day 1
   - Cooling: Pre-installed chiller systems; capacity verified
   - Networking: Dark fiber + public internet redundancy

3. **Deployment sequencing:** Rack-by-rack onboarding over 3 months
   - Each rack = 5–10 servers + networking + monitoring
   - Testing phase: 2 weeks per pod (stress test, cooling validation, customer acceptance)
   - Go-live: Customer cuts live traffic once pod certified

4. **Customer success setup:**
   - Dedicated GRRR team embedded on-site (20+ people)
   - 24/7 NOC (Network Operations Center) for monitoring
   - Quarterly capacity planning reviews with Yotta

**Risk:** Memory/storage shortage delays delivery by 4 weeks → Phase 1 slips to Aug, revenue hit Dec instead of Nov. **Mitigant:** Supermicro prioritization + forward contracting (likely in place per CEO comments).

---

## Thailand Korat 200-MW Campus (Strategic Asset)

### Timeline & Milestones

| Period            | Milestone                         | Status                                   |
|-------------------|-----------------------------------|------------------------------------------|
| **Q2 2026**       | Land acquisition complete         | ✅ Done; title secured                    |
| **Q3/Q4 2026**    | EPC (Engineering, Procurement, Const.) bidding | In progress                 |
| **Q4 2026–Q1 2027** | Foundation + concrete pour        | Planned Q3/Q4; EPC selection pending    |
| **2027 H1**       | Building shell + MEP (mechanical, electrical, plumbing) | 2027 timeline                |
| **2027 H2–2028**  | First pods online; capacity ramp   | Revenue starting 2027 H2                |

### Power & Infrastructure
- **Power securing:** 200 MW contract secured with Thai utility (Glow, state-owned)
  - Grid stability: Thailand has stable power infrastructure (vs. India's intermittency risk)
  - Cost: ~$0.05/kWh (regional cost advantage vs. US: $0.08–$0.10)
  - **Risk:** Geopolitical (Thailand political volatility could delay permits); low probability but monitored

- **Water (cooling):** Secured from local water authority; 50M gallons/day capacity
  - Immersion cooling technology (Astrikos optimization) = 40% reduction vs. air cooling

- **Connectivity:** Dark fiber partnerships + direct internet exchange (IXP) access in Bangkok region
  - Latency to India: <50ms (regional advantage)

### Capital Requirements
- **Capex estimate:** $80–100M for 200-MW buildout (phased)
  - Phase 1 (50 MW): $20M (Pod 1–4, 2027 online)
  - Phase 2 (100 MW): $50M (Pod 5–12, 2027–2028 online)
  - Phase 3 (50 MW): $30M (Future expansion, 2028+)

- **Funding:** Project financing expected to cover 70–80% ($60–80M term loans); GRRR equity + vendor financing cover remainder

**Risk:** Concrete pour delays (weather, permitting) → revenue pushed into 2028. **Mitigant:** EPC selection underway; conservative H1 2027 timeline already baked in CEO guidance.

---

## NeutraDC Co-location (Quick-Win Capacity)

### Contract Scope
- **Capacity:** 3–5 MW immediate; 10+ MW by end 2026
- **Facility:** Existing NeutraDC data center (already operational)
- **Timeline:** Racks online Q3/Q4 2026
- **Revenue:** $80–120 per rack-month = ~$1–3M annually (depending on fill rate)

### Technical Readiness
- **Power:** Already available at facility (no capex needed for power infra)
- **Cooling:** Existing chiller systems; adequate for GPU workloads
- **Networking:** NeutraDC partnering to upgrade peering + dark fiber (GRRR co-investing)
- **Deployment:** 4–6 weeks to onboard racks once signed

**Risk:** Low. Facility already built; GRRR just leasing racks. **Timeline confidence:** High.

---

## GPU Supply Chain & Procurement

### NVIDIA Allocation Status
- **Secure:** H100 and H200 GPUs available per Supermicro allocation
- **Watchpoint:** B300 (latest generation) supply constrained
  - Yotta Phases 2–3 depend on B300 availability
  - NVIDIA releasing Q3 2026; volume ramp Q4 2026
  - **Risk:** If Vera Rubin (next gen) launches ahead of expectations, customers may delay B300 purchases
  - **GRRR mitigation:** Long-term allocation agreement with NVIDIA (mentioned in call); CEO in regular discussions with Jensen Huang's office

### Memory & Storage Bottleneck (Current Pain Point)
- **HBM (high-bandwidth memory):** Supply <demand until Q3 2026
  - Delay: 2–4 weeks typically
  - **GRRR impact:** Phase 1 slips risk (mitigated by Supermicro priority)

- **NVMe Storage:** Similar constraints
  - GRRR using Supermicro as aggregator (they negotiate with component suppliers)

**Overall supply chain health:** 7/10. No show-stoppers, but tight execution required.

---

## Project Financing & Capital Stack

### Current Status (As of Q1 2026)
- **Term sheets received:** 3–4 offers in range of $300M–$800M+
  - Debt financing at project/SPV level (non-recourse to parent)
  - Structures: Senior debt + mezzanine + equity tranches
  - Terms: 7–10 year amortization (matching asset life)

- **Key lenders:** Global infrastructure funds (pension funds, endowments), DFIs (development finance institutions), commercial banks
  - Examples: Asian Development Bank, World Bank IFC, private equity infrastructure funds

- **Timing:** Documentation phase expected Q2/Q3 2026; closure by Q3/Q4 2026

### Leverage Profile
| Source              | Amount          | Cost      | Notes                                 |
|---------------------|-----------------|-----------|---------------------------------------|
| Project debt        | $500M–$800M     | 4–6%      | Non-recourse; secured on assets/contracts |
| Vendor financing    | $300M–$500M     | 2–4%      | Supermicro, equipment suppliers      |
| Equity / Internal   | $1B+            | Cost of capital | GRRR + strategic investors         |
| **Total capex need** | **$5B+**        | Blended ~4% | For 2026–2028 Korat + regional expansion |

**Capital deployment plan:**
- 2026: $500M–$700M (Korat Phase 1, Yotta hardware, co-location setup)
- 2027: $1.5–$2B (Korat expansion, new regional campuses)
- 2028: $1–1.5B (capacity scaling, technology refresh)

**Risk:** Project financing closes slower than expected → capex delayed 6 months. **Mitigant:** GRRR has $98.9M cash + vendor financing bridges gap (Supermicro provides favorable terms).

---

## Execution Risks & Mitigants

| Risk                           | Severity (1–10) | Mitigant                                  | Strength |
|--------------------------------|-----------------|-------------------------------------------|----------|
| **GPU supply delays**          | 6               | Supermicro priority agreement, CEO engagement | 7/10    |
| **Memory/storage shortage**    | 5               | Forward contracting, vendor relationships | 6/10    |
| **Korat permits / delays**     | 4               | Thai govt partnership, EPC pre-selection | 7/10    |
| **Project financing delay**    | 5               | Multiple term sheets in advanced stage   | 8/10    |
| **Yotta project creep**        | 4               | Signed contract + fixed price model      | 8/10    |
| **Hiring ramp slowdown**       | 5               | Added 100+ people Q1; plan for 5–10x more in H2 | 6/10 |
| **Geopolitical (Thailand/Egypt/Taiwan)** | 6 | Diversified footprint (India, Indonesia also building) | 6/10 |

---

## Key Technical Metrics to Monitor

| Metric                          | Target 2026E | Status | Watchpoint              |
|---------------------------------|--------------|--------|-------------------------|
| **GPU servers deployed**        | 1000–1500    | 0 (Q1) | Yotta Phase 1 ramp; expect 500+ by Q4 |
| **Co-location racks online**    | 100–150      | 0 (Q1) | NeutraDC ramp Q3/Q4     |
| **Korat MW operational**        | 0–10 (foundation stage) | Land secured | Concrete pour Sep–Oct critical |
| **Project financing closed**    | Yes          | In docs | Expected Q3 closure     |
| **Hiring headcount**            | 300–500      | 100+ in Q1 | Pace: 50–100 per month in H2 |
| **Data center uptime**          | 99.95%+      | TBD (deployment phase) | Track once Yotta online |
| **Customer deployment cycles**  | 8 weeks avg  | TBD    | Track per Yotta project |

---

## Investment Takeaway

GRRR's technical execution is credible. Three major projects (Yotta, Korat, co-location) are progressing on timeline. GPU supply chain is tight but manageable via Supermicro partnership. Project financing is advanced; closure expected Q3 2026. 

**Key execution window:** Jun–Oct 2026. If Yotta Phase 1 ships on schedule (July) and co-location comes online (Q3/Q4), GRRR gains critical mass for revenue ramp in H4 2026. If any slip by >8 weeks, 2026 guidance ($160–$200M) is at risk.

**Confidence level:** 7/10 on timeline, 8/10 on technical feasibility. Organizational execution (hiring, contractor coordination) is the variable.
