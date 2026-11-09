# ANT (Anthropic) analyst model — S-1/A No.1 (2 Nov 2026)

`python3 ant_model.py` writes `output.md` plus three charts: `dilution_waterfall.png`, `revenue_scenarios.png` and `price_per_share.png`. All inputs sit in two dicts at the top of the script. `FILING` holds S-1/A figures with page references. `ASSUMPTIONS` holds everything else, each marked ASSUMPTION or "Brief". Units are $m and millions of shares.

## What comes from the filing (S-1/A page refs)
- **Basic shares** (30 Sep 26): 2,168.8m Class A + 30.6m Class N (F-7). The share counts are post the 10-for-1 split (F-15).
- **Preferred:** taken series by series from the F-47 table. Conversion is 10:1, except D-1, D-2 and D-3 at ~10.6, 10.4 and 10.6 (F-47/48). That gives 8,560m as-converted, which reconciles to the F-59 figure of 8,559m.
- **Series H:** $589.0095 per preferred share, which at 10:1 is $58.90 per common share.
- **Amazon rollover notes:** $2,186m at $2.0928 plus $4,017m at $5.0478, each at the lower of that price and the IPO price. That makes 1,840m Class N shares (p.168). Amazon's 12% ownership cap applies and is waivable (p.168). Google's cap is 14.99% (p.172).
- **Options:** 1,774.3m at a $2.91 weighted-average exercise price (p.21/F-52), counted by the treasury stock method.
- **RSUs:** 1,128.0m double-trigger RSUs (F-53). The $8.2bn SBC catch-up at IPO, $24.1bn unrecognised over ~2 years, and $1.8bn of option cost over ~1.2 years are on F-52/53.
- **Public Benefit Fund:** 846.8m Class N, which is 5% of fully diluted shares at 30 Jun 26 (p.146). Further top-ups of up to 2% per +50% share-price milestone are **not modelled**.
- **Other:** donation-match liability 28.0m and holdback 1.6m (F-59), plus 0.85m post-Q3 acquisition Class N (p.21; the Class A number is blank).
- **SAFEs:** zero; all converted by Dec 2024 (F-32).
- **Warrants:** none issued by ANT. The F-31 warrant rights are an asset ANT holds.
- **Undrawn facilities:**
  - Google 2026 NPA: $20bn
  - Amazon 2026 NPA: $15bn
  - Broadcom NPA: $42bn at 9% PIK, converting at 90% of VWAP. The penalty case is 13% interest and conversion at 85% (p.169–171).
  - AMD put: $5bn (p.167)
  - Google's $10bn IPO private-placement option *reduces* the Google NPA, so it adds no extra shares (p.172).
- **Financials:**
  - Quarterly revenue and compute: p.161
  - 9M26 expenses by nature: p.24
  - 9M26 functional costs (cost of revenue $4,812m; R&D $19,240m): F-40
  - SBC and donation match: p.159
  - Cash and short-term investments of $131.8bn: p.26
  - Capex and lease prepayments: F-13
  - Commitments: $895.4bn total, $447.5bn of it by 2030, and $69.8bn in the next 12 months (p.140). The contractual table is on p.174.

## Key ASSUMPTIONS
- **IPO:** $25bn primary raise and 3% fees. The filing leaves the size and price range blank.
- **Facility shares:** all issued at the IPO price, per the brief. The filing actually uses the 30-day VWAP at each draw, so a higher future price would mean fewer shares. Broadcom shares are counted on principal only, at 90% or 85%. The share count holds the market cap fixed and ignores the ~$82bn of cash those shares bring in, which is slightly conservative per share.
- **RSUs:** counted gross. The filing says they settle net of tax withholding, but the rate is blank.
- **Amazon notes:** counted in full. In practice the 12% cap likely limits conversion at IPO, with the rest converting quarterly later.
- **Holder attribution:**
  - Amazon is credited with only the series the filing ties to it: E-2, F-2 and G-3 (note conversions), 19.3m of G-2, and $5bn of Series H.
  - Google is credited with E-3, E-4, E-5 and G-4, 38.6m of G-2, and $10bn of Series H.
  - Voting preferred is a *proxy* for venture/financial investors.
  - The other non-voting holders aren't disclosed.
  - **A precise venture-vs-strategic split can't be derived from the filing.**
- **Revenue:** paths start from 3Q26 revenue of $16,956m. QoQ growth starts at g0 in 4Q26, decays by d each quarter, and is floored at f:
  - Bear: 10% / 0.75 / 1.5%
  - Base: 22% / 0.85 / 2.5%
  - Bull: 30% / 0.88 / 3.5%
  - Thread: the Base 4Q26, then +145% and +69% (the thread's figures), then +30% and +20% (ASSUMPTION).
- **Costs:** each line glides linearly from its 9M26 actual (% of revenue) to a 2030 target.
  - Cost of revenue: 14.5% today, ending at 20% / 17% / 14% (bear / base / bull)
  - Training and other compute: 42.1% today, ending at 40% / 30% / 22%
  - Cash personnel: 4.8%, a proxy for R&D excluding compute, because the S-1 gives no SBC split by function
  - S&M and partnerships: 16.6%
  - Other G&A excluding donation: 9.7%
  - New SBC grants: 5% / 4% / 3%
  - Donation match: 2% / 1.5% / 1%
- **Commitment floor:** compute and infrastructure expense is at least the yearly commitment schedule: 4Q26 $14bn, then $74bn, $106bn, $120bn and $133.5bn (2027–2030). These add up to $447.5bn, and 4Q26 plus ¾ of 2027 roughly equals the $69.8bn next-12-month figure. **The split by year is an ASSUMPTION.** Bear expenses only 76% of it, walking away from the $213.8bn contingent or terminable portion (p.174).
- **Broadcom draws:** $42bn at 13% in bear, $21bn at 9% in base and thread, none in bull, drawn evenly over 2027–30. Interest is PIK.
- **Other:** cash yield 3.5%, tax 21%, $15bn of usable NOLs, capex outside the commitments at 5% of revenue, and no forecast for fair-value marks.
- **Valuation:** exit at 25x 2030 EPS after 4 years, discounted at 12%, per the brief.

## Big caveats
- The filing doesn't give the IPO price range, deal size, ARR, holder-level ownership of the non-voting shares, the SBC split by function, the yearly commitment schedule beyond the p.174 subset, the SpaceXAI $/hr, or its own forecasts.
- Treating commitments as an expense floor is crude. Leases run through amortisation and interest, and some deals can be cancelled, e.g. SpaceXAI on 90 days' notice after early 2027.
