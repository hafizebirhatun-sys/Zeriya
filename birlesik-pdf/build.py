"""Bütün içerikleri tek PDF'te birleştirir.
Kullanım:  python build.py && node pdf.js
Gerekenler: pip install markdown, Node.js + Playwright (Chromium)
"""
import re, html, os, glob
import markdown

R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
def md(text):
    return markdown.markdown(text, extensions=['tables', 'sane_lists'])

# ---------- Bakara (bakara.txt) ----------
def bakara_html():
    src = open(os.path.join(R, 'bakara-serisi/bakara.txt'), encoding='utf-8').read().strip()
    eps, cur = [], None
    for line in src.split('\n'):
        if line.startswith('## '):
            cur = dict(t=line[3:].strip(), body=[], P='', S='', E='', K='', N='', H='', ref=''); eps.append(cur)
        elif line.startswith('@ '): cur['ref'] = line[2:].strip()
        elif line.startswith('H: '): cur['H'] = line[3:].strip()
        elif line.startswith('> '): cur['body'].append(line[2:].strip())
        elif line[:3] in ('P: ', 'S: ', 'E: ', 'K: ', 'N: '): cur[line[0]] = line[3:].strip()
    fmt = lambda s: re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(s, quote=False))
    out = []
    for i, e in enumerate(eps, 1):
        body = ''.join(f'<p>{fmt(p)}</p>' for p in e['body'])
        extra = ''
        if e['P'] or e['S']:
            extra = '<div class="lessons">' + (f'<p><span class="lab">🧠 Psikolojik ders</span> {fmt(e["P"])}</p>' if e['P'] else '') + (f'<p><span class="lab">👥 Sosyolojik ders</span> {fmt(e["S"])}</p>' if e['S'] else '') + '</div>'
        meta = f'<div class="meta"><p><span class="lab">Ekran yazısı</span> “{fmt(e["E"])}”</p><p><span class="lab">Kaynak</span> {fmt(e["K"])}</p>' + (f'<p class="note"><span class="lab">Not</span> {fmt(e["N"])}</p>' if e['N'] else '') + '</div>'
        out.append(f'<section class="ep"><div class="num">Bakara · {i}. bölüm · {html.escape(e["ref"])}</div><h2>{html.escape(e["t"])}</h2><div class="hlab">Giriş (ilk 2 saniye)</div><div class="hook">{fmt(e["H"])}</div><div class="script">{body}</div>{extra}{meta}</section>')
    return out, [e['t'] for e in eps]

# ---------- Markdown dosyaları ----------
def md_section(path, title):
    text = open(os.path.join(R, path), encoding='utf-8').read()
    return f'<section class="mdsec"><div class="num">{html.escape(title)}</div>{md(text)}</section>'

PARTS = [
    ('Gelenek böyle diyor, din böyle diyor', [
        ('gelenek-ve-din/01_16_ornek.md', '16 örnek'),
        ('gelenek-ve-din/02_toplu_konusma_gelenek_din.md', 'Toplu konuşma metni'),
        ('gelenek-ve-din/03_hayatin_dongusu.md', 'Hayatın döngüsü'),
        ('gelenek-ve-din/04_dogumdan_olume_konusma.md', 'Doğumdan ölüme')]),
    ('Sure serileri ve diğer içerikler', [
        ('icerikler/01_yusuf_serisi.md', 'Yusuf'),
        ('icerikler/02_kehf_serisi.md', 'Kehf'),
        ('icerikler/03_hucurat_nur_meryem.md', 'Hucurât, Nûr, Meryem'),
        ('icerikler/04_ali_imran_ve_nazziat.md', 'Âl-i İmrân, Nâziât, Âdiyât'),
        ('icerikler/05_sorular_ve_kadinlar.md', 'Sorular, kadınlar, duygular'),
        ('icerikler/06_1400_yil_once_bugun.md', '1400 yıl önce, bugün'),
        ('icerikler/07_tefekkur_ve_ramazan.md', 'Tefekkür ve Ramazan'),
        ('icerikler/09_son_eklenenler.md', 'Son eklenenler'),
        ('icerikler/08_yazarlik_ve_hesap.md', 'Yazarlık ve hesap')]),
]

