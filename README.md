# oto

**Oto** est un toolkit d'automatisation B2B pour agents IA : une plateforme de **connecteurs** et de **process** exposés à la fois en **MCP** (Model Context Protocol) et en **REST**, multi-tenant et multi-LLM. On branche ses outils (données entreprise, CRM, email, messagerie, base de connaissance…) une fois, et n'importe quel agent (Claude, et autres) les utilise.

Ce dépôt est le **point d'entrée public** de la plateforme. Il ne contient pas le produit lui-même mais sa **doctrine d'architecture** : les décisions structurantes (ADRs) et une vue d'ensemble. Le code vit dans des dépôts dédiés (voir *Composants*).

## Vue d'ensemble

[`docs/architecture.md`](docs/architecture.md) — le schéma et le récit : un **backend central** à deux faces (MCP + REST), un **coffre de credentials chiffré**, des **connecteurs** vers les systèmes tiers, des **adaptateurs** qui projettent une déclaration unique sur les deux surfaces. Le backend est le centre ; aucune façade ne détient de secret.

## Décisions d'architecture (ADRs)

Une décision par fichier dans [`docs/adr/`](docs/adr/). Chaque ADR porte son contexte, sa décision et ses conséquences.

| # | Décision |
|---|---|
| [0001](docs/adr/0001-sirene-stock-served-via-mcp.md) | SIRENE stock servi via DuckDB sur parquet |
| [0002](docs/adr/0002-platform-dedicated-scaleway-box.md) | Serveur dédié pour la plateforme + chiffrement du coffre |
| [0003](docs/adr/0003-remote-connector-bridge.md) | Connecteur *remote* (bridge) : code et credential client hors plateforme |
| [0004](docs/adr/0004-layered-reversible-topology.md) | Architecture en couches à topologie réversible |
| [0005](docs/adr/0005-platform-composition.md) | Composition de la plateforme : packages composables, pas un monorepo |
| [0006](docs/adr/0006-harnais-vs-substrat.md) | Harnais vs substrat : un harnais consomme la plateforme par contrat |
| [0007](docs/adr/0007-dashboard-repo-separe.md) | Dashboard = repo produit séparé |
| [0008](docs/adr/0008-scout-dans-oto-substrat-factgraph.md) | Substrat « graphe de facts structurés » générique |
| [0009](docs/adr/0009-couche-capacite.md) | Couche capacité : autz, schéma et surfaces déclarés une seule fois |
| [0010](docs/adr/0010-providers-vs-capabilities-factory-connecteurs.md) | Providers vs capabilities : la factory de connecteurs |
| [0011](docs/adr/0011-organisation-connecteurs-outils-projections.md) | Organisation connecteurs & outils : spine vs connecteurs, activation = visibilité |
| [0012](docs/adr/0012-groupes-hierarchie-droits.md) | Groupes (départements) & hiérarchie de droits unifiée |
| [0013](docs/adr/0013-acces-plateforme-invitation-virale.md) | Accès plateforme & invitation virale : gate doux + referral à quota |
| [0014](docs/adr/0014-doctrine-objet-structure-refs-outils.md) | Doctrine = objet structuré à références d'outils résolues |
| [0015](docs/adr/0015-identite-par-org.md) | Identité par org : visibilité d'outils scopée par (user, org) |
| [0016](docs/adr/0016-datastore-spine-natif-pg.md) | Datastore = spine natif PostgreSQL |
| [0017](docs/adr/0017-boucle-usage-flux-evenements-session.md) | Boucle d'usage : un flux d'événements de session |
| [0018](docs/adr/0018-extraction-scout-repo-dedie.md) | Extraction de scout vers un repo dédié |

## Composants open source

Le socle réutilisable de la plateforme est publié indépendamment :

- [oto-core](https://github.com/otomata-tech/oto-core) — lib de connecteurs (`oto.tools`)
- [france-opendata](https://github.com/otomata-tech/france-opendata) — clients de données publiques françaises (SIRENE, INPI, BODACC, DVF…)
- [otomata-calllog](https://github.com/otomata-tech/otomata-calllog) — journal normalisé des appels d'outils MCP
- [o-browser](https://github.com/otomata-tech/o-browser) — automation de navigateur

## En savoir plus

- Plateforme : **oto.ninja**
- Socle open source : **stack.oto.ninja**
