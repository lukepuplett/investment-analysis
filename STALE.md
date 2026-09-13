# Data Staleness Table

**Last updated: 2026-09-13**

This table tracks how current each covered company's data is, based on the latest quarterly/period document present in its `quarterly/` or `financials/` directory. Regenerate periodically (suggest monthly, or before any cross-portfolio review) by checking the latest filename/period in each ticker folder against the current date.

Sorted most stale → most current as of the last-updated date above.

**Held?** = whether this is an active position, as distinct from a name we merely research/watch. Confirmed by the user as of 2026-09-12: **held** = SMCI, GTLB, INTC, CSCO, AMAT, GLW, KLIC, CLOUDFLARE/NET, TT, RKLB, HOOD, ENR.DE, DDOG, CRWV, ASML, DRO, AMZN, SPCE, MSFT, RYCEY, TSLA, GOOG; **not held (watchlist)** = MNTN, DUK, CAT, CVCO, LASE. All other rows remain unconfirmed ("—").

| Ticker | Company | Held? | Latest Period on File | Source Doc | Staleness |
|--------|---------|-------|------------------------|------------|-----------|
| **LASE** | Laser Photonics | No (watchlist) | Q2 2026 (6/30/2026) | `financials/2026_09/income_statement.md` | Recent — refreshed with Q1+Q2 2026 10-Q data |
| **RYCEY** | Rolls-Royce | Yes | H2 2025 (semi-annual reporter) | `2025_H2_earnings_call.txt` | ⚠️ Very stale — pre-2026 |
| **MSFT** | Microsoft | Yes | FY2025 Q2 (ended ~Dec 2024) | `2025_Q2_press_release.txt` | ⚠️ Very stale — ~3 quarters behind current FY2026 Q4 |
| **MNTN** | MNTN | No (watchlist) | 2025 Q2 | `2025_Q2_presentation.md` | ⚠️ Very stale |
| **SPCE** | Virgin Galactic | Yes | 2025 Q2 | `2025_Q2_press_release.txt` | ⚠️ Very stale |
| **DUK** | Duke Energy | No (watchlist) | 2025 Q2 | `2025_Q2_transcript.txt` | ⚠️ Very stale |
| **FLR** | Fluor | — | 2025 Q2 | `2025_Q2_presentation.txt` | ⚠️ Very stale |
| **CAT** | Caterpillar | No (watchlist) | 2025 Q2 | `2025_Q2_financial_review_presentation.md` | ⚠️ Very stale |
| **CVCO** | Cavco Industries | No (watchlist) | FY2026 Q2 (~Sep 2025) | `2025_Q2_transcript.txt` | ⚠️ Very stale |
| **AMZN** | Amazon | Yes | 2025 Q3 | `2025_Q3_10Q_summary.md` | Stale (partial coverage — summary only, no 10-Q/facts) |
| **DASH** | DoorDash | — | 2025 Q3 | `2025_Q3_press_release.md` | Stale |
| **DRO** | DroneShield | Yes | 2025 Q3 | `2025_Q3_press_release.txt` | Stale |
| **LYB** | LyondellBasell | — | 2025 Q3 | `2025_Q3_press_release.txt` | Stale |
| **NEE** | NextEra Energy | — | 2025 Q3 | `2025_Q3_presentation.md` | Stale |
| **ADBE** | Adobe | — | FY2025 Q3 (~Aug 2025) | `2025_Q3_earnings_call_transcript.txt` | Stale |
| **CBT** | Cabot | — | FY2025 Q4 (~Sep 2025) | `2025_Q4_press_release.md` | Stale |
| **JCI** | Johnson Controls | — | FY2025 Q4 (~Sep 2025) | `2025_Q4_earnings_summary.md` | Stale |
| **EMR** | Emerson | — | FY2025 Q4 (~Sep 2025) | `2025_Q4_earnings_summary.md` | Stale |
| **ASML** | ASML | Yes | 2026 Q1 | `2026_Q1_earnings_transcript.txt` | Recent |
| **CRWV** | CoreWeave | Yes | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **DDOG** | Datadog | Yes | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **ENR.DE** | Siemens Energy | Yes | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **GRRR** | Gorilla Technology | — | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **HOOD** | Robinhood | Yes | 2026 Q1 | `2026_Q1_earnings_call_transcript.txt` | Recent |
| **IBM** | IBM | — | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **PLAB** | Photronics | — | FY2026 Q1 | `2026_Q1_earnings_call_transcript.txt` | Recent |
| **RKLB** | Rocket Lab | Yes | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **TT** | Trane Technologies | Yes | 2026 Q1 | `2026_Q1_press_release.txt` | Recent |
| **NET** | Cloudflare (`cloudflare/`) | Yes | 2026 Q1 | `2026_Q1_earnings_call_analysis.md` | Recent |
| **AMAT** | Applied Materials | Yes | FY2026 Q2 | `2026_Q2_press_release.txt` | Fresh |
| **GLW** | Corning | Yes | 2026 Q2 | `2026_Q2_earnings_call_transcript.txt` | Fresh |
| **KLIC** | Kulicke & Soffa | Yes | FY2026 Q2 | `2026_Q2_earnings_call.txt` | Fresh |
| **PH** | Parker-Hannifin | — | FY2026 Q2 | `2026_Q2_earnings_call_transcript.md` | Fresh |
| **INTC** | Intel | Yes | Q2 2026 (ended 6/27/26) | `financials/2026_06/income_statement.md` | Fresh |
| **GOOG** | Alphabet | Yes | Q2 2026 (ended 6/30/26) | `quarterly/2026_Q2_10q.htm` / `financials/2026_06/` | Fresh |
| **TSLA** | Tesla | Yes | Q2 2026 (ended 6/30/26) | `quarterly/2026_Q2_10q.htm` / `financials/2026_06/` | Fresh |
| **CSCO** | Cisco | Yes | FY2026 Q4 (ended ~Jul 2026) | `2026_Q4_press_release.htm` | Fresh — most recent fiscal quarter closed |
| **GTLB** | GitLab | Yes | FY2026 Q4 (~Jan 2026 FYE) | `2026_Q4_earnings_call.txt` | Fresh |
| **SMCI** | Super Micro Computer | Yes | 2026 Q3 | `2026_Q3_earnings_call.txt` | ✅ Most current — matches present calendar quarter |

