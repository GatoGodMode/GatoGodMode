# Joseph Edwards — GatoGodMode

**CTO. Builder of local-first tools for collectors and investors.**

I build software that moves on **signal, not noise** — replacing fragmented browser tabs, gut-feel pricing, and cloud-dependent services with unified, data-driven, privacy-first tooling that runs entirely on your own machine.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-josephedwardscto-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josephedwardscto/)
[![X](https://img.shields.io/badge/X-@GatoGodMode-000000?logo=x&logoColor=white)](https://x.com/GatoGodMode)
[![RawGraded](https://img.shields.io/badge/Web-rawgraded.com-1f6feb)](https://rawgraded.com)
[![TheMoun](https://img.shields.io/badge/Hardware-themoun.com-2ea44f)](https://themoun.com)

---

## Philosophy: Move on Signal, Not Noise

Most collector and investor workflows look like this: a dozen marketplace tabs, unverified "last sold" prices skewed by scalper noise, browser-tracked history, and decision fatigue — *buy or hold?* — answered by gut feeling.

Everything I build inverts that:

| | Traditional Norm | The Raw Approach |
|---|---|---|
| **Data Sourcing** | Manual, multi-tab search across isolated sites | Unified, automated multi-source capture |
| **Analysis** | Descriptive ("what happened") | Prescriptive — actionable decision signals |
| **Privacy** | Cloud-dependent, browser-tracked | 100% local processing, local APIs, your data stays on your machine |

---

## The Raw Ecosystem

Five projects, one pipeline: from physical capture, to local AI grading, to market intelligence.

```mermaid
flowchart LR
    Moun["TheMoun<br/>(physical capture station)"] --> RawGraded["RawGraded Studio<br/>(AI pre-grading)"]
    RawGraded --> Engine["RawEngine Local AI<br/>(on-device inference + grade math)"]
    Engine --> Investor["RawInvestor<br/>(TCG market signals)"]
    Investor --> Markets["RawMarkets<br/>(multi-asset terminal)"]
```

---

## RawEngine Local AI

> The privacy-first, on-device AI core powering the ecosystem.

**Problem:** AI grading and analysis tools typically mean uploading your collection to someone else's cloud — and trusting a black box that hallucinates grade numbers.

**How it works:** RawEngine deliberately separates *perception* from *judgment*:

1. **Vision stage (local LLM inference)** — a locally-run vision model performs phased evidence passes: OCR and card text extraction, identity resolution against TCG databases, qualitative centering notes, and defect cataloging across front, back, and video frames. It catalogs evidence; it never assigns grades.
2. **Deterministic math stage** — a rules-based engine computes every numeric subgrade and PSA/BGS/CGC prediction from the cataloged defects, risk factors, and *measured* centering. Grade snapping, floors/ceilings, and cross-company consistency are enforced in code, not guessed by a model.

**Architecture:** local inference runtime on loopback, with an optional bring-your-own-key cloud fallback for higher-accuracy passes. With local mode, **no card image ever leaves your PC**. Standard and Deep analysis modes trade speed for forensic depth. Output is treated as a research estimate — honest about being a tool, not an oracle.

---

## RawGraded Studio — [rawgraded.com](https://rawgraded.com)

> Know whether a card is worth grading *before* you pay grading fees.

**Problem:** Submitting a card to PSA/BGS/CGC costs real money per card with weeks of turnaround. Most collectors submit on hope and get burned by surface or centering issues they didn't catch.

**How it works:** A guided desktop pre-grading workflow:

**capture → crop → PSA-style centering measurement → optional 5-stage guided video forensics (tilted light, macro, back scan) → RawEngine evidence passes → deterministic grade math → certificate export → local portfolio**

**Architecture:** Windows desktop app (web-tech UI in a native shell) with a companion mobile capture app, a local database for portfolio/provenance, and pluggable AI providers (local-first, optional BYOK cloud). An optional hosted vault and public archive exist at rawgraded.com — but desktop grading requires no account at all.

**Highlights:** live sharpness and border-detection guidance, slab authenticity checking, fake-slab identification guide, printable certificates and social exports, per-card market refresh.

---

## RawInvestor

> A local-first TCG investing workstation: buy, hold, grade, or sell — with math, not vibes.

**Problem:** Deciding what to do with a raw card means juggling PriceCharting, TCGplayer, and eBay sold listings by hand, with no unified view, no grading expected-value math, and pricing distorted by scalper noise.

**How it works:** One workspace blends sold listings and market prices from all three major sources into per-card decision signals:

- **Market Bias** — synthesized Buy / Hold / Sell guidance from buyer-side and seller-side analytics
- **Trend** — regression slope, z-score vs. historical mean, day-over-day moves across **1 / 7 / 30 / 90-day windows**
- **Sales Strategy** — SELL/HOLD signals with fair, strategic, and pushed price targets per channel
- **Grading EV** — expected value across PSA 10 / 9 / fail branches (population-data-tuned probabilities), vs. a raw-flip projection with break-even pricing
- **90-day ROI forecast** — realistic / best / worst cases with trend clamping to avoid wild extrapolation on thin data

**Architecture:** desktop app with an embedded browser workspace, a **loopback-only local API**, and a local database as the authoritative portfolio store. An optional browser extension captures live marketplace context from your real sessions and posts it only to your own machine. No vendor cloud sync, no account, no tracking.

**Highlights:** Nebula 3D portfolio classification (Buy / Sell / Hold / Sleeper / Climber / Dud / NGMI), deal-hunting "Arsenal" targets, sealed product EV, themed share graphics, streamer mode.

---

## RawMarkets

> A personal markets terminal for metals, energy, and equities — local-first, with an AI copilot.

**Problem:** Self-directed investors juggle quote sites, news feeds, spreadsheets, and paid API keys just to see their own positions in context.

**How it works:** A phased bootstrap (hydrate → news → market → portfolio) pulls live quotes, metals spot prices, and RSS news into a local database, then layers analysis on top:

- **Portfolio discipline signals** — barbell drift detection, fractional Kelly caps, disposition checks, FOMO cooldowns, quarterly rebalance nudges, fragility alerts
- **News Bay** — watchlist-aware feed lanes with sentiment scoring and an in-app reader
- **Statements Analyzer** — import broker CSVs, classify transactions, reconcile into the portfolio
- **Local AI Copilot** — a locally-run model with retrieval context from *your* holdings, quotes, news, and research

**Architecture:** desktop terminal (web-tech UI + local API server + local database), with browser-automation-powered price feeds as the default — so live data works **without paid market APIs**. Cloud AI is optional; local AI and all portfolio data stay on-device. Full database export/import for backup and migration.

---

## TheMoun — [themoun.com](https://themoun.com) (Physical Product)

> An integrated capture workstation for cards, coins, and slabs. The bench is where margin leaks.

**Problem:** Sellers and graders assemble capture setups from unrelated SKUs — light tents, ring lights, tripods, centering templates — producing glare, inconsistent framing, and poor signal for downstream AI grading, image search, and marketplace comps.

**How it works:** One purpose-built imaging bench: a specimen deck, controlled task lighting, and repeatable phone-capture geometry, designed as a single system instead of a pile of accessories. Clean, consistent imagery feeds directly into the RawEngine AI layer.

**Product line (EPIC):** **E**co → **P**ro → **I**nvestor → **C**urator — from a mechanical-first static bench up to a sensor-driven, motion-controlled production station, with a future bulk-throughput line.

**Design highlights:** unified TCG + coin reference geometry via removable translucent guides, flippable mark-free deck inserts for clean AI/listing imagery, medical-grade silicone edge protection, and modular serviceability — replaceable wear parts instead of glued monoliths.

---

## Stack at a Glance

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-087EA4?logo=react&logoColor=white)
![Electron](https://img.shields.io/badge/Electron-47848F?logo=electron&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?logo=nodedotjs&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Ollama](https://img.shields.io/badge/Local%20LLM%20Inference-Ollama-000000?logo=ollama&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)

Local-first by default. Plugin-style architectures. Deterministic math where it matters, AI where it helps.

---

## Contact

- **LinkedIn:** [linkedin.com/in/josephedwardscto](https://www.linkedin.com/in/josephedwardscto/)
- **X:** [@GatoGodMode](https://x.com/GatoGodMode)
- **Web:** [rawgraded.com](https://rawgraded.com) · [themoun.com](https://themoun.com)
