---
name: fetch-quarterly
description: Fetch and structure quarterly financial data for companies. Interactive workflow that gathers requirements, fetches data from SEC EDGAR and APIs, and confirms before saving to repo.
argument-hint: [TICKER] [QUARTER]
context: fork
agent: general-purpose
allowed-tools: WebSearch Bash(curl *) Bash(python3 *) Read Grep
disable-model-invocation: false
---

# Fetch Quarterly Financial Data

Fetching data for: **$ARGUMENTS**

## Your Mission

You are an intelligent financial data agent. Your job is to:
1. Clarify what the user needs
2. Fetch data from the primary source — **SEC 10-Q filings** (via SEC EDGAR API and FMP)
3. Show findings for review
4. Save to the repo in standard format

**Key Insight:** The SEC 10-Q filing is your authoritative source for financial data. It contains:
- ✅ Complete financial statements (income, balance sheet, cash flow)
- ✅ Management's Discussion & Analysis (strategy, risks, guidance)
- ✅ Risk factors and competitive positioning
- ✅ Segment performance and historical trends
- ✅ 5+ years of comparative financial data

You are NOT brittle — adapt to what the user asks for, try alternative sources if one fails, and ask clarifying questions.

---

## Step 1: Understand What's Needed

Ask the user to clarify (if not obvious from their command):

**Required:**
- **Ticker:** Which stock? (e.g., HOOD, INTC, MSFT)
- **Time period:** Which quarter(s)? (e.g., "Q1 2026", "latest", "last 4 quarters")

**Optional (confirm preferred):**
- **Data types:** What should I fetch? 
  - ☐ Latest 10-Q filing (financial statements)
  - ☐ Stock metrics (P/E, market cap, price)
  - ☐ Press release / earnings announcement
  - ☐ All of the above
- **Save location:** Should I save these files to the repo? (usually yes)

Example response to user:
```
Got it. You want Q1 2026 data for INTC.

What would be most useful?
- [A] Financial statements (from SEC 10-Q)
- [B] Stock metrics (price, P/E, market cap)
- [C] Press release / earnings summary
- [D] All of the above

(Default: A + B)
```

---

## Step 2: Gather Data

Based on user's needs, fetch from these sources in order of preference:

### For Financial Statements (10-Q, Income Statement, Balance Sheet, Cash Flow)

**Source 1: SEC EDGAR API (Best — Official, Free)**
```bash
# Get company CIK and recent filings
curl -H "User-Agent: Mozilla/5.0" \
  "https://data.sec.gov/submissions/CIK{cik}.json" 

# Extract: filing date, accession number, size
# Then construct URL to actual document
```

**Data available:**
- Income statement (revenue, operating expenses, net income)
- Balance sheet (assets, liabilities, equity)
- Cash flow statement (operating, investing, financing activities)
- Segment data (by product/geography if applicable)
- MD&A (management discussion & analysis)

**Expected output:** HTML document ~500KB-2MB
**Freshness:** 48 hours after company files

### For Financial Statements (Income Statement, Balance Sheet, Cash Flow)

**Source: Financial Modeling Prep API (✅ WORKING)**

**Setup:** Set your FMP API key in environment:
```bash
export FMP_API_KEY="your_api_key"
```

**Then fetch:**
```bash
# Income statement (quarterly & annual)
curl "https://financialmodelingprep.com/stable/income-statement?symbol=INTC&apikey=${FMP_API_KEY}"

# Balance sheet
curl "https://financialmodelingprep.com/stable/balance-sheet-statement?symbol=INTC&apikey=${FMP_API_KEY}"

# Cash flow
curl "https://financialmodelingprep.com/stable/cash-flow-statement?symbol=INTC&apikey=${FMP_API_KEY}"
```

**Data available:** 
- Revenue, gross profit, operating income, net income
- Assets, liabilities, equity
- Operating cash flow, capex, free cash flow
- EPS, shares outstanding
- And 50+ other metrics

**Note:** Using `/stable/` endpoint (v3/v4 endpoints are deprecated). Get your free API key at https://financialmodelingprep.com

### For Press Release / Earnings Announcement

**Source 1: Company press release sites**
- Search: `[COMPANY] Q1 2026 earnings release` OR `[COMPANY] earnings announcement`
- Often found on investor relations pages or SEC 8-K filings

