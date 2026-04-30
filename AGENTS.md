# AGENTS.md

**⚠️ CRITICAL RULES:**
1. **Do NOT use `cat`, `echo`, or shell output redirection to communicate with the user.** Write responses directly in the chat instead. Shell commands are for operations only, not communication.
2. **Do NOT create temporary .md documentation files just to communicate.** Only create documentation files that will be long-lived and part of the repository. Communicate analysis, findings, and summaries directly in chat instead.

This file provides comprehensive guidance for AI agents when working with this investment analysis repository.

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
├── quarterly/                   # Raw quarterly data
│   ├── YYYY_Q#_form_10Q.txt/.md
│   ├── YYYY_Q#_presentation.txt/.md
│   └── YYYY_Q#_press_release.txt
└── question_answers/            # Q&A documentation
    └── YYYY_MM_DD_topic.md
```

### Key Components

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
For comprehensive analysis, create all of these documents in the `analysis/` directory:
1. `YYYY_MM_DD_financial_analysis.md` - Financial metrics and health assessment
2. `YYYY_MM_DD_market_analysis.md` - Market position and industry trends  
3. `YYYY_MM_DD_competitive_analysis.md` - Competitive position and advantages
4. `YYYY_MM_DD_technical_analysis.md` - Technical capabilities and risks
5. `YYYY_MM_DD_risk_assessment.md` - Comprehensive risk analysis
6. `YYYY_MM_DD_investment_thesis.md` - Overall investment thesis and recommendations
7. `YYYY_MM_DD_valuation_analysis.md` - Valuation methodology and price targets

### File Naming Conventions
- **Analysis documents**: `YYYY_MM_DD_[analysis_type].md`
- **Financial statements**: `YYYY_MM/[statement_type].md` 
- **Quarterly filings**: `YYYY_Q#_[document_type].txt` or `.md`
- **Q&A documents**: `YYYY_MM_DD_[topic].md`
- All filenames use lowercase with underscores for spaces
- Maintain chronological order in all directories

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

## Analysis Workflow

### Document Creation Process
1. **Data Collection**: Gather quarterly financial statements, market data, company announcements
2. **Analysis Process**: Create ALL required analysis documents before providing summary analysis
3. **Documentation**: Store raw data in appropriate directories, ensure cross-referencing between documents
4. **Review and Update**: Quarterly performance review, monthly position checks

### Cross-Referencing Requirements
- Each analysis document should reference related documents
- Use consistent section headers across documents
- Maintain chronological order in filenames
- Include links to source materials in quarterly/ directory

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

## Analysis Workflow
1. Data Collection
   - Gather quarterly financial statements
   - Collect market data
   - Track company announcements
   - Monitor industry news
   - Track capacity metrics

2. Analysis Process
   - Create all required analysis documents
   - Update financial models
   - Review competitive position
   - Assess growth catalysts
   - Evaluate risks
   - Update valuation
   - Check assumptions

3. Documentation
   - Store raw data in appropriate directories
   - Create all required analysis documents
   - Update key metrics
   - Maintain investment thesis
   - Track scenario outcomes
   - Ensure cross-referencing between documents

4. Review and Update
   - Quarterly performance review
   - Monthly market position check
   - Weekly news monitoring
   - Daily price tracking
   - Capacity utilization updates

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

### Required Analysis Documents
For each analysis session, create the following documents in the `analysis/` directory:
1. `YYYY_MM_market_analysis.md`: Market position and industry trends
2. `YYYY_MM_competitive_analysis.md`: Competitive position and advantages
3. `YYYY_MM_technical_analysis.md`: Technical capabilities and risks
4. `YYYY_MM_financial_analysis.md`: Financial metrics and health
5. `YYYY_MM_risk_assessment.md`: Comprehensive risk analysis
6. `YYYY_MM_investment_thesis.md`: Overall investment thesis and recommendations
7. `YYYY_MM_delta_analysis.md`: Changes and shifts since previous assessment (quarterly or major updates)

