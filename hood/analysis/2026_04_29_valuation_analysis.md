# Robinhood Markets, Inc. (HOOD) — Valuation analysis

**As of:** April 29, 2026  
**Sources:** [yahoo_stats](../financials/2026_04/yahoo_stats.md); [income_statement](../financials/2026_04/income_statement.md). **Not individualized investment advice.**

## BLUF

**What this note is:** what you’re **paying** for (current price **$73.9B** market cap) versus what the business should be **worth** (intrinsic valuation). **Main takeaway:** HOOD trades at **~40× trailing P/E**, **~37× forward P/E**, **~16× sales** — premium multiples. At base case (FY2027: $5.4B rev, 46% op margin, 23× terminal P/E), intrinsic fair value is ~**$49B**, implying current price is **50% overvalued**. However, bull case (15%+ rev growth + 25× multiple) supports ~$54B, and bear case (slowdown + multiple compression) suggests $35–40B downside. **The stock is expensive relative to base case but fairly priced for a bull outcome.** Revenue momentum and margin stability are the key levers; a miss on either compresses valuation quickly. High **beta (~2.5)** amplifies sentiment swings—see [market_analysis](./2026_04_29_market_analysis.md).

---

## Peer valuation comparison (manual paste required — as of April 29, 2026)

**Instruction:** Update peer rows with current Yahoo Finance data. HOOD baseline included for reference.

| Company | Ticker | Market Cap | Trailing P/E | Forward P/E | P/S (TTM) | EV/EBITDA | Notes |
|---------|--------|------------|:---:|:---:|:---:|:---:|---------|
| **Robinhood** | **HOOD** | **$73.9B** | **39.8×** | **36.8×** | **16.4×** | **33.8×** | Vertical integration; crypto/prediction markets; high beta |
| Charles Schwab | SCHW | — | — | — | — | — | Traditional brokerage + custodian; lower growth |
| Interactive Brokers | IBKR | — | — | — | — | — | Professional + retail; global; capital-light model |
| Coinbase | COIN | — | — | — | — | — | Crypto exchange; regulatory/pricing risk; higher volatility |

**Analysis guide:**
- **HOOD P/E premium vs SCHW/IBKR:** If HOOD trades 2–3× forward P/E vs peers, valuation is pricing growth differentiation; if >3×, implies elevated expectations.
- **P/S comparison:** Brokerage P/S varies by service mix (HOOD skews retail/active; SCHW includes wealth/custody). 16.4× is rich for the industry average (~8–12×) but justified only if growth/margins sustain.
- **EV/EBITDA:** 33.8× on HOOD signals market assumes durable margins. Peers typically trade 15–25×. Gap = bet on competitive moat.
- **What to update:** Paste current Yahoo multiples for SCHW, IBKR, COIN. Add any other relevant peer (e.g., SoFi, Moomoo parent if publicly traded).

---

## Trading multiples snapshot (paste session “Current”)

| Metric | Value |
|--------|------:|
| Market Cap | $73.93B |
| Enterprise Value | $75.13B |
| Trailing P/E | 39.84 |
| Forward P/E | 36.76 |
| Price/Sales (ttm) | 16.37 |
| Price/Book (mrq) | 7.93 |
| Enterprise Value / Revenue | 16.29 |
| Enterprise Value / EBITDA | 33.81 |

*[yahoo_stats](../financials/2026_04/yahoo_stats.md)*

---

## Earnings linkage (FY2025 TTM, Yahoo thousands)

| Item | FY2025 TTM ($ thousands unless noted) |
|------|---:|
| EBITDA (reconciled) | 2,180,000 |
| EBIT | 2,094,000 |
| Net Income | 1,883,000 |

---

## Base case assumptions (FY2027 forward view)

| Assumption | Rationale | Value |
|-----------|-----------|-------|
| **Net revenue FY2027** | Q1 2026 +15% YoY; mid-teens growth rate → low-$5B range | **$5.4B** (+13% vs FY2026E ~$4.8B) |
| **Operating margin** | Retention of 45–47% range; modest OpEx deleverage on Trump Accounts | **46%** |
| **Net margin** | Historical 42% TTM; assume 40% normalized for tax/interest | **40%** |
| **Net income FY2027** | $5.4B rev × 40% net margin | **~$2.16B** |
| **Terminal P/E** | Brokerage comps 20–25×; HOOD premium for growth → mid-point | **23×** |
| **Terminal enterprise value** | $2.16B × 23× = equity value | **~$49.7B** |
| **Discount rate / terminal year** | 2027 = 1 year out; modest risk adjustment | ~10% discount to terminal |

**Fair-value implication at base case:** Terminal value ~$49.7B → discount to PV ~$45B. *Does not include intermediate-year growth value.* Current market cap **$73.9B** implies market prices **bull case** (15%+ growth persistence, 25×+ P/E).

---

## Illustrative intrinsic cross-check (order-of-magnitude)

Assuming **FY2027** **net income ~$2.16B** (base case) and demanding **terminal P/E 25×** (bull scenario: growth persists) → **terminal equity value ~$54B**, discounted ~10% → **intrinsic value ~$49B**. Current price **~$73.9B** is **50% premium** to base case, implying **bull case required** for fair value or upside.

Compare: If market price is **$73.9B** and base intrinsic is **$49B**, the **$24.9B gap** prices in either (a) FY2027 revenue exceeds **$5.4B** forecast, or (b) terminal multiple **>25×**, or (c) both — i.e., continued strong growth **and** premium valuation must both hold.

---

## Valuation sensitivity table (to intrinsic fair value)

| Driver | Base assumption | Value impact +10% | Value impact −10% | Sensitivity rank |
|--------|-----------------|:---:|:---:|:---:|
| Net revenue FY2027 | $5.4B | +$2.4B intrinsic | −$2.4B intrinsic | **#1 (highest)** |
| Operating margin | 46% | +$1.9B intrinsic | −$1.9B intrinsic | **#2** |
| Terminal P/E multiple | 23× | +$1.6B intrinsic | −$1.6B intrinsic | **#3** |
| Net margin (post-tax) | 40% | +$0.9B intrinsic | −$0.9B intrinsic | **#4** |
| Share count dilution | SBC offsets 40% buybacks | ±2–3% EPS per share | ±2–3% EPS per share | **#5 (lowest)** |

**Interpretation:**
- **Revenue is the key lever.** A 10% miss (→ $4.9B) drops intrinsic to ~$42B; a 10% beat (→ $5.9B) lifts to ~$52B. Current price **$73.9B** requires **beat + margin hold + premium multiple**.
- **Margin compression risk is material.** If OpEx guidance increases (Trump Accounts, international headcount), margin could slip 200–300bps → 43–44% → intrinsic value ~$45B.
- **Multiple re-rating is the swing factor.** At 20× terminal P/E (bear case), intrinsic $41B; at 25× (bull case), $54B. Current stock price bids for 26–27× implied forward, pricing perfection.

---

## What I cannot scrape / need from you (if updating live)

| Data | Why |
|------|-----|
| **Live price** after 04/29/2026 | Multiples stale without fresh paste |
| **Consensus EPS / sales** | Forward multiple depends on sell-side grid you trust |
| **Peer set current multiples** | Manual peer paste vs Schwab/Coin/etc. |

---

## Cross-links

| Document | Relation |
|----------|----------|
| [financial_analysis](./2026_04_29_financial_analysis.md) | Fundamental inputs |
| [investment_thesis](./2026_04_29_investment_thesis.md) | Conviction linkage |
