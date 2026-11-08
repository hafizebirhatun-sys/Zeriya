import os
D = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(D, "fonts/local.css")).read()

SLIDES = [
 dict(kind="cover"),
 dict(title="Hata yaptığında", sit="Bir hata yaptı ve pişmanlıkla Rabbine döndü.",
      ar="رَبِّ إِنِّي ظَلَمْتُ نَفْسِي فَاغْفِرْ لِي", ok="Rabbi innî zalemtü nefsî fağfir lî",
      meal="Rabbim, ben kendime zulmettim, beni bağışla.", ref="Kasas 16", end="Hata yaptın diye bitmedin."),
 dict(title="Korktuğunda", sit="Şehirden korka korka, etrafına bakınarak çıktı.",
      ar="رَبِّ نَجِّنِي مِنَ الْقَوْمِ الظَّالِمِينَ", ok="Rabbi neccinî mine'l-kavmi'z-zâlimîn",
      meal="Rabbim, beni zalimler topluluğundan kurtar.", ref="Kasas 21", end="Korkmak imansızlık değil."),
 dict(title="Yolunu bilmediğinde", sit="Nereye gittiğini bilmeden yola çıktı.",
      ar="عَسَىٰ رَبِّي أَنْ يَهْدِيَنِي سَوَاءَ السَّبِيلِ", ok="Asâ Rabbî en yehdiyenî sevâe's-sebîl",
      meal="Umarım Rabbim beni doğru yola iletir.", ref="Kasas 22", end="Haritan yoksa, Rehberin var."),
 dict(title="Yalnız ve muhtaç kaldığında", sit="Garip bir şehirde, yorgun ve aç, bir ağacın gölgesine oturdu.",
      ar="رَبِّ إِنِّي لِمَا أَنْزَلْتَ إِلَيَّ مِنْ خَيْرٍ فَقِيرٌ", ok="Rabbi innî limâ enzelte ileyye min hayrin fakîr",
      meal="Rabbim, bana indireceğin her hayra muhtacım.", ref="Kasas 24", end="Bu duadan sonra kapı çalındı."),
 dict(title="Yük ağır geldiğinde", sit="Firavun'a gitmesi emredildi. Dili tutuluyor, kalbi daralıyordu.",
      ar="رَبِّ اشْرَحْ لِي صَدْرِي ۝٢٥ وَيَسِّرْ لِي أَمْرِي ۝٢٦<br>وَاحْلُلْ عُقْدَةً مِنْ لِسَانِي ۝٢٧ يَفْقَهُوا قَوْلِي ۝٢٨",
      ok="Rabbi'şrah lî sadrî, ve yessir lî emrî, vahlul ukdeten min lisânî, yefkahû kavlî",
      meal="Rabbim, göğsümü aç, işimi kolaylaştır, dilimdeki düğümü çöz ki sözümü anlasınlar.",
      ref="Tâhâ 25–28", end="Sınavdan, görüşmeden, zor bir konuşmadan önce.", long=True),
 dict(kind="answer", title="Allah'ın cevabı", sit="Musa ve Harun “korkuyoruz” dediler. Cevap geldi:",
      ar="لَا تَخَافَا إِنَّنِي مَعَكُمَا أَسْمَعُ وَأَرَىٰ", ok="Lâ tehâfâ innenî meakümâ esmeu ve erâ",
      meal="Korkmayın, ben sizinle beraberim; işitirim ve görürüm.", ref="Tâhâ 46"),
 dict(title="Çıkış yok gibi göründüğünde", sit="Önünde deniz, arkasında Firavun'un ordusu. Herkes “yakalandık” dedi.",
      ar="كَلَّا إِنَّ مَعِيَ رَبِّي سَيَهْدِينِ", ok="Kellâ, inne maiye Rabbî seyehdîn",
      meal="Asla! Rabbim benimle, bana yol gösterecek.", ref="Şuarâ 62", end="Ve deniz yarıldı."),
 dict(kind="close"),
]
N = len(SLIDES)

