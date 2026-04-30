# Obscura Exploration Findings

**Date:** 2026-04-30  
**Focus:** Financial data scraping capabilities and limitations

## Test Results Summary

### ✅ Working Well

#### SEC EDGAR Filing Search
- **URL:** `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=XXXXXXXXX`
- **Status:** Excellent
- **Load Time:** ~2-3 seconds
- **Data Quality:** Perfect - clean HTML, extractable filing metadata
- **What we can get:**
  - Company info (name, CIK, address, SIC code)
  - Filing list with dates and accession numbers
  - File sizes and document links
  - Filter by filing type (10-Q, 10-K, 8-K, etc.)

**Example data extraction:**
```
Accession: 0000050863-26-000079
Date: 2026-04-24
Size: 9 MB
Filing Type: 10-Q (Quarterly Report)
```

#### BBC News
- **Status:** Works perfectly
- **Load Time:** ~2-3 seconds
- **Data Quality:** Full text extraction, no barriers
- **Use:** Validates Obscura's JavaScript rendering works for clean sites

### ⚠️ Partially Working

#### Trading Economics (INTC example)
- **Status:** Renders but charting library crashes
- **Load Time:** ~2-3 seconds
- **JS Error:** `TypeError: a.elementFromPoint is not a function`
- **What DOES work:**
  - Page title loads correctly
  - JavaScript variables available: `TEChartUrl`, `TEChartsDatasource`, `TEChartToken`
  - Metadata in `<meta>` tags accessible
  - Can extract data source endpoint from JS variables
  
**Workaround:** Use their data source API endpoint instead of rendering charts
```javascript
// Extract from JavaScript
TEChartsDatasource = "https://d3ii0wo49og5mi.cloudfront.net"
TEChartsToken = "20260324:loboantunes"
// Then query their API directly
```

#### Yahoo Finance
- **Status:** Blocked by consent modal, but page renders
- **Load Time:** ~2-3 seconds
- **Barrier:** Persistent privacy consent modal (guce = Google User Consent Engine)
- **What renders:** Page structure loads, JavaScript executes
- **Blocker:** Modal prevents access to actual stock data
- **Data visible:** Only JavaScript for consent management

### ❌ Not Accessible via HTML Scraping

#### Investor Relations Pages
- **Intel IR Example:** `investor.intel.com/financial-information/quarterly-earnings/`
- **Status:** No output (likely times out or has redirect)
- **Load Time:** Timeout/no response
- **Issue:** Heavy single-page application (SPA), complex JavaScript, possible redirect chains

---

## What We've Learned About Obscura

### Strengths
1. **Perfect for static/traditional HTML sites** — SEC EDGAR, news sites
2. **JavaScript execution works** — V8 engine runs scripts correctly
3. **Fast** — 2-3 seconds typical for page load + render
4. **No bot detection issues** (with `--stealth`)
5. **Eval capability** — Can extract JavaScript variables and compute data
6. **Timeout-safe** — Doesn't hang indefinitely, respects `--wait` and `--timeout`

### Limitations
1. **JavaScript DOM API gaps** — Some libraries need `elementFromPoint()` and similar APIs
2. **Consent modals** — Can't auto-dismiss (would need CDP server + Puppeteer interaction)
3. **SPA navigation** — Complex single-page apps with client-side routing may not work
4. **CLI interaction** — No way to click buttons, fill forms, navigate (would need CDP server)

### Best Use Cases for Obscura CLI
- ✅ SEC EDGAR filings and metadata
- ✅ News sites and blogs
- ✅ Company announcements/press releases
- ✅ Static financial pages (with fallback to APIs)
- ❌ Yahoo Finance (use API instead)
- ❌ Trading Economics (use their API)
- ❌ Complex investor relations SPAs

---

## Recommended Scraping Strategy for Investment Analysis

### Tier 1: SEC EDGAR (Recommended)
**Why:** Works perfectly with Obscura, authoritative financial data, no barriers
```bash
# Get filing list
obscura fetch "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=XXXX&type=10-Q"

# Could download actual 10-Q document text
# Parse for financial statements
```

### Tier 2: Direct APIs (if available)
**Trading Economics:** Has API endpoints, use directly
**Yahoo Finance:** Has WebSocket API for real-time quotes
**Alpha Vantage:** Free stock data API

### Tier 3: CDP Server + Puppeteer (for complex interaction)
Only if you need to:
- Click buttons and navigate
- Dismiss consent modals automatically
- Scrape SPA content that requires interaction

---

## Next Steps to Validate

1. **Test SEC EDGAR 10-Q document access** — Can we download and parse actual financial statements?
2. **Build SEC EDGAR utility** — Automated quarterly filing fetch + extract financial tables
3. **Test Trading Economics API** — Can we get stock data directly from their datasource?
4. **Compare: SEC filings vs Yahoo Finance data** — Which is more useful for your analysis?

---

## Performance Metrics

| Source | Load Time | Output Size | Success Rate | Timeout Safety |
|--------|-----------|-------------|--------------|-----------------|
| SEC EDGAR | 2-3s | 50-200 KB | 100% | ✅ Yes |
| BBC News | 2-3s | 100-300 KB | 100% | ✅ Yes |
| Yahoo Finance | 2-3s | 50-100 KB | Partial (modal blocks) | ✅ Yes |
| Trading Economics | 2-3s | 30-50 KB | Partial (JS error) | ✅ Yes |
| Intel IR | timeout | — | 0% | ❓ Unclear |

