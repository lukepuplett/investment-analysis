# ANT model output (S-1/A No.2, 10 Nov 2026)

All $ in millions unless stated; shares in millions. Run `python3 ant_model.py`. Inputs and sources are at the top of ant_model.py; method in README.md. Base case = the filed $70.00–$78.00 range (midpoint $74.00), no greenshoe.

## 1. The deal (S-1/A No.2)

| Piece | Shares (m) at $74 | $ | Source |
|---|---|---|---|
| Class A sold by Anthropic | 801 | $59.3bn gross at $74 | A2 cover |
| Class A sold by 7 co-founders (3.38m each) | 24 | $1.75bn to founders, not the company | A2 cover / p.301 |
| **Total IPO** | **825** | $57.8bn–$64.35bn gross | A2 cover |
| Greenshoe (company only) | 124 |  | A2 cover |
| PIPE: Google LLC (Class N) | 135.1 | $10.0bn | A2 p.20 |
| PIPE: NVIDIA (Class N) | 135.1 | $10.0bn | A2 p.20 |
| PIPE: AMD (Class N) | 33.8 | $2.5bn | A2 p.20 |
| PIPE: Broadcom (Class N) | 13.5 | $1.0bn | A2 p.20 |
| PIPE: Micron (Class N) | 13.5 | $1.0bn | A2 p.20 |
| PIPE: Microsoft (Class N) | 13.5 | $1.0bn | A2 p.20 |
| PIPE: TSMC Partners (Class N) | 6.8 | $0.5bn | A2 p.20 |
| **PIPE total (Class N, at IPO price)** | **351** | **$26.0bn** | A2 p.20 |


- **Net proceeds to Anthropic** (IPO primary + PIPE, after fees): ~$84.6bn at $74 ($81.4bn at $70, $87.8bn at $78; ±$793m per $1), or ~$93.7bn with the shoe (A2 p.21, p.128).
- The press "up to $64.4bn" is 825m × $78 = $64.35bn **gross IPO proceeds including the founders' secondary**, not net to the company. It excludes the $26bn PIPE.
- Board-affiliated IOIs of up to $303m (Hastings DAF $300m, Liddell trust $3m) are to buy **in this offering**, so they sit inside the 825m, not on top (A2 cover, p.301).
- Pro forma as adjusted cash and short-term investments: $212.7bn (A2 p.131), after ~$3.8bn of RSU tax withholding (51.6m shares × $74 at a 50.90% rate, A2 p.23).

## 2. Share count and implied value

| Layer (at $74) | Shares (m) | Cumulative (m) | Source |
|---|---|---|---|
| **Outstanding after IPO + PIPE** |  | **13,087** | A2 p.21 (incl. 847m PBF, 277m Amazon note shares) |
| Options (gross; TSM nets out only ~3.9%) | 1,774 | 14,861 | A2 p.23 |
| Unvested RSUs at 30 Sep | 1,027 | 15,888 | A2 p.23 |
| RSUs granted after 30 Sep | 47 | 15,935 | A2 p.23 |
| Post-30-Sep acquisition shares (A+N) | 1 | 15,936 | A2 p.24 |
| Matching Issuance (donation match, issued) | 28 | 15,964 | A2 p.24 |
| **= Tighter fully diluted** |  | **15,964** |  |
| Vested Matching Obligation + holdback | 555 | 16,519 | A2 p.24-25 |
| **= + vested donation-match obligation** |  | **16,519** |  |
| Amazon rollover notes (the drip) | 1,564 | 18,083 | A2 p.25 / p.173 |
| Less: options TSM buyback | -70 | 18,013 | A2 p.25 fn1 |
| **= Filing's fully diluted table (A2 p.25)** |  | **18,013** |  |
| Unused 2026 Plan + ESPP reserves | 2,049 | 20,062 | A2 p.24 |
| **= + unused plan reserves (overhang, not day-one)** |  | **20,062** |  |
| Facility: Google 2026 NPA remaining $10bn | 135 | 20,197 | A2 p.173 |
| Facility: Amazon 2026 NPA $15bn | 203 | 20,399 | A2 p.174 |
| Facility: Broadcom NPA $42bn @ 90% (principal only) | 631 | 21,030 | A2 p.175 |
| Facility: AMD commitment remaining $2.5bn | 34 | 21,064 | A2 p.172 |