CSS = FONTS + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden}
.s{width:1080px;height:1350px;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;
   padding:120px 110px;text-align:center;font-family:'Lora',serif;background:#F4EDE2;color:#3A2C24}
.s::before{content:"";position:absolute;inset:38px;border:2px solid rgba(168,123,79,.45);border-radius:6px;pointer-events:none}
.s::after{content:"";position:absolute;inset:50px;border:1px solid rgba(168,123,79,.22);border-radius:4px;pointer-events:none}
.dark{background:radial-gradient(ellipse at 50% 40%,#3A2B23 0%,#211813 75%);color:#F3E8D8}
.dark::before{border-color:rgba(214,170,112,.5)} .dark::after{border-color:rgba(214,170,112,.22)}
.top{position:absolute;top:84px;left:100px;right:100px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:3px;
     text-transform:uppercase;color:#A87B4F}
.dark .top{color:#D6AA70}
.foot{position:absolute;bottom:80px;left:0;right:0;font-size:24px;letter-spacing:2px;color:#A87B4F;opacity:.85}
.dark .foot{color:#D6AA70}
.arrow{position:absolute;bottom:72px;right:100px;font-size:44px;color:#A87B4F}
.dark .arrow{color:#D6AA70}
h2{font-weight:600;font-size:60px;line-height:1.15;margin-bottom:22px}
.sit{font-style:italic;font-size:33px;line-height:1.45;color:#7A6455;max-width:820px}
.dark .sit{color:#CDBBA6}
.orn{color:#A87B4F;font-size:30px;margin:38px 0 34px;letter-spacing:18px}
.dark .orn{color:#D6AA70}
.ar{font-family:'Amiri',serif;font-weight:700;font-size:70px;line-height:1.85;direction:rtl;color:#2E211A}
.ar.long{font-size:54px}
.dark .ar{color:#E9C48E;font-size:78px}
.ok{font-style:italic;font-size:29px;line-height:1.45;color:#8A7262;margin-top:22px;max-width:840px}
.dark .ok{color:#BFA88F}
.meal{font-size:37px;line-height:1.45;margin-top:28px;max-width:860px}
.ref{font-size:25px;letter-spacing:2px;color:#A87B4F;margin-top:14px}
.dark .ref{color:#D6AA70}
.end{font-weight:600;font-size:38px;color:#A87B4F;margin-top:46px;padding-top:30px;border-top:1px solid rgba(168,123,79,.4)}
.big{font-weight:600;font-size:104px;line-height:1.1}
.sub{font-size:44px;line-height:1.4;margin-top:40px;color:#E9DCC9}
.save{font-style:italic;font-size:30px;margin-top:60px;color:#D6AA70}
.wm{position:absolute;font-family:'Amiri',serif;font-size:420px;color:rgba(214,170,112,.06);top:50%;left:50%;transform:translate(-50%,-55%)}
.cl{font-size:52px;line-height:1.45;font-weight:600}
.cl2{font-size:40px;line-height:1.5;margin-top:44px;color:#E9DCC9}
.q{font-style:italic;font-size:46px;margin-top:70px;color:#E9C48E}
"""

def page(i, s):
    num = f"{i+1} / {N}"
    top = f'<div class="top"><span>Hz. Musa\'nın duaları</span><span>{num}</span></div>'
    foot = '<div class="foot">@zzeriyaca</div>'
    arrow = '<div class="arrow">→</div>' if i < N - 1 else ''
    k = s.get("kind")
    if k == "cover":
        body = f'''<div class="s dark"><div class="wm">موسى</div>
          <div class="big">Hz. Musa da<br>korktu.</div>
          <div class="sub">İşte sıkıntı anında<br>yapıştığı dualar</div>
          <div class="orn">✦ ✦ ✦</div>
          <div class="save">Kaydet, lazım olacak.</div>{foot}{arrow}</div>'''
    elif k == "close":
        body = f'''<div class="s dark">{top}
          <div class="cl">Musa korktu,<br>ama korkusuyla<br>Allah'a koştu.</div>
          <div class="orn">✦ ✦ ✦</div>
          <div class="cl2">Kaygı seni Rabbine götürüyorsa,<br>kaybetmiyorsun.</div>
          <div class="q">Bugün hangisi senin duan?</div>{foot}</div>'''
    else:
        dark = " dark" if k == "answer" else ""
        end = f'<div class="end">{s["end"]}</div>' if s.get("end") else ""
        long = " long" if s.get("long") else ""
        body = f'''<div class="s{dark}">{top}
          <h2>{s["title"]}</h2><div class="sit">{s["sit"]}</div>
          <div class="orn">✦</div>
          <div class="ar{long}">{s["ar"]}</div>
          <div class="ok">{s["ok"]}</div>
          <div class="meal">“{s["meal"]}”</div>
          <div class="ref">{s["ref"]}</div>{end}{foot}{arrow}</div>'''
    return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'

for i, s in enumerate(SLIDES):
    open(os.path.join(D, f"slide{i+1}.html"), "w").write(page(i, s))
print("html", N)
