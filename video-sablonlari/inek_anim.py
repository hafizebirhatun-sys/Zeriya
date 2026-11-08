import os
from themes import noise, blotch, torn, cow, DEFS
FONTS=open('fonts/local.css').read()+open('fonts/local2.css').read()
INK='#3b2616'; ACC='#8e2b1c'
P=lambda: f"background:{noise()},{blotch()},#ecdfc3;box-shadow:inset 0 0 60px rgba(110,70,30,.55);clip-path:{torn()};"
C=lambda w: cow('#efe2c6',INK,INK,w)
css=FONTS+f'''
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#000}}
#bg{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 35%,#a8968a 0%,#6e5f57 55%,#3b322d 100%)}}
#sil{{position:absolute;left:50%;top:600px;width:640px;margin-left:-320px;opacity:.85}}
#who{{position:absolute;left:0;right:0;top:1180px;text-align:center;font:500 30px 'EB Garamond';color:rgba(255,245,230,.55);letter-spacing:2px}}
.el{{position:absolute;opacity:0;will-change:transform,opacity}}
.panel{{{P()}padding:40px 50px;color:{INK};font-family:'EB Garamond',serif;filter:drop-shadow(0 12px 18px rgba(0,0,0,.45))}}
.h{{font-weight:700;color:{INK}}} .it{{font-style:italic;font-weight:500}} .acc{{color:{ACC}}}
.ar{{font-family:'Amiri';font-weight:700;direction:rtl;color:{INK};line-height:1.7}}
#badge{{right:46px;top:70px;opacity:1}}
#badge .panel{{padding:16px 28px;font-size:36px}}
#sub{{position:absolute;left:60px;right:60px;top:1420px;text-align:center;font:700 58px/1.25 'EB Garamond';color:#fff8ec;text-shadow:0 3px 0 rgba(0,0,0,.6),0 0 24px rgba(0,0,0,.7)}}
#sub span{{background:rgba(30,20,12,.45);padding:6px 18px;border-radius:14px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
svg.draw path{{fill:none;stroke-linecap:round;stroke-linejoin:round}}
'''
strike='<i class="dash" style="position:absolute;left:-6px;right:-6px;top:52%;height:6px;border-radius:3px;background:'+ACC+';transform-origin:left center;transform:rotate(-1.2deg) scaleX(0);display:block"></i>'
cows=''.join(f'''<div style="position:relative;display:inline-block;width:150px;margin:0 8px">{C(150)}
{'' if i==3 else f'<svg class="draw" viewBox="0 0 100 100" style="position:absolute;inset:0"><path pathLength="1" class="dash x{i}" d="M18 18 L82 82" stroke="{ACC}" stroke-width="9" filter="url(#rough)"/><path pathLength="1" class="dash x{i}" d="M82 18 L18 82" stroke="{ACC}" stroke-width="9" filter="url(#rough)"/></svg>'}
{f'<svg class="draw" viewBox="0 0 100 100" style="position:absolute;inset:-16px;width:calc(100% + 32px);height:calc(100% + 32px);overflow:visible"><path pathLength="1" class="dash keep" d="M50 10 C 95 10, 98 92, 50 94 C 3 95, 2 12, 46 10" stroke="{ACC}" stroke-width="4.5" filter="url(#rough)"/></svg>' if i==3 else ''}</div>''' for i in range(5))
body=f'''{DEFS}<div id="bg"></div>
<svg id="sil" viewBox="0 0 320 660"><g fill="#3e3430"><ellipse cx="160" cy="120" rx="95" ry="112"/><path d="M10 660 C 10 380, 60 260, 160 255 C 260 260, 310 380, 310 660 Z"/></g></svg>
<div id="who">· SENİN GÖRÜNTÜN BURADA OLACAK ·</div>
<div class="el" id="badge"><div class="panel h" style="transform:rotate(2deg)">🌙 Ramazan'a <span class="acc">91</span> gün</div></div>
<div class="el" id="s1" style="left:70px;right:70px;top:190px"><div class="panel" style="text-align:center;transform:rotate(-1.2deg)">
 <div class="h it" style="font-size:58px">Kur'an'ın en uzun suresinin adı…</div>
 <div style="display:flex;align-items:center;justify-content:center;gap:26px;margin-top:4px"><div class="h acc" id="inek" style="font-size:170px;line-height:1">İNEK</div><div id="cow1">{C(250)}</div></div></div></div>
<div class="el" id="s2" style="left:160px;right:160px;top:220px"><div class="panel" style="text-align:center;transform:rotate(1.5deg)">{C(230)}<div class="h it" style="font-size:66px;margin-top:6px">Herhangi bir inek.</div></div></div>
<div class="el" id="q0" style="left:70px;top:190px"><div class="panel h it" style="padding:22px 40px;font-size:72px;transform:rotate(-2deg)">Nasıl bir inek?</div></div>
<div class="el" id="q1" style="left:330px;top:350px"><div class="panel h it" style="padding:22px 40px;font-size:72px;transform:rotate(1.5deg)">Rengi ne?</div></div>
<div class="el" id="q2" style="left:150px;top:510px"><div class="panel h it" style="padding:22px 40px;font-size:72px;transform:rotate(-1deg)">Nasıl bir şey?!</div></div>
<div class="el" id="s4" style="left:70px;right:70px;top:200px"><div class="panel" style="text-align:center;transform:rotate(1deg)"><div style="white-space:nowrap">{cows}</div>
 <div class="h it" style="font-size:64px;margin-top:20px">Her soru, seçeneği <span class="acc">azalttı.</span></div></div></div>
<div class="el" id="s5" style="left:70px;right:70px;top:170px"><div class="panel" style="text-align:center;transform:rotate(-.8deg)">
 <div class="ar" style="font-size:86px"><span id="ar1">فَذَبَحُوهَا</span> <span id="hl">وَمَا كَادُوا يَفْعَلُونَ</span></div>
 <svg class="draw" width="160" height="110" viewBox="0 0 160 110" style="display:block;margin:-4px auto 0;overflow:visible"><path pathLength="1" class="dash arrow" d="M96 6 Q56 46 78 100 M56 80 L78 102 L100 84" stroke="{ACC}" stroke-width="7" filter="url(#rough)"/></svg>
 <div class="h" id="ner" style="font-size:86px;line-height:1.05"><span class="acc">NEREDEYSE</span><br><span class="it">yapmayacaklardı.</span></div>
 <div class="h it" style="font-size:40px;margin-top:8px;opacity:.8">Bakara 71</div></div></div>
<div class="el" id="s6" style="left:110px;right:110px;top:190px"><div class="panel" style="transform:rotate(-2deg)">
 <div class="h acc" style="font-size:80px;margin-bottom:6px">Bahanelerim:</div>
 {''.join(f'<div class="h it b{i}" style="font-size:64px;line-height:1.4;opacity:0"><span style="position:relative;display:inline-block">{s}{strike.replace("class=\"dash\"",f"class=\"st{i}\"")}</span></div>' for i,s in enumerate(["Önce biraz araştırayım","Hangi kitaptan başlasam?","Pazartesi başlarım"]))}</div></div>
<div class="el" id="s7" style="left:70px;right:70px;top:230px"><div class="panel" style="text-align:center;transform:rotate(-1deg)"><div class="h" style="font-size:118px;line-height:1.05">Senin <span class="acc">ineğin</span> ne?</div>
 <div class="h it" style="font-size:50px;margin-top:12px;opacity:.85">@zzeriyaca</div></div></div>
<div id="sub"></div>'''
js=r'''
const R=document.createElementNS('http://www.w3.org/2000/svg','svg');
window.ready=document.fonts.ready.then(()=>{
 const el=document.getElementById('hl'); const s5=document.getElementById('s5');
 s5.style.opacity=1; const r=el.getBoundingClientRect(); s5.style.opacity=0;
 const pad=34,px=60,w=r.width+px*2,h=r.height+pad*2;
 R.setAttribute('class','draw');R.setAttribute('width',w);R.setAttribute('height',h);
 R.style.cssText=`position:absolute;left:${r.left-px}px;top:${r.top-pad+12}px;overflow:visible;opacity:0`;R.id='ring';
 R.innerHTML=`<path pathLength="1" class="dash ring" d="M${w*0.62} ${h*0.05} C ${w*1.04} ${h*0.0}, ${w*1.05} ${h*0.96}, ${w*0.5} ${h*0.96} C ${-w*0.05} ${h*0.97}, ${-w*0.05} ${h*0.07}, ${w*0.42} ${h*0.06} L ${w*0.7} ${h*0.07}" stroke="#8e2b1c" stroke-width="7" filter="url(#rough)"/>`;
 document.body.appendChild(R);
 document.querySelectorAll('.dash').forEach(p=>{p.style.strokeDasharray=1;p.style.strokeDashoffset=1;});
});
const cl=x=>Math.max(0,Math.min(1,x)); const eo=x=>1-Math.pow(1-cl(x),3);
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
function show(id,t,a,b){const e=document.getElementById(id);const i=(t-a)/0.45,o=(b-t)/0.35;
 if(t<a||t>b){e.style.opacity=0;return 0}const k=Math.min(cl(i),cl(o));e.style.opacity=k;
 e.style.transform=`translateY(${(1-eo(i))*40}px) scale(${0.9+0.1*back(i)})`;return cl(i);}
function draw(sel,t,a,d){document.querySelectorAll(sel).forEach(p=>p.style.strokeDashoffset=1-eo((t-a)/d));}
const SUB=[[0.3,3.2,"Kur'an'ın en uzun suresinin adı neden İnek?"],[3.4,6.2,"Hz. Musa kavmine diyor ki: Allah size bir inek kesmenizi emrediyor."],[6.3,8.4,"Basit bir emir. Herhangi bir inek."],
[8.6,10.6,"Ama onlar soruyor: Nasıl bir inek?"],[10.7,12.6,"Rengi ne?"],[12.7,14.8,"Nasıl bir şey olduğunu açıkla!"],
[15,18,"Her soru, emri biraz daha zorlaştırıyor."],[18.1,20.6,"Sonunda tarife uyan tek bir inek kalıyor."],
[20.9,23.6,"Fe zebahûhâ ve mâ kâdû yef'alûn."],[23.7,27.4,"Sonunda kestiler. Ama neredeyse yapmayacaklardı."],
[27.8,29.6,"Ben bunu okuyunca kendimi gördüm."],[29.7,31.5,"Önce biraz araştırayım…"],[31.6,33.4,"Hangi kitaptan başlasam?"],[33.5,35.2,"Pazartesi başlarım."],
[35.4,38.8,"Bazen sorular, yapmamak için bulduğumuz en kibar bahane."],[39,43.5,"Senin ineğin ne? Hangi işi sorularla erteliyorsun?"]];
window.setT=function(t){
 document.getElementById('sil').style.transform=`scale(${1+0.01*Math.sin(t*1.3)})`;
 const b=document.getElementById('badge'); b.style.transform=`translateY(${(1-eo(t/0.6))*-60}px)`;
 let k=show('s1',t,0.2,6.2); document.getElementById('inek').style.clipPath=`inset(0 ${100-100*eo((t-0.6)/0.9)}% 0 0)`;
 document.getElementById('cow1').style.transform=`translateX(${(1-eo((t-1.2)/0.6))*80}px) rotate(${Math.sin(t*4)*2}deg)`;
 show('s2',t,6.3,8.5);
 show('q0',t,8.7,14.9);show('q1',t,10.7,14.9);show('q2',t,12.7,14.9);
 show('s4',t,15,20.8); [0,1,2,4].forEach((i,n)=>draw('.x'+i,t,15.6+n*0.65,0.35)); draw('.keep',t,18.4,0.7);
 show('s5',t,20.8,27.6); const ar=document.getElementById('ar1').parentElement; ar.style.clipPath=`inset(0 0 0 ${100-100*eo((t-21.1)/1.4)}%)`;
 const ring=document.getElementById('ring'); if(ring){ring.style.opacity=(t>21&&t<27.6)?Math.min(1,cl((27.6-t)/0.35)):0;} draw('.ring',t,22.6,0.9); draw('.arrow',t,23.5,0.5);
 document.getElementById('ner').style.opacity=cl((t-23.8)/0.4);
 show('s6',t,27.8,35.3); [0,1,2].forEach(i=>{document.querySelector('.b'+i).style.opacity=cl((t-(29.7+i*1.9))/0.3); document.querySelector('.st'+i).style.transform=`rotate(-1.2deg) scaleX(${eo((t-(30.5+i*1.9))/0.5)})`;});
 show('s7',t,38.9,45);
 const s=SUB.find(x=>t>=x[0]&&t<=x[1]); const sub=document.getElementById('sub');
 if(s){sub.innerHTML='<span>'+s[2]+'</span>'; sub.style.opacity=Math.min(cl((t-s[0])/0.2),cl((s[1]-t)/0.2));} else sub.style.opacity=0;
};'''
open('inek_anim.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}<script>{js}</script></body></html>')
print('ok')
