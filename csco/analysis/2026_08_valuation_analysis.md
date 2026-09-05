# CSCO — Valuation Analysis (FY2026 Q4 / Post-Earnings)

**Date:** 2026-08-13 (day after Q4 FY2026 earnings; stock -8.4% to $113.47)
**Sources:** [financials/2026_08/yahoo_stats.md](../financials/2026_08/yahoo_stats.md), [2026_08_financial_analysis.md](2026_08_financial_analysis.md), [2026_Q4_press_release.htm](../quarterly/2026_Q4_press_release.htm)

## Executive Summary

**BLUF: Cisco trades at 40.9x trailing GAAP earnings and roughly 22–26x forward earnings (depending on whether you use management's own FY2027 non-GAAP EPS guide or Yahoo's blended consensus estimate) after an 8.4% single-day decline on results that beat guidance — the drop reads as a valuation reset (multiple was ~33x trailing the prior quarter, now 41x) rather than a fundamentals miss. At $113.47, the stock is pricing in continued execution on the $7.5B AI infrastructure revenue guide and sustained "core" (ex-AI) growth near 10% — both plausible given the order backlog, but leaving limited room for error given how far the multiple has re-rated over the past year (Market Cap roughly doubled from $228.6B a year ago to $483.1B). Recommend: this is a "pay up for a real growth inflection" valuation, not a value entry point — position sizing should reflect that the risk/reward is asymmetric toward disappointment at these levels.**

---

## 1. Current Valuation Snapshot

| Metric | Value | Context |
|--------|-------|---------|
| Share Price | $113.47 | -8.4% on 8/13/2026 (day after Q4 earnings) |
| Market Cap | $483.10B | Up from $228.61B a year ago (+111%) — reflects both price appreciation and multiple expansion |
| Trailing P/E | 40.86x | Up from 25.32x a year ago |
| Forward P/E (Yahoo consensus) | 25.77x | Implies ~$4.40 NTM EPS — below management's own FY2027 non-GAAP guide midpoint ($5.08); likely blends GAAP/non-GAAP or uses a more conservative consensus estimate — **flagged as a data reconciliation item, not resolved here** |
| Forward P/E (company guide basis) | ~22.3x | $113.47 / $5.08 (FY2027 non-GAAP EPS guide midpoint) — the more directly comparable figure given we have management's own guidance |
| EV/EBITDA | 27.54x | Up from 16.61x a year ago |
| Price/Sales | 8.04x | Up from 4.29x a year ago |
| PEG (5yr expected) | 1.21 | Below 1.5–2.0x "fair value" heuristic, suggesting growth-adjusted multiple is less stretched than the headline P/E implies |

**The multiple has expanded faster than the business.** Over the trailing year, EV/Revenue went from 4.48x to 8.19x and EV/EBITDA from 16.61x to 27.54x — roughly a **65–83% multiple re-rating** — while FY2026 revenue grew 12% and non-GAAP EPS grew 14%. This confirms the market has already priced in a meaningful re-rating of Cisco's growth durability, not just the FY2026 results themselves.

## 2. Valuation Trend (Quarterly, per Yahoo)

| Metric | Current (8/13/26) | 4/30/2026 | 1/31/2026 | 10/31/2025 | 7/31/2025 | 4/30/2025 | Trend |
|--------|--------------------|-----------|-----------|------------|-----------|-----------|-------|
| Market Cap | $483.10B | $360.51B | $309.29B | $287.91B | $269.60B | $228.61B | ↗ Steady re-rating, accelerating |
| Trailing P/E | 40.86 | 32.91 | 30.24 | 28.67 | 27.79 | 25.32 | ↗ +61% over 5 quarters |
| EV/EBITDA | 27.54 | 18.87 | 19.64 | 19.34 | 18.71 | 16.61 | ↗ +66% over 5 quarters |

The re-rating has been gradual and consistent quarter-over-quarter — not a single earnings-driven spike — suggesting the market has been progressively pricing in the AI infrastructure story since well before this quarter's print, and the post-earnings 8.4% drop is a partial unwind of that, not a reversal.

## 3. Peer Comparison — Data Gap

