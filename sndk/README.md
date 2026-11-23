# Sandisk (SNDK) — first-pass coverage

**Status:** watchlist, new coverage started 23 Nov 2026. Not held. First pass from the FY2026 Form 10-K and the latest Form 10-Q only. The seven required analysis documents, the revenue-driver section and a monitoring schedule are **not written yet** (see "Still to do"). Nothing here is a recommendation. Sister page: [../mu/README.md](../mu/README.md) (Micron).

**Sources** (all in [quarterly/](quarterly/), made by `scripts/edgar_snapshot.py`):
- Form 10-Q for the quarter ended 2 Oct 2026 (first quarter of FY2027), filed 30 Oct 2026, accession 0001628280-26-068601: [2027_Q1_10q.htm](quarterly/2027_Q1_10q.htm), with facts and ratio inputs
- Form 10-K for the year ended 3 Jul 2026, filed 17 Aug 2026, accession 0001628280-26-057406: [2026_FY_10k.htm](quarterly/2026_FY_10k.htm), with facts and ratio inputs

Prices are Yahoo closes on 23 Nov 2026.

## Data warning: 8-for-1 stock split on 20 Nov 2026

The 10-Q says holders of record on 9 Nov receive seven additional shares per share, issued after the close on 19 Nov. Yahoo prices are split-adjusted ($95) but the filing's share counts are not (142m on the cover at 26 Oct). Multiplying them directly gives a market cap 8 times too small and a nonsensical P/E of 0.7. The figures below scale the share counts by 8. `scripts/edgar_snapshot.py` previously had this bug and now adjusts for splits after the filing; no other ticker used so far has had a recent split.

## BLUF

**BLUF: Sandisk went from losses to $12.4bn of operating profit in one year, and the latest quarter is larger still (revenue $11.0bn, gross margin 85%, net income $8.1bn), yet the stock, about $95 after the 8-for-1 split, is down roughly two-thirds from its June high and trades at about 6 times trailing earnings and about 3.3 to 3.6 times the latest quarter annualised. The market is pricing a sharp fall in earnings, or a doubt that this level lasts. Revenue rose about 4.8x in four quarters while capex stayed near $50m a quarter, so the gain looks like price, not volume, in a business where the same 10-K shows two loss-making years before it. I have not yet researched why the shares have fallen. No view on a trade.**

## Key metrics ($ billions; fiscal years end around 1 Jul)

| Metric | FY2024 | FY2025 | FY2026 | FQ1 FY27 (qtr to 2 Oct 2026) | Trend |
|---|---:|---:|---:|---:|---|
| Revenue | 6.7 | 7.4 | **20.2** | **11.0** | ↗ |
| Gross profit | 1.1 | 2.2 | 14.5 | 9.4 | ↗ |
| Gross margin | 16.1% | 30.1% | 71.5% | **85.0%** | ↗ ⚠️ |
| Operating income | –0.5 | –1.4 | **12.4** | **8.8** | ↗ |
| Operating margin | –7.0% | –18.7% | 61.2% | 79.6% | ↗ ⚠️ |
| Net income | –0.7 | –1.6 | **11.4** | **8.1** | ↗ |
| Operating cash flow | –0.3 | 0.1 | 11.7 | 6.4 | ↗ |
| Capex | 0.17 | 0.20 | 0.18 | 0.05 | → |

*FY figures from the 10-K facts, FQ1 FY27 from the 10-Q. ⚠️ = far above this company's own history in the table.*

## The last five quarters ($ billions)

| Quarter ended | Revenue | Gross margin | Operating income | Net income |
|---|---:|---:|---:|---:|
| 3 Oct 2025 | 2.31 | 29.8% | 0.18 | 0.11 |
| 2 Jan 2026 | 3.02 | 50.9% | 1.06 | 0.80 |
| 3 Apr 2026 | 5.95 | 78.4% | 4.11 | 3.62 |
| 3 Jul 2026 (derived: year less nine months) | 8.97 | 84.5% | 7.04 | 6.90 |
| 2 Oct 2026 | 11.03 | 85.0% | 8.78 | 8.10 |

