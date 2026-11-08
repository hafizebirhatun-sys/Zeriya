import os
D=os.path.dirname(os.path.abspath(__file__))
FONTS=open(os.path.join(D,'fonts/local.css')).read()
COW='''<svg viewBox="0 0 220 170" class="cow"><g fill="#fff" stroke="#2a2420" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" filter="url(#rough)">
<path d="M40 70 Q38 45 70 42 L150 40 Q178 42 176 72 L174 110 Q172 125 155 124 L65 126 Q42 126 41 108 Z"/>
<path d="M55 124 L54 158 M80 125 L80 158 M135 124 L136 158 M160 122 L161 156"/>
<path d="M176 60 Q200 58 205 85 Q206 108 186 112 Q170 110 168 92"/>
<path d="M186 58 Q186 40 196 36 M174 58 Q168 42 160 40" fill="none"/>
<ellipse cx="196" cy="100" rx="12" ry="9" fill="#f6b8b0"/>
<circle cx="186" cy="78" r="3" fill="#2a2420"/>
<path d="M85 55 Q100 50 104 68 Q100 85 84 80 Q74 70 85 55Z M128 85 Q145 80 148 98 Q140 112 126 104 Q118 94 128 85Z" fill="#2a2420"/>
<path d="M40 75 Q22 85 26 110" fill="none"/></g></svg>'''
DEFS='''<svg width="0" height="0" style="position:absolute"><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="4"/></filter></svg>'''
CSS=FONTS+'''
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:transparent;overflow:hidden}
.h{font-family:'Caveat',cursive;font-weight:700;color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.55),0 0 18px rgba(0,0,0,.45)}
.y{color:#FFD24A} .r{color:#FF6B5E}
.top{position:absolute;left:60px;right:60px;top:170px}
.bot{position:absolute;left:60px;right:60px;bottom:230px}
.c{text-align:center}
.cow{width:300px;height:auto;filter:drop-shadow(0 4px 6px rgba(0,0,0,.4))}
.bub{display:inline-block;background:#fff;color:#2a2420;font-family:'Caveat';font-weight:700;font-size:74px;padding:14px 38px 20px;border-radius:40px;border:5px solid #2a2420;position:relative;box-shadow:0 8px 18px rgba(0,0,0,.35)}
.bub::after{content:"";position:absolute;bottom:-28px;left:70px;border:16px solid transparent;border-top:24px solid #2a2420}
.note{background:#FFE68A;color:#3a2c18;font-family:'Caveat';font-weight:700;font-size:72px;line-height:1.35;padding:46px 56px;transform:rotate(-2.5deg);box-shadow:0 14px 30px rgba(0,0,0,.4);border-radius:6px;width:860px;margin:0 auto}
.note .t{font-size:84px;color:#b5402e;margin-bottom:10px}
.strike{position:relative;display:inline-block}
.strike svg{position:absolute;left:-10px;top:38%;width:calc(100% + 20px);height:40px;overflow:visible}
.ar{font-family:'Amiri';font-weight:700;font-size:96px;direction:rtl;line-height:1.8;color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.6),0 0 22px rgba(0,0,0,.5)}
.hl{position:relative;display:inline-block}
.ring{position:absolute;overflow:visible;pointer-events:none}
'''
def ring_js(color):
    return '''<script>
document.fonts.ready.then(()=>{document.querySelectorAll('.hl').forEach(el=>{const r=el.getBoundingClientRect();
const s=document.createElementNS('http://www.w3.org/2000/svg','svg');s.classList.add('ring');
const pad=38,px=70;s.setAttribute('width',r.width+px*2);s.setAttribute('height',r.height+pad*2);
s.style.left=(r.left-px)+'px';s.style.top=(r.top-pad+14)+'px';s.style.position='fixed';
const w=r.width+px*2,h=r.height+pad*2;
s.innerHTML=`<path d="M${w*0.62} ${h*0.04} C ${w*1.04} ${h*0.0}, ${w*1.06} ${h*0.96}, ${w*0.5} ${h*0.97} C ${-w*0.06} ${h*0.98}, ${-w*0.05} ${h*0.06}, ${w*0.42} ${h*0.05} L ${w*0.7} ${h*0.06}" fill="none" stroke="'''+color+'''" stroke-width="9" stroke-linecap="round" filter="url(#rough)"/>`;
document.body.appendChild(s);});document.body.dataset.ready=1;});</script>'''
STRIKE='<svg viewBox="0 0 100 10" preserveAspectRatio="none"><path d="M0 6 Q30 2 55 6 T100 4" stroke="#c0392b" stroke-width="2.4" fill="none" vector-effect="non-scaling-stroke" style="stroke-width:7px"/></svg>'
def cows_row():
    out=[]
    for i in range(5):
        keep=(i==3)
        mark=('' if keep else '<svg viewBox="0 0 100 100" style="position:absolute;inset:0" ><path d="M15 15 L85 85 M85 15 L15 85" stroke="#FF5A4E" stroke-width="11" stroke-linecap="round" filter="url(#rough)"/></svg>')
        ring=('<svg viewBox="0 0 100 100" style="position:absolute;inset:-18px;width:calc(100% + 36px);height:calc(100% + 36px);overflow:visible"><ellipse cx="50" cy="52" rx="47" ry="42" fill="none" stroke="#FFD24A" stroke-width="5" filter="url(#rough)"/></svg>' if keep else '')
        out.append(f'<div style="position:relative;width:170px;display:inline-block;margin:0 12px;opacity:{1 if keep else .8}">{COW.replace("class=\"cow\"","style=\"width:170px\"")}{mark}{ring}</div>')
    return ''.join(out)
