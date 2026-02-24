#!/usr/bin/env node
/**
 * HTML Refinement Tool
 * Strips noise from raw HTML and extracts:
 * - Main content (bare bones structure)
 * - Navigation URLs
 * - Structured data (tables, lists, etc.)
 *
 * Input: Raw HTML from any website
 * Output: Clean content + nav URLs + structure
 */

const fs = require('fs');

class HTMLRefiner {
  constructor(options = {}) {
    this.options = options;
  }

  /**
   * Refine raw HTML file
   */
  refineFile(filePath) {
    const html = fs.readFileSync(filePath, 'utf8');
    return this.refineHTML(html);
  }

  /**
   * Main refinement logic
   */
  refineHTML(html) {
    // Step 1: Remove noise elements
    let cleaned = this.removeNoiseElements(html);

    // Step 2: Extract main content area
    const mainContent = this.extractMainContent(cleaned);

    // Step 3: Extract navigation URLs
    const navUrls = this.extractNavUrls(html);

    // Step 4: Extract tables
    const tables = this.extractTables(cleaned);

    // Step 5: Extract structured text
    const text = this.extractCleanText(cleaned);

    return {
      mainContent,
      navUrls,
      tables,
      text,
      structure: {
        hasMainContent: !!mainContent,
        tableCount: tables.length,
        navUrlCount: navUrls.length,
        textLength: text.length
      },
      refinedAt: new Date().toISOString()
    };
  }

  /**
   * Remove noise: scripts, styles, nav, footer, ads, etc.
   */
  removeNoiseElements(html) {
    let cleaned = html;

    // Remove script tags and content
    cleaned = cleaned.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');

    // Remove style tags and content
    cleaned = cleaned.replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, '');

    // Remove common noise elements
    cleaned = cleaned.replace(/<nav\b[^<]*(?:(?!<\/nav>)<[^<]*)*<\/nav>/gi, '');
    cleaned = cleaned.replace(/<footer\b[^<]*(?:(?!<\/footer>)<[^<]*)*<\/footer>/gi, '');
    cleaned = cleaned.replace(/<header\b[^<]*(?:(?!<\/header>)<[^<]*)*<\/header>/gi, '');
    cleaned = cleaned.replace(/<aside\b[^<]*(?:(?!<\/aside>)<[^<]*)*<\/aside>/gi, '');

    // Remove common ad/tracking divs
    cleaned = cleaned.replace(/<div[^>]*(?:ad|advertisement|banner|sidebar|widget)[^>]*[^<]*(?:(?!<\/div>)<[^<]*)*<\/div>/gi, '');

    // Remove empty tags
    cleaned = cleaned.replace(/<[^>]+>\s*<\/[^>]+>/g, '');