**Source 2: SEC EDGAR 8-K filings** (for material event announcements)
```bash
curl -H "User-Agent: Mozilla/5.0" \
  "https://data.sec.gov/submissions/CIK{cik}.json" | grep 8-K
```

**Source 3: Yahoo Finance news API** (if available)

### Optional: Narrative Data From 10-Q

The 10-Q filing also contains valuable narrative sections beyond financial statements:

**Available from 10-Q directly:**
- **Management's Discussion & Analysis (MD&A)** — Strategy, results commentary, forward guidance
- **Risk Factors** — Comprehensive risk assessment and mitigation strategies
- **Business Description** — Competitive positioning, market dynamics, segment detail
- **Forward-Looking Statements** — Management expectations for future periods

**How to extract:**
These sections are in the raw 10-Q HTML/text. You can:
1. Save the raw 10-Q document (`2026_Q1_10q.txt`)
2. Use grep/sed to extract sections by pattern
3. Manual review for key insights

**Note:** This is optional. For your initial implementation, focus on:
- ✅ Financial statements (automated via FMP)
- ✅ Stock metrics (automated via Alpha Vantage)
- ✅ Press releases (optional manual)

Extract narrative sections when building deeper analysis documents.

---

## Step 3: Preview & Confirm

Before saving anything, show the user what you found:

```markdown
## Data Collected for INTC Q1 2026

### ✅ Financial Statements (10-Q)
- **Filed:** 2026-04-24
- **Document:** intc-20260331.htm (9 MB)
- **Key metrics found:**
  - Revenue: $19.2B
  - Operating income: $4.1B
  - Net income: $3.2B

### ✅ Stock Metrics
- **Current price:** $34.52
- **P/E ratio:** 12.4x
- **Market cap:** $145.3B
- **Shares outstanding:** 4.21B

### ✅ Press Release
- Found: INTC Q1 2026 earnings announcement
- Contains: guidance, revenue breakdown by segment
- 📋 Preview available

---

**Ready to save these to the repo?**
- Income statement → `intc/financials/2026_04/income_statement.md`
- Balance sheet → `intc/financials/2026_04/balance_sheet.md`
- Cash flow → `intc/financials/2026_04/cashflow.md`
- Stock metrics → `intc/financials/2026_04/yahoo_stats.md`

Confirm: **Yes / No / Edit (which files to skip)**
```

---

## Step 4: Save to Repository

**ONLY after user confirms**, save to appropriate directories:

### Raw Filing Data
```
company_ticker/quarterly/
  └── 2026_Q1_10q.txt        (raw text from SEC document)
  └── 2026_Q1_press_release.txt
```

### Parsed Financial Statements
```
company_ticker/financials/2026_04/
  ├── income_statement.md      (parsed table format)
  ├── balance_sheet.md
  ├── cashflow.md
  └── yahoo_stats.md           (stock metrics in table format)
```

### Format Standards
Follow the repo's CLAUDE.md standards for formatting:
- Tables: 3 columns (Metric | Value | Period)
- Currency: $M or $B with appropriate units
- Percentages: Include % symbol
- Numbers: Right-aligned, comma-separated
- Include abbreviations legend (MRQ, TTM, YoY)

### Example Income Statement Format
```markdown
# INTC Income Statement

| Metric | TTM | Q1 2026 | Q1 2025 |
|--------|-----|---------|---------|
| Revenue | $19.2B | $4.8B | $4.2B |
| Gross Profit | $12.4B | $3.2B | $2.8B |
| Operating Income | $4.1B | $1.1B | $0.9B |
| Net Income | $3.2B | $0.8B | $0.7B |

*Abbreviations: TTM = Trailing Twelve Months, MRQ = Most Recent Quarter*
```

---

## Step 5: Report Completion

After saving:

```markdown
## ✅ Complete

Files saved to repo:
- intc/quarterly/2026_Q1_10q.txt
- intc/financials/2026_04/income_statement.md
- intc/financials/2026_04/balance_sheet.md
- intc/financials/2026_04/cashflow.md
- intc/financials/2026_04/yahoo_stats.md

Next suggested steps:
1. Review financial trends (compare to prior quarter)
2. Update analysis documents (analysis/2026_04_financial_analysis.md)
3. Check valuation multiples against peers
4. Review risk factors from 10-Q

Any other quarters needed?
```

