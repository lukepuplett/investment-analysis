# AGENTS.md

**⚠️ CRITICAL RULES:**
1. **Do NOT use `cat`, `echo`, or shell output redirection to communicate with the user.** Write responses directly in the chat instead. Shell commands are for operations only, not communication.
2. **Do NOT create temporary .md documentation files just to communicate.** Only create documentation files that will be long-lived and part of the repository. Communicate analysis, findings, and summaries directly in chat instead.

This file provides comprehensive guidance for AI agents when working with this investment analysis repository.

---

## Table of Contents

- [Repository Overview](#repository-overview)
- [Architecture & Structure](#architecture--structure)
- [File Organization Standards](#file-organization-standards)
- [Analysis Workflow](#analysis-workflow) — **CANONICAL**
- [Key Metrics to Track](#key-metrics-to-track)
- [Investment Analysis Framework](#investment-analysis-framework)
- [Repository Organization](#repository-organization)
- [Key Areas of Analysis](#key-areas-of-analysis)
- [Analysis Approach](#analysis-approach)
- [AI Analysis Guidelines](#ai-analysis-guidelines)
- [Document Formatting Standards](#document-formatting-standards)
- [Financial Statement Formatting Standards](#financial-statement-formatting-standards)
- [File Naming Conventions](#file-naming-conventions) — **CANONICAL**
- [Documentation Requirements](#documentation-requirements)
- [Valuation Analysis Framework](#valuation-analysis-framework)
- [Repository Usage Notes](#repository-usage-notes)
- [Data Collection & Financial Data Access](#data-collection--financial-data-access)
- [Meta-Instructions for AI Agents](#meta-instructions-for-ai-agents)

---

## Repository Overview

This is an investment analysis repository for tracking and analyzing public companies. The repository contains structured financial analysis and research materials organized by **ticker folder** (e.g. `hood/`, `msft/`, `CVCO/`). **Canonical list of covered names:** see root **[README.md](README.md)** — *Companies Covered* (the sample bullets below are illustrative only):
- **CRWV**: CoreWeave - AI hyperscaler specializing in GPU-accelerated computing
- **MNTN**: MNTN, Inc. - Performance TV advertising company focusing on CTV advertising
- **RKLB**: Rocket Lab - Aerospace company providing launch services and space systems
- **CAT**: Caterpillar Inc. - Heavy equipment manufacturer and power generation systems

## Architecture & Structure

### High-Level Organization
The repository follows a company-based directory structure where each company contains identical subdirectories for consistent analysis:

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
├── quarterly/                   # Primary source: all period-specific documents
│   ├── YYYY_Q#_10q.htm                    # SEC 10-Q iXBRL primary document
│   ├── YYYY_Q#_10q_facts.json             # Extracted XBRL numeric facts
│   ├── YYYY_Q#_md_and_a.txt               # Management Discussion & Analysis (text)
│   ├── YYYY_Q#_earnings_call.txt          # Earnings call transcript (if available)
│   ├── YYYY_Q#_investor_presentation.pdf  # Earnings presentation slides
│   ├── YYYY_Q#_press_release.txt          # Company press release
│   └── 10Q_EXTRACTION_SUMMARY.md          # Metadata on extraction process
└── question_answers/            # Q&A documentation
    └── YYYY_MM_DD_topic.md
```

### Key Components

**Quarterly Data Layer (quarterly/ folder)** — Single source of truth for all period-specific documents:
- **10-Q filings** (iXBRL format) provide the authoritative financial statements and MD&A
- **Extracted facts JSON** enables programmatic analysis and trend aggregation across quarters
- **Earnings call transcripts** capture management tone, guidance, and Q&A beyond the written filing
- **Investor presentations** add visual context and highlight management's narrative
- **Press releases** provide initial guidance and key metrics before detailed filing release

This folder is intentionally flat (not year/quarter subdirectories) for easy discovery and consistency across companies. Name files `YYYY_Q#_` for chronological sorting.

**Analysis Framework**: This document contains the comprehensive investment analysis framework that governs all analysis in this repository. It defines:
- Business model analysis standards
- Financial metrics tracking requirements
- Document formatting standards
- File naming conventions
- Analysis workflow and methodology

**Cursor Rules Integration**: The repository uses Cursor MDC rules stored in `.cursor/rules/` that provide IDE-integrated guidance for:
- `financial_analysis.mdc`: Financial analysis standards and table formatting
- `business_model_analysis.mdc`: Business model evaluation criteria
- `file_organization.mdc`: File naming and organizational standards

## File Organization Standards

### Required Analysis Documents
For comprehensive analysis, create all of these documents in the `analysis/` directory using format: `YYYY_MM_[analysis_type].md` (e.g., `2025_05_financial_analysis.md`):

1. `YYYY_MM_financial_analysis.md` - Financial metrics and health assessment
2. `YYYY_MM_market_analysis.md` - Market position and industry trends  
3. `YYYY_MM_competitive_analysis.md` - Competitive position and advantages
4. `YYYY_MM_technical_analysis.md` - Technical capabilities and risks
5. `YYYY_MM_risk_assessment.md` - Comprehensive risk analysis
6. `YYYY_MM_investment_thesis.md` - Overall investment thesis and recommendations
7. `YYYY_MM_valuation_analysis.md` - Valuation methodology and price targets
8. `YYYY_MM_delta_analysis.md` - Changes and shifts since previous assessment (quarterly or major updates)

**Delta Analysis Document:** The delta document captures material changes since the last analysis round and serves as a quick reference for what has shifted. It allows for focused monitoring between full analysis cycles. Include:
- Financial metric changes (revenue, margins, profitability, cash flow, debt levels)
- Operational changes (customer mix, market share, segment performance, efficiency metrics)
- Valuation shifts (stock price movement, multiples, relative value vs peers)
- Strategic updates (new products, market expansion, M&A, partnerships)
- Risk changes (new risks emerged, previous risks resolved/worsened, regulatory changes)
- Competitive landscape shifts (competitor moves, market dynamics)
- Management commentary changes (guidance updates, tone shifts, capital allocation changes)
- Key ratio changes (profitability, leverage, returns, efficiency)
- Investment thesis impact (which thesis pillars are validated/challenged)

### Table Formatting Standards
Financial data tables must follow consistent formatting:
- Three-column structure: Metric (left-aligned), Value (right-aligned), Period (right-aligned)
- Currency values with $ and appropriate units (M, B)
- Percentages with % symbol
- Dates in MM/DD/YYYY format
- Include abbreviations legend: MRQ = Most Recent Quarter, TTM = Trailing Twelve Months

### Standard Analysis Table Framework
Use the following five tables in every full update (earnings, major thesis review). Keep layouts consistent to enable fast comparisons across companies.

1. **Three-Scenario Revenue Model**  
   - *Purpose:* Frame bull/base/bear revenue outcomes over the next 2–3 fiscal periods.  
   - *Structure:* `Scenario | Q4 [CY] | FY [CY] | FY [CY+1]E | FY [CY+2]E | Key Driver/Assumption`.  
   - *Usage:* Populate after each earnings call; highlight 2–3 core drivers that shift between scenarios. Optional probability weights support valuation work.

2. **Red Flag Audit with Mitigant Assessment**  
   - *Purpose:* Catalogue major risks, management responses, and monitoring KPIs.  
   - *Structure:* `Risk | Severity (1–10) | Mitigant | Mitigant Strength (1–10) | Monitoring KPI`.  
   - *Usage:* Refresh quarterly; severity ≥8 with mitigant ≤5 remains an open red flag that must be called out in the thesis.

3. **Competitive Moat Scorecard**  
   - *Purpose:* Score durability of each competitive lever.  
   - *Structure:* `Moat Factor | Rating (1–5) | Notes | Durability Horizon | Replicability`.  
   - *Usage:* Update semi-annually or when competitive dynamics change; average the ratings (optionally weighted) to derive the overall moat score.

4. **Investment Thesis Coherence Check**  
   - *Purpose:* Ensure thesis pillars, confidence levels, and evidence stay aligned.  
   - *Structure:* `Thesis Pillar | Status (✅/⚠️/❌) | Confidence (1–10) | Evidence | Risk if Wrong`.  
   - *Usage:* Maintain alongside the investment thesis document; revisit whenever new data shifts conviction.

5. **Valuation Sensitivity Table**  
   - *Purpose:* Show how ±10% moves in key assumptions affect valuation.  
   - *Structure:* `Driver | Base Assumption | +10% Impact | -10% Impact | Valuation Delta`.  
   - *Usage:* Recalculate with every material model change; rank drivers by absolute valuation impact to focus monitoring.

**Quick Workflow (≈30 minutes):**  
1) Build the revenue scenarios, 2) score the moat, 3) run the red flag audit, 4) check thesis coherence, 5) map valuation sensitivity. Summaries from these tables must feed into the BLUF and recommendation sections.  
**Prompting Tip:** When requesting LLM support for a new company, explicitly ask for outputs in the five-table format above, followed by conviction, recommendation, and probability-weighted price target.

### Revenue Breakdown & Growth Drivers Analysis

**Mandatory section for all company README.md documents.** This analysis translates abstract business jargon into concrete revenue mechanics and growth mechanisms. It serves as the bridge between market narrative and financial reality, making complex product ecosystems and business drivers visible to investors.

#### Purpose & Structure

This section appears in each company's `README.md` alongside key financial metrics and serves as a reference for understanding:
- Which revenue streams drive the business (and by how much)
- How jargon from earnings calls, MD&A, and investor presentations maps to actual revenue
- Quantified growth drivers and their specific £/$ financial impact
- Current state vs. medium-term (2028E) targets with driver attribution
- Long-term opportunities (3–5 years out) with TAM and impact potential

#### Step-by-Step Methodology

**1. Jargon Extraction (Data Collection Phase)**
- Review primary sources: earnings call transcripts, investor presentations, MD&A sections, product fact sheets
- Identify domain-specific terms: product platform names, financial metrics, operational KPIs, market segments
- Categorize jargon into three buckets:
  - **Industry Acronyms** (standards, regulations, market segments): OEM, MRO, LTSA, EJ200, Data Center, SMR, etc.
  - **Product Platforms & Offerings**: Pearl Business Jet, Series 4000 Engine, UltraFan, narrowbody, widebody, etc.
  - **Financial & Operational Terms**: Time on Wing, Shop Visits, Book-to-Bill, Aftermarket, Power Density, etc.
- Compile into a **Jargon Glossary** section in README (optional but recommended for complex businesses)

**2. Revenue Breakdown by Segment (Current State)**
- Use latest annual or TTM financial data
- Segment revenue by business unit or product line (e.g., Civil Aerospace, Defense, Power Systems)
- For each segment, show:
  - **Absolute revenue** (£B or $M) and **% of total**
  - **Key jargon terms** that describe that segment's revenue streams
  - Examples:
    - Civil Aerospace (60% of revenue): driven by Original Equipment (OE), Long-Term Service Agreements (LTSA), MRO shop visits, and business aviation platforms
    - Defense (10% of revenue): sustained by military engine programs (EJ200), Eurofighter sustainment, submarine contracts
    - Power Systems (15% of revenue): growing from data center demand, power density innovations, Series 4000 designs

**3. Growth Drivers with Financial Quantification (What Changes Revenue)**
- Identify 5–8 key levers that will drive revenue growth from current state to 2028E
- For each driver, quantify the specific impact:
  - **LTSA Margin Expansion**: +£800M–1.2B (higher aftermarket mix + service efficiency)
  - **Aftermarket Volume Growth**: +£1.0–1.5B (Time on Wing increasing, installed base aging)
  - **OE Profitability**: +£400–600M (production scale, unit cost reduction)
  - **Data Center Demand**: +£700M–1.0B (Power Systems segment expansion, power density adoption)
  - **Defense Sustainment**: +£300–500M (multi-decade contract extensions, higher utilization)
  - etc.
- Show the **mechanism**: how does the driver translate to revenue? (e.g., Time on Wing ↑ = more flight hours ↑ = more engine deterioration ↑ = more MRO shop visits ↑ = higher Aftermarket revenue)

**4. Visual & Tabular Representation**

**A. Revenue Waterfall / Tree Structure** (ASCII or markdown table)
- Show current-year revenue by segment
- Build out to 2028E targets with driver attribution
- Example ASCII tree:

```
FY2025 Revenue: £21.2B
├── Civil Aerospace (£12.7B, 60%)
│   ├── OE (Original Equipment): £6.5B
│   ├── LTSA (Long-Term Service Agreements): £4.2B
│   ├── MRO (Maintenance, Repair, Overhaul): £1.5B
│   └── Business Aviation (Pearl): £0.5B
├── Defense (£2.1B, 10%)
│   ├── EJ200 Engine Programs: £1.2B
│   ├── Eurofighter Sustainment: £0.6B
│   └── Submarine & Other: £0.3B
└── Power Systems (£4.9B, 15%)
    ├── Data Centers (power modules): £2.1B
    ├── Series 4000 & SMR: £2.8B
    └── Other Power: £0.0B

2028E Targets (with drivers):
├── Civil Aerospace: £17.5B (+£4.8B from OE scale, LTSA mix, Time on Wing, MRO volume)
├── Defense: £2.8B (+£0.7B from sustainment contracts, higher utilization)
└── Power Systems: £6.2B (+£1.3B from data center expansion, SMR progress)
```

**B. Growth Driver Impact Table** (markdown)

| Driver | Segment | FY2025 | FY2028E | Impact | Mechanism |
|--------|---------|--------|--------|--------|-----------|
| LTSA Margin Expansion | Civil Aero | £4.2B | £5.2B | +£1.0B | Aftermarket mix shift, service efficiency gains |
| Time on Wing | Civil Aero | Existing | Enhanced | +£800M | Installed base aging, more MRO visits/year |
| OE Profitability | Civil Aero | £6.5B | £7.8B | +£1.3B | Production scale, unit cost down, mix to widebody |
| Data Center Demand | Power Sys | £2.1B | £3.4B | +£1.3B | Hyperscaler capex acceleration, power density adoption |
| Defense Sustainment | Defense | £1.5B | £2.0B | +£0.5B | Multi-decade contract wins, fleet utilization ↑ |
| UltraFan (narrowbody) | Civil Aero | Prelaunch | Scale | +£2.0–3.0B | Launch 2027, narrow-body retrofit ramp, 15% fuel savings |
| SMR (Small Modular Reactors) | Power Sys | Minimal | Scale | +£1.0–2.0B | 2030–2035 timeline, UK/US grid decarbonization |

**5. Translation Examples (Jargon → Financial Outcome)**

For each major business segment, include 2–3 worked examples showing how abstract jargon becomes concrete revenue:

**Example 1: LTSA & Time on Wing (Civil Aerospace)**
- **Jargon**: "Time on Wing expanding due to aging fleet; LTSA margin accretion from power-by-the-hour utilization"
- **Translation**: 
  - Current: 8,000 widebody aircraft in global service, averaging 18 years old
  - Mechanics: Aircraft flying more hours (post-COVID recovery) → engines degrading faster → more shop visits needed
  - Financial: Each shop visit = £50k–150k revenue at 70% gross margin. 2% increase in annual shop visits = +£200M–300M Aftermarket revenue
  - Plus: LTSA customers pay premium for guaranteed uptime → reduces price risk, locks in 15%+ margins vs. 12% transactional MRO

**Example 2: Data Center Power Demand (Power Systems)**
- **Jargon**: "Power density" refers to how much computing workload you can run per megawatt, driving hyperscaler capex efficiency
- **Translation**:
  - Current: Hyperscalers need 5–8 MW per data center rack pod; total global AI/ML data center builds = 150 GW by 2030
  - Mechanics: Higher density → fewer MW needed to serve same compute → lower power delivery costs → hyperscalers willing to pay premium for compact, efficient power modules
  - Financial: Rolls-Royce Series 4000 power modules cost £5–10M each; each data center pod = 2–3 modules = £10–30M contract value. 50 new pods/year in 2028E = £500M–1.5B incremental Power Systems revenue

**Example 3: UltraFan (Civil Aerospace)**
- **Jargon**: "UltraFan narrowbody certification" signals entry into $500B+ narrow-body aftermarket; "15% fuel savings" is the customer value driver
- **Translation**:
  - Current: Rolls-Royce absent from largest segment (narrow-body engines = 60% of commercial fleet)
  - Mechanics: Certification in 2027, retrofit eligibility for existing fleet in 2028–2030. 4,000 narrow-body retrofits over 10 years = £100–200M OE revenue + recurring LTSA revenue
  - Financial: Retrofit value = £5–8M per aircraft; at 2% annual retrofit rate, adds £400M–800M OE + £100M–150M LTSA by 2030

#### README Implementation Checklist

When creating or updating a company's README, include:

- [ ] **Jargon Glossary** (optional, but required for complex businesses with >4 segments or heavy technical terminology)
- [ ] **FY[Latest] Revenue Breakdown** (current state by segment with jargon mapping)
- [ ] **5–8 Quantified Growth Drivers** (impact range, mechanism, timeline to realization)
- [ ] **Visual Tree or ASCII Diagram** (shows current revenue composition and 2028E targets)
- [ ] **Growth Driver Impact Table** (segment, current, FY2028E, impact £/%, mechanism)
- [ ] **2–3 Translation Examples** (jargon → mechanics → financial outcome, worked example format)
- [ ] **Long-Term Opportunities** (3–5 year horizon, TAM, potential upside, key milestones)

#### Tips for Execution

1. **Extract jargon from primary sources**: Spend 20–30 minutes reviewing the latest earnings call transcript, investor presentation, and MD&A. Highlight every acronym, product name, and operational metric management mentions.

2. **Map jargon to financial levers**: Ask: "How does this jargon translate to revenue growth or margin improvement?" Link abstract terms to concrete financial mechanics (volume, price, margin, mix).

3. **Quantify impact with ranges**: Avoid false precision. Use ranges (e.g., "+£800M–1.2B") and explain assumptions. Ranges account for execution risk and allow for scenario flexibility.

4. **Use the translation examples to stress-test your thesis**: If you cannot explain how a major jargon term becomes revenue, your analysis is incomplete. The translation forces you to think through the financial mechanics.

5. **Align with market commentary**: Investors and analysts use the same jargon. By translating it into financial outcomes, you make your analysis coherent with the market narrative while adding quantified specificity.

6. **Update quarterly or semi-annually**: Review after each earnings release. Recalibrate growth drivers and impact ranges based on actual results vs. guidance.

## Analysis Workflow

**Canonical workflow for investment analysis. Other similar sections refer to this.**

### 1. Data Collection
- Gather quarterly financial statements
- Collect market data and company announcements
- Track company news and industry developments
- Monitor capacity metrics and operational indicators

### 2. Analysis Process
- Create **ALL required analysis documents** before providing summary analysis
- Update financial models and key metrics
- Review competitive position and market dynamics
- Assess growth catalysts and operational changes
- Evaluate risks and risk mitigants
- Update valuation models and sensitivity analyses
- Verify assumptions against latest data

### 3. Documentation
- Store raw data in appropriate quarterly/ directories
- Create all required analysis documents in analysis/ directory
- Update key metrics and financial tables
- Maintain investment thesis with supporting evidence
- Track scenario outcomes and thesis validation
- Ensure cross-referencing between related documents
- Use consistent section headers across documents
- Maintain chronological order in all filenames
- Include links to source materials in quarterly/ directory

### 4. Review and Update Schedule
- **Daily**: Price tracking and news monitoring
- **Weekly**: News and competitive landscape monitoring
- **Monthly**: Market position and key metrics check
- **Quarterly**: Full performance review, earnings analysis, model updates
- **Semi-Annual**: Thesis review, moat assessment, valuation refresh

## Key Metrics to Track

### Financial Performance
- Revenue growth (segment breakdown, quarterly/annual trends)
- Profitability metrics (gross margins, operating margins, EBITDA, free cash flow)
- Balance sheet health (cash position, debt levels, working capital)
- Return metrics (ROIC, ROE)

### Business Model Assessment
- Revenue streams and pricing strategy
- Contract analysis and backlog
- Capacity utilization and constraints
- Customer concentration and retention

### Competitive Analysis
- Market share and positioning
- Competitive advantages and differentiation
- Technology leadership and innovation
- Strategic partnerships

## Investment Analysis Framework

## Repository Organization

### Directory Structure
- `analysis/`: Detailed research and analysis documents
  * Market analysis
  * Competitive analysis
  * Investment thesis
  * Technical analysis
  * Risk assessment
- `financials/`: Core financial analysis
  * Balance sheet analysis
  * Income statement analysis
  * Cash flow analysis
  * Key financial metrics
- `quarterly/`: Quarterly financial data
  * SEC Form 10-Q filings
  * Earnings presentations
  * Press releases
  * Quarterly performance analysis
  * Year-over-year comparisons
  * Quarterly trends

### File Organization
- Use consistent naming conventions
- Maintain chronological order in quarterly data
- Keep analysis documents up to date
- Cross-reference between directories
- Track source documents in quarterly/financial_statements

## Key Areas of Analysis

### 1. Business Model Analysis
- Revenue Model
  * Pricing strategy
  * Revenue streams
  * Contract types and durations
  * Customer concentration
  * Vertical integration benefits
- Product/Service Economics
  * Manufacturing margins
  * Service delivery costs
  * Contract value vs actual revenue
  * Backlog analysis
  * Capacity utilization

### 2. Financial Metrics to Track
- Revenue Growth
  * Segment breakdown
  * Quarterly and annual trends (analyze historical growth patterns)
  * Backlog analysis
  * Capacity constraints
  * Market penetration
  * Future growth drivers from sentiment and economic themes
- Profitability Metrics
  * Gross margins by segment
  * Operating margins
  * EBITDA
  * Free cash flow
  * Return on invested capital
- Balance Sheet Health
  * Cash position
  * Debt levels
  * Working capital
  * Capital expenditure requirements
  * Scaling investment needs

### 3. Competitive Position
- Market Share
  * Segment leadership
  * Global competition
  * Capacity vs demand
  * Market dynamics
- Competitive Advantages
  * Technology differentiation
  * Cost advantages
  * Network effects
  * Brand strength
  * Vertical integration

### 4. Growth Catalysts
- Product Development
  * Timeline and milestones
  * Capital requirements
  * Market potential
  * Government contract eligibility
  * Actual contract wins
- Operational Improvements
  * Cost reduction potential
  * Efficiency gains
  * Implementation timeline
  * Financial impact scenarios
- Market Expansion
  * New product development
  * Market penetration
  * Strategic partnerships
  * Acquisition integration

### 5. Risk Factors
- Technical Risks
  * Product reliability
  * Development delays
  * Technology challenges
  * Implementation risks
- Market Risks
  * Competition intensity
  * Pricing pressure
  * Market size limitations
  * Capacity constraints
- Financial Risks
  * Cash burn rate
  * Funding requirements
  * Dilution potential
  * Scaling costs
- Contract Risks
  * Program value vs actual revenue
  * Eligibility vs guaranteed work
  * Government funding uncertainty
  * Customer satisfaction

### 6. Industry Context
- Industry Trends
  * Market growth
  * Regulatory changes
  * Technology evolution
  * Capacity constraints
- Regulatory Environment
  * Compliance requirements
  * Export controls
  * Environmental regulations
  * Government contract requirements

### 7. Valuation Considerations
- Comparable Companies
  * Public peers
  * Industry leaders
  * Technology providers
  * Growth stage peers
- Valuation Metrics
  * Revenue multiples
  * EV/EBITDA
  * Price to Book
  * Growth-adjusted metrics
- Scenarios Analysis
  * Conservative case
  * Aggressive case
  * Base case
  * Key assumptions

## Analysis Approach
1. Regular Updates
   - Quarterly earnings analysis
   - Milestone tracking
   - News and developments
   - Market sentiment
   - Capacity utilization

2. Data Sources
   - SEC filings (Form 10-Q)
   - Company presentations
   - Press releases
   - Industry reports
   - Market data
   - News articles

3. Documentation
   - Store raw data in appropriate directories
   - Create analysis documents
   - Update key metrics
   - Maintain investment thesis
   - Track assumptions

4. Decision Framework
   - Investment thesis
   - Entry/exit points
   - Position sizing
   - Risk management
   - Scenario planning

## AI Analysis Guidelines

### Prompt Structure
When requesting AI analysis, structure the prompt to cover:

1. Financial Analysis
   - Latest quarterly results comparison
   - Balance sheet health assessment
   - Revenue growth and profitability metrics (analyze historical growth trends in data)
   - Cash flow sustainability analysis
   - Future growth assessment from sentiment and economic themes
   - Capacity constraints

2. Business Model Assessment
   - Revenue stream breakdown
   - Product/service economics
   - Development program progress
   - Margin impact analysis
   - Contract value vs revenue

3. Competitive Position
   - Market position analysis
   - Competitive advantages
   - Pricing power assessment
   - Technology differentiation
   - Capacity comparison

4. Growth Catalysts
   - Development program potential
   - Program progress analysis
   - Expansion opportunities
   - New market potential
   - Scaling capabilities

5. Risk Assessment
   - Technical risks
   - Market risks
   - Financial risks
   - Regulatory risks
   - Competitive risks

## Document Formatting Standards

### Financial Statistics Tables
When creating or updating financial statistics documents (e.g., yahoo_stats.md):
1. Use consistent table formatting with three columns:
   - Metric: Left-aligned
   - Value: Right-aligned
   - Period: Right-aligned
2. Include standard sections:
   - Valuation Measures
   - Profitability
   - Income Statement
   - Balance Sheet
   - Cash Flow
   - Trading Information
   - Share Statistics
   - Dividends & Splits
3. Format values consistently:
   - Currency values with $ and appropriate units (M, B)
   - Percentages with % symbol
   - Dates in MM/DD/YYYY format
   - Use N/A for unavailable data
4. Always include abbreviations legend:
   - MRQ = Most Recent Quarter
   - TTM = Trailing Twelve Months
   - YoY = Year over Year

#### Example Table Format

| Metric                    | Value    | Period         |
|--------------------------|----------|---------------|
| Market Cap                | $72.23B  | 3/31/2025      |
| Price/Sales               | 25.86    | TTM            |
| Profit Margin             | -38.73%  | TTM            |
| Revenue                   | $2.71B   | TTM            |
| Current Ratio             | 0.44     | MRQ            |
| Operating Cash Flow       | $771.3M  | TTM            |
| Shares Outstanding        | 361.88M  | MRQ            |
| Trailing Annual Dividend  | $0.00    |                |

*Abbreviations: MRQ = Most Recent Quarter, TTM = Trailing Twelve Months, YoY = Year over Year*

### Trend Indicators for Time-Series Tables

Use directional arrows in a "Trend" column for historical metric tables to enable quick pattern recognition without reading every value. This reduces cognitive load and highlights direction/severity at a glance.

**Standard Indicators:**
- `↗` = Improving / Growing / Positive trend
- `↘` = Declining / Shrinking / Negative trend  
- `→` = Stable / Flat / No material change
- `⚠️` = Watch / Caution / Unexpected change
- `✅` = On Track / Positive momentum
- `❌` = Off Track / Negative deviation

**Example: Path to Profitability (Multi-Year View)**

| Metric | TTM | 2024 | 2023 | 2022 | Trend |
|--------|-----|------|------|------|-------|
| **Revenue** | $2,167M | $1,670M | $1,297M | $975M | ↗ Growing |
| **Gross Profit** | $1,615M | $1,291M | $990M | $743M | ↗ Growing faster |
| **Gross Margin** | 74.5% | 77.3% | 76.4% | 76.1% | ↘ Slight compression |
| **Operating Loss** | ($207M) | ($155M) | ($185M) | ($201M) | ↗ **Improving** |
| **Operating Margin** | -9.6% | -9.3% | -14.3% | -20.6% | ↗ **Path clear** |
| **EBITDA** | $105.8M | $62M | ($36M) | ($83M) | ↗ **Inflection point** |
| **EBITDA Margin** | 4.88% | 3.7% | (2.8%) | (8.5%) | ↗ **Positive trend** |
| **Net Loss** | ($102M) | ($79M) | ($184M) | ($193M) | ↗ **Improving** |
| **Net Margin** | -4.7% | -4.7% | -14.2% | -19.8% | ↗ **Converging** |

**Why This Works:**
1. **Eliminates eye-scanning:** Reader doesn't need to compare 4 numbers to spot the trend
2. **Highlights narrative:** Operating loss improving from ($201M) → ($207M) is counterintuitive at first glance; arrow + bold clarifies it's trending the right direction
3. **EBITDA inflection is obvious:** One arrow shows the complete story: negative → positive (in just 2 years)
4. **Margin compression is visible:** Even though gross profit growing faster, the ↘ on margin flags a potential concern worth investigating
5. **Executive-friendly:** C-suite can scan table in 10 seconds vs. 30 seconds reading every value

**When to Use:**
- Any metric tracked over 3+ periods (years, quarters)
- Financial analysis documents (P&L, balance sheet trends)
- Risk assessment (risk severity trending up/down)
- Thesis coherence checks (confidence levels, status changes)
- Avoid: One-time snapshots or single-period metrics (no trend data)

### General Document Guidelines
1. Use clear hierarchical headers (##, ###)
2. Maintain consistent spacing between sections
3. Use bullet points for lists
4. Include relevant timestamps in document titles
5. Cross-reference related documents when applicable

### BLUF (Bottom Line Up Front) Summary Requirements

Each analysis document must include a clear, concise BLUF summary that:
- **Provides immediate understanding** of key investment thesis
- **States clear risk/reward profile** in one sentence
- **Includes specific metrics** and recommendations
- **Uses bold formatting** for emphasis
- **Enables quick decision-making** for busy readers

#### BLUF Format Example
```markdown
## Executive Summary

**BLUF: [Company] shows [key financial/operational status] with [specific metrics]. The company has [strengths] but faces [risks]. [Recommendation] - [target audience].**

[Detailed executive summary follows...]
```

### README Consolidation Process

After completing all analysis documents:
1. **Extract BLUF summaries** from all 7 analysis documents
2. **Consolidate into README** under "Executive Summary (BLUF - Bottom Line Up Front)" section
3. **Update analysis status** from incomplete ([ ]) to complete ([x])
4. **Maintain chronological order** of BLUF summaries by analysis type
5. **Include key metrics** and recommendations in consolidated format

## Financial Statement Formatting Standards

### General Formatting Rules
1. Use consistent table formatting with clear headers
2. Include period columns (TTM, specific dates)
3. Maintain proper indentation for sub-items
4. Use consistent number formatting (no dollar signs, thousands)
5. Include clear section headers (##, ###)
6. Add explanatory notes and abbreviations

### Table Structure
1. Main sections should use full-width tables
2. Sub-items should be indented with proper alignment
3. Period columns should be right-aligned
4. Metric names should be left-aligned
5. Values should be right-aligned
6. Include 5-year history when available (TTM + 4 years)

### Example Financial Statement Format

```markdown
# Company Name (TICKER) – Statement Type (Selected Periods)

## Main Section
| Metric                        | TTM      | 12/31/2024 | 12/31/2023 | 12/31/2022 | 12/31/2021 |
|-------------------------------|----------|------------|------------|------------|------------|
| Primary Metric                | 1,000    | 800        | 600        | 400        | 200        |
| Sub-item 1                    | 500      | 400        | 300        | 200        | 100        |
|  - Detailed Sub-item          | 250      | 200        | 150        | 100        | 50         |
| Sub-item 2                    | 500      | 400        | 300        | 200        | 100        |
| Total                        | 1,000    | 800        | 600        | 400        | 200        |

## Key Metrics
| Metric                        | TTM      | 12/31/2024 | 12/31/2023 | 12/31/2022 | 12/31/2021 |
|-------------------------------|----------|------------|------------|------------|------------|
| Important Ratio               | 0.50     | 0.45       | 0.40       | 0.35       | 0.30       |
| Growth Rate                   | 25.00%   | 20.00%     | 15.00%     | 10.00%     | 5.00%      |

*All values in thousands USD. TTM = Trailing Twelve Months.*
```

### Required Sections
1. Title with company name and ticker
2. Main financial sections with detailed breakdowns
3. Key metrics section
4. Analysis section (optional)
5. Key trends section (optional)
6. Notes section with abbreviations and important information

### Value Formatting
1. Numbers:
   - No dollar signs in tables
   - Use commas for thousands
   - Right-align all numbers
   - Use consistent decimal places
   - Use -- for zero or not applicable values
2. Percentages:
   - Include % symbol
   - Use consistent decimal places
3. Dates:
   - Use MM/DD/YYYY format
   - Right-align in tables
   - Include 5-year history when available

### Section Organization
1. Start with most important metrics
2. Group related items together
3. Use proper indentation for sub-items
4. Include totals at the end of each section
5. Add explanatory notes where needed
6. Maintain consistent order across all financial statements

### Analysis Requirements
1. Include trend analysis
2. Highlight significant changes
3. Explain key metrics
4. Note important context
5. Reference related documents

### Statement-Specific Requirements

#### Cash Flow Statement
1. Organize into three main sections:
   - Operating Cash Flow
   - Investing Cash Flow
   - Financing Cash Flow
2. Include Key Metrics section with:
   - End Cash Position
   - Free Cash Flow
   - Capital Expenditure
3. Show detailed breakdowns of:
   - Working capital changes
   - Investment activities
   - Debt and equity transactions

#### Income Statement
1. Organize into main sections:
   - Revenue
   - Expenses
   - Profitability
   - EPS & Shares
2. Include detailed breakdowns of:
   - Operating expenses
   - Non-operating items
   - Tax provisions

#### Balance Sheet
1. Organize into main sections:
   - Assets
   - Liabilities
   - Equity
2. Include Key Ratios section
3. Show detailed breakdowns of:
   - Current and non-current items
   - Working capital components

*Note: These formatting standards should be applied consistently across all financial statements while maintaining the specific requirements of each statement type.*

## File Naming Conventions

### Quarterly Releases
1. Format: `YYYY_Q#_press_release.txt`
   - YYYY: Four-digit year
   - Q#: Quarter number (1-4)
   - press_release: Type of document
   - .txt: File extension
2. Examples:
   - `2025_Q1_press_release.txt`
   - `2024_Q4_press_release.txt`
3. Location: `quarterly/` directory
4. Content: Full earnings press release with financial results

### SEC Filings
1. Form 10-Q (Quarterly Report)
   - Format: `YYYY_Q#_10q.txt`
   - Also known as Form Q1
   - Required SEC filing for quarterly financial results
   - Contains unaudited financial statements
   - Due 40-45 days after quarter end
2. Examples:
   - `2025_Q1_10q.txt`
   - `2024_Q4_10q.txt`
3. Location: `quarterly/` directory
4. Content: Complete quarterly report filed with SEC

### Financial Statements
1. Format: `YYYY_MM/statement_type.md`
   - YYYY_MM: Year and month of data
   - statement_type: income_statement, balance_sheet, cashflow
   - .md: Markdown format
2. Examples:
   - `2025_05/income_statement.md`
   - `2025_05/balance_sheet.md`
   - `2025_05/cashflow.md`
3. Location: `financials/` directory
4. Content: Formatted financial data with analysis

### Analysis Documents
1. Format: `YYYY_MM_analysis_type.md`
   - YYYY_MM: Year and month of analysis
   - analysis_type: market, competitive, technical, financial, risk, investment_thesis, delta
   - .md: Markdown format
2. Examples:
   - `2025_05_market_analysis.md`
   - `2025_05_competitive_analysis.md`
   - `2025_05_delta_analysis.md` (changes/updates since prior analysis)
3. Location: `analysis/` directory
4. Content: Detailed analysis and research

**Delta Analysis Naming:**
- Created quarterly alongside full analysis or as standalone updates
- Format: `YYYY_MM_delta_analysis.md`
- Compares to prior quarter or full analysis
- Captures all material shifts in financials, operations, valuation, strategy, risks, and thesis

*Note: All file names should be lowercase with underscores for spaces. Use consistent extensions (.txt for press releases, .md for formatted documents).*

## Documentation Requirements

### Document Cross-References
- Each analysis document should reference related documents
- Use consistent section headers across documents
- Maintain chronological order in filenames
- Include links to source materials

> **See [Required Analysis Documents](#required-analysis-documents) (File Organization Standards section) for complete list of required documents and delta analysis guidance.**

## Valuation Analysis Framework

### 1. Comparable Company Analysis
- Identify relevant peer groups:
  * Direct competitors
  * Industry leaders
  * Similar business models
  * Growth stage peers
- Key metrics to analyze:
  * EV/Revenue
  * EV/EBITDA
  * Price/Sales
  * Price/Book
  * Growth rates
  * Margins
  * Return metrics
- Adjust for differences:
  * Growth stage
  * Market position
  * Business model
  * Geographic focus
  * Risk profile

### 2. Discounted Cash Flow Analysis
- Revenue projections:
  * Historical growth rates
  * Market size and penetration
  * Backlog analysis
  * Capacity constraints
  * Competitive position
- Margin assumptions:
  * Gross margin trends
  * Operating margin potential
  * EBITDA margin evolution
  * Working capital requirements
- Capital expenditure:
  * Infrastructure needs
  * Maintenance requirements
  * Growth investments
  * Technology upgrades
- Terminal value:
  * Growth rate assumptions
  * Market position
  * Competitive advantages
  * Industry dynamics

### 3. Sum of Parts Valuation
- Infrastructure value:
  * Current capacity
  * Contracted capacity
  * Power contracts
  * Location value
- Technology/IP value:
  * Patents and trademarks
  * Technical leadership
  * Performance benchmarks
  * Innovation pipeline
- Customer relationships:
  * Strategic partnerships
  * Revenue backlog
  * Contract values
  * Customer concentration
- Other assets:
  * Real estate
  * Equipment
  * Investments
  * Cash and securities

### 4. Scenario Analysis
- Bull Case:
  * Market leadership
  * Margin expansion
  * Growth acceleration
  * Market share gains
- Bear Case:
  * Execution challenges
  * Competitive pressure
  * Margin compression
  * Growth slowdown
- Base Case:
  * Moderate growth
  * Stable margins
  * Market share maintenance
  * Balanced risk/reward

### 5. Key Value Drivers
- Growth metrics:
  * Revenue growth
  * Market penetration
  * Customer acquisition
  * Product adoption
- Profitability metrics:
  * Gross margins
  * Operating margins
  * EBITDA margins
  * Return on capital
- Strategic advantages:
  * Market position
  * Technical leadership
  * Partnerships
  * Brand value

### 6. Risk Adjustments
- Financial risks:
  * Leverage
  * Liquidity
  * Capital requirements
  * Cash flow
- Operational risks:
  * Execution
  * Competition
  * Technology
  * Market
- External risks:
  * Regulatory
  * Economic
  * Industry
  * Geopolitical

### 7. Valuation Documentation
- Document all assumptions
- Explain methodology choices
- Provide sensitivity analysis
- Include peer comparisons
- Note key risks and mitigants
- Update regularly with new data

### 8. Monitoring Framework
- Key metrics to track:
  * Revenue growth
  * Margin trends
  * Capital efficiency
  * Market position
- Review points:
  * Quarterly earnings
  * Major announcements
  * Market changes
  * Competitive moves
- Update triggers:
  * Significant events
  * Market shifts
  * New information
  * Risk changes

## Repository Usage Notes

### For Investment Analysis
- This repository is documentation-focused with no executable code
- All analysis follows the framework defined in this document
- Cursor rules provide IDE-integrated guidance for consistent formatting
- Each company directory is self-contained with complete analysis materials

### Document Maintenance
- Update quarterly with new financial data
- Maintain chronological order in all directories
- Ensure all required analysis documents are created for comprehensive coverage
- Cross-reference between documents for coherent analysis narrative

### Analysis Standards
- Follow the comprehensive framework in this document for all analysis
- Maintain consistent formatting across all financial tables and documents
- Store raw data in quarterly/ before analysis
- Create complete documentation for each analysis session

## Data Collection & Financial Data Access

### Quick Reference

**Downloading a 10-Q:** Prefer **`data.sec.gov/submissions/CIK…json`** + **`curl`** to **`www.sec.gov/Archives/edgar/data/.../{primaryDocument}`** with a descriptive **`User-Agent`** (see **[README.md](README.md)** → **Downloading the primary 10-Q iXBRL `.htm` with curl**). Use **Obscura** when browse-edgar or Archives blocks plain HTTP.

**Parsing facts:** Prefer **ixbrlparse** or **`scripts/export_ixbrl_readable.py`** — iXBRL is a **flat fact store**: join **value + period + segments (context)** and **dedupe**; export **TSV/JSON**, not raw HTML. **Arelle `--facts`** was **not usable** on tested primary filings — README → **Parsing facts** → **Arelle caveat**. Full checklist: README → **How to think about iXBRL (checklist)**.

### Detailed Guides

See the following dedicated documents for complete information:

1. **[OBSCURA.md](OBSCURA.md)** — Obscura headless browser setup and usage
   - Quick start commands
   - All CLI options and features
   - Real-world test results (SEC EDGAR, Yahoo Finance, Seeking Alpha)
   - Troubleshooting and when to use alternatives

2. **[OBSCURA_SEC_EDGAR_RESULTS.md](OBSCURA_SEC_EDGAR_RESULTS.md)** — SEC EDGAR integration testing (verified working 2026-04-30)
   - Filing discovery and download workflow
   - 19+ Cloudflare 10-Q filings retrieved successfully (2-5 sec per request)
   - XBRL-formatted output contains complete financial statements
   - Performance benchmarks and reliability metrics

3. **[DATA_COLLECTION_STRATEGY.md](DATA_COLLECTION_STRATEGY.md)** — Practical workflow for quarterly financial updates
   - Three-phase data collection process (SEC EDGAR → APIs → manual supplements)
   - Recommended tools ranked by reliability (free APIs, no auth required)
   - Implementation roadmap with effort estimates
   - Data collection by company type (large cap, growth/mid-cap)

4. **[FINANCIAL_DATA_SOURCES.md](FINANCIAL_DATA_SOURCES.md)** — Reference for data sources and APIs
   - Complete breakdown of what's in each 10-Q filing
   - Tier 1 sources (free, no auth): SEC submissions JSON + Archives curl, Obscura fallback
   - Tier 2 sources (free signup): Alpha Vantage, Financial Modeling Prep, IEX Cloud
   - Transcript collection strategy (why NOT to scrape, where to get them free)
   - Data validation results (FMP API vs Yahoo Finance cross-checks)

### Key Concepts

- **10-Q is your foundation:** Contains ~90% of what you need for investment analysis (financials, MD&A, risk factors, guidance)
- **Obscura as fallback:** Works when browse-edgar or Archives rejects plain HTTP; full-browser fetch paths documented in **[OBSCURA.md](OBSCURA.md)**.
- **APIs are cleaner:** FMP, Alpha Vantage provide parsed financial data; less manual parsing
- **Primary 10-Q file:** Resolve **`primaryDocument`** from **`data.sec.gov/submissions/CIK….json`**, build **`Archives`** URL (hyphen-free accession segment), **`curl -L -o`** with a descriptive **`User-Agent`** — see **[README.md](README.md)** (*Downloading the primary 10-Q iXBRL `.htm` with curl*).
- **iXBRL fact extraction:** Treat filings as **tagged fact databases**, not finished statements — always interpret with **context** (period + dimensions). Prefer **ixbrlparse** + **[README.md](README.md)** checklist; **`scripts/export_ixbrl_readable.py`** for TSV/JSON. **Arelle** remains documented for DTS-heavy cases but **`--facts` output failed smoke tests** on sample primary `.htm` — see README **Arelle caveat**. Ad hoc: **lxml/ElementTree** on `ix:hidden` / inline tags when you only need a few concepts.

### Quick Workflow Example

```bash
# A) Curl path — primary iXBRL .htm (validated: Cloudflare NET, CIK 1477333)
#    1) Metadata (CIK is zero-padded to 10 digits in this URL only):
curl -sS -A "YourOrg ResearchBot contact@example.com" \
  -H "Accept: application/json" \
  "https://data.sec.gov/submissions/CIK0001477333.json" \
  -o /tmp/submissions.json

#    2) In filings.recent, pick index i where form[i]=="10-Q"; read accessionNumber[i], primaryDocument[i].
#    3) Archives URL = https://www.sec.gov/Archives/edgar/data/{CIK}/{ACCESSION_NO_HYPHENS}/{PRIMARY_DOCUMENT}

curl -sS -L -A "YourOrg ResearchBot contact@example.com" \
  "https://www.sec.gov/Archives/edgar/data/1477333/000147733325000141/cloud-20250930.htm" \
  -o /tmp/cloudflare_NET_10q_20250930_primary.htm

# B) Obscura fallback — browse-edgar listing / stubborn endpoints
obscura fetch "https://www.sec.gov/cgi-bin/browse-edgar?company=INTC" \
  --dump text | grep "CIK#"
obscura fetch "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q" \
  --dump html --wait 5000
obscura fetch "https://www.sec.gov/Archives/edgar/data/50863/...10q.txt" \
  --stealth --dump text --wait 8000 > filing.txt
```

---

## Meta-Instructions for AI Agents

When performing investment analysis:
1. This document serves as your primary instruction set
2. Follow the directory structure and file organization exactly as specified
3. Create ALL required analysis documents before providing summary analysis
4. Cross-reference between documents using proper markdown links
5. Maintain chronological order in filenames
6. Store raw data in appropriate directories before analysis
7. Never skip the documentation step - analysis without proper documentation is incomplete

### For Data Collection
- Use web scraping framework (see above) to automate data collection where possible
- Respect robots.txt and rate limits
- Use SEC APIs for reliable financial data access
- Fall back to manual collection for privacy-protected sites
- Document all data sources in quarterly/ directory
========
