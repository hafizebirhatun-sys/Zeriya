const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const pg=await b.newPage();
 await pg.goto('file://'+path.join(__dirname,'birlesik.html')); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(800);
 await pg.pdf({path:path.join(__dirname,'Zeriya_Butun_Icerikler.pdf'),width:'148mm',height:'210mm',printBackground:true,preferCSSPageSize:true});
 await b.close(); console.log('pdf ok');})();
