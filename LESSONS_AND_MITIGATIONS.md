# Lessons and mitigations for finances and outlook research

*Added 11 November 2026. A companion to [THINKING_FRAMEWORK.md](THINKING_FRAMEWORK.md). Use this when researching a company's finances and outlook, before or alongside a thesis.*

The expensive mistakes happen when the demand or bottleneck call is right and the claim on the profits is wrong. These notes turn that into practical checks on the accounts, the capital structure, and the outlook.

## Lessons

- **Demand is not value capture.** A backlog, a raised outlook, or a scarce service can all be real, and still leave shareholders with little if lenders, lessors, suppliers, customers or the state take the rents.
- **A cheap cost of capital is not a moat.** Today's funding rate is a condition, not an advantage, unless something durable keeps it there. If the equity thesis only works at an unusually low cost of funds, the thesis is about credit conditions, not the business.
- **A risk you list but do not treat as a kill switch is a risk you have not really underwritten.** If the outlook depends on debt falling as spending moderates, write the date, the figure, and what you will do if spending is raised instead.
- **For a leveraged business, coverage after interest and leases is the number that matters, not adjusted earnings before those costs.** A large adjusted EBITDA, or a similar figure, can coexist with operating profit that does not cover the interest bill.
- **Prefer the owner of a scarce bottleneck to the leveraged renter of it.** If the same outlook can be expressed through a company that owns the scarce asset or right, the renter needs a much larger margin of safety — or you should own the other thing.
- **A sharp fall from a price that assumed cheap capital or perpetual growth is often the correction, not a bargain.** "Beaten up" is not the same as cheap.
- **A low multiple at record margins is not the same as cheap.** For a cyclical business, trailing earnings at a peak make the P/E look low exactly when they are least likely to last. Micron (about 9.5x on FY2026) and SanDisk (about 6x) both show cost of goods far below the revenue jump, which means the gain is price, not volume. Ask how much of the margin is price, and what the multiple looks like at mid-cycle earnings.
- **Credit can reprice the equity before the income statement does.** Bond yields, new-issue pricing, lease-adjusted leverage and dilution programmes often move first.
- **"We would be cash-flow positive if we stopped expanding" is a warning, not a comfort, when the outlook requires them to keep expanding.** Continuous access to markets is then a load-bearing assumption, not a footnote.

## Mitigations

Run these checks on any new name, and again when the outlook or the capital structure changes.

- **Map the claim.** Who keeps the rent if money gets expensive, or if the scarce thing becomes less scarce? Is this the owner of a bottleneck, or a renter of someone else's? If it is the renter, the equity is only the spread after lenders, lessors and depreciation have been paid. Price that spread, not the revenue.
- **Rebuild coverage the hard way.** Compare GAAP, or IFRS, operating income, and cash flow after capital spending, to interest and lease payments. A comforting adjusted earnings figure does not count until that residual is clearly positive, or can get there without another turn of cheap credit.
- **Stress the funding.** What happens if unsecured yields double, or new borrowing stops? List maturities, secured versus unsecured debt, leases, converts and any at-the-market or other dilution programme. If the firm would be cash-flow positive only if it stopped expanding, treat continuous market access as a load-bearing assumption.
- **Match the clocks.** Contract length, asset life and debt tenor should fit. An asset that may lose economic life before the debt is repaid, or a contract shorter than the financing that funds the capacity, is a mismatch waiting for a refinancing.
- **Inspect the backlog and the outlook.** Firm orders and customer prepayments are one thing; amounts estimated to be recognised if capacity is delivered, or contracts with customers who can substitute or build their own, are another. A raised outlook should be compared with the immediate prior guide, not an older range that makes the change look larger than it was.
- **Write the kill switch in advance.** If you say debt should decline as spending moderates, define the date, the number, and what you do if spending is raised instead. A risk you only "monitor" will not change the recommendation in time.
- **Check the cleaner expression of the same outlook.** If another company gives you the same scarcity or demand story without the leveraged residual, you need a much larger margin of safety to own the weaker claim — or you should own the other thing.
- **Let credit lead.** Bond yields, new-issue pricing and lease-adjusted leverage will often tell you the equity is in trouble before the earnings release does. Do not add just because the shares have fallen from a high that assumed cheap capital.

## The debt and obligations check (what to extract)

Run this on every full analysis, in addition to the mitigations above, and put the result in the risk assessment. It exists because for CoreWeave the headline debt number understated the claims ahead of equity: operating leases, converts and the maturity ladder were separate lines. Pull the figures from the debt and lease notes in the 10-Q or 10-K; the facts file `scripts/edgar_snapshot.py` writes (`quarterly/*_facts.tsv`) usually has them tagged. Record the source accession.

| Check | What to extract | Why |
|---|---|---|
| Instruments | Each borrowing: balance, effective rate, maturity, secured or not. Sum it; it must tie to the balance sheet (CRWV: 19 instruments, $47,505m principal). | A single total hides the expensive and the short-dated pieces. |
| Maturity ladder | Principal due in each of the next years, against cash and operating cash flow. | Shows what has to be repaid or refinanced, and when. |
| Leases | Operating and finance lease liabilities and the undiscounted payments. | Leases sit outside the debt line (CRWV: $18.7bn of operating leases against $46.9bn of debt). |
| Converts | Conversion price against today's price, capped calls, dilution if converted. | Far out of the money, a convert is debt; in the money it is dilution. |
| Funding access | Undrawn facilities, covenants, at-the-market programmes, anything that can be switched off. | Continuous market access is a load-bearing assumption if cash flow is negative after spending. |
| Coverage, the hard way | GAAP or IFRS operating income, and cash flow after capex, against interest and lease payments; debt plus leases against equity. | Adjusted earnings can hide a residual that does not cover the bill. |
| Off balance sheet | Purchase obligations, guarantees, joint ventures, commitments not on the balance sheet. | They compete with equity for the same cash. |

If any row cannot be filled from the filings, say so in the analysis (as "not extracted" or "not disclosed") instead of leaving it out.

## How to use this

These checks sit inside layer 2 and layer 3 of the thinking framework: who captures the value, and what is already in the price. If a check fails, write it into the thesis as a kill switch with a date and a number, or do not recommend the equity. When a later print or outlook change arrives, ask first whether it repairs the residual claim, or only restates that demand is still there.