Filing check: A2 p.25 totals 18,013m; model 18,013m. The facility rows stack on the filing FD (excluding plan reserves) and assume issue at the IPO price; the filing says 30-day VWAP at each draw.

| Basis | Shares at $74 (m) | Value at $70 | Value at $74 | Value at $78 | Mid / $81bn ARR |
|---|---|---|---|---|---|
| Outstanding after deal | 13,087 | $917bn | $968bn | $1.019tn | 12.0x |
| Tighter FD | 15,964 | $1.119tn | $1.181tn | $1.244tn | 14.6x |
| Tighter FD + vested match | 16,519 | $1.158tn | $1.222tn | $1.287tn | 15.1x |
| Filing FD (A2 p.25) | 18,013 | $1.262tn | $1.333tn | $1.404tn | 16.5x |
| Filing FD + plan reserves | 20,062 | $1.405tn | $1.485tn | $1.564tn | 18.3x |
| Filing FD + facilities | 19,015 | $1.336tn | $1.407tn | $1.478tn | 17.4x |


- Press headline (Reuters "up to $1.02tn") multiplies the fixed $74 share count by the range: $916bn / $968bn / $1.021tn. Re-striking the $26bn PIPE at each price moves the low and high ends by under $2bn.
- CNBC's "$1.405tn" at $78 = the filing's own p.25 fully diluted table (18,013m) × $78 = $1.405tn. That table includes all 1.56bn Amazon rollover note shares and the 553m vested donation-match obligation, but **not** the unused 2026 Plan/ESPP reserves.
- Tighter FD adds only shares already granted or issued: options, RSUs, acquisition and matching shares. It leaves out the rollover notes (blocked by the cap) and contingent donation matches.
- Implied Note Capitalization: Amazon's 1,921m / 12% ≈ 16,004m, close to the tighter FD count (derived, not stated).
- ARR multiples: $81bn at 31 Oct (A2 p.203), up $10bn from 30 Sep. 3Q26 revenue annualised is $67.8bn, so midpoint outstanding value is 14.3x that.

## 3. Amazon notes and the 12% cap (the drip)

| Notes | Principal | Conv. price | Shares if uncapped (m) | Converts at IPO | Left as rollover notes | Maturity |
|---|---|---|---|---|---|---|
| 2023 NPA | $2,186m | $2.0928 | 1,045 | $579.3m / 277m | $1,606.7m / 768m | Mar 2034 |
| 2024 NPA | $4,017m | $5.0478 | 796 | — | $4,017m / 796m | Jan/May/Nov 2035 |
| **Total** | **$6,203m** |  | **1,840** | **$579.3m / 277m** | **$5,624m / 1,564m** |  |


- Amazon **elected not to waive** the 12% cap (A2 p.62, p.172). After the IPO conversion it holds 1,921m Class N (14.7% of outstanding), and Google holds 1,790m (13.7%) after its $10bn PIPE (A2 p.120–121).
- The rollover notes are non-interest-bearing. They try to convert at each fiscal quarter-end at the **lowest of the fixed price, the IPO price and the 10-day VWAP**, up to the cap. Anything still unconverted is repaid in cash at maturity, or Amazon can set it off against amounts it owes Anthropic (A2 p.173–174). At any price above $5.05 the fixed prices apply.
- Fully converted with no cap, the notes would be 12.6% of total common and 25.5% of Class N after the deal (A2 p.62). At $74 they are worth ~$116bn for ~$5.62bn of principal; the pro forma balance sheet carries them at $110.9bn fair value (A2 p.131).
- **Drip arithmetic (derived):** at the cap, Amazon can convert only ~12–13.6% of any new non-Amazon capitalization (12/88 if the unconverted notes sit outside the cap base, 12% if they are inside it; the filing does not say which, so the model uses 12/88). Clearing all 1,564m would need ~11,467m of new shares issued to others. At an ASSUMED 60m a quarter of other issuance, about 8.2m convert per quarter, leaving 1,531m / 1,498m / 1,465m / 1,433m after 1/2/3/4 years. Amazon's own $15bn 2026 NPA draws use the same cap headroom. In practice the notes clear faster only if Amazon sells Class N (which converts to Class A on transfer), the cap base grows faster, or Amazon waives the cap.

## 4. Price per share at $1.0tn / $1.5tn / $2.0tn

