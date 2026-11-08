# Google İşletme Profili — kurulum paketi (hizmet alanı işletmesi)

**Durum: taslak. Sahip teyidi (2026-11-08) uygulandı; kalan maddeler sonundaki tabloda.** Bu paket, DOZATECH'in Google İşletme Profili'ni (GBP) hizmet alanı işletmesi olarak kurmak için hazırlanmıştır. Kaynak: [`business-context.md`](business-context.md) (2026-11-08 güncellemesi) ve [`seo-roadmap.md`](seo-roadmap.md).

**Kural:** Bilinmeyen her bilgi `[SAHİBİNDEN TEYİT]` ile işaretlenmiştir. Marka, ambalaj (teyitli olanlar hariç), fiyat, garanti veya sayısal iddia bu pakette uydurulmamıştır.

## Temel bilgiler

- **Fiziksel işletme adresi:** Yok. Profilde adres gizlenecek. Adres yalnızca doğrulama amacıyla kullanılacaksa bu ayrı bir karardır (bkz. §6).
- **Hizmet alanı:** İstanbul'un her bölgesi; montaj ve toplu işlerde şehir dışı. Şehir dışı iller: [SAHİBİNDEN TEYİT].
- **Çalışma saatleri:** Haftanın her günü açık.
- **İşletme türü:** Şahıs şirketi. Vergi levhası mevcut.
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
| Birincil | Kimyasal tedarikçisi | [SAHİBİNDEN TEYİT: arayüzde aratıp birebir ad seç] |
| Ek 1 | Temizlik malzemeleri tedarikçisi | [SAHİBİNDEN TEYİT: arayüzde aratıp birebir ad seç] |
| Ek 2 | Endüstriyel ekipman tedarikçisi | [SAHİBİNDEN TEYİT: arayüzde aratıp birebir ad seç] |

Kategori adları bu pakette Google'ın listesinden kopyalanmamıştır. Listede birebir ad yoksa en yakın mevcut kategori seçilir ve bu karar sahibine bildirilir.

## 3. İşletme açıklaması (750 karakter sınırı)

