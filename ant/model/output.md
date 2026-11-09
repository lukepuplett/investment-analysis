# ANT model output (S-1/A No.1, 2 Nov 2026)

All $ in millions unless stated; shares in millions. Run `python3 ant_model.py`. Assumptions are listed in README.md and at the top of ant_model.py.

## 1. Share bridge / dilution waterfall

Priced at the **$1.5tn fully-diluted IPO price of $90.37** (solved as a fixed point: price = $1.5tn / FD shares incl. IPO primary).

| Step | Shares (m) | Cumulative (m) | Source |
|---|---|---|---|
| Basic: Class A + Class N | 2,199 | 2,199 | F-7 |
| Preferred -> common (10:1; D-series 10.4-10.6) | 8,560 | 10,759 | F-47 |
| Amazon rollover notes ($6.2bn @ $2.09/$5.05) | 1,840 | 12,599 | p.168 |
| Options (treasury stock method) | 1,717 | 14,317 | F-52 / p.21 |
| RSUs (1,128m, counted gross) | 1,128 | 15,445 | F-53 |
| Public Benefit Fund (Class N) | 847 | 16,292 | p.146 |
| Donation match + holdback + post-Q3 acq. | 30 | 16,322 | F-59 / p.21 |
| SAFEs / ANT warrants | 0 | 16,322 | F-32 / F-31 |
| **= Fully diluted, pre-IPO** |  | **16,322** |  |
| IPO primary (ASSUMPTION $25bn) | 277 | 16,599 | ASSUMPTION |
| **= Fully diluted incl. IPO primary** |  | **16,599** |  |
| Google 2026 NPA $20bn | 221 | 16,820 | p.169 |
| Amazon 2026 NPA $15bn | 166 | 16,986 | p.169 |
| Broadcom NPA $42bn @ 90% of price (principal only) | 516 | 17,502 | p.171 |
| AMD put $5bn | 55 | 17,558 | p.167 |
| **= Post-facility (all committed facilities drawn)** |  | **17,558** |  |


- Preferred as-converted from series table: 8,560m vs F-59 anti-dilutive figure 8,559m (D-series ratios explain the gap vs a flat 10:1 = 8,534m).
- Amazon notes check: 1,840m vs filing 1,840m. Fixed conversion prices ($2.09/$5.05) are far below any plausible IPO price, so the IPO price does not change this count. Most of it is likely blocked at IPO by Amazon's 12% cap (see ownership), and the remainder rolls over and converts quarterly. It is counted in full here.
- Options via TSM at $90.37: 1,717m net of 1,774m gross (strike $2.91 is trivial vs price).
- **Dilution vs basic (2,199m):** FD pre-IPO 16,322m = **7.4x basic (+642%)**; FD incl. IPO 16,599m; post-facility 17,558m (+5.8% vs FD incl. IPO); penalty Broadcom case 17,588m.
- Note: the large 'basic -> FD' step is mostly **preferred conversion**: venture money that is already invested and is not new dilution at IPO. The genuinely *new* dilution after IPO is the facilities (+5.8%) plus ongoing SBC and Public Benefit Fund top-ups (up to 2% per +50% share-price milestone, p.146; not modelled).

### Ownership (economic, as-converted)

| Holder group | FD incl. IPO (m) | % | Post-facility (m) | % |
|---|---|---|---|---|
| Co-founders (7, Class A of record) | 1,677 | 10.1% | 1,677 | 9.6% |
| Other common holders (employees, ex-employees, others) | 522 | 3.1% | 522 | 3.0% |
| Employee options (TSM) + RSUs | 2,845 | 17.1% | 2,845 | 16.2% |
| Voting preferred holders (A,C-1,D-1,D-2,E-1,F-1,G-1,H-1) - venture/financial proxy | 4,407 | 26.5% | 4,407 | 25.1% |
| Amazon (identified preferred + rollover notes) | 3,484 | 21.0% | 3,650 | 20.8% |
| Google (identified preferred) | 1,112 | 6.7% | 1,333 | 7.6% |
| Non-voting preferred, holder not disclosed (B, C-2, D-3, part G-2/H-2) | 1,398 | 8.4% | 1,398 | 8.0% |
| Public Benefit Fund | 847 | 5.1% | 847 | 4.8% |
| Other (donation match, holdback, acq.) | 30 | 0.2% | 30 | 0.2% |
| IPO investors (ASSUMPTION $25bn) | 277 | 1.7% | 277 | 1.6% |
| Broadcom / assignee (notes) | 0 | 0.0% | 516 | 2.9% |
| AMD (put) | 0 | 0.0% | 55 | 0.3% |
| **Total** | 16,599 | 100% | 17,558 | 100% |


