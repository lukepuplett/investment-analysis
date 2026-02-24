#!/usr/bin/env node
/**
 * General-Purpose HTML Acquisition Tool
 *
 * Usage:
 *   node acquire-html.js --output <dir> --urls <url1,url2,...> [OPTIONS]
 *
 * Options:
 *   --initial <url>       Initial page to load (for cookie/session setup)
 *   --modal <strategy>    Modal handling: wait-for-accept, auto-click, detect, none (default: auto)
 *   --timeout <ms>        Navigation timeout (default: 15000)
 *   --delay <ms>          Delay between URLs (default: 2000)
 *   --tabs <mode>         Tab mode: new-tab (one tab per URL), single (same tab) (default: new-tab)
 *   --throttle <ms>       Min delay between any navigation (default: 3000)
 *
 * Modal Strategies:
 *   wait-for-accept  - Wait for user to click Accept (default for yahoo.com, finance.yahoo.com)
 *   auto-click       - Try to auto-click Accept button (fallback)
 *   detect           - Auto-detect and handle modals intelligently
 *   none             - Skip modal handling
 *
 * Examples:
 *   node acquire-html.js --output ./html --urls "https://example.com" --tabs new-tab
 *   node acquire-html.js --output ./html --initial "https://yahoo.com" --tabs new-tab --throttle 5000
 *   node acquire-html.js --output ./html --urls "https://example.com" --tabs single --delay 10000
 */

const UniversalScraper = require('./lib-universal-scraper');
const fs = require('fs');
const path = require('path');

/**
 * Simple logger that writes to both console and file
 */
class Logger {
  constructor(logFile) {
    this.logFile = logFile;
    this.startTime = new Date();
    this.writeHeader();
  }

  writeHeader() {
    const header = `\n${'='.repeat(80)}\nHTML Acquisition Log Started: ${this.startTime.toISOString()}\n${'='.repeat(80)}\n`;
    fs.appendFileSync(this.logFile, header);
  }

  log(message) {
    console.log(message);
    const timestamp = new Date().toISOString();
    fs.appendFileSync(this.logFile, `[${timestamp}] ${message}\n`);
  }

  logRequest(index, total, url) {
    const msg = `[${index}/${total}] 📄 ${url}`;
    this.log(msg);
  }

  logSuccess(filename, sizeKb) {
    const msg = `  ✅ ${filename} (${sizeKb}KB)`;
    this.log(msg);
  }

  logError(errorMsg) {
    const msg = `  ❌ Failed: ${errorMsg}`;
    this.log(msg);
  }

  logBlockerDetected(type, text) {
    const msg = `  🚫 Blocker Detected: ${type}`;
    this.log(msg);
    this.log(`     Context: ${text.substring(0, 100).replace(/\n/g, ' ')}`);
  }

  logWaiting(reason, seconds) {
    const msg = `  ⏳ ${reason} (${seconds}s)`;
    this.log(msg);
  }

  logTiming(url, elapsedMs) {
    const msg = `  ⏱️  Request took ${elapsedMs}ms`;
    this.log(msg);
  }

  logSummary(total, successful, failed, duration) {
    const summary = `\n${'='.repeat(80)}\nSummary: ${successful}/${total} successful (${failed} failed) in ${duration}ms\n${'='.repeat(80)}\n`;
    this.log(summary);
  }
}

class HTMLAcquisition {
  constructor(options) {
    this.outputDir = options.output;
    this.urls = options.urls || [];
    this.initialUrl = options.initial || null;
    this.modalStrategy = options.modal || 'auto';  // Default: auto-detect per URL
    this.navigationTimeout = options.timeout || 15000;  // Default: 15 seconds
    this.delayBetweenUrls = options.delay || 2000;  // Default: 2 seconds between URLs
    this.minDelayBetweenNavs = options.throttle || 3000;  // Minimum delay between ANY navigation (configurable)
    this.tabMode = options.tabs || 'new-tab';  // new-tab: one tab per URL, single: reuse same tab
    this.lastNavigationTime = 0;  // Track when we last navigated
    this.logFile = path.join(this.outputDir, 'download.log');
    this.logger = null;
    this.pages = [];  // Track all pages for new-tab mode
  }

