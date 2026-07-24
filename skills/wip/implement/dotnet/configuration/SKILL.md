---
name: configuration
description: Options pattern, secrets, environments, feature flags. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Configuration

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New settings, secrets wiring, or feature flags.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Sources
- appsettings hierarchy; env vars; secret stores we use
- Never commit secrets

### Options pattern
- Named options; validation at startup; reload semantics

### Feature flags
- Library/process; default-off for risky paths

### Environments
- Dev/Staging/Prod differences we allow

### Align with
- security (secrets), dependency-injection (IOptions lifetimes)

## Don't
- Don't read raw `IConfiguration["Secret"]` scattered in code — bind options.
- Don't ship with Development settings in Production.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