- **What can and can't be derived:** Amazon and Google holdings are a *floor*: only the series the filing ties to them (note conversions, G-2 tranche, Series H amounts). The principal-stockholders table (p.294) lists only voting holders, so Amazon/Google (non-voting Class N) are not shown with %. Holders of the other non-voting series (B, C-2, D-3, the rest of G-2/H-2) are not disclosed. 'Voting preferred' is a proxy for venture/financial investors and may include strategics. **A precise venture-vs-strategic split can't be derived from the filing.**
- Amazon identified preferred = 1,644m; with all notes converted it would hold 21.0%. The 12% cap would allow only about 145m of the 1,840m note shares to convert at IPO (if Amazon holds nothing else and does not waive the cap). The rest stays as rollover notes.
- Google identified preferred = 1,112m (6.7%); 14.99% cap applies to NPA draws.

## 2. Price per share at market cap

| Market cap | Basic shares | FD incl. IPO | Post-facility (Broadcom 90%) | Post-facility (Broadcom 85%) |
|---|---|---|---|---|
| $1.0tn | $454.66 | $59.84 | $54.55 | $54.38 |
| $1.5tn | $681.99 | $90.37 | $85.08 | $84.91 |
| $2.0tn | $909.33 | $120.90 | $115.60 | $115.44 |


- **Series H:** $589.0095 per preferred share / 10:1 conversion (F-47, ratio verified) = **$58.90 per common share**. At that price, FD pre-IPO shares imply roughly **$0.96tn** (post-money ~ $1.0tn). The $1.5tn FD price of $90.37 is +53% vs Series H.
- Holding market cap fixed while adding facility shares understates value slightly, because those shares are issued for cash ($82bn) that stays on the balance sheet.

## 3. Operating model 2026E–2030E (GAAP)

EPS uses post-facility diluted shares (17,558m: all facilities issued at the $1.5tn FD/IPO price). 2026E = 9M actual + modelled 4Q. 2026 SBC includes the one-off $8.2bn RSU catch-up at IPO.

### Bear ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 51.9 | 86.1 | 95.6 | 101.5 | 107.7 |
|   growth | 1031.8% | 65.9% | 11.0% | 6.2% | 6.1% |
| Compute+infra | 29.5 | 56.3 | 80.7 | 91.3 | 101.6 |
|   % rev | 56.8% | 65.4% | 84.4% | 90.0% | 94.3% |
|   commitment floor binds? | yes | yes | yes | yes | yes |
|   of which cost of revenue | 7.5 | 13.6 | 16.5 | 18.9 | 21.5 |
|   of which training/other | 22.0 | 42.7 | 64.2 | 72.5 | 80.1 |
| Personnel (cash, R&D-ex-compute proxy) | 2.5 | 4.2 | 4.7 | 5.0 | 5.4 |
| S&M & partnerships | 8.6 | 14.2 | 15.6 | 16.4 | 17.2 |
| G&A / other (ex donation) | 5.0 | 8.0 | 8.4 | 8.5 | 8.6 |
| SBC | 13.3 | 21.2 | 19.1 | 6.3 | 5.4 |
| Donation match (non-cash) | 3.3 | 4.5 | 4.0 | 3.1 | 2.2 |
| GAAP operating income | -10.3 | -22.3 | -36.9 | -29.2 | -32.7 |
|   margin | -19.8% | -25.9% | -38.7% | -28.8% | -30.3% |
| Adj. op. income (ex SBC, donation) | 6.3 | 3.4 | -13.9 | -19.8 | -25.1 |
| Interest income | 3.5 | 5.5 | 6.3 | 6.6 | 6.7 |
| Broadcom note PIK interest | 0.0 | 0.7 | 2.1 | 3.8 | 5.6 |
| Tax | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Net income | -6.8 | -17.6 | -32.7 | -26.4 | -31.6 |
| EPS (post-facility, $) | -0.38 | -1.00 | -1.86 | -1.50 | -1.80 |
| FCF | 7.2 | 4.6 | -12.3 | -18.3 | -23.8 |
| Year-end cash (incl. IPO & facility draws) | 156.1 | 181.2 | 189.3 | 191.6 | 188.2 |


