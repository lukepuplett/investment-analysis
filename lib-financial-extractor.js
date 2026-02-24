#!/usr/bin/env node
/**
 * Financial Data Extractor
 * Extracts structured financial metrics from HTML
 *
 * This is a "swappable refinement tool" - designed to work on raw HTML
 * from various financial websites. Can be improved independently of
 * the scraper without re-acquiring data.
 */

class FinancialExtractor {
  constructor(options = {}) {
    this.options = options;
  }

  /**
   * Extract financial metrics from HTML based on source type
   * @param {string} html - Raw HTML content
   * @param {string} source - Source identifier (e.g. 'yahoo-finance')
   * @returns {object} Extracted metrics
   */
  extractFromHTML(html, source = 'yahoo-finance') {
    if (source === 'yahoo-finance') {
      return this.extractFromYahooFinance(html);
    }
    return { metrics: {}, source };
  }

  /**
   * Extract from Yahoo Finance page HTML
   * Strategy: Convert HTML to clean text, use line-based lookup with regex
   */
  extractFromYahooFinance(html) {
    // Remove script tags and clean HTML
    const cleanHTML = html
      .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
      .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, '');

    // Extract text content
    const text = cleanHTML
      .replace(/<[^>]+>/g, '\n')  // Replace tags with newlines
      .replace(/\n\s*\n/g, '\n')  // Remove blank lines
      .trim();

    const metrics = {};

    // Strategy: Find label, then capture value on same or next line
    // Yahoo format typically has label on one line, value on next
    const lines = text.split('\n').map(l => l.trim()).filter(l => l.length > 0);

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      const nextLine = lines[i + 1] || '';

      // Market Cap
      if (line.match(/Market Cap/i) && !metrics.marketCap) {
        const val = this.extractValue(nextLine);
        if (val) metrics.marketCap = val;
      }

      // Price - Previous Close
      if (line.match(/Previous Close/i) && !metrics.previousClose) {
        const val = nextLine.match(/[\d,]+\.?\d*/)?.[0];
        if (val) metrics.previousClose = val;
      }

      // Beta
      if (line.match(/Beta/i) && !metrics.beta) {
        const val = nextLine.match(/[\d.]+/)?.[0];
        if (val) metrics.beta = val;
      }

      // PE Ratio (TTM)
      if (line.match(/PE Ratio|P\/E Ratio/i) && !metrics.peRatio) {
        const val = nextLine.match(/[\d.-]+/)?.[0];
        if (val) metrics.peRatio = val;
      }

      // EPS (TTM)
      if (line.match(/EPS|Earnings Per Share/i) && !metrics.eps) {
        const val = nextLine.match(/[\d.-]+/)?.[0];
        if (val) metrics.eps = val;
      }

      // 52 Week Range - next line has "High", line after has value
      if (line.match(/52 Week Range/i) && !metrics.fiftyTwoWeekRange) {
        const val = nextLine.match(/[\d.,]+ - [\d.,]+/)?.[0];
        if (val) {
          const parts = val.split('-').map(p => p.trim());
          metrics.fiftyTwoWeekLow = parts[0];
          metrics.fiftyTwoWeekHigh = parts[1];
        }
      }

      // Volume
      if (line.match(/^Volume$/i) && !metrics.volume) {
        const val = nextLine.match(/[\d,]+/)?.[0];
        if (val) metrics.volume = val;
      }

      // Avg Volume
      if (line.match(/Avg\. Volume|Average Volume/i) && !metrics.avgVolume) {
        const val = nextLine.match(/[\d,]+/)?.[0];
        if (val) metrics.avgVolume = val;
      }

      // Dividend
      if (line.match(/Forward Dividend|Dividend/i) && !metrics.dividend) {
        const val = nextLine.match(/\$?[\d.]+/)?.[0];
        if (val && val !== '--') metrics.dividend = val;
      }

      // 1y Target Estimate
      if (line.match(/1y Target|Target Est/i) && !metrics.targetEstimate) {
        const val = nextLine.match(/\$?[\d.,]+/)?.[0];
        if (val) metrics.targetEstimate = val;
      }

      // Revenue (often in description section)
      if (line.match(/Revenue/i) && !metrics.revenue && nextLine.match(/[\d.]+[BMK]/i)) {
        const val = this.extractValue(nextLine);
        if (val) metrics.revenue = val;
      }

      // Profit Margin
      if (line.match(/Profit Margin|Net Margin/i) && !metrics.profitMargin) {
        const val = nextLine.match(/[\d.-]+%?/)?.[0];
        if (val) metrics.profitMargin = val;
      }
    }

    return {
      metrics,
      source: 'yahoo-finance',
      metricsCount: Object.keys(metrics).length,
      extractedAt: new Date().toISOString()
    };
  }

  /**
   * Extract value with unit (B, M, K)
   */
  extractValue(text) {
    const match = text.match(/[\d.,]+(\.?\d+)?[BMK]/i);
    return match ? match[0] : null;
  }
}

module.exports = FinancialExtractor;
