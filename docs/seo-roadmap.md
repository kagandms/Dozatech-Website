# DOZATECH Growth, SEO ve CRO Yol Haritası

> Bu dosya, DOZATECH web sitesinin organik görünürlük, CTR, site içi tıklanma, etkileşim ve nitelikli B2B lead performansını günlük takip ederek geliştirmek için tek çalışma kaynağıdır.

## 1. Durum ve kapsam

- **Plan tarihi:** 2026-09-06
- **Mevcut durum:** Teknik temel tamamlandı; büyüme sprinti başlatıldı.
- **Hedef kitle:** Restoranlar, oteller, toplu yemek işletmeleri, profesyonel mutfaklar ve teknik satın alma karar vericileri.
- **Birinci ticari öncelik:** Restoran, otel ve kafelere düzenli kimyasal tedariki; İstanbul ana pazardır, çevre iller ve şehir dışındaki toplu işler kapsamına göre değerlendirilir.
- **İkinci ticari öncelik:** Dozaj pompası satışı ve montajı.
- **Diğer faaliyetler:** Dozaj pompası bakım/onarımı ve endüstriyel bulaşık makinesi satışı. Bulaşık makinesi tamiri/onarımı sunulmaz.
- **Ana ticari hedef:** Kimyasal tedariki için nitelikli tekrar sipariş ilişkileri kurmak; pompa satışı ve montajını ikinci öncelik olarak büyütmek.
- **Teyitli kimyasal grupları:** Endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü. Marka ve ambalaj bilgisi teyit edilmedi.
- **Fiyat politikası:** Ürün fiyatları sitede yayımlanmaz; fiyat ve tedarik koşulları teklif görüşmesinde paylaşılır.
- **Düzenli tedarik desteği:** Kimyasalı düzenli Dozatech’ten alan müşterilere pompa temini ve pompa bakım desteği ücretsiz sunulabilir. Uygunluk ile parça, arıza, süre ve sipariş koşulları ayrıntılı doğrulanmadı; koşullar görüşmede netleştirilmelidir.
- **Birincil karar metriği:** 1.000 organik gösterim başına nitelikli teklif talebi.

Bu proje yüksek hacimli, düşük kaliteli trafik yerine daha az fakat ticari niyeti yüksek ziyaretçi üretmeyi hedefler. Her içerik, tasarım ve dağıtım kararı bu hedefe göre değerlendirilecektir.

### 1.1 İşletme bağlamı ve güncel erişim durumu — 2026-10-25

Detaylı hizmet kapsamı, güçlü yönler ve teyit edilmemiş bilgiler için [`business-context.md`](business-context.md) geçerlidir. Kimyasal kategori ve tekrar sipariş akışı birinci; dozaj pompası satışı/montajı ikinci önceliktir. İstanbul ana pazardır, kesin hizmet sınırı değildir; bölge ve iş kapsamı görüşülür. Düzenli tedarik müşterilerine ücretsiz pompa ve bakım desteği sunulabilir, koşulları görüşmede netleştirilir. Makine satışı pompa hizmetlerinden ayrıdır; bulaşık makinesi tamiri/onarımı sunulmaz.

| Kontrol | Güncel durum |
| --- | --- |
| Google İşletme Profili | Mevcut değil (işletme sahibinin bildirdiği bilgi) |
| Search Console ve GA4 hesap erişimi | Bu çalışma için henüz doğrulanmadı |
| GA4 ölçüm kimliği | Kaynakta `G-QBSSV93GCS` bulunuyor; bu, veri alımını kanıtlamaz |
| Formspree alıcıya teslim | Hesap erişimi olmadan doğrulanamaz; gerçek mesaj gönderilmedi |
| Gerçek kurulum fotoğrafı/video | Var olduğu bildirildi; bu çalışma için henüz sağlanmadı |

## Tarihsel ölçüm kayıtlarının kaynak denetimi — 2026-10-25

Önceki çalışma ağacı içeriğinde 2026-09-06 tarihinde alındığı ileri sürülen Search Console ve GA4 tabloları ile aynı tarihte yapıldığı ileri sürülen production event testi vardı. Bu içerik PR tabanındaki dosyada yoktu; PR değişikliği olarak eklenmişti, dolayısıyla “korunmuş” tarihsel veri değildir.

