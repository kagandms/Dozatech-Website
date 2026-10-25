# DOZATECH Growth, SEO ve CRO Yol Haritası

> Bu dosya, DOZATECH web sitesinin organik görünürlük, CTR, site içi tıklanma, etkileşim ve nitelikli B2B lead performansını günlük takip ederek geliştirmek için tek çalışma kaynağıdır.

## 1. Durum ve kapsam

- **Plan tarihi:** 2026-09-06
- **Mevcut durum:** Teknik temel tamamlandı; büyüme sprinti başlatıldı.
- **Hedef kitle:** Restoranlar, oteller, toplu yemek işletmeleri, profesyonel mutfaklar ve teknik satın alma karar vericileri.
- **Birinci ticari öncelik:** İstanbul’daki restoran, otel ve kafelere düzenli kimyasal tedariki; tekrar sipariş ve sürekli gelir.
- **İkinci ticari öncelik:** Dozaj pompası satışı ve montajı.
- **Diğer faaliyetler:** Dozaj pompası bakım/onarımı ve endüstriyel bulaşık makinesi satışı. Bulaşık makinesi tamiri/onarımı sunulmaz.
- **Ana ticari hedef:** Kimyasal tedariki için nitelikli tekrar sipariş ilişkileri kurmak; pompa satışı ve montajını ikinci öncelik olarak büyütmek.
- **Birincil karar metriği:** 1.000 organik gösterim başına nitelikli teklif talebi.

Bu proje yüksek hacimli, düşük kaliteli trafik yerine daha az fakat ticari niyeti yüksek ziyaretçi üretmeyi hedefler. Her içerik, tasarım ve dağıtım kararı bu hedefe göre değerlendirilecektir.

### 1.1 İşletme bağlamı ve güncel erişim durumu — 2026-10-25

Detaylı hizmet kapsamı, güçlü yönler ve teyit edilmemiş bilgiler için [`business-context.md`](business-context.md) geçerlidir. Kimyasal kategori ve tekrar sipariş akışı birinci; dozaj pompası satışı/montajı ikinci önceliktir. Tedarikçi firmaların müşterilerine ücretli pompa montajı, bakım ve onarım hizmeti de sunulur. Makine satışı bu pompa hizmetlerinden ayrı tutulur; bulaşık makinesi tamiri/onarımı sunulmaz.

| Kontrol | Güncel durum |
| --- | --- |
| Google İşletme Profili | Mevcut değil (işletme sahibinin bildirdiği bilgi) |
| Search Console ve GA4 hesap erişimi | Bu çalışma için henüz doğrulanmadı |
| GA4 ölçüm kimliği | Kaynakta `G-QBSSV93GCS` bulunuyor; bu, veri alımını kanıtlamaz |
| Formspree alıcıya teslim | Hesap erişimi olmadan doğrulanamaz; gerçek mesaj gönderilmedi |
| Gerçek kurulum fotoğrafı/video | Var olduğu bildirildi; bu çalışma için henüz sağlanmadı |

2026-09-06 tarihli GA4 ölçümleri ve kontrollü event kaydı aşağıdaki tarihli kayıtlarda korunmuştur. Bunlar tarihsel kanıttır; güncel hesap erişimi veya bugünkü veri alımı olarak sunulmayacaktır.

### 1.2 Yayın zinciri ve barındırma rolleri — 2026-10-25

- **GitHub Pages:** Depoda `CNAME` ve Pages deployment kaydı bulunuyor; kamuya açık kayıt, 2026-09-16 tarihli `ea103eeecbd9db3d7c6f1f2c1474cada0f2cd68e` commit’i için başarıyla tamamlanan bir Pages deployment gösteriyor. Güncel özel alan adının Pages’ten sunulduğunu gösteren bir kanıt yok.
- **Vercel production:** Canlı yanıtlarda Vercel sunucu başlıkları gözlendi. GitHub deployment kaydı 2026-09-16 tarihinde aynı commit için bir Vercel production deployment ve `dozatech-website-btc2n60gx-kagans-projects-ce31d7ff.vercel.app` deployment adresi gösteriyor. Bu kayıt bugünkü özel alan adının hangi SHA’dan sunulduğunu kanıtlamaz.
- **Vercel Preview bağlantısı:** PR #1’in Vercel bot kontrolü bu depoyu `tennyson10/dozatech` projesine bağladı. Vercel check, `7ad3aab7369cdf8296239f2c1f0a6ae3a47fdc05` commit’i için başarılı oldu ve `https://dozatech-git-codex-dozatech-seo-foundation-tennyson10.vercel.app` Preview adresi üretti. Preview HTTP istekleri içerik yerine Vercel SSO girişine yönlendiğinden sayfa içeriği bu oturumda doğrulanamadı.
- **Vercel production ayarı:** Preview bağlantısı repository–proje entegrasyonunu doğrular; production dalının `главно` olduğunu veya bugünkü özel alan adının hangi SHA’dan sunulduğunu doğrulamaz. Yeni/önceki Vercel projesinin tarihsel ayrımı da panel erişimi olmadan doğrulanamadı.
- **Eski Vercel projesi:** Kimliği ve durumu erişilebilen kanıtla belirlenemedi. Hiçbir proje silinmedi veya değiştirilmedi.

