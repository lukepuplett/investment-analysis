# ANT (Anthropic) analyst model — S-1/A No.2 (10 Nov 2026)

`python3 ant_model.py` writes `output.md` plus three charts: `dilution_waterfall.png`, `revenue_scenarios.png` and `price_per_share.png`. All inputs sit in two dicts at the top of the script. `FILING` holds filing figures with page references: "A2 p.x" is [S-1/A No.2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm), and un-prefixed "p.x"/"F-x" is S-1/A No.1, for financial statements carried over unchanged. `ASSUMPTIONS` holds everything else, each marked ASSUMPTION or with its origin. Units are $m and millions of shares.

The base case is the filed deal: **$70.00–$78.00, midpoint $74.00**, no greenshoe. The 9 Nov version used S-1/A No.1 with an assumed $25bn raise and solved for the price at $1.5tn. That is kept in git history as prior work, not as the current base case.

## What comes from the filing (S-1/A No.2)
- **Offering:** 825.0m Class A. Anthropic sells 801.35m and the seven co-founders sell 23.65m (3.38m each). The greenshoe is 123.75m, all from the company (cover, A2 p.20, p.301).
- **Concurrent private placement:** $26.0bn of Class N at the IPO price. It is contingent on the IPO, unregistered and not locked up. At $74 it buys: Google $10.0bn (135.1m shares), NVIDIA $10.0bn (135.1m), AMD $2.5bn (33.8m), Broadcom, Micron and Microsoft $1.0bn each (13.5m), and TSMC $0.5bn (6.8m). That is 351.4m shares in total (A2 p.20). The share count moves inversely with the price.
- **Board IOIs:** up to $303m (Hastings DAF $300m, Liddell trust $3m) to buy **in** the offering, so inside the 825m (cover, A2 p.301).
- **Net proceeds to the company:** ~$84.6bn at $74, ±$793m per $1, or ~$93.7bn with the shoe (A2 p.21, p.128). Pro forma as adjusted cash and short-term investments are $212.7bn after RSU tax withholding (A2 p.131).
- **Outstanding after the deal:** 7,427,991,791 Class A + 5,658,680,800 Class N + 1 Class T + 1 Class F = **13,086,672,593** (13,210,422,593 with the shoe) (A2 p.21). This includes the 846.8m Public Benefit Fund shares and the 276.8m Amazon note shares that convert at the IPO.
- **Fully diluted layers (A2 p.23–25):**
  - options 1,774.3m at $2.91
  - unvested RSUs 1,026.7m and post-30-Sep RSUs 47.0m
  - acquisition shares 1.4m, Matching Issuance 28.0m
  - Vested Matching Obligation 553.4m, holdback 1.6m
  - Amazon rollover notes 1,563.6m
  - The filing's own fully diluted table totals **18,012,993,381** at $74 (options by TSM).
  - Not counted even there: the 2026 Plan reserve of 1,920.6m and the ESPP reserve of 128.0m.
- **Amazon notes:** $2,186m at $2.0928 and $4,017m at $5.0478, which is 1,840.4m shares uncapped. Amazon **did not waive** its 12% cap, so only $579.3m / 276.8m shares convert at the IPO. The remaining ~$5.62bn / 1,563.6m shares become non-interest-bearing rollover notes. They convert each quarter-end at the lowest of the fixed price, the IPO price and the 10-day VWAP, up to the cap, or are repaid in cash at maturity in 2034–35 (A2 p.62, p.172–174). After the deal Amazon holds 1,920.5m Class N and Google 1,789.6m (A2 p.120–121).
- **Remaining facilities:**
  - Google 2026 NPA cut from $20bn to **$10bn** by the PIPE (A2 p.173)
  - Amazon 2026 NPA $15bn, none expected before the IPO
  - Broadcom $42bn at 9% PIK and 90% of VWAP, or 13% and 85% in the penalty case (A2 p.175)
  - AMD commitment cut from $5bn to **$2.5bn**, first milestones in 2027 (A2 p.172)
- **ARR:** ~$81bn at 31 Oct 2026, up $10bn from 30 Sep (A2 p.203). NRR is still ~900%.
- **Commitments (updated in No.2):** $900.9bn in total, $451.6bn of it by 2030, and $70.7bn in the next 12 months. $186.2bn is terminable or contingent (A2 p.144, p.178–179). No.1 had $895.4bn, $447.5bn, $69.8bn and $213.8bn. Microsoft is now at least $47.2bn and up to $49.2bn.
- **Financials:** the 9M26 P&L, quarterly revenue and compute, functional costs and SBC are as in S-1/A No.1 (p.24, p.159, p.161, F-40, F-52/53).

## Share bases used
| Basis | What it adds | Shares at $74 |
|---|---|---|
| Outstanding | IPO + PIPE, as filed | 13.09bn |
| Tighter FD | + options (gross), RSUs, acquisition and matching shares already issued | 15.96bn |
| + vested match | + Vested Matching Obligation + holdback | 16.52bn |
| Filing FD | + Amazon rollover notes, options on TSM (= A2 p.25 table; CNBC's $1.405tn at $78) | 18.01bn |
| + plan reserves | + unused 2026 Plan and ESPP reserves (overhang, not day-one shares) | 20.06bn |
| + facilities | Filing FD + remaining Google, Amazon, Broadcom and AMD facilities at the IPO price | 19.02bn |

## Key ASSUMPTIONS
- **Prices other than $74:** only the PIPE share count is re-struck. RSU withholding and the cap-limited Amazon conversion also move slightly with price but are held at the $74 figures.
- **Amazon drip:** the cap lets Amazon convert about 12–13.6% of any new non-Amazon capitalization. The model assumes 60m a quarter of other issuance (ASSUMPTION), so the notes barely drip. They clear faster only if Amazon sells, the cap base grows faster, or Amazon waives the cap.
- **Facility shares:** issued at the IPO price. The filing uses the 30-day VWAP at each draw.
- **Revenue paths, cost glide paths, Broadcom draws, tax, NOLs and the 25x / 12% exit:** unchanged from 9 Nov (see the `ASSUMPTIONS` dict). Bear's 4Q26 ($18.7bn) is now below a flat 31 Oct run-rate (~$20.2bn).
- **Commitment floor:** 4Q26 $15bn, then $74bn, $106bn, $120bn and $136.6bn. That sums to No.2's $451.6bn; the split by year is an ASSUMPTION. Bear expenses 79%, walking away from the $186.2bn contingent or terminable portion.
- **EPS:** uses the filing FD plus all remaining facilities (19.0bn shares), which is conservative.

## Big caveats
- The filing doesn't give the yearly commitment schedule beyond the A2 p.178 table, holder-level ownership of the other non-voting holders, the SBC split by function, or its own forecasts.
- Whether the unconverted notes count inside Amazon's "Note Capitalization" is not stated. Amazon's 1,920.5m / 12% ≈ 16.0bn is derived.
- Treating commitments as an expense floor is crude. Leases run through amortisation and interest, and some deals can be cancelled.
