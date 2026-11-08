const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const pg=await b.newPage();
 await pg.goto('file://'+path.join(__dirname,'bakara.html')); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(500);
 await pg.pdf({path:path.join(__dirname,'Bakara_Serisi_49_Bolum.pdf'),width:'148mm',height:'210mm',printBackground:true,preferCSSPageSize:true});
 await b.close(); console.log('pdf ok');})();
