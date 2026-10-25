# Vercel domain geçişi — yayın notu

**Durum: hazırlık notu; production ayarı ve deployment yapılmadı.**

## Mevcut ve hedef davranış

- **Canlıda gözlenen:** `https://dozatech.com.tr/` `308` ile `https://www.dozatech.com.tr/` adresine gidiyor; www ana sayfası `200` dönüyor. `https://dozatech.com.tr/urunler?utm_source=codex_audit&probe=1` isteğinin `Location` başlığı aynı path ve query’yi www’ye taşıyor ve yanıt `200` oluyor. Bu HTTP sonucu paneldeki gerçek domain ayarını göstermez.
- **Panel:** Vercel production domain/primary ayarı bu çalışma sırasında incelenemedi; mevcut panel konfigürasyonu doğrulanmış değil.
- **Hedef:** `https://dozatech.com.tr` doğrudan `200`; www aynı path ve query korunarak apex’e kalıcı yönlenir; HTTP hostları HTTPS’e çıkar. Vercel panelinde apex production primary olur; www yalnızca apex’e yönlenir. Repo kuralı `www.dozatech.com.tr` → `https://dozatech.com.tr/:path*` yönünü uygular.

## Yayın sırası

1. Değişiklik öncesi Vercel domain listesini ve yönlendirme ayarlarını kayda al; apex ve www domainlerinin bağlı/TLS hazır olduğunu panelden doğrula.
2. Vercel production domainini apex olarak ayarla. www için varsa panel yönlendirmesini yalnızca apex’e ver; apex’ten www’ye giden ters yönlü panel kuralı bırakma. Böylece panel ve repo aynı yönde çalışır.
3. PR’ı yayımla ve otomatik production deployment tamamlandıktan sonra tam URL’lerle doğrula: apex ana sayfası `200`; www `308` ile apex; path ve query değişmeden korunmuş; HTTP istekleri HTTPS’e çıkar; yönlendirme döngüsü yok.
4. Kanıtı, istek URL’leri ve her adımın status/Location başlıklarıyla kaydet. Panel erişimi veya gerçek HTTP yanıtı yoksa kontrolü tamamlandı işaretleme.

## Geri dönüş

Loop, beklenmeyen `5xx` veya rota kaybında önce değişiklik öncesi kaydedilen Vercel domain/yönlendirme ayarlarını geri yükle; ardından repo değişikliğini geri alıp son bilinen production commit’ini yeniden yayımla. Geri dönüşten sonra apex, www ve path/query örneklerini tekrar kontrol et. Bu görevde ayar, DNS veya production deployment değişikliği yapılmadı.
