# Investment Analysis Repository

This repository contains comprehensive investment analysis for multiple public companies, following a structured framework for financial analysis, market research, and investment thesis development.

## Repository Overview

This is an investment analysis repository for tracking and analyzing public companies. The repository contains structured financial analysis and research materials for multiple companies.

## Companies Covered

_Top-level ticker folders mirror these symbols (mixed case preserved, e.g. **CVCO**)._

- **ADBE**: Adobe Inc. — Creative software and digital marketing solutions
- **AMAT**: Applied Materials, Inc. — Semiconductor wafer fabrication equipment and services
- **AMZN**: Amazon.com, Inc. — E-commerce and cloud (AWS)
- **ASML**: ASML Holding N.V. — Semiconductor lithography (EUV, DUV) systems and services
- **CAT**: Caterpillar Inc. — Heavy equipment and power generation
- **CBT**: Cabot Corporation — Specialty chemicals and performance materials
- **CRWV**: CoreWeave — GPU-focused cloud infrastructure
- **CVCO**: Cavco Industries, Inc. — Factory-built manufactured and modular housing
- **DASH**: DoorDash Inc. — Local commerce and delivery
- **DRO**: DroneShield Limited — Counter-drone detection and mitigation
- **DUK**: Duke Energy Corporation — Regulated utilities
- **EMR**: Emerson Electric Co. — Industrial automation and software
- **FLR**: Fluor Corporation — Engineering, procurement, and construction (EPC)
- **GLW**: Corning Incorporated — Specialty glass and materials
- **HOOD**: Robinhood Markets, Inc. — Retail brokerage, banking, and related financial services
- **JCI**: Johnson Controls International — Building technology and systems
- **LYB**: LyondellBasell Industries — Chemicals and polymers
- **MNTN**: MNTN, Inc. — Performance TV advertising (CTV)
- **MSFT**: Microsoft Corporation — Cloud (Azure), productivity, and devices
- **NEE**: NextEra Energy, Inc. — Utilities and renewables
- **PH**: Parker-Hannifin Corporation — Motion and control technologies
- **RKLB**: Rocket Lab USA — Launch services and space systems
- **SPCE**: Virgin Galactic Holdings — Space tourism and related

### Non-ticker folders

| Path | Purpose |
|------|---------|
| `consolidated/` | Cross-cutting analysis across names |
| `excel_poc/` | Spreadsheet tooling and experiments |

## Valuation Metrics Summary

**⚠️ IMPORTANT: Update this table whenever:**
- New quarterly earnings are released
- Stock prices change significantly (>5%)
- Valuation multiples are updated in company analysis documents
- After major market events affecting valuations

### Combined Valuation Metrics (P/E and P/S Ratios)

