#!/usr/bin/env node
/**
 * General-Purpose HTML Acquisition Tool
 *
 * Usage:
 *   node acquire-html.js --output <dir> --urls <url1,url2,...> [--initial <url>] [--modal <strategy>]
 *
 * Modal Strategies:
 *   wait-for-accept  - Wait for user to click Accept (default for yahoo.com, finance.yahoo.com)
 *   auto-click       - Try to auto-click Accept button (fallback)
 *   detect           - Auto-detect and handle modals intelligently
 *   none             - Skip modal handling
 *
 * Examples:
 *   node acquire-html.js --output ./html --urls "https://example.com" --modal detect
 *   node acquire-html.js --output ./html --initial "https://yahoo.com" --modal wait-for-accept
 */

const UniversalScraper = require('./lib-universal-scraper');
const fs = require('fs');
const path = require('path');

class HTMLAcquisition {
  constructor(options) {
    this.outputDir = options.output;
    this.urls = options.urls || [];
    this.initialUrl = options.initial || null;
    this.modalStrategy = options.modal || 'auto';  // Default: auto-detect per URL
  }

  /**
   * Determine modal strategy based on URL
   */
  getStrategyForUrl(url) {
    // If explicit strategy provided, use it
    if (this.modalStrategy !== 'auto') {
      return this.modalStrategy;
    }

    // Auto-detect based on URL domain
    if (url.includes('yahoo.com')) {
      return 'wait-for-accept';  // Yahoo has persistent privacy modals
    }
    if (url.includes('sec.gov')) {
      return 'none';  // SEC doesn't have privacy modals
    }
    if (url.includes('linkedin.com')) {
      return 'wait-for-accept';
    }
    if (url.includes('facebook.com')) {
      return 'auto-click';
    }

    // Default: try to detect and handle
    return 'detect';
  }

  async acquire() {
    console.log('=== HTML ACQUISITION ===\n');
    console.log(`📁 Output: ${this.outputDir}\n`);

    if (!fs.existsSync(this.outputDir)) {
      fs.mkdirSync(this.outputDir, { recursive: true });
    }

    const scraper = new UniversalScraper({
      headless: false,
      realChrome: true,
      timeout: 20000
    });

    await scraper.init();

    try {
      // Step 1: Initial page for cookie acceptance
      if (this.initialUrl) {
        console.log('📖 Opening initial page\n');
        console.log(`🌐 ${this.initialUrl}\n`);

        await scraper.page.goto(this.initialUrl, {
          waitUntil: 'load',
          timeout: 20000
        });
        console.log('✅ Page loaded\n');

        // Wait for content to appear (blocks user to solve CAPTCHAs, etc.)
        await this.waitForRealContent(scraper.page, this.initialUrl);

        await new Promise(resolve => setTimeout(resolve, 2000));
      }

      // Step 2: Download HTML for URL list
      console.log(`📥 Downloading ${this.urls.length} URLs\n`);

      const results = [];

      for (let i = 0; i < this.urls.length; i++) {
        const url = this.urls[i];
        console.log(`[${i + 1}/${this.urls.length}] 📄 ${url}`);

        try {
          const result = await this.downloadURL(scraper.page, url);
          results.push(result);
          console.log(`  ✅ ${result.filename} (${result.size}KB)\n`);
        } catch (err) {
          console.log(`  ❌ Failed: ${err.message}\n`);
          results.push({
            url,
            success: false,
            error: err.message
          });
        }
      }

      // Save manifest
      const successful = results.filter(r => r.success).length;
      console.log(`=== RESULTS ===\n`);
      console.log(`✅ Downloaded: ${successful}/${this.urls.length}`);
      console.log(`📂 Location: ${this.outputDir}/\n`);

      const manifest = {
        output: this.outputDir,
        initial: this.initialUrl,
        urls: this.urls,
        timestamp: new Date().toISOString(),
        results,
        summary: {
          total: this.urls.length,
          successful,
          failed: this.urls.length - successful
        }
      };

      const manifestFile = path.join(this.outputDir, 'manifest.json');
      fs.writeFileSync(manifestFile, JSON.stringify(manifest, null, 2));
      console.log(`📋 Manifest: manifest.json\n`);

      console.log('=== COMPLETE ===\n');
      console.log(`✅ Done! ${successful}/${this.urls.length} HTML files saved\n`);

      await scraper.close();
      process.exit(0);

    } catch (err) {
      console.error('❌ Error:', err.message);
      await scraper.close();
      process.exit(1);
    }
  }

