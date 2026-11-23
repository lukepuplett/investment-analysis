# Micron Technology (MU) — first-pass coverage

**Status:** watchlist, new coverage started 23 Nov 2026. Not held. First pass from the FY2026 Form 10-K only; the seven required analysis documents, the revenue-driver section and a monitoring schedule are **not written yet** (see "Still to do"). Nothing here is a recommendation.

**Source:** Form 10-K for the fiscal year ended 3 Sep 2026, filed 9 Oct 2026, accession 0000723125-26-000023, saved as [quarterly/2026_FY_10k.htm](quarterly/2026_FY_10k.htm) with [facts](quarterly/2026_FY_10k_facts.tsv) and [ratio inputs](quarterly/2026_FY_10k_ratio_inputs.json) (made by `scripts/edgar_snapshot.py`). Prices are Yahoo closes on 23 Nov 2026.

## BLUF

**BLUF: Micron's FY2026 was extraordinary: revenue $133.2bn (+256%), operating margin 75%, net income $85.0bn, and the stock ($713.57) trades at about 9.5x trailing earnings and 6.1x sales after falling 41% from its June high. That low multiple sits on what looks like peak-cycle earnings: cost of goods rose 14% while revenue rose 256%, so the jump is price, not volume, and the company's own 10-K says memory prices have swung from +200% to −50% over past cycles. A low trailing P/E for a memory maker at record margins is not the same as cheap; the open question is how long prices hold. No view on a trade.**

## Key metrics (fiscal years end late Aug / early Sep; $ billions)

| Metric | FY2024 | FY2025 | FY2026 | Trend |
|---|---:|---:|---:|---|
| Revenue | 25.1 | 37.4 | **133.2** | ↗ +49%, then +256% |
| Cost of goods sold | 19.5 | 22.5 | 25.7 | → +14% in FY26 on 3.6x revenue |
| Gross profit | 5.6 | 14.9 | **107.5** | ↗ |
| Gross margin | 22.4% | 39.8% | **80.7%** | ↗ ⚠️ |
| R&D | 3.4 | 3.8 | 5.7 | ↗ |
| SG&A | 1.1 | 1.2 | 1.9 | ↗ |
| Operating income | 1.3 | 9.8 | **99.3** | ↗ |
| Operating margin | 5.2% | 26.1% | **74.6%** | ↗ ⚠️ |
| Net income | 0.8 | 8.5 | **85.0** | ↗ |
| Operating cash flow | 8.5 | 17.5 | 89.7 | ↗ |
| Capex | 8.4 | 15.9 | 30.7 | ↗ (23% of revenue) |
| Free cash flow (OCF − capex) | 0.1 | 1.7 | **59.0** | ↗ |

*Computed from the 10-K facts file. FY2023 is not in this filing. ⚠️ = unusually high versus Micron's own history in this table; margins this high have not been shown to persist.*

## Balance sheet at 3 Sep 2026

| Item | $bn |
|---|---:|
| Cash and equivalents | 38.4 (9.6 a year earlier) |
| Debt (long-term 2.8 + current 0.5) | 3.3 |
| Net cash (cash less that debt; short-term investments not counted) | about 35 |
| Inventory | 10.4 (8.4 a year earlier) |
| Stockholders' equity | 138.4 (54.2 a year earlier) |
| Share buybacks / dividends paid, FY26 | 0.65 / 0.61 |

## Valuation snapshot (23 Nov 2026)

| | |
|---|---|
| Price | $713.57 |
| Market cap | $807bn (cover-page shares, 1,131m) to $816bn (diluted, 1,143m) |
| P/E (trailing, FY2026) | 9.5–9.6x |
| P/S | 6.1x |
| Enterprise value / operating income | about 7.8x (market cap less about $35bn net cash, on $99.3bn) |
| 52-week range | $223.93 (24 Nov 2025) to $1,213.56 (25 Jun 2026) |
| Recent moves | −0.8% 1 week, −18.7% 1 month, −21.6% 3 months, +150% year to date |
| Off 52-week high | −41.2% |

## Where the revenue comes from (FY2026)

| Cut | $bn | Share |
|---|---:|---:|
| **Business unit:** Cloud Memory (CMBU) | 43.1 (operating income 31.2) | 32% |
| Core Data Center (CDBU) | 37.6 (29.5) | 28% |
| Mobile and Client (MCBU) | 36.6 (29.2) | 27% |
| Automotive and Embedded (AEBU) | 15.9 (11.2) | 12% |
| **Product:** DRAM | 100.7 | 76% |
| NAND | 31.8 | 24% |
| **Geography:** United States | 91.3 | 69% |
| Taiwan / China / Hong Kong | 17.0 / 8.3 / 6.3 | |

*Segment and product splits are from the 10-K's tagged facts. Business-unit shares do not sum to exactly 100% because of rounding and small other items.*

## What the 10-K says about the cycle

- Average selling prices "have ranged from an increase of approximately 200% to a decrease of approximately 50%" in past periods.
- It also warns that prices may fall "as we and others increase supply," particularly if demand growth slows.

## Still to do (required by AGENTS.md)

- [ ] The seven analysis documents (financial, market, competitive, technical, risk, thesis, valuation) in `analysis/`, plus the five-table framework
- [ ] Revenue breakdown and growth drivers, with HBM and data-centre mechanics (this page only has tagged segment facts)
- [ ] Quarterly history for FY2026 (this 10-K has annual data only; the 10-Qs show how fast margins rose and whether they are still rising or already rolling over)
- [ ] Capex plans, supply additions at Micron and rivals (Samsung, SK Hynix, SanDisk) and the supply/demand balance
- [ ] Customer concentration and contract terms (prepayments, long-term agreements)
- [ ] Next earnings date and a monitoring schedule (the first quarter of FY2027, date not checked)
- [ ] SanDisk (SNDK) coverage, as a NAND comparison
