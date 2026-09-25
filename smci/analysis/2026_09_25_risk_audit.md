# Super Micro Computer (SMCI) — Risk Audit & Thesis Invalidation Check

**Analysis date:** 25 Sep 2026 (Europe/London)  
**Price (NASDAQ:SMCI):** **$41.51 USD** (Yahoo chart API, regular-session close / last print as of 24–25 Sep 2026; 52-week range ~$19.48–$58.78)  
**Period evidence:** FY2026 full year + Q4 (ended 30 Jun 2026), reported **11 Aug 2026** (8-K Item 2.02 + Ex. 99.1); audited detail in **Form 10-K filed 31 Aug 2026**  
**Prior anchors:** June 2026 thesis/risk pack (~$50.17); Q3 FY2026 delta (~$46.88, May 2026 call)  
**Status:** ✅ Complete — research recommendation only (no trade ticket)

---

## Thesis status (BLUF)

### Verdict: **WATCH (one pillar wobbling)** — **not invalidated**

| Pillar | Status vs June / Q3 notes | vs hard invalidation triggers |
|--------|---------------------------|-------------------------------|
| Customer concentration | **WOBBLING** — breadth improved (≥10% customers 4→1), but **single-customer sales rose to 28.1%** | Pass (no >65–70% top-4 spike; no disclosed major CSP defection) |
| Gross margin compression | **IMPROVED** — Q4 GAAP GM **17.5%** / non-GAAP **17.6%**; FY GM 10.8% | Pass (not <9.5%) |
| DCBBS execution | **IMPROVED (qualitative)** — management credits DCBBS for mix/profitability; product line scaled | Pass (no evidence of pilot failure / >6-mo slip) |
| Competitive share loss | **NO HARD FAIL** — FY26 $39.1B (+78%), FY27 guide $65–72B, >$60B Q4 new orders | Pass (no evidence share <15%; data gap remains) |

**Why WATCH, not INTACTor INVALIDATED:** Growth, Q4 margin, backlog, and DCBBS commentary **strengthen** the June BUY / Q3 STRONG-BUY operating thesis. The **shape** of concentration risk worsened (one customer = 28.1% of FY26 net sales ≈ **$11.0B**). Price has also fallen into the prior **bear band ($40–50)** while WC intensity (FY26 operating cash flow **−$6.8B**) and ongoing **government export-control inquiries** remain market overhangs — they are not the four card flags, but they help explain the tape vs fundamentals.

**Recommendation to Luke (not an order):** Hold thesis on monitor; **dig deeper** on Customer One identity/contract durability and Q1 FY27 WC/FCF; **consider trim only if** concentration disclosure worsens, Q1 GM collapses back toward single digits without mix explanation, or a named hyperscaler exit appears. Buy/sell/size remains Luke’s call.

---

## Sources (primary)

1. Super Micro Ex. 99.1 press release, **11 Aug 2026** — “Fourth Quarter and Full Fiscal Year 2026 Financial Results” (8-K 0001375365-26-000021).  
2. Super Micro **Form 10-K** for year ended 30 Jun 2026, filed **31 Aug 2026** (0001375365-26-000022) — concentration XBRL, MD&A, risk factors, investigation disclosure.  
3. Repo priors: `smci/analysis/2026_06_risk_assessment.md`, `2026_06_investment_thesis.md`, `2026_Q3_delta_analysis.md`, `smci/README.md`, `SMCI_MONITORING_SCHEDULE.md`.  
4. Spot price: Yahoo Finance chart API (`SMCI`), 25 Sep 2026 session.

FMP `/stable/quote` was unavailable on this box plan (402); Yahoo used for price. Social/X chatter used only as pointers; **all numbers below are from SEC Ex. 99.1 / 10-K** unless marked otherwise.

---

## FY2026 / Q4 snapshot (facts)

