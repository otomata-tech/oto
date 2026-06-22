# oto

**Oto** is a B2B automation toolkit for AI agents: a platform of **connectors** and
**processes** exposed both over **MCP** (Model Context Protocol) and **REST**,
multi-tenant and multi-LLM. You wire your tools (company data, CRM, email,
messaging, knowledge base…) once, and any agent (Claude and others) can use them.

This repository is the platform's **public entry point**. It does not contain the
product itself but its **architecture doctrine**: the structuring decisions (ADRs)
and an overview. The code lives in dedicated repositories (see *Repositories*).

## Overview

[`docs/architecture.md`](docs/architecture.md) — the diagram and the narrative: a
**central backend** with two faces (MCP + REST), an **encrypted credential vault**,
**connectors** to third-party systems, and **adapters** that project a single
declaration onto both surfaces. The backend is the center; no façade holds a secret.

## Repositories

Oto is **not a monorepo** — it is a constellation of independently versioned repos
(see ADR [0005](docs/adr/0005-platform-composition.md)). The reusable substrate is
open source; the product repositories are private.

### Open-source building blocks

The reusable core of the platform is published independently and can be consumed
on its own:

| Repo | Role |
|---|---|
| [oto-core](https://github.com/otomata-tech/oto-core) | Connector library (`oto.tools` namespace + config/secrets). Single source of the connector clients, consumed by both the CLI and the backend. |
| [oto-cli](https://github.com/otomata-tech/oto-cli) | `oto` — Typer CLI façade over oto-core (humans and local agents). |
| [oto-plugin](https://github.com/otomata-tech/oto-plugin) | Claude Code plugin: auto-configured MCP connector + a universal skill. Third-party onboarding entry point. |
| [france-opendata](https://github.com/otomata-tech/france-opendata) | French public-data clients (Recherche Entreprises, SIRENE, INPI, BODACC, DVF) + SIRENE stock over DuckDB/parquet. |
| [otomata-calllog](https://github.com/otomata-tech/otomata-calllog) | Normalized MCP tool-call journal — FastMCP middleware + pluggable sinks, canonical `tool_calls` schema shared across every Otomata MCP server. |
| [o-browser](https://github.com/otomata-tech/o-browser) | Browser-automation client (Patchright + remote CDP sessions). |
| [scout](https://github.com/otomata-tech/scout) | White-label Vue 3 + Fastify shell for lead-enrichment platforms (mission-driven theming, generic OAuth/cache/Logto helpers). |
| [memento](https://github.com/otomata-tech/memento) | Structured, sourced, living knowledge substrate for AI agents over MCP (Apache-2.0, hosted at mento.cc). |

### Product repositories

The platform itself. The **core product — backend and dashboard — is open source**;
the rest stays private. Listed here so the architecture maps onto real repos.

| Repo | Visibility | Role |
|---|---|---|
| [oto-backend](https://github.com/otomata-tech/oto-backend) | public | **The backend** — encrypted credential vault, orgs, doctrine, monitoring. Two faces: MCP (`mcp.oto.ninja/mcp`) + REST (`/api/*`). Imports `oto.tools` from oto-core. The center of the architecture. |
| [oto-dashboard](https://github.com/otomata-tech/oto-dashboard) | public | Product dashboard for the backend (Vue 3 + shadcn-vue + Tailwind, Logto PKCE). Has no server of its own — the backend is oto-backend. |
| `oto-websites` | private | Sites monorepo: marketing (oto.ninja), scout vitrine, otomata.tech / oto.zone / mento.cc, the Oto Companion extension, and the `@otomata/ui` design system. |
| `academy` | private | Academy product (change-management / AI adoption) — public best-practices knowledge base + gated accompaniment. Live at academy.otomata.tech. |
| `client-backoffice-bridge` | private | Reference **remote connector** (bridge, ADR [0003](docs/adr/0003-remote-connector-bridge.md)): the client credential lives outside the platform. |
| `otomata-private` | private | Working meta-repo — cross-project index, issue tracker, and the ADR drafting copy mirrored into this public repo. |

## Architecture Decision Records (ADRs)

One decision per file in [`docs/adr/`](docs/adr/). Each ADR carries its context,
decision, and consequences. The authoritative status of each record is the
`Status:` field inside the ADR, not this index.

| # | Decision |
|---|---|
| [0001](docs/adr/0001-sirene-stock-served-via-mcp.md) | SIRENE stock served via DuckDB over parquet |
| [0002](docs/adr/0002-platform-dedicated-scaleway-box.md) | Dedicated platform server + vault encryption |
| [0003](docs/adr/0003-remote-connector-bridge.md) | Remote connector (bridge): client code and credential kept off-platform |
| [0004](docs/adr/0004-layered-reversible-topology.md) | Layered architecture with reversible topology |
| [0005](docs/adr/0005-platform-composition.md) | Platform composition: composable packages, not a monorepo |
| [0006](docs/adr/0006-harnais-vs-substrat.md) | Harness vs substrate: a harness consumes the platform by contract |
| [0007](docs/adr/0007-dashboard-repo-separe.md) | Dashboard = separate product repo |
| [0008](docs/adr/0008-scout-dans-oto-substrat-factgraph.md) | Generic "structured fact graph" substrate |
| [0009](docs/adr/0009-couche-capacite.md) | Capability layer: authz, schema, and surfaces declared once |
| [0010](docs/adr/0010-providers-vs-capabilities-factory-connecteurs.md) | Providers vs capabilities: the connector factory |
| [0011](docs/adr/0011-organisation-connecteurs-outils-projections.md) | Connectors & tools layout: spine vs connectors, activation = visibility |
| [0012](docs/adr/0012-groupes-hierarchie-droits.md) | Groups (departments) & unified rights hierarchy |
| [0013](docs/adr/0013-acces-plateforme-invitation-virale.md) | Platform access & viral invitation: soft gate + quota referral |
| [0014](docs/adr/0014-doctrine-objet-structure-refs-outils.md) | Doctrine = structured object with resolved tool references |
| [0015](docs/adr/0015-identite-par-org.md) | Per-org identity: tool visibility scoped by (user, org) |
| [0016](docs/adr/0016-datastore-spine-natif-pg.md) | Datastore = native PostgreSQL spine |
| [0017](docs/adr/0017-boucle-usage-flux-evenements-session.md) | Usage loop: a stream of session events |
| [0018](docs/adr/0018-extraction-scout-repo-dedie.md) | Extraction of scout into a dedicated repo |
| [0019](docs/adr/0019-marketplace-connecteurs-selection.md) | Connector marketplace: "org proposes / member selects" |
| [0020](docs/adr/0020-strategie-release-canari-cohorte.md) | Release strategy: pinned versions, test gate, cohort canary (blue/green) |
| [0021](docs/adr/0021-procedures-et-executions.md) | Procedures (reusable) vs executions (instances) |

## Learn more

- Platform: **oto.ninja**
- Open-source building blocks: **oto.ninja/oss**
