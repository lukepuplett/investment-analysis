# IBM 10-Q Filings: Data Extraction Summary

**Status:** Successfully downloaded and parsed 2 10-Q filings from SEC EDGAR  
**Date:** 2026-05-04

## Filings Processed

| Quarter | Filing Date | Report Date | File | Size | Facts Extracted |
|---------|-----------|------------|------|------|-----------------|
| Q1 2026 | 2026-04-23 | 2026-03-31 | ibm-20260331.htm | 2,459 KB | 1,517 numeric |
| Q3 2025 | 2025-10-23 | 2025-09-30 | ibm-20250930.htm | 3,754 KB | 2,288 numeric |

## Data Extraction Process

### Step 1: SEC EDGAR API Lookup ✅
- Retrieved IBM submissions metadata from `data.sec.gov/submissions/CIK0000051143.json`
- Identified latest 10-Q filings and extracted metadata:
  - Filing dates, accession numbers, primary document filenames
  - Report dates, document descriptions

### Step 2: Document Download ✅
- Downloaded primary iXBRL .htm files from SEC Archives
- Used `curl` with descriptive User-Agent header
- Both files successfully retrieved from:
  - `https://www.sec.gov/Archives/edgar/data/51143/{accession}/{filename}`

### Step 3: XBRL Fact Extraction ✅
- Parsed iXBRL (Inline XBRL) markup using **ixbrlparse** (Python package)
- Extracted numeric facts, contexts, and metadata from financial markup
- Warnings: Expected SEC-specific format variations (date-monthname, state names, etc.)
  - Non-critical for numeric fact extraction

## Key Metrics Extracted

### Q1 2026 vs Q1 2025 Comparison

**Consolidated Revenues:**
- Q1 2026: $15,917M (U.S. + International)
- Q1 2025: $14,541M
- **Growth: +9.5% YoY**

**Cost of Revenue:**
- Q1 2026: $6,968M
- Q1 2025: $6,510M
- **Change: +7.0% YoY**

**Gross Profit:**
- Q1 2026: $8,949M (56.2% margin)
- Q1 2025: $8,031M (55.2% margin)
- **Margin expansion: +100 bps**

**Net Income Loss:**
- Q1 2026: $1,216M
- Q1 2025: $1,055M
- **Growth: +15.3% YoY**

### Revenue by Segment (Q1 2026 vs Q1 2025)

| Segment | Q1 2026 | Q1 2025 | Growth |
|---------|---------|---------|--------|
| Technology Services | $7,688M | $7,280M | +5.6% |
| Product | $8,009M | $7,070M | +13.3% |
| Financial Services | $220M | $191M | +15.2% |

## Financial Concepts Identified

### Income Statement Line Items
- Revenues (consolidated & by segment)
- Cost of Revenue (consolidated & by segment)
- Gross Profit
- Research & Development Expense
- Selling, General & Administrative Expense
- Operating Income
- Interest Income/Expense
- Net Income Loss (continuing & discontinued operations)
- Earnings Per Share (Basic & Diluted)

### Balance Sheet Line Items
- Total Assets (Current & Non-current)
- Cash and Cash Equivalents
- Accounts Receivable (Gross & Net)
- Inventory (Work in Process & Finished Goods)
- Property, Plant & Equipment (Gross & Accumulated Depreciation)
- Goodwill and Intangible Assets
- Total Liabilities (Current & Non-current)
- Accounts Payable
- Debt (Short-term & Long-term)
- Stockholders' Equity
- Retained Earnings
- Treasury Stock

### Cash Flow Line Items
- Operating Cash Flow
- Capital Expenditures
- Business Acquisitions (Net)
- Debt Issuance/Repayment
- Dividend Payments
- Stock Repurchases
- Free Cash Flow

## Files Generated

### Downloaded from SEC
- `2026_Q1_10q.htm` — Primary iXBRL document (2,459 KB)
- `2025_Q3_10q.htm` — Primary iXBRL document (3,754 KB)

### Extracted Data
- `2026_Q1_10q_facts.json` — 1,517 numeric facts with contexts
- `2025_Q3_10q_facts.json` — 2,288 numeric facts with contexts

## Next Steps

### Data Integration
1. Extract key statements from fact JSON into markdown tables:
   - Consolidated Income Statement (quarterly & YTD)
   - Consolidated Balance Sheet (period-end snapshot)
   - Consolidated Cash Flow Statement (quarterly)

2. Create segment breakdowns and trend analysis

3. Cross-reference with Yahoo Finance data already captured in financials/2026_03/

### Analysis Enhancement
- Document MD&A (Management Discussion & Analysis) sections
- Extract risk factors and management commentary
- Identify material changes from prior periods
- Build ratio analysis from fact data

### Validation
- Compare extracted metrics against Yahoo Stats already in repo
- Verify period-over-period consistency
- Identify any data anomalies

## Tools & Methodology

**SEC Access:**
- API: `data.sec.gov/submissions/{cik}.json`
- Download: `curl` with descriptive User-Agent
- Format: Primary iXBRL `.htm` files

**Parsing:**
- Tool: `ixbrlparse` (Python package, v0.11.2+)
- CLI: `ixbrlparse --format json --outfile {output} {input.htm}`
- Output: JSON with numeric facts, contexts, timestamps

**Data Model:**
- Facts: Tagged financial values with XBRL concepts
- Contexts: Period metadata (instant vs duration, segments, entity)
- Schemas: GAAP (US-GAAP) accounting taxonomy

## References

- **README.md** → Data Access Strategy section (full workflow)
- **DATA_COLLECTION_STRATEGY.md** → Phase 1 implementation details
- **OBSCURA_SEC_EDGAR_RESULTS.md** → Validation results & performance
- **ixbrlparse** documentation: https://github.com/Donnland/ixbrlparse

---

**Status:** ✅ Complete  
**Effort:** ~15 minutes for download + parsing of 2 quarters  
**Next:** Extract and structure financial statements from fact JSON