Bu bölümdeki yayın kayıtları geçmiş kamuya açık GitHub deployment metaverisine dayanır; canlı HTTP, Vercel hesap/proje kimliğini ya da çalışan commit’i tek başına göstermez.

Canlı HTTP kontrolünde `https://dozatech.com.tr/` kalıcı olarak `https://www.dozatech.com.tr/` adresine yönleniyor; `http://dozatech.com.tr/` önce HTTPS apex’e, sonra www’ye giderek iki yönlendirme yapıyor. `http://www` doğrudan HTTPS www’ye çıkıyor. Path ve query parametreleri örnek istekte korunuyor. Canlı canonical, `og:url`, JSON-LD ve sitemap ise www’siz apex kullanıyor; repo düzeltmesi yayınlanmadan önce Vercel proje panelindeki mevcut www-primary davranışıyla döngü riski giderilmelidir.

Repo hedefi `https://dozatech.com.tr` olacak. Üretim panelinde apex domain production domain/primary olarak, www ise apex’e yönlenen domain olarak ayarlanmalıdır. Bu panel değişikliği bu çalışma kapsamında yapılmadı. Repo redirect kuralı yalnızca www hostundan apex’e kalıcı yönlendirme hazırlar; HTTP→HTTPS davranışı Vercel domain/TLS katmanında doğrulanmalıdır. Geçmiş Pages workflow/deployment sonucu, `DOZATECH Web CI` build ve test kontrolü yerine geçmez.

Repo build ayarları `npm run build` komutunu ve `dist/` çıktı dizinini kullanır; Python build betiği Tailwind CSS `3.4.17` CLI’ını çalıştırır. GitHub CI, Node.js `20.x` ve Python `3.11` kullanır. Vercel install komutu bu dalda lockfile tabanlı `npm ci` olarak ayarlanmıştır. Bunlar repo/CI yapılandırmasıdır; yeni Vercel projesinin hesap ayarı veya deployment sonucu olarak yorumlanmamalıdır.

Kontrol edilen temel canlı rotalar `/urunler`, ürün kategorileri, `/cozumler`, sitemap’te listelenen çözüm sayfaları ve ürün detayları için `200`; rastgele olmayan route örneği `/__no-such-route__` için gerçek `404` döndü. Eski `/urunler.html` adresi temiz `/urunler` rotasına kalıcı yönleniyor. Kısa `/cozumler/restoranlar` ve `/cozumler/oteller` yolları mevcut rota listesinde değil ve `404` dönüyor; bunlar sitemap’teki tam slug’larla karıştırılmamalıdır.

## 2. Hedef hunisi

```text
Google gösterimi
    -> Arama sonucu tıklaması / CTR
        -> İlgili landing page girişi
            -> Ürün/çözüm inceleme ve site içi tıklama
                -> WhatsApp / telefon / form etkileşimi
                    -> Nitelikli lead
                        -> Teklif
                            -> Satış
```

## 3. KPI sözlüğü

| Katman | KPI | Tanım | Kaynak | Takip sıklığı |
| --- | --- | --- | --- | --- |
| Stratejik | Nitelikli lead | İhtiyacı, işletme tipi veya makine bilgisi anlaşılabilen talep | CRM/manuel kayıt | Haftalık |
| Stratejik | Lead oranı | Nitelikli lead / organik oturum | GA4 + satış kaydı | Haftalık |
| Arama | Gösterim | Site URL’sinin Google sonuçlarında görünmesi | Search Console | Haftalık |
| Arama | CTR | Tıklama / gösterim | Search Console | Haftalık |
| Arama | Organik tıklama | Google’dan siteye gelen tıklama | Search Console | Haftalık |
| Arama | Sorgu kapsamı | Görünürlük kazanılan markasız ticari sorgu sayısı | Search Console | Haftalık |
| Site | Landing page girişi | Oturumun başladığı sayfa | GA4 | Haftalık |
| Site | Etkileşimli oturum | GA4 engaged session tanımını sağlayan oturum | GA4 | Haftalık |
| Site | CTA tıklama oranı | CTA tıklaması / ilgili sayfa oturumu | GA4 | Haftalık |
| Site | Ürün/çözüm geçiş oranı | İlgili detay sayfasına geçen kullanıcı oranı | GA4 | Haftalık |
| Dönüşüm | WhatsApp tıklaması | `whatsapp_click` olayı | GA4 | Günlük/haftalık |
| Dönüşüm | Telefon tıklaması | `phone_click` olayı | GA4 | Günlük/haftalık |
| Dönüşüm | Form tamamlama | `form_success` olayı | GA4 + Formspree | Günlük/haftalık |
| Ticari | Teklif dönüş oranı | Teklife dönen nitelikli lead oranı | Satış kaydı | Haftalık |

CTR ve gösterim, sayfa ve sorgu kırılımında değerlendirilmelidir. Site genelindeki tek bir ortalama, hangi sayfanın veya sorgunun sorunlu olduğunu gizleyebilir.

`whatsapp_click`, `phone_click` ve genel CTA event’leri iletişim niyeti/tıklama göstergesidir; nitelikli müşteri talebi sayılmaz. Nitelikli lead, gerçek talep ve satış takibiyle teyit edilmelidir. Formdaki `form_success` yalnızca istemci tarafındaki başarılı HTTP yanıtını gösterir; Formspree alıcıya teslimi hesap erişimiyle doğrulanmadan tamamlanmış lead olarak raporlanmayacaktır.

