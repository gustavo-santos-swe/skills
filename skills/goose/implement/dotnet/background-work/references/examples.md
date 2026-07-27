# Background work sketches

## Enqueue from a handler (not Task.Run)

```csharp
// After successful save / decision
BackgroundJob.Enqueue<ICleanupOrphansJob>(j => j.RunAsync(CancellationToken.None));

return Results.Accepted(); // or 202/204 per endpoint conventions
```

```csharp
// Bad — lost on process exit, no retry dashboard
_ = Task.Run(() => CleanupAsync());
```

## Idempotent job body

```csharp
public async Task RunAsync(CancellationToken ct)
{
    // Safe if Hangfire runs this twice: natural key / "already done" check
    var orphans = await _db.Attachments.Where(a => a.IsOrphan).Take(100).ToListAsync(ct);
    foreach (var a in orphans)
    {
        await _storage.DeleteAsync(a.Key, ct);
        _db.Attachments.Remove(a);
    }
    await _db.SaveChangesAsync(ct);
}
```

## Hangfire outbox (atomic with EF)

```text
Same transaction:
  - business rows
  - OutboxJob { Type, Payload, CreatedAt }

Dispatcher (recurring Hangfire job or BackgroundService):
  - claim pending OutboxJob
  - BackgroundJob.Enqueue(...)
  - mark Dispatched

Never rely on: SaveChanges(); BackgroundJob.Enqueue(...); // dual-write
```

## Intent check

```text
Same app, deferred unit of work → Hangfire (this skill).
Other process must react to an event → messaging ports/bus.
Unclear → ask.
```
