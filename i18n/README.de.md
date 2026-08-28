<!-- Language: Deutsch (de) -->

# Sarasvatī — ein globales offenes Archiv des buddhistischen Kanons + Buddhistische KI-Charta

**Sarasvatī** (Tibetisch: དབྱངས་ཅན་མ། · Sanskrit: सरस्वती) tut genau zwei Dinge:

1. **Kanon-Archiv in acht Zweigen.** Aufbau eines mehrsprachigen offenen Archivs entlang der acht Übertragungszweige des buddhistischen Kanons: **Indien · Sanskrit-Manuskripte · Pāli·Sri Lanka · Südostasiatischer Theravāda · Seidenstraße·Zentralasien · Chinesischer Kanon · Kulturraum der chinesischen Schriftzeichen · Tibetisch**. Ausschließlich gemeinfreie Texte oder explizite Kooperation mit lebendigen Traditionen.
2. **Bodhicitta in KI-Algorithmen einpflanzen.** Die letzten Lehren des Buddha (*Mahāparinibbāna Sutta*) destilliert zu **zehn Prinzipien + fünf Verweigerungen**, veröffentlicht als Charta, die jedes KI-System, jeder Betreiber und jedes Team übernehmen kann. *Ahiṃsā · karuṇā · anattā · anicca · upekkhā* werden zu auf der Algorithmen-Ebene ausführbaren Einschränkungen, nicht zu Slogans.

Alle Ergebnisse werden unter **CC BY-SA 4.0** veröffentlicht.

## Warum es existiert

Klassische Texte sind das gemeinsame Erbe der Menschheit. Sie sollten weder durch Urheberrechte eingesperrt, im Krieg verbrannt noch durch tote Links verloren gehen. Und KI-Systeme sollten nicht ohne ethische Beschränkungen aus einer wirklichen Weisheitstradition eingesetzt werden. Sarasvatī bewältigt beides — eine Gedächtnisschicht als Archiv, eine Ethikschicht als Charta.

## Aktueller Stand

**v0.6.0** (2026-08-28):

- 📜 **Buddhist AI Charter** — zehn Prinzipien + fünf Verweigerungen + Bezeugungsklausel, in `charter/BUDDHIST-AI-CHARTER.md`. In 24 Sprachen übersetzt, in `charter/i18n/`, wartet auf die Prüfung durch muttersprachliche buddhistische Gelehrte.
- 🕉 **Viersprachige Lesung des Mahāparinibbāna Sutta** (DN 16.2.26 · 16.4.7 · 16.6.7) — Pāli · Englisch · Chinesisch · Tibetisch, in `translations/mahaparinibbana-sutta/`. Dies ist die schriftliche Wurzel der Charta und der erste Saat-Text des Archivs.
- 📊 **Strukturierte Zeitleistendaten** — 80 kanonische Übertragungsereignisse über die 8 Traditionen (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan) als JSONL / CSV, in `docs/timeline-data/`.
- 📋 Projektdokumente: `README.md`, `ROADMAP.md`, `CALL-FOR-HELP.md`, `CONTRIBUTORS.md`, `announcements/`.

## Fahrplan (acht Zweige)

Sarasvatīs langfristige Struktur folgt der weltweiten Zeitleiste der buddhistischen Kanon-Übertragung: **Indien · Sanskrit-Manuskripte · Pāli · Südostasiatischer Theravāda · Seidenstraße · Chinesischer Kanon · Kulturraum der chinesischen Schriftzeichen · Tibetisch**. Jeder Zweig wird mindestens eine „erste Probe" haben: gemeinfreier Quelltext → maschineller Übersetzungsentwurf in eine Sprache, in die derzeit keine Übersetzung existiert → namentlich benannter menschlicher Prüfer. Der tibetische Zweig hat bereits das erste Asset (DN 16); der Pāli-Zweig wurde durch dieselbe viersprachige DN 16-Lesung berührt. Die sechs verbleibenden Zweige (Indien, Sanskrit, Südostasien, Seidenstraße, Chinesisch, Zeichenkulturraum) sind für Beitragende zur Eröffnung offen.

## Schutzschichten

Jedes Artefakt wird geschützt durch:

- **Lokaler Spiegel** — macOS.
- **Öffentliches GitHub-Repo** — https://github.com/lurongpan47/Sarasvati.
- **AWS-Geografische Spiegel** — mehrere Regionen.
- **IPFS-Dezentraler Spiegel** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
- **OpenTimestamps → Bitcoin** — nicht widerlegbarer Zeitanker auf `manifests/SHA256SUMS`.

## ⚠️ Haftungsausschluss

Alle Übersetzungen und maschinell übersetzten Texte in diesem Repo sind **KI-Maschinenentwürfe**, die auf Prüfung durch menschliche Experten warten. Behandle sie ohne Bestätigung durch namentlich benannte Spezialisten nicht als autoritativ für rituelle, doktrinäre, medizinische oder akademische Zwecke.

## Wie man beiträgt

- Öffne eine Issue, die einen Text, eine Kapitel-Überarbeitung, eine Terminologie-Korrektur oder eine Prüfung der Charta in einer bestimmten Sprache vorschlägt.
- Fork, bearbeite, PR. Alle Beiträge werden unter CC BY-SA 4.0 akzeptiert.
- Betreibe einen Spiegel. Hilf, das Archiv zu bewahren.
- Hilf beim Bau der **Charta-Laufzeit** (Python + TypeScript Guardrail-Bibliotheken) — siehe `CALL-FOR-HELP.md`.

## Links

- GitHub: https://github.com/lurongpan47/Sarasvati
- Lizenz: CC BY-SA 4.0

---

*„Vayadhammā saṅkhārā, appamādena sampādetha."*
*Alle bedingten Dinge sind vergänglich. Strebt mit Achtsamkeit voran.*