  /**
   * Navigate to URL with enforced minimum delay between navigations
   */
  async navigateWithThrottle(page, url, options = {}) {
    const timeSinceLastNav = Date.now() - this.lastNavigationTime;
    const remainingDelay = this.minDelayBetweenNavs - timeSinceLastNav;

    if (remainingDelay > 0) {
      const seconds = (remainingDelay / 1000).toFixed(1);
      console.log(`  ⏳ Throttling: waiting ${seconds}s since last navigation...`);
      if (this.logger) {
        this.logger.log(`  ⏳ Throttling: ${Math.round(remainingDelay)}ms delay to enforce 3s minimum between navs`);
      }
      await new Promise(resolve => setTimeout(resolve, remainingDelay));
    }

    this.lastNavigationTime = Date.now();
    return page.goto(url, options);
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
    if (url.includes('seekingalpha.com')) {
      return 'detect';  // Seeking Alpha has "Press & Hold" bot detection
    }

    // Default: try to detect and handle
    return 'detect';
  }

  /**
   * Determine content detection strategy based on URL
   * Different sites have different content markers for "real content"
   */
  getContentDetectionStrategy(url) {
    if (url.includes('finance.yahoo.com')) {
      return 'yahoo-finance';  // Look for financial data, metrics
    }
    if (url.includes('seekingalpha.com')) {
      return 'seekingalpha';   // Look for transcript/article text
    }
    if (url.includes('sec.gov')) {
      return 'sec-edgar';      // Look for filing document body
    }
    if (url.includes('investor.') || url.includes('/investors/')) {
      return 'company-ir';     // Look for press release/article content
    }
    return 'generic';          // Default: just check for reasonable text content
  }

  /**
   * Detect if page has real content based on URL type
   */
  async hasRealContent(page, url) {
    try {
      const pageText = await page.evaluate(() => document.body.innerText);
      const pageTitle = await page.evaluate(() => document.title);
      const strategy = this.getContentDetectionStrategy(url);

      // Minimum text length check (all strategies)
      const minTextLength = 500;  // At least 500 characters of text

      if (strategy === 'yahoo-finance') {
        // Yahoo Finance: check for proper title (not generic blocker title) + financial data
        const hasProperTitle = pageTitle &&
                              pageTitle.length > 5 &&
                              !pageTitle.includes('Yahoo') &&
                              !pageTitle.includes('Error');

        const hasFinancialData = pageText.toLowerCase().includes('earnings') ||
                                 pageText.toLowerCase().includes('revenue') ||
                                 pageText.toLowerCase().includes('eps') ||
                                 pageText.toLowerCase().includes('price') ||
                                 pageText.toLowerCase().includes('news');

        return pageText.length > minTextLength && hasFinancialData && hasProperTitle;
      }

      if (strategy === 'seekingalpha') {
        // Seeking Alpha: look for transcript/article content
        const hasTranscriptContent = pageText.toLowerCase().includes('earnings call') ||
                                     pageText.toLowerCase().includes('operator') ||
                                     pageText.toLowerCase().includes('question and answer');
        return pageText.length > minTextLength && hasTranscriptContent;
      }

      if (strategy === 'sec-edgar') {
        // SEC EDGAR: look for filing content (10-K, 10-Q, etc.)
        const hasFilingContent = pageText.toLowerCase().includes('item') ||
                                 pageText.toLowerCase().includes('management') ||
                                 pageText.toLowerCase().includes('financial statements');
        return pageText.length > minTextLength && hasFilingContent;
      }

      if (strategy === 'company-ir') {
        // Company IR: look for press release or investor news content
        const hasIRContent = pageText.toLowerCase().includes('announce') ||
                             pageText.toLowerCase().includes('release') ||
                             pageText.toLowerCase().includes('results');
        return pageText.length > minTextLength && hasIRContent;
      }

      // Generic: just check for reasonable text content
      return pageText.length > minTextLength;
    } catch (err) {
      return false;
    }
  }

