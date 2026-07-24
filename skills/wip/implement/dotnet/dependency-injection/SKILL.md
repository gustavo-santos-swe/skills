---
name: dependency-injection
description: Lifetimes, captive dependencies, options pattern, factory registration. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Dependency Injection

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New services, lifetime bugs, or composition root changes.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Lifetimes
- Singleton / Scoped / Transient — cheatsheet for our types
- Captive dependency checklist (singleton → scoped = ban)

### Registration
- Extension methods per assembly? Scrutor scanning?
- Where composition root lives per host

### Options
- `IOptions` / `IOptionsMonitor` / `IOptionsSnapshot` — when each
- Validating options at startup

### Factories
- Typed HttpClient, DbContext pooling — registration patterns

### Testability
- What we replace in tests; avoid static service locators

## Don't
- Don't resolve scoped services from singletons.
- Don't call `BuildServiceProvider()` inside registration.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
