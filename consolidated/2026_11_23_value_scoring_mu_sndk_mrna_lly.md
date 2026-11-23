# Value scoring: Micron, SanDisk, Moderna, Eli Lilly (23 Nov 2026)

**Status:** a working comparison, not a recommendation. None of these four is a chosen trade. The scores are my judgments from the filings and prices gathered on 23 Nov 2026, not measurements, and one point either way on any row is inside the noise. Any trade needs the firm's pre-clearance first.

Related: [mu/README.md](../mu/README.md), [sndk/README.md](../sndk/README.md), [mrna/README.md](../mrna/README.md) with its [debt check](../mrna/analysis/2026_11_23_debt_and_obligations_check.md) and [projection](../mrna/model/README.md). Eli Lilly (LLY) has no folder in the repo yet.

## The scale

Each row runs from **–5** (very unfavourable for someone buying today) through **0** (neutral or unknown) to **+5** (very favourable). The overall figure is an **unweighted average**; it treats all rows as equally important, which the reader should not. It scores *price against evidence*, not business quality: a high-quality business can score low because its price already assumes the quality.

| Row | What it asks |
|---|---|
| 1. Valuation on trailing earnings | P/E, P/S and enterprise value to operating income at the current price |
| 2. Valuation stress test | One test per company type: **Micron, SanDisk:** the P/E if margins fell back to an earlier level. **Moderna:** the revenue needed at break-even. **Lilly:** the earnings growth needed to bring a 45x P/E to 20x in five years |
| 3. Balance sheet and obligations | Result of the debt and obligations check: debt, maturities, leases, converts, undrawn credit, off-balance-sheet commitments, against cash and cash flow |
| 4. Cash conversion | Free cash flow against profit; capex intensity |
| 5. Earnings momentum | Direction and pace of revenue and profit |
| 6. Peak-cycle or event risk | **Micron, SanDisk:** how much of the gain is price, not volume. **Moderna:** pipeline and regulatory events, and how far the price has run. **Lilly:** pipeline, pricing policy and price near the all-time high |
| 7. Capital return and dilution | Buybacks and dividends, or new debt and shares issued |
| 8. Gaps in our evidence | How much of the analysis is still missing |

## Scores

| Row | Micron | SanDisk | Moderna | Lilly |
|---|---:|---:|---:|---:|
| 1. Trailing valuation | +3 | +4 | –4 | –3 |
| 2. Stress test | –1 | –2 | –4 | –2 |
| 3. Balance sheet and obligations | +5 | +4 | +1 | +1 |
| 4. Cash conversion | +2 | +4 | –3 | +4 |
| 5. Earnings momentum | 0 | +1 | +2 | +3 |
| 6. Peak-cycle or event risk | –4 | –5 | –4 | –2 |
| 7. Capital return and dilution | +1 | +3 | –2 | +2 |
| 8. Gaps in our evidence | –1 | –2 | –1 | –2 |
| **Unweighted average** | **+0.6** | **+0.9** | **–1.9** | **+0.1** |

## The reasoning

**Micron (FY2026 10-K, 3 Sep 2026).** P/E 9.4–9.5x at $705.50, P/S about 6.0x, enterprise value about 7.4x operating income. Net cash about $68bn, notes of $2.8bn with nothing due for five years, undrawn $2.0bn revolver, no converts, $10.8bn of purchase obligations. Capex is 23% of revenue and free cash flow $59bn. Cost of goods rose 14% while revenue rose 256%, so the gain is price. If the operating margin fell to its FY25 level (26%) on the same revenue, the P/E would be about 27x. No quarterly data yet (momentum unknown).

**SanDisk (10-Q to 2 Oct 2026).** P/E 5.3–5.7x, or about 3.2–3.4x on the latest quarter annualised, at $90.49 after the 8-for-1 split of 20 Nov. No debt (the $2.0bn term loan was repaid on 4 Mar 2026), $1.5bn revolver undrawn, $6.8bn of purchase obligations, buyback programmes of $20bn with $5.0bn spent in a quarter. Revenue growth is slowing (+97%, +51%, +23%). NAND-only, and it lost money in FY24 and FY25; at its October 2025 margin the P/E on today's run-rate revenue would be about 35–38x.

**Moderna (10-Q to 30 Sep 2026).** P/E not meaningful, P/S 34–36x. Q3 was a seasonal profit (+$162m, the first meaningful one in at least two years) but nine months show a $2.0bn loss and operating cash flow of –$2.7bn. Cash and investments $8.0bn against $3.6bn of debt (a $600m secured term loan due 2030 and $3.0bn of 0% converts due 2032 with a conversion price about equal to the stock price). Break-even needs about $5.6bn of revenue against about $2.3bn guided, and management's 2028 cash break-even target is not reached in any of three scenarios in the [projection](../mrna/model/README.md). Up 614% this year (about sevenfold); overall-survival data and the regulatory path are open.

**Eli Lilly (10-Q to 30 Sep 2026).** P/E 44.5–46.9x, P/S 14.2–15.0x at $1,374.54, about 5% below its all-time high. Revenue +39% in Q3 (slowing from about +51% in the first half), gross margin 84%, operating cash flow 131% of net income, free cash flow about $19bn in nine months. Debt $49.5bn, up $7.0bn this year to fund acquisitions (Ventyx, Orna, Ajax, Centessa, Kelonia, Curevo, AtaiBeckley, and Merida in October for up to $2.9bn), against $4.9bn of cash and $10.1bn of undrawn credit. Dividends and buybacks took about 43% of net income. To bring about 45x to 20x in five years needs earnings growth of about 17–19% a year.

### Lilly: debt and obligations check (partial)

| Check | Finding |
|---|---|
| Instruments | Total debt $49.5bn; notes 2028–2066 at 4.15%–5.70%, including $1.3bn floating (SOFR + 0.35% / 0.46%); $9.0bn issued in May 2026; commercial paper programme |
| Funding access | $10.1bn unused committed credit ($6.0bn 364-day, renewed; $4.0bn multi-year to Aug 2031); $10.0bn supports the commercial paper |
| Converts | None found |
| Coverage | Pre-tax income $26.5bn for nine months; interest expense not extracted |
| **Not extracted** | Leases, purchase obligations, covenant terms, interest expense (10-Q has no lease note; use the 10-K) |

## How to read this

- **The top three are within noise.** SanDisk +0.9, Micron +0.6 and Lilly +0.1 differ by less than any single row's uncertainty.
- **The rubric favours profitable names.** Four rows rest on earnings; Moderna has none yet, and rows 2 and 6 use different tests for it. It is not like for like.
- **Different risks.** Memory: whether prices hold. Lilly: paying a high price for slowing growth. Moderna: pipeline outcomes.
- **What would move the scores:** the reasons for the 20–23 Nov swings in memory stocks (Micron –13.9% then +18.7%; SanDisk –16.1% then +14.2%), quarterly Micron data, Lilly's 10-K, and the oncology timeline.

## Data as of

Prices are Yahoo closes on 23 Nov 2026. Filings: Micron 10-K filed 9 Oct 2026; SanDisk 10-Q filed 30 Oct 2026; Moderna 10-Q filed 6 Nov 2026; Lilly 10-Q filed 29 Oct 2026. Ratios from `scripts/edgar_snapshot.py`, with share counts scaled for the SanDisk split.
