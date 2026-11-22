# CoreWeave (CRWV) — equity residual toy model (Q3 2026 pack, 10 Nov 2026)

*Toy model, not a production DCF and not a recommendation. Written for the Q3 2026 8-K/Ex.99.1, presentation and call. The Q3 10-Q was filed on 12 Nov 2026 (crwv/quarterly/2026_Q3_10q.htm) but this version still uses the 11 Nov proxies, so debt and lease schedules, coupons, converts and diluted shares are not yet taken from it. $ millions unless stated.*

## Punchline

**Demand printed. Whether anything reaches equity is decided by funding, replacement capex and the multiple a buyer pays, not by the outlook raise. On the hard measures the claim is tight: in the keep-building path debt + leases rise from about 66bn to 118.8bn against 4.6bn of book equity, and each 1x of EV/EBITDA moves equity by about $43 a share (toy count), so equity is a levered option on the multiple.**

- **The Q4 guide does not cover its own interest.** FY adj. OI guide ($1.275-1.375bn) less 9M actual $528m implies Q4 adj. OI of about $747-847m (mid 797); Q4 net interest is guided at $1.05-1.15bn (mid 1,100). Adj. OI minus interest in Q4 is **-303** at the midpoint; model GAAP OI is about 625, so GAAP OI / interest is **0.57x**.
- **Keep building (1A) is funded by lenders, not by operations.** FY27 cash after interest and cash capex excluding prepayments is -26.4bn (-19.5bn with net prepayments), covered by about 33.5bn of new debt-like funding against 5.0bn of undrawn DDTLs today. GAAP OI / interest is 0.90x in FY27 and 1.00x in FY28. At steady state on the exit-2028 run-rate, owner earnings after replacement capex, interest, tax and SBC are -3.9bn.
- **Harvest (2) turns cash after capex positive by design (4.4bn FY27, 5.8bn FY28 excluding prepayments), but it does not reach equity cleanly.** Against the 10-Q maturity ladder it is short by 0.9bn in FY27 and ~0bn in FY28 of scheduled principal (met from refinancing or the ATM; ATM draws 35.0m shares), prepayments unwind (net -1.5bn in FY27), its maintenance capex of 5.1bn is below steady-state fleet replacement of 10.9bn, and it gives up growth: FY28 revenue 23.0bn vs 35.9bn in 1A. Steady-state owner earnings are -0.3bn.
- **Funding stress (3)** has no parent unsecured issuance. Capex flexes down to what can be funded: FY27 pres capex 19.3bn of 38.0bn planned and FY28 9.3bn of 38.0bn. The ATM is needed in FY27 (35.0m shares, about 1.2bn at the $34 stress price) and is then exhausted; the FY28 unfunded gap is ~0bn. Toy end-2028 share count 632.1m vs 585.7m in 1A.
- Reference only: 10 Nov close $48.73 x 556.1m shares on the 10-Q cover (30 Oct 2026) = about $27.1bn (basic, not fully diluted). Debt + all leases at 30 Sep were about $66.2bn against $4.0bn of book equity.
- The residual is a function of a few assumptions that the pack does not give: **(1) useful life and residual GPU value, (2) EV/EBITDA a buyer pays, (3) cash vs presentation capex, (4) how much of the 9.2% implied interest rate is coupon versus capitalised-interest and fee effects.** See sensitivity and the closing list.

## Checks against the pack

38 of 38 arithmetic/provenance checks passed.

## Q4 2026 implied by the official guide

| Case | Q4 revenue | Q4 adj. OI | Q4 interest | Adj. OI - interest | Q4 GAAP OI (model) | GAAP OI / interest | Q4 pres capex |
|---|---:|---:|---:|---:|---:|---:|---:|
| Low end of FY guide | 4,686 | 747 | 1,050 | -303 | 575 | 0.55x | 4,900 |
| Midpoint | 4,836 | 797 | 1,100 | -303 | 625 | 0.57x | 5,900 |
| High end | 4,986 | 847 | 1,150 | -303 | 675 | 0.59x | 6,900 |

*FY less nine months: revenue 13,000-13,300 less 8,314; adj. OI 1,275-1,375 less 528; pres capex 37-39bn less 32.1bn (8.2 + 9.4 + 14.5). Low end pairs with the low end of every guide. Q4 GAAP OI = adj. OI - SBC - other adjustments (ASSUMPTION, Q3 bridge). The implied effective rate on existing debt that reproduces the Q4 interest guide is **9.2%**, against management's 7.9% weighted average cost of debt; the gap is lease interest, fees and amortisation, and lower capitalised interest as CIP falls (inference, not disclosed).*

## Scenarios (all go through to cash after interest, leases, capex)

**Where leases enter:** operating lease cost is already inside adj. EBITDA and GAAP OI, so every coverage ratio below is after lease cost. Finance-lease / OEM-financed capex is added to debt and pays interest at the new-asset rate. Operating lease liabilities are added to debt in the leverage lines. Lease additions are ASSUMPTIONS per scenario.

Q4 2026 is common to all scenarios (official guide, midpoint). Scenarios diverge from FY27. 2027 'committed backlog only' follows management: capex in line with 2026 and revenue and EBITDA grow significantly; revenue itself is an ASSUMPTION.

### 1A Keep building (committed backlog only)

