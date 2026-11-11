# SPCX terrestrial model output


**Scope:** Earth-only (Starlink, launch, terrestrial Super Intelligence). 
Orbital compute is **excluded**; residual = market cap minus terrestrial value.


Market reference: **$141.30/share**, 13.581bn shares, 
~$1.92tn market cap ([valuation_snapshot](../analysis/2026_11_valuation_snapshot.md)).


Run `python3 spcx_model.py`. Inputs: `FILING` / `ASSUMPTIONS` at top of script; 
register: [2026_11_model_inputs.md](../analysis/2026_11_model_inputs.md).


**xAI / X:** SI advertising ($538M/qtr HARD) grows inside SI; Grok subscription not separable in 10-Q — folded into SI ads line.


## 1. Segment revenue & profit (terrestrial)


### Bear


| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Total revenue | 41.9 | 60.8 | 61.4 | 66.5 | 74.0 |
|   Connectivity | 18.2 | 22.2 | 25.0 | 28.1 | 31.6 |
|   Space | 5.2 | 5.1 | 6.5 | 7.9 | 9.3 |
|   Super Intelligence | 18.5 | 33.5 | 30.0 | 30.5 | 33.1 |
| EBIT (after corp overhead) | 1.3 | 10.3 | 11.1 | 12.2 | 13.5 |
|   EBIT margin | 3.0% | 16.9% | 18.1% | 18.4% | 18.3% |
| Capex | 67.7 | 41.1 | 58.7 | 70.9 | 72.1 |
| FCF | -58.0 | -21.0 | -33.5 | -37.4 | -27.8 |
| Unlevered FCF | -57.3 | -19.5 | -30.9 | -33.2 | -22.2 |
|   Funding need after lease (2026 = Q4 only) | 17.2 | 12.5 | 20.0 | 20.4 | 10.8 |
|   New debt outstanding (cum) | 12.0 | 20.8 | 34.7 | 49.0 | 56.6 |
|   Equity issued | 5.2 | 3.8 | 6.0 | 6.1 | 3.2 |
|   Shares (m, after issuance) | 13,617 | 13,644 | 13,686 | 13,730 | 13,753 |
| SI nameplate GW (EOY) | 1.7 | 2.2 | 3.0 | 4.0 | 5.0 |


### Base


| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Total revenue | 41.9 | 92.8 | 135.7 | 177.7 | 214.0 |
|   Connectivity | 18.2 | 23.9 | 29.0 | 35.2 | 42.7 |
|   Space | 5.2 | 5.9 | 8.2 | 10.5 | 12.8 |
|   Super Intelligence | 18.5 | 62.9 | 98.5 | 132.0 | 158.4 |
| EBIT (after corp overhead) | 1.3 | 13.8 | 20.6 | 29.6 | 40.0 |
|   EBIT margin | 3.0% | 14.8% | 15.2% | 16.7% | 18.7% |
| Capex | 67.7 | 94.6 | 127.2 | 150.9 | 152.1 |
| FCF | -58.0 | -71.5 | -84.2 | -80.4 | -48.0 |
| Unlevered FCF | -57.3 | -69.0 | -78.3 | -70.7 | -35.2 |
|   Funding need after lease (2026 = Q4 only) | 17.2 | 46.6 | 49.6 | 38.8 | 6.5 |
|   New debt outstanding (cum) | 12.0 | 44.6 | 79.3 | 106.5 | 111.0 |
|   Equity issued | 5.2 | 14.0 | 14.9 | 11.6 | 1.9 |
|   Shares (m, after issuance) | 13,617 | 13,716 | 13,822 | 13,904 | 13,918 |
| SI nameplate GW (EOY) | 1.7 | 3.5 | 6.0 | 9.0 | 12.0 |


### Bull


| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Total revenue | 41.9 | 144.4 | 258.4 | 428.2 | 643.2 |
|   Connectivity | 18.2 | 25.7 | 33.4 | 43.6 | 57.0 |
|   Space | 5.2 | 6.9 | 10.2 | 13.6 | 16.9 |
|   Super Intelligence | 18.5 | 111.8 | 214.8 | 371.0 | 569.3 |
| EBIT (after corp overhead) | 1.3 | 19.7 | 41.2 | 82.5 | 148.8 |
|   EBIT margin | 3.0% | 13.6% | 15.9% | 19.3% | 23.1% |
| Capex | 67.7 | 139.0 | 204.7 | 319.9 | 397.1 |
| FCF | -58.0 | -110.0 | -134.6 | -179.6 | -143.0 |
| Unlevered FCF | -57.3 | -106.7 | -125.7 | -163.5 | -119.0 |
|   Funding need after lease (2026 = Q4 only) | 17.2 | 71.4 | 76.0 | 86.0 | 26.0 |
|   New debt outstanding (cum) | 12.0 | 62.0 | 115.2 | 175.4 | 193.6 |
|   Equity issued | 5.2 | 21.4 | 22.8 | 25.8 | 7.8 |
|   Shares (m, after issuance) | 13,617 | 13,769 | 13,931 | 14,113 | 14,168 |
| SI nameplate GW (EOY) | 1.7 | 5.0 | 10.0 | 18.0 | 28.0 |


