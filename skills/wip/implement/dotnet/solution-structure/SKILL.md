---
name: solution-structure
description: Solution layout, project boundaries, Directory.Build.props, how packages reference each other. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Solution Structure

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Changing project graph, adding a host, or debating where code lives.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Layout
- Project names, folders, one-deployable vs many
- Where Domain / Application / Infrastructure / Hosts live
- Test project pairing (mirrors production?)

### Boundaries
- What may reference what (dependency rule)
- Shared Kernel vs duplication — our rule
- Public surface of each project (no leaking Internals casually)

### Build / repo mechanics
- Directory.Build.props / targets — what we centralize
- Package versions (Central Package Management?)
- Analyzers / treat warnings as errors — where enforced

### Multi-host
- API vs worker vs migrations host — how we split

## Don't
- Don't invent a new layer for one file.
- Don't reverse the dependency rule just this once.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
