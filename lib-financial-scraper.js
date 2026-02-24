#!/usr/bin/env node
/**
 * Financial Data Scraper
 * Extends UniversalScraper for financial documents (10-Q, 10-K, earnings, etc.)
 */

const UniversalScraper = require('./lib-universal-scraper');

class FinancialScraper extends UniversalScraper {
  /**
   * Extract financial data with intelligence
   */
  async scrapeFinancialPage(url, documentType = 'auto') {
    console.log(`\n💰 Financial Scraper: ${documentType === 'auto' ? 'Auto-detecting' : documentType}`);

    const data = await this.fetchAndParse(url);

    // Detect document type if auto
    if (documentType === 'auto') {
      documentType = this.detectFinancialDocumentType(data);
      console.log(`   📋 Detected: ${documentType}`);
    }

    // Extract financial metrics based on document type
    const financialData = this.extractFinancialMetrics(data, documentType);

    return {
      ...data,
      documentType,
      financialData,
    };
  }

  /**
   * Detect what financial document this is
   */
  detectFinancialDocumentType(data) {
    const text = data.content.bodyText.toUpperCase();

    if (text.includes('10-Q') || text.includes('FORM 10-Q')) {
      return '10-Q (Quarterly Report)';
    }

    if (text.includes('10-K') || text.includes('FORM 10-K')) {
      return '10-K (Annual Report)';
    }

    if (text.includes('8-K') || text.includes('FORM 8-K')) {
      return '8-K (Current Report)';
    }

    if (
      text.includes('EARNINGS') &&
      (text.includes('PRESS RELEASE') || text.includes('ANNOUNCEMENT'))
    ) {
      return 'EARNINGS ANNOUNCEMENT';
    }

    if (text.includes('BALANCE SHEET') && text.includes('ASSETS')) {
      return 'BALANCE SHEET';
    }

    if (text.includes('INCOME STATEMENT') || text.includes('CONSOLIDATED STATEMENTS OF OPERATIONS')) {
      return 'INCOME STATEMENT';
    }

    if (text.includes('CASH FLOW')) {
      return 'CASH FLOW STATEMENT';
    }

    return 'GENERIC FINANCIAL DOCUMENT';
  }

  /**
   * Extract financial metrics from tables
   */
  extractFinancialMetrics(data, documentType) {
    const metrics = {
      documentType,
      tables: [],
      keyMetrics: {},
      financialStatements: {},
    };

    // Extract common financial metrics from page text
    const text = data.content.bodyText;

    // Revenue patterns
    metrics.keyMetrics.revenue = this.extractFinancialValue(text, ['revenue', 'total revenue', 'net sales']);

    // Profit patterns
    metrics.keyMetrics.netIncome = this.extractFinancialValue(text, ['net income', 'net earnings']);
    metrics.keyMetrics.grossProfit = this.extractFinancialValue(text, ['gross profit']);
    metrics.keyMetrics.operatingIncome = this.extractFinancialValue(text, ['operating income']);

    // Margins
    metrics.keyMetrics.grossMargin = this.extractFinancialValue(text, ['gross margin']);
    metrics.keyMetrics.operatingMargin = this.extractFinancialValue(text, ['operating margin']);
    metrics.keyMetrics.netMargin = this.extractFinancialValue(text, ['net margin']);

    // Balance sheet items
    metrics.keyMetrics.totalAssets = this.extractFinancialValue(text, ['total assets']);
    metrics.keyMetrics.totalLiabilities = this.extractFinancialValue(text, ['total liabilities']);
    metrics.keyMetrics.stockholdersEquity = this.extractFinancialValue(text, ['stockholders equity', "shareholders' equity"]);

    // Cash flow
    metrics.keyMetrics.operatingCashFlow = this.extractFinancialValue(text, ['operating cash flow']);
    metrics.keyMetrics.freeCashFlow = this.extractFinancialValue(text, ['free cash flow']);
    metrics.keyMetrics.capitalExpenditures = this.extractFinancialValue(text, ['capital expenditures', 'capex']);

    // Per share data
    metrics.keyMetrics.eps = this.extractFinancialValue(text, ['earnings per share', 'eps']);
    metrics.keyMetrics.dividendPerShare = this.extractFinancialValue(text, ['dividend per share']);

    // Process tables into financial statements
    metrics.financialStatements = this.processFinancialTables(data.tables, documentType);

    return metrics;
  }

  /**
   * Extract financial values from text (handles various formats)
   */
  extractFinancialValue(text, patterns) {
    for (const pattern of patterns) {
      // Match pattern followed by a number, currency, or percentage
      const regex = new RegExp(
        `${pattern}[:\\s]*\\$?([\\d,.]+ [BMK]?|[\\d,.]+)%?`,
        'gi'
      );

      const match = regex.exec(text);
      if (match) {
        return {
          value: match[1],
          rawText: match[0],
        };
      }
    }
    return null;
  }

