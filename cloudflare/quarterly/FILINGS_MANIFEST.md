# Cloudflare (NET) - 10-Q Historical Filings Manifest

**Data Source:** SEC EDGAR via Obscura headless browser  
**Retrieval Date:** 2026-04-30  
**Company:** Cloudflare, Inc.  
**Ticker:** NET  
**CIK:** 0001477333

## Filing History (Quarterly Reports - Form 10-Q)

| Date Filed | Quarter/Year | Accession Number | Filing Size | Status |
|-----------|-------------|------------------|-------------|--------|
| 2025-10-30 | Q3 2025 | 0001477333-25-000141 | 9 MB | ✅ Available |
| 2025-07-31 | Q2 2025 | 0001477333-25-000137 | 9 MB | ✅ Available |
| 2025-05-08 | Q1 2025 | 0001477333-25-000082 | 8 MB | ✅ Available |
| 2024-11-07 | Q3 2024 | 0001477333-24-000085 | 8 MB | ✅ Available |
| 2024-08-01 | Q2 2024 | 0001477333-24-000070 | 10 MB | ✅ Available |
| 2024-05-02 | Q1 2024 | 0001477333-24-000050 | 7 MB | ✅ Available |
| 2023-11-02 | Q3 2023 | 0001477333-23-000064 | 10 MB | ✅ Available |
| 2023-08-03 | Q2 2023 | 0001477333-23-000056 | 9 MB | ✅ Available |
| 2023-04-27 | Q1 2023 | 0001477333-23-000043 | 10 MB | ✅ Available |
| 2022-11-03 | Q3 2022 | 0001477333-22-000060 | 11 MB | ✅ Available |
| 2022-08-04 | Q2 2022 | 0001477333-22-000048 | 13 MB | ✅ Available |
| 2022-05-05 | Q1 2022 | 0001477333-22-000031 | 10 MB | ✅ Available |
| 2021-11-05 | Q3 2021 | 0001477333-21-000045 | 12 MB | ✅ Available |
| 2021-08-06 | Q2 2021 | 0001477333-21-000036 | 10 MB | ✅ Available |
| 2021-05-07 | Q1 2021 | 0001477333-21-000026 | 9 MB | ✅ Available |
| 2020-11-10 | Q3 2020 | 0001477333-20-000042 | 11 MB | ✅ Available |
| 2020-08-10 | Q2 2020 | 0001628280-20-012347 | 12 MB | ✅ Available |
| 2020-05-11 | Q1 2020 | 0001477333-20-000024 | 10 MB | ✅ Available |
| 2019-11-12 | Q3 2019 | 0001477333-19-000013 | 13 MB | ✅ Available |

## How to Access

Each filing can be accessed at:
```
https://www.sec.gov/Archives/edgar/data/1477333/[ACCESSION-NUMBER]/[ACCESSION-NUMBER]-index.htm
```

**Example for Q3 2025 10-Q:**
```
https://www.sec.gov/Archives/edgar/data/1477333/000147733325000141/0001477333-25-000141-index.htm
```

## Tool Used for Retrieval

**Obscura Headless Browser**
- Command: `obscura fetch "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001477333&type=10-Q&dateb=&owner=exclude&count=100"`
- Performance: ~3 seconds to fetch entire filing list
- Status: ✅ **Works perfectly** (SEC EDGAR has clean HTML, no anti-scraping barriers)

## Next Steps

To extract financial data from these 10-Qs:
1. Download the specific 10-Q HTML files from accession numbers above
2. Parse the structured financial tables (income statement, balance sheet, cash flow)
3. Create formatted analysis documents in `analysis/` directory

---

*Data retrieved via Obscura - SEC EDGAR integration works excellently for financial data access.*
