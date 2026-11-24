const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+process.cwd()+'/kapak6.html');await p.evaluate(()=>document.fonts.ready);
 fs.mkdirSync('fr6',{recursive:true});
 const FPS=30,D=5.45,N=Math.round(FPS*D);
 for(let i=0;i<N;i++){await p.evaluate(t=>setT(t),i/FPS);await p.screenshot({path:`fr6/f${String(i).padStart(4,'0')}.png`,omitBackground:true});}
 await p.evaluate(()=>setT(2.6));await p.screenshot({path:'kapak6_seffaf.png',omitBackground:true});
 await b.close();console.log('ok',N);
})();
