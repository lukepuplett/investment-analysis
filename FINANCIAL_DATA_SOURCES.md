# Financial Data Sources Reference

Quick lookup for data sources, APIs, and scraping methods.

## ⭐ Core Insight: 10-Q is Your Primary Source

The SEC Form 10-Q contains almost everything needed for investment analysis. See below for complete breakdown of what's included vs what requires separate sources.

### What's Inside Each 10-Q Filing
| Content | Included | Source |
|---------|----------|--------|
| **Income Statement** | ✅ YES | Part I, Item 1 |
| **Balance Sheet** | ✅ YES | Part I, Item 1 |
| **Cash Flow Statement** | ✅ YES | Part I, Item 1 |
| **5+ Year History** | ✅ YES | Financial statements tables |
| **MD&A (Strategy)** | ✅ YES | Part I, Item 2 |
| **Risk Factors** | ✅ YES | Part I, Item 1A |
| **Business Description** | ✅ YES | Part I, Item 1 |
| **Segment Performance** | ✅ YES | Part I, Item 1 (Financial Statements) |
| **Management Guidance** | ✅ YES | Part I, Item 2 (MD&A) |
| **Earnings Call Transcript** | ❌ NO | Separate source (Seeking Alpha, IR) |
| **Stock Price Data** | ❌ NO | Separate source (Yahoo, Alpha Vantage) |
| **Real-time Events** | ❌ NO | SEC 8-K filings or news sources |

### Collection Priority
1. **Primary:** Historical 10-Q filings (via SEC EDGAR API)
2. **Secondary:** FMP API for parsed financial data (convenience)
3. **Tertiary:** Earnings call transcripts (manual, quarterly)
4. **Optional:** Stock metrics APIs, news aggregators

### Parsing SEC Inline XBRL (primary `.htm` 10-Q / 10-K)

Validated approaches on repo-standard machines:

| Tool | Install | Typical use |
|------|---------|-------------|
| **ixbrlparse** | `pip install ixbrlparse` | **Default for fact lists.** Python API `IXBRL.open(path)` or CLI with **`--format`** and **stdin** (avoid `-f` for file paths — it maps to **`--format`**). Pair with **`scripts/export_ixbrl_readable.py`** for TSV/JSON tuned for grep / LLMs. |
| **Arelle** | `pip install arelle-release` | Full DTS processor; **`--facts` exports failed repo smoke tests on Cloudflare primary iXBRL** — see README → **Parsing facts** → **Arelle caveat**. |

Full workflow (mental model + copy-paste): **[README.md](README.md)** → **Data Access Strategy: SEC EDGAR via Obscura** → **Parsing facts from SEC iXBRL filings**.

### ✅ Tested iXBRL Parsing Workflow (Validated 2026-05-01)

**Problem:** ElementTree and manual XML parsing cannot extract facts from iXBRL—the namespace complexity requires a specialized parser.

**Solution:** Use `ixbrlparse` CLI with JSON output.

**Step 1: Download 10-Q iXBRL filing**
```bash
# Get CIK, accession, primaryDocument from SEC EDGAR API (see below)
curl -sS -L -A "Investment Research Bot contact@example.com" \
  "https://www.sec.gov/Archives/edgar/data/{CIK}/{ACCESSION_NO_HYPHENS}/{PRIMARY_DOCUMENT}" \
  -o filing.htm
```

**Step 2: Parse with ixbrlparse**
```bash
# Options first, then input file
ixbrlparse --format json --outfile facts.json filing.htm
```

**Step 3: Extract facts from JSON**
```python
import json
with open('facts.json') as f:
    data = json.load(f)

# Numeric facts (revenue, income, etc.)
numeric = data['numeric']  # List of {name, value, context, unit, ...}

# Find a specific fact
revenue = [f for f in numeric if 'RevenueFromContractWithCustomer' in f['name']]
# Output: [{'name': '...', 'value': 885651000.0, 'context': 'c-10', ...}]

# Cross-reference context to get period
contexts = data['contexts']
period = contexts['c-10']  # {'entity': {...}, 'startdate': '2025-07-01', 'enddate': '2025-09-30', ...}
```

**Why this works:**
- ixbrlparse handles XBRL namespace resolution automatically
- JSON output maps facts to contexts (periods) by ID
- Each fact has `{name, value, context, unit}` — cross-reference `context` to `contexts` dict to get period dates
- Success: parsed Datadog Q3 2025 10-Q in <1 second, extracted 933 numeric facts