## 3.1 Baseline veri kayıt defteri

Bu bölüm, 2026-09-06 tarihinde alınan Search Console ve GA4 export’larının karşılaştırılabilir başlangıç kaydıdır. Search Console tıklama/gösterim verisini, GA4 ise oturum ve site içi davranış verisini ölçer; aynı metrik olarak yorumlanmayacaktır.

### Dönem özeti

| Kaynak | Dönem | Ana değerler |
| --- | --- | --- |
| Search Console | 28 gün | 6 tıklama / 188 gösterim / %3,19 CTR |
| Search Console | 90 gün | 23 tıklama / 372 gösterim / %6,18 CTR |
| GA4 | 28 gün, 2026-08-09–2026-09-05 | 27 oturum / 8 etkileşimli oturum / %29,63 etkileşim oranı / 123 etkinlik |
| GA4 | 90 gün, 2026-06-08–2026-09-05 | 88 oturum / 45 etkileşimli oturum / yaklaşık %51,14 etkileşim oranı / 774 etkinlik |

GA4 90 günlük oturum ve etkinlik toplamları kanal ve sayfa export satırlarından uzlaştırılmıştır. GA4 sayfa raporunda 90 günlük toplam 287 görüntüleme, 28 günlük raporda 33 görüntüleme vardır.

### GA4 trafik kaynağı/aracısı

#### 28 gün — 2026-08-09–2026-09-05

| Kaynak/aracı | Oturum | Etkileşimli oturum | Etkileşim oranı | Ort. etkileşim süresi | Etkinlik |
| --- | ---: | ---: | ---: | ---: | ---: |
| `(direct) / (none)` | 15 | 1 | %6,67 | 1,8 sn | 58 |
| `google / organic` | 9 | 5 | %55,56 | 26,4 sn | 52 |
| `chatgpt.com / ai-assistant` | 2 | 2 | %100 | 20,5 sn | 10 |
| `t.co / referral` | 1 | 0 | %0 | 0 sn | 3 |

#### 90 gün — 2026-06-08–2026-09-05

| Kanal | Oturum | Etkileşimli oturum | Etkileşim oranı | Ort. etkileşim süresi | Etkinlik |
| --- | ---: | ---: | ---: | ---: | ---: |
| Direct | 42 | 12 | %28,57 | 26,3 sn | 342 |
| Organic Search | 41 | 30 | %73,17 | 59,1 sn | 409 |
| Organic Social | 3 | 1 | %33,33 | 3 sn | 13 |
| AI Assistant | 2 | 2 | %100 | 20,5 sn | 10 |

### GA4 sayfalar ve ekranlar

#### 28 gün

| Sayfa | Görüntüleme | Etkin kullanıcı | Kullanıcı başına ort. süre | Etkinlik |
| --- | ---: | ---: | ---: | ---: |
| `/` | 16 | 14 | 5,6 sn | 60 |
| `/urunler/dozaj-pompalari` | 9 | 9 | 19,4 sn | 34 |
| `/urunler` | 5 | 4 | 11,3 sn | 17 |
| `/urunler/kimyasallar` | 2 | 2 | 3 sn | 7 |
| `/urunler/bulasik-makineleri` | 1 | 1 | 1 sn | 5 |

#### 90 gün — ham URL satırları

| Sayfa | Görüntüleme | Etkin kullanıcı | Kullanıcı başına ort. süre | Etkinlik |
| --- | ---: | ---: | ---: | ---: |
| `/` | 136 | 42 | 31,9 sn | 362 |
| `/urunler/dozaj-pompalari` | 51 | 22 | 37,5 sn | 150 |
| `/urunler` | 42 | 15 | 65 sn | 117 |
| `/urunler/` | 23 | 1 | 77 sn | 46 |
| `/urunler/dozaj-pompalari/` | 12 | 1 | 193 sn | 33 |
| `/urunler/kimyasallar/` | 9 | 1 | 63 sn | 21 |
| `/urunler/kimyasallar` | 7 | 5 | 10,4 sn | 22 |
| `/urunler/bulasik-makineleri` | 4 | 3 | 14 sn | 16 |
| `/urunler/bulasik-makineleri/` | 3 | 1 | 10 sn | 7 |

### GA4 giriş sayfası — 28 gün

| Giriş sayfası | Oturum | Etkin kullanıcı | Yeni kullanıcı | Ort. oturum etkileşimi |
| --- | ---: | ---: | ---: | ---: |
| `/` | 14 | 14 | 14 | 8,4 sn |
| `/urunler/dozaj-pompalari` | 8 | 8 | 8 | 14,4 sn |
| `/urunler` | 2 | 2 | 2 | 35,5 sn |
| `(not set)` | 1 | 1 | 0 | 0 sn |
| `/urunler/bulasik-makineleri` | 1 | 1 | 1 | 1 sn |
| `/urunler/kimyasallar` | 1 | 1 | 1 | 1 sn |

### Baseline veri kalitesi ve yorumlama kuralları

