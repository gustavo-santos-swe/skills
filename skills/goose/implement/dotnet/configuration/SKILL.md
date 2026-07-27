---
name: configuration
description: Use when adding or reviewing .NET configuration — appsettings hierarchy, env/secrets, typed options, feature toggles — or when implement loads the dotnet pack for config work.
disable-model-invocation: true
metadata:
  area: goose
---

# Configuration

Goose handbook for how settings and secrets enter a .NET host.

**Target repo wins** if sources or secret wiring are already settled.

Voice: **`write-like-goose`**.

Registration lifetimes and **`ValidateOnStart`** → **`dependency-injection`**. This skill owns **sources**, **secrets hygiene**, **environments**, and **flags**.

## When to use

- New settings sections, secret stores, env-specific config
- Feature toggles / gradual rollout knobs
- **`implement`** loading this pack

## Sources (greenfield)

Load order (later wins):

1. `appsettings.json`
2. `appsettings.{Environment}.json`
3. Environment variables
4. User secrets (Development) / secret store (Production)
5. Optional host-only **`.env`** for local runs (never commit; gitignore it)

Bind into **typed options** at the composition root. Don’t sprinkle `IConfiguration["Some:Key"]` through Application/handlers.

## Secrets

- Never commit secrets, connection strings with passwords, or API keys
- Prefer a cloud secret store in prod when the platform supports it
- Local: user secrets and/or `.env`
- Never log option instances wholesale; never put secrets in health JSON or span attributes (**`observability`**, **`health-and-readiness`**)

## Options

- One options type per concern (`StripeOptions`, `OpeniOptions`, …)
- Bind + validate at startup — see **`dependency-injection`** (`ValidateDataAnnotations` / `ValidateOnStart`)
- `IOptions<T>` for mostly static config; `IOptionsMonitor<T>` only when live reload is required

## Feature flags

- Start with **bool / small enum** on typed options for most toggles
- Risky paths **default off**
- Introduce a flag platform (OpenFeature, App Config, LaunchDarkly, …) only when you need remote flip, % rollout, or per-tenant gates
- Don’t invent a second config system beside options for every boolean

## Environments

- `Development` / `Staging` / `Production` (or the repo’s names) via `ASPNETCORE_ENVIRONMENT`
- Don’t ship Development-only sinks, verbose logging, or relaxed auth into Production
- Env-specific *values* live in env/secret store; keep committed appsettings free of real secrets

## Don't

- Don’t commit `.env`, user-secrets XML, or KeyVault dumps
- Don’t read raw configuration keys in Domain
- Don’t default a dangerous feature flag to on
- Don’t duplicate options validation rules outside the options type / DI registration

## References

- [`references/examples.md`](references/examples.md) — bind sketch + `.env` note

## Related

- Options lifetimes / ValidateOnStart → **`dependency-injection`**
- Secret exposure in telemetry → **`observability`** / **`security`**