| Metric | Q4 FY26 | FY2026 | YoY / vs prior guide |
|--------|---------|--------|----------------------|
| Net sales | **$11.12B** | **$39.06B** | FY +78% vs $22.0B; within raised guide $38.9–40.4B |
| Gross margin (GAAP) | **17.5%** | **10.8%** | Q4 vs Q4’25 9.5%; FY vs FY25 **11.1%** (−30 bps) |
| Gross margin (non-GAAP) | **17.6%** | **10.9%** | Q4 vs Q4’25 non-GAAP 9.6% |
| Diluted EPS (GAAP) | $1.62 | $3.26 | FY vs $1.68 |
| Diluted EPS (non-GAAP) | $1.70 | $3.63 | — |
| Cash & equiv. (30 Jun 26) | — | **$7.5B** | vs $5.2B YE FY25 |
| Bank debt + convertibles | — | **$8.7B** | Balance-sheet leverage up with growth |
| Operating cash flow (FY) | Q4 OCF +$747M | **−$6.81B** | Inventory/AR build dominated |
| Q1 FY27 sales guide | — | **$14.5–15.5B** | — |
| FY27 sales guide | — | **$65–72B** | — |
| Q4 new orders / backlog | — | **>$60B** new orders; “record backlog” into FY27 | CEO quote, Ex. 99.1 |

MD&A (10-K): FY GM decline to 10.8% attributed to **competitive pricing to gain share**, product/customer mix, and higher manufacturing costs — even as Q4 mix/margins spiked.

---

## Flag 1 — Customer concentration

### Evidence since June / Q3

- **FY2025 (10-K XBRL):** Four customers each ≥10% of net sales — **20.9% + 11.5% + 11.3% + 11.1% ≈ 54.8%** (aligns with prior “~60% / 4 CSPs” OEM framing).  
- **FY2026 (10-K narrative + XBRL):** **One** customer ≥10% of net sales — **Customer One = 28.1%** of FY26 net sales (~**$11.0B**). Count of ≥10% names **fell 4→1** (diversification of *named* mega-accounts), but **peak single-name exposure rose** (20.9%→28.1%).  
- **AR concentration (30 Jun 2026):** Three customers **23.0%, 17.1%, 12.5%** of AR (~52.6% combined) — credit/collection concentration still high.  
- **Geographic:** US **70.9%** of FY26 net sales (vs 59.4% FY25) — more US-centric with large AI deployments.  
- CEO (Ex. 99.1): “added several hundred enterprise and other customers”; richer enterprise mix cited alongside DCBBS.  
- **Not disclosed:** Named identity of Customer One; updated “6–8 large CSP” count; top-4 % under the old definition (only one name clears 10%).

### Severity / mitigants

| | June 2026 | 25 Sep 2026 |
|--|-----------|-------------|
| Severity | 8/10 | **8/10 (reshaped)** — fewer ≥10% accounts, higher single-name peak |
| Mitigants | Diversify to 6–8 CSPs; enterprise/sovereign; DCBBS stickiness | Enterprise adds + DCBBS still cited; **single-customer mitigant weaker** |

### Pass / fail vs invalidation triggers

| Trigger (thesis / schedule) | Result |
|-----------------------------|--------|
| Large CSP major defection announced | **Not triggered** (no such disclosure) |
| Customer concentration >65% (top-4 style) / >70% hard stop | **Not triggered** — cannot recompute top-4; single name 28.1% |
| Concentration rises to >65% (bear case) | **Not triggered** |

**Flag score: WATCH / FAIL-OPEN on “mitigated” narrative** — mitigant partially working on *breadth*, failing on *peak*.

---

## Flag 2 — Gross margin compression

### Evidence since June / Q3

- Q3 FY26 delta celebrated non-GAAP GM **~10.1%** as de-risking the path to 12%+ FY27.  
- Q4 FY26: GAAP **17.5%**, non-GAAP **17.6%** — far above the Sep monitoring green light (10.5%+) and above the old “sustain double-digit” bar.  
- Full-year FY26 GAAP GM **10.8%** (vs 11.1% FY25): recovery is **back-half / mix driven**, not yet a full-year structural 12%+.  
- Management explicitly links profitability improvement to **enterprise mix + DCBBS adoption** (Ex. 99.1).  
- MD&A still flags competitive pricing / mix as FY headwind — Q4 quality must be sustained in Q1 FY27 ($14.5–15.5B guide).

### Severity / mitigants

| | June 2026 | 25 Sep 2026 |
|--|-----------|-------------|
| Severity | 8/10 | **5/10** (near-term) / 6/10 (sustainability) |
| Mitigants | Tariff relief, DCBBS, Malaysia | Appearing in P&L; Q4 proves upside elasticity |

