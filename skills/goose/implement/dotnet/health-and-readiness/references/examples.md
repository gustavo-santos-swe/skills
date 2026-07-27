# Health and readiness sketches

## Aspire-shaped mapping

```csharp
app.MapHealthChecks("/health"); // readiness: all checks

app.MapHealthChecks("/alive", new HealthCheckOptions
{
    Predicate = r => r.Tags.Contains("live"),
});
```

```csharp
builder.Services.AddHealthChecks()
    .AddCheck("self", () => HealthCheckResult.Healthy(), tags: ["live"])
    .AddNpgSql(connectionString, name: "postgres", timeout: TimeSpan.FromSeconds(2))
    .AddRedis(redisConnection, name: "redis", timeout: TimeSpan.FromSeconds(2));
```

## PR / implement callout (copy when relevant)

```text
Health exposure: /health returns per-dependency detail and is anonymous.
Confirm before merge: cluster-internal only | probe key | status-only on public ingress.
Never include connection strings or secrets in the payload.
```