**Delta Analysis Document:**
The delta document captures material changes since the last analysis round. It serves as a quick reference for what has shifted and allows for focused monitoring between full analysis cycles. Include:
- **Financial metric changes** (revenue, margins, profitability, cash flow, debt levels)
- **Operational changes** (customer mix, market share, segment performance, efficiency metrics)
- **Valuation shifts** (stock price movement, multiples, relative value vs peers)
- **Strategic updates** (new products, market expansion, M&A, partnerships)
- **Risk changes** (new risks emerged, previous risks resolved/worsened, regulatory changes)
- **Competitive landscape shifts** (competitor moves, market dynamics)
- **Management commentary changes** (guidance updates, tone shifts, capital allocation changes)
- **Key ratio changes** (profitability, leverage, returns, efficiency)
- **Investment thesis impact** (which thesis pillars are validated/challenged)

### Document Cross-References
- Each analysis document should reference related documents
- Use consistent section headers across documents
- Maintain chronological order in filenames
- Include links to source materials

### Analysis Workflow
1. Data Collection
   - Gather quarterly financial statements
   - Collect market data
   - Track company announcements
   - Monitor industry news
   - Track capacity metrics

2. Analysis Process
   - Create all required analysis documents
   - Update financial models
   - Review competitive position
   - Assess growth catalysts
   - Evaluate risks
   - Update valuation
   - Check assumptions

3. Documentation
   - Store raw data in appropriate directories
   - Create all required analysis documents
   - Update key metrics
   - Maintain investment thesis
   - Track scenario outcomes
   - Ensure cross-referencing between documents

4. Review and Update
   - Quarterly performance review
   - Monthly market position check
   - Weekly news monitoring
   - Daily price tracking
   - Capacity utilization updates

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

## Web Scraping & Data Acquisition Framework

### ⭐ RECOMMENDED: Obscura + SEC EDGAR (Verified Working - 2026-04-30)

**For accessing SEC filings, use Obscura headless browser.** It bypasses SEC's bot detection and works reliably where direct HTTP fails.

#### Quick Workflow
```bash
# 1. Find company CIK by name
obscura fetch "https://www.sec.gov/cgi-bin/browse-edgar?company=cloudflare&owner=exclude&action=getcompany" \
  --dump text | grep "CIK#"

# 2. Get all 10-Q filings
obscura fetch "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001477333&type=10-Q&count=100" \
  --dump html --wait 5000

# 3. Download specific 10-Q document
obscura fetch "https://www.sec.gov/Archives/edgar/data/1477333/000147733325000141/0001477333-25-000141.txt" \
  --stealth --dump text --wait 8000
```

**Results:** 
- ✅ 19+ historical Cloudflare 10-Q filings retrieved successfully
- ✅ Performance: 2-5 seconds per request
- ✅ Bypass SEC bot detection via `--stealth` mode
- ✅ XBRL-formatted output contains all financial statements

**See: OBSCURA_SEC_EDGAR_RESULTS.md for complete test results and workflow**

---

### Legacy: Three-Phase Scraping System

Production-ready three-phase scraping system for collecting financial data and research materials:

### Phase 1: HTML Acquisition - `acquire-html.js`

**Smart URL downloader with intelligent blocker detection**

```bash
node acquire-html.js \
  --output ./output_dir \
  --urls "url1,url2,url3" \
  [--initial "url_for_initial_load"] \
  [--modal <strategy>]
```

**Key Features:**
- ✅ Smart blocker detection (CAPTCHA, bot detection, access denied, privacy modals)
- ✅ Waits intelligently for blocking UI to disappear
- ✅ Detects when real content appears and auto-continues
- ✅ URL-based modal strategy selection (wait-for-accept, auto-click, detect, none)
- ✅ Handles JavaScript-rendered content with real Chrome
- ✅ Creates manifest.json with download log

**Modal Strategies:**
- `wait-for-accept` - Waits for user to manually click (Yahoo Finance, LinkedIn)
- `auto-click` - Tries to auto-click Accept button (Facebook, generic modals)
- `detect` - Smart detection and fallback to auto-click
- `none` - Skip modal handling (SEC, company IR pages)
- `auto` - Auto-detect per URL domain (default)

