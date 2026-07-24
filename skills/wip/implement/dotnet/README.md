# dotnet

C# / .NET stack conventions for Goose’s backends. Lives under **`implement`** — process is the parent skill; this pack is *how we write .NET*.

Path: `skills/wip/implement/dotnet/`. Load from **`implement`** (or by name) when the change touches that concern. Prefer progressive disclosure: keep `SKILL.md` short; put deep examples in `references/`.

Each skill is still a **stub**: `Topics to fill` lists decisions Goose should define later (conventions, defaults, Don'ts). Schema/SQL stays in [`../database/`](../database/).

## Map

### Core
| Skill | Focus |
|-------|--------|
| [`solution-structure`](./solution-structure/) | Repo/project layout |
| [`domain-modeling`](./domain-modeling/) | Domain in C# |
| [`application-layer`](./application-layer/) | Use cases / handlers |
| [`time-and-ids`](./time-and-ids/) | Clocks, UTC, ID generation |
| [`async`](./async/) | Async correctness |
| [`db-integration`](./db-integration/) | Persistence (.NET); schema rules → [`../database/`](../database/) |
| [`endpoint-conventions`](./endpoint-conventions/) | HTTP API surface |
| [`dependency-injection`](./dependency-injection/) | DI lifetimes |
| [`validation`](./validation/) | Input/domain validation |
| [`error-handling`](./error-handling/) | Errors → HTTP/results |
| [`testing`](./testing/) | Tests for .NET |

### Production
| Skill | Focus |
|-------|--------|
| [`observability`](./observability/) | Traces, metrics, structured logs |
| [`health-and-readiness`](./health-and-readiness/) | Probes / health checks |
| [`configuration`](./configuration/) | Options, secrets, flags |
| [`resilience`](./resilience/) | Timeouts, retries, idempotency |
| [`security`](./security/) | AuthN/Z, secrets (.NET) |
| [`serialization`](./serialization/) | JSON / contracts wire format |
| [`localization`](./localization/) | Cultures, resources, locale formatting |

### Boundaries
| Skill | Focus |
|-------|--------|
| [`api-contracts`](./api-contracts/) | OpenAPI, versioning |
| [`rate-limiting`](./rate-limiting/) | Throttles / 429 policy |
| [`messaging`](./messaging/) | Async messaging |
| [`caching`](./caching/) | Cache patterns |
| [`file-storage`](./file-storage/) | Uploads, blobs, streaming |
| [`background-work`](./background-work/) | Hosted services / jobs |
| [`http-clients`](./http-clients/) | Outbound HTTP |

### Quality
| Skill | Focus |
|-------|--------|
| [`code-style`](./code-style/) | C# style & analyzers |
| [`performance`](./performance/) | Hot-path perf |
| [`migrations-and-compat`](./migrations-and-compat/) | Schema/API evolution |

Out of scope here: multi-tenancy, Blazor/MAUI (add later if needed).
