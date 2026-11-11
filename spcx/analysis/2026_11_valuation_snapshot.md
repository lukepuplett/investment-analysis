# SpaceX (SPCX) — valuation snapshot, 11 Nov 2026

Rough multiples taken from the filed numbers in [2026_11_model_inputs.md](2026_11_model_inputs.md). This is not a scenario model. "Run rate" means Q3 FY2026 × 4.

## Price and capital structure

| Item | Value | Source |
|---|---:|---|
| Price | $141.30 (about 20:13 London, 11 Nov 2026) | Yahoo chart API |
| Shares outstanding | 13.581B (Class A 8,246.5M + Class B 5,334.5M) | Q3 10-Q cover, 15 Oct 2026 |
| Market cap | ~$1.92T | price × shares |
| Cash and equivalents | $51.3B | 10-Q, 30 Sep 2026 |
| Debt principal | $38.0B (excluding finance leases) | 10-Q Note 9 |
| Enterprise value | ~$1.91T | before the ~$40B Apollo GPU lease, which is not yet fully on the balance sheet |

## Multiples on the run rate

| Metric | Q3 | Run rate | Multiple |
|---|---:|---:|---:|
| Revenue | $14.6B | ~$58B | ~33x EV/sales |
| Adjusted EBITDA (non-GAAP) | $8.8B | ~$35B | ~54x |
| Operating income | $2.79B | ~$11B | ~170x |
| Net income | $4.4B (9M: −$0.4B) | n/m | n/m |

Q3 operating income by segment: Connectivity (Starlink) $2,367M, Super Intelligence $431M on $7.56B of revenue, Space −$7M. Starlink earns almost all of the profit.

Cash flow over 9M 2026: operating cash flow $13.1B, capex $48.1B, so free cash flow is about −$35B.

## The forward case from contracts already signed

- The Google contract is $920M a month, about $11B a year (FWP, 5 Jun 2026; cancellable on 90 days' notice after 31 Dec 2026).
- The Anthropic deal is about $3.1B a month at full delivery, about $37B a year (Anthropic S-1/A; capped at $120.5B).
- Adding both to the run rate gives roughly $100B of revenue, which is about 19x EV/sales. Part of the Q3 revenue already includes these contracts ramping, so $100B is an upper-bound sum, not a forecast.

## Reverse test

To justify ~$1.9T at a mature 25x P/E, SpaceX needs about **$75B of net income**, roughly 17 times Q3's annualised operating income. Starlink plus the signed compute contracts don't get there. The price requires Musk's multi-GW terrestrial ramp, orbital compute, or both, to deliver at scale. The filings contain no orbital capex or revenue plan, only the 100 TW milestone in Musk's award against 1.7 GW of nameplate compute today.

## Conclusion

The price is for the bull case. You're paying today for compute capacity that hasn't been built yet, much of it in space. The parts that are investable on filed numbers are Starlink (profitable and growing) and the contracted Super Intelligence revenue (concentrated: two customers are 16.6% and 34.5% of revenue, with cancellation rights).

## Caveats

- Run-rate × 4 overstates a business that is ramping fast in some places and understates it in others. Q3 SI revenue jumped from $2.56B in Q2 to $7.56B.
- The EV excludes finance leases and the Apollo lease. Including them pushes the multiples up slightly.
- Adjusted EBITDA is the company's non-GAAP figure.
- Earth-based scenario model: [../model/README.md](../model/README.md) (`spcx/model/spcx_model.py`); orbital compute as residual vs market cap.

Tags: #SPCX #valuation #GOOG #AI #compute
