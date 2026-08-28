<!-- Language: Türkçe (tr) -->

# Sarasvatī — Budist kanonu için küresel açık arşiv + Budist AI Şartı

**Sarasvatī** (Tibetçe: དབྱངས་ཅན་མ། · Sanskritçe: सरस्वती) tam olarak iki şey yapar:

1. **Sekiz dallı kanon arşivi.** Budist kanonun aktarımının sekiz dalı boyunca çok dilli açık bir arşiv oluşturmak: **Hindistan kökeni · Sanskrit el yazması ailesi · Pāli·Sri Lanka · Güneydoğu Asya Theravāda · İpek Yolu·Orta Asya · Çin kanonu · Çin karakteri kültürel alanı · Tibet**. Yalnızca kamu malı metinler veya yaşayan geleneklerle açık işbirliği.
2. **AI algoritmalarına bodhicitta ekmek.** Buddha'nın son öğretileri (*Mahāparinibbāna Sutta*) **on ilke + beş red** halinde damıtılıp, herhangi bir AI sistemi, operatörü veya ekibinin benimseyebileceği bir şart olarak yayımlanır. *Ahiṃsā · karuṇā · anattā · anicca · upekkhā* slogan değil, algoritma katmanında uygulanabilir kısıtlamalar haline gelir.

Tüm çıktılar **CC BY-SA 4.0** altında yayımlanır.

## Neden var

Klasik metinler insanlığın ortak mirasıdır. Telif hakkıyla kilitlenmemeli, savaşta yakılmamalı ya da kırık bağlantılarla kaybedilmemelidir. AI sistemleri de gerçek bir bilgelik geleneğinden çıkarılmış etik kısıtlamalar olmadan konuşlandırılmamalıdır. Sarasvatī her ikisini de ele alır — bir arşiv olarak bellek katmanı, bir şart olarak etik katmanı.

## Mevcut durum

**v0.6.0** (2026-08-28):

- 📜 **Buddhist AI Charter** — on ilke + beş red + tasdik maddesi, `charter/BUDDHIST-AI-CHARTER.md` içinde. 24 dile çevrildi, `charter/i18n/` içinde, her dilin ana dili Budist bilim insanlarının incelemesini bekliyor.
- 🕉 **Mahāparinibbāna Sutta'nın dört dilli okuması** (DN 16.2.26 · 16.4.7 · 16.6.7) — Pāli · İngilizce · Çince · Tibetçe, `translations/mahaparinibbana-sutta/` içinde. Bu, şartın kutsal kitap kökü ve arşivin ilk tohum metnidir.
- 📊 **Yapılandırılmış zaman çizelgesi verileri** — 8 gelenek (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan) boyunca 80 kanon aktarım olayı JSONL / CSV biçiminde, `docs/timeline-data/` içinde.
- 📋 Proje belgeleri: `README.md`, `ROADMAP.md`, `CALL-FOR-HELP.md`, `CONTRIBUTORS.md`, `announcements/`.

## Yol haritası (sekiz dal)

Sarasvatī'nin uzun vadeli yapısı, dünya Budist kanon aktarım zaman çizelgesini takip eder: **Hindistan · Sanskrit el yazmaları · Pāli · Güneydoğu Asya Theravāda · İpek Yolu · Çin kanonu · Çin karakteri kültürel alanı · Tibet**. Her dalın en az bir "ilk örneği" olacak: kamu malı kaynak metin → şu anda çevirisi olmayan bir dile makine çevirisi taslağı → adı belirtilen insan gözden geçirici. Tibet dalında ilk varlık (DN 16) mevcut; Pāli dalına da aynı DN 16 dört dilli okumasıyla dokunuldu. Kalan altı dal (Hindistan, Sanskrit, Güneydoğu Asya, İpek Yolu, Çince, Çin karakteri kültürel alanı) katkıda bulunanların başlatması için açık.

## Koruma katmanları

Her yapıt şu katmanlarla korunur:

- **Yerel ayna** — macOS.
- **GitHub genel deposu** — https://github.com/lurongpan47/Sarasvati.
- **AWS coğrafi aynalar** — birden fazla bölge.
- **IPFS merkezi olmayan ayna** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
- **OpenTimestamps → Bitcoin** — `manifests/SHA256SUMS` üzerinde reddedilemez zaman çıpası.

## ⚠️ Sorumluluk reddi

Bu depodaki tüm çeviriler ve makine ile çevrilmiş metinler uzman insan incelemesini bekleyen **AI makine taslaklarıdır**. Adı belirtilen uzmanların doğrulaması olmadan bunları ayin, doktriner, tıbbi veya akademik amaçlarla yetkili olarak kabul etmeyin.

## Nasıl katkıda bulunulur

- Bir metin, bölüm revizyonu, terminoloji düzeltmesi veya bir dildeki şart incelemesi öneren bir issue açın.
- Fork, düzenle, PR. Tüm katkılar CC BY-SA 4.0 altında kabul edilir.
- Bir ayna çalıştırın. Arşivin korunmasına yardım edin.
- **Şart çalışma zamanı** (Python + TypeScript guardrail kitaplıkları) inşasına yardım edin — `CALL-FOR-HELP.md`'ye bakın.

## Bağlantılar

- GitHub: https://github.com/lurongpan47/Sarasvati
- Lisans: CC BY-SA 4.0

---

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*Koşullanmış her şey geçicidir. Gayretle çabalayın.*