This repository does not yet contain financial data for direct comparables (Arista Networks, Juniper/HPE, Palo Alto Networks, Nvidia/Broadcom for the AI-networking-silicon comparison). A standalone Price/Sales of 8.0x and EV/EBITDA of 27.5x should be benchmarked against networking-hardware peers (historically lower multiples, often 4–8x EV/EBITDA for Arista-like growth networking names) and AI-infrastructure peers (often higher) before drawing firm conclusions on relative value. **Recommend adding lightweight peer valuation snapshots** (at minimum Arista Networks, given closest business-model overlap) in a future update.

## 4. Valuation Sensitivity Table

| Driver | Base Assumption | +10% Impact | -10% Impact | Valuation Delta |
|--------|-------------------|-------------|--------------|-------------------|
| FY2027 Non-GAAP EPS (company guide midpoint $5.08) | $5.08 | $5.59 | $4.57 | At a constant ~22.3x forward multiple: **~$125 (+10%) / ~$102 (-10%)** — direct 1:1 sensitivity, largest single lever |
| Forward P/E multiple (base ~22.3x on guide basis) | 22.3x | 24.5x | 20.1x | At constant $5.08 EPS: **~$125 (+10%) / ~$102 (-10%)** — multiple compression to "high-quality hardware" peer levels (~18–20x) would imply high-single-digit downside from here even with no EPS miss |
| AI infrastructure revenue (FY2027 guide $7.5B, ~10% of total) | $7.5B | $8.25B | $6.75B | Modest direct EPS impact (~+/-$0.05–0.10, given high incremental margin per management commentary) but **outsized sentiment/multiple impact** given this is the number the market is most focused on — a miss here likely triggers multiple compression beyond the direct EPS effect |
| "Core" (ex-AI) revenue growth (management's own ~10% estimate for FY2027) | ~10% | ~11% | ~9% | Largest revenue-dollar sensitivity given ~90% of revenue base; a reversion toward the pre-cycle long-term algorithm (4–6%) rather than just -1pt would be the real bear-case trigger — see [market analysis](2026_08_market_analysis.md) bear scenario |
| Non-GAAP gross margin (FY2027 guide 65–66%, vs. 66.3% Q4 FY26 exit) | 65.5% | 66.5%+ (less compression than guided) | 64.5% (worse than low end of guide) | Direct opex-neutral flow-through to operating margin/EPS of roughly the same magnitude as the margin change itself — a full point of gross margin is worth several percentage points of non-GAAP net income |

**Ranked by absolute valuation impact:** (1) forward P/E multiple re-rating risk (both directions), (2) core ex-AI revenue growth durability, (3) FY2027 EPS delivery against guide, (4) AI infrastructure revenue (smaller direct $ impact, larger sentiment impact), (5) gross margin trajectory.

## 5. DCF Sketch (Directional Only — Not a Formal Model)

Given the AI infrastructure business is guided to grow from ~$4B to $7.5B in one year (+88%) before likely decelerating toward more normal networking-hardware growth rates in later years, and "core" business growth (~10% per management) is itself elevated versus Cisco's pre-cycle long-term algorithm of 4–6%, a formal multi-year DCF is highly sensitive to the terminal decay assumption for both segments. Directionally:
- A base case blending a 2–3 year AI/core growth premium tapering to Cisco's historical 4–6% long-term algorithm by FY2030, at a WACC in the 8–9% range (large-cap tech, investment-grade balance sheet) and a terminal growth rate of 3–3.5%, would need to validate against the current ~$483B enterprise value.
- **This document does not build the full multi-year cash flow model** — flagged as a follow-up task once peer data and a longer post-10-K financial history are available in the repo (a single fiscal year of data is a thin base for terminal-value-sensitive DCF work).

## 6. Recommendation Framing

The valuation is **not** obviously cheap or obviously overvalued in isolation — the PEG ratio (1.21) suggests growth-adjusted pricing is reasonable *if* the ~15% FY2027 revenue growth guide is delivered. The risk is asymmetric: delivering the guide roughly justifies the current price, while any miss (AI revenue, core growth, or margin) likely triggers both an earnings cut *and* multiple compression simultaneously, as happened directionally on 8/13/2026 despite an actual beat. This is the central tension for the [investment thesis](2026_08_investment_thesis.md).

---

*Abbreviations: NTM = Next Twelve Months, WACC = Weighted Average Cost of Capital, PEG = Price/Earnings-to-Growth ratio.*

**Related documents:** [Financial Analysis](2026_08_financial_analysis.md) | [Risk Assessment](2026_08_risk_assessment.md) | [Investment Thesis](2026_08_investment_thesis.md)
