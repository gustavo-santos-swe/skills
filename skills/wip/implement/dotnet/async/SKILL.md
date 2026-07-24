---
name: async
description: async/await, cancellation, sync-over-async traps, ConfigureAwait, ValueTask. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Async

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Any async I/O, deadlocks, or cancellation bugs.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Defaults
- Async all the way for I/O; no `.Result` / `.Wait()` on ASP.NET
- `CancellationToken` from the request — always flow it

### ConfigureAwait
- Library vs app code — our rule (usually false in libs, default in apps)

### ValueTask / channels
- When ValueTask is worth it; when it isn't

### Parallelism
- `Task.WhenAll` bounds; don't fan-out unbounded
- `Parallel.ForEachAsync` — when allowed

### Traps
- Sync-over-async in constructors / DI
- Async void (except event handlers we don't use)
- Capturing DbContext across threads

## Don't
- Don't block on async in request threads.
- Don't invent fire-and-forget without an explicit host pattern (see background-work).

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