*Capex basis: 2027: Call - capex 'in line with 2026' if only committed backlog (FY26 mid $38bn). 2028: ASSUMPTION flat.*

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Revenue | 4,836 | 25,630 | 35,890 |
| Exit run-rate revenue (ARR) | 20,500 | 30,760 | 41,020 |
| Adj. EBITDA | 2,998 | 15,891 | 22,252 |
| D&A | 2,213 | 10,343 | 14,420 |
| Adj. operating income | 797 | 5,595 | 7,879 |
| GAAP operating income | 625 | 4,907 | 7,191 |
| Net interest expense | 1,100 | 5,428 | 7,172 |
| Net income (toy) | -462 | -469 | 56 |
| Pres capex (placed in service) | 5,900 | 38,000 | 38,000 |
| Cash capex | 5,900 | 34,200 | 34,200 |
|   of which OEM/vendor-financed (added to debt) | 0 | 3,800 | 3,800 |
| Op. cash flow excl. net prepayments | 265 | 7,848 | 12,573 |
| Net prepayments (receipts less released to revenue) | 7,912 | 6,866 | 4,806 |
| Op. cash flow incl. prepayments | 8,177 | 14,714 | 17,379 |
| Cash after interest and capex, excl. prepayments | -5,635 | -26,352 | -21,627 |
| Cash after interest and capex, incl. prepayments | 2,277 | -19,486 | -16,821 |
| Adj. EBITDA / interest | 2.73x | 2.93x | 3.10x |
| GAAP OI / interest | 0.57x | 0.90x | 1.00x |
| Op. CF ex-prepay / (cash interest + scheduled principal) | 0.08x | 0.49x | 0.65x |

**Sources and uses** (funding identity: uses = sources + unfunded)

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Uses: cash capex | 5,900 | 34,200 | 34,200 |
| Uses: scheduled debt principal | 2,433 | 10,909 | 12,706 |
| Uses: capped calls | 0 | 0 | 0 |
| Uses total | 8,333 | 45,109 | 46,906 |
| Sources: op. cash flow (incl. net prepayments) | 8,177 | 14,714 | 17,379 |
| Sources: asset-level debt draws | 4,425 | 25,650 | 25,650 |
| Sources: parent-level raise | 0 | 4,000 | 2,000 |
| Sources: cash drawdown to floor | 0 | 745 | 1,877 |
| Sources: ATM equity | 0 | 0 | 0 |
| UNFUNDED gap | 0 | 0 | 0 |
| Surplus added to cash | 4,269 | 0 | 0 |

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Debt (recourse + non-recourse + new) | 48,865 | 71,406 | 90,150 |
| Finance lease liabilities | 649 | 649 | 649 |
| Operating lease liabilities | 18,530 | 23,868 | 28,015 |
| Debt + all leases | 68,044 | 95,923 | 118,814 |
| Book equity (toy roll-forward) | 3,723 | 3,894 | 4,590 |
| (Debt + leases) / book equity | 18.28x | 24.63x | 25.88x |
| Share count (m): 559 + SBC + ATM | 559.4 | 572.5 | 585.7 |
|   ATM shares issued in period (m) | 0.0 | 0.0 | 0.0 |
| Usable cash + securities | 8,453 | 7,708 | 5,831 |
| Deferred revenue balance | 17,914 | 24,780 | 29,586 |

**Terminal (steady state at exit-2028 run-rate 41.0bn):** EBITDA 25,432; replacement capex 20,736 (life 6y, residual 10%); interest 7,965; tax 0; SBC 640; **owner earnings -3,909**; (EBITDA - replacement) / interest 0.59x. Equity bridge: EV - debt 90,150 - finance leases 649 + usable cash 5,831 - cost to serve deferred revenue 11,243.

### 1B Keep building (optional growth, higher capex + renewals)

*Capex basis: ASSUMPTION: optional higher-capex growth case ($12bn above committed-only).*

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Revenue | 4,836 | 29,250 | 47,750 |
| Exit run-rate revenue (ARR) | 20,500 | 38,000 | 57,500 |
| Adj. EBITDA | 2,998 | 18,135 | 29,605 |
| D&A | 2,213 | 11,228 | 16,944 |
| Adj. operating income | 797 | 6,955 | 12,709 |
| GAAP operating income | 625 | 6,267 | 12,021 |
| Net interest expense | 1,100 | 5,873 | 8,419 |
| Net income (toy) | -462 | 352 | 2,887 |
| Pres capex (placed in service) | 5,900 | 50,000 | 50,000 |
| Cash capex | 5,900 | 45,000 | 45,000 |
|   of which OEM/vendor-financed (added to debt) | 0 | 5,000 | 5,000 |
| Op. cash flow excl. net prepayments | 265 | 7,469 | 15,315 |
| Net prepayments (receipts less released to revenue) | 7,912 | 9,926 | 6,948 |
| Op. cash flow incl. prepayments | 8,177 | 17,395 | 22,263 |
| Cash after interest and capex, excl. prepayments | -5,635 | -37,531 | -29,685 |
| Cash after interest and capex, incl. prepayments | 2,277 | -27,605 | -22,737 |
| Adj. EBITDA / interest | 2.73x | 3.09x | 3.52x |
| GAAP OI / interest | 0.57x | 1.07x | 1.43x |
| Op. CF ex-prepay / (cash interest + scheduled principal) | 0.08x | 0.46x | 0.68x |

