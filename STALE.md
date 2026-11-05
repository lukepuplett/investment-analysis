# Data Staleness Table

**Last updated: 2026-11-05**

This table tracks how current each covered company's data is, based on the latest quarterly/period document present in its `quarterly/` or `financials/` directory. Regenerate periodically (suggest monthly, or before any cross-portfolio review) by checking the latest filename/period in each ticker folder against the current date.

Sorted most stale → most current as of the last-updated date above.

**Held?** = whether this is an active position, as distinct from a name we merely research/watch. Confirmed / updated by the user as of **2026-09-18** (interest open): **held** = AAPL, AMAT, AMZN, ASML, AVGO, CLOUDFLARE/NET, CRWV, CSCO, DDOG, DRO, ENR.DE, GLW, GOOG, GTLB, HOOD, INTC, KLIC, MSFT, NVDA, PH, RKLB, RYCEY, SMCI, SPCE, TSLA, TT; **not held (watchlist)** = MNTN, DUK, CAT, CVCO, LASE. Sep 2026 additions / explicit confirms vs 2026-09-12 list: **AVGO, NVDA, AAPL, PH**. Prior held names (CSCO, GLW, CLOUDFLARE/NET, DRO, AMZN, SPCE, etc.) retained — user said *add*, not replace. `aapl/` folder created 2026-11-03 (FQ4 FY26 delta note; no full thesis doc yet) (AVGO added 2026-09-28; **NVDA** added 2026-10-02).


