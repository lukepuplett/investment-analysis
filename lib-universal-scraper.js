#!/usr/bin/env node
/**
 * Universal Web Scraper Library
 * Generic purpose information extraction from any website
 *
 * Features:
 * - Automatic content type detection
 * - Generic table extraction
 * - Text/metadata extraction
 * - Link discovery
 * - Structured data (JSON-LD, microdata)
 * - Configurable extraction rules
 * - Multiple fallback strategies
 */

const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const fs = require('fs');

puppeteer.use(StealthPlugin());

/**
 * Universal Scraper - Main class
 */
class UniversalScraper {
  constructor(options = {}) {
    this.options = {
      headless: true,
      timeout: 30000,
      waitForNetworkIdle: true,
      stealth: true,
      userAgent:
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 InvestmentAnalysisTool/1.0',
      ...options,
    };
    this.browser = null;
    this.page = null;
  }

  async init() {
    const launchOptions = {
      headless: this.options.headless,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    };

    // Support real Chrome mode (non-headless, harder to detect)
    if (this.options.realChrome) {
      launchOptions.headless = false;
      launchOptions.args.push('--disable-blink-features=AutomationControlled');
      launchOptions.defaultViewport = null;
    }

    this.browser = await puppeteer.launch(launchOptions);
    this.page = await this.browser.newPage();
    await this.page.setUserAgent(this.options.userAgent);
    await this.page.setViewport({ width: 1920, height: 1080 });
  }

  async close() {
    if (this.browser) {
      await this.browser.close();
    }
  }

  /**
   * Generic fetch and parse - auto-detects content
   */
  async fetchAndParse(url, options = {}) {
    const config = { ...this.options, ...options };

    try {
      console.log(`\n📍 Fetching: ${url}`);
      await this.page.goto(url, {
        waitUntil: config.waitForNetworkIdle ? 'networkidle2' : 'load',
        timeout: config.timeout,
      });

      // Collect all available data
      const data = {
        url,
        timestamp: new Date().toISOString(),
        metadata: await this.extractMetadata(),
        content: await this.extractContent(),
        tables: await this.extractTables(),
        links: await this.extractLinks(),
        structuredData: await this.extractStructuredData(),
        formFields: await this.extractFormFields(),
        images: await this.extractImages(),
      };

      console.log(`✅ Successfully parsed ${url}`);
      return data;
    } catch (err) {
      console.error(`❌ Error fetching ${url}:`, err.message);
      throw err;
    }
  }

  /**
   * Extract metadata (title, description, author, etc.)
   */
  async extractMetadata() {
    return this.page.evaluate(() => {
      const meta = {};

      // Standard meta tags
      meta.title = document.title;
      meta.description =
        document.querySelector('meta[name="description"]')?.content || null;
      meta.author =
        document.querySelector('meta[name="author"]')?.content || null;
      meta.keywords =
        document.querySelector('meta[name="keywords"]')?.content || null;

      // Open Graph (social media)
      meta.og = {
        title: document.querySelector('meta[property="og:title"]')?.content,
        description: document.querySelector('meta[property="og:description"]')
          ?.content,
        image: document.querySelector('meta[property="og:image"]')?.content,
        type: document.querySelector('meta[property="og:type"]')?.content,
      };

      // Published date patterns
      meta.datePublished =
        document.querySelector('meta[property="article:published_time"]')
          ?.content ||
        document.querySelector('meta[name="publish_date"]')?.content ||
        document.querySelector('time')?.dateTime ||
        null;

      // Canonical URL
      meta.canonical = document.querySelector('link[rel="canonical"]')?.href;

      // Language
      meta.lang = document.documentElement.lang;

      // Character set
      meta.charset = document.querySelector('meta[charset]')?.charset;

      return meta;
    });
  }

