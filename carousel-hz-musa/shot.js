const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const D = __dirname; fs.mkdirSync(path.join(D,'gorseller'),{recursive:true});
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  const n = fs.readdirSync(D).filter(f => /^slide\d+\.html$/.test(f)).length;
  for (let i = 1; i <= n; i++) {
    await pg.goto('file://' + path.join(D, `slide${i}.html`));
    await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(300);
    const r = await pg.evaluate(() => { const s=document.querySelector('.s'); const kids=[...s.children].filter(e=>!['top','foot','arrow','wm'].includes(e.className));
      const top=Math.min(...kids.map(e=>e.getBoundingClientRect().top)); const bot=Math.max(...kids.map(e=>e.getBoundingClientRect().bottom)); return [Math.round(top),Math.round(bot)]; });
    await pg.screenshot({ path: path.join(D, 'gorseller', `musa_${String(i).padStart(2,'0')}.png`) });
    console.log(i, r);
  }
  await b.close();
})();
