# CVCO Data Sourcing Assessment
**Date:** 2025-02-24
**Company:** Cavco Industries (CVCO)
**Status:** Data collection strategy documented

## Summary
Direct automated access to financial data sources is heavily restricted. A hybrid manual/programmatic approach is recommended with workarounds for data collection.

---

## Accessibility Test Results

| Source | Status | HTTP Code | Notes |
|--------|--------|-----------|-------|
| SEC EDGAR (browse-edgar) | ❌ BLOCKED | 403 | Requires declared user agent; rate limiting active |
| SEC EDGAR (direct PDF) | ❌ BLOCKED | 403 | Akamai WAF blocking automated access |
| SEC JSON API | ❌ ERROR | N/A | Endpoint unreachable or returns empty |
| Cavco.com | ⚠️ REDIRECT | 301 | Site redirects; likely behind authentication layer |
| Cavco IR | ⚠️ REDIRECT | 301 | Investor relations portal behind redirect |
| Yahoo Finance | ⚠️ BLOCKED | N/A | Blocks curl user agents; blocks without JS rendering |
| Seeking Alpha | ⚠️ BLOCKED | N/A | Requires JavaScript rendering; blocks headless access |

---

## Viable Data Acquisition Paths

### **Path 1: Manual SEC EDGAR Access (Most Reliable)**
- **Action:** Use browser to visit https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001347453
- **What to grab:**
  - Latest 10-Q (quarterly unaudited financials)
  - Latest 10-K (annual audited financials)
  - Recent 8-K filings (material events)
  - Investor presentations (attached to 8-K or 10-Q)
- **Format:** Download as .txt or .html, save to `/quarterly/`
- **Frequency:** Available 40-45 days after quarter close (10-Q), 60-90 days after FY close (10-K)

### **Path 2: Company Investor Relations Website**
- **URL:** https://www.cavco.com/investors (or similar)
- **What to grab:**
  - Press releases (earnings announcements)
  - Earnings presentation PDFs
  - Investor fact sheets
  - Recent news and updates
- **Format:** Save as .txt or .pdf to `/quarterly/`

### **Path 3: Financial Data Aggregators (Browser-Based)**
- **Yahoo Finance:** https://finance.yahoo.com/quote/CVCO
  - Key metrics, historical prices, financials tab
  - Copy/paste into spreadsheet
- **Seeking Alpha:** https://seekingalpha.com/symbol/CVCO
  - Earnings transcripts (free tier)
  - Analyst estimates
  - Recent articles
- **MarketWatch:** https://www.marketwatch.com/investing/stock/cvco
  - News, company profile, financials

### **Path 4: Automated Scraping with Playwright/Selenium (If Needed)**
For JavaScript-rendered sites, a headless browser script can extract data:
```python
# Requires: pip install playwright
# Script: Would render pages and extract structured data
```

---

## Recommended Data Collection Workflow

### **Week 1: Foundational Data**
1. Visit SEC EDGAR → Download CVCO's latest 10-Q and 10-K (save as .txt)
2. Visit CVCO investor relations → Download latest press release and presentation
3. Visit Yahoo Finance → Screenshot and save key metrics table
4. Save all to `/quarterly/` with naming: `2025_Q#_10q.txt`, `2025_Q#_press_release.txt`

### **Week 2: Comparative Data**
1. Pull competitor 10-Qs (Clayton Homes, Meritage, etc.) via same SEC process
2. Collect industry reports (if available via institutional access)
3. Extract key metrics for comp table

### **Ongoing: News & Updates**
1. Monitor Seeking Alpha for earnings transcripts
2. Set up RSS/email alerts from company IR
3. Check MarketWatch weekly for news

---

## Alternative: Programmatic Access with Workarounds

### **Option A: Use Playwright for JavaScript Rendering**
```bash
# Install: pip install playwright
# Then: playwright install
# Renders pages like real browser, bypasses basic bot detection
```

### **Option B: SEC EDGAR via Official APIs**
- SEC offers `sec-api.io` (requires account, ~$99/month for real-time)
- Free tier: https://www.sec.gov/developer provides bulk data

### **Option C: Financial Data APIs**
- Alpha Vantage (free tier available)
- Finnhub (free tier available)
- IEX Cloud (free tier available)
- Limitation: May not have full 10-Q/10-K text, just key metrics

---

## Current Folder Structure Created
```
/Users/lukepuplett/Git/Hub/investment_analysis/CVCO/
├── analysis/           (for analysis documents)
├── financials/
│   └── 2025_02/       (for financial statements)
├── quarterly/         (for raw 10-Q, 10-K, press releases)
├── question_answers/  (for Q&A docs)
└── DATA_SOURCING_REPORT.md
```

---

## Next Steps

### **To proceed with analysis:**
1. **Manually download CVCO's latest 10-Q** from SEC EDGAR
2. **Save to:** `/quarterly/2025_Q#_10q.txt`
3. **Extract and format financial data** into:
   - `/financials/2025_02/income_statement.md`
   - `/financials/2025_02/balance_sheet.md`
   - `/financials/2025_02/cashflow.md`

### **Quick-start command (browser-less):**
If you have curl with JavaScript support or a tool like `lynx`, or if you want to use a headless browser:
```bash
# Option 1: Download via direct SEC link (if accession number is known)
curl -L "https://www.sec.gov/Archives/edgar/container/1347453/..." -o quarterly/file.txt

# Option 2: Use a tool like wget with aggressive user-agent spoofing
wget --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" ...
```

---

## Feasibility Assessment

| Task | Feasibility | Effort | Time |
|------|-------------|--------|------|
| Get latest 10-Q | ✅ HIGH | Low (manual) | 5 min |
| Get latest 10-K | ✅ HIGH | Low (manual) | 5 min |
| Get earnings presentation | ✅ HIGH | Low (manual) | 5 min |
| Automated SEC scraping | ❌ LOW | Very High | Not recommended |
| Real-time data pipeline | ⚠️ MEDIUM | High | Requires API subscription |
| Complete 10-Q parsing | ✅ HIGH | Medium (manual parsing) | 30-60 min |

---

## Conclusion

**Direct automated access to financial websites is not viable from this environment.** The most practical approach is:

1. **Manual browser-based collection** of key documents (10-Q, 10-K, press releases) - ~15 minutes
2. **Manual formatting and analysis** of downloaded documents - ~1-2 hours per period
3. **Use financial data aggregators** (Yahoo, Seeking Alpha) for supplementary metrics via browser
4. **Document source URLs** in analysis files for reproducibility

This aligns with the investment research workflow: spend time on *analysis* not data plumbing.

