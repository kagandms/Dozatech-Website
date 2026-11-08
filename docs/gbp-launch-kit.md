# Google İşletme Profili — kurulum paketi (hizmet alanı işletmesi)

**Durum: taslak. Sahip teyidi bekleniyor.** Bu paket, DOZATECH'in Google İşletme Profili'ni (GBP) hizmet alanı işletmesi olarak kurmak için hazırlanmıştır. Kaynak: [`business-context.md`](business-context.md) (2026-10-30) ve [`seo-roadmap.md`](seo-roadmap.md).

**Kural:** Bilinmeyen her bilgi `[SAHİBİNDEN TEYİT]` ile işaretlenmiştir. Marka, ambalaj, teslimat koşulu, fiyat, garanti veya sayısal iddia bu pakette uydurulmamıştır.

## Temel bilgiler

- **Fiziksel adres:** Yok. Profilde adres gizlenecek; hizmet alanı İstanbul olarak tanımlanacak.
- **Hizmet alanı:** İstanbul. Montaj ve toplu işler için şehir dışı görüşme yapılabilir; bu alan GBP'ye eklenmeyecek [SAHİBİNDEN TEYİT: şehir dışı için ek bölge gerekiyor mu?].
- **Çalışma saatleri:** Esnek. [SAHİBİNDEN TEYİT: GBP'de "7 gün açık" mı, "randevuyla" mı seçilecek?]
- **Telefon:** +90 532 206 3859 (WhatsApp da bu numara üzerinden).
- **Site:** https://dozatech.com.tr
- **Hedef müşteriler:** Restoran, otel, kafe.

## 1. İşletme adı

**Yazılacak:** `DOZATECH`

**Neden:** Google İşletme Profili, işletmenin gerçekte kullanılan adını ister. Adı anahtar kelimelerle doldurmak (ör. "DOZATECH Dozaj Pompası Kimyasal") Google politikasını ihlal eder ve profilin askıya alınmasına yol açabilir. Web sitesindeki tam unvan ("DOZATECH - Endüstriyel Temizlik ve Dozaj Sistemleri") profil adına eklenmez; anahtar kelimeler açıklama ve hizmet alanlarında yer alır.

## 2. Kategoriler

Birincil kategori ticari önceliğe göre seçilmiştir: 1) kimyasal tedarik, 2) dozaj pompası satış/montaj.

