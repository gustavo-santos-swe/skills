---
name: async
description: Use when writing or reviewing async/await, cancellation, parallelism, or sync-over-async traps in .NET — or when implement loads the dotnet pack for async code.
disable-model-invocation: true
metadata:
  area: wip
---

# Async

Goose handbook for async correctness in backends. **Target repo wins** if it already has a documented async policy.

Voice: **`write-like-goose`**.

## When to use

- New I/O, timeouts, fan-out, or “why is this deadlocking?”
- **`implement`** loading this pack

## Defaults

- **Async all the way** for I/O: handlers, ports, EF, HTTP clients
- **Always flow `CancellationToken`** on those paths; endpoints pass the request token (minimal APIs: `CancellationToken` parameter / `RequestAborted`)
- Prefer returning **`Task` / `Task<T>`**. Use **`ValueTask`** only on measured hot paths that often complete synchronously — not as a default API style

## No sync-over-async

On the request path (Api / Application / Infrastructure serving requests):

- No `.Result`, `.Wait()`, `.GetAwaiter().GetResult()`
- No async work in constructors or sync DI factory methods
- No `async void` (we don’t use UI-style event handlers here)

If something must run after the HTTP response, use **`background-work`** or **`messaging`** — don’t discard tasks in the handler (`_ = DoAsync()`).

## ConfigureAwait

In Api / Application / Infrastructure for ASP.NET: **omit** `ConfigureAwait` (default is fine).

Use `ConfigureAwait(false)` only in reusable library code that must not capture a synchronization context. Don’t spray it on every await “for performance.”

## Parallelism

Concurrent I/O is OK when it helps:

- Bound concurrency (`SemaphoreSlim`, chunked `Task.WhenAll`, `Parallel.ForEachAsync` with `MaxDegreeOfParallelism`)
- **Never** use one `DbContext` (or other non-thread-safe scoped service) from multiple tasks at once — one context per task/scope, or stay sequential
- Unbounded `WhenAll` over a large list is a smell (pool / upstream overload)

## Traps checklist

| Trap | Do instead |
|------|------------|
| Block on async in a request | `await` |
| Fire-and-forget in a handler | Hosted service / queue / outbox |
| Parallel + shared DbContext | Sequential, or new scope per task |
| Missing cancellation | Pass the token through |
| `async void` | `async Task` |

## Don't

- Don’t block the request thread on async work
- Don’t invent fire-and-forget without an explicit host pattern
- Don’t share EF contexts across parallel awaits
- Don’t default every method to `ValueTask`
- Don’t add `ConfigureAwait(false)` on every line of app code

## References

- [`references/examples.md`](references/examples.md) — token flow, bounded fan-out

## Related

- Handlers → **`application-layer`**
- EF / DbContext lifetime → **`db-integration`**
- Outbound HTTP → **`http-clients`**
- Jobs after the request → **`background-work`**
- Retries / timeouts → **`resilience`**