  /**
   * Extract main content (text, headings, paragraphs)
   */
  async extractContent() {
    return this.page.evaluate(() => {
      const content = {};

      // Main heading
      content.mainHeading = document.querySelector('h1')?.textContent.trim();

      // All headings hierarchy
      content.headings = Array.from(
        document.querySelectorAll('h1, h2, h3, h4, h5, h6')
      ).map(h => ({
        level: parseInt(h.tagName[1]),
        text: h.textContent.trim(),
      }));

      // Paragraphs
      const paragraphs = Array.from(document.querySelectorAll('p')).map(p =>
        p.textContent.trim()
      );
      content.paragraphs = paragraphs.filter(p => p.length > 20); // Filter short ones
      content.paragraphCount = paragraphs.length;

      // Body text
      content.bodyText =
        document.body.innerText.substring(0, 5000) + '...'; // First 5000 chars
      content.bodyTextLength = document.body.innerText.length;

      // Lists
      content.lists = Array.from(document.querySelectorAll('ul, ol')).map(
        list => ({
          type: list.tagName,
          items: Array.from(list.querySelectorAll('li')).map(li =>
            li.textContent.trim()
          ),
        })
      );

      // Blockquotes
      content.blockquotes = Array.from(
        document.querySelectorAll('blockquote')
      ).map(bq => bq.textContent.trim());

      // Code blocks
      content.codeBlocks = Array.from(document.querySelectorAll('pre, code')).map(
        code => code.textContent.trim()
      );

      return content;
    });
  }

  /**
   * Extract all tables with intelligent parsing
   */
  async extractTables() {
    return this.page.evaluate(() => {
      const tables = Array.from(document.querySelectorAll('table')).map(
        (table, idx) => {
          // Extract headers
          const headers = Array.from(
            table.querySelectorAll('thead th, tr:first-child th, tr:first-child td')
          ).map(th => th.textContent.trim());

          // Extract rows
          const rows = Array.from(table.querySelectorAll('tbody tr, tr')).map(
            row => {
              const cells = Array.from(row.querySelectorAll('td, th')).map(
                cell => ({
                  text: cell.textContent.trim(),
                  isHeader: cell.tagName === 'TH',
                })
              );

              return cells.map(c => c.text);
            }
          );

          // If no headers detected, use first row as headers
          const finalHeaders = headers.length > 0 ? headers : rows[0] || [];
          const dataRows = headers.length > 0 ? rows : rows.slice(1);

          // Convert to array of objects for easier processing
          const data = dataRows.map(row => {
            const obj = {};
            finalHeaders.forEach((header, i) => {
              obj[header] = row[i] || null;
            });
            return obj;
          });

          return {
            id: `table-${idx}`,
            headers: finalHeaders,
            rows: rows.slice(0, 10), // First 10 rows for preview
            rowCount: rows.length,
            colCount: headers.length,
            data: data.slice(0, 5), // First 5 rows as objects
            allRows: rows,
          };
        }
      );

      return tables;
    });
  }

  /**
   * Extract all links (internal, external, unique)
   */
  async extractLinks() {
    return this.page.evaluate(() => {
      const links = Array.from(document.querySelectorAll('a[href]'))
        .map(a => ({
          text: a.textContent.trim(),
          href: a.href,
          target: a.target,
          isExternal: !a.href.includes(window.location.hostname),
        }))
        .filter(l => l.href && l.href.startsWith('http'));

      // Deduplicate
      const unique = [];
      const seen = new Set();
      links.forEach(link => {
        if (!seen.has(link.href)) {
          seen.add(link.href);
          unique.push(link);
        }
      });

      return {
        totalLinks: links.length,
        uniqueLinks: unique.length,
        internal: unique.filter(l => !l.isExternal),
        external: unique.filter(l => l.isExternal),
        links: unique.slice(0, 20), // First 20 for preview
        allLinks: unique,
      };
    });
  }

  /**
   * Extract structured data (JSON-LD, microdata, RDFa)
   */
  async extractStructuredData() {
    return this.page.evaluate(() => {
      const structured = {};

      // JSON-LD
      const jsonLdScripts = Array.from(
        document.querySelectorAll('script[type="application/ld+json"]')
      ).map(script => {
        try {
          return JSON.parse(script.textContent);
        } catch (e) {
          return null;
        }
      });
      structured.jsonLd = jsonLdScripts.filter(x => x);

      // Schema.org types via data attributes
      const schemaElements = Array.from(
        document.querySelectorAll('[itemtype], [typeof]')
      ).map(el => ({
        type: el.itemType || el.typeof,
        properties: Array.from(el.querySelectorAll('[itemprop], [property]')).map(
          prop => ({
            name: prop.itemProp || prop.property,
            value: prop.content || prop.textContent,
          })
        ),
      }));
      structured.schema = schemaElements;

      // Meta tags with property attribute (Open Graph, Twitter Card, etc.)
      const customMeta = Array.from(
        document.querySelectorAll('meta[property], meta[name^="twitter"]')
      ).map(meta => ({
        key: meta.getAttribute('property') || meta.getAttribute('name'),
        value: meta.getAttribute('content'),
      }));
      structured.customMeta = customMeta;

      return structured;
    });
  }

