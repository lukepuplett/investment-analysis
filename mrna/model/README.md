# MRNA toy projection (income, free cash flow, balance sheet), FY2026E-FY2030E

`python3 mrna_projection.py` writes `output.md` and `cash_and_fcf.png`. It needs Python 3, numpy and matplotlib. Units are $m and millions of shares. All inputs sit in `OFFICIAL`, `ASSUMPTIONS` and `SCENARIOS` at the top of the script, each with a source string or the word ASSUMPTION.

It is a toy, not a forecast and not a recommendation.

## What it does
- **FY2026E** is built from management's FY2026 framework (revenue growth 15–25%, R&D about $2.7bn, SG&A about $1.0bn, cost of sales about $1.7bn including a settlement charge, year-end cash $8.1–8.3bn), as recorded in [../analysis/2026_11_q3_delta_analysis.md](../analysis/2026_11_q3_delta_analysis.md), and the [Q3 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1682852/). FY2026 free cash flow is the plug that reproduces the year-end cash guide.
- **FY2027–30** are assumptions in three scenarios (Bear, Base, Bull) for vaccine and respiratory revenue, Moderna's share of oncology revenue (intismeran, shared with Merck), and R&D. SG&A, interest, tax and working capital follow the rules listed in `ASSUMPTIONS`.
- **Free cash flow** is net income plus D&A and stock compensation, less working capital absorbed by growth and capex. **Balance sheet items** are cash and investments, the $600m term loan (repaid at its Nov 2030 maturity, not refinanced), the $3.0bn convertible, leases, receivables, inventory and equity.
- A "what would have to be true" table solves for the revenue needed to reach zero free cash flow in 2028, management's stated cash break-even year, at different R&D levels.

## Limits
- Oncology revenue is not guided. The scenario numbers are illustrations, and the timeline (filing by end-2026, approval possible in H2 2027) comes from the repo's [23 Nov note](../analysis/2026_11_23_profitability_and_intismeran_timing.md), not verified against the call.
- Seasonality is ignored: it is annual. No new financing is modelled, even where Bear cash gets close to the $500m minimum-cash covenant.
- The convertible (conversion price about $210, near today's price) is treated as debt; conversion would add about 14m shares.
