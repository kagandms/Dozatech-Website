# DOZATECH | Endüstriyel Temizlik ve Dozaj Sistemleri

DOZATECH, endüstriyel hijyen ve temizlik sektöründe hizmet veren kurumsal bir firmanın web sitesidir. Bu proje, işletmenin ürünlerini (endüstriyel bulaşık makineleri, dozaj pompaları ve kimyasallar) tanıtmak ve müşterilerle iletişim kurmak amacıyla hazırlanmıştır.

## 🌐 Canlı Site
Production domain: **[https://dozatech.com.tr](https://dozatech.com.tr)** (apex).

- **Barındırma:** Vercel. Proje: `tennyson10/dozatech`.
- **Production dalı:** `главно`. Canlı commit: `c77bcdd` (PR #2 merge).
- **Alan adları:** `dozatech.com.tr` (production) ve `dozatech.vercel.app`. `www.dozatech.com.tr` isteği `https://dozatech.com.tr/` adresine 308 ile yönlenir; `vercel.json` içindeki kural bunu uygular.
- **Doğrulama:** 2026-11-08 tarihinde Vercel paneli ve canlı HTTP kontrolü.
- **GitHub Pages:** Kullanılmıyor. Depodaki `CNAME` dosyası bu geçişin kalıntısıdır; kullanılmıyor, silme kararı bekliyor.

## 🛠️ Geliştirme
- `npm ci` — bağımlılıkları lockfile'a göre kurar.
- `npm run build` — Python build betiğini çalıştırır ve `dist/` çıktısını üretir.
- `npm test` — build'i çalıştırır ve rota, sitemap, yönlendirme ile çıktı dosyalarını doğrular. GitHub Actions'taki "DOZATECH Web CI" aynı komutu kullanır.

## 📂 Proje İçeriği
Sitede aşağıdaki ana bölümler yer almaktadır:
- **Ana Sayfa (index.html):** Genel tanıtım, hizmetler ve öne çıkan özellikler.
- **Ürünler (urunler.html):** Tüm ürün kategorilerinin genel görünümü.
  - **Bulaşık Makineleri:** Electrolux, Öztiryakiler ve Giyotin tip makineler.
  - **Dozaj Pompaları:** Atiker uyumlu, Dualdose ve Tekli pompalar.
  - **Kimyasallar:** Deterjan, Parlatıcı, Kireç ve Yağ çözücüler.

## 🚀 Teknolojiler
- **HTML5:** Semantik yapı.
- **Tailwind CSS:** Modern ve responsive tasarım.
- **JavaScript:** Mobil menü ve animasyonlar.

## 📞 İletişim
Sitedeki formlar ve WhatsApp butonları üzerinden doğrudan iletişime geçilebilir.