def carousel_html():
    files = sorted(glob.glob(os.path.join(R, 'carousel-hz-musa/gorseller/*.png')))
    if not files: return ''
    imgs = ''.join(f'<img src="file:///{f.replace(os.sep, "/")}">' for f in files)
    return f'<section class="car"><div class="num">Hz. Musa\'nın duaları · carousel görselleri</div><div class="grid">{imgs}</div></section>'

def fontface():
    eb = os.path.join(R, 'bakara-serisi'); am = os.path.join(R, 'video-sablonlari/fonts')
    u = lambda p: 'file:///' + p.replace(os.sep, '/')
    L = 'U+0000-00FF'; X = 'U+0100-024F,U+1E00-1EFF,U+2000-206F'
    def F(fam, st, wt, f, rng): return f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{wt};src:url('{u(f)}');unicode-range:{rng};}}"
    return ''.join([
        F('EBG','normal',500,f'{eb}/EBGaramond-normal-500-latin.woff2',L), F('EBG','normal',500,f'{eb}/EBGaramond-normal-500-latin-ext.woff2',X),
        F('EBG','normal',700,f'{eb}/EBGaramond-normal-700-latin.woff2',L), F('EBG','normal',700,f'{eb}/EBGaramond-normal-700-latin-ext.woff2',X),
        F('EBG','italic',500,f'{eb}/EBGaramond-italic-500-latin.woff2',L), F('EBG','italic',500,f'{eb}/EBGaramond-italic-500-latin-ext.woff2',X),
        f"@font-face{{font-family:'AmiriX';font-weight:700;src:url('{u(am+'/Amiri-normal-700-arabic.woff2')}');}}"])

