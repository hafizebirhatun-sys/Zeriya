import os, random
D=os.path.dirname(os.path.abspath(__file__))
FONTS=open(os.path.join(D,'fonts/local.css')).read()+open(os.path.join(D,'fonts/local2.css')).read()
random.seed(11)

def torn(n=34, j=2.2):
    pts=[]
    for i in range(n+1): pts.append((i*100/n, random.uniform(0,j)))
    for i in range(1,n+1): pts.append((100-random.uniform(0,j*0.8), i*100/n))
    for i in range(n,-1,-1): pts.append((i*100/n, 100-random.uniform(0,j)))
    for i in range(n,0,-1): pts.append((random.uniform(0,j*0.8), i*100/n))
    return 'polygon('+','.join(f'{x:.2f}% {y:.2f}%' for x,y in pts)+')'

def noise(op=0.22, freq=0.85, r=0.35,g=0.25,b=0.12):
    s=(f"<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='{freq}' numOctaves='3' stitchTiles='stitch'/>"
       f"<feColorMatrix values='0 0 0 0 {r} 0 0 0 0 {g} 0 0 0 0 {b} 0 0 0 {op} 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")
    return 'url("data:image/svg+xml;utf8,'+s.replace('"',"'").replace('#','%23')+'")'
def blotch(op=0.25):
    return noise(op,0.012,0.45,0.30,0.12)

DEFS='''<svg width="0" height="0" style="position:absolute"><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="5"/><feDisplacementMap in="SourceGraphic" scale="3.5"/></filter>
<filter id="ink"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="2"/><feDisplacementMap in="SourceGraphic" scale="1.6"/></filter></svg>'''

def cow(fill, stroke, spot, w=300):
    return f'''<svg viewBox="0 0 220 170" style="width:{w}px;height:auto"><g fill="{fill}" stroke="{stroke}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" filter="url(#rough)">
<path d="M40 70 Q38 45 70 42 L150 40 Q178 42 176 72 L174 110 Q172 125 155 124 L65 126 Q42 126 41 108 Z"/>
<path d="M55 124 L54 158 M80 125 L80 158 M135 124 L136 158 M160 122 L161 156"/>
<path d="M176 60 Q200 58 205 85 Q206 108 186 112 Q170 110 168 92"/>
<path d="M186 58 Q186 40 196 36 M174 58 Q168 42 160 40" fill="none"/>
<ellipse cx="196" cy="100" rx="12" ry="9" fill="{fill}"/><circle cx="186" cy="78" r="3" fill="{stroke}"/>
<path d="M85 55 Q100 50 104 68 Q100 85 84 80 Q74 70 85 55Z M128 85 Q145 80 148 98 Q140 112 126 104 Q118 94 128 85Z" fill="{spot}"/>
<path d="M60 112 l8 -8 M72 114 l8 -8 M84 115 l8 -8 M110 116 l8 -8 M122 116 l8 -8" stroke-width="2" opacity=".55"/>
<path d="M40 75 Q22 85 26 110" fill="none"/></g></svg>'''

T={
 'parsomen':dict(
   name='Eski kâğıt', ink='#3b2616', acc='#8e2b1c', acc2='#6b4a22', head="'EB Garamond',serif", hand="'EB Garamond',serif", italic='italic',
   cowfill='#efe2c6', cowstroke='#3b2616', cowspot='#3b2616',
   panel=lambda: f"background:{noise()},{blotch()},#ecdfc3;box-shadow:inset 0 0 60px rgba(110,70,30,.55),0 10px 24px rgba(0,0,0,.45);clip-path:{torn()};",
   ar='#3b2616'),
 'tezhip':dict(
   name='Osmanlı tezhip', ink='#f4e7c6', acc='#d8b25a', acc2='#d8b25a', head="'Cormorant Garamond',serif", hand="'Cormorant Garamond',serif", italic='normal',
   cowfill='#f4e7c6', cowstroke='#1d2a4c', cowspot='#1d2a4c',
   panel=lambda: f"background:{noise(0.12,0.9,0.05,0.08,0.2)},#1d2a4c;border:3px solid #d8b25a;outline:2px solid #d8b25a;outline-offset:-14px;box-shadow:0 12px 28px rgba(0,0,0,.5);border-radius:6px;",
   ar='#e8c776'),
 'defter':dict(
   name='Eski defter', ink='#1f3a8a', acc='#b3261e', acc2='#1f3a8a', head="'Caveat',cursive", hand="'Caveat',cursive", italic='normal',
   cowfill='#f6f0dc', cowstroke='#1f3a8a', cowspot='#1f3a8a',
   panel=lambda: (f"background:{noise(0.16)},repeating-linear-gradient(transparent 0 58px,rgba(70,110,190,.38) 58px 60px),linear-gradient(90deg,transparent 70px,rgba(200,60,60,.55) 70px 73px,transparent 73px),#f6f0dc;"
                  f"background-position:0 0,0 22px,0 0,0 0;box-shadow:inset 0 0 40px rgba(120,90,40,.35),0 10px 22px rgba(0,0,0,.45);"),
   ar='#1f3a8a'),
}

