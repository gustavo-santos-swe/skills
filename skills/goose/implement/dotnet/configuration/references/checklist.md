| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Bind into typed options at the composition root; no raw `IConfiguration` reads in Application/Domain | architecture-test | Sources — assembly-dependency ban on `Microsoft.Extensions.Configuration` in Application/Domain |
| Load order (later wins): appsettings.json → appsettings.\{Environment\}.json → env vars → user secrets/secret store → optional local `.env` | verify | Sources |
| Secrets, connection strings with passwords, and API keys are never committed | verify | Secrets — needs a dedicated secret-scanner (gitleaks/trufflehog), a different tool family than compiler/analyzer/arch-test/unit-test |
| Prefer a cloud secret store in prod when the platform supports it | verify | Secrets |
| Never log option instances wholesale; never put secrets in health JSON or span attributes | verify | Secrets |
| One options type per concern (`StripeOptions`, `OpeniOptions`, …) | verify | Options |
| Invalid options fail fast at startup (`ValidateDataAnnotations()` + `ValidateOnStart()`) | regression-test | Options — build the host with a bad options section, assert it throws |
| Risky feature-flag paths default off | verify | Feature flags |
| Don't ship Development-only sinks, verbose logging, or relaxed auth into Production | verify | Environments |
| Don't default a dangerous feature flag to on | verify | Don't |
| Don't duplicate options validation rules outside the options type / DI registration | verify | Don't |