**Sources and uses** (funding identity: uses = sources + unfunded)

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Uses: cash capex | 5,900 | 45,000 | 45,000 |
| Uses: scheduled debt principal | 2,433 | 10,909 | 14,804 |
| Uses: capped calls | 0 | 0 | 0 |
| Uses total | 8,333 | 55,909 | 59,804 |
| Sources: op. cash flow (incl. net prepayments) | 8,177 | 17,395 | 22,263 |
| Sources: asset-level debt draws | 4,425 | 33,750 | 33,750 |
| Sources: parent-level raise | 0 | 5,000 | 3,000 |
| Sources: cash drawdown to floor | 0 | 0 | 791 |
| Sources: ATM equity | 0 | 0 | 0 |
| UNFUNDED gap | 0 | 0 | 0 |
| Surplus added to cash | 4,269 | 236 | 0 |

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Debt (recourse + non-recourse + new) | 48,865 | 81,706 | 108,652 |
| Finance lease liabilities | 649 | 649 | 649 |
| Operating lease liabilities | 18,530 | 27,868 | 36,872 |
| Debt + all leases | 68,044 | 110,223 | 146,174 |
| Book equity (toy roll-forward) | 3,723 | 4,715 | 8,242 |
| (Debt + leases) / book equity | 18.28x | 23.38x | 17.73x |
| Share count (m): 559 + SBC + ATM | 559.4 | 572.5 | 585.7 |
|   ATM shares issued in period (m) | 0.0 | 0.0 | 0.0 |
| Usable cash + securities | 8,453 | 8,689 | 7,898 |
| Deferred revenue balance | 17,914 | 27,840 | 34,788 |

**Terminal (steady state at exit-2028 run-rate 57.5bn):** EBITDA 35,650; replacement capex 24,906 (life 6y, residual 10%); interest 9,568; tax 0; SBC 640; **owner earnings 536**; (EBITDA - replacement) / interest 1.12x. Equity bridge: EV - debt 108,652 - finance leases 649 + usable cash 7,898 - cost to serve deferred revenue 13,219.

### 2 Harvest (capex falls to maintenance)

*Capex basis: ASSUMPTION: maintenance = maintenance_pct_net_ppe x opening in-service net PPE, adds no revenue; the $9.3bn already in CIP is completed in 2027 with no further cash (ASSUMPTION) and does add revenue.*

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Revenue | 4,836 | 21,756 | 23,011 |
| Exit run-rate revenue (ARR) | 20,500 | 23,011 | 23,011 |
| Adj. EBITDA | 2,998 | 13,488 | 14,267 |
| D&A | 2,213 | 8,605 | 8,819 |
| Adj. operating income | 797 | 4,931 | 5,496 |
| GAAP operating income | 625 | 4,243 | 4,808 |
| Net interest expense | 1,100 | 3,998 | 3,263 |
| Net income (toy) | -462 | 235 | 1,262 |
| Pres capex (placed in service) | 5,900 | 5,116 | 5,698 |
| Cash capex | 5,900 | 4,605 | 5,128 |
|   of which OEM/vendor-financed (added to debt) | 0 | 512 | 570 |
| Op. cash flow excl. net prepayments | 265 | 8,977 | 10,900 |
| Net prepayments (receipts less released to revenue) | 7,912 | -1,520 | -916 |
| Op. cash flow incl. prepayments | 8,177 | 7,457 | 9,984 |
| Cash after interest and capex, excl. prepayments | -5,635 | 4,372 | 5,772 |
| Cash after interest and capex, incl. prepayments | 2,277 | 2,852 | 4,856 |
| Adj. EBITDA / interest | 2.73x | 3.37x | 4.37x |
| GAAP OI / interest | 0.57x | 1.06x | 1.47x |
| Op. CF ex-prepay / (cash interest + scheduled principal) | 0.08x | 0.61x | 1.18x |

**Sources and uses** (funding identity: uses = sources + unfunded)

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Uses: cash capex | 5,900 | 4,605 | 5,128 |
| Uses: scheduled debt principal | 2,433 | 10,909 | 6,179 |
| Uses: capped calls | 0 | 0 | 0 |
| Uses total | 8,333 | 15,514 | 11,307 |
| Sources: op. cash flow (incl. net prepayments) | 8,177 | 7,457 | 9,984 |
| Sources: asset-level debt draws | 4,425 | 0 | 0 |
| Sources: parent-level raise | 0 | 0 | 0 |
| Sources: cash drawdown to floor | 0 | 5,453 | 1,323 |
| Sources: ATM equity | 0 | 1,680 | 0 |
| UNFUNDED gap | 0 | 923 | 0 |
| Surplus added to cash | 4,269 | 0 | 0 |

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Debt (recourse + non-recourse + new) | 48,865 | 38,468 | 32,858 |
| Finance lease liabilities | 649 | 649 | 649 |
| Operating lease liabilities | 18,530 | 17,868 | 17,230 |
| Debt + all leases | 68,044 | 56,985 | 50,737 |
| Book equity (toy roll-forward) | 3,723 | 6,278 | 8,179 |
| (Debt + leases) / book equity | 18.28x | 9.08x | 6.20x |
| Share count (m): 559 + SBC + ATM | 559.4 | 607.5 | 620.7 |
|   ATM shares issued in period (m) | 0.0 | 35.0 | 0.0 |
| Usable cash + securities | 8,453 | 4,680 | 3,357 |
| Deferred revenue balance | 17,914 | 16,395 | 15,479 |