**Example:**
```bash
# Auto-detect strategy per URL
node acquire-html.js --output ./data --initial "https://finance.yahoo.com/quote/CVCO" \
  --urls "https://finance.yahoo.com/quote/CVCO,https://www.sec.gov/cgi-bin/browse-edgar?..."

# Force wait-for-accept strategy
node acquire-html.js --output ./data --urls "https://finance.yahoo.com/..." --modal wait-for-accept

# Skip modals (SEC EDGAR, company IR)
node acquire-html.js --output ./data --urls "https://www.sec.gov/...,https://company.com" --modal none
```

### Phase 2: HTML Refinement - `lib-html-refiner.js`

**Strips HTML noise and extracts clean content structure**

```bash
node lib-html-refiner.js input.html output_refined.json
```

**Outputs:**
- Clean text content (scripts, styles, nav removed)
- Extracted tables with row/cell structure
- Navigation URLs (internal + external classified)
- Main content section
- Metadata and statistics

**Results Format:**
```json
{
  "metadata": { "stats": { "tableCount": 5, "navUrlCount": 45 } },
  "content": { "text": "...", "tables": [...], "mainContent": "..." },
  "navigation": { "urls": [...] }
}
```

### Phase 3: Financial Data Extraction - `lib-financial-extractor.js`

**Extract financial metrics from refined HTML**

```javascript
const extractor = new FinancialExtractor();
const data = extractor.extractFromHTML(html, 'yahoo-finance');
```

**Supports:**
- Yahoo Finance format (price, PE, EPS, beta, market cap, etc.)
- Extensible for other financial sources

### Workflow for Investment Analysis

**Step 1: Acquire Raw HTML**
```bash
node acquire-html.js \
  --output ./CVCO/financials/2025_02/raw_html \
  --initial "https://finance.yahoo.com/quote/CVCO" \
  --urls "https://finance.yahoo.com/quote/CVCO,https://finance.yahoo.com/quote/CVCO/analysis"
```

**Step 2: Refine HTML to Extract Structure**
```bash
node lib-html-refiner.js ./raw_html/quote__cvco.html ./refined/quote_refined.json
```

**Step 3: Extract Financial Data**
```javascript
const data = extractor.extractFromHTML(refinedData.content.text, 'yahoo-finance');
```

**Step 4: Acquire Additional Sources**
```bash
# SEC filings
node acquire-html.js --output ./sec_docs --urls "https://www.sec.gov/..." --modal none

# Earnings transcripts (handles bot detection intelligently)
node acquire-html.js --output ./transcripts --urls "https://seekingalpha.com/..." --modal detect
```

**Step 5: Create Analysis Documents**
- Use acquired and refined data for the 7 required analysis documents
- Follow directory structure in AGENTS.md

### Key Capabilities
- ✅ Intelligent blocker detection (CAPTCHA, modals, rate limiting, access denied)
- ✅ Auto-waits for blocking UI to disappear, continues when real content appears
- ✅ Works on any website (financial sites, SEC EDGAR, company IR, news sites)
- ✅ Handles JavaScript-rendered content with real Chrome
- ✅ Extracts clean content + navigation + tables from ANY page
- ✅ Specialized financial data extraction available
- ✅ Manifest tracking (what succeeded/failed per URL)

---

## Data Access Strategy - Complete Workflow (2026-04-30)

### ✅ What Works: Obscura + SEC EDGAR + XBRL Parsing

**Tested and Verified:**
- ✅ **Retrieval:** 100% success rate via Obscura (19+ Cloudflare 10-Qs retrieved, 2-5 sec/request)
- ✅ **XBRL Parsing:** Standard libraries (lxml, ElementTree) parse hidden XBRL perfectly
- ✅ **Fact Extraction:** 1,000+ financial facts extractable per 10-Q
- ✅ **Production-Ready:** Complete workflow documented, tested, automatable

**Key Discovery:** iXBRL contains **pure XML `<ix:hidden>` section** + inline XBRL facts. Both parseable with standard Python libraries (no specialized XBRL parsers needed).

