<<<<<<<< HEAD:AGENTS.md
# AGENTS.md

This file provides comprehensive guidance for AI agents when working with this investment analysis repository.

## Repository Overview

This is an investment analysis repository for tracking and analyzing public companies. The repository contains structured financial analysis and research materials for multiple companies including:
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
   - analysis_type: market, competitive, technical, etc.
   - .md: Markdown format
2. Examples:
   - `2025_05_market_analysis.md`
   - `2025_05_competitive_analysis.md`
3. Location: `analysis/` directory
4. Content: Detailed analysis and research

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

## Meta-Instructions for AI Agents

When performing investment analysis:
1. This document serves as your primary instruction set
2. Follow the directory structure and file organization exactly as specified
3. Create ALL required analysis documents before providing summary analysis
4. Cross-reference between documents using proper markdown links
5. Maintain chronological order in filenames
6. Store raw data in appropriate directories before analysis
7. Never skip the documentation step - analysis without proper documentation is incomplete
========

>>>>>>>> 0ca2ccd09a2932b8a9ca475226e6984397dc2aee:llms.txt