**Terminal (steady state at exit-2028 run-rate 23.0bn):** EBITDA 14,267; replacement capex 10,906 (life 6y, residual 10%); interest 3,005; tax 0; SBC 640; **owner earnings -284**; (EBITDA - replacement) / interest 1.12x. Equity bridge: EV - debt 32,858 - finance leases 649 + usable cash 3,357 - cost to serve deferred revenue 5,882.

### 3 Funding stress (no parent unsecured; capex flexes to funding)

*Capex basis: Plan = committed-only $38bn; capex is cut until funded (bisection).*

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Revenue | 4,836 | 23,111 | 26,980 |
| Exit run-rate revenue (ARR) | 20,500 | 25,721 | 28,238 |
| Adj. EBITDA | 2,998 | 14,329 | 16,727 |
| D&A | 2,213 | 8,968 | 9,758 |
| Adj. operating income | 797 | 5,409 | 7,017 |
| GAAP operating income | 625 | 4,721 | 6,329 |
| Net interest expense | 1,100 | 4,578 | 4,603 |
| Net income (toy) | -462 | 154 | 1,404 |
| Pres capex (placed in service) | 5,900 | 19,337 | 9,323 |
| Cash capex | 5,900 | 17,404 | 8,391 |
|   of which OEM/vendor-financed (added to debt) | 0 | 1,934 | 932 |
| Op. cash flow excl. net prepayments | 265 | 8,508 | 11,341 |
| Net prepayments (receipts less released to revenue) | 7,912 | 2,107 | -1,079 |
| Op. cash flow incl. prepayments | 8,177 | 10,614 | 10,262 |
| Cash after interest and capex, excl. prepayments | -5,635 | -8,896 | 2,950 |
| Cash after interest and capex, incl. prepayments | 2,277 | -6,789 | 1,871 |
| Adj. EBITDA / interest | 2.73x | 3.13x | 3.63x |
| GAAP OI / interest | 0.57x | 1.03x | 1.37x |
| Op. CF ex-prepay / (cash interest + scheduled principal) | 0.08x | 0.56x | 0.88x |

**Sources and uses** (funding identity: uses = sources + unfunded)

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Uses: cash capex | 5,900 | 17,404 | 8,391 |
| Uses: scheduled debt principal | 2,433 | 10,909 | 8,659 |
| Uses: capped calls | 0 | 0 | 0 |
| Uses total | 8,333 | 28,312 | 17,050 |
| Sources: op. cash flow (incl. net prepayments) | 8,177 | 10,614 | 10,262 |
| Sources: asset-level debt draws | 4,425 | 9,572 | 4,615 |
| Sources: parent-level raise | 0 | 1,500 | 1,000 |
| Sources: cash drawdown to floor | 0 | 5,453 | 1,172 |
| Sources: ATM equity | 0 | 1,172 | 0 |
| UNFUNDED gap | 0 | 1 | 1 |
| Surplus added to cash | 4,269 | 0 | 0 |

| $m | Q4'26 | FY27 | FY28 |
|---|---:|---:|---:|
| Debt (recourse + non-recourse + new) | 48,865 | 50,962 | 48,850 |
| Finance lease liabilities | 649 | 649 | 649 |
| Operating lease liabilities | 18,530 | 20,868 | 22,122 |
| Debt + all leases | 68,044 | 72,479 | 71,622 |
| Book equity (toy roll-forward) | 3,723 | 5,689 | 7,734 |
| (Debt + leases) / book equity | 18.28x | 12.74x | 9.26x |
| Share count (m): 559 + SBC + ATM | 559.4 | 613.2 | 632.1 |
|   ATM shares issued in period (m) | 0.0 | 35.0 | 0.0 |
| Usable cash + securities | 8,453 | 4,172 | 3,000 |
| Deferred revenue balance | 17,914 | 20,021 | 18,942 |

*Capex flexed to funding: FY27 pres capex delivered 19,337 of 38,000 planned; FY28 9,323 of 38,000.*

**Terminal (steady state at exit-2028 run-rate 28.2bn):** EBITDA 17,508; replacement capex 12,373 (life 6y, residual 10%); interest 4,527; tax 0; SBC 640; **owner earnings -32**; (EBITDA - replacement) / interest 1.13x. Equity bridge: EV - debt 48,850 - finance leases 649 + usable cash 3,000 - cost to serve deferred revenue 7,198.

## Residual to equity (end-2028, toy)

| Scenario | EV/EBITDA 4x: equity $m (per share) | EV/EBITDA 6x: equity $m (per share) | EV/EBITDA 8x: equity $m (per share) | Owner earnings / 12% | Shares (m) |
|---|---:|---:|---:|---:|---:|
| 1A Keep building | 5,518 ($9) | 56,383 ($96) | 107,248 ($183) | -32,571 ($-56) | 585.7 |
| 1B Growth capex | 27,977 ($48) | 99,277 ($170) | 170,577 ($291) | 4,470 ($8) | 585.7 |
| 2 Harvest | 21,035 ($34) | 49,568 ($80) | 78,102 ($126) | -2,364 ($-4) | 620.7 |
| 3 Funding stress | 16,334 ($26) | 51,349 ($81) | 86,365 ($137) | -263 ($-0) | 632.1 |

*Negative = equity is out of the money under that multiple. Per-share values use the toy share count above (559m + SBC + ATM), not a diluted count. EV/EBITDA multiples and the cap rate are ASSUMPTIONS, not market data. This is a range under stated assumptions, not a price target.*

## Backlog cover (diagnostic)

