# DOZATECH Growth, SEO ve CRO Yol Haritası

> Bu dosya, DOZATECH web sitesinin organik görünürlük, CTR, site içi tıklanma, etkileşim ve nitelikli B2B lead performansını günlük takip ederek geliştirmek için tek çalışma kaynağıdır.

## 1. Durum ve kapsam

- **Plan tarihi:** 2026-09-06
- **Mevcut durum:** Teknik temel tamamlandı; büyüme sprinti başlatıldı.
- **Hedef kitle:** Restoranlar, oteller, toplu yemek işletmeleri, profesyonel mutfaklar ve teknik satın alma karar vericileri.
- **Ana ticari hedef:** Ürün veya çözüm arayan ziyaretçiyi nitelikli teklif görüşmesine taşımak.
- **Birincil karar metriği:** 1.000 organik gösterim başına nitelikli teklif talebi.

Bu proje yüksek hacimli, düşük kaliteli trafik yerine daha az fakat ticari niyeti yüksek ziyaretçi üretmeyi hedefler. Her içerik, tasarım ve dağıtım kararı bu hedefe göre değerlendirilecektir.

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

- bulaşık makinesi dozaj pompası
- deterjan dozaj pompası
- parlatıcı dozaj pompası
- Seko PR4 deterjan pompası
- Atiker APM 0300 pompa
- endüstriyel bulaşık makinesi deterjanı
- restoran bulaşık yıkama sistemi
- otel mutfağı hijyen çözümleri
- toplu yemek dozaj sistemi
- bulaşık makinesi kireç sökücü

Öncelikli title testleri:

- Ana sayfa: `Endüstriyel Dozaj Pompası ve Bulaşık Makinesi Kimyasalları | DOZATECH`
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
- “Hangi makine/işletme için uygun?” seçim akışı
- Her sayfada üst, orta ve alt CTA konumlandırması
- Ürün detayından ilgili çözüm sayfasına geçiş
- Çözüm sayfasından ilgili ürün kategorisine geçiş
- Kısa B2B teklif formu: işletme türü, makine türü, şehir, ihtiyaç
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

- Google Business Profile
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
- [ ] Search Console property erişimini doğrula
- [ ] GA4 property erişimini doğrula
- [ ] GSC ve GA4 export formatını kesinleştir

Gün 1 bulgusu: Site tarafında GA4 ID `G-QBSSV93GCS` ve temel event’ler mevcut. Gerçek hesap verileri bu çalışma alanına aktarılmadığı için gösterim, CTR ve lead baseline’ı henüz sayısal olarak doldurulmadı.

### Gün 2 — Search Console baseline

- [ ] Son 28 gün ve 90 gün karşılaştırmasını çıkar
- [ ] Sayfa bazında gösterim, tıklama ve CTR tablosu oluştur
- [ ] Markalı ve markasız sorguları ayır
- [ ] Cihaz ve ülke kırılımını ekle
- [ ] İlk 20 fırsat sorgusunu seç

Çıktı: `search-console-baseline.csv` veya eşdeğer rapor.

### Gün 3 — GA4 funnel baseline

- [ ] Landing page bazında oturum ve engagement oranını çıkar
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

- [ ] En fazla giriş alan 10 sayfayı listele
- [ ] En yüksek çıkış oranına sahip ticari sayfaları listele
- [ ] İlk ekran mesajı, güven unsuru ve CTA eksiklerini not et
- [ ] Mobil ve masaüstü farklarını karşılaştır

Çıktı: Önceliklendirilmiş CRO sorun listesi.

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
- Gerçek olmayan yorum, referans, tasarruf oranı veya performans iddiası yayınlanmayacaktır.
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

## 11. Değişiklik günlüğü

| Tarih | Değişiklik | Durum |
| --- | --- | --- |
| 2026-09-06 | Teknik temel tamamlandı; production `главно` deployment doğrulandı | Tamamlandı |
| 2026-09-06 | Büyüme planı, KPI sözlüğü ve 7 günlük Sprint 1 eklendi | Devam ediyor |