| Ticker | Company | Held? | Latest Period on File | Source Doc | Staleness |
|--------|---------|-------|------------------------|------------|-----------|
| **NVDA** | NVIDIA | Yes | FY2027 Q2 (7/26/2026) | `nvda/quarterly/2026_Q2_summary.txt` / `2026_Q2_10q.htm` | ✅ Fresh — first-pass Oct 2026; Q2 rev $96.2B; Q3 guide $108B; next print ~Nov 18, 2026 |
| **AVGO** | Broadcom | Yes | FY2026 Q3 (8/2/2026) | `avgo/quarterly/2026_Q3_summary.txt` / `2026_Q3_10q.htm` | ✅ Fresh — first-pass Sep 2026; Q3 record revenue/FCF; AI semi $16.7B |
| **MRNA** | Moderna | No (watchlist / interest) | Q2 2026 (6/30/2026) | `mrna/quarterly/2026_Q2_summary.txt` | ✅ Fresh — first-pass Sep 2026; Ph3 INT melanoma Aug 19; **Q3 print expected ~6 Nov 2026** (FMP calendar; no Item 2.02 as of 5 Nov morning) |
| **LASE** | Laser Photonics | No (watchlist) | Q2 2026 (6/30/2026) | `financials/2026_09/income_statement.md`; `2026-11-pre-Q3-update.md` (Oct 8-Ks) | Recent — Q3 not yet printed; **confirmed 12 Nov 2026 BMO**; Oct: founder Nikitin Exec Chair, CFO permanent, Nasdaq $1 bid notice (cure by 19 Apr 2027) |
| **RYCEY** | Rolls-Royce | Yes | H1 2026 (30 Jul 2026) | `quarterly/2026_H1_results.txt` | ✅ Fresh — H1 2026 results; FY26 guidance raised |
| **MSFT** | Microsoft | Yes | FY2027 Q1 (9/30/2026) | `2026-10-FY27Q1-delta.md` (8-K; 10-Q not yet reconciled) | ✅ Fresh — FY27 Q1 printed 28 Oct 2026 |
| **MNTN** | MNTN | No (watchlist) | 2025 Q2 | `2025_Q2_presentation.md` | ⚠️ Very stale |
| **SPCE** | Virgin Galactic | Yes | Q2 2026 (6/30/2026) | `quarterly/2026_Q2_summary.txt` | ✅ Fresh — Q2 2026 data; going concern, $286M cash |
| **DUK** | Duke Energy | No (watchlist) | 2025 Q2 | `2025_Q2_transcript.txt` | ⚠️ Very stale |
| **FLR** | Fluor | — | 2025 Q2 | `2025_Q2_presentation.txt` | ⚠️ Very stale |
| **CAT** | Caterpillar | No (watchlist) | 2025 Q2 | `2025_Q2_financial_review_presentation.md` | ⚠️ Very stale |
| **CVCO** | Cavco Industries | No (watchlist) | FY2026 Q2 (~Sep 2025) | `2025_Q2_transcript.txt` | ⚠️ Very stale |
| **AAPL** | Apple | Yes | FY2026 Q4 (9/26/2026) | `aapl/2026-11-Q4FY26-delta.md` (8-K Ex 99.1; 10-K not yet reconciled) | ✅ Fresh — FQ4 printed 2 Nov 2026; rev $114.5B (+12%), iPhone +17.5%, FY FCF ~$136B; no thesis doc yet |
| **AMZN** | Amazon | Yes | Q3 2026 (9/30/2026) | `2026-10-Q3-delta.md` (8-K Ex 99.1; 10-Q not yet reconciled) | ✅ Fresh — Q3 printed 29 Oct 2026; AWS +39%, OI $28.1B |
| **DASH** | DoorDash | — | 2025 Q3 | `2025_Q3_press_release.md` | Stale |
| **DRO** | DroneShield | Yes | 1H 2026 (30 Jun 2026) | `quarterly/2026_H1_4d_notes.md` | Fresh |
| **LYB** | LyondellBasell | — | 2025 Q3 | `2025_Q3_press_release.txt` | Stale |
| **NEE** | NextEra Energy | — | 2025 Q3 | `2025_Q3_presentation.md` | Stale |
| **ADBE** | Adobe | — | FY2025 Q3 (~Aug 2025) | `2025_Q3_earnings_call_transcript.txt` | Stale |
| **CBT** | Cabot | — | FY2025 Q4 (~Sep 2025) | `2025_Q4_press_release.md` | Stale |
| **JCI** | Johnson Controls | — | FY2025 Q4 (~Sep 2025) | `2025_Q4_earnings_summary.md` | Stale |
| **EMR** | Emerson | — | FY2025 Q4 (~Sep 2025) | `2025_Q4_earnings_summary.md` | Stale |
| **ASML** | ASML | Yes | 2026 Q1 | `2026_Q1_earnings_transcript.txt` | Recent |
| **CRWV** | CoreWeave | Yes | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **DDOG** | Datadog | Yes | Q3 2026 (9/30/2026) | `ddog/2026-11-Q3-delta.md` (8-K Ex 99.1; 10-Q filed 4 Nov, not yet reconciled) | ✅ Fresh — Q3 printed 4 Nov 2026; rev $1.197B (+35%), non-GAAP EPS $0.81; Q4 guide ~flat seq → −14% tape |
| **ENR.DE** | Siemens Energy | Yes | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **GRRR** | Gorilla Technology | — | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **HOOD** | Robinhood | Yes | Q3 2026 (9/30/2026) | `hood/2026_10_27_q3_2026_results.md` | ✅ Fresh — Q3 note already filed (SHA 0d4cb79 cluster); next LASE-related watch is separate |
| **IBM** | IBM | — | 2026 Q1 | `2026_Q1_earnings_call.txt` | Recent |
| **PLAB** | Photronics | — | FY2026 Q1 | `2026_Q1_earnings_call_transcript.txt` | Recent |
| **RKLB** | Rocket Lab | Yes | Q2 2026 (6/30/2026) | `quarterly/2026_Q2_summary.txt` / `financials/2026_06/` | ✅ Fresh — Q2 2026 + Sep Iridium financing / Electron ops |
| **TT** | Trane Technologies | Yes | Q3 2026 (9/30/2026) | `2026-10-Q3-delta.md` (8-K Ex 99.1; 10-Q filed 29 Oct, not yet reconciled) | ✅ Fresh — Q3 printed 29 Oct 2026; backlog $12.5B; FY rev guide raised |
| **NET** | Cloudflare (`cloudflare/`) | Yes | 2026 Q1 | `2026_Q1_earnings_call_analysis.md` | Stale-ish — Q2 not pulled; **Q3 still expected 5 Nov 2026 after close** (no Item 2.02 as of ~09:45 UK 5 Nov) |
| **AMAT** | Applied Materials | Yes | FY2026 Q2 | `2026_Q2_press_release.txt` | Fresh |
| **GLW** | Corning | Yes | Q3 2026 (9/30/2026) | `2026-10-Q3-delta.md` (8-K Ex 99; 10-Q filed 29 Oct, not yet reconciled) | ✅ Fresh — Q3 printed 27 Oct 2026; core sales +19% |
| **KLIC** | Kulicke & Soffa | Yes | FY2026 Q3 (7/4/2026) | `quarterly/2026_Q3_10q.htm` / `financials/2026_10/` | ✅ Fresh — Q3 beat; Q4 guide $375M; next print est. Nov 17–18, 2026 |
| **PH** | Parker-Hannifin | Yes | FY2026 Q2 | `2026_Q2_earnings_call_transcript.md` | Fresh — **FY27 Q1 expected 5 Nov BMO** (call ~16:00 UK); no Item 2.02 as of ~09:45 UK 5 Nov |
| **INTC** | Intel | Yes | Q3 2026 (ended 9/26/26) | `2026-10-Q3-delta.md` (8-K Ex 99.1; 10-Q not yet reconciled) | ✅ Fresh — Q3 printed 29 Oct 2026; DCAI +78% |
| **GOOG** | Alphabet | Yes | Q3 2026 (ended 9/30/26) | `2026-10-Q3-delta.md` (8-K; 10-Q not yet reconciled) | Fresh — Q3 printed 28 Oct 2026 |
| **TSLA** | Tesla | Yes | Q3 2026 (ended 9/30/26) | `2026-10-Q3-delta.md` (8-K deck + 10-Q filed 2026-10-22) / `financials/2026_06/` | Fresh (Q3 financials folder not yet pulled) |
| **CSCO** | Cisco | Yes | FY2026 Q4 (ended ~Jul 2026) | `2026_Q4_press_release.htm` | Fresh — most recent fiscal quarter closed |
| **GTLB** | GitLab | Yes | FY2026 Q4 (~Jan 2026 FYE) | `2026_Q4_earnings_call.txt` | Fresh |
| **SMCI** | Super Micro Computer | Yes | FY2027 / Q1 (to 30 Sep 2026) | 8-K Ex. 99.1 (3 Nov, prelim); `analysis/2026_11_04_Q1FY27_delta.md` | ✅ Fresh — Q1 FY27 delta 2026-11-04 (10-Q not yet reconciled) |