  async acquire() {
    console.log('=== HTML ACQUISITION ===\n');
    console.log(`📁 Output: ${this.outputDir}\n`);

    if (!fs.existsSync(this.outputDir)) {
      fs.mkdirSync(this.outputDir, { recursive: true });
    }

    this.logger = new Logger(this.logFile);
    this.logger.log('=== HTML ACQUISITION START ===');
    this.logger.log(`Output directory: ${this.outputDir}`);
    this.logger.log(`Total URLs: ${this.urls.length}`);
    this.logger.log(`Tab mode: ${this.tabMode} (new-tab = one tab per URL, single = reuse same tab)`);
    this.logger.log(`Navigation timeout: ${this.navigationTimeout}ms`);
    this.logger.log(`Delay between URLs: ${this.delayBetweenUrls}ms`);
    this.logger.log(`Min delay between navs: ${this.minDelayBetweenNavs}ms\n`);

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

        await this.navigateWithThrottle(scraper.page, this.initialUrl, {
          waitUntil: 'load',
          timeout: 20000
        });
        console.log('✅ Page loaded\n');

        // Wait for content to appear (blocks user to solve CAPTCHAs, etc.)
        await this.waitForRealContent(scraper.page, this.initialUrl);

        await new Promise(resolve => setTimeout(resolve, 2000));
      }

      // Step 2: Download HTML for URL list
      console.log(`📥 Downloading ${this.urls.length} URLs (tab mode: ${this.tabMode})\n`);
      this.logger.log(`\n📥 Downloading ${this.urls.length} URLs (tab mode: ${this.tabMode})`);

      const results = [];
      const downloadStartTime = Date.now();

      for (let i = 0; i < this.urls.length; i++) {
        const url = this.urls[i];
        const requestStartTime = Date.now();

        this.logger.logRequest(i + 1, this.urls.length, url);
        console.log(`[${i + 1}/${this.urls.length}] 📄 ${url}`);

        try {
          let pageToUse = scraper.page;

          // Create new tab for each URL if in new-tab mode
          if (this.tabMode === 'new-tab') {
            pageToUse = await scraper.browser.newPage();
            this.pages.push(pageToUse);
            console.log(`  🆕 Opened new tab (${this.pages.length} tabs open)`);
            if (this.logger) {
              this.logger.log(`  🆕 Created new tab (inherits cookies from initial page)`);
            }
          }

          const result = await this.downloadURL(pageToUse, url);

          // Close tab if in new-tab mode (save memory)
          if (this.tabMode === 'new-tab') {
            await pageToUse.close();
            this.pages = this.pages.filter(p => p !== pageToUse);
            if (this.logger) {
              this.logger.log(`  ❌ Closed tab (${this.pages.length} tabs remaining)`);
            }
          }
          const requestTime = Date.now() - requestStartTime;

          results.push(result);
          this.logger.logSuccess(result.filename, result.size);
          this.logger.logTiming(url, requestTime);
          console.log(`  ✅ ${result.filename} (${result.size}KB)\n`);

          // Add delay between URLs to avoid rate limiting
          if (i < this.urls.length - 1) {
            const delaySeconds = this.delayBetweenUrls / 1000;
            this.logger.logWaiting('Waiting before next request', Math.round(delaySeconds));
            console.log(`⏳ Waiting ${delaySeconds}s before next request...\n`);
            await new Promise(resolve => setTimeout(resolve, this.delayBetweenUrls));
          }
        } catch (err) {
          const requestTime = Date.now() - requestStartTime;

          this.logger.logError(err.message);
          this.logger.logTiming(url, requestTime);
          console.log(`  ❌ Failed: ${err.message}\n`);
          results.push({
            url,
            success: false,
            error: err.message
          });

          // Still add delay even on failure
          if (i < this.urls.length - 1) {
            const delaySeconds = this.delayBetweenUrls / 1000;
            this.logger.logWaiting('Waiting before retry', Math.round(delaySeconds));
            console.log(`⏳ Waiting ${delaySeconds}s before retry...\n`);
            await new Promise(resolve => setTimeout(resolve, this.delayBetweenUrls));
          }
        }
      }

      const totalTime = Date.now() - downloadStartTime;

      // Save manifest
      const successful = results.filter(r => r.success).length;
      const failed = this.urls.length - successful;

      console.log(`=== RESULTS ===\n`);
      console.log(`✅ Downloaded: ${successful}/${this.urls.length}`);
      console.log(`📂 Location: ${this.outputDir}/\n`);

