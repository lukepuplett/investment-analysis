# SpaceX (SPCX)

Public since **12 June 2026** (Nasdaq: SPCX). This folder collects filings and model inputs for Space Exploration Technologies Corp. (CIK **1181412**).

## Model inputs (start here)

**[analysis/2026_11_model_inputs.md](analysis/2026_11_model_inputs.md)** — register of HARD / PROXY / GUESS inputs (canonical sources for the model).
- [Valuation snapshot, 11 Nov 2026](analysis/2026_11_valuation_snapshot.md) — rough multiples on filed Q3 numbers plus a reverse test
- **[Terrestrial scenario model](model/README.md)** — `python3 spcx/model/spcx_model.py` → Bear/Base/Bull revenue, EBIT, FCF, DCF + exit vs **$141.30**; orbital compute excluded (residual line only)

## Saved primary sources

### `filings/`

| File | Description |
|------|-------------|
| [2026_05_20_S-1.htm](filings/2026_05_20_S-1.htm) | Form S-1 |
| [2026_06_01_S-1A.htm](filings/2026_06_01_S-1A.htm) | S-1/A #1 |
| [2026_06_03_S-1A.htm](filings/2026_06_03_S-1A.htm) | S-1/A #2 |
| [2026_06_12_424B4.htm](filings/2026_06_12_424B4.htm) | 424(b)(4) final prospectus |
| [2026_06_05_google_cloud_fwp.htm](filings/2026_06_05_google_cloud_fwp.htm) | Google Cloud Service Agreement FWP (~110k NVIDIA GPUs; $920M/mo) |
| [2026_10_26_gpu_master_lease_8k.htm](filings/2026_10_26_gpu_master_lease_8k.htm) | ~$40B GPU master finance lease commitment (Apollo) |
| [2026_11_10_anthropic_s1a_reference.htm](filings/2026_11_10_anthropic_s1a_reference.htm) | Anthropic S-1/A (SpaceXAI up to $120.5B) |

### `quarterly/`

| File | Description |
|------|-------------|
| [2026_Q2_10q.htm](quarterly/2026_Q2_10q.htm) | Q2 FY2026 Form 10-Q |
| [2026_Q3_10q.htm](quarterly/2026_Q3_10q.htm) | Q3 FY2026 Form 10-Q |
| [2026_Q2_10q_facts.tsv](quarterly/2026_Q2_10q_facts.tsv) | iXBRL numeric extract |
| [2026_Q3_10q_facts.tsv](quarterly/2026_Q3_10q_facts.tsv) | iXBRL numeric extract |
| [2026_Q2_google_cloud_fwp_extract.txt](quarterly/2026_Q2_google_cloud_fwp_extract.txt) | Google FWP text extract |
| [2026_Q3_press_release.htm](quarterly/2026_Q3_press_release.htm) | Q3 FY2026 earnings release (Ex. 99.1) |
| [2026_Q3_earnings_8k.htm](quarterly/2026_Q3_earnings_8k.htm) | Q3 results 8-K |
| [2026_Q2_IPO_pricing_8k.htm](quarterly/2026_Q2_IPO_pricing_8k.htm) | $25B notes pricing |
| [2026_Q2_IPO_closing_8k.htm](quarterly/2026_Q2_IPO_closing_8k.htm) | IPO closing |
| [2026_Q2_senior_notes_8k.htm](quarterly/2026_Q2_senior_notes_8k.htm) | Inaugural notes offering |
| [2026_Q4_event_8k.htm](quarterly/2026_Q4_event_8k.htm) | Board change (Nov 2026) |

## Other references in repo

- [munster-2026-10.md](munster-2026-10.md) — secondary commentary on SPCX / Street revenue expectations
- Alphabet Q3 stake: [goog/quarterly/2026_Q3_10q.htm](../goog/quarterly/2026_Q3_10q.htm) (SpaceX fair value $75.2B)

## Analysis status

| Document | Status |
|----------|--------|
| [analysis/2026_11_model_inputs.md](analysis/2026_11_model_inputs.md) | [x] Input register (Nov 2026) |
| [model/README.md](model/README.md) | [x] Terrestrial scenario model (Nov 2026) |
| Full analysis set per AGENTS.md | [ ] Not started |