*The July quarter is not reported separately in the filings; it is the 10-K year less the first three quarters. Revenue grew in every quarter, but the rise slowed (+31%, +97%, +51%, +23%). That is arithmetic on the table, not a forecast.*

## Balance sheet and capital return (2 Oct 2026)

| Item | $bn |
|---|---:|
| Cash and equivalents | 5.1 (4.8 at 3 Jul) |
| Inventory | 3.0 (2.7 at 3 Jul) |
| Stockholders' equity | 18.1 (15.7 at 3 Jul, 9.2 at 27 Jun 2025) |
| Share repurchases, FQ1 FY27 | **5.0** (none in the same quarter a year earlier) |
| Debt | none outstanding: the $2.0bn term loan B was repaid in full with cash on 4 Mar 2026; the $1.5bn revolver is undrawn |
| Operating lease liability | 0.2 |

## Valuation snapshot (23 Nov 2026, split-adjusted)

| | |
|---|---|
| Price | about $95.23 |
| Shares (after the 8:1 split) | about 1,138m (cover page) to 1,232m (diluted) |
| Market cap | $108bn to $117bn |
| Net cash (cash $5.1bn, no debt) and enterprise value | about $5bn; EV about $103bn to $112bn |
| Trailing (to 2 Oct 2026) revenue / net income | $29.0bn / $19.4bn |
| P/E (trailing) | 5.6x to 6.0x |
| P/S (trailing) | 3.7x to 4.1x |
| P/E on the latest quarter annualised (x4, $32.4bn) | about 3.3x to 3.6x (arithmetic, not a forecast) |
| 52-week closing range | $24.30 (3 Dec 2025) to $291.88 (25 Jun 2026) |
| Recent moves | about –6% 1 week, –39% 1 month, –49% 3 months, +220% year to date |
| Off the 52-week high | about –67% |

## Debt and obligations check (10-Q for the quarter to 2 Oct 2026)

| Check | Finding | Source |
|---|---|---|
| Instruments | No borrowings outstanding. The $2.0bn term loan B was settled in full on 4 Mar 2026 using cash on hand, with a loss on early extinguishment from writing off issuance costs. | 10-Q debt note |
| Maturity ladder | Not applicable; the revolver's maturity was extended from 21 Feb 2030 to 9 Sep 2031 (Amendment No. 1, 9 Sep 2026). | 10-Q debt note |
| Leases | Operating lease liability $201m ($23m current), discount rate 7.4%, undiscounted payments $297m. No finance leases found in the tags (not checked in the text). | Lease note |
| Converts | None found. | Facts and text search |
| Funding access | $1.5bn revolving credit facility, undrawn, subject to a maximum leverage ratio covenant. Share repurchase programmes: $6.0bn (announced 30 Apr 2026) plus $14.0bn (5 Aug 2026), $20bn in all; $5.0bn was spent in the first quarter of FY27. | 10-Q debt and equity notes |
| Coverage, the hard way | Interest expense $2m in the quarter against operating income $8.78bn. | Income statement |
| Off balance sheet | Purchase obligations $6.8bn as tagged: $1.4bn in the rest of FY27, then $2.0bn, $2.3bn and $1.0bn in the next three years, and under $0.1bn after. Counterparty not yet identified. | Purchase obligation facts |

*The check closed the "debt not extracted" gap on this page. The buyback authorisations are large relative to the roughly $108bn to $117bn market cap, and the 5.0bn spent in one quarter was funded from cash flow, not debt.*

## Still to do (required by AGENTS.md)

- [ ] The seven analysis documents (financial, market, competitive, technical, risk, thesis, valuation) in `analysis/`, plus the five-table framework
- [ ] Why the shares have fallen so far since June (not researched yet), and what the market may be pricing
- [ ] Who the purchase obligations are owed to, and the relationship with its manufacturing partner (not extracted yet)
- [ ] Revenue breakdown and growth drivers: NAND pricing, data-centre mix, customers
- [ ] Supply additions at rivals (Micron, Samsung, SK Hynix, Kioxia) and the supply/demand balance
- [ ] Next earnings date and a monitoring schedule (date not checked)