    return cleaned;
  }

  /**
   * Extract main content area
   * Looks for common patterns: main, article, [role="main"], etc.
   */
  extractMainContent(html) {
    // Try to find main content containers in order of preference
    const patterns = [
      /<main[^>]*>([\s\S]*?)<\/main>/i,
      /<article[^>]*>([\s\S]*?)<\/article>/i,
      /<div[^>]*role=["\']main["\']\s*[^>]*>([\s\S]*?)<\/div>/i,
      /<div[^>]*class=["\']content["\'][^>]*>([\s\S]*?)<\/div>/i,
      /<div[^>]*class=["\']main["\'][^>]*>([\s\S]*?)<\/div>/i,
    ];

    for (const pattern of patterns) {
      const match = html.match(pattern);
      if (match && match[1].length > 500) { // Only if substantial content
        return match[1];
      }
    }

    // Fallback: return body content without script/style
    const bodyMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
    return bodyMatch ? bodyMatch[1] : html;
  }

  /**
   * Extract all navigation URLs with context
   */
  extractNavUrls(html) {
    const urls = [];
    const linkPattern = /<a\s+(?:[^>]*?\s+)?href=["']([^"']+)["'][^>]*>([^<]*)<\/a>/gi;

    let match;
    while ((match = linkPattern.exec(html)) !== null) {
      const href = match[1];
      const text = match[2].trim();

      // Filter out empty or javascript links
      if (href && !href.startsWith('javascript:') && text.length > 0) {
        urls.push({
          url: href,
          text: text,
          isExternal: href.startsWith('http') && !href.includes(new URL('http://base').hostname)
        });
      }
    }

    // Deduplicate
    const seen = new Set();
    return urls.filter(u => {
      if (seen.has(u.url)) return false;
      seen.add(u.url);
      return true;
    });
  }

  /**
   * Extract tables with structure
   */
  extractTables(html) {
    const tables = [];
    const tablePattern = /<table[^>]*>([\s\S]*?)<\/table>/gi;

    let match;
    let tableIndex = 0;

    while ((match = tablePattern.exec(html)) !== null) {
      const tableHtml = match[1];

      // Extract headers
      const headers = [];
      const thPattern = /<th[^>]*>([^<]*)<\/th>/gi;
      let thMatch;
      while ((thMatch = thPattern.exec(tableHtml)) !== null) {
        headers.push(thMatch[1].trim());
      }

      // Extract rows
      const rows = [];
      const trPattern = /<tr[^>]*>([\s\S]*?)<\/tr>/gi;
      let trMatch;

      while ((trMatch = trPattern.exec(tableHtml)) !== null) {
        const rowHtml = trMatch[1];
        const cells = [];
        const tdPattern = /<t[dh][^>]*>([^<]*)<\/t[dh]>/gi;
        let tdMatch;

        while ((tdMatch = tdPattern.exec(rowHtml)) !== null) {
          cells.push(tdMatch[1].trim());
        }

        if (cells.length > 0) {
          rows.push(cells);
        }
      }

      if (rows.length > 0) {
        tables.push({
          index: tableIndex,
          headers: headers.length > 0 ? headers : null,
          rows,
          rowCount: rows.length
        });
        tableIndex++;
      }
    }

    return tables;
  }

  /**
   * Extract clean text content
   */
  extractCleanText(html) {
    let text = html
      // Replace br with newlines
      .replace(/<br\s*\/?>/gi, '\n')
      // Replace block elements with newlines
      .replace(/<\/(p|div|section|article|header|footer|h[1-6]|li|dt|dd)>/gi, '\n')
      // Remove all tags
      .replace(/<[^>]+>/g, '')
      // Decode HTML entities
      .replace(/&nbsp;/g, ' ')
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>')
      .replace(/&amp;/g, '&')
      // Clean up whitespace
      .replace(/[ \t]+/g, ' ')
      .replace(/\n\s*\n+/g, '\n')
      .trim();

    return text;
  }

  /**
   * Refine and output to file
   */
  refineAndSave(inputFile, outputFile) {
    const result = this.refineFile(inputFile);

    // Create output structure
    const output = {
      metadata: {
        sourceFile: inputFile,
        refinedAt: result.refinedAt,
        stats: result.structure
      },
      content: {
        text: result.text.substring(0, 5000), // First 5000 chars
        tables: result.tables.slice(0, 5), // First 5 tables
        mainContent: result.mainContent.substring(0, 3000) // First 3000 chars
      },
      navigation: {
        urls: result.navUrls.slice(0, 20), // First 20 links
        internalCount: result.navUrls.filter(u => !u.isExternal).length,
        externalCount: result.navUrls.filter(u => u.isExternal).length
      }
    };

    fs.writeFileSync(outputFile, JSON.stringify(output, null, 2));

    return output;
  }
}

module.exports = HTMLRefiner;

// CLI usage
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length < 1) {
    console.log('Usage: node lib-html-refiner.js <input.html> [output.json]');
    process.exit(1);
  }

  const inputFile = args[0];
  const outputFile = args[1] || inputFile.replace('.html', '_refined.json');

  const refiner = new HTMLRefiner();
  const result = refiner.refineAndSave(inputFile, outputFile);

  console.log('✅ Refinement complete');
  console.log(`📊 Found: ${result.content.tables.length} tables, ${result.navigation.urls.length} URLs`);
  console.log(`💾 Saved: ${outputFile}`);
}
