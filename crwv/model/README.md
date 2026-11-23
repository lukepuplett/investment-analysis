# CRWV equity residual toy model (Q3 2026 pack, 10 Nov 2026)

`python3 crwv_residual_model.py` writes `output.md` plus four charts: `coverage.png`, `cash_after_capex.png`, `leverage.png` and `residual_range.png`. It needs Python 3, numpy and matplotlib. Units are $m and millions of shares.

It is a toy model of what is left for equity after lenders, lessors, depreciation, cash capex and dilution. It is not a production DCF, has no price target and makes no recommendation. The Q3 2026 Form 10-Q was filed on 12 Nov 2026 and is saved as `../quarterly/2026_Q3_10q.htm` (facts in `_10q_facts.tsv`), but this version still uses the 11 Nov proxies: the debt maturity ladder, lease schedule, convert terms and share counts in the filing have not yet replaced them. Do not download a 10-Q from the IR site without checking the period on page one; the CloudFront PDF on the results page was the Q2 10-Q (period ended 30 Jun 2026).

## Where inputs live
- `OFFICIAL`: figures from Exhibit 99.1 to the 10 Nov 8-K ([acc. 0001769628-26-000461](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000461/0001769628-26-000461-index.html)), the presentation (backlog tenor chart read from the slide 13 image, not the .txt), and management call comments. The call items are tagged `Call` and are claims, not facts. Each has a source string.
- `ASSUMPTIONS`: everything else, tagged `ASSUMPTION`, `DERIVED` (computed from `OFFICIAL`) or `STRESS RATE ONLY`.
- `SCENARIOS`: per-year capex, renewals, DDTL share and cap, parent raise and lease additions.
- `verify_official()` re-checks the derived totals (debt $46,873m, leases, cash $6,466m, backlog) and looks for key figures in the Ex.99.1 text extract. It reads `../quarterly/2026_Q3_press_release.txt`.

## Scenarios
1. **1A Keep building (committed backlog only)**: Q4 on the official guide, then 2027 pres capex in line with 2026 ($38bn), per the call. 2028 is an ASSUMPTION. **1B** is a separate higher-capex growth case with the call's renewal claim (about $4bn of annualised revenue in 2027, about $10bn including 2028). It is a claim, not contracted.
2. **Harvest**: growth capex stops. Cash capex is maintenance at 10% of in-service net PPE, an ASSUMPTION that sensitivities should vary (steady-state replacement is about 1/life). The $9.3bn already in CIP is finished with no further cash and does add revenue.
3. **Funding stress**: no new parent unsecured debt. Asset-level debt is capped, the parent raise is small and priced at a 15% stress rate (an unverified press report, not an official input), and the ATM is used at a $34 assumed price. Capex is cut until the plan is funded.

## Method in brief
- Q4 2026 = FY guide minus 9M actuals (revenue, adj. OI, pres capex), common to all scenarios. Interest on existing debt is built from the 10-Q's 19 instruments (principal $47,505m; weighted effective rate 7.9%, which confirms management's figure), in four classes (secured/OEM, unsecured notes, converts, other). Scheduled repayments hit secured/OEM debt first (ASSUMPTION), so the cheap converts and 9-10% notes make up more of what remains. The Q4 interest guide implies a further non-coupon cost of about 1.4 points on existing debt (capitalised interest unwinding, fees, amortisation; inferred, not disclosed), backed out of the guide and carried forward at 100% (`nc_persistence`, a sensitivity row).
- Presentation capex (placed in service, drives D&A, PPE and revenue) and cash capex (cash-flow statement) are separate series. The gap, 10% in 2027-28, is treated as OEM/vendor/finance-lease financed and added to debt.
- Revenue: exit-2026 run-rate (official $20-21bn) plus new capacity at an assumed revenue per $ of capex, plus renewals only where stated.
- Coverage is computed the hard way: GAAP operating income / interest, op. cash flow excluding prepayments / (cash interest + scheduled principal), cash after interest and capex with and without net prepayments. Operating lease cost is already inside EBITDA and GAAP OI.
- Prepayments are funding and deferred revenue to be earned. Net prepayments = receipts less amounts released to revenue, and they are never counted as equity residual.
- Sources and uses balance each period: cash capex + principal + capped calls = op. cash flow + asset-level draws + parent raise + cash above floor + ATM, plus an explicit unfunded gap.
- Residual: two lenses at the exit-2028 run-rate. (a) EV/EBITDA multiples (4/6/8x, ASSUMPTIONS) less debt, finance leases and the cost to serve deferred revenue, plus usable cash. This ignores replacement capex, so it is generous. (b) Steady-state owner earnings (EBITDA less replacement capex, interest, tax and SBC) capitalised at 12%. This assumes no growth, so it is harsh. Both are shown.

## Known limits
- Which instruments the maturity ladder actually repays is not in the filing (modelled secured/OEM first). Existing-debt principal follows the Q3 10-Q maturity ladder (Q4'26 $2,433m; the 12-month windows $10,974m, $5,479m, $4,727m, $4,247m), spread evenly within each window. New asset-level debt still uses current debt / total debt (22.6%) as a repayment proxy.
- Share count opens at the 556.1m 10-Q cover-page shares (30 Oct 2026) plus SBC and ATM shares. The 2033 and 2032 converts ($97.85 and $119.60 conversion prices, capped calls to $199.70 and $230) are far out of the money and treated as debt; an if-converted case is in `output.md`.
- Taxes ignore NOLs and deferred tax. Margins are held flat. 2028 funding assumptions have no management support.