İki alternatif de 750 karakterin altındadır. Telefon, URL, "en iyi", garanti ve kanıtsız iddia içermez. Bulaşık makinesi tamiri/bakımı bu metinde yer almaz (bu bilgi yalnızca §8 S&C madde 4'te).

**Alternatif A (388 karakter):**

> DOZATECH, restoran, otel ve kafeler için endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü tedariki yapar. Dozaj pompası satışı, montajı, bakımı ve onarımı da sunuyoruz. Yaklaşık 30 yıllık teknik tecrübemizle çalışıyoruz. İstanbul'un her bölgesine ulaşıyoruz; montaj ve toplu işlerde şehir dışına da çıkıyoruz. Endüstriyel bulaşık makinesi satışı da yapıyoruz.

**Alternatif B (441 karakter):**

> Restoran, otel ve kafeler için kimyasal tedariki sağlıyoruz: endüstriyel bulaşık makinesi deterjanı, parlatıcı, yağ sökücü ve kireç sökücü. Dozaj pompası satış, montaj, bakım ve onarım hizmetlerimiz var. Yaklaşık 30 yıllık teknik tecrübemizle çalışıyoruz. Ürün fiyatları teklif görüşmesinde paylaşılır. İstanbul'un her bölgesine ulaşıyoruz; montaj ve toplu işlerde şehir dışına da çıkıyoruz. Endüstriyel bulaşık makinesi satışı da yapıyoruz.

**Karakter sayısı kontrolü:** Sayılar, metnin boşluk ve noktalama dahil Python `len()` ile sayılmasıyla alındı. GBP kendi sayacını kullanır; yayımlamadan önce arayüzde de kontrol edilmeli.

**Not:** "Yaklaşık 30 yıllık teknik tecrübe" ifadesi `business-context.md`'de belirtilen biçimde kullanıldı. Şirketin kuruluş yaşı olarak yazılmadı.

## 4. Hizmetler

GBP "Hizmetler" alanı için 5 hizmet. Makine tamiri ve bakımı yoktur.

| Hizmet | Açıklama |
| --- | --- |
| Kimyasal tedariki | Endüstriyel bulaşık makinesi deterjanı ve parlatıcı 20 L ambalajda; yağ sökücü ve kireç sökücü tedarik edilir. |
| Dozaj pompası montajı | Dozaj pompaları müşterinin makinesine montajlanır. |
| Dozaj pompası bakım ve onarımı | Dozaj pompalarının bakım ve onarımı yapılır. |
| Dozaj pompası satışı | Dozaj pompası satışı yapılır; fiyat teklif görüşmesinde paylaşılır. |
| Endüstriyel bulaşık makinesi satışı | Endüstriyel bulaşık makinesi satışı yapılır. Makine tamiri veya bakımı yapılmaz. |

[SAHİBİNDEN TEYİT: GBP'de hizmetler serbest metin mi, yoksa seçim listesi mi? Liste varsa birebir adlar kontrol edilmeli.]

## 5. Hizmet alanı

- **Ana bölge:** İstanbul'un her bölgesi. Profilde şehir düzeyinde "İstanbul" seçilir; ilçe listesi eklenmez.
- **Şehir dışı:** Montaj ve toplu işlerde şehir dışına çıkılır. Hangi illerin hizmet alanına ekleneceği: [SAHİBİNDEN TEYİT: hangi iller eklensin? Sahibin bildirdiği bilgiye göre GBP en fazla 20 alan kabul ediyor; bu limit arayüzde doğrulanacak.]
- **Değişiklik:** Sahibinden onay alınmadan hizmet alanına yeni il veya ilçe eklenmez.

## 6. Doğrulama rehberi

Google, hizmet alanı işletmelerinde doğrulama yöntemini hesaba göre belirler; yöntemler zamanla değişebilir. Bu bölüm bir tahmin değil, hazırlık listesidir. **Kesin yöntem, profil oluşturulduğunda Google'ın gösterdiği seçeneğe bağlıdır.**

**Adres ve gizlilik:** Profilde fiziksel adres gizlenecek. Google bir adres isterse, bu adres yalnızca doğrulama amacıyla kullanılacak ve profilde gösterilmeyecek. Fiziksel işletme adresi olmadığı için hangi adresin kullanılacağı sahibinin kararıdır: [SAHİBİNDEN TEYİT: posta kartı veya benzeri doğrulama için gerçek bir adres var mı?]

Olası yöntemler (Google'ın o anki isteğine göre değişir):
- Posta kartı: Gerçek bir adrese gönderilir (yukarıdaki karar gerekir).
- Telefon, SMS veya e-posta: Google'ın gösterdiği durumda kullanılır.
- Video doğrulama: İşletmenin gerçekten faaliyet gösterdiğini gösteren kısa bir video istenebilir.
- Belge: İşletme belgesi veya benzeri kayıt istenebilir.

**Sahibinin hazırlaması gerekenler:**
- Şahıs şirketi vergi levhası: **mevcut** (2026-11-08).
- Araç, ekipman ve depo görselleri (gerçek olanlar; stok görsel kullanılmaz).
- Ürün görselleri (gerçek ürün ve ambalajlar; marka [SAHİBİNDEN TEYİT]).
- Kısa ve kesintisiz çekilmiş bir işletme videosu (varsa).

## 7. Fotoğraf ve video kontrol listesi

Bu liste, gerçek görseller sahibinden geldiğinde kullanılacaktır. Henüz kurulum fotoğrafı yoktur; yer tutucu veya stok görsel kullanılmayacaktır.

| Çekilecek | Not |
| --- | --- |
| Dozaj pompası montajı (gerçek) | Müşterinin alanı görünüyorsa izin alınır. |
| Kimyasal ürün ambalajları | Deterjan ve parlatıcı 20 L ambalajda (teyitli); marka [SAHİBİNDEN TEYİT]. Yalnızca gerçek ürünler. |
| Depo ve ekipman | Gerçek depo ve araçlar. |
| Logo | Logo kullanımı sahibinin onayıyla. |

**Müşteri izni:** Müşteri alanı, çalışanı veya logosu görünüyorsa yazılı izin alınır. İzin yoksa kadraj değiştirilir veya görsel kullanılmaz.

**Dosya adı örneği:** `dozatech-dozaj-pompasi-montaj-01.jpg` (kısa, küçük harf, tire ile ayrılmış; anahtar kelime doldurma amacı taşımaz).

**Sahibinden beklenenler:** Gerçek fotoğraf ve video dosyaları, müşteri izinleri, logo dosyası [SAHİBİNDEN TEYİT: ne zaman ve hangi formatta gönderilecek?].

## 8. Soru-Cevap (6 hazır yanıt)

Yanıtlar yalnızca doğrulanabilir bilgiyle yazılmıştır.

1. **Hangi bölgelere hizmet veriyorsunuz?**
   İstanbul'un her bölgesine ulaşıyoruz. Montaj ve toplu işlerde şehir dışına da çıkıyoruz.

2. **Fiyat ve sipariş koşulları nedir?**
   Ürün fiyatları web sitemizde yayımlanmaz; fiyat teklif görüşmesinde paylaşılır. Deterjan ve parlatıcı için asgari sipariş: 2 deterjan + 1 parlatıcı. Müşteri konumumuza yakınsa: 1 deterjan + 1 parlatıcı. [SAHİBİNDEN TEYİT: "yakın" kriteri ne?]

3. **Dozaj pompası bakım ve onarımı yapıyor musunuz?**
   Evet, dozaj pompalarının bakım ve onarımını yapıyoruz.

4. **Bulaşık makinesi tamiri yapıyor musunuz?**
   Hayır. Bulaşık makinesi tamiri veya bakımı yapmıyoruz; endüstriyel bulaşık makinesi satışı yapıyoruz.

5. **Pompa desteği var mı?**
   Büyük işletmeler ve sürekli kimyasal alımı üzerinde anlaşan müşterilere ücretsiz montaj ve bakım olabilir. Bu koşullu bir olanaktır; kapsam ve koşullar görüşmede netleştirilir. [SAHİBİNDEN TEYİT: parça, arıza türü, süre ve sipariş koşulları.]

6. **Hangi ürünleri, hangi ambalajda ve ne zaman teslim ediyorsunuz?**
   Endüstriyel bulaşık makinesi deterjanı ve parlatıcı 20 L ambalajda temin edilir. Sipariş saatine göre aynı gün veya ertesi gün teslimat yapılabilir. Yağ sökücü ve kireç sökücü ambalajı ve markalar: [SAHİBİNDEN TEYİT].

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

## Açık maddeler (sahip teyidi bekleniyor)

| # | Madde | Bölüm |
| --- | --- | --- |
| 1 | Doğrulama için gerçek bir adres var mı? (posta kartı) | §6 |
| 2 | Şehir dışında hangi iller hizmet alanına eklensin? GBP alan limiti arayüzde doğrulanacak. | §5 |
| 3 | Kategori adları GBP arayüzünde birebir var mı? (3 aday: Kimyasal tedarikçisi, Temizlik malzemeleri tedarikçisi, Endüstriyel ekipman tedarikçisi) | §2 |
| 4 | GBP hizmetleri serbest metin mi, seçim listesi mi? | §4 |
| 5 | "Konumumuza yakın" kriteri nedir? (asgari sipariş) | §8 |
| 6 | Yağ sökücü ve kireç sökücü ambalaj boyutları ve markalar | §4, §7, §8 |
| 7 | Pompa desteği: parça, arıza türü, süre ve sipariş koşulları | §8 |
| 8 | Gerçek kurulum fotoğrafları ve videolar; müşteri izinleri; logo dosyası | §7 |
| 9 | Diğer sosyal profiller (`sameAs` için) | §10 |
| 10 | GA4 hesap erişimi (14 günlük takip için) | §11 |
| 11 | GBP arayüz adları (Performans sekmesi vb.) | §11 |
