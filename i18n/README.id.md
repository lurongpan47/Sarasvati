<!-- Language: Bahasa Indonesia (id) -->

# Sarasvatī — arsip terbuka global untuk kanon Buddhis + Piagam AI Buddhis

<p align="center">
  <a href="../docs/Global-Buddhist-Canon-Transmission-Timeline.pdf">
    <img src="../docs/timeline-preview-3lang.png" alt="Garis waktu pewarisan kanon Buddhis dunia — delapan cabang pandangan paralel (judul tiga bahasa: Tionghoa · Inggris · Tibet)" width="860">
  </a>
  <br>
  <sub><i>Garis waktu pewarisan kanon Buddhis dunia · delapan cabang pandangan paralel (中文 · English · བོད་ཡིག judul tiga bahasa)<br>PDF lengkap: <a href="../docs/Global-Buddhist-Canon-Transmission-Timeline.pdf"><code>docs/Global-Buddhist-Canon-Transmission-Timeline.pdf</code></a></i></sub>
</p>

**Sarasvatī** (Tibet: དབྱངས་ཅན་མ། · Sanskerta: सरस्वती) melakukan tepat dua hal:

1. **Arsip kanon delapan cabang.** Membangun arsip terbuka multibahasa mengikuti delapan cabang transmisi kanon Buddhis: **India asal · Naskah Sanskerta · Pāli·Sri Lanka · Theravāda Asia Tenggara · Jalur Sutra·Asia Tengah · Kanon Tionghoa · Wilayah budaya aksara Tionghoa · Tibet**. Hanya teks domain publik, atau kolaborasi eksplisit dengan tradisi yang masih hidup.
2. **Menanam Bodhicitta ke dalam algoritma AI.** Ajaran terakhir Sang Buddha (*Mahāparinibbāna Sutta*) disuling menjadi **sepuluh prinsip + lima penolakan**, diterbitkan sebagai piagam yang dapat diadopsi oleh sistem AI, operator, atau tim mana pun. *Ahiṃsā · karuṇā · anattā · anicca · upekkhā* menjadi batasan yang dapat dieksekusi di lapisan algoritma, bukan slogan.

Semua keluaran dirilis di bawah **CC BY-SA 4.0**.

## Mengapa ini ada

Teks klasik adalah warisan bersama umat manusia. Mereka tidak boleh dikunci oleh hak cipta, dibakar dalam perang, atau hilang karena tautan rusak. Sistem AI juga tidak boleh dikerahkan tanpa batasan etika yang diambil dari tradisi kebijaksanaan yang sungguh-sungguh. Sarasvatī menangani keduanya — lapisan memori sebagai arsip, lapisan etika sebagai piagam.

## Status saat ini

**v0.6.3** (2026-08-29):

- 🖼 **Baru di v0.6.3** — Menambahkan **spanduk garis waktu pewarisan dengan judul tiga bahasa** (Tionghoa · Inggris · Tibet) di bagian atas, dan menyelesaikan **verifikasi A untuk 82 peristiwa** yang mencakup delapan cabang pewarisan (India asal · cabang naskah Sansekerta · Pāli·Sri Lanka · Theravada Asia Tenggara · Jalur Sutra · kanon Tionghoa · lingkup budaya aksara Han · Tibet).
- 📜 **Buddhist AI Charter** — sepuluh prinsip + lima penolakan + klausul pengesahan, di `charter/BUDDHIST-AI-CHARTER.md`. Sudah diterjemahkan ke 24 bahasa di `charter/i18n/`, menunggu tinjauan oleh sarjana Buddhis penutur asli setiap bahasa.
- 🕉 **Pembacaan empat bahasa Mahāparinibbāna Sutta** (DN 16.2.26 · 16.4.7 · 16.6.7) — Pāli · Inggris · Tionghoa · Tibet, di `translations/mahaparinibbana-sutta/`. Inilah akar tekstual dari piagam dan teks benih pertama dari arsip.
- 📊 **Data linimasa terstruktur** — 80 peristiwa transmisi kanon di 8 tradisi (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan) sebagai JSONL / CSV, di `docs/timeline-data/`.
- 📋 Dokumen proyek: `README.md`, `ROADMAP.md`, `CALL-FOR-HELP.md`, `CONTRIBUTORS.md`, `announcements/`.

## Peta jalan (delapan cabang)

Struktur jangka panjang Sarasvatī mengikuti linimasa transmisi kanon Buddhis dunia: **India · Naskah Sanskerta · Pāli · Theravāda Asia Tenggara · Jalur Sutra · Kanon Tionghoa · Wilayah budaya aksara Tionghoa · Tibet**. Setiap cabang akan memiliki setidaknya satu "sampel pertama": teks sumber domain publik → draf terjemahan mesin ke bahasa yang saat ini belum memiliki terjemahan → peninjau manusia bernama. Cabang Tibet sudah memiliki aset pertama (DN 16); cabang Pāli juga tersentuh melalui pembacaan empat bahasa DN 16 yang sama. Enam cabang tersisa (India, Sanskerta, Asia Tenggara, Jalur Sutra, Tionghoa, wilayah aksara Tionghoa) terbuka bagi kontributor untuk memulai.

## Lapisan perlindungan

Setiap artefak dilindungi oleh:

- **Cermin lokal** — macOS.
- **Repo publik GitHub** — https://github.com/lurongpan47/Sarasvati.
- **Cermin geografis AWS** — beberapa wilayah.
- **Cermin terdesentralisasi IPFS** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
- **OpenTimestamps → Bitcoin** — jangkar waktu yang tak dapat disangkal pada `manifests/SHA256SUMS`.

## ⚠️ Sanggahan

Semua terjemahan dan teks terjemahan mesin di repo ini adalah **draf AI** yang menunggu tinjauan pakar manusia. Jangan perlakukan sebagai otoritatif untuk tujuan ritual, doktrinal, medis, atau akademis tanpa validasi oleh spesialis bernama.

## Cara berkontribusi

- Buka issue yang mengusulkan sebuah teks, revisi bab, koreksi terminologi, atau tinjauan piagam bahasa tertentu.
- Fork, edit, PR. Semua kontribusi diterima di bawah CC BY-SA 4.0.
- Jalankan cermin. Bantu melestarikan arsip.
- Bantu membangun **runtime piagam** (pustaka guardrail Python + TypeScript) — lihat `CALL-FOR-HELP.md`.

## Tautan

- GitHub: https://github.com/lurongpan47/Sarasvati
- Lisensi: CC BY-SA 4.0

---

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*Segala yang berkondisi adalah anicca. Berjuanglah dengan tekun.*