def css(t):
    return FONTS+f'''
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;background:transparent;overflow:hidden}}
.top{{position:absolute;left:70px;right:70px;top:150px}} .bot{{position:absolute;left:70px;right:70px;bottom:210px}}
.c{{text-align:center}}
.panel{{{t['panel']()}padding:44px 54px;position:relative;color:{t['ink']};font-family:{t['head']};}}
.h{{font-family:{t['head']};color:{t['ink']};font-weight:700}}
.it{{font-style:{t['italic']};font-weight:500}}
.acc{{color:{t['acc']}}}
.ar{{font-family:'Amiri';font-weight:700;direction:rtl;color:{t['ar']};line-height:1.7}}
.tape{{position:absolute;width:190px;height:52px;background:rgba(222,205,160,.75);box-shadow:0 2px 4px rgba(0,0,0,.15);top:-24px}}
.star{{position:absolute;width:46px;height:46px}}
.strike{{position:relative;display:inline-block}}
.strike svg{{position:absolute;left:-8px;top:42%;width:calc(100% + 16px);height:30px;overflow:visible}}
.ring{{position:fixed;overflow:visible}}
'''

def extras(k):
    if k=='defter':
        return '<div class="tape" style="left:38%;transform:rotate(-4deg)"></div>'
    if k=='tezhip':
        st='<svg class="star" viewBox="0 0 40 40" style="{p}"><g fill="#d8b25a"><rect x="12" y="12" width="16" height="16"/><rect x="12" y="12" width="16" height="16" transform="rotate(45 20 20)"/></g><circle cx="20" cy="20" r="4" fill="#1d2a4c"/></svg>'
        return ''.join(st.format(p=p) for p in ['left:-22px;top:-22px','right:-22px;top:-22px','left:-22px;bottom:-22px','right:-22px;bottom:-22px'])
    return ''

def ring_js(color):
    return '''<script>document.fonts.ready.then(()=>{document.querySelectorAll('.hl').forEach(el=>{const r=el.getBoundingClientRect();
const s=document.createElementNS('http://www.w3.org/2000/svg','svg');s.classList.add('ring');const pad=34,px=60;const w=r.width+px*2,h=r.height+pad*2;
s.setAttribute('width',w);s.setAttribute('height',h);s.style.left=(r.left-px)+'px';s.style.top=(r.top-pad+12)+'px';
s.innerHTML=`<path d="M${w*0.62} ${h*0.05} C ${w*1.04} ${h*0.0}, ${w*1.05} ${h*0.96}, ${w*0.5} ${h*0.96} C ${-w*0.05} ${h*0.97}, ${-w*0.05} ${h*0.07}, ${w*0.42} ${h*0.06} L ${w*0.7} ${h*0.07}" fill="none" stroke="'''+color+'''" stroke-width="7" stroke-linecap="round" filter="url(#rough)"/>`;
document.body.appendChild(s);});});</script>'''

