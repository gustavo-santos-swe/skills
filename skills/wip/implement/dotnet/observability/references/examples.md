# Observability sketches

## Structured log + scope

```csharp
using (_logger.BeginScope(new Dictionary<string, object>
{
    ["UserId"] = userId,
    ["StatementId"] = statementId,
}))
{
    _logger.LogInformation("Settled statement {StatementId} for user {UserId}", statementId, userId);
}
```

## Custom span (only when needed) — OTel API

```csharp
using var activity = ActivitySource.StartActivity("ReconcileInstallments");
activity?.SetTag("card.id", cardId.ToString());

// work…

activity?.SetStatus(ActivityStatusCode.Ok);
```

Prefer the OpenTelemetry Tracer/shim style your host already uses; keep attribute names low-cardinality and PII-free.

## What not to log

```csharp
// Bad
_logger.LogDebug("Webhook body: {Body}", rawBody);
_logger.LogInformation("Login for {Email} password={Password}", email, password);

// Good
_logger.LogInformation("Processed webhook {EventId} for connection {ConnectionId}", eventId, connectionId);
```
