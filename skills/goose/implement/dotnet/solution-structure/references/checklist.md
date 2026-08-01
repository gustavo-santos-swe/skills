| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Domain has no outward references to Application, Infrastructure, or Api | architecture-test | Dependency rule — `AppLayerTests.Domain_ShouldNotDependOn_*` |
| Application references Domain and abstractions (ports) only; it does not reference Infrastructure projects | architecture-test | Dependency rule — `AppLayerTests.Application_ShouldNotDependOn_Infrastructure` |
| Every Domain repository interface has exactly one implementation, in `Infrastructure.Persistence.Repositories` | architecture-test | Ports (by kind) — `RepositoryPortAdapterTests` |
| Infrastructure implements ports; registered in the host | verify | Dependency rule |
| Organize Application by feature, not by type buckets (`Commands/`, `Handlers/`) | verify | Naming and folders |
| Domain objects are type-oriented (`Entities/`, `ValueObjects/`, `Enums/`), reused across features | verify | Naming and folders |
| Don't invent a new top-level layer for one type | verify | Don't |
| Separate verticals when audiences differ (e.g. App vs Admin), not for every new screen | verify | Verticals and hosts |
| Default one Infrastructure project; split only when a slice is fat or has a different lifecycle | verify | Infrastructure splits |
| Don't split Infrastructure preemptively for one adapter | verify | Infrastructure splits |
| Prefer duplication across verticals until it hurts (third copy or ownership fight) before extracting shared code | verify | Shared code across verticals |
| Don't reverse the dependency rule "just this once" | architecture-test | Don't — same `AppLayerTests` suite |
| Don't put Stripe/email ports in Domain | verify | Don't |
| Don't create a SharedKernel project on day one | verify | Don't |