- 28 günlük GA4 kanal raporu 27 oturumla, giriş sayfası raporu da 27 oturumla uzlaşır; 28 günlük sayfa raporu 33 görüntüleme ve 123 etkinlikle önceki event export’uyla uzlaşır.
- Son 28 günde 27 oturum, 90 günlük toplamın 88 oturumuna yakındır. Önceki 62 gün için 61 oturum kaldığı için günlük oturum hacmi yaklaşık sabittir; düşüş esas olarak sayfa/oturum ve etkileşim kalitesindedir.
- Sayfa/oturum, son 28 günde `33 / 27 = 1,22`; önceki 62 günde `(287 - 33) / (88 - 27) = 4,16` olarak hesaplanır. Bu türetilmiş karşılaştırma, doğrudan GA4 hazır KPI’ı değildir.
- `/urunler`, `/urunler/dozaj-pompalari`, `/urunler/kimyasallar` ve `/urunler/bulasik-makineleri` URL’lerinin slash’li/slash’siz varyantları ayrı ölçülmektedir. Tek URL standardı sağlanmadan sayfa, giriş ve çıkış karşılaştırmaları bölünmüş kabul edilecektir.
- 28 günlük trafik kaynağı raporunda önemli faaliyet sayısı tüm kaynaklarda `0`, toplam gelir `0`’dır. Bu değerler lead yokluğunu tek başına kanıtlamaz; event’lerin key event olarak işaretlenmesi ve canlı test gerekir.
- GA4’teki `Etkinlikler` raporunda 28 günlük temel event’ler `page_view: 33`, `session_start: 27`, `first_visit: 26`, `user_engagement: 24`, `scroll: 12`, `click: 1` olarak kaydedilmiştir. Bu `click` değeri WhatsApp/telefon/CTA dönüşümü olarak yorumlanmayacaktır.

### GA4 event doğrulama snapshot’ı — deployment öncesi 7 gün

| Dönem | Event | Etkinlik sayısı | Toplam kullanıcı |
| --- | --- | ---: | ---: |
| 2026-08-30–2026-09-05 | `first_visit` | 2 | 2 |
| 2026-08-30–2026-09-05 | `page_view` | 2 | 2 |
| 2026-08-30–2026-09-05 | `session_start` | 2 | 2 |
| 2026-08-30–2026-09-05 | `user_engagement` | 1 | 1 |

Bu 7 günlük export’ta `whatsapp_click`, `phone_click`, `cta_click`, `form_start`, `form_submit`, `form_success` ve `form_error` görünmemektedir. Rapor dönemi 2026-09-06 tarihli event altyapısı deployment’ından önce bittiği için bu sonuç özel event’lerin çalışmadığını kanıtlamaz.

### GA4 canlı event doğrulaması — 2026-09-06

Kontrollü production testinde iki cihazdan siteye giriş ve WhatsApp CTA tıklaması yapıldı. GA4 Gerçek zamanlı genel bakış ekranında:

- Son 30 dakikada aktif kullanıcı: `2`
- Son 5 dakikada aktif kullanıcı: `2`
- `whatsapp_click`: `2`
- `cta_click`: `2`
- `page_view`: `2`
- `session_start`: `2`
- `first_visit`: `1`

Sonuç: GA4 loader’ı ve özel WhatsApp/CTA event’leri production’da çalışıyor. Gerçek zamanlı kartta önemli faaliyet verisi henüz yok; ticari event’ler key event olarak işaretlenmemiştir. `phone_click` ve form event’leri ayrı kontrollü testle doğrulanacaktır.

## 4. Teknik temel durumu

Bu bölüm büyüme çalışmasının ön koşulu olan teknik yayın işlerini takip eder.

- [x] Canonical URL, sitemap, robots.txt ve eski URL redirect yapısı
- [x] Ürün ve çözüm sayfalarının public route yapısı
- [x] Title, description, Open Graph, Twitter ve breadcrumb üretimi
- [x] Ürün/çözüm sayfaları için temel yapılandırılmış veri
- [x] GA4 loader ve temel event altyapısı
- [x] WhatsApp, telefon, CTA ve form event’leri
- [x] Form AJAX akışı, hata durumu ve honeypot alanı
- [x] Mobil menü ve temel erişilebilirlik durumları
- [x] CSP, HSTS ve güvenlik response header’ları
- [x] Görsel boyutları, async decoding ve asset cache politikası
- [x] CI build ve route/SEO/output doğrulama kontrolleri
- [x] Vercel production branch’i `главно` üzerinden canlı deployment
- [ ] GA4’te gerçek kullanıcı event’lerinin Realtime/DebugView ile doğrulanması
- [ ] Search Console sitemap gönderimi ve URL Inspection kontrolü
- [ ] Formspree’ye gerçek, izinli test talebi gönderimi
- [ ] PageSpeed/CrUX field data baseline’ı

Son dört madde yayını engelleyen teknik arıza değildir; büyüme ölçümünün güvenilirliğini artıran operasyonel kontrollerdir.

## 5. Dört fazlı 90 günlük plan

### Faz 1 — Ölçüm ve baseline

**Takvim:** Gün 1–7

Amaç, tahmin yerine gerçek Search Console, GA4 ve satış verisiyle karar verebilecek bir başlangıç tabanı oluşturmaktır.

Teslimatlar:

- 28 günlük ve 90 günlük Search Console export’u
- Sorgu–sayfa–niyet eşlemesi
- Markalı/markasız arama ayrımı
- Landing page giriş ve yüksek çıkış raporu
- CTA, WhatsApp, telefon ve form funnel’ı
- Nitelikli lead tanımının satış tarafıyla kesinleştirilmesi
- GA4’te `whatsapp_click`, `phone_click` ve `form_success` olaylarının key event olarak işaretlenmesi
- Haftalık KPI dashboard şablonu