| Ticker | Company | Trailing P/E | Forward P/E | Price/Sales | Growth | Notes |
|--------|---------|--------------|-------------|-------------|--------|-------|
| **[DASH](dash/README.md)** | DoorDash | 148.40x | 56.3x* | 9.0x* | 27% YoY | Updated post-earnings ($213.24), premium growth stock |
| **[PH](ph/README.md)** | Parker-Hannifin | 27.96x | 26.18x | 4.97x | 1% organic | Premium valuation, exceptional margins |
| **[JCI](jci/README.md)** | Johnson Controls | 36.22x | 25.19x | 3.08x | 6% organic | Premium valuation, transformation story |
| **[EMR](emr/README.md)** | Emerson Electric | 34.20x | 20.33x | 4.26x | ~2% (2026) | Reasonable for quality industrial |
| **[GLW](glw/README.md)** | Corning | 87.79x | 28.99x | 5.05x | 14% YoY | Trailing P/E distorted by earnings recovery |
| **[HOOD](hood/README.md)** | Robinhood Markets | ~39.8x* | ~36.8x* | ~16.4x* | ~15% YoY rev (Q1 file) | Profitable vs 2022–23 losses; multiples assume growth continues—legal/sentiment/beta swings (yahoo paste Apr 2026) |
| **[AMAT](amat/README.md)** | Applied Materials | 40.44x | 36.23x | 13.22x | Semiconductor WFE cycle | Semiconductor equipment premium; stats Apr 2026 |
| **[AMZN](amzn/README.md)** | Amazon | 34.93x | 34.60x | 3.69x | 13.3% YoY rev | E-commerce / AWS; stats Jan 2026 |
| **[ASML](asml/financials/2026_04/yahoo_stats.md)** | ASML Holding | 32.4x | — | 9.8x | ~28.5% YoY rev | EUV monopoly; lithography capex; stats Apr 2026 |
| **[CVCO](CVCO/financials/2025_02/yahoo_stats.md)** | Cavco Industries | 25.24x | — | — | Modular housing cyclical | No P/S in pasted stats Feb 2026 |
| **[MSFT](msft/README.md)** | Microsoft | 29.2x | 27.5x | 11.1x | Cloud / AI cycle | Stats Feb 2025 snapshot; refresh in `msft/financials/` |
| **[FLR](flr/README.md)** | Fluor | 1.80x | 17.64x | 0.46x | Stable | Trailing P/E distorted (recovery), forward reasonable |
| **[ADBE](adbe/README.md)** | Adobe | 21.91x | 15.06x | 6.57x | 10-12% | Reasonable software valuation |
| **[CAT](cat/README.md)** | Caterpillar | 22.95x | 21.32x | 3.43x | -1% (recovery) | Reasonable cyclical industrial |
| **[NEE](nee/README.md)** | NextEra Energy | 27.24x | 20.04x | 6.22x | 6-8% EPS | Premium utility (renewable growth) |
| **[CBT](cbt/README.md)** | Cabot | 9.90x | 9.94x | 1.08x | 0-2% near-term | Deep value play |
| **[DUK](duk/README.md)** | Duke Energy | 19.90x | 18.21x | 3.01x | 5-7% EPS | Reasonable utility valuation |
| **[LYB](lyb/README.md)** | LyondellBasell | 104.96x | 12.99x | 0.41x | Cyclical trough | Trailing P/E distorted (cyclical downturn) |
| **[MNTN](mntn/README.md)** | MNTN | N/A | N/A | 6.38x | 25% YoY | Not profitable yet |
| **[RKLB](rklb/README.md)** | Rocket Lab | N/A | N/A | 27.43x | Growth stage | Not profitable yet, growth stage |
| **[SPCE](spce/README.md)** | Virgin Galactic | N/A | N/A | 82.95x | Pre-revenue | Not profitable yet, minimal revenue |
| **[CRWV](crwv/README.md)** | CoreWeave | N/A | N/A | 19.10x | 420% YoY | Not profitable yet, growth stage |
| **[DRO](dro/README.md)** | DroneShield | 701.23x | N/A | 40.18x | 1,091% YoY | Very high (small company, early stage) |

*Footnotes:* DASH forward P/E and P/S reflect legacy post-earnings update in readme history; verify live. HOOD multiples: `hood/financials/2026_04/yahoo_stats.md`. **AMAT, AMZN:** company folder README + `financials/*/yahoo_stats`. **ASML:** `asml/financials/2026_04/yahoo_stats.md` — no standalone `README` in folder yet. **CVCO:** uppercase folder [`CVCO/`](CVCO/) — sparse stats [`CVCO/financials/2025_02/yahoo_stats.md`](CVCO/financials/2025_02/yahoo_stats.md). **MSFT:** `msft/financials/2025_02/yahoo_stats.md` dated Feb 2025.

**Valuation Observations:**

**Lowest Multiples (Value Plays):**
- **P/E:** CBT (9.90x), DUK (19.90x), ADBE (21.91x)
- **P/S:** LYB (0.41x), FLR (0.46x), CBT (1.08x); **AMZN** (3.69x) is **low versus** revenue scale for a megacap retailer/cloud mix

**Highest Multiples (Premium/Growth):**
- **P/E:** DASH (148.40x trailing), GLW (87.79x trailing - distorted), LYB (104.96x trailing - distorted), HOOD (~39.8×, Apr 2026 paste), AMAT (~40×, WFE/upcycle)
- **P/S:** SPCE (82.95x), DRO (40.18x), RKLB (27.43x), HOOD (~16×), CRWV (19.10x); **AMAT** (13.22×) and **ASML** (9.8×) sit **rich for equipment** peers

**Most Reasonable (Profitable Companies):**
- **P/E:** ADBE (21.91x/15.06x), CAT (22.95x/21.32x), **MSFT** (29.2×/27.5× dated file), EMR (34.20x/20.33x), AMZN (34.93×)
- **P/S:** CAT (3.43x), DUK (3.01x), JCI (3.08x), EMR (4.26x); **CVCO** (no P/S in pasted stats Feb 2026)

## Value Perception Framework

**⚠️ HIGH VALUATION RISK WARNING:**