| Bucket (slide 13 chart, read from the PDF) | Share | $bn | Average |
|---|---:|---:|---:|
| < 24 months | 36% | 47.7 | 23.9 per year |
| 25-48 months | 38% | 50.4 | 25.2 per year |
| > 48 months | 26% | 34.5 | tenor beyond 48 months not given |

*Shares are 'percentage of backlog we expect to recognise in the months following quarter-end'. Backlog is RPO plus 'other amounts', subject to delivery and availability; more than 50% sits on contracts whose delivery commences by end-2026 (commencement, not recognition).*

| Scenario | Modelled revenue Q4'26 to Q3'28 ($bn) | Backlog < 24m ($bn) | Revenue / backlog | Exit-2028 run-rate ($bn) | Backlog 25-48m avg per year ($bn) |
|---|---:|---:|---:|---:|---:|
| 1A Keep building | 57.4 | 47.7 | 1.20x | 41.0 | 25.2 |
| 1B Growth capex | 69.9 | 47.7 | 1.47x | 57.5 | 25.2 |
| 2 Harvest | 43.8 | 47.7 | 0.92x | 23.0 | 25.2 |
| 3 Funding stress | 48.2 | 47.7 | 1.01x | 28.2 | 25.2 |

*A ratio above 1.0x means the scenario needs bookings and renewals beyond today's < 24-month backlog. The 25-48 month bucket averages well below the modelled exit run-rate, so the later years depend on renewals and new contracts. Backlog is not a revenue floor.*

## Sensitivity (scenario 1A; equity per share at 6x EV/EBITDA, and owner earnings)

Base: **$96 per share**, owner earnings -3,909.

| Change (low / high) | $/share, first | $/share, second | Owner earnings, first | Owner earnings, second |
|---|---:|---:|---:|---:|
| Adj. EBITDA margin 60% / 64% | $85 | $108 | -4,743 | -3,074 |
| Revenue per $ capex 0.22 / 0.32 | $70 | $122 | -6,265 | -1,553 |
| Cash capex / pres capex 1.00 / 0.80 | $96 | $96 | -3,765 | -4,052 |
| Useful life 5 / 7 years | $96 | $96 | -8,056 | -946 |
| Residual value 0% / 20% | $96 | $96 | -6,213 | -1,605 |
| New DDTL rate 10.5% / 6.5% | $94 | $98 | -4,978 | -2,839 |
| EV/EBITDA multiple 4x / 8x | $9 | $183 | -3,909 | -3,909 |

## Dilution (10-Q terms)

| Item | Shares (m) | Source / note |
|---|---:|---:|
| Cover-page shares, 30 Oct 2026 (Class A 465.8m + Class B 90.3m) | 556.1 | 10-Q cover; the model's opening share count |
| Q3 weighted-average shares (basic and diluted) | 559.0 | Ex.99.1; a loss quarter, so converts and RSUs are anti-dilutive and excluded |
| ATM, up to | 35.0 | OFFICIAL cap; take-up unknown; at $48.73 raises up to $1.7bn net |
| 2033 converts if converted ($4,200m at $97.85) | 42.9 | 10-Q; capped call to $199.70. Price is $48.73, so far out of the money and treated as DEBT |
| 2032 converts if converted ($4,000m at $119.60) | 33.4 | 10-Q; capped call to $230.00. Treated as DEBT |
| 2031 converts ($2,588m carrying) | n/a | conversion price not separately tagged in the filing; treated as DEBT |
| Toy count end-2028, scenario 1A | 585.7 | 556.1 + SBC $/price + ATM drawn |
| Toy count end-2028, scenario 3 | 632.1 | stress price $34 for ATM |

*If both the 2032 and 2033 converts were converted instead of repaid (1A at 6x): equity $64,583m over 662.0m shares = $98 per share, against $96 with the notes as debt. Arithmetic only: conversion needs the stock above $97.85 and $119.60.*

## Inputs

### OFFICIAL (value, source)