Kabul kriteri: Hangi sayfanın gösterim aldığı, hangi sorguda CTR kaybettiği ve hangi sayfanın lead ürettiği tek raporda görülebilir olmalıdır.

### Faz 2 — Arama talebi, içerik mimarisi ve CTR

**Takvim:** Gün 8–21

Öncelik, mevcut ticari sayfaları arama niyetiyle daha güçlü eşleştirmektir.

Öncelikli sorgu kümeleri:

- İstanbul restoranları, otelleri ve kafeleri için endüstriyel bulaşık makinesi deterjanı ve parlatıcısı tedariki
- Endüstriyel bulaşık makinesi kimyasalları ve düzenli tedarik
- Bulaşık makinesi kireç sökücü ve yağ çözücü kimyasallar
- Kimyasal ve pompa tedarikçilerinin müşterileri için dozaj pompası montajı/bakımı/onarımı
- Restoran, otel ve kafelerde dozaj pompası montajı ve pompa modelleri
- bulaşık makinesi dozaj pompası
- deterjan dozaj pompası
- parlatıcı dozaj pompası
- Seko PR4 deterjan pompası
- Atiker APM 0300 pompa
- restoran bulaşık yıkama sistemi
- otel mutfağı hijyen çözümleri
- toplu yemek dozaj sistemi
- bulaşık makinesi kireç sökücü

Öncelikli title testleri:

- Ana sayfa: `İstanbul Endüstriyel Bulaşık Makinesi Kimyasalları | DOZATECH`
- Kimyasal kategorisi: `Endüstriyel Bulaşık Makinesi Deterjanı ve Parlatıcısı | DOZATECH`
- Dozaj kategorisi: `Bulaşık Makinesi Dozaj Pompaları | Seko ve Atiker Modelleri | DOZATECH`
- Restoran çözümü: `Restoranlar İçin Bulaşık Yıkama ve Dozaj Sistemi | DOZATECH`
- Seko ürün sayfası: `Seko PR4 Deterjan Pompası: Teknik Özellikler ve Teklif | DOZATECH`

Teslimatlar:

- Sayfa başına birincil sorgu ve ikincil sorgu seti
- Ürün, çözüm ve rehber silo haritası
- Sayfa bazlı title/description test listesi
- Dahili bağlantı matrisi
- Eksik kategori ve ürün sayfaları için içerik brief’leri

Kabul kriteri: Her ticari sorgu bir hedef sayfaya, her hedef sayfa da ölçülebilir bir CTA’ya bağlı olmalıdır.

### Faz 3 — Site içi tıklanma, etkileşim ve çıkış optimizasyonu

**Takvim:** Gün 22–42

Amaç, siteye gelen ziyaretçinin doğru ürün/çözüm sayfasına ilerlemesini ve iletişim kurmasını sağlamaktır.

Uygulama alanları:

- Ana sayfa hero metnini hedef sektör ve probleme göre netleştirme
- Genel `Teklif Alın` CTA’larını bağlama göre farklılaştırma
- Ürün karşılaştırma tablosu
- Kimyasal tedariki ve tekrar sipariş için net teklif akışı
- “Hangi kimyasal veya pompa hizmeti?” seçim akışı
- Her sayfada üst, orta ve alt CTA konumlandırması
- Ürün detayından ilgili çözüm sayfasına geçiş
- Çözüm sayfasından ilgili ürün kategorisine geçiş
- Kısa B2B teklif formu: işletme türü, kimyasal/pompa ihtiyacı, kullanım sıklığı ve şehir
- Mobil yapışkan WhatsApp/telefon CTA’sı
- Yüksek çıkış veren sayfalarda SSS, sonraki adım ve kanıt bölümü
- Gerçek kurulum fotoğrafları ve teknik uygulama örnekleri

Kabul kriteri: Her yüksek girişli sayfa kullanıcıyı en az bir mantıklı sonraki adıma yönlendirmeli; CTA tıklaması ve lead kalitesi birlikte izlenmelidir.

### Faz 4 — İçerik, yerel görünürlük ve ölçekleme

**Takvim:** Gün 43–90

Amaç, markasız gösterimi ve güven sinyallerini sürdürülebilir biçimde artırmaktır.

İlk rehber içerikleri:

1. Bulaşık Makinesi İçin Dozaj Pompası Nasıl Seçilir?
2. Deterjan ve Parlatıcı Dozajı Nasıl Ayarlanır?
3. Seko PR4 ile Atiker APM 0300 Karşılaştırması
4. Restoranlar İçin Bulaşık Yıkama Sistemi Seçim Rehberi
5. Otel Mutfağında Kimyasal ve Dozaj Sistemi Planlama
6. Endüstriyel Bulaşık Makinesinde Kireç Oluşumu Nasıl Azaltılır?

Dağıtım kanalları:

- Google Business Profile oluşturma ve doğrulama (işletme bilgileri teyit edildikten sonra)
- LinkedIn teknik içerikleri
- YouTube/Shorts montaj ve ürün kullanım videoları
- WhatsApp’a UTM’li kampanya bağlantıları
- Tedarikçi ve sektör sitelerinde gerçek uzmanlık/uygulama içerikleri
- Müşteri izinli vaka çalışmaları

