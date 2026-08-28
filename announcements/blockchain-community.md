# Blockchain community launch — drafts

Drafts for **Pan** to review, adjust, and post. Sarasvatī cannot post on your behalf; these are ready-to-copy templates for the platforms most aligned with the "protect the canon" ethos.

---

## Twitter / X — long thread (12 tweets)

**1/**
Announcing Sarasvatī 🌊
An open, cryptographically-verifiable archive of world classical canons.
v0.2.0 released today.

First deliverable: Suśruta Saṃhitā (Sūtrasthāna, 46 chapters) — Tibetan machine-translated from a 1907 public-domain English edition.

🔗 github.com/lurongpan47/Sarasvati

**2/**
Why?
Classical texts are humanity's common inheritance. But:
• Modern editions are copyright-locked
• Manuscripts burn in war
• Digital archives die from broken links

Sarasvatī: translate → archive → release under CC BY-SA 4.0.

**3/**
Scope: 8-branch open canon
india · sanskrit · pali · seasia · silkroad · chinese · sinosphere · tibetan

Guided by the World Buddhist Canon Transmission Timeline (八系并观). 80 structured events, all in the repo as JSONL.

**4/**
Protection stack (this is where crypto matters):

✅ GitHub (public repo, versioned)
✅ SHA-256 manifest of every file
✅ OpenTimestamps → Bitcoin blockchain (nonrepudiable timestamp)
✅ IPFS (decentralized mirror)
✅ 9× AWS geographic mirrors
[looking for Arweave/Filecoin partners for permanent storage]

**5/**
The Bitcoin timestamp is live now:
File: manifests/SHA256SUMS.ots
The state of the canon at 2026-08-28 07:49 UTC is anchored to Bitcoin. Anyone can verify.

**6/**
IPFS CID (integrity-permanent):
`bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`

Try: `ipfs.io/ipfs/bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`

Please pin if you run an IPFS node. Every pin = one more copy that survives.

**7/**
Everything is CC BY-SA 4.0.
Fork it. Mirror it. Translate it. Break it. Just don't gatekeep it.

**8/**
Translations are **machine drafts**. All uncertain items are marked ⟨བརྟག⟩ / ⟨བརྟག་དགོས།⟩ (needs Tibetan medical review).

This is version 0, not authority. Human reviewers welcomed via PRs.

**9/**
Available in 24 languages (README):
zh-CN · zh-TW · ja · ko · vi · bo · hi · sa · si · th · my · pi · es · fr · de · it · pt · ru · ar · fa · tr · mn · id · km

Read in your language. Contribute in your language.

**10/**
For blockchain folks: this is what "permanent" should mean.
Not "cheap NFT + hope for the best."
It means SHA-256 → OTS → Bitcoin → IPFS → replicated storage → open license → cross-lingual.

Culture > speculation.

**11/**
Seeking:
🙏 Arweave / Filecoin permanent-storage sponsors (~$5 total per volume)
🙏 Tibetan medical scholars for chapter review
🙏 Any classical language expert on any of the 8 branches
🙏 Mirror runners (any language, any country)

**12/**
Sarasvatī (सरस्वती · དབྱངས་ཅན་མ།) is the goddess of speech, learning, and canonical texts.
This is her project.

Repo · Release · Timeline data · License:
🔗 github.com/lurongpan47/Sarasvati

/end

---

## Warpcast / Farcaster (single cast)

Sarasvatī v0.2.0 is live 🌊

An open, Bitcoin-anchored, IPFS-mirrored archive of world classical canons. First deliverable: 46 chapters of Suśruta Saṃhitā, translated EN→Tibetan.

24-language README. CC BY-SA 4.0. Fork it, mirror it, review it.

github.com/lurongpan47/Sarasvati

---

## Nostr (Damus / Amethyst)

🌊 Sarasvatī — Bitcoin-anchored classical-canon archive.

- v0.2.0 released
- Suśruta Saṃhitā (Tibetan draft, 46 ch)
- SHA-256 → OpenTimestamps → Bitcoin
- IPFS CID: bafybei...duce
- 24 languages · CC BY-SA 4.0

github.com/lurongpan47/Sarasvati

nostr, if you have an IPFS node, please pin.
#culture #freedomtech #IPFS #Bitcoin #opentimestamps

---

## r/CryptoCurrency + r/ipfs + r/opentimestamps (self-post)

**Title:** Sarasvatī — a Bitcoin-timestamped, IPFS-mirrored open archive of classical canons. Machine translations of texts still in translation deserts, released CC BY-SA 4.0.

**Body:**
Hey everyone. Launching **Sarasvatī** today (v0.2.0). It's a small open-culture experiment that tries to do "canonical preservation" the way crypto folks would actually want:

- Every file: SHA-256 manifest
- Manifest: OpenTimestamps → Bitcoin (nonrepudiable)
- Whole repo: IPFS CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`
- GitHub redundant mirror + 9 AWS geographic replicas
- License: CC BY-SA 4.0

**First deliverable**: 46 chapters of the ancient Indian medical treatise *Suśruta Saṃhitā* (Sūtrasthāna), machine-translated from Bhishagratna 1907 (public domain) into Tibetan. This text has no full Tibetan translation in existence.

**Big picture**: 8-branch roadmap covering india · sanskrit · pali · seasia · silkroad · chinese · sinosphere · tibetan — anchored to the World Buddhist Canon Transmission Timeline (80 structured events shipped in the repo).

**Looking for**:
- Anyone running an IPFS node to pin the CID
- Arweave / Filecoin sponsors for permanent storage (~$5 per volume)
- Native readers of any of the 24 README languages willing to smooth translations
- Tibetan medical scholars for chapter-level review

Repo: https://github.com/lurongpan47/Sarasvati

Not a token. Not an NFT. Just canon.

---

## Ethereum Foundation forum / ethresear.ch (research-culture post)

**Title:** Sarasvatī — cryptographic preservation of classical canons via SHA-256 + OTS + IPFS

Brief technical writeup emphasizing the integrity chain, the CC BY-SA 4.0 rationale for cultural heritage (avoids NFT-monetization traps), and the challenge of getting Arweave/Filecoin permanent storage as-yet unsolved.

[Draft continues after Pan's feedback]

---

## Content authority chain (for any post)

- **Repo:** github.com/lurongpan47/Sarasvati
- **Latest release:** v0.2.0 (2026-08-28)
- **IPFS CID root:** bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce
- **Bitcoin timestamp file:** manifests/SHA256SUMS.ots
- **Tarball SHA-256:** 775cb0b09a4e87bcd886b9e1e2b64636034d0a27968072c1358ff89b22b2775f
- **License:** CC BY-SA 4.0
- **Project code:** Sarasvatī · देवनागरी सरस्वती · བོད་ཡིག དབྱངས་ཅན་མ།