### Base ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 53.9 | 121.3 | 176.7 | 216.5 | 242.8 |
|   growth | 1076.2% | 125.0% | 45.7% | 22.5% | 12.1% |
| Compute+infra | 32.8 | 74.0 | 106.0 | 120.0 | 133.5 |
|   % rev | 60.8% | 61.0% | 60.0% | 55.4% | 55.0% |
|   commitment floor binds? | yes | yes | yes | yes | yes |
|   of which cost of revenue | 7.8 | 18.3 | 27.8 | 35.4 | 41.3 |
|   of which training/other | 25.0 | 55.7 | 78.2 | 84.6 | 92.2 |
| Personnel (cash, R&D-ex-compute proxy) | 2.6 | 5.8 | 8.3 | 9.9 | 10.9 |
| S&M & partnerships | 9.0 | 19.1 | 26.2 | 30.1 | 31.6 |
| G&A / other (ex donation) | 5.2 | 10.6 | 13.9 | 15.0 | 14.6 |
| SBC | 13.5 | 24.0 | 24.2 | 11.8 | 9.7 |
| Donation match (non-cash) | 3.4 | 6.2 | 6.9 | 5.8 | 3.6 |
| GAAP operating income | -12.5 | -18.3 | -8.7 | 23.8 | 38.9 |
|   margin | -23.3% | -15.1% | -4.9% | 11.0% | 16.0% |
| Adj. op. income (ex SBC, donation) | 4.3 | 11.9 | 22.4 | 41.5 | 52.2 |
| Interest income | 3.5 | 5.5 | 6.4 | 7.6 | 9.4 |
| Broadcom note PIK interest | 0.0 | 0.2 | 0.7 | 1.3 | 1.9 |
| Tax | 0.0 | 0.0 | 0.0 | 3.2 | 9.7 |
| Net income | -9.0 | -13.1 | -3.0 | 27.0 | 36.7 |
| EPS (post-facility, $) | -0.51 | -0.74 | -0.17 | 1.54 | 2.09 |
| FCF | 5.1 | 11.3 | 20.0 | 35.1 | 39.7 |
| Year-end cash (incl. IPO & facility draws) | 156.1 | 182.6 | 217.9 | 268.2 | 323.2 |


### Thread ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 53.9 | 132.1 | 223.3 | 290.3 | 348.3 |
|   growth | 1076.2% | 145.0% | 69.0% | 30.0% | 20.0% |
| Compute+infra | 32.8 | 74.0 | 115.6 | 143.4 | 163.7 |
|   % rev | 60.8% | 56.0% | 51.8% | 49.4% | 47.0% |
|   commitment floor binds? | yes | yes | no | no | no |
|   of which cost of revenue | 7.8 | 20.0 | 35.1 | 47.5 | 59.2 |
|   of which training/other | 25.0 | 54.0 | 80.5 | 95.9 | 104.5 |
| Personnel (cash, R&D-ex-compute proxy) | 2.6 | 6.3 | 10.4 | 13.3 | 15.7 |
| S&M & partnerships | 9.0 | 20.8 | 33.1 | 40.4 | 45.3 |
| G&A / other (ex donation) | 5.2 | 11.6 | 17.5 | 20.1 | 20.9 |
| SBC | 13.5 | 24.9 | 27.4 | 15.8 | 13.9 |
| Donation match (non-cash) | 3.4 | 6.7 | 8.7 | 7.8 | 5.2 |
| GAAP operating income | -12.5 | -12.1 | 10.5 | 49.5 | 83.6 |
|   margin | -23.3% | -9.1% | 4.7% | 17.1% | 24.0% |
| Adj. op. income (ex SBC, donation) | 4.3 | 19.5 | 46.6 | 73.1 | 102.8 |
| Interest income | 3.5 | 5.5 | 6.6 | 8.6 | 11.1 |
| Broadcom note PIK interest | 0.0 | 0.2 | 0.7 | 1.3 | 1.9 |
| Tax | 0.0 | 0.0 | 0.3 | 11.9 | 19.5 |
| Net income | -9.0 | -6.9 | 16.1 | 44.9 | 73.4 |
| EPS (post-facility, $) | -0.51 | -0.39 | 0.92 | 2.56 | 4.18 |
| FCF | 5.1 | 18.4 | 41.8 | 55.3 | 76.9 |
| Year-end cash (incl. IPO & facility draws) | 156.1 | 189.7 | 246.8 | 317.3 | 409.5 |