## Notes

- Several tickers (ADBE, CSCO, GTLB, EMR, JCI, PH, MSFT, CVCO, AMAT, KLIC, PLAB) run non-calendar fiscal years, so "Q#" labels don't map directly to calendar quarters — staleness above is a rough proxy, not exact days-since-filing.
- **GOOG** and **TSLA** were refreshed on 2026-09-12 (10-Q + FMP-sourced financials for Q2 2026, period ended 6/30/26). They still only have the raw filing + `financials/` — no `analysis/` documents yet (market, competitive, thesis, etc. per the standard 7-doc workflow). GOOG's Q2 2026 income statement carries a ~$98B non-cash "other income" item that skews TTM net margin/P/E in `financials/2026_06/yahoo_stats.md` — verify against the 10-Q MD&A before using in valuation. FMP rejected the `GOOG` ticker directly; `GOOGL` was used instead (economically equivalent for fundamentals).
- **NET/Cloudflare** now uses single `cloudflare/` folder (Q1 2026 latest; Q4 2025 historical materials preserved under `analysis/2025_12_*` and `financials/2025_12/`). The legacy `net/` folder was removed 2026-09-13.
- **Held? column**: populated from the user's confirmed holdings list (2026-09-12). Ask before assuming a ticker not on that list is or isn't an active position.
- **Refresh priority among held names** (staleness-ranked): RYCEY (H2 2025) > MSFT (FY2025 Q2) > SPCE (2025 Q2) > AMZN/DRO (2025 Q3). GOOG/TSLA refreshed 2026-09-12. NET refreshed Q1 2026.

## How to regenerate

For each ticker folder, find the most recent file in `quarterly/` matching `YYYY_Q#_*` (or the latest dated subfolder in `financials/` if `quarterly/` is empty/sparse), compare its period to the current date, and re-rank from most to least stale.