**Avoid stocks with premium valuations vulnerable to missteps:**
- **High P/E (>50x) or High P/S (>8x)** without exceptional growth or quality
- **Recent earnings disappointments** showing market sensitivity (e.g., DASH -10.4% on Q4 guidance)
- **Premium multiples** that require perfect execution to justify
- **Growth stocks** where any guidance miss triggers significant selloff
- **Margin compression concerns** despite premium valuations

**Example: DASH (DoorDash)**
- Traded at 148.40x trailing P/E, 10.10x P/S before earnings
- Q4 guidance showing flat sequential EBITDA growth triggered -10.4% decline
- Premium valuation left no margin for error
- **Lesson:** High valuations amplify downside risk on any disappointment

**Risk Management for High Valuation Stocks:**
1. **Avoid or reduce position size** in stocks with premium multiples (>50x P/E, >8x P/S)
2. **Require exceptional growth** (>30% YoY) to justify premium valuations
3. **Monitor guidance closely** - any miss triggers significant downside
4. **Prefer value plays** (P/E <20x, P/S <3x) with margin of safety
5. **Wait for pullbacks** on premium stocks before entry

### Understanding Valuation Multiples

**P/E Ratio Context:**
- **Low P/E (<15x):** Typically value plays, mature companies, or companies facing headwinds
- **Moderate P/E (15-25x):** Reasonable valuations for quality companies with growth
- **High P/E (>25x):** Growth stocks, premium quality, or earnings recovery stories
- **Very High P/E (>50x):** High-growth companies, earnings recovery, or distorted by one-time factors

**P/S Ratio Context:**
- **Low P/S (<1x):** Deep value, cyclical troughs, or low-margin businesses
- **Moderate P/S (1-3x):** Reasonable for mature, profitable companies
- **Premium P/S (3-6x):** Quality companies with strong margins or growth potential
- **High P/S (>6x):** Growth stocks, high-margin businesses, or not-yet-profitable companies

### Value Assessment Framework

**1. Profitability Context:**
- **Profitable Companies:** P/E ratio is meaningful; compare to growth rate (PEG ratio)
- **Not Yet Profitable:** P/S ratio more relevant; assess path to profitability
- **Cyclical Companies:** Trailing P/E may be distorted; forward P/E more meaningful

**2. Growth vs. Value:**
- **Growth Stocks:** Higher P/E and P/S justified by growth rate and market opportunity
- **Value Stocks:** Lower P/E and P/S indicate potential undervaluation or mature businesses
- **Quality at Reasonable Price:** Moderate multiples with strong fundamentals

**3. Industry Context:**
- **Software/Tech:** Higher P/S ratios (5-10x+) common due to high margins and scalability
- **Industrials:** Moderate P/E (15-25x) and P/S (2-4x) typical
- **Utilities:** Lower P/E (15-20x) and P/S (2-3x) due to regulated returns
- **Cyclicals:** Wide range depending on cycle position

**4. Margin Considerations:**
- **High-Margin Businesses:** Can justify higher P/S ratios (e.g., software with 30%+ margins)
- **Low-Margin Businesses:** Lower P/S ratios typical (e.g., EPC contractors, commodities)
- **Margin Expansion Stories:** Premium multiples justified if margins improving

### Identifying Good Value

**Value Indicators:**
1. **Low P/E relative to growth rate** (PEG < 1.0 attractive)
2. **Low P/S relative to margin potential** (P/S < margin % suggests value)
3. **Multiple expansion potential** (current multiples below historical or peer averages)
4. **Earnings recovery stories** (forward P/E much lower than trailing P/E)
5. **Cyclical trough valuations** (deep discounts to historical averages)

**Quality Indicators:**
1. **Consistent profitability** with improving margins
2. **Strong cash generation** relative to earnings
3. **Market leadership** with competitive advantages
4. **Reasonable multiples** relative to growth and quality
5. **Balance sheet strength** with financial flexibility

**Risk Indicators:**
1. **Very high multiples** without corresponding growth or quality
2. **Not yet profitable** with unclear path to profitability
3. **Cyclical peaks** with elevated multiples
4. **Margin compression** despite premium multiples
5. **High leverage** with premium valuations

### Value Scoring Framework

**Scoring Companies by Value:**

**Excellent Value (Score 8-10):**
- P/E < 15x with growth > 15% (PEG < 1.0)
- P/S < 1.5x with margin expansion potential
- Multiple below historical average
- Strong fundamentals (profitability, cash flow, balance sheet)

**Good Value (Score 6-7):**
- P/E 15-25x with growth matching or exceeding multiple
- P/S 1.5-3x with reasonable margins
- Multiple at or below peer average
- Solid fundamentals

