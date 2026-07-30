# Contributing

The Oto projects are open source under the [MIT licence](LICENSE). Contributions
are welcome.

## Licence and CLA

Two documents govern the code:

- **[LICENSE](LICENSE)** (MIT) — what *you* may do with the code. Almost
  everything: use it, modify it, ship it in a closed-source product, sell it.
  Keep the copyright notice.
- **[CLA.md](CLA.md)** — what happens to the code *you* write and submit. You
  keep your copyright; you grant a broad, sublicensable licence so the projects
  can keep distributing your work, including under different terms later.

The CLA is signed once and covers all your contributions across every
participating repository. A bot asks for it on your first pull request — reply
in the thread with the sentence it gives you and you are done.

If you contribute as part of your job, check §4 of the CLA: your employer may
own what you write, in which case you need their go-ahead (or a corporate CLA).

## Where things live

`oto` is the doctrine repository — architecture and decisions, not code. Code
lives in dedicated repositories:

| Repository | What it is |
| --- | --- |
| [`oto-core`](https://github.com/otomata-tech/oto-core) | Connector library — API clients for agents, no CLI |
| [`oto-cli`](https://github.com/otomata-tech/oto-cli) | `oto` command-line façade over oto-core |
| [`oto-backend`](https://github.com/otomata-tech/oto-backend) | The backend: credential vault, orgs, MCP + REST faces |
| [`oto-dashboard`](https://github.com/otomata-tech/oto-dashboard) | Product dashboard (Vue 3) |
| [`oto-plugin`](https://github.com/otomata-tech/oto-plugin) | Claude Code plugin |
| [`otomata-mcp`](https://github.com/otomata-tech/otomata-mcp) | Shared foundation for MCP servers |
| [`france-opendata`](https://github.com/otomata-tech/france-opendata) | French public-data connectors |
| [`o-browser`](https://github.com/otomata-tech/o-browser) | Browser automation client |

Open the pull request on the repository that owns the code, not here.

## Before you open a pull request

- Read the architecture overview in [`docs/architecture.md`](docs/architecture.md).
  The projects are composable packages, not a monorepo — a change that spans two
  repositories usually means the seam is in the wrong place.
- Keep the existing conventions of the file you are editing.
- Run the repository's own test suite. Each repository documents its own setup.
- One concern per pull request.

## Reporting a security issue

Do not open a public issue. Write to
[alexis@otomata.tech](mailto:alexis@otomata.tech).
