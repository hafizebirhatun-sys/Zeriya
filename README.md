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
python3 build.py && node pdf.js
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
python3 inek_anim.py && node inek_render.js
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