O={}
O['o1']=f'''<div class="top c"><div class="h" style="font-size:76px">Kur'an'ın en uzun suresinin adı…</div>
<div style="display:flex;align-items:center;justify-content:center;gap:24px;margin-top:10px"><div class="h y" style="font-size:200px;line-height:1">İNEK</div>{COW}</div>
<svg width="640" height="40" viewBox="0 0 640 40" style="display:block;margin:-10px auto 0"><path d="M10 25 Q200 8 330 22 T630 14" stroke="#FFD24A" stroke-width="10" fill="none" stroke-linecap="round" filter="url(#rough)"/></svg></div>'''
O['o2']='''<div class="top"><div class="bub" style="margin-left:0">Nasıl bir inek?</div><br><br>
<div class="bub" style="margin-left:250px">Rengi ne?</div><br><br>
<div class="bub" style="margin-left:90px">Nasıl bir şey?! 🤔</div></div>'''.replace(' 🤔','')
O['o3']=f'''<div class="bot c"><div style="white-space:nowrap">{cows_row()}</div>
<div class="h" style="font-size:78px;margin-top:40px">Her soru, seçeneği <span class="y">azalttı.</span></div></div>'''
O['o4']='''<div class="top c"><div class="ar">فَذَبَحُوهَا <span class="hl">وَمَا كَادُوا يَفْعَلُونَ</span></div>
<svg width="200" height="150" viewBox="0 0 200 150" style="display:block;margin:-6px auto 0;overflow:visible"><path d="M120 6 Q70 60 98 138 M72 112 L98 140 L126 116" stroke="#FFD24A" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round" filter="url(#rough)"/></svg>
<div class="h" style="font-size:96px;line-height:1.05"><span class="y">NEREDEYSE</span><br>yapmayacaklardı.</div>
<div class="h" style="font-size:52px;margin-top:16px;opacity:.9">Bakara 71</div></div>'''+ring_js('#FF5A4E')
O['o5']=f'''<div class="top"><div class="note"><div class="t">Bahanelerim:</div>
<div><span class="strike">Önce biraz araştırayım{STRIKE}</span></div>
<div><span class="strike">Hangi kitaptan başlasam?{STRIKE}</span></div>
<div><span class="strike">Pazartesi başlarım{STRIKE}</span></div></div></div>'''
O['o6']='''<div class="bot c"><div class="h" style="font-size:132px;line-height:1.05">Senin <span class="y">ineğin</span> ne?</div>
<svg width="520" height="40" viewBox="0 0 520 40" style="display:block;margin:4px auto 0"><path d="M10 22 Q160 6 260 20 T510 14" stroke="#FFD24A" stroke-width="9" fill="none" stroke-linecap="round" filter="url(#rough)"/></svg>
<div class="h" style="font-size:60px;margin-top:22px;opacity:.95">@zzeriyaca</div></div>'''
for k,v in O.items():
    open(os.path.join(D,k+'.html'),'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{DEFS}{v}</body></html>')
print(list(O))
