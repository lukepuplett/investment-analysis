# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an investment analysis repository for tracking and analyzing public companies. The repository contains structured financial analysis and research materials for three companies:
- **CRWV**: CoreWeave - AI hyperscaler specializing in GPU-accelerated computing
- **MNTN**: MNTN, Inc. - Performance TV advertising company focusing on CTV advertising
- **RKLB**: Rocket Lab - Aerospace company providing launch services and space systems

## Architecture & Structure

### High-Level Organization
The repository follows a company-based directory structure where each company (crwv/, mntn/, rklb/) contains identical subdirectories for consistent analysis:

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
└── quarterly/                   # Raw quarterly data
    ├── YYYY_Q#_form_10Q.txt/.md
    ├── YYYY_Q#_presentation.txt/.md
    └── YYYY_Q#_press_release.txt
```

### Key Components

**Analysis Framework**: The root `llms.txt` file contains the comprehensive investment analysis framework that governs all analysis in this repository. It defines:
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

## Repository Usage Notes

### For Investment Analysis
- This repository is documentation-focused with no executable code
- All analysis follows the framework defined in `llms.txt`
- Cursor rules provide IDE-integrated guidance for consistent formatting
- Each company directory is self-contained with complete analysis materials

### Document Maintenance
- Update quarterly with new financial data
- Maintain chronological order in all directories
- Ensure all required analysis documents are created for comprehensive coverage
- Cross-reference between documents for coherent analysis narrative

### Analysis Standards
- Follow the comprehensive framework in `llms.txt` for all analysis
- Maintain consistent formatting across all financial tables and documents
- Store raw data in quarterly/ before analysis
- Create complete documentation for each analysis session