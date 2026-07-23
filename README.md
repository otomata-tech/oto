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

Oto is **not a monorepo** — it is a constellation of independently versioned repos.
The reusable substrate and the product core are open source; some repos stay private.

### Open-source building blocks

The reusable core of the platform is published independently and can be consumed
on its own:

| Repo | Role |
|---|---|
| [oto-core](https://github.com/otomata-tech/oto-core) | Connector library (`oto.tools` namespace + config/secrets). Single source of the connector clients, consumed by both the CLI and the backend. |
| [oto-cli](https://github.com/otomata-tech/oto-cli) | `oto` — Typer CLI façade over oto-core (humans and local agents). |
| [oto-plugin](https://github.com/otomata-tech/oto-plugin) | Claude Code plugin: auto-configured MCP connector + a universal skill. Third-party onboarding entry point. |
| [otomata-mcp](https://github.com/otomata-tech/otomata-mcp) | Common base for Otomata MCP servers — doctrines served as tools, runs, scoped RBAC, canonical tool-call logging. |
| [france-opendata](https://github.com/otomata-tech/france-opendata) | French public-data clients (Recherche Entreprises, SIRENE, INPI, BODACC, DVF) + SIRENE stock over DuckDB/parquet. |
| [o-browser](https://github.com/otomata-tech/o-browser) | Browser-automation client (Patchright + remote CDP sessions). |
| [oto-memento](https://github.com/otomata-tech/oto-memento) | Structured, sourced, living knowledge substrate for AI agents over MCP (Apache-2.0, hosted at mento.cc). |

### Product repositories

The platform itself. The **core product — backend and dashboard — is open source**;
the rest stays private. Listed here so the architecture maps onto real repos.

| Repo | Visibility | Role |
|---|---|---|
| [oto-backend](https://github.com/otomata-tech/oto-backend) | public | **The backend** — encrypted credential vault, orgs, doctrine, monitoring. Two faces: MCP (`mcp.oto.cx/mcp`) + REST (`/api/*`). Imports `oto.tools` from oto-core. The center of the architecture. |
| [oto-dashboard](https://github.com/otomata-tech/oto-dashboard) | public | Product dashboard for the backend (Vue 3 + shadcn-vue + Tailwind, Logto PKCE). Has no server of its own — the backend is oto-backend. |
| `oto-websites` | private | Sites monorepo: marketing (oto.cx), otomata.tech / oto.zone / mento.cc, the Oto Companion extension, and the `@otomata/ui` design system. |
| `academy` | private | Academy product (change-management / AI adoption) — public best-practices knowledge base + gated accompaniment. Live at academy.otomata.tech. |
| *client bridges* | private | Reference **remote connectors** (bridge pattern): per-client back-office services that hold the client credential off-platform — see [`architecture.md`](docs/architecture.md). |
| `oto-private` | private | Working meta-repo — cross-project index, issue tracker, ADRs. |

## Architecture decisions

The platform is shaped by a series of architecture decisions (ADRs). The enduring
ones are summarized in [`docs/architecture.md`](docs/architecture.md); the full
decision records are kept internally.

## Learn more

- Platform: **[oto.cx](https://oto.cx)**
- Open-source building blocks: **[oto.cx/oss](https://oto.cx/oss)**
