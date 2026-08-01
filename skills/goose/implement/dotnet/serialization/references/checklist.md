| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| System.Text.Json for HTTP APIs; Newtonsoft only when a library forces it (e.g. Hangfire) | verify | Defaults |
| Wire JSON uses camelCase names and string enums (`JsonStringEnumConverter`) | regression-test | Defaults — serialize a sample DTO in a test, assert the JSON shape |
| Configure serializer options once at the host — don't invent per-endpoint serializer settings | verify | Defaults |
| Serialize request/response DTOs only — never EF entities or graphs with navigation cycles | verify | What to serialize |
| Instants are NodaTime `Instant` as ISO-8601 UTC on the wire; calendar dates are `LocalDate`, not a midnight `DateTime` | verify | Types |
| Money is `decimal` (+ currency code when multi-currency); never `double` | analyzer | Types — banned-type analyzer on property/param type |
| Polymorphism only when the contract needs it, with an explicit discriminator documented in OpenAPI | verify | Types |
| Don't silently change enum or date formats on a shipped public API | verify | Don't |
| Don't use numeric enums on public APIs without an explicit migration | verify | Don't |
| Don't change camelCase / string-enum defaults mid-flight without a version story | verify | Don't |
