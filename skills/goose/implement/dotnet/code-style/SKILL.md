---
name: code-style
description: Use when writing or reviewing C# style — nullable, records, var, naming, EditorConfig/analyzers — or when implement loads the dotnet pack for style work.
metadata:
  area: goose
---

# Code Style

Goose handbook for C# house style. **Target repo wins** if `.editorconfig` / analyzers already disagree — follow the repo.

Voice: **`write-like-goose`**.

Deeper protection (architecture tests, mutation) → **`testing`**. Auth/trust → **`security`**.

## When to use

- Style debates; new files; analyzer/editorconfig changes
- **`implement`** loading this pack

## Language

| Topic | Rule |
|-------|------|
| Collections | Prefer **collection expressions**: `[]`, `[x]`, `[..items]` over `Array.Empty<T>()` / `new List<T>()` when applicable |
| Nullable | **Enabled**; nullable warnings **fail CI** (warnings-as-errors for nullable / practical WAE). Don’t disable project-wide without a written reason |
| Namespaces | **File-scoped** for new files |
| Records vs classes | **`record`** for DTOs / immutable payloads; **`class`** for entities with identity. **Classic property declarations** — not positional `record Foo(string Bar)` |
| Primary constructors | **Don’t use** — classic constructor bodies |
| `var` | **Prefer `var`** by default |
| Async names | Public async methods end with **`Async`** |
| Private fields | **`_camelCase`** |
| Interfaces | **`I` prefix** (`IClock`) |

## Tooling

- Repo **`.editorconfig`**
- **`dotnet format`** (or IDE equivalent) clean on **CI**
- SDK / nullable analyzers on; don’t `#pragma` suppress without a short reason
- Extra packs (Roslynator, StyleCop, …) optional per repo — not required Goose-wide
- Optional later: BannedApi analyzer for `DateTime.Now` / `new HttpClient()` — not mandatory yet

## Don't

- Don’t disable nullable for a whole project without a reason on record
- Don’t introduce positional records or primary constructors as the house style
- Don’t fight CI format/analyzers with one-off local settings
- Don’t skip `Async` on public async APIs

## References

- [`references/examples.md`](references/examples.md) — preferred shapes

## Related

- Test naming / mutation → **`testing`**
- Solution-wide build props → **`solution-structure`**
