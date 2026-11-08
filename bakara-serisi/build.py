import re, html
src=open('bakara.txt',encoding='utf-8').read().strip()
eps=[]; cur=None
for line in src.split('\n'):
    if line.startswith('## '):
        cur=dict(t=line[3:].strip(),body=[],P='',S='',E='',K='',N='',H='',ref=''); eps.append(cur)
    elif line.startswith('@ '): cur['ref']=line[2:].strip()
    elif line.startswith('H: '): cur['H']=line[3:].strip()
    elif line.startswith('> '): cur['body'].append(line[2:].strip())
    elif line[:3] in ('P: ','S: ','E: ','K: ','N: '): cur[line[0]]=line[3:].strip()
def fmt(s):
    s=html.escape(s,quote=False); return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
toc=''.join(f'<li><span class="n">{i}</span><span class="tt">{html.escape(e["t"])}</span><span class="r">{html.escape(e["ref"])}</span></li>' for i,e in enumerate(eps,1))
parts=[]
for i,e in enumerate(eps,1):
    body=''.join(f'<p>{fmt(p)}</p>' for p in e['body'])
    extra=''
    if e['P'] or e['S']:
        extra='<div class="lessons">'+(f'<p><span class="lab">🧠 Psikolojik ders</span> {fmt(e["P"])}</p>' if e['P'] else '')+(f'<p><span class="lab">👥 Sosyolojik ders</span> {fmt(e["S"])}</p>' if e['S'] else '')+'</div>'
    meta=f'<div class="meta"><p><span class="lab">Ekran yazısı</span> “{fmt(e["E"])}”</p><p><span class="lab">Kaynak</span> {fmt(e["K"])}</p>'+(f'<p class="note"><span class="lab">Not</span> {fmt(e["N"])}</p>' if e['N'] else '')+'</div>'
    parts.append(f'<section class="ep"><div class="num">{i}. Bölüm · {html.escape(e["ref"])}</div><h2>{html.escape(e["t"])}</h2><div class="hlab">Giriş (ilk 2 saniye)</div><div class="hook">{fmt(e["H"])}</div><div class="script">{body}</div>{extra}{meta}</section>')
F=lambda fam,st,wt,f,rng: f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{wt};src:url('{f}');unicode-range:{rng};}}"
L='U+0000-00FF'; X='U+0100-024F,U+1E00-1EFF,U+2000-206F'
fonts=''.join([F('EBG','normal',500,'EBGaramond-normal-500-latin.woff2',L),F('EBG','normal',500,'EBGaramond-normal-500-latin-ext.woff2',X),
 F('EBG','normal',700,'EBGaramond-normal-700-latin.woff2',L),F('EBG','normal',700,'EBGaramond-normal-700-latin-ext.woff2',X),
 F('EBG','italic',500,'EBGaramond-italic-500-latin.woff2',L),F('EBG','italic',500,'EBGaramond-italic-500-latin-ext.woff2',X)])
css=fonts+'''
@page{size:148mm 210mm;margin:14mm 13mm 15mm}
body{font-family:'EBG',serif;color:#2e2117;font-size:12.2pt;line-height:1.5;background:#fff}
.cover{box-sizing:border-box;height:176mm;background:#f6eedd;display:flex;flex-direction:column;justify-content:center;text-align:center;page-break-after:always;border:1.5px solid #9a6a3a;outline:1px solid #9a6a3a;outline-offset:-6px;padding:14mm}
.cover h1{font-size:30pt;line-height:1.1;color:#7c2a1a;margin:0 0 6mm}.cover .s{font-style:italic;font-size:14pt}.cover .b{margin-top:14mm;font-size:11pt;color:#6b4a22}
.toc{page-break-after:always}.toc h3{color:#7c2a1a;font-size:17pt;margin:0 0 4mm}
.toc ol{list-style:none;padding:0;margin:0}.toc li{display:flex;gap:3mm;font-size:10.6pt;padding:1.1mm 0;border-bottom:.4px dotted #b89a73}
.toc .n{width:7mm;color:#7c2a1a;font-weight:700}.toc .tt{flex:1}.toc .r{color:#6b4a22;font-style:italic;white-space:nowrap}
.ep{page-break-before:always}.num{font-size:9.5pt;letter-spacing:.6pt;text-transform:uppercase;color:#9a6a3a}
h2{font-size:19pt;color:#7c2a1a;margin:1mm 0 3mm;line-height:1.15}
.hlab{font-size:8.5pt;letter-spacing:.6pt;text-transform:uppercase;color:#9a6a3a;margin-bottom:1mm}
.hook{font-weight:700;font-size:13.4pt;line-height:1.35;background:#f6eedd;border-left:3px solid #7c2a1a;padding:2.5mm 3mm;margin-bottom:4mm}
.script p{margin:0 0 2.4mm}.script p:last-child b{color:#7c2a1a}
.lessons,.meta{margin-top:4mm;padding:3mm 3.5mm;background:#efe3c8;border-radius:2mm;font-size:10.4pt;line-height:1.42}
.lessons p,.meta p{margin:0 0 1.6mm}.lab{font-weight:700;color:#6b4a22;margin-right:1.5mm}
.meta{background:transparent;border:.6px solid #c7aa80}.note{color:#5d4a36}
'''
cover='<div class="cover"><h1>Bakara Suresi\'nde<br>kimsenin fark etmediği<br>cümleler</h1><div class="s">Ayet sırasına göre 49 bölüm</div><div class="b">@zzeriyaca</div></div>'
open('bakara.html','w',encoding='utf-8').write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{css}</style></head><body>{cover}<div class="toc"><h3>İçindekiler</h3><ol>{toc}</ol></div>{"".join(parts)}</body></html>')
print(len(eps))