| Key | Value | Source |
|---|---|---|
| q3_revenue | 3661 | Ex.99.1 income statement, Q3 2026 |
| q3_opex | 3454 | Ex.99.1 |
| q3_gaap_oi | 207 | Ex.99.1 |
| q3_interest | 846 | Ex.99.1: interest expense, net |
| q3_other_income | 13 | Ex.99.1 |
| q3_net_loss | -709 | Ex.99.1 |
| q3_adj_ebitda | 2256 | Ex.99.1 non-GAAP reconciliation |
| q3_adj_oi | 379 | Ex.99.1 non-GAAP reconciliation |
| q3_da | 1889 | Ex.99.1 cash-flow statement |
| q3_sbc | 160 | Ex.99.1 cash-flow statement |
| q3_ocf | 1975 | Ex.99.1 cash-flow statement |
| q3_cash_ppe | 9441 | Ex.99.1: purchases of property and equipment (cash) |
| q3_pres_capex | 14500 | Presentation slide 8/14: $14.5bn capex (pres definition) |
| q3_wtd_shares | 559 | Ex.99.1: weighted-average shares, basic and diluted (NOT a period-end FD count) |
| q2_revenue | 2575 | Prior official release (Q2 2026), not this exhibit |
| m9_revenue | 8314 | Ex.99.1 |
| m9_gaap_oi | 14 | Ex.99.1 |
| m9_interest | 2022 | Ex.99.1 |
| m9_adj_ebitda | 4923 | Ex.99.1 |
| m9_adj_oi | 528 | Ex.99.1 |
| m9_ocf | 5638 | Ex.99.1 |
| m9_cash_ppe | 23558 | Ex.99.1 |
| m9_da | 4429 | Ex.99.1 |
| m9_sbc | 478 | Ex.99.1 |
| m9_debt_discount_amort | 143 | Ex.99.1 cash-flow statement: amortization of debt discounts, issuance costs |
| m9_deferred_revenue_cf | 3492 | Ex.99.1 cash-flow statement: change in deferred revenue (net, 9M) |
| m9_capped_calls | 1058 | Ex.99.1 |
| m9_private_placements | 2982 | Ex.99.1 |
| pres_capex_q1_26 | 8200 | Presentation capex chart |
| pres_capex_q2_26 | 9400 | Presentation |
| pres_capex_q3_26 | 14500 | Presentation |
| q3_debt_proceeds | 10301 | Ex.99.1 |
| q3_debt_repay | 2344 | Ex.99.1 |
| q3_capped_calls | 566 | Ex.99.1 |
| cip_q3_26 | 9300 | Presentation: CIP fell to $9.3bn from $11.9bn in Q2 |
| cash | 4122 | Ex.99.1 balance sheet |
| restricted_cash_cur | 1405 | Ex.99.1 |
| restricted_cash_noncur | 877 | Ex.99.1 |
| marketable_securities | 62 | Ex.99.1 |
| receivables | 4280 | Ex.99.1 |
| ppe_net | 56778 | Ex.99.1 |
| op_lease_rou | 18922 | Ex.99.1 |
| total_assets | 91481 | Ex.99.1 |
| recourse_debt_cur | 9183 | Ex.99.1 |
| recourse_debt_noncur | 32417 | Ex.99.1 |
| nonrecourse_debt_cur | 1389 | Ex.99.1 |
| nonrecourse_debt_noncur | 3884 | Ex.99.1 |
| deferred_rev_cur | 2269 | Ex.99.1 |
| deferred_rev_noncur | 7733 | Ex.99.1 |
| op_lease_liab_cur | 668 | Ex.99.1 |
| op_lease_liab_noncur | 18029 | Ex.99.1 |
| fin_lease_liab_cur | 296 | Ex.99.1 |
| fin_lease_liab_noncur | 353 | Ex.99.1 |
| total_liabilities | 87456 | Ex.99.1 |
| equity | 4025 | Ex.99.1 |
| total_cash_like_call | 6500 | Call: ~$6.5bn cash, equivalents, restricted cash and marketable securities |
| fy_rev_low | 13000 | Ex.99.1 outlook (prior Aug range $12.4-13.2bn; older $12-13bn) |
| fy_rev_high | 13300 | Ex.99.1 |
| fy_adj_oi_low | 1275 | Ex.99.1 outlook (Aug range $960m-1.15bn) |
| fy_adj_oi_high | 1375 | Ex.99.1 |
| fy_capex_low | 37000 | Ex.99.1 outlook, pres definition (prior $35-39bn) |
| fy_capex_high | 39000 | Ex.99.1 |
| q4_interest_low | 1050 | Ex.99.1 outlook |
| q4_interest_high | 1150 | Ex.99.1 |
| exit_arr_low | 20000 | Ex.99.1: exit-2026 annualised run-rate revenue (last month x12); Aug guide $18.5-19.5bn |
| exit_arr_high | 21000 | Ex.99.1 |
| active_power_gw_ye | 1.85 | Ex.99.1: >1.85 GW active power at year-end |
| prepay_next_3m | 9000 | Ex.99.1: ~$9bn prepayments and deposits next three months; >$3bn is recontracting existing infrastructure (Call) |
| convert_raise | 4200 | Ex.99.1: ~$4.2bn upsized convertible senior notes; terms now in the 10-Q (convert_2033) |
| atm_shares_max | 35.0 | Ex.99.1: inaugural ATM, up to 35m Class A (take-up NOT disclosed) |
| ddtl_55 | 2600 | Ex.99.1: $2.6bn DDTL 5.5 closed |
| undrawn_ddtl | 5000 | Call: nearly $5bn undrawn under committed DDTLs |
| parent_raise_through_2027_max | 5000 | Call: expect <$5bn incremental parent-level capital through 2027 |
| backlog | 132500 | Ex.99.1 / Presentation slide 13 |
| backlog_rpo | 132300 | Presentation backlog table |
| backlog_other | 200 | Presentation backlog table |
| backlog_prior_year | 55600 | Presentation slide 13 |
| backlog_pct_le24m | 0.36 | Presentation slide 13 CHART (read from the PDF image: dark-blue bottom bar = <24 months) |
| backlog_pct_25_48m | 0.38 | Presentation slide 13 chart: mid bar = 25-48 months |
| backlog_pct_gt48m | 0.26 | Presentation slide 13 chart: top light bar = >48 months |
| backlog_commence_by_ye26 | 0.5 | Call: >50% of backlog on contracts where delivery commences by end 2026 (commencement, not recognition) |
| wacd | 0.079 | Call: weighted-average cost of debt 7.9% at end Q3 (-250bp YoY). A claim |
| ddtl_financing_range | (0.7, 1.0) | Call: DDTLs finance 70%-100% of associated capex |
| ddtl_spread_bp | (225, 550) | Call: priced SOFR+225 to +550bp since IPO; <10% at the high end today |
| new_ig_ddtl_yield | (0.07, 0.075) | Call: next IG DDTL implied 7%-7.5%, >90% of capex |
| ig_enterprise_share_committed_capex | 0.75 | Call: >75% of committed capex tied to IG/enterprise customers |
| debt_paid_down_via_contracts | 4000 | Call: >$4bn paid down through contract cash flow |
| gpus_off_contract_2027 | 130000 | Call |
| gpus_off_contract_2028 | 170000 | Call |
| renewal_arr_2027 | 4000 | Call: 2027 renewals ~ approaching $4bn incremental annualised revenue, no new capex (claim) |
| renewal_arr_through_2028 | 10000 | Call: ~nearly $10bn cumulative incl. 2028 renewals (claim) |
| ladder_remainder_fy26 | 2433 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): LongTermDebtMaturities...RemainderOfFiscalYear |
| ladder_year1 | 10974 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): ...InNextTwelveMonths (Oct 2026 - Sep 2027; includes the Q4 2026 remainder) |
| ladder_year2 | 5479 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): ...InYearTwo (Oct 2027 - Sep 2028) |
| ladder_year3 | 4727 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): ...InYearThree |
| ladder_year4 | 4247 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): ...InYearFour |
| debt_principal_total | 47505 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): DebtInstrumentCarryingAmount, total principal |
| instrument_weighted_effective_rate | 0.0793 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): carrying-amount weighted effective rate across 18 instruments ($46,305m); the filing rounds each rate to whole percent. Confirms the call's 7.9% |
| convert_2033 | (4200, 97.85, 199.7) | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): 2033 convertible senior notes $4.2bn, 2.875% stated, conversion price $97.85, capped-call cap $199.70 |
| convert_2032 | (4000, 119.6, 230.0) | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): 2032 convertible senior notes $4.0bn, 1.75% stated, conversion price $119.60, cap $230.00 |
| convert_2031_carrying | 2588 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): 2031 convertible senior notes carrying $2,588m, ~2% effective; conversion price not separately tagged, so not converted below |
| op_lease_payments_due_12m | 2375 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): operating lease payments due in the next twelve months |
| op_lease_payments_undiscounted | 32954 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv): total undiscounted operating lease payments; weighted discount rate 10% |
| shares_cover_30oct | 556.125724 | 10-Q (acc. 0001769628-26-000465, crwv/quarterly/2026_Q3_10q_facts.tsv) cover: Class A 465,847,732 + Class B 90,277,992 + Class C 0 at 30 Oct 2026 |
| price_close_10nov | 48.73 | README / Yahoo regular close 10 Nov 2026 (prior close 48.98) |

