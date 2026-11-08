# Vercel domain geçişi — yayın notu

**Durum: tamamlandı (2026-11-08). `https://dozatech.com.tr` apex production domain olarak canlı; `www` apex'e yönleniyor.**

## Doğrulanmış mevcut durum (2026-11-08)

- **Vercel paneli:** Proje `tennyson10/dozatech`; production dalı `главно`; canlı commit `c77bcdd` (PR #2 merge). Apex `dozatech.com.tr` production domain; www apex'e yönleniyor. Kaynak: proje sahibinin Vercel paneli kontrolü, 2026-11-08.
- **Canlı HTTP (2026-11-08, bu depoda tekrar kontrol edildi):**

| İstek | Sonuç |
| --- | --- |
| `https://dozatech.com.tr/` | `200` |
| `https://www.dozatech.com.tr/` | `308`, `Location: https://dozatech.com.tr/` |
| `http://dozatech.com.tr/` | `308`, `Location: https://dozatech.com.tr/` |
| `https://www.dozatech.com.tr/urunler?utm_source=x&probe=1` | `308`, `Location: https://dozatech.com.tr/urunler?utm_source=x&probe=1` (path ve query korunuyor) |
| `https://dozatech.vercel.app/` | `200` |

- **Repo kuralı:** `vercel.json` içinde `www.dozatech.com.tr` → `https://dozatech.com.tr/:path*` (kalıcı). Bu kural `главно` dalındadır.

## Tarihsel kayıt (2026-10-25, artık geçerli değil)

2026-10-25 kontrolünde yön tersti: `https://dozatech.com.tr/` `308` ile `https://www.dozatech.com.tr/` adresine gidiyordu ve www ana sayfası `200` dönüyordu. Bu kayıt, geçişten önceki durumu belgelemek için tutulmuştur.

## Yayın sırası ve durum

1. **Değişiklik öncesi Vercel domain listesi ve yönlendirme ayarlarının kaydı:** Bu depoda kayıt yok. Bu geçişe ait panel görüntüsü veya önceki ayar kaydı depoda yok.
2. **Vercel production domaini apex olarak ayarlandı, www apex'e yönleniyor:** Tamamlandı. Canlı HTTP sonuçları yukarıdaki tabloda.
3. **Repo tarafı (`vercel.json` www → apex kuralı):** `главно` dalında mevcut; canlı davranışla uyumlu.
4. **Kanıt:** Yukarıdaki istek sonuçları. Panel ekran görüntüsü bu depoda saklanmadı.

## Açık kalanlar

- **Eski Vercel projesi:** Kimliği ve durumu bu depodan belirlenemedi. Hiçbir proje silinmedi veya değiştirilmedi.
- **Panel www kuralı:** Vercel panelinde ayrıca bir www yönlendirmesi tanımlı olup olmadığı bu depodan doğrulanamaz; canlı davranış 308 ile apex'e yönleniyor.
- **`CNAME` dosyası:** GitHub Pages kalıntısı. Kullanılmıyor; silme kararı bekliyor. Dosya bu çalışmada silinmedi.

## Geri dönüş

Beklenmeyen `5xx` veya rota kaybında önce Vercel panelindeki domain/yönlendirme ayarlarını kayıtlı önceki haline döndür; ardından repo değişikliğini geri al ve son bilinen production commit'ini (`c77bcdd`) yeniden yayımla. Geri dönüşten sonra apex, www ve path/query örneklerini yukarıdaki tabloyla tekrar kontrol et.

Bu dokümanın güncellenmesi sırasında Vercel ayarı, DNS veya production deployment değiştirilmedi.
