---
name: testing
description: xUnit patterns, Testcontainers, fakes vs mocks, architecture tests. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Testing

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Writing or structuring .NET tests.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Pyramid
- Unit vs integration vs smoke — what we require per change type
- DAMP over DRY in tests — our stance

### Unit
- What we fake; avoid mocking EF DbSet if we ban it
- Clock/id abstractions

### Integration
- Testcontainers (Postgres/SQL Server); shared fixtures; isolation
- InMemory EF — allowed or forbidden

### Architecture tests
- NetArchTest / similar — rules we enforce

### Naming & structure
- Test project layout; method naming

### Align with
- TDD process skills (wip/obra); this skill = .NET mechanics

## Don't
- Don't ship features with only happy-path unit tests when I/O is the risk.
- Don't use production database for tests.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