---

## Earnings Call Transcript Source Testing (April 30, 2026)

### Test Results: 10 Transcript Sources

Tested Obscura against common sources for earnings call transcripts:

| Source | Status | Issue | Notes |
|--------|--------|-------|-------|
| **SEC EDGAR Search** | ✅ WORKS | None | Perfect for filing metadata |
| **SEC EDGAR Documents** | ⚠️ HTTP 404 | Archive links broken | Metadata accessible, actual docs need direct curl |
| **Seeking Alpha** | ❌ BLOCKED | JS error in app bundle | `Cannot read properties of undefined (reading 'prototype')` |
| **Stockanalysis.com** | ❌ 404 | Page doesn't exist | URL structure may have changed |
| **Yahoo Finance** | ❌ BLOCKED | Consent modal | Same barrier as before; modal prevents content access |
| **Motley Fool** | ❌ BROKEN | Multiple JS errors | Stack overflow + `elementFromPoint not a function` |
| **Intel IR (intc.com)** | ❌ 404 | Page not found | Corporate IR structure doesn't exist at expected paths |
| **Motley Fool (stealth)** | ❌ BROKEN | Complex SPA | Even with --stealth flag, JavaScript runtime errors persist |
| **Company IR (investor.intc.com)** | ❌ NETWORK | Domain unreachable | Investor IR subdomain doesn't respond |

### Detailed Findings

**What Works:**
- SEC EDGAR filing **search/browse** pages (clean HTML, no JS complexity)
- Text extraction from listing pages

**What Doesn't Work:**
- Seeking Alpha transcripts (JS runtime errors in React app)
- Yahoo Finance (consent modal barrier; known limitation)
- Motley Fool (SPA with complex React; multiple JS errors)
- Company IR pages (either 404, SPA-based, or unreachable)

**V8 Engine Limitations:**
- `elementFromPoint()` not implemented (charting libraries fail)
- Some DOM methods missing for modern frameworks
- Stack overflow in certain React/Vue patterns
- Prototype chain issues with minified code

### Recommendation: Don't Use Obscura for Transcripts

**Why:** Earnings transcript pages are almost all complex SPAs or behind barriers that Obscura can't handle.

**Better Approach:**

| Use Case | Method | Works | Notes |
|----------|--------|-------|-------|
| **Get filing metadata** | SEC EDGAR API (curl) | ✅ YES | Use SEC API for CIK, dates, accession numbers |
| **Download 10-Q documents** | curl to SEC Archives | ✅ YES | Direct HTTP works better than Obscura |
| **Get transcripts** | Manual collection | ✅ YES | Google search, company IR, Seeking Alpha free tier |
| **Monitor for updates** | SEC 8-K API (curl) | ✅ YES | Real-time alerts via SEC filings API |
| **Parse 10-Q tables** | grep + sed or simple HTML parsing | ✅ YES | Raw documents have structured tables |

**Practical Flow:**
1. Use SEC EDGAR API to find latest 10-Q accession number (Obscura works here)
2. Download 10-Q HTML directly with curl (no Obscura needed)
3. Find transcripts manually via Google or company IR (more reliable)
4. Use grep/sed to extract financial tables from 10-Q (doesn't need browser)

---

## Conclusion

**Obscura is highly suitable for financial data scraping IF:**
1. You focus on SEC EDGAR (authoritative, works perfectly)
2. You use APIs as fallback for sites with barriers
3. You don't need automated interaction with modals/forms

**Not suitable for:**
1. Consumer financial sites with consent modals
2. Complex single-page applications (Seeking Alpha, Motley Fool, Yahoo Finance)
3. Sites requiring user interaction
4. Earnings call transcripts (use manual collection instead)

**Best path forward:** 
- Use SEC EDGAR for filings (Obscura for search, curl for documents)
- Use FMP API for parsed financials
- Manual collection for transcripts (more reliable than scraping)
- Avoid Obscura for consumer financial sites and SPAs

---

## Final Integration Test Results (2026-04-30)

### Investment Analysis Workflow Tested

**Real-world scenario:** Retrieve and analyze Cloudflare (NET) Q3 2025 earnings

**Data retrieval:**
✅ SEC EDGAR filing search → Obscura (fast, reliable)
✅ 10-Q document download → Obscura with stealth mode (complete)
❌ XBRL parsing → Specialized parsers (limited environment support)

**Practical conclusion:**
- **Use Obscura for:** Document retrieval, filing discovery, historical access
- **Use APIs for:** Financial metrics, valuation data, current stock stats
- **Use manual for:** Qualitative analysis, competitive assessment

**Workflow recommendation:**
```
Quarterly earnings → Obscura retrieves 10-Q (2-5 sec)
                  → User provides stock metrics from Yahoo (5 min)
                  → AI formats financials + analysis (20 min)
                  → Complete investment thesis update (30 min total)
```

### Key Learning

**Obscura is not an end-to-end financial data extraction tool.** It's an excellent **document retrieval tool** that solves the specific problem: "How do we get SEC documents when curl is blocked?"

The full data pipeline requires:
1. **Retrieval layer:** Obscura (SEC EDGAR) ✅
2. **Extraction layer:** APIs or manual (Yahoo, FMP, etc.) ⚠️
3. **Analysis layer:** Our framework (7-doc analysis structure) ✅

Don't spend engineering time on XBRL parsing when higher-level sources are available and faster.