| Market cap | Outstanding | Tighter FD | Filing FD | Filing FD + facilities |
|---|---|---|---|---|
| $1.0tn | $76.48 | $62.38 | $55.22 | $51.04 |
| $1.5tn | $115.74 | $94.41 | $83.42 | $79.24 |
| $2.0tn | $155.00 | $126.43 | $111.62 | $107.44 |


- **Series H:** $589.0095 per preferred share / 10 = **$58.90 per common share** (S-1/A No.1 F-47). The range is +19% to +32% above Series H. Series H × the 9 Nov ~16.9bn FD was ≈ $1.0tn, and Series H × today's tighter FD is $940bn.
- **Against Luke's earlier view (29 Oct: ~$1.5tn, more likely $2tn, then doubling on day one):** the top of the range is $1.019tn on outstanding and $1.244tn on tighter FD. $1.5tn needs $116 a share on outstanding ($94 on tighter FD), +48% above the top of the range. $2tn needs $155 (+99% vs $78). A day-one double from $74 to $148 would be $1.911tn on outstanding, so the $2tn idea now rests on the first-day pop, not on the IPO price.

## 5. Operating model 2026E–2030E (GAAP)

EPS uses the filing FD plus all remaining facilities issued at $74 (19,015m). 2026E = 9M actual + modelled 4Q, and 2026 cash includes $80.8bn of net IPO + PIPE proceeds after RSU withholding (A2 p.131). 2026 SBC includes the one-off $8.2bn RSU catch-up at IPO.

ARR check: if revenue simply held at the 31 Oct run-rate, 4Q26 would be ~$20.2bn (+19% QoQ). Bear 4Q26 = $18.7bn, Base 4Q26 = $20.7bn, Bull 4Q26 = $22.0bn. Bear now sits below a flat October run-rate. The growth paths are unchanged from 9 Nov.

### Bear ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 51.9 | 86.1 | 95.6 | 101.5 | 107.7 |
|   growth | 1031.8% | 65.9% | 11.0% | 6.2% | 6.1% |
| Compute+infra | 30.7 | 58.7 | 84.1 | 95.2 | 108.4 |
|   % rev | 59.2% | 68.2% | 88.0% | 93.8% | 100.6% |
|   commitment floor binds? | yes | yes | yes | yes | yes |
|   of which cost of revenue | 7.5 | 13.6 | 16.5 | 18.9 | 21.5 |
|   of which training/other | 23.2 | 45.1 | 67.6 | 76.3 | 86.8 |
| Personnel (cash, R&D-ex-compute proxy) | 2.5 | 4.2 | 4.7 | 5.0 | 5.4 |
| S&M & partnerships | 8.6 | 14.2 | 15.6 | 16.4 | 17.2 |
| G&A / other (ex donation) | 5.0 | 8.0 | 8.4 | 8.5 | 8.6 |
| SBC | 13.3 | 21.2 | 19.1 | 6.3 | 5.4 |
| Donation match (non-cash) | 3.3 | 4.5 | 4.0 | 3.1 | 2.2 |
| GAAP operating income | -11.5 | -24.7 | -40.3 | -33.1 | -39.4 |
|   margin | -22.2% | -28.7% | -42.2% | -32.6% | -36.6% |
| Adj. op. income (ex SBC, donation) | 5.0 | 1.0 | -17.3 | -23.7 | -31.9 |
| Interest income | 3.5 | 7.4 | 8.2 | 8.3 | 8.2 |
| Broadcom note PIK interest | 0.0 | 0.7 | 2.1 | 3.8 | 5.6 |
| Tax | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Net income | -8.0 | -17.9 | -34.3 | -28.5 | -36.8 |
| EPS (filing FD + facilities, $) | -0.42 | -0.94 | -1.80 | -1.50 | -1.94 |
| FCF | 5.9 | 4.2 | -13.8 | -20.4 | -29.1 |
| Year-end cash (incl. IPO, PIPE & facility draws) | 212.7 | 234.2 | 237.7 | 234.7 | 223.0 |