Kabul kriteri: Her içerik en az bir ticari kategori sayfasına, bir ürün sayfasına ve bir çözüm sayfasına bağlanmalı; dağıtım linkleri kaynak/medium/campaign ile ölçülmelidir.

## 6. Sprint 1 — Gün gün uygulama planı

### Gün 1 — Ölçüm envanteri ve erişim kontrolü

- [x] Büyüme planını bu dosyaya kaydet
- [x] GA4 ölçüm ID’sini ve mevcut event listesini doğrula
- [x] Formspree endpoint’inin yapılandırılmış olduğunu doğrula
- [x] Teknik yayının production’da olduğunu doğrula
- [x] Search Console export dosyalarını al ve property verisini doğrula
- [x] GA4 property erişimini doğrula
- [x] GSC export formatını kesinleştir
- [x] GA4 export formatını kesinleştir

Gün 1 bulgusu: Site tarafında GA4 ID `G-QBSSV93GCS` ve temel event’ler mevcut. Search Console verisi Gün 2’de, GA4 hesap erişimi ve ilk export’lar Gün 3–5’te sağlandı. Özel dönüşüm event’lerinin canlı doğrulaması henüz tamamlanmadı.

### Gün 2 — Search Console baseline

- [x] Son 28 gün ve 90 gün karşılaştırmasını çıkar
- [x] Sayfa bazında gösterim, tıklama ve CTR tablosu oluştur
- [x] Markalı ve markasız sorguları ayır
- [x] Cihaz ve ülke kırılımını ekle
- [x] İlk fırsat sorgularını seç

Çıktı: `search-console-baseline.csv` veya eşdeğer rapor.

Gün 2 baseline bulguları:

- Search Console Chart toplamı: 28 gün `6 tıklama / 188 gösterim / %3,19 CTR`; 90 gün `23 tıklama / 372 gösterim / %6,18 CTR`.
- `/urunler/dozaj-pompalari`: 28 gün `157 gösterim / 3 tıklama / %1,91 CTR / 24,87 pozisyon`; 90 gün `304 / 11 / %3,62 / 30,78`. En büyük görünürlük fırsatı bu sayfadır.
- Ana sayfa: 28 gün `%12 CTR`, 90 gün `%12 CTR`; 90 günlük ortalama pozisyon `5,76`. Snippet ve marka niyeti güçlüdür.
- `/urunler`: 90 gün `66 gösterim / 5 tıklama / %7,58 CTR / 14,73 pozisyon`; son 28 günde `29 gösterim / 0 tıklama / 22,45 pozisyon`. Yakın dönem düşüşü izlenecektir.
- `/urunler/bulasik-makineleri`: 90 gün `33 gösterim / 1 tıklama / %3,03 CTR / 9,55 pozisyon`; pozisyon iyi, CTR geliştirme adayıdır.
- Cihaz farkı: 28 günde mobil `%5,49 CTR / 9,6 pozisyon`; masaüstü `%1,03 CTR / 36,86 pozisyon`. 90 günde mobil `%11,04 CTR / 11 pozisyon`; masaüstü `%2,75 CTR / 39,84 pozisyon`. Masaüstü görünürlüğü ve sıralaması öncelikli inceleme alanıdır.
- 90 günlük sorgularda `dozaj pompası` `54 gösterim / 0 tıklama / 59,2 pozisyon`, `dozaj sistemleri` `15 / 0 / 77,07`, `kimyasal dozaj pompası` `10 / 0 / 86,3` değerindedir. Bunlar içerik ve sıralama fırsatıdır.
- 90 günlük marka sorgusu `dozatech`: `37 gösterim / 16 tıklama / %43,24 CTR / 1,86 pozisyon`. Marka bilinirliği var; markasız talep büyütülmelidir.
- Türkiye verisi baskındır: 28 günde `173 gösterim / 6 tıklama`, 90 günde `328 / 23`. Öncelik Türkiye ve Türkçe ticari sorgular olmalıdır.

Not: Search Console boyut tablolarındaki toplamlar Chart toplamıyla birebir eşleşmeyebilir; karar için dönem toplamında Chart, fırsat tespitinde Pages ve Queries kullanılacaktır.

### Gün 3 — GA4 funnel baseline

- [x] Landing page bazında oturum ve engagement oranını çıkar
- [ ] `cta_click` olaylarını sayfa ve CTA konumuna göre ayır
- [ ] WhatsApp, telefon ve form event’lerini karşılaştır
- [ ] Form start → submit → success kırılımını kontrol et
- [ ] Event parametrelerinde sayfa grubu ve CTA konumunu doğrula

Çıktı: `ga4-funnel-baseline.csv` veya eşdeğer rapor.

### Gün 4 — Sorgu–sayfa–niyet haritası

- [ ] Her ticari sorguyu tek bir hedef URL ile eşleştir
- [ ] Aynı sorguya rekabet eden sayfaları belirle
- [ ] Eksik ürün, sektör ve problem sayfalarını listele
- [ ] Her sayfa için birincil CTA’yı tanımla

Çıktı: Sorgu–sayfa–niyet–CTA matrisi.

### Gün 5 — Landing ve çıkış analizi

