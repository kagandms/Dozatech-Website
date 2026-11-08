# Search Console baseline — 2026-11-06

**Kaynak türü: ekran okuması. Ham export dosyası YOK.**

Bu baseline, Google Search Console'un proje sahibinin oturumunda açık olan ekranından Claude tarafından okunarak 2026-11-08 tarihinde kaydedilmiştir. CSV veya XLSX export'u alınmadığı için sayılar yeniden indirilip karşılaştırılamaz; okuma hatası olasılığı ve tutarsızlıklar aşağıdaki "Bilinmeyenler" bölümünde işaretlenmiştir.

| Alan | Değer |
| --- | --- |
| Mülk | `sc-domain:dozatech.com.tr` |
| Rapor dönemi | 2026-08-07 → 2026-11-06 (3 ay) |
| Arama türü | Web |
| Okuma tarihi | 2026-11-08 |
| Yöntem | Ekran okuması (proje sahibinin oturumu) |

## Özet rakamlar

| Metrik | 3 ay (2026-08-07 → 2026-11-06) | Son 7 gün (31 Eki → 6 Kas) |
| --- | --- | --- |
| Tıklama | 20 | 3 |
| Gösterim | 682 | 61 |
| Ortalama CTR | %2,9 | %4,9 |
| Ortalama pozisyon | 20,1 | 20,5 |

## İlk 10 sorgu (tıklama / gösterim)

Toplam 32 sorgu var; yalnızca ilk 10'u okundu.

| Sorgu | Tıklama / gösterim |
| --- | --- |
| dozatech | 1 / 29 |
| dozajlama pompası | 1 / 13 |
| dozaj pompası | 0 / 63 |
| hızlı yıkama döngüleri için tasarlanmış kaliteli çözümler kimler yapıyor? | 0 / 32 |
| dozaj sistemleri | 0 / 16 |
| endüstriyel kireç çözücü | 0 / 13 |
| kimyasal dozaj pompası | 0 / 13 |
| dozaj pompaları | 0 / 10 |
| endüstriyel kireç sökücü | 0 / 7 |
| sanayi tipi kireç çözücü | 0 / 6 |

## İlk 10 sayfa (tıklama / gösterim)

11 sayfa var; yalnızca ilk 10'u okundu.

| Sayfa | Tıklama / gösterim |
| --- | --- |
| `/urunler/dozaj-pompalari` | 10 / 472 |
| `/` | 6 / 78 |
| `/urunler` | 2 / 105 |
| `www.dozatech.com.tr/urunler` | 1 / 28 |
| `/urunler/seko-pr4-deterjan-pompasi` | 1 / 25 |
| `/urunler/kimyasallar` | 0 / 42 |
| `www.dozatech.com.tr/urunler/bulasik-makineleri` | 0 / 35 |
| `/urunler/bulasik-makineleri` | 0 / 32 |
| `www.dozatech.com.tr/urunler/dozaj-pompalari` | 0 / 11 |
| `www.dozatech.com.tr/` | 0 / 4 |

## Sayfa indeksleme

- İndekslenen: 5 sayfa.
- İndekslenmeyen: 10 sayfa. 7 "yönlendirmeli sayfa", 1 "4xx nedeniyle engellendi", 2 "tarandı, şu an indekslenmedi".
- Hangi URL'lerin hangi kategoride olduğu okunamadı.

## Sitemap

Search Console'da gönderilmiş sitemap yok (2026-11-08 itibarıyla).

## Bulgular

1. **Tıklama hacmi düşük:** 3 ay içinde 20 tıklama ve 682 gösterim var; CTR %2,9, ortalama pozisyon 20,1.
2. **Tıklamalar tek sayfada toplanıyor:** `/urunler/dozaj-pompalari` 10 tıklama ile okunan sayfaların toplam tıklamasının yarısını aldı. Okunan 10 sayfanın tıklama toplamı 20'ye eşit; buradan 11. sayfanın tıklamasının 0 olduğu çıkıyor (türetilmiş, doğrudan okunmadı).
3. **Gösterim var, tıklama yok:** "dozaj pompası" 63 gösterim aldı, 0 tıklama. `/urunler/kimyasallar` 42 gösterim, 0 tıklama.
4. **Kimyasal niyetli sorgularda tıklama yok:** "endüstriyel kireç çözücü" (13), "endüstriyel kireç sökücü" (7), "sanayi tipi kireç çözücü" (6) gösterim aldı; hiçbiri tıklama almadı.
5. **Son 7 günde CTR yükselmiş ama örnek küçük:** %4,9 (3 tıklama / 61 gösterim). Bu tek bir haftalık gözlem; eğilim olarak yorumlanmamalı.
6. **İndeksleme ve sitemap:** 10 sayfa indekslenmiyor (çoğu yönlendirmeli), Search Console'a sitemap gönderilmemiş.

## Bilinmeyenler

- **Ham veri yok:** Sayılar ekran okumasından; tekrar indirilip doğrulanamıyor.
- **Sayfa gösterimleri toplamla uyuşmuyor:** Okunan ilk 10 sayfanın gösterim toplamı 832; genel toplam 682. Bu fark okuma hatası, filtre farkı veya Search Console'un sayfa kırılımındaki bir tutarsızlık olabilir. [SAHİBİNDEN TEYİT: export alınarak doğrulanmalı.]
- **Okunmayan veriler:** 32 sorgunun 22'si ve 11 sayfanın 1'i okunmadı.
- **İndekslenmeyen URL'ler belirsiz:** Hangi 10 sayfanın hangi durumda olduğu okunamadı.
- **`www` hostlu URL'lerin gösterimi:** `www.dozatech.com.tr` altında gösterim ve tıklama görünüyor. Repo'da www → apex 308 yönlendirmesi var (2026-11-08 itibarıyla canlı). Bu URL'lerin dönemin büyük kısmında hâlâ görünür olduğu düşünülebilir, ancak neden bu kadar gösterim aldığı doğrulanmadı.
- **Dönem sonrası değişiklikler:** 2026-11-08'de apex yönlendirme geçişi yapıldı; bu, dönem bitişinden (11-06) sonra. Dönem içinde ne zaman hangi değişikliğin yayınlandığı ayrıca kayıt altında değil.
- **Kırılımlar yok:** Cihaz, ülke ve tarih bazlı kırılımlar okunmadı.
- **GA4 ile eşleştirme yok:** GA4 hesap erişimi bu baseline'da doğrulanmadı.
- **Sitemap gönderilmemesinin nedeni:** Bilinmiyor.