### Base ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 53.9 | 121.3 | 176.7 | 216.5 | 242.8 |
|   growth | 1076.2% | 125.0% | 45.7% | 22.5% | 12.1% |
| Compute+infra | 33.8 | 74.0 | 106.0 | 120.0 | 136.6 |
|   % rev | 62.7% | 61.0% | 60.0% | 55.4% | 56.3% |
|   commitment floor binds? | yes | yes | yes | yes | yes |
|   of which cost of revenue | 7.8 | 18.3 | 27.8 | 35.4 | 41.3 |
|   of which training/other | 26.0 | 55.7 | 78.2 | 84.6 | 95.3 |
| Personnel (cash, R&D-ex-compute proxy) | 2.6 | 5.8 | 8.3 | 9.9 | 10.9 |
| S&M & partnerships | 9.0 | 19.1 | 26.2 | 30.1 | 31.6 |
| G&A / other (ex donation) | 5.2 | 10.6 | 13.9 | 15.0 | 14.6 |
| SBC | 13.5 | 24.0 | 24.2 | 11.8 | 9.7 |
| Donation match (non-cash) | 3.4 | 6.2 | 6.9 | 5.8 | 3.6 |
| GAAP operating income | -13.5 | -18.3 | -8.7 | 23.8 | 35.8 |
|   margin | -25.1% | -15.1% | -4.9% | 11.0% | 14.7% |
| Adj. op. income (ex SBC, donation) | 3.3 | 11.9 | 22.4 | 41.5 | 49.1 |
| Interest income | 3.5 | 7.4 | 8.3 | 9.5 | 11.2 |
| Broadcom note PIK interest | 0.0 | 0.2 | 0.7 | 1.3 | 1.9 |
| Tax | 0.0 | 0.0 | 0.0 | 3.6 | 9.5 |
| Net income | -10.0 | -11.1 | -1.1 | 28.5 | 35.7 |
| EPS (filing FD + facilities, $) | -0.53 | -0.58 | -0.06 | 1.50 | 1.88 |
| FCF | 4.1 | 13.2 | 21.9 | 36.6 | 38.7 |
| Year-end cash (incl. IPO, PIPE & facility draws) | 212.7 | 238.0 | 272.1 | 320.8 | 371.7 |


### Thread ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 53.9 | 132.1 | 223.3 | 290.3 | 348.3 |
|   growth | 1076.2% | 145.0% | 69.0% | 30.0% | 20.0% |
| Compute+infra | 33.8 | 74.0 | 115.6 | 143.4 | 163.7 |
|   % rev | 62.7% | 56.0% | 51.8% | 49.4% | 47.0% |
|   commitment floor binds? | yes | yes | no | no | no |
|   of which cost of revenue | 7.8 | 20.0 | 35.1 | 47.5 | 59.2 |
|   of which training/other | 26.0 | 54.0 | 80.5 | 95.9 | 104.5 |
| Personnel (cash, R&D-ex-compute proxy) | 2.6 | 6.3 | 10.4 | 13.3 | 15.7 |
| S&M & partnerships | 9.0 | 20.8 | 33.1 | 40.4 | 45.3 |
| G&A / other (ex donation) | 5.2 | 11.6 | 17.5 | 20.1 | 20.9 |
| SBC | 13.5 | 24.9 | 27.4 | 15.8 | 13.9 |
| Donation match (non-cash) | 3.4 | 6.7 | 8.7 | 7.8 | 5.2 |
| GAAP operating income | -13.5 | -12.1 | 10.5 | 49.5 | 83.6 |
|   margin | -25.1% | -9.1% | 4.7% | 17.1% | 24.0% |
| Adj. op. income (ex SBC, donation) | 3.3 | 19.5 | 46.6 | 73.1 | 102.8 |
| Interest income | 3.5 | 7.4 | 8.6 | 10.5 | 12.9 |
| Broadcom note PIK interest | 0.0 | 0.2 | 0.7 | 1.3 | 1.9 |
| Tax | 0.0 | 0.0 | 0.7 | 12.3 | 19.9 |
| Net income | -10.0 | -4.9 | 17.7 | 46.4 | 74.8 |
| EPS (filing FD + facilities, $) | -0.53 | -0.26 | 0.93 | 2.44 | 3.93 |
| FCF | 4.1 | 20.3 | 43.4 | 56.8 | 78.4 |
| Year-end cash (incl. IPO, PIPE & facility draws) | 212.7 | 245.1 | 300.6 | 369.6 | 460.1 |