def build(k,t):
    C=lambda w=300: cow(t['cowfill'],t['cowstroke'],t['cowspot'],w)
    X=extras(k)
    strike=f'<svg viewBox="0 0 100 10" preserveAspectRatio="none"><path d="M0 6 Q30 2 55 6 T100 4" stroke="{t["acc"]}" fill="none" style="stroke-width:6px" vector-effect="non-scaling-stroke"/></svg>'
    O={}
    O['o1']=f'''<div class="top"><div class="panel c" style="transform:rotate(-1.2deg)">{X}
<div class="h it" style="font-size:62px">Kur'an'ın en uzun suresinin adı…</div>
<div style="display:flex;align-items:center;justify-content:center;gap:26px;margin-top:6px"><div class="h acc" style="font-size:170px;line-height:1">İNEK</div>{C(250)}</div></div></div>'''
    qs=["Nasıl bir inek?","Rengi ne?","Nasıl bir şey?!"]
    O['o2']=f'''<div class="top">'''+''.join(f'<div class="panel" style="display:inline-block;margin:0 0 30px {m}px;padding:22px 40px;transform:rotate({r}deg)">{X if i==0 else ""}<span class="h it" style="font-size:72px">{q}</span></div><br>' for i,(q,m,r) in enumerate(zip(qs,[0,240,90],[-2,1.5,-1])))+'</div>'
    def cowcell(keep):
        mark='' if keep else f'<svg viewBox="0 0 100 100" style="position:absolute;inset:0"><path d="M18 18 L82 82 M82 18 L18 82" stroke="{t["acc"]}" stroke-width="9" stroke-linecap="round" filter="url(#rough)"/></svg>'
        ring=f'<svg viewBox="0 0 100 100" style="position:absolute;inset:-16px;width:calc(100% + 32px);height:calc(100% + 32px);overflow:visible"><ellipse cx="50" cy="52" rx="47" ry="42" fill="none" stroke="{t["acc"]}" stroke-width="4" filter="url(#rough)"/></svg>' if keep else ''
        return f'<div style="position:relative;display:inline-block;width:150px;margin:0 8px;opacity:{1 if keep else .75}">{C(150)}{mark}{ring}</div>'
    O['o3']=f'''<div class="bot"><div class="panel c" style="transform:rotate(1deg)">{X}<div style="white-space:nowrap">{''.join(cowcell(i==3) for i in range(5))}</div>
<div class="h it" style="font-size:66px;margin-top:22px">Her soru, seçeneği <span class="acc">azalttı.</span></div></div></div>'''
    O['o4']=f'''<div class="top"><div class="panel c" style="transform:rotate(-0.8deg)">{X}<div class="ar" style="font-size:84px">فَذَبَحُوهَا <span class="hl">وَمَا كَادُوا يَفْعَلُونَ</span></div>
<svg width="160" height="110" viewBox="0 0 160 110" style="display:block;margin:-4px auto 0;overflow:visible"><path d="M96 6 Q56 46 78 100 M56 80 L78 102 L100 84" stroke="{t['acc']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" filter="url(#rough)"/></svg>
<div class="h" style="font-size:84px;line-height:1.05"><span class="acc">NEREDEYSE</span><br><span class="it">yapmayacaklardı.</span></div>
<div class="h it" style="font-size:42px;margin-top:10px;opacity:.8">Bakara 71</div></div></div>'''+ring_js(t['acc'])
    O['o5']=f'''<div class="top"><div class="panel" style="transform:rotate(-2deg);width:860px;margin:0 auto">{X}
<div class="h acc" style="font-size:80px;margin-bottom:8px">Bahanelerim:</div>'''+''.join(f'<div class="h it" style="font-size:66px;line-height:1.4"><span class="strike">{s}{strike}</span></div>' for s in ["Önce biraz araştırayım","Hangi kitaptan başlasam?","Pazartesi başlarım"])+'</div></div>'
    O['o6']=f'''<div class="bot"><div class="panel c" style="transform:rotate(-1deg)">{X}<div class="h" style="font-size:118px;line-height:1.05">Senin <span class="acc">ineğin</span> ne?</div>
<div class="h it" style="font-size:50px;margin-top:14px;opacity:.85">@zzeriyaca</div></div></div>'''
    for o,v in O.items():
        open(os.path.join(D,f'{k}_{o}.html'),'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css(t)}</style></head><body>{DEFS}{v}</body></html>')
for k,t in T.items(): build(k,t)
print('ok')