| Rol | Aday kategori | Durum |
| --- | --- | --- |
| Birincil | Kimyasal ürün tedarikçisi | [SAHİBİNDEN TEYİT: GBP'de aratıp birebir ad var mı?] |
| Ek 1 | Temizlik malzemesi tedarikçisi | [SAHİBİNDEN TEYİT: GBP'de aratıp birebir ad var mı?] |
| Ek 2 | Endüstriyel ekipman tedarikçisi | [SAHİBİNDEN TEYİT: GBP'de aratıp birebir ad var mı?] |

Kategori adları bu pakette Google'ın listesinden kopyalanmamıştır. Listede birebir ad yoksa en yakın mevcut kategori seçilir ve bu karar sahibine bildirilir.

## 3. İşletme açıklaması (750 karakter sınırı)

Her iki alternatif de 750 karakterin altındadır. Telefon, URL, "en iyi", garanti ve kanıtsız iddia içermez.

**Alternatif A (412 karakter):**

> DOZATECH, restoran, otel ve kafeler için endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü tedariki yapar. Dozaj pompası satışı, montajı, bakımı ve onarımı da sunuyoruz. Yaklaşık 30 yıllık teknik tecrübemizle İstanbul merkezli çalışıyoruz; bölge ve toplu işler için görüşme yapıyoruz. Endüstriyel bulaşık makinesi satışı yapıyoruz; bulaşık makinesi tamiri ve bakımı hizmetimiz yoktur.

**Alternatif B (413 karakter):**

> Restoran, otel ve kafeler için kimyasal tedariki sağlıyoruz: endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü. Dozaj pompası satış, montaj, bakım ve onarım hizmetlerimiz var. Yaklaşık 30 yıllık teknik tecrübemizle İstanbul merkezli çalışıyoruz; ürün fiyatları teklif görüşmesinde paylaşılır. Endüstriyel bulaşık makinesi satışı yapıyoruz; bulaşık makinesi tamiri ve bakımı yapmıyoruz.

**Karakter sayısı kontrolü:** Yukarıdaki sayılar, metnin boşluklar ve noktalama dahil Python `len()` ile sayılmasıyla alındı. GBP kendi sayacını kullanır; yayımlamadan önce arayüzde de kontrol edilmeli.

**Not:** "Yaklaşık 30 yıllık teknik tecrübe" ifadesi `business-context.md`'de belirtilen biçimde kullanıldı. Şirketin kuruluş yaşı olarak yazılmadı.

## 4. Hizmetler

GBP "Hizmetler" alanı için 5 hizmet. Makine tamiri ve bakımı yoktur.

| Hizmet | Açıklama |
| --- | --- |
| Kimyasal tedariki | Endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü tedarik edilir. |
| Dozaj pompası montajı | Dozaj pompaları müşterinin makinesine montajlanır. |
| Dozaj pompası bakım ve onarımı | Dozaj pompalarının bakım ve onarımı yapılır. |
| Dozaj pompası satışı | Dozaj pompası satışı yapılır; fiyat teklif görüşmesinde paylaşılır. |
| Endüstriyel bulaşık makinesi satışı | Endüstriyel bulaşık makinesi satışı yapılır. Makine tamiri veya bakımı yapılmaz. |

[SAHİBİNDEN TEYİT: GBP'de hizmetler serbest metin mi, yoksa seçim listesi mi? Liste varsa birebir adlar kontrol edilmeli.]

## 5. Hizmet alanı

- **Seçim:** İstanbul (şehir düzeyi).
- **İlçe listesi:** Yok. Çok sayıda ilçe eklemek yerine şehir düzeyi seçilir. İlçe listesi isteniyorsa sahibinden onay alınır: [SAHİBİNDEN TEYİT].
- **Şehir dışı:** Hizmet alanına eklenmez. Bölge ve toplu işler için görüşme ile değerlendirilir.

## 6. Doğrulama rehberi

Google, hizmet alanı işletmelerinde doğrulama yöntemini hesaba göre belirler; yöntemler zamanla değişebilir. Bu bölümdeki bilgiler bir tahmin değil, hazırlık listesidir. **Kesin yöntem, profil oluşturulduğunda Google'ın gösterdiği seçeneğe bağlıdır.**

Olası yöntemler (Google'ın o anki isteğine göre değişir):
- Posta kartı: Gerçek bir adrese gönderilir. [SAHİBİNDEN TEYİT: Posta kartının gönderilebileceği gerçek bir adres (depo, ofis veya başka) var mı? Adres yalnızca doğrulama için kullanılsa bile gerçek olmalıdır.]
- Telefon, SMS veya e-posta: Google'ın gösterdiği durumda kullanılır.
- Video doğrulama: İşletmenin gerçekten faaliyet gösterdiğini gösteren kısa bir video istenebilir.
- Belge: İşletme belgesi veya benzeri kayıt istenebilir.

**Sahibinin hazırlaması gerekenler (varsa):**
- İşletme belgesi veya vergi levhası [SAHİBİNDEN TEYİT: mevcut mu?].
- Araç, ekipman ve depo görselleri (gerçek olanlar; stok görsel kullanılmaz).
- Ürün görselleri (ambalaj ve marka bilgisi teyit edilmediği için yalnızca gerçek fotoğraflar; [SAHİBİNDEN TEYİT: ambalaj ve markalar]).
- Kısa ve kesintisiz çekilmiş bir işletme videosu (varsa).

## 7. Fotoğraf ve video kontrol listesi

Bu liste, gerçek görseller sahibinden geldiğinde kullanılacaktır. Henüz kurulum fotoğrafı yoktur; yer tutucu veya stok görsel kullanılmayacaktır.

| Çekilecek | Not |
| --- | --- |
| Dozaj pompası montajı (gerçek) | Müşterinin alanı görünüyorsa izin alınır. |
| Kimyasal ürün ambalajları | Marka ve ambalaj teyit edilene kadar yalnızca gerçek ürünler. [SAHİBİNDEN TEYİT] |
| Depo ve ekipman | Gerçek depo ve araçlar. |
| Logo | Logo kullanımı sahibinin onayıyla. |

**Müşteri izni:** Müşteri alanı, çalışanı veya logosu görünüyorsa yazılı izin alınır. İzin yoksa kadraj değiştirilir veya görsel kullanılmaz.

**Dosya adı örneği:** `dozatech-dozaj-pompasi-montaj-01.jpg` (kısa, küçük harf, tire ile ayrılmış; anahtar kelime doldurma amacı taşımaz).

**Sahibinden beklenenler:** Gerçek fotoğraf ve video dosyaları, müşteri izinleri, logo dosyası [SAHİBİNDEN TEYİT: ne zaman ve hangi formatta gönderilecek?].

## 8. Soru-Cevap (6 hazır yanıt)

Yanıtlar yalnızca doğrulanabilir bilgiyle yazılmıştır.

1. **Hangi bölgelere hizmet veriyorsunuz?**
   İstanbul merkezli çalışıyoruz. Bölge ve toplu işler için teklif görüşmesi yapıyoruz.

2. **Ürün fiyatlarınız nedir?**
   Ürün fiyatları web sitemizde yayımlanmaz; fiyat ve tedarik koşulları teklif görüşmesinde paylaşılır.

3. **Dozaj pompası bakım ve onarımı yapıyor musunuz?**
   Evet, dozaj pompalarının bakım ve onarımını yapıyoruz.

4. **Bulaşık makinesi tamiri yapıyor musunuz?**
   Hayır. Bulaşık makinesi tamiri veya bakımı yapmıyoruz; endüstriyel bulaşık makinesi satışı yapıyoruz.

5. **Düzenli kimyasal alan müşterilere pompa desteği veriliyor mu?**
   Düzenli kimyasal alan müşterilere pompa temini ve bakım desteği ücretsiz sunulabilir. Uygunluk, kapsam ve sipariş koşulları görüşmede netleştirilir. [SAHİBİNDEN TEYİT: parça, arıza türü ve süre koşulları.]

6. **Hangi kimyasal ürünleri temin ediyorsunuz?**
   Endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü. [SAHİBİNDEN TEYİT: markalar, ambalaj boyutları, teslimat koşulları ve minimum sipariş miktarı.]

## 9. Yorum isteme politikası

**İlkeler:**
- Yorum yalnızca gerçek müşterilerden istenir.
- Teşvik, indirim, hediye veya ödül verilmez.
- Sahte, yazdırılmış veya başkası adına yorum yazılmaz ya da yazdırılmaz.
- Yalnızca memnun müşteriler değil, işi tamamlanmış tüm müşteriler aynı şekilde davet edilir (seçici davet yapılmaz).
- Müşteri istemezse baskı yapılmaz.

**Müşteriye gönderilecek kısa WhatsApp metni** (tek tek, toplu gönderim değil):

> Merhaba, DOZATECH olarak hizmetimizle ilgili deneyiminizi Google'da kısa bir yorumla paylaşabilirseniz çok memnun oluruz. İsterseniz buradan yazabilirsiniz: [GBP_YORUM_LINKI]. Teşekkür ederiz.

[GBP_YORUM_LINKI] yer tutucusu, profil açıldıktan sonra Google'ın verdiği yorum bağlantısıyla değiştirilecek. Bu bağlantıda UTM parametresi kullanılmaz; yorum linki Google'ın kendi bağlantısıdır.

## 10. Site tarafı eşleşme

**GBP web sitesi alanı:**
`https://dozatech.com.tr/?utm_source=google&utm_medium=organic&utm_campaign=gbp`

**Organization JSON-LD `sameAs` için yer tutucu liste** (profil açılınca eklenecek; şimdi koda eklenmez):
- Google İşletme Profili URL'si: `[PROFİL AÇILINCA EKLENECEK]`
- Diğer sosyal profiller: `[SAHİBİNDEN TEYİT: var mı, hangileri?]`

Mevcut durumda `sameAs` boş dizidir (`[]`); bu, profil URL'leri henüz olmadığı için bilinçli olarak böyledir.

## 11. 14 günlük takip

Profil açıldıktan sonra ilk 14 gün aşağıdaki verileri haftalık kaydedilecek.

**Nereden okunacak:**
- **GBP Performans sekmesi:** Arama ve harita görünümü, web sitesi tıklamaları, telefon çağrıları, yol tarifi istekleri. [TEYİT: arayüz adları güncel panelde doğrulanacak.]
- **Search Console:** `dozatech` ve marka sorgularında tıklama ve gösterim (`docs/search-console-baseline-2026-11-06.md` ile karşılaştırma için).
- **GA4:** `whatsapp_click`, `phone_click` ve GBP UTM'siyle gelen oturumlar. [SAHİBİNDEN TEYİT: GA4 hesap erişimi doğrulanmadı; bu veri okunmadan önce erişim gerekir.]

**Haftalık kayıt şablonu:**

| Hafta | Tarih aralığı | GBP arama görünümü | GBP harita görünümü | GBP web tıklaması | GBP telefon çağrısı | GBP yol tarifi | GA4 WhatsApp tıklaması | GA4 telefon tıklaması | GSC marka tıklama/gösterim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |

**Not:** GBP sayıları, Google'ın sağladığı gösterim ve tıklama sayılarıdır; kesin müşteri talebi değildir. Nitelikli talep, teklif ve satış kaydıyla ayrıca teyit edilir.

## Açık maddeler özeti

- Çalışma saatleri: esnek mi, 7 gün açık mı, randevulu mu?
- Kategori adlarının GBP'de birebir varlığı (3 aday).
- Hizmet alanı: şehir dışı için ek bölge gerekiyor mu, ilçe listesi istenecek mi?
- Doğrulama: posta kartı için gerçek bir adres var mı?
- İşletme belgesi veya vergi levhası var mı?
- Kimyasal markalar, ambalaj boyutları, teslimat koşulları, minimum sipariş miktarı.
- Pompa desteği: parça, arıza türü, süre ve sipariş koşulları.
- Gerçek kurulum fotoğrafları ve videolar; müşteri izinleri; logo.
- GBP hizmet listesi serbest metin mi, seçim listesi mi?
- Diğer sosyal profiller (`sameAs` için).
- GA4 hesap erişimi (14 günlük takip için).