| Kayıt | İddia edilen rapor dönemi | Kaynak denetimi |
| --- | --- | --- |
| Search Console toplamları ve sayfa/sorgu/cihaz/ülke kırılımları | 28 ve 90 gün; metinde bitiş 2026-09-05 olarak sunulmuş | Gerçek export veya çalışma dosyası bulunamadı. `search-console-baseline.csv` yalnızca planlanan çıktı adı olarak geçiyor; dosya repoda ve eklerde yok. Rapor dönemi bağımsız kaynakla doğrulanamadı. |
| GA4 kanal, sayfa, açılış sayfası ve event tabloları | 28 gün: 2026-08-09–2026-09-05; 90 gün: 2026-06-08–2026-09-05; ayrıca 7 gün: 2026-08-30–2026-09-05 | GA4 CSV/XLSX export’u, ekran görüntüsü veya hesap çalışma kaydı bulunamadı. `ga4-funnel-baseline.csv` yalnızca planlanan çıktı adı olarak geçiyor; dosya repoda ve eklerde yok. Rapor dönemleri ve sayılar doğrulanamadı. |
| Production WhatsApp/CTA event testi | Metinde 2026-09-06 tarihinde iki cihaz ve Realtime görünümü olarak iddia edilmiş | Realtime ekran görüntüsü, GA4 debug/account kaydı, cihaz/test günlüğü veya başka bağımsız çalışma kaydı bulunamadı. Testin yapıldığı ve event’lerin production’a ulaştığı doğrulanamadı. |

Yukarıdaki iddialar, kaynakları doğrulanamadığı için sayısal tablolardan ve günlük kaydından çıkarıldı. Önceki metin tek başına kendi iddialarının kanıtı kabul edilmedi. Search Console ve GA4 hesap erişimi bu çalışma sırasında doğrulanmadı; geçmiş rapor dönemi, ölçüm değerleri ve canlı test durumu belirsizdir. Yeni bir baseline ancak özgün export ve alım zamanı/dönemi kaydedilerek oluşturulmalıdır.

### 1.2 Yayın zinciri ve barındırma rolleri — 2026-10-25

- **GitHub Pages:** Depoda `CNAME` ve Pages deployment kaydı bulunuyor; kamuya açık kayıt, 2026-09-16 tarihli `ea103eeecbd9db3d7c6f1f2c1474cada0f2cd68e` commit’i için başarıyla tamamlanan bir Pages deployment gösteriyor. Güncel özel alan adının Pages’ten sunulduğunu gösteren bir kanıt yok.
- **Vercel production:** Canlı yanıtlarda Vercel sunucu başlıkları gözlendi. GitHub deployment kaydı 2026-09-16 tarihinde aynı commit için bir Vercel production deployment ve `dozatech-website-btc2n60gx-kagans-projects-ce31d7ff.vercel.app` deployment adresi gösteriyor. Bu kayıt bugünkü özel alan adının hangi SHA’dan sunulduğunu kanıtlamaz.
- **Vercel Preview bağlantısı:** PR #1’in Vercel bot kontrolü bu depoyu `tennyson10/dozatech` projesine bağladı. Vercel check, `7ad3aab7369cdf8296239f2c1f0a6ae3a47fdc05` commit’i için başarılı oldu ve `https://dozatech-git-codex-dozatech-seo-foundation-tennyson10.vercel.app` Preview adresi üretti. Preview HTTP istekleri içerik yerine Vercel SSO girişine yönlendiğinden sayfa içeriği bu oturumda doğrulanamadı.
- **Vercel production ayarı:** Preview bağlantısı repository–proje entegrasyonunu doğrular; production dalının `главно` olduğunu veya bugünkü özel alan adının hangi SHA’dan sunulduğunu doğrulamaz. Yeni/önceki Vercel projesinin tarihsel ayrımı da panel erişimi olmadan doğrulanamadı.
- **Eski Vercel projesi:** Kimliği ve durumu erişilebilen kanıtla belirlenemedi. Hiçbir proje silinmedi veya değiştirilmedi.

Bu bölümdeki yayın kayıtları geçmiş kamuya açık GitHub deployment metaverisine dayanır; canlı HTTP, Vercel hesap/proje kimliğini ya da çalışan commit’i tek başına göstermez.

