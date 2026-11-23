# Zeriya

@zzeriyaca Instagram hesabı için içerik arşivi: video şablonları, seri metinleri ve görseller.

## Klasörler

### `bakara-serisi/`
"Bakara Suresi'nde kimsenin fark etmediği cümleler" serisi.

- `Bakara_Serisi_49_Bolum.pdf`: 49 bölümün tamamı, ayet sırasına göre. Her bölümde giriş cümlesi, konuşma metni, ekran yazısı ve kaynaklar var.
- `bakara.txt`: Metinlerin düzenlenebilir hali. PDF bu dosyadan üretilir.
- `build.py` ve `pdf.js`: Metin değişince PDF'i yeniden üretmek için.

`bakara.txt` dosyasındaki işaretler:

| İşaret | Anlamı |
|---|---|
| `## ` | Bölüm başlığı |
| `@ ` | Ayet numarası |
| `H: ` | Giriş cümlesi (ilk 2 saniye) |
| `> ` | Konuşma metni |
| `P: ` / `S: ` | Psikolojik / sosyolojik ders |
| `E: ` | Ekran yazısı |
| `K: ` | Kaynak |
| `N: ` | Not |

PDF'i yeniden üretmek için `bakara-serisi` klasöründe:

```
python build.py && node pdf.js
```

### `gelenek-ve-din/`
"Gelenek böyle diyor, din böyle diyor" serisi.

- `01_16_ornek.md`: Dinden sanılan 16 gelenek ve Kur'an ile sünnetteki karşılıkları.
- `02_toplu_konusma_gelenek_din.md`: Bu 16 örneği tek videoda anlatan konuşma metni (2,5–3 dk).
- `03_hayatin_dongusu.md`: Doğumdan ölüme geleneklerin tablosu (dinde var, gelenek, dinle çatışıyor).
- `04_dogumdan_olume_konusma.md`: "Doğumdan ölüme" konuşma metni, kısa ve uzun versiyon.

### `icerikler/`
Bu sohbette yazılan diğer bütün içerikler (Bakara, gelenek-ve-din ve carousel hariç, onlar kendi klasörlerinde).

- `01_yusuf_serisi.md`: Yusuf Suresi, 5 bölüm
- `02_kehf_serisi.md`: Kehf Suresi, 5 bölüm + mağara arkadaşları
- `03_hucurat_nur_meryem.md`: Hucurât, Nûr ve Meryem serileri (5'er bölüm)
- `04_ali_imran_ve_nazziat.md`: Âl-i İmrân (psikolojik/sosyolojik derslerle), Nâziât, Âdiyât
- `05_sorular_ve_kadinlar.md`: Allah'a soru soranlar, Kur'an'da böyle yazmıyor, Kur'an'daki kadınlar, peygamberlerin duyguları
- `06_1400_yil_once_bugun.md`: Toplumsal kıssalar, Kârûn, Cumartesi balıkları, Hendek sahipleri, modern putlar, güncel problemler
- `07_tefekkur_ve_ramazan.md`: Ramazan duyurusu, "Bir ömür bir akşamüstü", Buz satıcısı, Yusuf'un kapıları, gece namazı, şükür
- `08_yazarlik_ve_hesap.md`: "Eşik" denemesi, öykü, profil stratejisi, çekim notları

### `birlesik-pdf/`
Bütün içeriklerin tek PDF'te birleşmiş hali (`Zeriya_Butun_Icerikler.pdf`). Yeni içerik eklenince yeniden üretmek için bu klasörde:

```
pip install markdown
python build.py
node pdf.js
```

### `video-sablonlari/`
Videoların üstüne gelen çizimler ve animasyonlar.

- `themes.py`: Üç stil: eski kâğıt, Osmanlı tezhip, eski defter.
- `overlays.py`: İlk el çizimi stil.
- `inek_anim.py` ve `inek_render.js`: İnek bölümü için animasyonlu örnek video (Ramazan sayacı, altyazılar ve çizimlerle).
- `onizlemeler/`: Stillerin önizleme görselleri.
- `ornek/inek_ornek.mp4`: İnek bölümünün örnek editi.

Örnek videoyu yeniden üretmek için `video-sablonlari` klasöründe:

```
python inek_anim.py && node inek_render.js
```

### `carousel-hz-musa/`
"Hz. Musa'nın duaları" carousel'i (9 görsel, 1080×1350).

- `gorseller/`: Paylaşıma hazır görseller.
- `build.py` ve `shot.js`: Görselleri yeniden üretmek için.

## Gerekenler

- Python 3 ve Pillow
- Node.js ve Playwright (Chromium)
- ffmpeg

## Fontlar

Fontlar Google Fonts'tan alınmıştır (Amiri, EB Garamond, Cormorant Garamond, Caveat, Lora). Hepsi SIL Open Font License ile lisanslıdır ve serbestçe kullanılabilir.
