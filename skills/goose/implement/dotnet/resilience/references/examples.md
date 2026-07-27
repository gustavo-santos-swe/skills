# Resilience sketches

## Standard handler on a typed client

```csharp
builder.Services.AddHttpClient<IOpeniClient, OpeniClient>(/* … */)
    .AddStandardResilienceHandler(); // or AddStandardResilienceHandler(o => { … per-client tune })
```

## Idempotency for a mutating call

```csharp
// Prefer natural key / Idempotency-Key header the vendor understands
request.Headers.TryAddWithoutValidation("Idempotency-Key", commandId.ToString());
await _http.SendAsync(request, cancellationToken);
```

Don’t enable retries on that client for POST unless the key (or API contract) makes duplicates safe.