### Bull ($bn unless %)

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Revenue | 55.3 | 152.3 | 273.3 | 393.3 | 491.9 |
|   growth | 1105.8% | 175.6% | 79.4% | 43.9% | 25.1% |
| Compute+infra | 33.8 | 78.4 | 126.5 | 161.8 | 177.1 |
|   % rev | 61.2% | 51.4% | 46.3% | 41.1% | 36.0% |
|   commitment floor binds? | yes | no | no | no | no |
|   of which cost of revenue | 8.0 | 21.9 | 38.9 | 55.5 | 68.9 |
|   of which training/other | 25.8 | 56.5 | 87.6 | 106.3 | 108.2 |
| Personnel (cash, R&D-ex-compute proxy) | 2.7 | 7.1 | 12.1 | 16.6 | 19.7 |
| S&M & partnerships | 9.2 | 23.2 | 37.8 | 48.8 | 54.1 |
| G&A / other (ex donation) | 5.3 | 13.0 | 20.1 | 24.3 | 24.6 |
| SBC | 13.6 | 26.2 | 29.5 | 18.5 | 14.8 |
| Donation match (non-cash) | 3.5 | 7.6 | 9.9 | 9.1 | 4.9 |
| GAAP operating income | -12.8 | -2.9 | 37.4 | 114.3 | 196.8 |
|   margin | -23.2% | -1.9% | 13.7% | 29.1% | 40.0% |
| Adj. op. income (ex SBC, donation) | 4.3 | 30.8 | 76.9 | 141.9 | 216.4 |
| Interest income | 3.5 | 7.4 | 8.8 | 11.3 | 15.2 |
| Broadcom note PIK interest | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Tax | 0.0 | 0.0 | 7.5 | 26.4 | 44.5 |
| Net income | -9.3 | 4.5 | 38.7 | 99.2 | 167.5 |
| EPS (filing FD + facilities, $) | -0.49 | 0.24 | 2.03 | 5.21 | 8.81 |
| FCF | 5.0 | 30.6 | 64.5 | 107.1 | 162.6 |
| Year-end cash (incl. IPO, PIPE & facility draws) | 212.7 | 250.2 | 321.5 | 435.5 | 605.0 |


Commitment check: compute is floored at the assumed annual schedule (2026: $15.0bn, 2027: $74.0bn, 2028: $106.0bn, 2029: $120.0bn, 2030: $136.6bn; total $451.6bn to 2030 per A2 p.144, allocation = ASSUMPTION). Where 'floor binds = yes', fixed commitments, not demand, set compute cost.

## 6. Valuation at the IPO range

| IPO price | Mkt cap (outstanding) | Tighter FD value | EV (outstanding less pro forma cash) | Mkt cap / ARR | EV / Base 27E sales | EV / Base 28E sales |
|---|---|---|---|---|---|---|
| $70 | $917bn | $1.119tn | $708bn | 11.3x | 5.8x | 4.0x |
| $74 | $968bn | $1.181tn | $756bn | 12.0x | 6.2x | 4.3x |
| $78 | $1.019tn | $1.244tn | $803bn | 12.6x | 6.6x | 4.5x |


EV treats the Amazon rollover notes as equity (they settle in shares), not as the $110.9bn fair-value liability on the pro forma balance sheet.

IPO buyer at the $74 midpoint; P/E on filing-FD-plus-facilities EPS; exit at 25x 2030E EPS after 4 years; PV at 12%.

| Scenario | P/E 27E | P/E 28E | EPS 30E | Exit price | PV today | IRR from $74 |
|---|---|---|---|---|---|---|
| Bear | n/m | n/m | $-1.94 | $-48 | $-31 | n/m |
| Base | n/m | n/m | $1.88 | $47 | $30 | -10.8% |
| Thread | n/m | 80x | $3.93 | $98 | $62 | 7.4% |
| Bull | 313x | 36x | $8.81 | $220 | $140 | 31.3% |


## 7. Sensitivity: 2028E EPS ($) vs revenue path × total compute % of revenue

| Path (2028E rev) | compute 40% | compute 50% | compute 60% | compute 70% | compute 80% | modelled |
|---|---|---|---|---|---|---|
| Bear ($95.6bn) | 0.61 | 0.11 | -0.40 | -0.90 | -1.40 | -1.80 @ 88.0% |
| Base ($176.7bn) | 1.59 | 0.85 | -0.06 | -0.99 | -1.92 | -0.06 @ 60.0% |
| Thread ($223.3bn) | 2.02 | 1.09 | 0.00 | -1.17 | -2.35 | 0.93 @ 51.8% |
| Bull ($273.3bn) | 2.75 | 1.61 | 0.46 | -0.98 | -2.42 | 2.03 @ 46.3% |


Note: grid cells ignore the commitment floor. The assumed 2028 floor is $106bn, i.e. 60% of Base and 111% of Bear 2028 revenue.