  /**
   * Sniff page to detect if it's a blocking page (CAPTCHA, bot detection, etc.)
   * or real content
   */
  async isBlockingPage(page) {
    try {
      const pageText = await page.evaluate(() => document.body.innerText);
      const html = await page.evaluate(() => document.documentElement.outerHTML);

      // Detect common blocking indicators
      const blockers = [
        { name: 'CAPTCHA', patterns: ['captcha', 'verify you', 'not a robot', 'recaptcha', 'human'] },
        { name: 'Bot Detection', patterns: ['bot', 'automated', 'suspicious activity', 'temporarily unavailable'] },
        { name: 'Access Denied', patterns: ['access denied', 'access to this page', 'not allowed', '403', '401'] },
        { name: 'Press & Hold', patterns: ['press & hold', 'confirm you are', 'reference id'] },
        { name: 'Rate Limited', patterns: ['rate limit', 'too many requests', '429', 'try again later'] },
        { name: 'Privacy Modal', patterns: ['privacy', 'cookie', 'consent', 'accept all', 'reject all'] }
      ];

      for (const blocker of blockers) {
        for (const pattern of blocker.patterns) {
          if (pageText.toLowerCase().includes(pattern) || html.toLowerCase().includes(pattern)) {
            return { isBlocking: true, type: blocker.name, text: pageText.substring(0, 200) };
          }
        }
      }

      return { isBlocking: false, type: null };
    } catch (err) {
      return { isBlocking: false, type: null };
    }
  }

  /**
   * Wait for real content to appear (sniff page, detect blockers, wait for them to go)
   */
  async waitForRealContent(page, url, maxWaitSeconds = 120) {
    const startTime = Date.now();
    let lastBlockType = null;

    while (Date.now() - startTime < maxWaitSeconds * 1000) {
      const blockStatus = await this.isBlockingPage(page);

      if (!blockStatus.isBlocking) {
        if (lastBlockType) {
          console.log(`✅ Content appeared (${lastBlockType} resolved)\n`);
        } else {
          console.log(`✅ Page content ready\n`);
        }
        return true;
      }

      if (lastBlockType !== blockStatus.type) {
        console.log(`🚫 Blocking detected: ${blockStatus.type}`);
        console.log(`⏳ Waiting for content to appear... (max ${maxWaitSeconds}s)\n`);
        lastBlockType = blockStatus.type;
      }

      // Check every 2 seconds
      await new Promise(resolve => setTimeout(resolve, 2000));
    }

    console.log(`⚠️  Timeout waiting for content (${lastBlockType} still present)\n`);
    return false;
  }

  /**
   * Handle modal based on strategy
   */
  async handleModal(page, strategy) {
    if (strategy === 'none') {
      console.log('⏭️  Skipping modal handling\n');
      return true;
    }

    if (strategy === 'wait-for-accept') {
      console.log('🔐 Modal detected - waiting for user to click Accept');
      console.log('⏳ Click "Accept" on the modal when ready\n');
      return await this.waitForModalGone(page, 60000);
    }

    if (strategy === 'auto-click') {
      console.log('🔐 Modal detected - attempting auto-click\n');
      return await this.autoClickAccept(page);
    }

    if (strategy === 'detect') {
      console.log('🔐 Detecting modal type...\n');
      const hasModal = await this.hasModal(page);
      if (!hasModal) {
        console.log('   ℹ️  No modal detected\n');
        return true;
      }
      // Try auto-click first
      return await this.autoClickAccept(page);
    }

    return true;
  }

  /**
   * Check if modal is present
   */
  async hasModal(page) {
    try {
      return await page.evaluate(() => {
        const modals = document.querySelectorAll(
          '[role="dialog"], .modal, .consent-modal, [data-testid*="modal"], [aria-modal="true"]'
        );
        return modals.length > 0;
      });
    } catch (err) {
      return false;
    }
  }