### ASSUMPTIONS (value, source)

| Key | Value | Source |
|---|---|---|
| ebitda_margin | 0.62 | ASSUMPTION: held at Q3 2026 adj. EBITDA margin (Ex.99.1 62%) |
| rev_yield | 0.27 | ASSUMPTION: annualised revenue per $1 of pres capex placed in service. Cross-check: Q4'26 annualised revenue minus Q3'25 annualised revenue / last four quarters' pres capex = ~0.35 before CIP lag; 0.27 is deliberately lower |
| inyear_factor | 0.5 | ASSUMPTION: new capacity contributes half a year of revenue in the year it is placed in service |
| sbc_annual | 640 | ASSUMPTION: Q3 SBC $160m x 4 |
| other_income_annual | 52 | ASSUMPTION: Q3 other income $13m x 4 |
| other_adj_per_year | 48 | ASSUMPTION: Q3 adj OI -> GAAP OI bridge: 379 - 160 SBC - 207 = $12m/qtr other, x4 |
| adj_oi_bridge_per_year | 48 | ASSUMPTION: Q3 adj. OI minus (adj. EBITDA - D&A) = 379 - 367 = $12m/qtr, x4 |
| tax_rate | 0.21 | ASSUMPTION: US statutory rate on positive pre-tax income; NOLs and deferred tax ignored |
| cash_floor | 3000 | ASSUMPTION: minimum usable cash (cash + securities); Dec-25 usable cash was $3.1bn |
| cash_ratio_q4 | 1 | ASSUMPTION: Q4 cash capex = pres capex (Q3 deliveries pulled forward; payables unwind). 9M history 0.73, Q3 0.65 |
| cash_ratio_fwd | 0.9 | ASSUMPTION: cash capex / pres capex in 2027-28; the rest is OEM/vendor/finance-lease financed and added to debt. 9M26 actual 0.73 |
| amort_rate_debt | 0.2255 | DERIVED: current debt $10,572 m / total debt $46,873 m at 30 Sep 2026 (Ex.99.1) |
| amort_rate_lease | 0.03573 | DERIVED: current / total operating lease liability (Ex.99.1) |
| noncash_interest_share | 0.07072 | DERIVED: 143/2,022 (Ex.99.1) |
| ar_ratio | 0.2923 | DERIVED: receivables / (Q3 revenue x4) (Ex.99.1) |
| da_rate | 0.1591 | DERIVED: Q3 D&A x4 / (PPE net - CIP $9.3bn) |
| rate_ddtl_new | 0.085 | ASSUMPTION: new asset-level debt; mgmt: <10% at high end, 7-7.5% for IG; 8.5% blended |
| rate_parent_new | 0.1 | ASSUMPTION: new limited parent raise (converts/secured/term) at ~10% |
| rate_parent_stress | 0.15 | STRESS RATE ONLY: unverified mid-Oct press report of ~15% yield on 2032 unsecured; not an official input |
| release_rate_annual | 0.3 | ASSUMPTION: share of (opening deferred revenue + half of receipts) earned into revenue per year |
| receipt_rate_new | 0.3 | ASSUMPTION: customer prepayments received per $1 of pres capex; calibrated so net deferred-revenue inflow ~ 9M26 pace ($3.5bn) |
| q4_ddtl_share | 0.75 | ASSUMPTION: share of Q4 cash capex funded by asset-level debt (mgmt 70-100%) |
| atm_fee | 0.015 | ASSUMPTION: ATM commission/fees |
| convert_in_debt_already | True | CONFIRMED by the 10-Q: the 2033 convertible notes ($4,200m) are in the 30 Sep 2026 instrument list |
| useful_life_yrs | 6 | ASSUMPTION: GPU fleet economic life; not in the pack |
| residual_value_pct | 0.1 | ASSUMPTION: used-GPU resale as % of cost at end of life; not in the pack |
| gross_up | 1.35 | ASSUMPTION: gross / net PPE for a young fleet (about a quarter depreciated) |
| maintenance_pct_net_ppe | 0.1 | ASSUMPTION: harvest-case maintenance pres capex as % of opening in-service net PPE; steady-state replacement is 1/life = 16.7% |
| ev_ebitda_multiples | (4.0, 6.0, 8.0) | ASSUMPTION: EV / terminal adj. EBITDA range for a capital-intensive GPU lessor; not market data |
| owner_cap_rate | 0.12 | ASSUMPTION: capitalisation rate on steady-state owner earnings |
| atm_price_normal | 48.73 | Official 10 Nov close, used as issue price |
| atm_price_stress | 34 | ASSUMPTION: ~30% below 10 Nov close for the stress case |