**Example output (Datadog Q3 2025):**
| Fact | Value | Period |
|------|-------|--------|
| RevenueFromContractWithCustomerExcludingAssessedTax | 885,651,000 | Q3 2025 (7/1-9/30) |
| GrossProfit | 709,194,000 | Q3 2025 |
| NetIncomeLoss | 33,885,000 | Q3 2025 |

---

## ✅ WORKING NOW: Financial Modeling Prep

**Endpoint:** `/stable/income-statement?symbol=[TICKER]&apikey=$FMP_API_KEY`

**Also available:**
- `/stable/balance-sheet-statement`
- `/stable/cash-flow-statement`

**Returns:** Clean JSON with quarterly & annual financial data (Revenue, Net Income, Assets, Cash Flow, EPS, etc.)

**Setup:**
```bash
export FMP_API_KEY="your_key_here"
```

**Usage in skill:**
```bash
curl "https://financialmodelingprep.com/stable/income-statement?symbol=INTC&apikey=${FMP_API_KEY}"
```

## Primary Sources (Free, No Auth)

| Data | Source | Method | Freshness |
|------|--------|--------|-----------|
| **Company info, CIK, filings list** | SEC EDGAR API | `curl https://data.sec.gov/submissions/CIK{cik}.json` | 48h after filing |
| **Financial statements** | SEC 10-Q/10-K iXBRL `.htm` | Submissions JSON + `curl` to Archives URL (+ ixbrlparse / export script); Obscura fallback | 48h after filing |
| **Material events** | SEC 8-K filings | SEC EDGAR API | Real-time |
| **Macro data** | Federal Reserve FRED | API: `https://api.stlouisfed.org/fred/series/GDP` | Monthly |

## Stock Data (Free Tier Available)

| Data | Source | Endpoint | Freshness | Works? |
|------|--------|----------|-----------|--------|
| **Income statement** | Financial Modeling Prep | `/stable/income-statement?symbol=INTC` | Quarterly | ✅ YES |
| **Balance sheet** | Financial Modeling Prep | `/stable/balance-sheet-statement?symbol=INTC` | Quarterly | ✅ YES |
| **Cash flow** | Financial Modeling Prep | `/stable/cash-flow-statement?symbol=INTC` | Quarterly | ✅ YES |
| **Quote data** | Alpha Vantage | `/query?function=OVERVIEW&symbol=INTC` | Real-time | ⚠️ Need key |

**FMP API Key:** Already have a working demo key (see FINANCIAL_DATA_SOURCES.md for current key)
- Use the `/stable/` endpoints (v3 endpoints are deprecated)
- Returns clean JSON with all financial metrics
- No signup needed if using provided key

## News & Transcripts

| Data | Source | Method | Cost |
|------|--------|--------|------|
| **Press releases** | Company IR RSS feeds | Monitor for RSS | Free |
| **Earnings transcripts** | Seeking Alpha | Manual collection or Selenium scrape | Free (manual), $$ (automated) |
| **News mentions** | Yahoo Finance News | Web scraping or news API | Free |

## What Each Option Gets

### Option A: Filing Checklist
```
Source: SEC EDGAR API only
Data: Company names, latest 10-Q dates, filing links
Freshness: 48 hours
Cost: Free
Effort: 1 hour
```

### Option B: Quarterly Snapshot
```
Sources:
  - SEC 10-Q documents (via Obscura)
  - Alpha Vantage API (stock metrics)
  - SEC EDGAR API (company/filing metadata)

Data:
  - Financial statements (income, balance sheet, cash flow)
  - Stock metrics (P/E, market cap, shares)
  - Management commentary (from 10-Q MD&A)

Freshness: 48 hours (quarterly)
Cost: Free (after 5 min Alpha Vantage signup)
Effort: 4-6 hours to build, ~30 min per company to run
```

### Option C: Real-Time System
```
Option B data PLUS:
  - Earnings transcripts (Seeking Alpha, manual or Selenium)
  - 8-K alerts (SEC EDGAR API monitoring)
  - Stock price trends (daily Alpha Vantage fetches)
  - Insider transactions (SEC Form 4 API)

Freshness: Real-time (8-K/news), Real-time (stock), Quarterly (transcripts)
Cost: Free to ~$500/year (if transcript service)
Effort: 1-2 days to build, ~1 hour/week to maintain
```

## API Setup (5 minutes each)

