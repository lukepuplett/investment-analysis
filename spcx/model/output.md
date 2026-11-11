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
| Capex | 51.2 | 41.1 | 58.7 | 70.9 | 72.1 |
| FCF | -39.0 | -21.0 | -32.8 | -35.7 | -25.5 |
|   Funding need (if FCF<0) | 39.0 | 21.0 | 32.8 | 35.7 | 25.5 |
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
| Capex | 51.2 | 94.6 | 127.2 | 150.9 | 152.1 |
| FCF | -39.0 | -70.4 | -81.0 | -75.2 | -42.0 |
|   Funding need (if FCF<0) | 39.0 | 70.4 | 81.0 | 75.2 | 42.0 |
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
| Capex | 51.2 | 139.0 | 204.7 | 319.9 | 397.1 |
| FCF | -39.0 | -108.1 | -129.2 | -170.1 | -130.7 |
|   Funding need (if FCF<0) | 39.0 | 108.1 | 129.2 | 170.1 | 130.7 |
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
| Bear | $1.4 | $10.3 | $5.9 | $141.30 | -96% | $1.84tn implied orbital/option |
| Base | $12.4 | $31.5 | $22.0 | $141.30 | -84% | $1.62tn implied orbital/option |
| Bull | $87.5 | $129.7 | $108.6 | $141.30 | -23% | $445bn implied orbital/option |


**Implied value left for orbital/option** = market cap − terrestrial blended equity (per scenario). 
Negative terrestrial blended ⇒ market already prices orbital/out-of-model upside in bull segments.


## 4. Sensitivity — 2030 exit value per share ($) vs revenue/GW-yr × GW deployed


| rev\GW | 5 GW | 8 GW | 12 GW | 18 GW | 28 GW |
|---|---|---|---|---|---|
| $8B/GW-yr | $7 | $9 | $12 | $16 | $23 |
| $12B/GW-yr | $8 | $11 | $15 | $22 | $32 |
| $16B/GW-yr | $9 | $13 | $19 | $27 | $41 |
| $20B/GW-yr | $10 | $15 | $23 | $33 | $51 |
| $24B/GW-yr | $11 | $18 | $26 | $39 | $60 |


Cells: stylized 2030 exit (25× NI) holding Base Starlink/Space; merchant GW = deployed − 1.6 contracted. **GUESS** interest/corp costs.


## 5. Funding & financing hooks


- **Debt** 38,006M HARD; **cash** 51,294M HARD.

- **Apollo GPU lease** up to 40,000M principal HARD (8-K); model assumes gradual draw with SI capex.

- **9M capex** 48,069M HARD; SI dominated (16,444M/qtr Q3).

- Cumulative terrestrial funding need (negative FCF years): Bear $154bn, Base $308bn, Bull $577bn (GUESS capex/lease splits).


## 6. Three biggest drivers (terrestrial vs $141.30)


1. **GW deployed × $/GW-year (merchant + contract utilization)** — filings anchor Google $11B/yr and Anthropic ~$37B/yr at full delivery, but only **1.7 GW** nameplate today (HARD). Bull case needs 10–28 GW terrestrial by 2030 (GUESS) at neocloud-to-hyperscaler yields.

2. **Capex per GW and lease/debt funding** — $38–55B/GW proxies (PROXY) × GW delta drives FCF deeply negative; Apollo **~$40B** lease (HARD) not fully on balance sheet yet.

3. **Starlink profit vs SI ramp** — Q3 op income is **$2.37B/qtr Connectivity vs $0.43B SI** (HARD); market at ~33× run-rate sales prices SI growth contracts already partially in revenue (Customer A/B 51% of Q3 rev, HARD).