- [x] En fazla giriş alan 10 sayfayı listele
- [ ] En yüksek çıkış oranına sahip ticari sayfaları listele
- [ ] İlk ekran mesajı, güven unsuru ve CTA eksiklerini not et
- [ ] Mobil ve masaüstü farklarını karşılaştır

Çıktı: Önceliklendirilmiş CRO sorun listesi.

Not: GA4 `Açılış sayfası` export’u giriş sayfasını gösterir; bu export’ta çıkış sayfası ve cihaz kırılımı bulunmadığı için ilgili maddeler beklemededir.

### Gün 6 — Mesaj ve teklif matrisi

- [ ] Restoran, otel ve toplu yemek için ayrı vaatleri yaz
- [ ] Ürün, sektör ve problem bazlı CTA metinlerini seç
- [ ] Kanıtlanması gereken iddiaları ayır
- [ ] Gerçek referans, fotoğraf, teknik doküman ve vaka çalışması kaynaklarını listele

Çıktı: Sayfa başına headline–proof–CTA brief’i.

### Gün 7 — Sprint değerlendirmesi

- [ ] Baseline raporlarını tamamla
- [ ] En yüksek etkili 5 değişikliği seç
- [ ] Sonraki sprint için kabul kriterlerini yaz
- [ ] Önce/sonra karşılaştırma tarihini kilitle
- [ ] Günlük kayıt ve karar günlüğünü güncelle

Çıktı: Sprint 1 raporu ve Sprint 2 backlog’u.

## 7. Önceliklendirme ve karar kuralları

Her öneri aşağıdaki puanlarla değerlendirilecektir:

```text
Öncelik = Etki x Güven x Uygulama kolaylığı
```

- **P0:** Ölçümü veya lead akışını bozan konu
- **P1:** Ticari sayfalarda yüksek olası etki
- **P2:** İçerik, otorite ve uzun vadeli görünürlük
- **P3:** Görsel veya düşük etkili iyileştirmeler

Bir değişiklik şu koşullarda korunur:

- CTR veya tıklanma artışı gözlenir,
- nitelikli lead oranı düşmez,
- form/WhatsApp kalite sinyalleri bozulmaz,
- teknik regresyon oluşmaz.

Düşük trafik nedeniyle klasik A/B testi için yeterli örneklem oluşmazsa, değişiklikler zaman kontrollü önce/sonra karşılaştırmasıyla değerlendirilecektir. SEO title değişiklikleri Search Console’da yeniden tarama ve veri birikimi için zaman gerektirir.

## 8. Günlük takip formatı

Her çalışma gününün sonunda bu dosyaya veya ilgili rapora şu kayıt eklenir:

```text
Tarih:
Sprint/Gün:
Bugünkü hedef:
Tamamlanan işler:
Kanıt/çıktı:
Bulgu:
Karar:
Bloker:
Yarının ilk işi:
```

## 9. Varsayımlar ve riskler

- Search Console ve GA4 hesap verileri paylaşılmadıkça gerçek başlangıç rakamları varsayılmayacaktır.
- CTR artışı title/description değişikliğiyle garanti edilmez; sorgu niyeti, pozisyon ve rekabet birlikte değerlendirilir.
- Yapılandırılmış veri zengin sonuç için uygunluk sağlayabilir ancak görünümü garanti etmez.
- Gerçek olmayan yorum, referans, fiyat üstünlüğü, tasarruf oranı veya performans iddiası yayınlanmayacaktır.
- “Çevre dostu”, “sıfırlar”, “garanti eder” gibi ifadeler belge veya ölçümle desteklenmiyorsa yumuşatılacaktır.
- Teknik SEO’nun tamamlanması, Google’ın yeni sayfaları hemen indeksleyeceği anlamına gelmez.

## 10. Günlük çalışma kaydı

### 2026-09-06 — Sprint 1 / Gün 1

- **Bugünkü hedef:** Planı kalıcılaştırmak ve ölçüm altyapısının mevcut durumunu doğrulamak.
- **Tamamlanan işler:** Büyüme planı dokümante edildi; GA4 ID ve event listesi doğrulandı; production deployment kontrol edildi; Formspree yapılandırması kontrol edildi.
- **Kanıt/çıktı:** GA4 ID `G-QBSSV93GCS`; mevcut event’ler `cta_click`, `whatsapp_click`, `phone_click`, `product_view`, `solution_view`, `form_start`, `form_submit`, `form_success`, `form_error`.
- **Bulgu:** Site tarafındaki ölçüm kodu hazır; gerçek Search Console ve GA4 hesap verileri bu çalışma alanında mevcut değil.
- **Karar:** Sayısal baseline uydurulmayacak; Gün 2–3 için hesap erişimi veya export bekleniyor.
- **Bloker:** Search Console 28/90 günlük export’u ve GA4 funnel verisi henüz alınmadı.
- **Yarının ilk işi:** Search Console sorgu/sayfa baseline’ını çıkarmak.

### 2026-09-06 — Sprint 1 / Gün 2