## Notes

- **2026-11-05 (morning UK):** **DDOG** Q3 printed 4 Nov (8-K accession 0001628280-26-069792): rev $1.197B (+35%), non-GAAP OI $334M (28% margin), non-GAAP EPS $0.81; Q4 rev guide $1.19–1.20B (~flat sequential) → stock −14.4% to $188.72. Note: `ddog/2026-11-Q3-delta.md`. **PH** (FY27 Q1, BMO / call ~16:00 UK) and **NET** (Q3 after close) — no Item 2.02 yet as of ~09:45 UK. **MRNA** Q3 still expected ~**6 Nov** (FMP; no 8-K). **LASE** still 12 Nov BMO.
- **2026-11-04 (morning UK):** **SMCI** Q1 FY27 printed 3 Nov: rev $19.95B (+298%), GM 12.7%, non-GAAP EPS $1.81, OCF −$434M (helped by +$3.1B customer advances), FY27 guide raised to $72–82B. CFO said one customer was **44%** of Q1 revenue (FY26: 28.1%), which meets conditional trim trigger (a) from the 25 Sep audit pending 10-Q. Note: `smci/analysis/2026_11_04_Q1FY27_delta.md`. Next: **DDOG** today BMO (call 13:00 UK), **PH** + **NET** 5 Nov.
- **2026-11-03 (morning UK):** **AAPL** FQ4 FY26 printed 2 Nov; first `aapl/` file added (`aapl/2026-11-Q4FY26-delta.md`, from 8-K Ex 99.1). Rev $114.5B (+12%), GM 47.9% incl. ~1pt tariff refunds, EPS $2.10 (+14%). Next: **SMCI** tonight (3 Nov, call 22:00 UK).
- **2026-11-02 (morning UK):** No new prints since 30 Oct (EDGAR checked: no Item 2.02 8-Ks for AAPL, NET, SMCI, DDOG, CRWV, RKLB, SPCE, PH, CSCO, AMAT or LASE). Confirmed dates: **AAPL** FQ4 FY26 today, 2 Nov (21:30 UK time); **SMCI** FY27 Q1 3 Nov (22:00 UK); **DDOG** 4 Nov BMO (call 13:00 UK); **PH** FY27 Q1 5 Nov BMO (call 16:00 UK); **NET** 5 Nov after close; **RKLB** 9 Nov after close; **CRWV** 10 Nov (call 22:00 UK); **ENR.DE** 11 Nov 07:00 CET; **LASE** 12 Nov BMO (call 13:00 UK); **AMAT**, **CSCO** and **SPCE** 12 Nov after close. LASE pre-print governance note added (`lase/2026-11-pre-Q3-update.md`).