### Pass / fail vs invalidation

| Trigger | Result |
|---------|--------|
| GM <9.5% (hard stop / thesis invalidation) | **PASS** — Q4 17.5%; FY 10.8% |
| Margin stalls <11% with no path | **PASS for now** — Q4 overshoots; FY still ~11% |

**Flag score: PASS** — compression thesis risk **materially reduced** vs June; watch **sustainability** and mix disclosure in Q1 FY27.

---

## Flag 3 — DCBBS execution

### Evidence since June / Q3

- June: pilots / <1% revenue; Q3 delta: “visible” in margin mix, still no %.  
- Ex. 99.1: CEO credits “broader adoption of our optimized **DCBBS** architecture” for improving profitability with richer enterprise mix.  
- 10-K: DCBBS framed as core strategy (rack-to-site modular AI factories); **>10 key subsystems** in ~1 year (CDUs, heat exchangers, power shelves, BBU, towers, switching, DCIM software, etc.); DCBBS campus / Silicon Valley capacity; blueprints for next-gen NVIDIA rack platforms (incl. Vera Rubin NVL72 / HGX Rubin NVL8 per 10-K product discussion).  
- **Still not disclosed:** DCBBS **% of revenue**, services attach rate, or cohort gross margin.

### Severity / mitigants

| | June 2026 | 25 Sep 2026 |
|--|-----------|-------------|
| Severity | 7/10 | **5/10** (execution risk down; disclosure risk remains) |
| Mitigants | Pilots, management track record | Commercial narrative + margin co-movement |

### Pass / fail vs invalidation

| Trigger | Result |
|---------|--------|
| Pilots >20% cost overrun or >6-month slip | **Not evidenced** |
| DCBBS adoption stalls / <2% of revenue (schedule red flag) | **Unknown** — % not disclosed; qualitative evidence of adoption |

**Flag score: PASS (qualitative) / MONITOR (quantitative gap)** — do not treat as failed product; demand Luke-grade % disclosure next earnings.

---

## Flag 4 — Competitive share loss

### Evidence since June / Q3

- June risk: HPE/Dell/Lenovo closing TTM gap; share could fall toward 12–15% by FY28E.  
- FY26 revenue **$39.1B** (+78%) and FY27 guide **$65–72B** are inconsistent with an acute share collapse in the AI systems bag.  
- Ex. 99.1: **>$60B** new Q4 orders; record backlog into FY27.  
- 10-K competitors unchanged in kind: branded OEMs (Cisco, Dell, HPE, Lenovo) + ODMs (Foxconn, Quanta, Wiwynn). MD&A admits **competitive pricing to gain share** — implies SMCI still playing offense on price/volume.  
- **No independent market-share %** found in filings for GPU server / AI rack share vs HPE/Dell/ODMs; CSP in-house designs remain a medium-term structural risk (unchanged).

### Severity / mitigants

| | June 2026 | 25 Sep 2026 |
|--|-----------|-------------|
| Severity | 7/10 | **6/10** (intensity high; realized share loss unproven) |
| Mitigants | TTM advantage, DCBBS | Backlog + guide support; moat still time-limited |

### Pass / fail vs invalidation

| Trigger | Result |
|---------|--------|
| SMCI market share drops below 15% | **Not evidenced** (data gap — neither pass with proof nor fail) |
| Competitive share losses “evident in market data” (bear case) | **Not evidenced** in public share series reviewed here |

**Flag score: PASS by absence of contrary proof** — keep as elevated watch; do not invent share %.

---

## What changed vs 2026_06 risk assessment + Q3 delta

