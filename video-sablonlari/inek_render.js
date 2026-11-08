const { chromium } = require('playwright'); const path=require('path'); const {spawn}=require('child_process');
(async()=>{ const FPS=30, DUR=45, OUT=path.join(__dirname,'inek_ornek.mp4');
 const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1080,height:1920}});
 await pg.goto('file://'+path.join(__dirname,'inek_anim.html')); await pg.evaluate(()=>window.ready); await pg.waitForTimeout(300);
 if(process.argv[2]){ for(const t of process.argv.slice(2)){ await pg.evaluate(t=>setT(t),+t); await pg.screenshot({path:path.join(__dirname,`snap_${t}.jpg`),type:'jpeg',quality:80}); } await b.close(); return; }
 const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','fast','-c:a','aac','-movflags','+faststart',OUT]);
 for(let f=0;f<FPS*DUR;f++){ await pg.evaluate(t=>setT(t),f/FPS); const buf=await pg.screenshot({type:'jpeg',quality:88}); if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); }
 ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close(); console.log('video ok');})();