### Bull ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 55.3 | 152.3 | 273.3 | 393.3 | 491.9 |
|   growth | 1105.8% | 175.6% | 79.4% | 43.9% | 25.1% |
| Compute+infra | 32.8 | 78.4 | 126.5 | 161.8 | 177.1 |
|   % rev | 59.3% | 51.4% | 46.3% | 41.1% | 36.0% |
|   commitment floor binds? | yes | no | no | no | no |
|   of which cost of revenue | 8.0 | 21.9 | 38.9 | 55.5 | 68.9 |
|   of which training/other | 24.8 | 56.5 | 87.6 | 106.3 | 108.2 |
| Personnel (cash, R&D-ex-compute proxy) | 2.7 | 7.1 | 12.1 | 16.6 | 19.7 |
| S&M & partnerships | 9.2 | 23.2 | 37.8 | 48.8 | 54.1 |
| G&A / other (ex donation) | 5.3 | 13.0 | 20.1 | 24.3 | 24.6 |
| SBC | 13.6 | 26.2 | 29.5 | 18.5 | 14.8 |
| Donation match (non-cash) | 3.5 | 7.6 | 9.9 | 9.1 | 4.9 |
| GAAP operating income | -11.8 | -2.9 | 37.4 | 114.3 | 196.8 |
|   margin | -21.4% | -1.9% | 13.7% | 29.1% | 40.0% |
| Adj. op. income (ex SBC, donation) | 5.3 | 30.8 | 76.9 | 141.9 | 216.4 |
| Interest income | 3.5 | 5.5 | 6.8 | 9.4 | 13.4 |
| Broadcom note PIK interest | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Tax | 0.0 | 0.0 | 6.7 | 26.0 | 44.1 |
| Net income | -8.3 | 2.5 | 37.6 | 97.7 | 166.1 |
| EPS (post-facility, $) | -0.47 | 0.14 | 2.14 | 5.56 | 9.46 |
| FCF | 6.0 | 28.6 | 63.4 | 105.6 | 161.1 |
| Year-end cash (incl. IPO & facility draws) | 156.1 | 194.7 | 268.1 | 383.7 | 554.9 |


Commitment check: the modelled compute line is floored at the assumed annual commitment schedule (2026: $14bn, 2027: $74bn, 2028: $106bn, 2029: $120bn, 2030: $134bn; total $447.5bn to 2030 per p.140, allocation = ASSUMPTION). Where 'floor binds = yes', fixed commitments, not demand, set compute cost.

## 4. Valuation at $1.5tn

EV = $1.5tn - cash $156.1bn (Sep-26 cash + net IPO proceeds) = $1,343.9bn. P/E = IPO price $90.37 / post-facility EPS. IRR for an IPO buyer at the FD price $90.37, exit at 25x 2030E EPS after 4 yrs; PV discounted at 12%.

| Scenario | EV/Sales 27E | EV/Sales 28E | P/E 27E | P/E 28E | EPS 30E | Exit price | PV today | IRR |
|---|---|---|---|---|---|---|---|---|
| Bear | 15.6x | 14.1x | n/m | n/m | $-1.80 | $-45 | $-29 | n/m |
| Base | 11.1x | 7.6x | n/m | n/m | $2.09 | $52 | $33 | -12.8% |
| Thread | 10.2x | 6.0x | n/m | 98x | $4.18 | $104 | $66 | 3.7% |
| Bull | 8.8x | 4.9x | 630x | 42x | $9.46 | $236 | $150 | 27.2% |


## 5. Sensitivity: 2028E EPS ($, post-facility) vs revenue path x total compute % of revenue

| Path (2028E rev) | compute 40% | compute 50% | compute 60% | compute 70% | compute 80% | modelled |
|---|---|---|---|---|---|---|
| Bear ($95.6bn) | 0.55 | 0.01 | -0.53 | -1.08 | -1.62 | -1.86 @ 84.4% |
| Base ($176.7bn) | 1.63 | 0.83 | -0.17 | -1.18 | -2.19 | -0.17 @ 60.0% |
| Thread ($223.3bn) | 2.10 | 1.10 | -0.11 | -1.38 | -2.65 | 0.92 @ 51.8% |
| Bull ($273.3bn) | 2.91 | 1.68 | 0.39 | -1.17 | -2.73 | 2.14 @ 46.3% |


Note: grid cells ignore the commitment floor. The assumed 2028 floor is $106bn, i.e. 60% of Base and 111% of Bear 2028 revenue, so the low-compute cells are not reachable on lower revenue paths without renegotiating or cancelling commitments.
