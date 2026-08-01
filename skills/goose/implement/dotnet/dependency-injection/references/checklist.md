| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Never inject a scoped service into a singleton (captive dependency) | regression-test | Lifetimes — `BuildServiceProvider(validateScopes: true, validateOnBuild: true)` throws at container build |
| Handlers default to scoped (one instance per request scope) | verify | Lifetimes |
| Composition root (`Program.cs`) stays thin: `AddApplication()` / `AddInfrastructure()` split into submethods per concern | verify | Registration shape |
| Don't dump every registration into one giant method or leave all wiring only in `Program.cs` once the host grows | verify | Registration shape |
| Prefer typed HttpClients (`AddHttpClient<TClient>()`) over `IHttpClientFactory` sprinkled through Application | verify | Typed HttpClients |
| Bind options to typed classes with `ValidateDataAnnotations()` + `ValidateOnStart()` — fail at boot, not on first request | regression-test | Options — build the host with a bad options section, assert it throws |
| Constructor injection in Application/Infrastructure; ban resolving from `IServiceProvider`/`GetRequiredService` in normal app code | architecture-test | Resolution rules — reflection over constructor parameter types across Application/Infrastructure |
| Ban `BuildServiceProvider()` inside `Add*` registration methods | analyzer | Resolution rules — ASP0000 (SDK-shipped analyzer) |
| Don't introduce static service locators "to make tests easier" | verify | Testing |
| Don't leave options unbound/unvalidated until runtime | verify | Don't |
