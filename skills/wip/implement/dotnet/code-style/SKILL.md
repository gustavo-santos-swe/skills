---
name: code-style
description: Nullable, analyzers, records, file-scoped namespaces, team C# style. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Code Style

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Style debates or analyzer/editorconfig changes.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Language
- Nullable reference types required?
- Records vs classes — when
- File-scoped namespaces; primary constructors

### Analyzers
- Which packs (StyleCop, Roslynator, custom); warnings-as-errors

### Naming
- Async suffix; interfaces; private fields

### Formatting
- EditorConfig / dotnet format — CI gate?

## Don't
- Don't disable nullable for a whole project without ADR.
- Don't fight the analyzer with pragmas unless documented.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
