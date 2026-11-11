# SpaceX (SPCX) — synthesis of the 11 Nov 2026 work

This note ties together the [inputs register](2026_11_model_inputs.md), the [valuation snapshot](2026_11_valuation_snapshot.md), the [terrestrial model](../model/README.md) and the [orbital data centre model](../orbital/README.md).

## 1. The price is ~$1.9T (about $141 a share)

On Q3 run rates that is ~33x EV/sales, ~54x adjusted EBITDA and ~170x operating income, with 9M free cash flow of about −$35B. Starlink earns almost all of the profit. At a mature 25x P/E the price needs ~$75B of net income.

## 2. The ground business is worth far less than that

From the terrestrial model (`spcx/model/`), 50/50 blend of DCF and 25x 2030 net income:

| Scenario | Value per share | Unexplained by ground business |
|---|---:|---:|
| Bear | ~$6 | ~$1.84T |
| Base | ~$22 | ~$1.62T |
| Bull | ~$109 | ~$445bn |

Even the bull case (10–28 GW on the ground by 2030 at neocloud yields) is below the market price. The DCF is dragged down by years of negative compute cash flow, so the exit-multiple half carries most of the weight. The three things that move it most are GW deployed × revenue per GW, capex per GW plus financing ($154–577B of funding needed), and how fast Starlink grows.

## 3. Orbital compute does not beat the ground yet

From the orbital model (`spcx/orbital/`):
- Cost per GW is ~$64B to install and ~$84B over its life in the base case (bear $150B, bull $52B), against ~$60B on the ground.
- Mass is ~6.5 kilotonnes per GW, about 65 Starship flights at 100 tonnes each.
- Breakeven launch cost is ~$123 per kg, against Falcon 9 at ~$1,500–3,000 per kg today.
- The constraint that kills it is launch rate. 100 GW a year needs ~18 Starship flights a day. After that comes cooling, which needs radiator fields kilometres across.
- Baker's ~$30B per GW doesn't add up even on his own inputs ($35B IT + $5B launch = $40B). Only the bull case gets near it.

**So the market is paying ~$1.6T (base case) for a business that is still more expensive per GW than the ground and needs a launch rate nobody has reached.** The alternative explanations are a Tesla merger premium, or a Musk premium.

## 4. Are they paying for "free electricity"?

Mostly, but it's worth little. 1 GW running all year uses ~8.8 TWh, about $0.5–0.7B a year at $60–80 per MWh. Chip depreciation (~$35B of IT over 5–6 years) is about $6–7B a year, so power is only ~5–10% of the annual cost of running a GW. Orbit doesn't extend chip life, and radiation plus no repairs probably shortens it. Every replacement chip has to be launched, which is why the orbital lifetime cost runs ~$20B above install cost.

The real case for orbit is **getting power quickly**, not cheaply. On Earth the bottleneck is grid connections, permits and turbines. If Starship can put a GW up faster than one can be connected on the ground, that's worth paying for. But it's a bet on launch cadence, and cadence is exactly where the model breaks.

## 5. What would change the view

- Starship flying reused, at a high rate, at well under $200 per kg (track the flight record).
- Signed orbital compute contracts, or orbital capex disclosed in a 10-Q.
- Terrestrial GW additions running well ahead of the 1.7 GW base (watch for MW figures in the Q4 10-K).
- Concrete Tesla–SpaceX merger terms.

Tags: #SPCX #valuation #orbital #compute #GOOG