CSS = fontface() + '''
@page{size:148mm 210mm;margin:14mm 13mm 15mm}
body{font-family:'EBG','AmiriX',serif;color:#2e2117;font-size:12pt;line-height:1.5;background:#fff}
.cover{box-sizing:border-box;height:176mm;background:#f6eedd;display:flex;flex-direction:column;justify-content:center;text-align:center;page-break-after:always;border:1.5px solid #9a6a3a;outline:1px solid #9a6a3a;outline-offset:-6px;padding:14mm}
.cover h1{font-size:30pt;line-height:1.1;color:#7c2a1a;margin:0 0 6mm}.cover .s{font-style:italic;font-size:14pt}.cover .b{margin-top:14mm;font-size:11pt;color:#6b4a22}
.toc{page-break-after:always}.toc h3{color:#7c2a1a;font-size:17pt;margin:0 0 4mm}.toc .part{font-weight:700;color:#7c2a1a;margin:3mm 0 1mm}
.toc ol{list-style:none;padding:0;margin:0}.toc li{display:flex;gap:3mm;font-size:10pt;padding:.8mm 0;border-bottom:.4px dotted #b89a73}
.toc .n{width:7mm;color:#7c2a1a;font-weight:700}.toc .tt{flex:1}.toc .r{color:#6b4a22;font-style:italic;white-space:nowrap}
.part-page{page-break-before:always;page-break-after:always;height:176mm;display:flex;flex-direction:column;justify-content:center;text-align:center;background:#f6eedd;border:1.5px solid #9a6a3a;padding:14mm;box-sizing:border-box}
.part-page h1{font-size:26pt;color:#7c2a1a;margin:0}
.ep{page-break-before:always}.num{font-size:9.5pt;letter-spacing:.6pt;text-transform:uppercase;color:#9a6a3a;margin-bottom:2mm}
h2{font-size:19pt;color:#7c2a1a;margin:1mm 0 3mm;line-height:1.15}
.hlab{font-size:8.5pt;letter-spacing:.6pt;text-transform:uppercase;color:#9a6a3a;margin-bottom:1mm}
.hook{font-weight:700;font-size:13.4pt;line-height:1.35;background:#f6eedd;border-left:3px solid #7c2a1a;padding:2.5mm 3mm;margin-bottom:4mm}
.script p{margin:0 0 2.4mm}.script p:last-child b{color:#7c2a1a}
.lessons,.meta{margin-top:4mm;padding:3mm 3.5mm;background:#efe3c8;border-radius:2mm;font-size:10.4pt;line-height:1.42}
.lessons p,.meta p{margin:0 0 1.6mm}.lab{font-weight:700;color:#6b4a22;margin-right:1.5mm}
.meta{background:transparent;border:.6px solid #c7aa80}.note{color:#5d4a36}
.mdsec{page-break-before:always}.mdsec h1{font-size:20pt;color:#7c2a1a;margin:0 0 3mm;line-height:1.15}
.mdsec h2{font-size:15.5pt;color:#7c2a1a;margin:6mm 0 2mm;page-break-after:avoid}
.mdsec h3{font-size:12.5pt;color:#6b4a22;margin:4mm 0 1.5mm;page-break-after:avoid}
.mdsec p{margin:0 0 2.2mm}.mdsec blockquote{margin:2mm 0 3mm;padding:1mm 0 1mm 3.5mm;border-left:3px solid #c7aa80;color:#3a2a1c}
.mdsec blockquote p{margin:0 0 2mm}.mdsec hr{border:0;border-top:.6px solid #c7aa80;margin:4mm 0}
.mdsec ul,.mdsec ol{margin:1mm 0 3mm;padding-left:5mm}.mdsec li{margin-bottom:1mm}
.mdsec table{border-collapse:collapse;width:100%;font-size:9.6pt;margin:2mm 0 3mm}.mdsec th,.mdsec td{border:.5px solid #c7aa80;padding:1mm 1.6mm;vertical-align:top}.mdsec th{background:#efe3c8}
.mdsec code{font-size:9.5pt;background:#efe3c8;padding:0 1mm}
.car{page-break-before:always}.car .grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3mm}.car img{width:100%;border:.5px solid #c7aa80}
'''

def build():
    bk, bk_titles = bakara_html()
    toc = []
    body = []
    # Bakara
    toc.append('<div class="part">1. Bakara Suresi: 49 bölüm</div><ol>' + ''.join(f'<li><span class="n">{i}</span><span class="tt">{html.escape(t)}</span></li>' for i, t in enumerate(bk_titles, 1)) + '</ol>')
    body.append('<div class="part-page"><h1>Bakara Suresi\'nde kimsenin fark etmediği cümleler</h1><p>49 bölüm, ayet sırasına göre</p></div>')
    body += bk
    n = 2
    for title, files in PARTS:
        toc.append(f'<div class="part">{n}. {html.escape(title)}</div><ol>' + ''.join(f'<li><span class="tt">{html.escape(t)}</span></li>' for _, t in files) + '</ol>')
        body.append(f'<div class="part-page"><h1>{html.escape(title)}</h1></div>')
        for p, t in files: body.append(md_section(p, t))
        n += 1
    car = carousel_html()
    if car:
        toc.append(f'<div class="part">{n}. Hz. Musa\'nın duaları: carousel görselleri</div>')
        body.append(car)
    cover = '<div class="cover"><h1>Zeriya</h1><div class="s">Bütün içerikler, tek kitapta</div><div class="b">@zzeriyaca</div></div>'
    doc = f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{cover}<div class="toc"><h3>İçindekiler</h3>{"".join(toc)}</div>{"".join(body)}</body></html>'
    open(os.path.join(os.path.dirname(__file__), 'birlesik.html'), 'w', encoding='utf-8').write(doc)
    print('html hazır')

build()
