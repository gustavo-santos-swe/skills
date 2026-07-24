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

## Next

Self-review the branch diff here (or as the first step of **pr-raise**), then **git-practices** → **pr-raise**.