  /**
   * Identify and process financial statement tables
   */
  processFinancialTables(tables, documentType) {
    const statements = {
      incomeStatement: null,
      balanceSheet: null,
      cashFlow: null,
      otherTables: [],
    };

    tables.forEach(table => {
      const headerText = table.headers.join(' ').toUpperCase();

      if (
        headerText.includes('REVENUE') ||
        headerText.includes('OPERATIONS') ||
        headerText.includes('NET INCOME')
      ) {
        statements.incomeStatement = {
          title: 'Income Statement',
          headers: table.headers,
          rows: table.rows,
          data: table.data,
        };
      } else if (
        headerText.includes('ASSET') ||
        headerText.includes('LIABILITY') ||
        headerText.includes('EQUITY')
      ) {
        statements.balanceSheet = {
          title: 'Balance Sheet',
          headers: table.headers,
          rows: table.rows,
          data: table.data,
        };
      } else if (
        headerText.includes('CASH') &&
        headerText.includes('FLOW')
      ) {
        statements.cashFlow = {
          title: 'Cash Flow Statement',
          headers: table.headers,
          rows: table.rows,
          data: table.data,
        };
      } else if (table.rowCount > 3) {
        // Could be relevant
        statements.otherTables.push({
          title: `Table (${table.rowCount} rows)`,
          headers: table.headers,
          rows: table.rows.slice(0, 10),
        });
      }
    });

    return statements;
  }

  /**
   * Compare financial metrics across periods
   */
  compareMetrics(currentMetrics, previousMetrics) {
    const comparison = {};

    Object.keys(currentMetrics).forEach(key => {
      const current = currentMetrics[key];
      const previous = previousMetrics[key];

      if (current && previous) {
        const currentVal = parseFloat(String(current).replace(/[^0-9.-]/g, ''));
        const previousVal = parseFloat(String(previous).replace(/[^0-9.-]/g, ''));

        if (!isNaN(currentVal) && !isNaN(previousVal)) {
          const change = currentVal - previousVal;
          const pctChange = ((change / previousVal) * 100).toFixed(2);

          comparison[key] = {
            current: currentVal,
            previous: previousVal,
            change: change,
            pctChange: parseFloat(pctChange),
            direction: change > 0 ? '📈' : '📉',
          };
        }
      }
    });

    return comparison;
  }

  /**
   * Generate financial analysis summary
   */
  generateSummary(financialData) {
    let summary = '## Financial Analysis Summary\n\n';

    if (financialData.keyMetrics) {
      summary += '### Key Metrics Extracted\n\n';
      Object.entries(financialData.keyMetrics).forEach(([key, value]) => {
        if (value) {
          summary += `- **${this.camelToTitle(key)}:** ${value.value}\n`;
        }
      });
      summary += '\n';
    }

    if (financialData.financialStatements.incomeStatement) {
      summary += '### Income Statement\n\n';
      const stmt = financialData.financialStatements.incomeStatement;
      summary += this.tableToMarkdown(stmt.headers, stmt.rows.slice(0, 10));
      summary += '\n';
    }

    if (financialData.financialStatements.balanceSheet) {
      summary += '### Balance Sheet\n\n';
      const stmt = financialData.financialStatements.balanceSheet;
      summary += this.tableToMarkdown(stmt.headers, stmt.rows.slice(0, 10));
      summary += '\n';
    }

    if (financialData.financialStatements.cashFlow) {
      summary += '### Cash Flow Statement\n\n';
      const stmt = financialData.financialStatements.cashFlow;
      summary += this.tableToMarkdown(stmt.headers, stmt.rows.slice(0, 10));
      summary += '\n';
    }

    return summary;
  }

  /**
   * Convert table to markdown format
   */
  tableToMarkdown(headers, rows) {
    let md = `| ${headers.join(' | ')} |\n`;
    md += `|${headers.map(() => ' --- ').join('|')}|\n`;

    rows.forEach(row => {
      md += `| ${row.join(' | ')} |\n`;
    });

    return md;
  }

  /**
   * Convert camelCase to Title Case
   */
  camelToTitle(str) {
    return str
      .replace(/([A-Z])/g, ' $1')
      .replace(/^./, char => char.toUpperCase())
      .trim();
  }

  /**
   * High-level API: Scrape and analyze a financial document
   */
  async analyzeFinancialDocument(url) {
    const data = await this.scrapeFinancialPage(url);

    return {
      url: data.url,
      documentType: data.documentType,
      title: data.metadata.title,
      extractedMetrics: data.financialData.keyMetrics,
      financialStatements: data.financialData.financialStatements,
      summary: this.generateSummary(data.financialData),
      rawData: data, // For inspection
    };
  }
}

// Export for use as library
module.exports = FinancialScraper;

// CLI usage if run directly
if (require.main === module) {
  (async () => {
    const url = process.argv[2] || 'https://example.com/10q.html';

    const scraper = new FinancialScraper();
    await scraper.init();

    try {
      console.log('\n' + '='.repeat(60));
      console.log('FINANCIAL DATA SCRAPER');
      console.log('='.repeat(60));

      const analysis = await scraper.analyzeFinancialDocument(url);

      console.log(`\n📋 Document Type: ${analysis.documentType}`);
      console.log(`📊 Title: ${analysis.title}`);

      console.log('\n💰 Extracted Metrics:');
      Object.entries(analysis.extractedMetrics).forEach(([key, value]) => {
        if (value) {
          console.log(`   ${key}: ${value.value}`);
        }
      });

      console.log('\n' + '='.repeat(60) + '\n');
    } finally {
      await scraper.close();
    }
  })();
}