  /**
   * Wait for modal to disappear (user clicks)
   */
  async waitForModalGone(page, timeout = 60000) {
    const startTime = Date.now();

    while (Date.now() - startTime < timeout) {
      try {
        const modalGone = await page.evaluate(() => {
          const modals = document.querySelectorAll(
            '[role="dialog"], .modal, .consent-modal, [data-testid*="modal"], [aria-modal="true"]'
          );
          return modals.length === 0;
        });

        if (modalGone) {
          console.log('✅ Modal dismissed\n');
          return true;
        }
      } catch (err) {
        if (err.message.includes('Execution context was destroyed')) {
          console.log('✅ Modal handled (context changed)\n');
          return true;
        }
        throw err;
      }

      await new Promise(resolve => setTimeout(resolve, 500));
    }

    console.log('⚠️  Modal timeout - proceeding anyway\n');
    return false;
  }

  /**
   * Try to auto-click Accept button
   */
  async autoClickAccept(page) {
    try {
      const selectors = [
        'button[data-testid="yrco-accept-all"]',
        'button:contains("Accept All")',
        'button[aria-label*="Accept"]',
        'button:has-text("Accept")',
        '[role="button"]:has-text("Accept")',
        'button'
      ];

      for (const selector of selectors) {
        try {
          const buttons = await page.$$(selector);
          for (const button of buttons) {
            const text = await button.evaluate(el => el.textContent);
            if (text && text.toLowerCase().includes('accept')) {
              await button.click();
              await new Promise(resolve => setTimeout(resolve, 1000));
              console.log(`✅ Clicked: "${text.trim().substring(0, 30)}"\n`);
              return true;
            }
          }
        } catch (e) {
          // Continue to next selector
        }
      }

      console.log('ℹ️  No accept button found - proceeding\n');
      return true;
    } catch (err) {
      console.log(`⚠️  Auto-click failed: ${err.message}\n`);
      return true;
    }
  }

  async downloadURL(page, url) {
    try {
      console.log(`  ⏳ Navigating...`);
      const startTime = Date.now();

      await page.goto(url, { waitUntil: 'load', timeout: 15000 });

      const navTime = Date.now() - startTime;
      console.log(`  ✓ Loaded in ${navTime}ms, extracting content...`);

      const html = await page.content();
      const filename = this.urlToFilename(url);
      const filepath = path.join(this.outputDir, filename);

      fs.writeFileSync(filepath, html);

      return {
        url,
        filename,
        success: true,
        size: Math.round(html.length / 1024),
        timestamp: new Date().toISOString()
      };
    } catch (err) {
      throw new Error(`Navigation failed: ${err.message}`);
    }
  }

  urlToFilename(url) {
    const urlObj = new URL(url);
    const pathname = urlObj.pathname
      .replace(/^\/+/, '')
      .replace(/\/+$/, '')
      .replace(/\//g, '__')
      .replace(/[^a-z0-9_-]/gi, '_')
      .toLowerCase();

    return pathname || 'index' + '.html';
  }
}

// Parse CLI arguments
function parseArgs() {
  const args = process.argv.slice(2);
  const options = {};

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--output' && args[i + 1]) {
      options.output = args[i + 1];
      i++;
    } else if (args[i] === '--urls' && args[i + 1]) {
      options.urls = args[i + 1].split(',').map(u => u.trim());
      i++;
    } else if (args[i] === '--initial' && args[i + 1]) {
      options.initial = args[i + 1];
      i++;
    } else if (args[i] === '--modal' && args[i + 1]) {
      options.modal = args[i + 1];
      i++;
    }
  }

  return options;
}

// Main
const options = parseArgs();

if (!options.output || !options.urls || options.urls.length === 0) {
  console.error('Usage: node acquire-html.js --output <dir> --urls <url1,url2,...> [--initial <url>] [--modal <strategy>]');
  console.error('\nStrategies: wait-for-accept, auto-click, detect, none');
  console.error('\nExample:');
  console.error('  node acquire-html.js --output ./html --initial "https://yahoo.com" --urls "https://yahoo.com" --modal wait-for-accept');
  console.error('  node acquire-html.js --output ./html --urls "https://sec.gov/..." --modal none');
  process.exit(1);
}

const acquisition = new HTMLAcquisition(options);
acquisition.acquire().catch(console.error);