| Topic | June risk | Q3 delta (May/Jun 2026) | This audit (post FY26 report) |
|-------|-----------|-------------------------|------------------------------|
| Margin | Acute compression (11.2% FY25; Q1 path uncertain) | De-risked at ~10.1% Q3 | **Q4 17.5%** — inflection stronger than Q3 hoped; FY still ~10.8% |
| DCBBS | Pilot / execution risk | “Visible” in margins | Management + 10-K product scale; **% still missing** |
| Concentration | 4 CSPs ~60% OEM | Pipeline 6–8; NeoCloud/sovereign | **1× ≥10% customer at 28.1%** — diversify narrative incomplete |
| Competition | Rising | Elevated but TTM intact | Guide/backlog argue against acute loss |
| Legal / export | New Q3 disclosure | Monitor | **Internal investigation closed** (no senior-mgmt knowledge of diversion; FS still reliable per Independent Advisors); **gov’t inquiries ongoing** |
| Liquidity / FCF | Strong FY25 FCF | Assumed intact | **FY26 OCF −$6.8B**; cash $7.5B funded by financing (incl. mandatory convertible preferred + common issuance) — **new overhang** |
| Price | ~$50 thesis / ~$47 Q3 | STRONG BUY zone | **~$41.5** — in prior bear band despite ops beat |

Net: **operating thesis improved; risk surface rotated** toward single-customer peak, WC/FCF, and compliance overhang — not toward margin or DCBBS failure.

---

## Explicit invalidation checklist (from June thesis + Sep schedule)

Hard stops from `2026_06_investment_thesis.md` / monitoring schedule:

- [ ] **Q1 FY26 GM <9.5%** — N/A window passed; **Q4 FY26 GM 17.5%** → treat as **clear**  
- [ ] **Large CSP major defection** — **clear** (not disclosed)  
- [ ] **DCBBS pilots >20% overrun or >6-mo slip** — **clear** (no evidence)  
- [ ] **Market share <15%** — **uncleared / unknown** (no reliable public series in this audit)  
- [ ] **Concentration >65% (top-4) / >70%** — **clear** on disclosed metrics (single name 28.1%; ≥10% count down)  
- [ ] **Sep schedule: Revenue <$11B** — **clear** (Q4 $11.12B)  
- [ ] **Sep schedule: GM <9.5%** — **clear**  
- [ ] **Sep schedule: DCBBS <2% of revenue** — **unknown** (not disclosed)  
- [ ] **Major customer capex pullback in Q&A** — **not flagged** in Ex. 99.1; FY27 guide implies opposite  

**Conclusion:** Card-level invalidation **not met**. Thesis moves to **WATCH** because concentration **mitigation** (pillar 4 in June BLUF) is the wobbling leg.

---

## Recommended Luke actions (research only)

1. **Monitor (default):** Keep position thesis alive into Q1 FY27 print (guide $14.5–15.5B). Track sequential GM vs Q4’s 17.5% — mean-reversion toward low-teens would be normal; sub-10% would re-open Flag 2.  
2. **Dig deeper:**  
   - Customer One durability (contract length, GPU generation lock-in, dual-sourcing).  
   - Inventory ($12.9B) and AR ($6.1B) days — path back to positive OCF.  
   - Ask IR / next call for **DCBBS % of sales** and services attach.  
   - Government export-control inquiry status (10-K: ongoing despite clean internal review).  
3. **Consider trim (conditional):** Only if (a) next 10-Q shows Customer One ≥~30%+ with no offsetting enterprise disclosure, (b) sequential GM collapses without mix explanation, or (c) a named hyperscaler exit / share-loss evidence appears. **No trim recommended solely because price is $41** while FY26/ FY27 guide print strong — that is valuation/sentiment, not automatic invalidation.  
4. **Do not:** Treat this note as a buy/sell/size order. Hand sizing to Luke.

---

## Sep / Oct monitoring checkbox outcomes (filled)

**2026-09 earnings checklist (actuals):**

- [x] Revenue in $11.0–12.5B guide → **$11.12B**  
- [x] GM >10% → **17.5% GAAP**  
- [ ] DCBBS explicit % → **still missing**  
- [~] New CSP wins toward 6–8 → **≥10% count 4→1**; “hundreds” of enterprise adds (not CSP count)  
- [x] FY27 guide → **$65–72B** (far above old $40B+ hope)  

**Red flags:** none of the hard stops checked.  
**Green lights:** revenue mid-guide, GM ≫10.5%, FY27 guide raised aggressively; DCBBS % and CSP-count disclosure still incomplete.

---

*Prepared 25 Sep 2026 for lukepuplett/grok-bot-coord issue #8 (Charlie Munger research runner). Push target: lukepuplett/investment-analysis master.*