## 2. Contracted vs uncontracted SI (Base)


| Year | Google (M) | Anthropic (M) | Merchant SI (M) | GW | Contract+merchant |
|---|---|---|---|---|---|
| 2026 | 11,040 | 20,000 | 1,120 | 1.7 | 32,160 |
| 2027 | 11,040 | 28,000 | 21,280 | 3.5 | 60,320 |
| 2028 | 11,040 | 35,000 | 49,280 | 6.0 | 95,320 |
| 2029 | 8,000 | 37,200 | 82,880 | 9.0 | 128,080 |
| 2030 | 0 | 37,200 | 116,480 | 12.0 | 153,680 |


RPO **$62.96B** HARD supports recognition timing; bear case cuts Google after 2027 and trims Anthropic (90-day cancel rights after 2027 — HARD in Anthropic S-1/A / Google FWP).


## 3. Terrestrial valuation vs $141.30 market


| Scenario | DCF equity/sh | Exit 25×2030 NI PV/sh | Blended 50/50 | Market | Blended vs mkt | Orbital residual |
|---|---|---|---|---|---|---|
| Bear | $-2.8 | $5.9 | $1.6 | $141.30 | -99% | $1.90tn implied orbital/option |
| Base | $-1.8 | $21.7 | $10.0 | $141.30 | -93% | $1.78tn implied orbital/option |
| Bull | $31.1 | $105.9 | $68.5 | $141.30 | -52% | $989bn implied orbital/option |


*Method: DCF is unlevered, at the 30 Sep 2026 balance-sheet date (Q4'26 stub, FY27-30 mid-year, normalised terminal), less net debt -7,288M (debt + drawn lease - cash). Exit lens is 2030 NI x 25x, discounted 4.25 years and scaled for shares issued to fund the gap. The funding gap is financed 70% debt at 7% and the rest equity at $141.30.*


**Implied value left for orbital/option** = market cap − terrestrial blended equity (per scenario). 
Negative terrestrial blended ⇒ market already prices orbital/out-of-model upside in bull segments.


## 4. Sensitivity — 2030 exit value per share ($) vs revenue/GW-yr × GW deployed


| rev\GW | 5 GW | 8 GW | 12 GW | 18 GW | 28 GW |
|---|---|---|---|---|---|
| $8B/GW-yr | $21 | $18 | $15 | $10 | $2 |
| $12B/GW-yr | $22 | $21 | $20 | $17 | $13 |
| $16B/GW-yr | $24 | $24 | $24 | $24 | $24 |
| $20B/GW-yr | $25 | $27 | $28 | $31 | $35 |
| $24B/GW-yr | $26 | $29 | $33 | $38 | $46 |


Cells: exit-lens PV per current share from a full Base-case run (25× 2030 NI, funding cost and dilution included), with 2030 GW and merchant $/GW-yr overridden and GW ramping linearly from 1.7. Merchant GW = deployed − 1.6 contracted.


## 5. Funding & financing hooks


- **Debt** 38,006M HARD; **cash** 51,294M HARD.

- **Apollo GPU lease** up to 40,000M principal HARD (8-K); model assumes gradual draw with SI capex.

- **9M capex** 48,069M HARD; SI dominated (16,444M/qtr Q3).

- Cumulative funding need after lease financing, Q4'26 to 2030: Bear $81bn (debt $57bn, equity $24bn), Base $159bn (debt $111bn, equity $48bn), Bull $277bn (debt $194bn, equity $83bn) (GUESS capex, lease and debt/equity splits). It carries interest and dilution in the valuation above.


## 6. Three biggest drivers (terrestrial vs $141.30)


1. **GW deployed × $/GW-year (merchant + contract utilization)** — filings anchor Google $11B/yr and Anthropic ~$37B/yr at full delivery, but only **1.7 GW** nameplate today (HARD). Bull case needs 10–28 GW terrestrial by 2030 (GUESS) at neocloud-to-hyperscaler yields.

2. **Capex per GW and lease/debt funding** — $38–55B/GW proxies (PROXY) × GW delta drives FCF deeply negative; Apollo **~$40B** lease (HARD) not fully on balance sheet yet.

3. **Starlink profit vs SI ramp** — Q3 op income is **$2.37B/qtr Connectivity vs $0.43B SI** (HARD); market at ~33× run-rate sales prices SI growth contracts already partially in revenue (Customer A/B 51% of Q3 rev, HARD).

