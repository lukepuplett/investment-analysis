# Compute prices

A monthly gauge of what a unit of matrix multiplication sells or rents for. It's a cheap, unmanaged proxy for AI compute supply and demand, which underpins valuations across the AI stack (NVDA, CRWV, the hyperscalers).

`gpu-prices.csv` has one row per observation:
- `metric`: `launch_msrp`, `launch_rrp`, `used_median` (resale) or `rent_hourly` (cloud rental per GPU-hour).
- `price_type`: `list`, `ebay_bin_asking` (active Buy It Now asking prices, which overstate realised prices), `ebay_sold`, or `rental_quote`.
- `p25` and `p75`: the interquartile range, where available. `n` is the sample size.

Chart value over date per `item` + `region` + `metric`. Compare rows with like `price_type` only.

Context: [Jon Gray on neocloud pricing and H100 lease rates](../diary/2026-10.md) (2026-10-24) and [CRWV notes](../crwv/README.md).