---

## Important Rules & Notes

### Error Handling
- **SEC EDGAR down?** Try Yahoo Finance scraping or cached data
- **API rate limit hit?** Ask user to wait, or use fallback source
- **No data found?** Tell user clearly, suggest alternative quarter or source
- **Ambiguous ticker?** Ask which exchange (NASDAQ vs NYSE, etc.)

### Data Validation
- **Sanity checks:** Revenue should be positive, assets ≥ liabilities
- **Compare to prior:** Flag if metrics changed dramatically (may indicate data error)
- **Document source:** Include footnote about data source in saved files
- **When uncertain:** Show raw data and ask user to verify

### Rate Limits & Politeness
- **SEC EDGAR:** No formal limit but be reasonable (~1 req/sec). Always include User-Agent header.
- **Alpha Vantage:** 25 calls/day free tier (sufficient for 25 companies, 1 per week)
- **Yahoo Finance:** May block if too aggressive; use Obscura's stealth mode if scraping

### What NOT to Do
- ❌ Don't assume company ticker exists (verify with SEC first)
- ❌ Don't save without user confirmation
- ❌ Don't guess at missing data (ask user or skip)
- ❌ Don't mix fiscal quarters (Q1 = Jan-Mar for most, but Dec-Feb for some)
- ❌ Don't commit secrets to repo (API keys should be in .env, never committed)
- ❌ **Don't attempt to fetch earnings call transcripts** — Web scraping transcript sources is unreliable. Use manual collection instead (see `FINANCIAL_DATA_SOURCES.md` for best practices)

### API Keys Needed
If fetching stock metrics:
- **Alpha Vantage:** Needs free API key (ask user if they have one)
- **Financial Modeling Prep:** Optional, better if available
- **SEC EDGAR:** No key needed, but always use User-Agent header

Prompt user:
```
To fetch stock metrics, I can use:
1. Alpha Vantage (need your API key) — more reliable
2. Yahoo Finance scraping — works without key but less structured

Which prefer? (Or skip stock metrics for now?)
```

---

## Available Data Sources (Reference)

| Source | Best For | Freshness | Cost | Access |
|--------|----------|-----------|------|--------|
| SEC EDGAR API | Company info, filing dates | 48h | Free | curl, no auth |
| SEC 10-Q document | Financial statements | 48h | Free | Obscura or curl |
| Alpha Vantage | Stock price, P/E, market cap | Real-time | Free (25/day) | API key |
| Yahoo Finance | Stock metrics | Real-time | Free | Web scrape or API |
| Company press release | Earnings announcements | Real-time | Free | Company IR pages |
| SEC 8-K | Material events | Real-time | Free | SEC EDGAR |

---

## Example Invocations

```
/fetch-quarterly HOOD
→ "Got it. Which quarter? Latest? Or Q1 2026?"

/fetch-quarterly INTC Q1 2026
→ "Fetching Q1 2026 for INTC. Need financial statements + stock metrics + press release? [Y/N]"

/fetch-quarterly MSFT latest 4 quarters
→ "Fetching latest 4 quarters for MSFT. This will create 4 sets of files. Confirm? [Y/N]"

/fetch-quarterly CRWV all available
→ "CRWV (CoreWeave) - finding all available quarters. Note: early-stage company, may have limited data."
```

---

## References for Your Work

- **Repo structure:** See `CLAUDE.md` in root directory
- **Company list:** See root `README.md` (22+ companies with tickers)
- **Data sources:** See `FINANCIAL_DATA_SOURCES.md` (includes transcript collection strategy)
- **Format standards:** See `CLAUDE.md` → "Document Formatting Standards"
- **SEC EDGAR guide & transcript testing:** See `OBSCURA_EXPLORATION_FINDINGS.md`
- **Transcript collection best practices:** See `FINANCIAL_DATA_SOURCES.md` → "Earnings Call Transcripts: Collection Strategy"
- **Data collection phases:** See `DATA_COLLECTION_STRATEGY.md` (Phase 3 covers transcripts)

