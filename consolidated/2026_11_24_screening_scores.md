# Screening scores: profitability, growth and distance from the 52-week high (data to the 23 Nov 2026 close)

**Status:** a working screen, not a recommendation. It scores three measures I could compute from filings and prices. **Guidance and outlook are not scored**: they need each company's latest results release and call, which I have not read. A high score here means "profitable, growing and well off its high", not "cheap" or "will recover". I have not researched why any of these stocks fell.

Related: [value scoring of Micron, SanDisk, Moderna and Lilly](2026_11_23_value_scoring_mu_sndk_mrna_lly.md) (a different, eight-row rubric). The valuation snapshot these names come from is in the diary entry "Valuation snapshot: a selection of stocks (close Fri 20 Nov 2026)" in [../diary/2026-11.md](../diary/2026-11.md).

## The scale

Each measure runs from **–5** to **+5**. The average is unweighted.

| Measure | How it is computed | Bands |
|---|---|---|
| Profitability | Operating margin on trailing twelve months (net margin where there is no operating income) | 40% or more +5; 30–40% +4; 20–30% +3; 12–20% +2; 5–12% +1; 0–5% 0; –10–0% –2; –25 to –10% –3; below –25% –5 |
| Growth | Revenue in the latest reported quarter against the same quarter a year earlier | 80% or more +5; 40–80% +4; 25–40% +3; 15–25% +2; 8–15% +1; 0–8% 0; negative –2 |
| Off highs | Latest close against the highest close in the past year; a **bigger fall scores higher** | More than 55% below +5; 45–55% +4; 35–45% +3; 25–35% +2; 15–25% +1; 5–15% –1; within 5% –3 |

## Scores (sorted by average)

| Ticker | Latest quarter | Op margin (net) | Growth | Off high | Profit | Growth | Off high | Avg |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| AVGO | 2 Aug 2026 | 48% (43%) | +86% | –36% | +5 | +5 | +3 | **+4.3** |
| NVDA | 26 Jul 2026 | 65% (64%) | +106% | –31% | +5 | +5 | +2 | **+4.0** |
| KLIC | 4 Jul 2026 | 13% (12%) | +123% | –54% | +2 | +5 | +4 | +3.7 |
| SMCI | 30 Sep 2026 | 9% (7%) | +298% | –51% | +1 | +5 | +4 | +3.3 |
| AMAT | 26 Jul 2026 | 30% (30%) | +25% | –53% | +3 | +2 | +4 | +3.0 |
| GLW | 30 Sep 2026 | 16% (12%) | +18% | –57% | +2 | +2 | +5 | +3.0 |
| HOOD | 30 Sep 2026 | n/a (39%) | +12% | –51% | +4 | +1 | +4 | +3.0 |
| CRWV | 30 Sep 2026 | –1% (–26%) | +168% | –66% | –2 | +5 | +5 | +2.7 |
| GOOG | 30 Sep 2026 | 33% (50%) | +25% | –30% | +4 | +2 | +2 | +2.7 |
| CAT | 30 Sep 2026 | 18% (15%) | +17% | –49% | +2 | +2 | +4 | +2.7 |
| DELL | 31 Jul 2026 | 9% (8%) | +58% | –43% | +1 | +4 | +3 | +2.7 |
| CSCO | 24 Oct 2026 | 26% (22%) | +24% | –26% | +3 | +2 | +2 | +2.3 |
| DDOG | 30 Sep 2026 | 2% (6%) | +35% | –43% | 0 | +3 | +3 | +2.0 |
| INTC | 26 Sep 2026 | 3% (–20%) | +21% | –59% | –1 | +2 | +5 | +2.0 |
| MSFT | 30 Sep 2026 | 47% (41%) | +19% | –11% | +5 | +2 | –1 | +2.0 |
| HPE | 31 Jul 2026 | 6% (7%) | +34% | –35% | +1 | +3 | +2 | +2.0 |
| ENR.DE | FY to 30 Sep 2026 | 12.4% before special items | +15.5% (year) | –33% | +2 | +2 | +2 | +2.0 |
| TT | 30 Sep 2026 | 18% (14%) | +18% | –19% | +2 | +2 | +1 | +1.7 |
| PH | 30 Sep 2026 | 24% (17%) | +18% | –15% | +3 | +2 | –1 | +1.3 |
| RKLB | 30 Sep 2026 | –28% (–26%) | +73% | –67% | –5 | +4 | +5 | +1.3 |
| NEE | 31 Mar 2026 | 32% (32%) | +2% | –14% | +4 | 0 | –1 | +1.0 |
| AAPL | 27 Jun 2026 | 33% (28%) | +16% | –2% | +4 | +2 | –3 | +1.0 |
| AMZN | 30 Sep 2026 | 13% (17%) | +12% | –9% | +2 | +1 | –1 | +0.7 |
| GTLB | 31 Jul 2026 | –9% (–5%) | +21% | –23% | –2 | +2 | +1 | +0.3 |
| NET | 30 Sep 2026 | –14% (–9%) | +39% | –20% | –3 | +3 | +1 | +0.3 |
| DUK | 31 Mar 2026 | 28% (16%) | +9% | –3% | +3 | +1 | –3 | +0.3 |
| TSLA | 30 Sep 2026 | 3% (3%) | 0% | –21% | 0 | –2 | +1 | –0.3 |

*Computed with the helpers in `scripts/edgar_snapshot.py` from SEC `companyfacts` and Yahoo closes, except ENR.DE, whose figures are from [../enr.de/analysis/2026_11_delta_analysis.md](../enr.de/analysis/2026_11_delta_analysis.md). Caterpillar is from its Q3 10-Q in [../cat/quarterly/](../cat/quarterly/).*

**Not scored:** ASML (20-F, annual only, in euros; 31% below its high), DroneShield (77% below its high; A$ and ASX, no financials pulled), Rolls-Royce (18% below its high; sterling, half-yearly), and Virgin Galactic (revenue too small for the ratios to mean anything).

## Caveats

- **Stale quarters.** Several names' latest quarter is a quarter behind: AAPL (to June), AVGO, NVDA, AMAT, DELL, HPE, KLIC and GTLB (to July or August). Duke and NextEra show the quarter to 31 Mar 2026; I do not know why later quarters were missing from the data and have not checked. The price distance is current.
- **Judgment calls.** INTC's profit score is –1, not the band's 0, because it had a 20% net loss. HOOD's profit score uses net margin because it reports no operating income. ENR.DE's margin is before special items and its growth is annual, so it is not like for like.
- **Utilities and financials.** Margin means less for Duke, NextEra, Robinhood and Caterpillar's finance arm, which carry or lend large amounts of debt; the repo's debt and obligations check matters more for them.
- **Net above operating.** GOOG's and HPE's net income is above or near operating income because of non-operating items; I have not checked what they are.
- **Beaten up is not mispriced.** Several high scorers are still up a lot over twelve months (DELL +165%, HPE +128%, INTC +62%).

## What it would take to finish

Pull each company's latest results release and score guidance and outlook, refresh the stale quarters, and run the debt and obligations check on the utilities and Dell.
