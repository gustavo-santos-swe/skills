# Caching sketches

## HybridCache get-or-create

```csharp
public sealed class GetInsightsHandler(HybridCache cache, /* … */)
{
    public async Task<InsightsResponse> Handle(GetInsightsRequest request, CancellationToken ct)
    {
        var key = $"financial-insights:{request.UserId}:{request.Year}-{request.Month:00}";

        return await cache.GetOrCreateAsync(
            key,
            async cancel => await LoadFromSourceAsync(request, cancel),
            new HybridCacheEntryOptions
            {
                Expiration = TimeSpan.FromMinutes(10), // absolute — tune per feature
            },
            cancellationToken: ct);
    }
}
```

## Invalidate on write

```csharp
await _db.SaveChangesAsync(ct);
await _cache.RemoveAsync($"financial-insights:{userId}:{year}-{month:00}", ct);
```

Key must match the read path (including principal segments).