**Alpha Vantage:**
- Go to https://www.alphavantage.co/support/#api-key
- Enter email, click "GET FREE API KEY"
- Use in: `https://www.alphavantage.co/query?function=OVERVIEW&symbol=INTC&apikey=KEY`

**Financial Modeling Prep:**
- Go to https://site.financialmodelingprep.com
- Click "Sign up", enter email
- Free tier: 100 calls/day
- Use in: `https://financialmodelingprep.com/api/v3/quote/INTC?apikey=KEY`

**SEC EDGAR API:**
- No signup needed
- Always use User-Agent header: `-H "User-Agent: Mozilla/5.0"`
- Free, no rate limit (be reasonable)

## Common Scraping Patterns

**Get company CIK number:**
```bash
curl -H "User-Agent: Mozilla/5.0" \
  "https://data.sec.gov/submissions/CIK0000050863.json" | \
  jq '.name'
```

**Get recent 10-Q metadata:**
```bash
curl -H "User-Agent: Mozilla/5.0" \
  "https://data.sec.gov/submissions/CIK0000050863.json" | \
  jq '.filings.recent | [.form, .filingDate, .accessionNumber] | transpose | map(select(.[0]=="10-Q")) | .[0:3]'
```

**Include `primaryDocument` when picking a filing** — In `filings.recent`, **`form`**, **`accessionNumber`**, **`filingDate`**, and **`primaryDocument`** are parallel arrays (same index `i`). Choose `i` where `form[i]=="10-Q"`, then read `accessionNumber[i]` and `primaryDocument[i]`.

```bash
# Peek first rows (adjust slice); identify index i for target 10-Q
curl -sS -A "YourOrg ResearchBot contact@example.com" \
  "https://data.sec.gov/submissions/CIK0001477333.json" | \
  jq '.filings.recent | {form: .form[0:15], accession: .accessionNumber[0:15], doc: .primaryDocument[0:15]}'
```

**Download primary 10-Q iXBRL `.htm` from Archives (curl)** — After you have **numeric CIK** (no zero-padding), **accession**, and **`primaryDocument`** from step above:

```
https://www.sec.gov/Archives/edgar/data/{CIK}/{ACCESSION_WITHOUT_HYPHENS}/{PRIMARY_DOCUMENT}
```

Example (Cloudflare NET, tested): accession `0001477333-25-000141`, primary `cloud-20250930.htm`:

```bash
curl -sS -L -A "YourOrg ResearchBot contact@example.com" \
  "https://www.sec.gov/Archives/edgar/data/1477333/000147733325000141/cloud-20250930.htm" \
  -o /tmp/cloudflare_10q.htm
```

Full narrative: **[README.md](README.md)** → **Downloading the primary 10-Q iXBRL `.htm` with curl**.

**Fetch/browse filings HTML via Obscura** (when browse-edgar or curl misbehaves):

```bash
timeout 8 ~/Git/Hub/obscura/target/release/obscura fetch \
  "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q" \
  --wait 2000 --dump text
```

**Get stock metrics:**
```bash
curl "https://www.alphavantage.co/query?function=OVERVIEW&symbol=INTC&apikey=KEY" | jq '.PERatio, .MarketCapitalization'
```

## Files to Create for Data Collection

1. **config/companies.csv** - Ticker → CIK mapping
2. **config/api_keys.env** - Alpha Vantage + FMP keys (never commit)
3. **scripts/fetch-quarterly.js** - Main data fetcher
4. **scripts/parse-10q.js** - Extract tables from 10-Q HTML
5. **scripts/update-metrics.js** - Get stock data from APIs

## Key Limitations

| Source | Limitation | Workaround |
|--------|-----------|-----------|
| **Yahoo Finance** | Consent modal blocks content | Use Alpha Vantage API instead |
| **Trading Economics** | JS charting library errors | Use their API endpoints directly |
| **Investor IR pages** | Complex SPAs, timeouts | Stick with SEC EDGAR |
| **Earnings transcripts** | Paywalled on many sites | Use free Seeking Alpha |
| **Alpha Vantage** | 25 calls/day limit | Fine for 25 companies (1 per week) |

## What NOT to Collect (Not Worth It)

- Real-time level 2 order book (costs $500+/year, not needed for analysis)
- Proprietary analyst ratings (paywalled, use your own analysis)
- Bloomberg-level data (costs $25K+/year, SEC is better anyway)
- Insider transaction alerts (low signal, high noise)

## Decision Tree