### SCENARIO inputs

| Scenario | Pres capex | Renewal ARR add (claim) | DDTL share of cash capex | DDTL cap | Parent raise (amount, rate key) | Lease additions |
|---|---|---|---|---|---|---|
| 1A Keep building | {2027: 38000, 2028: 38000} | {2027: 0, 2028: 0} | {2027: 0.75, 2028: 0.75} | {2027: None, 2028: None} | {2027: (4000, 'rate_parent_new'), 2028: (2000, 'rate_parent_new')} | {2027: 6000, 2028: 5000} |
| 1B Growth capex | {2027: 50000, 2028: 50000} | {2027: 4000, 2028: 6000} | {2027: 0.75, 2028: 0.75} | {2027: None, 2028: None} | {2027: (5000, 'rate_parent_new'), 2028: (3000, 'rate_parent_new')} | {2027: 10000, 2028: 10000} |
| 2 Harvest | {2027: 'maintenance', 2028: 'maintenance'} | {2027: 0, 2028: 0} | {2027: 0.0, 2028: 0.0} | {2027: 0, 2028: 0} | {2027: (0, 'rate_parent_new'), 2028: (0, 'rate_parent_new')} | {2027: 0, 2028: 0} |
| 3 Funding stress | {2027: 38000, 2028: 38000} | {2027: 0, 2028: 0} | {2027: 0.55, 2028: 0.55} | {2027: 13000, 2028: 10000} | {2027: (1500, 'rate_parent_stress'), 2028: (1000, 'rate_parent_stress')} | {2027: 3000, 2028: 2000} |

## What would change the answer

- **Q3 10-Q, now partly used**: existing-debt repayments follow its maturity ladder (Q4'26 $2.4bn, FY27 about $9.9bn, FY28 about $5.3bn, assuming even repayment within each 12-month window) and the 2033/2032 convert terms and cover-page shares are in. Still open: the model backs the interest rate out of the Q4 guide (about 9.2%) instead of building it from each instrument's coupon; the 10-Q's weighted effective rate is 7.9%, so the gap of about 1.3 points is non-coupon cost (capitalised interest unwinding, fees, amortisation; an inference). Covenants and the new-DDTL repayment profile are not modelled.
- **Current bond prices and yields**: asset-level loans were said to trade near par; the unsecured 2032 yield (mid-October press report of about 15%, unverified) is used only as a stress rate in scenario 3.
- **Converts**: terms are now in the 10-Q ($97.85 and $119.60 conversion prices against a $39.51 share price, so they behave as debt). The 2031 notes' conversion price is not separately tagged and is not modelled.
- **Fully diluted share count**: the model now opens at the 556.1m cover-page shares (30 Oct 2026); RSUs, options and ATM take-up are still not in the filing data used.
- **Residual / used-GPU values and depreciation lives**: drive replacement capex and the terminal multiple; the pack gives neither. Management says depreciation 'dissipates' after contracts outlast depreciable lives.
- **Backlog conversion by year in dollars, customer concentration, termination rights**, and how much of the 36% < 24-month bucket is already delivering.
- **Cash vs presentation capex**: 9M cash PPE was 73% of the presentation series; how much of the gap is payables, finance leases and vendor financing (all debt-like) is not in the pack.
- **Capitalised interest**: Q4 interest guided about 30% above Q3 on similar debt suggests less capitalisation as CIP falls; the 10-Q should confirm.
- **Whether prepayments recur at the 2026 pace**: they are funding and deferred revenue that must be earned, not residual; the harvest case shows how they unwind.
- **Renewal pricing**: the call claims approaching $4bn incremental annualised revenue from 2027 renewals (about $10bn with 2028); only scenario 1B includes it, as a claim.