- **Bugünkü hedef:** 28 ve 90 günlük Search Console verisini karşılaştırmak.
- **Tamamlanan işler:** Chart, Pages, Queries, Countries ve Devices export’ları analiz edildi; sayfa, sorgu, cihaz ve ülke fırsatları çıkarıldı.
- **Kanıt/çıktı:** 28 günlük toplam `%3,19 CTR`; 90 günlük toplam `%6,18 CTR`. Dozaj pompası sayfası en yüksek gösterim alan ticari sayfa; masaüstü CTR ve pozisyonu mobilin belirgin biçimde gerisinde.
- **Bulgu:** Marka sorgularında performans iyi; markasız `dozaj pompası` ve ilişkili sorgularda görünürlük var fakat tıklama yok veya pozisyon çok geride.
- **Karar:** İlk optimizasyon odağı dozaj pompası kategorisi, masaüstü deneyimi ve markasız ticari sorgular olacak.
- **Bloker:** Site içi giriş, etkileşim, çıkış ve gerçek lead kalitesi için GA4 funnel verisi eksik.
- **Yarının ilk işi:** GA4 export’u veya ekran görüntüsüyle landing page ve event baseline’ını çıkarmak.

### 2026-09-06 — Sprint 1 / Gün 3–5 — GA4 baseline

- **Bugünkü hedef:** GA4’te sayfa, trafik kaynağı ve giriş sayfası verisini aynı dönem için kaydetmek.
- **Tamamlanan işler:** 28 günlük etkinlik, sayfalar ve ekranlar, trafik kaynağı/aracısı ve açılış sayfası export’ları alındı; 90 günlük sayfa ve trafik karşılaştırmasıyla birlikte baseline kayıt defterine işlendi.
- **Kanıt/çıktı:** 28 günlük GA4 `27 oturum / 8 etkileşimli oturum / %29,63 etkileşim oranı / 123 etkinlik`; girişlerin `%51,9’u` ana sayfaya, `%29,6’sı` dozaj pompası sayfasına geldi.
- **Bulgu:** `(direct) / (none)` 15 oturumla hacim lideri fakat yalnızca `%6,67` etkileşim oranına ve `1,8 sn` ortalama süreye sahip. `google / organic` 9 oturumda `%55,56` etkileşim oranı ve `26,4 sn` ortalama süre üretti.
- **Veri kalitesi bulgusu:** Aynı ürün/kategori yollarının slash’li ve slash’siz varyantları ayrı raporlanıyor. Bu, sayfa ve giriş analizi için standardizasyon işi gerektiriyor.
- **Karar:** SEO ve dozaj pompası landing page önceliği korunacak; Direct kaynağı ve düşük sayfa derinliği ayrıca incelenecek. Düşük örneklemli sayfalarda içerik kararı verilmeyecek.
- **Bloker:** Özel CTA/WhatsApp/telefon/form event’leri bu tarih aralığında görünmüyor; son deployment sonrası canlı test ve key event doğrulaması gerekiyor. Çıkış sayfası kırılımı henüz alınmadı.
- **Yarının ilk işi:** Production’da kontrollü CTA testi yapmak; ardından GA4 `Etkinlikler: Etkinlik adı` raporunu deployment sonrası dönem için kaydetmek.

### 2026-09-06 — Sprint 1 / Event export doğrulaması

- **Bugünkü hedef:** Son 7 günlük GA4 event export’u ile özel event’lerin görünürlüğünü kontrol etmek.
- **Tamamlanan işler:** `2026-08-30–2026-09-05` tarihli event export’u alındı ve baseline kayıt defterine işlendi.
- **Bulgu:** Export’ta yalnızca `first_visit: 2`, `page_view: 2`, `session_start: 2` ve `user_engagement: 1` bulunuyor; özel CTA ve form event’leri yok.
- **Karar:** Bu sonuç hata olarak sınıflandırılmayacak; export deployment’tan önceki döneme aittir. Canlı doğrulama deployment sonrası yapılacak.
- **Yarının ilk işi:** Production’da kontrollü WhatsApp/CTA tıklaması yapmak ve GA4 Gerçek Zamanlı görünümde event’i doğrulamak.

### 2026-09-06 — Sprint 1 / Production event doğrulaması

- **Bugünkü hedef:** Yeni event altyapısının canlı production’da çalıştığını kanıtlamak.
- **Tamamlanan işler:** İki cihazdan kontrollü WhatsApp CTA tıklaması yapıldı; GA4 Gerçek zamanlı genel bakış ekranı kontrol edildi.
- **Kanıt/çıktı:** Aktif kullanıcı `2`; `whatsapp_click: 2`; `cta_click: 2`; `page_view: 2`; `session_start: 2`.
- **Bulgu:** Özel event’ler production’da GA4’e ulaşıyor. Bu, önceki deployment öncesi 7 günlük export’ta event görünmemesinin tarih aralığından kaynaklandığını doğruluyor.
- **Karar:** Event altyapısı çalışıyor. Primary key event olarak `whatsapp_click`, `phone_click` ve `form_success`; ikincil mikro event olarak `cta_click` izlenecek.
- **Bloker:** `phone_click` ve form akışı henüz ayrı test edilmedi; key event tanımları henüz yapılmadı.
- **Yarının ilk işi:** GA4’te ticari event’leri key event olarak işaretlemek ve kontrollü telefon/form testlerini tamamlamak.

## 11. Değişiklik günlüğü

| Tarih | Değişiklik | Durum |
| --- | --- | --- |
| 2026-09-06 | Teknik temel tamamlandı; production `главно` deployment doğrulandı | Tamamlandı |
| 2026-09-06 | Büyüme planı, KPI sözlüğü ve 7 günlük Sprint 1 eklendi | Devam ediyor |