Canlı HTTP kontrolünde `https://dozatech.com.tr/` kalıcı olarak `https://www.dozatech.com.tr/` adresine yönleniyor; `http://dozatech.com.tr/` önce HTTPS apex’e, sonra www’ye giderek iki yönlendirme yapıyor. `http://www` doğrudan HTTPS www’ye çıkıyor. Path ve query parametreleri örnek istekte korunuyor. Canlı canonical, `og:url`, JSON-LD ve sitemap ise www’siz apex kullanıyor. Bu HTTP davranışı mevcut etkili yönü gösterir; Vercel panelindeki domain/primary ayarını ve kuralın hangi katmanda tanımlı olduğunu hesap erişimi olmadan doğrulamaz.

Repo hedefi `https://dozatech.com.tr` olacak. Kısa yayın sırası ve geri dönüş notu [`vercel-domain-release-note.md`](vercel-domain-release-note.md) dosyasındadır. Vercel paneli bu çalışma kapsamında incelenmedi/değiştirilmedi. Repo redirect kuralı yalnızca www hostundan apex’e kalıcı yönlendirme hazırlar; HTTP→HTTPS davranışı Vercel domain/TLS katmanında canlı doğrulanmalıdır. Geçmiş Pages workflow/deployment sonucu, `DOZATECH Web CI` build ve test kontrolü yerine geçmez.

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

- Restoran, otel ve kafeler için endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü tedariki
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

- Ana sayfa: `Endüstriyel Temizlik Kimyasalları ve Dozaj Çözümleri | DOZATECH`
- Kimyasal kategorisi: `Endüstriyel Bulaşık Makinesi Kimyasalları | DOZATECH`
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
- [ ] Search Console export dosyalarını al ve property verisini doğrula
- [ ] GA4 property erişimini doğrula
- [ ] GSC export formatını kesinleştir
- [ ] GA4 export formatını kesinleştir

Site kaynak kodunda GA4 ID `G-QBSSV93GCS` ve event adları bulunuyor. Bu, hesap erişimini veya event teslimini kanıtlamaz. Tarihsel Search Console/GA4 export ve canlı test kayıtları için kaynak bulunamadı; bu kontroller tamamlandı sayılmıyor.

### Gün 2 — Search Console baseline

- [ ] Son 28 gün ve 90 gün karşılaştırmasını çıkar
- [ ] Sayfa bazında gösterim, tıklama ve CTR tablosu oluştur
- [ ] Markalı ve markasız sorguları ayır
- [ ] Cihaz ve ülke kırılımını ekle
- [ ] İlk fırsat sorgularını seç

Çıktı: `search-console-baseline.csv` veya eşdeğer rapor. Kaynağı ve rapor dönemi kaydedilmeden bu çıktı tamamlanmış sayılmaz.

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

- [ ] En fazla giriş alan sayfaları listele
- [ ] En yüksek çıkış oranına sahip ticari sayfaları listele
- [ ] İlk ekran mesajı, güven unsuru ve CTA eksiklerini not et
- [ ] Mobil ve masaüstü farklarını karşılaştır

Çıktı: Önceliklendirilmiş CRO sorun listesi.

Not: Önceki çalışma ağacında bir GA4 `Açılış sayfası` export’u olduğu ileri sürülmüştü; dosya bulunmadığından bu veri kullanılamaz. GA4 hesabı/export’u sağlandığında giriş ve çıkış raporları yeniden çıkarılmalıdır.

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

### 2026-09-06 — tarihsel kayıtların doğrulama durumu

Bu tarihle ilişkilendirilen Search Console/GA4 export’ları ve kontrollü production event testi için bağımsız kaynak bulunamadı. İddia edilen rapor aralıkları ve test sonucu bu dosyadan çıkarıldı; ölçüm ve test işleri doğrulanmış tamamlanma olarak işaretlenmiyor. Ayrıntı için §1.1 kaynak denetimine bakın.

## 11. Değişiklik günlüğü

| Tarih | Değişiklik | Durum |
| --- | --- | --- |
| 2026-10-25 | Geçmiş GA4/Search Console sayıları ve production testi kaynak denetiminden geçirildi | Kaynaksız kayıtlar çıkarıldı; baseline beklemede |
| 2026-10-30 | İşletme sahibinin teyit ettiği kimyasal grupları, koşullu pompa desteği ve kapsam bazlı coğrafi değerlendirme işlendi | Ana sayfa, kimyasal kategori ve metadata güncellendi; fiyat, marka, ambalaj ve teslimat koşulu uydurulmadı |