**Q: Do you need real-time data?**  
A: No → Use Option B (quarterly)

**Q: Do you need earnings transcripts?**  
A: Manual review only → Option B + manual Seeking Alpha  
A: Automated → Option C (complex)

**Q: How many companies?**  
A: <50 → Alpha Vantage free tier is plenty  
A: >50 → Upgrade to paid tier or FMP

**Q: How often do you analyze?**  
A: Quarterly → Option B (run after earnings)  
A: Weekly → Option C (need real-time monitoring)

## Data Validation & Source Verification

### Cross-Check: FMP API vs Yahoo Finance (April 29, 2026)

✅ **INTC FY 2025 Financial Data Verified**

Compared Financial Modeling Prep API output against Yahoo Finance data for INTC annual results (FY 2025). **Perfect alignment on all metrics:**

| Metric | FMP | Yahoo | Match |
|--------|-----|-------|-------|
| Revenue | $52.85B | $52.85B | ✓ |
| Gross Profit | $18.38B | $18.38B | ✓ |
| Net Income | -$267M | -$267M | ✓ |
| Diluted EPS | -$0.06 | -$0.06 | ✓ |
| Operating Cash Flow | $9.697B | $9.697B | ✓ |
| Capital Expenditure | -$14.646B | -$14.646B | ✓ |
| Free Cash Flow | -$4.949B | -$4.949B | ✓ |
| Total Debt | $46.59B | $46.59B | ✓ |

**Conclusion:** Both FMP and Yahoo pull from identical SEC filings. FMP API `/stable/` endpoints are reliable and authoritative for annual/quarterly financial data. No discrepancies detected.

---

## Earnings Call Transcripts: Collection Strategy

### Available Sources (Ranked by Reliability)

| Source | Type | Access | Reliability | Effort |
|--------|------|--------|-------------|--------|
| **Company IR Pages** | Direct | Free | High | Manual |
| **SEC 8-K Filings** | Official | Free API | High | Low (requires parsing) |
| **Seeking Alpha** | Web | Free (partial) | Medium | Manual + Google |
| **Motley Fool** | Web | Free | Medium | Manual from articles |
| **FastTranscripts** | Service | Paid | High | None (subscription) |
| **Stockanalysis.com** | Aggregator | Free | Medium | Manual lookup |
| **Yahoo Finance** | Links | Free | Low | Blocked by consent |
| **Web Scraping** | Automated | Free | Low | Complex, fragile |

### Why NOT to Use Web Scraping for Transcripts

**Tested Obscura against 10 transcript sources (4/30/2026):**
- Seeking Alpha: JavaScript runtime errors
- Yahoo Finance: Consent modal blocks content
- Motley Fool: Complex SPA, stack overflow errors
- Company IR pages: 404 or unreachable

**Recommendation:** Use **manual collection** instead. It's:
- ✅ More reliable (no JS errors)
- ✅ Faster (direct links work)
- ✅ Simpler (no scraping maintenance)
- ✅ Better quality (official transcripts only)

### Practical Workflow for Transcripts

**Option 1: Manual Collection (Recommended)**
```bash
# Step 1: Find transcript
google-chrome "INTC Q1 2026 earnings call transcript"

# Step 2: Copy text or save PDF
# Step 3: Store in company/transcripts/2026_Q1_earnings.txt
```

**Option 2: Seeking Alpha Free Tier**
1. Search company on Seeking Alpha
2. Go to "Transcripts" tab
3. Find relevant quarter
4. Copy text (free articles contain full transcripts)
5. Save to repo

**Option 3: Company IR Direct (Most Official)**
1. Visit company investor relations page
2. Navigate to "Events & Presentations" or "Earnings"
3. Find earnings call date
4. Download transcript if available (many provide .pdf or .docx)
5. Save to repo

### When to Invest in Paid Service

Use FastTranscripts or similar **only if:**
- You have 50+ companies to track
- You need automated quarterly updates
- You can't manually maintain collection
- Budget allows $500-1000/year per service

For your current setup (25 companies), **manual collection is more cost-effective**.

### Storage Format

Once collected, store transcripts in:
```
company_ticker/transcripts/
├── 2026_Q1_earnings_call.txt
├── 2026_Q1_press_release.txt
└── 2026_Q1_earnings_call.pdf (if available)
```

Include metadata in filename:
- Year
- Quarter or specific date
- Document type (earnings_call, press_release, etc.)
- Format (txt, pdf, md)