**Fair Value (Score 4-5):**
- P/E 25-35x with growth justifying premium
- P/S 3-5x with quality margins
- Multiple at peer average
- Adequate fundamentals

**Premium/Expensive (Score 1-3):**
- P/E > 35x without exceptional growth
- P/S > 5x without high margins or clear path to profitability
- Multiple significantly above peers
- Fundamentals don't justify premium
- **⚠️ HIGH RISK:** Vulnerable to missteps and guidance misses

**Examples from Portfolio:**

**Excellent Value:**
- **CBT** (Cabot): 9.90x P/E, 1.08x P/S - Deep value with profitability
- **FLR** (Fluor): 0.46x P/S - Deep value (EPC discount), forward P/E 17.64x reasonable
- **LYB** (LyondellBasell): 0.41x P/S, 12.99x Forward P/E - Cyclical trough value

**Good Value:**
- **CAT** (Caterpillar): 22.95x P/E, 3.43x P/S - Reasonable for cyclical industrial
- **DUK** (Duke Energy): 19.90x P/E, 3.01x P/S - Reasonable utility valuation
- **ADBE** (Adobe): 21.91x P/E, 6.57x P/S - Reasonable software valuation

**Fair Value:**
- **EMR** (Emerson Electric): 34.20x P/E, 4.26x P/S - Premium justified by quality
- **PH** (Parker-Hannifin): 27.96x P/E, 4.97x P/S - Premium justified by exceptional margins
- **NEE** (NextEra Energy): 27.24x P/E, 6.22x P/S - Premium utility (renewable growth)

**Premium/Expensive (High Risk - Vulnerable to Missteps):**
- **DASH** (DoorDash): 148.40x P/E, 9.0x P/S - **⚠️ HIGH RISK:** Punished -10.4% on Q4 guidance miss
- **GLW** (Corning): 87.79x P/E (distorted), 5.05x P/S - Earnings recovery story, monitor closely
- **HOOD** (Robinhood): ~40x P/E, ~16x P/S (Apr 2026 paste) — growth-style pricing vs improved fundamentals; headline and tape risk (**high beta**)
- **RKLB/CRWV/SPCE**: Not profitable, high P/S ratios - Growth stage investments, high risk

## Repository Structure

Each company follows a consistent directory structure:

```
company_ticker/
├── README.md                    # Company overview and metrics
├── analysis/                    # Detailed research documents
│   ├── YYYY_MM_DD_financial_analysis.md
│   ├── YYYY_MM_DD_market_analysis.md
│   ├── YYYY_MM_DD_competitive_analysis.md
│   ├── YYYY_MM_DD_technical_analysis.md
│   ├── YYYY_MM_DD_risk_assessment.md
│   ├── YYYY_MM_DD_investment_thesis.md
│   └── YYYY_MM_DD_valuation_analysis.md
├── financials/                  # Core financial analysis by period
│   └── YYYY_MM/
│       ├── balance_sheet.md
│       ├── cashflow.md
│       ├── income_statement.md
│       └── yahoo_stats.md
├── quarterly/                   # Raw quarterly data
│   ├── YYYY_Q#_form_10Q.txt/.md
│   ├── YYYY_Q#_presentation.txt/.md
│   └── YYYY_Q#_press_release.txt
└── question_answers/            # Q&A documentation
    └── YYYY_MM_DD_topic.md
```

## Analysis Framework

All analysis follows the comprehensive framework defined in `AGENTS.md`, covering:
- Business model analysis
- Financial metrics tracking
- Competitive position assessment
- Growth catalysts evaluation
- Risk factor analysis
- Industry context
- Valuation considerations

## Key Resources

- **AGENTS.md**: Comprehensive guide for AI agents and analysis framework
- **consolidated/**: Cross-company analysis and comparisons
- **excel_poc/**: Spreadsheet / extraction experiments (not issuer coverage)
- Individual company READMEs: Company-specific overviews and investment theses

---

*Last Updated: April 29, 2026 — **Companies Covered** aligned to top-level ticker folders (incl. **AMAT, AMZN, ASML, CVCO, HOOD**, **consolidated/** + **excel_poc/** documented separately).*  
*Valuation shortcuts: pasted snapshot dates vary by ticker (see Footnotes row under combined table).*  
*HOOD multiples: [hood/financials/2026_04/yahoo_stats.md](hood/financials/2026_04/yahoo_stats.md); refresh when prices change.*
