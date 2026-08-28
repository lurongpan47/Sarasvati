<!-- Language: Português (pt) -->

# Sarasvatī — arquivo global aberto do cânone budista + Carta Budista para IA

**Sarasvatī** (tibetano: དབྱངས་ཅན་མ། · sânscrito: सरस्वती) faz exatamente duas coisas:

1. **Arquivo do cânone em oito ramos.** Construir um arquivo aberto multilíngue ao longo dos oito ramos de transmissão do cânone budista: **Índia · Manuscritos sânscritos · Pāli·Sri Lanka · Theravāda do sudeste asiático · Rota da Seda·Ásia Central · Cânone chinês · Zona cultural dos caracteres chineses · Tibetano**. Apenas textos de domínio público, ou colaboração explícita com tradições vivas.
2. **Plantar bodhicitta em algoritmos de IA.** Os últimos ensinamentos do Buda (*Mahāparinibbāna Sutta*) destilados em **dez princípios + cinco recusas**, publicados como carta que qualquer sistema de IA, operador ou equipe pode adotar. *Ahiṃsā · karuṇā · anattā · anicca · upekkhā* tornam-se restrições executáveis na camada algorítmica, não slogans.

Todas as produções são publicadas sob **CC BY-SA 4.0**.

## Por que existe

Os textos clássicos são herança comum da humanidade. Não devem ser trancados por direitos autorais, queimados na guerra, nem perdidos por links quebrados. E os sistemas de IA também não devem ser implantados sem restrições éticas retiradas de uma verdadeira tradição de sabedoria. Sarasvatī lida com ambos — uma camada de memória como arquivo, uma camada ética como carta.

## Estado atual

**v0.6.0** (2026-08-28):

- 📜 **Buddhist AI Charter** — dez princípios + cinco recusas + cláusula de atestação, em `charter/BUDDHIST-AI-CHARTER.md`. Traduzida para 24 idiomas, em `charter/i18n/`, à espera de revisão por estudiosos budistas falantes nativos.
- 🕉 **Leitura em quatro idiomas do Mahāparinibbāna Sutta** (DN 16.2.26 · 16.4.7 · 16.6.7) — pāli · inglês · chinês · tibetano, em `translations/mahaparinibbana-sutta/`. É a raiz textual da carta e o primeiro texto-semente do arquivo.
- 📊 **Dados estruturados da linha do tempo** — 80 eventos de transmissão canônica através das 8 tradições (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan) em JSONL / CSV, em `docs/timeline-data/`.
- 📋 Documentos do projeto: `README.md`, `ROADMAP.md`, `CALL-FOR-HELP.md`, `CONTRIBUTORS.md`, `announcements/`.

## Roteiro (oito ramos)

A estrutura de longo prazo de Sarasvatī segue a linha do tempo mundial de transmissão do cânone budista: **Índia · Manuscritos sânscritos · Pāli · Theravāda do sudeste asiático · Rota da Seda · Cânone chinês · Zona cultural dos caracteres chineses · Tibetano**. Cada ramo terá pelo menos uma "primeira amostra": texto-fonte de domínio público → esboço de tradução automática para um idioma atualmente sem tradução → revisor humano nomeado. O ramo tibetano já tem o primeiro ativo (DN 16); o ramo pāli também foi tocado pela mesma leitura em quatro idiomas do DN 16. Os seis ramos restantes (Índia, sânscrito, sudeste asiático, Rota da Seda, chinês, zona cultural dos caracteres chineses) estão abertos a colaboradores para inicialização.

## Camadas de proteção

Cada artefato é protegido por:

- **Espelho local** — macOS.
- **Repo público no GitHub** — https://github.com/lurongpan47/Sarasvati.
- **Espelhos geográficos AWS** — várias regiões.
- **Espelho descentralizado IPFS** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
- **OpenTimestamps → Bitcoin** — âncora temporal irrefutável em `manifests/SHA256SUMS`.

## ⚠️ Isenção de responsabilidade

Todas as traduções e textos traduzidos automaticamente neste repo são **rascunhos gerados por IA** aguardando revisão humana especializada. Não os trate como autoritativos para propósitos rituais, doutrinários, médicos ou acadêmicos sem validação por especialistas nomeados.

## Como contribuir

- Abra uma issue propondo um texto, uma revisão de capítulo, uma correção terminológica ou uma revisão da carta em algum idioma.
- Fork, edite, PR. Todas as contribuições são aceitas sob CC BY-SA 4.0.
- Execute um espelho. Ajude a preservar o arquivo.
- Ajude a construir o **runtime da carta** (bibliotecas guardrail Python + TypeScript) — veja `CALL-FOR-HELP.md`.

## Links

- GitHub: https://github.com/lurongpan47/Sarasvati
- Licença: CC BY-SA 4.0

---

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*Todas as coisas condicionadas são impermanentes. Esforcem-se com diligência.*
