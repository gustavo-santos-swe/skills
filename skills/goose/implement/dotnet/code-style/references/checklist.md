| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Prefer collection expressions (`[]`, `[x]`, `[..items]`) over `Array.Empty<T>()` / `new List<T>()` when applicable | editorconfig | Language — IDE0300-IDE0305 |
| `var` preferred by default | editorconfig | Language — `csharp_style_var_*` |
| File-scoped namespaces for new files | editorconfig | Language — `csharp_style_namespace_declarations` |
| `record` for DTOs / immutable payloads; `class` for entities with identity | verify | Language — needs per-type identity judgment |
| Classic property declarations — not positional `record Foo(string Bar)` | analyzer | Language — no off-the-shelf ban once written; IDE0290 only suggests adding a primary constructor, the opposite direction; needs a small custom Roslyn analyzer to be fully deterministic |
| Don't use primary constructors as the house style | analyzer | Don't — same tooling gap as above |
| Private fields `_camelCase` | editorconfig | Language — `dotnet_naming_rule` |
| Interfaces use `I` prefix (`IClock`) | editorconfig | Language — `dotnet_naming_rule` |
| Nullable enabled; nullable warnings fail CI (warnings-as-errors) | editorconfig | Tooling — project-level switch + compiler, `TreatWarningsAsErrors` |
| Don't disable nullable project-wide without a reason on record | verify | Tooling |
| `dotnet format` (or IDE equivalent) clean on CI | editorconfig | Tooling — IDE0055 |
| SDK / nullable analyzers on; don't `#pragma` suppress without a short reason | editorconfig | Tooling — IDE0079 |
| Don't fight CI format/analyzers with one-off local settings | verify | Don't |
| Don't skip `Async` on public async APIs | analyzer | Don't — VSTHRD200, see `async` skill |