  /**
   * Extract form fields and structure
   */
  async extractFormFields() {
    return this.page.evaluate(() => {
      const forms = Array.from(document.querySelectorAll('form')).map(
        (form, idx) => ({
          id: form.id || `form-${idx}`,
          action: form.action,
          method: form.method || 'GET',
          fields: Array.from(form.querySelectorAll('input, textarea, select')).map(
            field => ({
              type: field.type,
              name: field.name,
              id: field.id,
              placeholder: field.placeholder,
              required: field.required,
              value: field.value,
              options: field.tagName === 'SELECT'
                ? Array.from(field.querySelectorAll('option')).map(o => o.value)
                : null,
            })
          ),
        })
      );

      return forms;
    });
  }

  /**
   * Extract images
   */
  async extractImages() {
    return this.page.evaluate(() => {
      const images = Array.from(document.querySelectorAll('img')).map(img => ({
        src: img.src,
        alt: img.alt,
        title: img.title,
        width: img.width,
        height: img.height,
      }));

      return {
        count: images.length,
        images: images.slice(0, 10), // First 10
        allImages: images,
      };
    });
  }

  /**
   * Smart extraction based on content type
   */
  async smartExtract(url, hints = {}) {
    const data = await this.fetchAndParse(url, hints);

    // Detect likely content type and extract accordingly
    const contentType = this.detectContentType(data);

    return {
      ...data,
      contentType,
      smartExtract: this.extractByType(data, contentType),
    };
  }

  /**
   * Detect what type of page this is
   */
  detectContentType(data) {
    const { content, tables, links, structuredData } = data;

    // News article
    if (
      content.headings.some(h => h.level === 1) &&
      data.metadata.datePublished &&
      structuredData.jsonLd.some(item => item['@type']?.includes('Article'))
    ) {
      return 'NEWS_ARTICLE';
    }

    // Product/E-commerce
    if (
      structuredData.jsonLd.some(item => item['@type']?.includes('Product')) ||
      content.bodyText.includes('price') ||
      content.bodyText.includes('add to cart')
    ) {
      return 'PRODUCT';
    }

    // Table/Data heavy (financial, statistics)
    if (tables.length > 1 || (tables.length > 0 && tables[0].rowCount > 10)) {
      return 'DATA_TABLE';
    }

    // Directory/Listing
    if (links.allLinks.length > 50 || content.lists.length > 3) {
      return 'DIRECTORY';
    }

    // Video page
    if (
      document.querySelector('video, iframe[src*="youtube"], iframe[src*="vimeo"]')
    ) {
      return 'VIDEO';
    }

    return 'GENERIC';
  }

  /**
   * Extract relevant data based on detected type
   */
  extractByType(data, contentType) {
    const extracted = {};

    switch (contentType) {
      case 'NEWS_ARTICLE':
        extracted.headline = data.metadata.og.title || data.metadata.title;
        extracted.summary = data.metadata.description;
        extracted.datePublished = data.metadata.datePublished;
        extracted.mainContent = data.content.paragraphs.slice(0, 3).join('\n\n');
        extracted.images = data.images.images;
        break;

      case 'DATA_TABLE':
        extracted.tables = data.tables.map(t => ({
          title: `Table ${t.id}`,
          headers: t.headers,
          rows: t.allRows,
          summary: `${t.rowCount} rows × ${t.colCount} columns`,
        }));
        break;

      case 'PRODUCT':
        extracted.title = data.metadata.og.title || data.content.mainHeading;
        extracted.description = data.metadata.description;
        extracted.price = data.content.bodyText.match(/\$[\d,.]+/)?.[0];
        extracted.image = data.images.images[0];
        extracted.specs = data.content.lists;
        break;

      case 'DIRECTORY':
        extracted.title = data.metadata.title;
        extracted.description = data.metadata.description;
        extracted.categories = data.content.lists.slice(0, 3);
        extracted.externalLinks = data.links.allLinks.filter(l => l.isExternal);
        break;

      default:
        extracted.title = data.metadata.title;
        extracted.description = data.metadata.description;
        extracted.mainHeading = data.content.mainHeading;
        extracted.keyPoints = data.content.headings.slice(0, 5);
        extracted.summary = data.content.paragraphs.slice(0, 2).join('\n\n');
    }

    return extracted;
  }

