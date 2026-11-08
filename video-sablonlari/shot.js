const { chromium } = require('playwright'); const path=require('path'); const fs=require('fs');
(async()=>{ const D=__dirname; const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1080,height:1920}});
 for (const f of fs.readdirSync(D).filter(f=>/^o\d\.html$/.test(f)).sort()) {
  await pg.goto('file://'+path.join(D,f)); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(400);
  await pg.screenshot({path:path.join(D,f.replace('.html','.png')),omitBackground:true}); console.log(f);}
 await b.close();})();