- **2026-10-30:** Q3 2026 post-print delta notes added for **INTC** (29 Oct), **AMZN** (29 Oct), **GLW** (27 Oct) and **TT** (29 Oct), all from 8-K Ex 99.1 with 10-Qs not yet reconciled. Not yet printed: **AAPL** FQ4 FY26 confirmed **2 Nov 2026** (still no `aapl/` folder), **NET** Q3 confirmed **5 Nov 2026**, **SMCI** FY27 Q1 call **3 Nov 2026** (8-K preliminary on 20 Oct: revenue $18.5–19.5B vs $14.5–15.5B guide, GM 12.0–12.5%).
- **2026-10-15:** **DRO** got a mid-October FY26 committed-revenue stamp (A$261M, at the midpoint of guidance; `dro/analysis/2026_10_15_committed_revenue_update.md`). No Q3 Appendix 4C is coming: ASX confirmed on 18 May 2026 that DroneShield no longer has to lodge quarterly 4Cs (last one was 1Q2026, 22 Apr). It now reports half- and full-year only, so the period stays 1H 2026 until FY2026 results (~Feb 2027).
- **2026-10-02:** Added **NVDA** (NVIDIA) first-pass folder — **held**; FY2027 Q2 (period 7/26/2026) SEC 10-Q + Aug 26 earnings; THINKING_FRAMEWORK scorecard in `nvda/analysis/2026_10_scorecard.md`; stance **HOLD**; post–Q3 delta placeholder only.
- **2026-09-28:** Added **AVGO** (Broadcom) first-pass research folder — **held**; FY2026 Q3 (period 8/2/2026) SEC 10-Q + Sep 2 earnings PR; THINKING_FRAMEWORK thesis in `avgo/analysis/2026_09_investment_thesis.md`; stance **HOLD**.
- **2026-09-25:** SMCI risk audit & thesis invalidation check (`smci/analysis/2026_09_25_risk_audit.md`) vs FY2026 Ex. 99.1 / 10-K. Verdict: **WATCH (customer-concentration pillar wobbling)**; hard invalidation not met. Period financials now FY2026/Q4; Q3 call retained.
- **2026-09-23:** Added **MRNA** (Moderna) first-pass research folder — biotech expansion; watchlist/interest (not held). Q2 2026 financials + Aug 19 INTerpath-001 Ph3 win noted.

- **RKLB** refreshed 2026-09-16: Q2 2026 10-Q/PR financials, Sep Iridium ATM financing, Electron cadence, Neutron schedule, GAO MTN protest, IMM Apex; see `rklb/analysis/2026_09_delta_analysis.md`.
- Several tickers (ADBE, CSCO, GTLB, EMR, JCI, PH, MSFT, CVCO, AMAT, KLIC, PLAB) run non-calendar fiscal years, so "Q#" labels don't map directly to calendar quarters — staleness above is a rough proxy, not exact days-since-filing.
- **GOOG** and **TSLA** were refreshed on 2026-09-12 (10-Q + FMP-sourced financials for Q2 2026, period ended 6/30/26). They still only have the raw filing + `financials/` — no `analysis/` documents yet (market, competitive, thesis, etc. per the standard 7-doc workflow). GOOG's Q2 2026 income statement carries a ~$98B non-cash "other income" item that skews TTM net margin/P/E in `financials/2026_06/yahoo_stats.md` — verify against the 10-Q MD&A before using in valuation. FMP rejected the `GOOG` ticker directly; `GOOGL` was used instead (economically equivalent for fundamentals).
- **NET/Cloudflare** now uses single `cloudflare/` folder (Q1 2026 latest; Q4 2025 historical materials preserved under `analysis/2025_12_*` and `financials/2025_12/`). The legacy `net/` folder was removed 2026-09-13.
- **Held? column**: populated from the user's confirmed holdings list (2026-09-18; additive update vs 2026-09-12). Ask before assuming a ticker not on that list is or isn't an active position.
- **Refresh priority among held names** (staleness-ranked): All major held names now current to Q2 2026. GOOG/TSLA refreshed 2026-09-12. NET refreshed Q1 2026. DRO refreshed 2026-09-13 (1H 2026). RYCEY/MSFT refreshed 2026-09-14. SPCE/AMZN refreshed 2026-09-14.


- **2026-09-18 holdings update:** User confirmed invested interest open for TSLA, AVGO, CRWV, ASML, PH, HOOD, GOOG, DDOG, KLIC, AMAT, RKLB, GTLB, SMCI, TT, RYCEY, NVDA, plus INTC, ENR.DE, MSFT, AAPL (and retained prior held names). **AAPL** still not covered as a top-level folder — add when researched.

## How to regenerate

For each ticker folder, find the most recent file in `quarterly/` matching `YYYY_Q#_*` (or the latest dated subfolder in `financials/` if `quarterly/` is empty/sparse), compare its period to the current date, and re-rank from most to least stale.