      this.logger.logSummary(this.urls.length, successful, failed, totalTime);

      const manifest = {
        output: this.outputDir,
        initial: this.initialUrl,
        urls: this.urls,
        timestamp: new Date().toISOString(),
        results,
        summary: {
          total: this.urls.length,
          successful,
          failed,
          duration_ms: totalTime,
          log_file: this.logFile
        }
      };

      const manifestFile = path.join(this.outputDir, 'manifest.json');
      fs.writeFileSync(manifestFile, JSON.stringify(manifest, null, 2));
      console.log(`📋 Manifest: manifest.json`);
      console.log(`📝 Log file: download.log\n`);

      console.log('=== COMPLETE ===\n');
      console.log(`✅ Done! ${successful}/${this.urls.length} HTML files saved\n`);

      // Close any remaining pages
      for (const page of this.pages) {
        try {
          await page.close();
        } catch (e) {
          // Page already closed, ignore
        }
      }

      await scraper.close();
      process.exit(0);

    } catch (err) {
      console.error('❌ Error:', err.message);

      // Close any remaining pages on error
      for (const page of this.pages) {
        try {
          await page.close();
        } catch (e) {
          // Ignore
        }
      }

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
      const pageSize = html.length;

      // Check if there's a visible modal/dialog element
      const hasVisibleModal = await page.evaluate(() => {
        const modals = document.querySelectorAll(
          '[role="dialog"], .modal, .consent-modal, [data-testid*="modal"], [aria-modal="true"]'
        );
        for (const modal of modals) {
          const style = window.getComputedStyle(modal);
          if (style.display !== 'none' && style.visibility !== 'hidden') {
            return true;
          }
        }
        return false;
      });

      // If there's a visible modal, it's blocking
      if (hasVisibleModal) {
        return { isBlocking: true, type: 'Modal Dialog', text: pageText.substring(0, 200) };
      }

      // Check for specific full-page blockers (very high confidence patterns)
      const fullPageBlockers = [
        { name: 'Press & Hold', patterns: ['press & hold', 'confirm you are human', 'reference id'] },
        { name: 'CAPTCHA', patterns: ['recaptcha', 'i\'m not a robot', 'verify you\'re human'] },
        { name: 'Rate Limited', patterns: ['too many requests', 'rate limit exceeded', 'try again later'] },
        { name: 'Access Denied', patterns: ['access denied', 'forbidden', '403 error', '401 unauthorized'] }
      ];

      for (const blocker of fullPageBlockers) {
        // Only flag if multiple blockers patterns match AND page is small (likely a blocker page)
        let matchCount = 0;
        for (const pattern of blocker.patterns) {
          if (pageText.toLowerCase().includes(pattern)) {
            matchCount++;
          }
        }
        // Require 2+ pattern matches AND small page size
        if (matchCount >= 2 && pageSize < 50000) {
          return { isBlocking: true, type: blocker.name, text: pageText.substring(0, 200) };
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
    let lastContentStatus = false;
    let sniffCount = 0;

    while (Date.now() - startTime < maxWaitSeconds * 1000) {
      sniffCount++;

      // Get page stats
      const pageStats = await page.evaluate(() => {
        const html = document.documentElement.outerHTML;
        const text = document.body.innerText;
        const title = document.title;
        const hasVisibleModal = (() => {
          const modals = document.querySelectorAll('[role="dialog"], .modal, .consent-modal, [data-testid*="modal"], [aria-modal="true"]');
          for (const modal of modals) {
            const style = window.getComputedStyle(modal);
            if (style.display !== 'none' && style.visibility !== 'hidden') return true;
          }
          return false;
        })();

        return {
          htmlSize: html.length,
          textLength: text.length,
          title: title,
          hasVisibleModal: hasVisibleModal,
          firstLine: text.split('\n')[0]
        };
      });

      const blockStatus = await this.isBlockingPage(page);
      const hasContent = await this.hasRealContent(page, url);

      // Log detailed page stats on each sniff
      if (this.logger) {
        this.logger.log(`  [SNIFF #${sniffCount}] Size: ${Math.round(pageStats.htmlSize/1024)}KB | Text: ${pageStats.textLength} chars | Title: "${pageStats.title}" | Modal: ${pageStats.hasVisibleModal} | Blocking: ${blockStatus.isBlocking} | HasContent: ${hasContent}`);
      }

      // Success: no blocker AND has real content
      if (!blockStatus.isBlocking && hasContent) {
        if (lastBlockType) {
          console.log(`✅ Content appeared (${lastBlockType} resolved)\n`);
        } else {
          console.log(`✅ Page content ready\n`);
        }
        if (this.logger) {
          this.logger.log(`  ✅ Real content detected`);
        }
        return true;
      }

      // Log blocker changes
      if (lastBlockType !== blockStatus.type) {
        if (blockStatus.isBlocking) {
          console.log(`🚫 Blocking detected: ${blockStatus.type}`);
          if (this.logger) {
            this.logger.logBlockerDetected(blockStatus.type, blockStatus.text);
          }

          // Special handling for Press & Hold - requires user action
          if (blockStatus.type === 'Press & Hold') {
            console.log(`⏳ ATTENTION: Press & Hold for ~20 seconds to verify you're human`);
            console.log(`⏳ Waiting up to ${maxWaitSeconds}s for verification...\n`);
            if (this.logger) {
              this.logger.log(`  ⚠️  Requires user interaction: Press & Hold for ~20 seconds`);
            }
          } else {
            console.log(`⏳ Waiting for blocker to clear... (max ${maxWaitSeconds}s)\n`);
          }
        }
        lastBlockType = blockStatus.type;
      }

      // Log content status changes
      if (lastContentStatus !== hasContent) {
        if (!blockStatus.isBlocking && !hasContent) {
          console.log(`⏳ Blocker cleared but waiting for real content to load...\n`);
          if (this.logger) {
            this.logger.log(`  ⏳ Blocker resolved, waiting for page content to render`);
          }
        } else if (!blockStatus.isBlocking && hasContent) {
          if (this.logger) {
            this.logger.log(`  ✅ Real content confirmed`);
          }
        }
        lastContentStatus = hasContent;
      }

      // Check every 2 seconds
      await new Promise(resolve => setTimeout(resolve, 2000));
    }

    console.log(`⚠️  Timeout waiting for content (${lastBlockType} still present or no content detected)\n`);
    if (this.logger) {
      this.logger.log(`  ⚠️  Timeout after ${sniffCount} sniffs: blocker=${lastBlockType}, hasContent=${lastContentStatus}`);
    }
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

      await this.navigateWithThrottle(page, url, { waitUntil: 'load', timeout: this.navigationTimeout });

      const navTime = Date.now() - startTime;
      console.log(`  ✓ Loaded in ${navTime}ms, extracting content...`);

      // Check for blockers and wait for them to disappear
      const blockStatus = await this.isBlockingPage(page);
      if (blockStatus.isBlocking) {
        console.log(`  🚫 Blocker detected: ${blockStatus.type}`);
        if (this.logger) {
          this.logger.logBlockerDetected(blockStatus.type, blockStatus.text);
        }

        // For Press & Hold, inform user and wait longer
        if (blockStatus.type === 'Press & Hold') {
          console.log(`  ⏳ ATTENTION: Press & Hold for ~20 seconds to verify you're human`);
          if (this.logger) {
            this.logger.log(`  ⚠️  Requires user interaction: Press & Hold for ~20 seconds`);
          }
        }

        // Wait for blocker to disappear
        const contentReady = await this.waitForRealContent(page, url, 120);
        if (!contentReady) {
          throw new Error(`Blocker timeout: ${blockStatus.type} not resolved after 120s`);
        }
      }

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
    } else if (args[i] === '--timeout' && args[i + 1]) {
      options.timeout = parseInt(args[i + 1], 10);
      i++;
    } else if (args[i] === '--delay' && args[i + 1]) {
      options.delay = parseInt(args[i + 1], 10);
      i++;
    } else if (args[i] === '--tabs' && args[i + 1]) {
      options.tabs = args[i + 1];
      i++;
    } else if (args[i] === '--throttle' && args[i + 1]) {
      options.throttle = parseInt(args[i + 1], 10);
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
