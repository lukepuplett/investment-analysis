# CoreWeave, Inc. (CRWV) – Technical & Infrastructure Analysis
*Analysis Date: November 11, 2025*

## Executive Summary

**BLUF: CoreWeave expanded active power to ~590 MW and contracted capacity to ~2.9 GW, leading industry adoption of NVIDIA Blackwell systems while mitigating third-party build delays through self-development initiatives—execution hinges on synchronizing power, cooling, and GPU deliveries to unlock >1 GW of unsold capacity.**

## Infrastructure Footprint
- Added eight new U.S. data centers in Q3, strategically located to diversify grid exposure and reduce latency for coastal customers.
- International push includes UK government-supported campuses (notably in Scotland) and a $6B commitment to a Lancaster, Pennsylvania, facility scaling from 100 MW to 300 MW.
- Contracted power portfolio reaches 2.9 GW with >1 GW available for future bookings, indicating substantial latent capacity once shells and electrical fit-outs complete.

## Power & Cooling
| Component | Status | Notes |
|-----------|--------|-------|
| Active Power | ~590 MW | +120 MW QoQ, reflecting rapid energization of new halls |
| Contracted Power | ~2.9 GW | Mix of utility agreements and third-party shell partnerships |
| Cooling Innovations | Liquid and immersion-ready | Necessary for GB300 NVL72 densities |
| Supply Bottleneck | Powered-shell delays | Third-party developer running behind schedule; self-builds to offset |

- Powered-shell delays at a partner site are the primary gating factor for near-term revenue recognition; customer agreements have been amended to extend expiration dates, preserving economics.
- DDTL financing and OEM arrangements reduce upfront cash needs for electrical gear and GPUs, enabling parallelism across multiple sites.
- Q&A confirmed customer willingness to adjust schedules without sacrificing contract value, validating resilience of CoreWeave’s delivery commitments despite the isolated shell delay.
- Capex guidance was trimmed to $12–14B for 2025, shifting spend into early 2026; while management views this as timing, it underscores dependency on third-party construction pacing and the need for tighter project controls as self-build ramps.

## Compute & Networking Stack
- First to deploy NVIDIA GB300 NVL72 systems and general availability of RTX PRO 6000 Blackwell Server Edition instances, cementing early-mover advantage.
- Existing clusters leverage H100 and GH200 GPUs with proprietary networking to deliver low-latency, high-throughput interconnects tailored for large-scale training.
- Acquisition of OpenPipe enhances reinforcement learning tooling, while Marimo and Monolith add orchestration and physical-world inference capabilities, layering software differentiation atop hardware.

## Operational Initiatives
- Self-build program: CoreWeave is taking direct control of site development to combat third-party delays, enabling tighter control of schedules and cost.
- CoreWeave Ventures: Strategic investments in AI startups create design partners for emerging workloads, helping tune hardware-software co-optimization.
- Capacity management: >1 GW of contracted but unsold power provides buffer to onboard customers as GPU deliveries ramp; ensures flexible matching of demand surges.

## Scalability & Reliability
- Multi-region architecture across U.S. and UK improves resilience and supports sovereign hosting requirements.
- Redundant power feeds and diversified providers mitigate single-point failure risk, though dependency on high-voltage upgrades remains a watch item.
- Automation and AI ops (via acquisitions) aim to streamline cluster provisioning, reducing time-to-utility for new racks.

## Key Technical Risks
- Continued reliance on third-party powered shells until self-build assets fully replace delayed capacity.
- Synchronizing GPU supply (dependent on NVIDIA production) with energized racks; any manufacturing slip could create stranded capital.
- Rapid scale increases thermal and operational complexity; requires ongoing investment in tooling and talent.

## Cross References
- Market demand lens: `2025_11_11_market_analysis.md`
- Competitive dynamics: `2025_11_11_competitive_analysis.md`
- Financial impact: `2025_11_11_financial_analysis.md`
- Risk consolidation: `2025_11_11_risk_assessment.md`
- Strategic synthesis: `2025_11_11_investment_thesis.md`
- Source documents: `../quarterly/2025_Q3_press_release.txt`, `2025_11_11_metric_notes.md`
