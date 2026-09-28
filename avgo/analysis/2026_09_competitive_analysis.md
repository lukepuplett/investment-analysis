# AVGO — Competitive analysis (Sep 2026)

## Executive Summary

**BLUF: Broadcom’s moat in AI infrastructure is a bundle of cornered-resource ASIC relationships, scale/process in networking silicon, and switching costs in VMware — durable but not permanent as hyperscalers insource and Nvidia pushes Spectrum-X.**

## AI custom silicon (hyperscaler ASICs / XPUs)

| Factor | Assessment |
|--------|------------|
| Position | Leading external custom AI accelerator vendor for top hyperscalers (co-design, multi-year ramps) |
| Moat type | **Cornered resource** (customer-specific designs + execution track record) + **process power** (tape-out cadence, packaging, bring-up) |
| Threats | Customer insourcing (Google TPU, Amazon Trainium, etc.); second-source ASIC houses; margin pressure as programs mature |
| Monitoring | AI semi revenue vs guide ($16.7B Q3 → $21.7B Q4 outlook); design-win commentary on calls |

## AI networking (merchant silicon)

| Factor | Assessment |
|--------|------------|
| Position | Dominant merchant Ethernet switch ASIC supplier (Tomahawk/Jericho families) for cloud/AI fabrics |
| Moat type | **Scale economies** + **switching costs** (qualification cycles, software stack integration) |
| Threats | **Nvidia** (Spectrum-X, vertical stack); **Marvell**; OEM captive designs; **China** scrutiny on networking gear (Sep 2026 headline risk) |
| Monitoring | Networking called out with custom XPUs as “very strong”; watch hyperscaler architecture shifts (scale-up vs scale-out) |

## Infrastructure software (VMware)

| Factor | Assessment |
|--------|------------|
| Position | Enterprise virtualization / cloud foundation incumbent post-2023 acquisition |
| Moat type | **Switching costs** + **scale** in installed base |
| Threats | Public-cloud native stacks; open-source KVM; customer pushback on bundling/pricing; integration execution |
| Monitoring | Infrastructure software +29% YoY Q3 — healthy but slower than AI semi; renewal churn KPIs in 10-Q MD&A |

## Competitive Moat Scorecard

| Moat factor | Rating (1–5) | Notes | Durability | Replicability |
|-------------|:------------:|-------|------------|---------------|
| Custom AI ASIC relationships | 5 | Q3 AI semi $16.7B scale | 3–5 yr program cycles | Medium — insource risk at top 3 clouds |
| Networking ASIC leadership | 4 | Shared AI cluster build-out | 3–5 yr | Medium-high — Nvidia vertical integration |
| VMware installed base | 4 | Recurring subscription engine | 5+ yr | Medium — cloud substitution |
| M&A integration playbook | 4 | Serial acquirer (CA, Symantec, VMware) | Ongoing | Hard for smaller peers |
| Scale / gross margin | 5 | ~75% gross margin Q3 | Cycle-dependent | High capital + talent barrier |

**Average (unweighted): ~4.4/5** — strong compounder profile in semis + software, cyclicality still real.

## Peers to watch

- **NVDA** — GPU + networking vertical; competes for AI cluster budget  
- **MRVL** — Custom silicon + networking  
- **ANET** — Systems layer using merchant silicon  
- **CSCO** — Platform integration narrative vs merchant ASIC supply (see `csco/` analyses)  

## Cross-references

- Financial segments: [`../financials/2026_08/income_statement.md`](../financials/2026_08/income_statement.md)  
- Risk audit: [`2026_09_risk_assessment.md`](2026_09_risk_assessment.md)  
