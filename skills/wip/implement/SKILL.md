---
name: implement
description: Build the work described by a ticket or small plan — TDD at agreed seams, stop at a reviewable branch.
disable-model-invocation: true
metadata:
  area: wip
---

# Implement

Status: **stub**.

Drive the build.

### Stack packs

- **Data / DB (language-agnostic):** [`database/`](./database/README.md) — schema, integrity, indexes, evolution.
- **.NET / C#:** [`dotnet/`](./dotnet/README.md) — including [`db-integration`](./dotnet/db-integration/) (EF/Dapper adapter).
- **React Native / Expo:** [`react-native/`](./react-native/README.md) — mobile UI, navigation, device APIs.
- **Frontend / Next.js:** [`frontend/`](./frontend/README.md) — App Router web tier.

Pick by concern — don’t load a whole pack. Persistence often needs **both** `database` + `dotnet/db-integration`.

## Voice (required)

Before calling the slice done, run **`write-like-goose`** on durable text you added:

- new/changed **code comments** and docstrings (why only; silence if obvious)
- ticket notes, plan scraps, or handoff lines left in the repo

Do not ship AI-shaped comments. Chat chatter in the session does not need the full catalog.

## Next

Self-review the branch diff here (or as the first step of **pr-raise**), then **git-practices** → **pr-raise**.
