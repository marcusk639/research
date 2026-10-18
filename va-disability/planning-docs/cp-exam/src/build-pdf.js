// Concatenate the HTML sections and print to PDF with Chromium.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const dir = __dirname;
const parts = ['00-head.html', '01-cover-partA.html', '02-partB1.html', '03-partB2.html', '04-partCDE.html'];
const html = parts.map(p => fs.readFileSync(path.join(dir, p), 'utf8')).join('\n');
const combined = path.join(dir, 'mock-cp-exam.html');
fs.writeFileSync(combined, html);

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
  const page = await browser.newPage();
  await page.goto('file://' + combined, { waitUntil: 'load' });
  await page.pdf({
    path: path.join(dir, '..', 'MOCK-CP-EXAM-PTSD-MST-2026-10-21.pdf'),
    format: 'Letter',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:7pt;font-family:DejaVu Sans,Arial;color:#666;width:100%;padding:0 0.7in;display:flex;justify-content:space-between"><span>Mock C&amp;P Exam — M. Klein — prep material, not evidence · contains PHI</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>',
    margin: { top: '0.7in', bottom: '0.8in', left: '0.7in', right: '0.7in' },
  });
  await browser.close();
  console.log('pdf written');
})();