  /**
   * Save results to file
   */
  async saveResults(data, format = 'json', filepath = null) {
    const defaultPath =
      filepath ||
      `/tmp/scrape-${Date.now()}.${format === 'json' ? 'json' : 'md'}`;

    if (format === 'json') {
      fs.writeFileSync(defaultPath, JSON.stringify(data, null, 2));
    } else if (format === 'markdown') {
      const md = this.toMarkdown(data);
      fs.writeFileSync(defaultPath, md);
    } else if (format === 'csv') {
      // For tables
      if (data.tables && data.tables.length > 0) {
        const csv = this.tablesToCSV(data.tables);
        fs.writeFileSync(defaultPath, csv);
      }
    }

    console.log(`💾 Results saved to: ${defaultPath}`);
    return defaultPath;
  }

  /**
   * Convert scraped data to Markdown format
   */
  toMarkdown(data) {
    let md = `# ${data.metadata.title || 'Scraped Page'}\n\n`;

    if (data.metadata.description) {
      md += `> ${data.metadata.description}\n\n`;
    }

    if (data.metadata.datePublished) {
      md += `**Published:** ${data.metadata.datePublished}\n\n`;
    }

    md += `**Source:** [${data.url}](${data.url})\n\n`;

    // Content
    if (data.content.paragraphs.length > 0) {
      md += `## Content\n\n`;
      data.content.paragraphs.slice(0, 5).forEach(p => {
        md += `${p}\n\n`;
      });
    }

    // Tables
    if (data.tables.length > 0) {
      md += `## Data Tables\n\n`;
      data.tables.forEach((table, idx) => {
        md += `### Table ${idx + 1}: ${table.colCount} columns × ${table.rowCount} rows\n\n`;

        // Create markdown table
        md += `| ${table.headers.join(' | ')} |\n`;
        md += `|${table.headers.map(() => ' --- ').join('|')}|\n`;

        table.rows.slice(0, 5).forEach(row => {
          md += `| ${row.join(' | ')} |\n`;
        });

        if (table.rowCount > 5) {
          md += `\n*... and ${table.rowCount - 5} more rows*\n\n`;
        }
      });
    }

    // Links
    if (data.links.allLinks.length > 0) {
      md += `## Links (${data.links.allLinks.length} total)\n\n`;
      data.links.allLinks.slice(0, 10).forEach(link => {
        md += `- [${link.text || link.href}](${link.href})\n`;
      });
      if (data.links.allLinks.length > 10) {
        md += `\n*... and ${data.links.allLinks.length - 10} more*\n\n`;
      }
    }

    return md;
  }

  /**
   * Convert tables to CSV
   */
  tablesToCSV(tables) {
    return tables
      .map((table, idx) => {
        let csv = `# Table ${idx + 1}\n`;
        csv += table.headers.join(',') + '\n';
        table.rows.forEach(row => {
          csv += row.map(cell => `"${cell}"`).join(',') + '\n';
        });
        return csv;
      })
      .join('\n\n');
  }
}

// Export for use as library
module.exports = UniversalScraper;

// CLI usage if run directly
if (require.main === module) {
  (async () => {
    const url = process.argv[2] || 'https://example.com';
    const format = process.argv[3] || 'json';

    const scraper = new UniversalScraper();
    await scraper.init();

    try {
      console.log('\n' + '='.repeat(60));
      console.log('UNIVERSAL WEB SCRAPER');
      console.log('='.repeat(60));

      const data = await scraper.smartExtract(url);

      console.log('\n📊 Analysis Results:');
      console.log(`   Content Type: ${data.contentType}`);
      console.log(`   Tables Found: ${data.tables.length}`);
      console.log(`   Links Found: ${data.links.uniqueLinks}`);
      console.log(`   Text Length: ${data.content.bodyTextLength} chars`);

      await scraper.saveResults(data, format);

      console.log('\n' + '='.repeat(60) + '\n');
    } finally {
      await scraper.close();
    }
  })();
}