### 📋 Agent Workflow: Parse 10-Q from Ticker

**12-Step Process (Agent-Executable):**

#### **1-3: Discovery Phase**
1. Find CIK from ticker (Obscura search)
2. Get filing list with dates (Obscura + parse HTML)
3. Filter to target quarter/year

#### **4: Retrieval Phase**
4. Download iXBRL HTML document (Obscura + stealth mode, ~2 sec)

#### **5-9: Extraction Phase**
5. Extract namespace declarations from HTML root
6. Extract `<ix:hidden>` section (regex, pure XBRL)
7. Parse hidden XBRL metadata (lxml/ElementTree)
8. Extract context definitions (period mappings)
9. Extract inline XBRL facts from HTML body (1,000+ facts)

#### **10-12: Aggregation & Output Phase**
10. Aggregate facts by statement type (Balance Sheet, Income Statement, Cash Flow)
11. Format output (JSON, markdown, or CSV)
12. Save to repo in standard directory structure

**Expected Output:**
```
✅ net/financials/2025_09/balance_sheet.json
✅ net/financials/2025_09/income_statement.json
✅ net/financials/2025_09/cash_flow.json
✅ net/quarterly/2025_Q3_10Q_parsed.json
```

### 🔧 Technical Details for Implementation

**Libraries Required:**
- `lxml` or `xml.etree.ElementTree` (XML parsing)
- `regex` (pattern extraction)
- Built-in `json` (output)

**Key Patterns:**
```python
# Extract hidden section
hidden = re.search(r'<ix:hidden>(.*?)</ix:hidden>', html, re.DOTALL).group(1)

# Parse with namespace awareness
ns = {'ix': 'http://www.xbrl.org/2013/inlineXBRL'}
facts = root.xpath('.//ix:nonfraction', namespaces=ns)

# Map contexts to periods
for fact in facts:
    context_id = fact.get('contextref')
    period = contexts[context_id]  # Maps to Q3 2025, TTM, etc.
```

**Performance:**
- Download: ~3 seconds (Obscura)
- Parse & Extract: ~2 seconds (Python)
- Total: ~5 seconds per 10-Q

### 📊 Three-Tier Data Strategy (Hybrid)

**Tier 1: SEC EDGAR via Obscura** ✅ AUTOMATED
- Authoritative historical financials (5+ years)
- 1,000+ facts per quarter
- XBRL parsing complete, no manual work

**Tier 2: Market Data (Current Valuations)**
- Stock price, P/E, market cap
- User pastes from Yahoo or API
- Quick update before analysis

**Tier 3: Qualitative Data**
- Earnings transcripts, competitive intel
- Manual collection as needed
- Feeds into thesis validation

### ✅ What Was Learned

**XBRL is parseable:**
- Hidden section = pure XML, parses with lxml/ElementTree
- Inline facts = XML tags mixed in HTML, extractable via regex
- Context mapping = period definitions in filing, deterministic lookup
- No specialized XBRL parsers needed for basic extraction

**Parser Testing Results:**
- ✅ lxml: Works perfectly (4 numeric + 6 non-numeric facts extracted)
- ✅ ElementTree: Works perfectly (standard library)
- ❌ py-xbrl: API issues (abstract class)
- ❌ ixbrl-parse: Import issues (but available)
- ⚠️ fast_xbrl_parser: Designed for full SEC filings, overkill

**Conclusion:** Build custom parser using lxml/ElementTree (100 lines) vs. debugging specialized libraries (1-2 hours). ROI strongly favors custom approach.

### 🚀 Path Forward

**Immediate (Next Sprint):**
- Build 12-step parser in Python (~200 lines, modular)
- Integrate with Obscura workflow
- Test on 5 companies, multiple years
- Validate output vs. SEC EDGAR

**Scaling (After Validation):**
- Batch processing (process multiple companies)
- Caching layer (don't re-download)
- Rate limit management (10 req/sec SEC limit)
- Error recovery (retry logic, validation)

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
