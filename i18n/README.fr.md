<!-- Language: Français (fr) -->

# Sarasvatī — archive ouverte mondiale du canon bouddhique + Charte bouddhique pour l'IA

<p align="center">
  <a href="../docs/Global-Buddhist-Canon-Transmission-Timeline.pdf">
    <img src="../docs/timeline-preview-3lang.png" alt="Chronologie de la transmission du canon bouddhique mondial — vue parallèle des huit branches (titre trilingue : chinois · anglais · tibétain)" width="860">
  </a>
  <br>
  <sub><i>Chronologie de la transmission du canon bouddhique mondial · vue parallèle des huit branches (中文 · English · བོད་ཡིག titre trilingue)<br>PDF complet : <a href="../docs/Global-Buddhist-Canon-Transmission-Timeline.pdf"><code>docs/Global-Buddhist-Canon-Transmission-Timeline.pdf</code></a></i></sub>
</p>

**Sarasvatī** (tibétain : དབྱངས་ཅན་མ། · sanskrit : सरस्वती) fait exactement deux choses :

1. **Archive du canon en huit branches.** Construire une archive ouverte multilingue le long des huit branches de transmission du canon bouddhique : **Inde · Manuscrits sanskrits · Pāli·Sri Lanka · Theravāda d'Asie du Sud-Est · Route de la Soie·Asie centrale · Canon chinois · Zone culturelle des caractères chinois · Tibétain**. Uniquement des textes du domaine public, ou une collaboration explicite avec les traditions vivantes.
2. **Planter la bodhicitta dans les algorithmes d'IA.** Les derniers enseignements du Bouddha (*Mahāparinibbāna Sutta*) distillés en **dix principes + cinq refus**, publiés comme une charte que tout système d'IA, opérateur ou équipe peut adopter. *Ahiṃsā · karuṇā · anattā · anicca · upekkhā* deviennent des contraintes exécutables au niveau algorithmique, non des slogans.

Toutes les productions sont publiées sous **CC BY-SA 4.0**.

## Pourquoi cela existe

Les textes classiques sont l'héritage commun de l'humanité. Ils ne devraient pas être verrouillés par le droit d'auteur, brûlés par la guerre, ni perdus par des liens rompus. Les systèmes d'IA non plus ne devraient pas être déployés sans contraintes éthiques tirées d'une véritable tradition de sagesse. Sarasvatī s'occupe des deux — une couche de mémoire comme archive, une couche éthique comme charte.

## État actuel

**v0.6.3** (2026-08-29) :

- 🖼 **Nouveau dans v0.6.3** — Ajout en haut d'une **bannière de chronologie de transmission avec titre trilingue** (chinois · anglais · tibétain), et achèvement de la **révision A pour 82 événements** couvrant les huit branches de transmission du canon bouddhique (origine indienne · branche des manuscrits sanskrits · Pāli·Sri Lanka · Theravada d'Asie du Sud-Est · Route de la Soie · canon chinois · aire culturelle des caractères chinois · tibétain).
- 📜 **Buddhist AI Charter** — dix principes + cinq refus + clause d'attestation, dans `charter/BUDDHIST-AI-CHARTER.md`. Traduite en 24 langues, dans `charter/i18n/`, en attente de relecture par des spécialistes bouddhistes locuteurs natifs.
- 🕉 **Lecture quadrilingue du Mahāparinibbāna Sutta** (DN 16.2.26 · 16.4.7 · 16.6.7) — pāli · anglais · chinois · tibétain, dans `translations/mahaparinibbana-sutta/`. C'est la racine scripturaire de la charte et le premier texte-graine de l'archive.
- 📊 **Données structurées de chronologie** — 80 événements de transmission canonique à travers les 8 traditions (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan) au format JSONL / CSV, dans `docs/timeline-data/`.
- 📋 Documents du projet : `README.md`, `ROADMAP.md`, `CALL-FOR-HELP.md`, `CONTRIBUTORS.md`, `announcements/`.

## Feuille de route (huit branches)

La structure à long terme de Sarasvatī suit la chronologie mondiale de transmission du canon bouddhique : **Inde · Manuscrits sanskrits · Pāli · Theravāda d'Asie du Sud-Est · Route de la Soie · Canon chinois · Zone culturelle des caractères chinois · Tibétain**. Chaque branche aura au moins un « premier échantillon » : texte source du domaine public → brouillon de traduction automatique vers une langue actuellement dépourvue de traduction → relecteur humain nommé. La branche tibétaine possède déjà le premier actif (DN 16) ; la branche pāli a été effleurée par la même lecture quadrilingue de DN 16. Les six branches restantes (Inde, sanskrit, Asie du Sud-Est, Route de la Soie, chinois, zone culturelle des caractères chinois) sont ouvertes à des contributeurs pour être lancées.

## Couches de protection

Chaque artefact est protégé par :

- **Miroir local** — macOS.
- **Dépôt public GitHub** — https://github.com/lurongpan47/Sarasvati.
- **Miroirs géographiques AWS** — plusieurs régions.
- **Miroir décentralisé IPFS** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
- **OpenTimestamps → Bitcoin** — ancre temporelle irrévocable sur `manifests/SHA256SUMS`.

## ⚠️ Avertissement

Toutes les traductions et textes traduits automatiquement de ce dépôt sont des **brouillons produits par IA** en attente de relecture humaine experte. Ne les considérez pas comme faisant autorité à des fins rituelles, doctrinales, médicales ou universitaires sans validation par des spécialistes nommés.

## Comment contribuer

- Ouvrez une issue proposant un texte, une révision de chapitre, une correction terminologique, ou une relecture de la charte dans une langue donnée.
- Fork, éditez, PR. Toutes les contributions sont acceptées sous CC BY-SA 4.0.
- Faites tourner un miroir. Aidez à préserver l'archive.
- Aidez à construire le **runtime de la charte** (bibliothèques guardrail Python + TypeScript) — voir `CALL-FOR-HELP.md`.

## Liens

- GitHub : https://github.com/lurongpan47/Sarasvati
- Licence : CC BY-SA 4.0

---

*« Vayadhammā saṅkhārā, appamādena sampādetha. »*
*Toutes les choses conditionnées sont impermanentes. Efforcez-vous avec diligence.*
