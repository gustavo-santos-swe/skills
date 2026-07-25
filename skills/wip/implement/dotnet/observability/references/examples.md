# Observability examples

## Packages (non-Aspire host)

```bash
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Instrumentation.Http
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
# optional: OpenTelemetry.Instrumentation.EntityFrameworkCore
# optional: OpenTelemetry.Instrumentation.Runtime
```

## Host wiring sketch (when Aspire ServiceDefaults isn’t already doing this)

```csharp
builder.Services.AddOpenTelemetry()
    .ConfigureResource(r => r.AddService(builder.Environment.ApplicationName))
    .WithTracing(t => t
        .AddAspNetCoreInstrumentation(o =>
        {
            o.Filter = ctx =>
                !ctx.Request.Path.StartsWithSegments("/alive")
                && !ctx.Request.Path.StartsWithSegments("/health");
        })
        .AddHttpClientInstrumentation()
        .AddSource("Goose.Billing")) // must match ActivitySource name
    .WithMetrics(m => m
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddMeter("Goose.Billing"))
    .WithLogging(l => l.IncludeScopes = true)
    .UseOtlpExporter(); // OTEL_EXPORTER_OTLP_ENDPOINT — 4317 gRPC / 4318 HTTP
```

Prefer Aspire `AddServiceDefaults()` when the AppHost already owns this shape.

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

## Custom span (only when needed)

```csharp
private static readonly ActivitySource ActivitySource = new("Goose.Billing");

using var activity = ActivitySource.StartActivity("ReconcileInstallments");
activity?.SetTag("card.id", cardId.ToString());

// work…

activity?.SetStatus(ActivityStatusCode.Ok);
```

`ActivitySource` name **must** match `.AddSource("Goose.Billing")` or `StartActivity` returns null.

Custom metrics: create meters with `IMeterFactory`, register the name with `.AddMeter(...)`.

## What not to log

```csharp
// Bad
_logger.LogDebug("Webhook body: {Body}", rawBody);
_logger.LogInformation("Login for {Email} password={Password}", email, password);

// Good
_logger.LogInformation("Processed webhook {EventId} for connection {ConnectionId}", eventId, connectionId);
```
