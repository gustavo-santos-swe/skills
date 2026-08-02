| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Use `async`/`await` all the way for I/O (handlers, ports, EF, HTTP clients) | verify | Defaults |
| Always flow `CancellationToken` on I/O paths; endpoints pass the request token | analyzer | Defaults — CA2016 (built-in Roslyn analyzer) |
| Prefer `Task`/`Task<T>`; use `ValueTask` only on measured hot paths, not as a default API style | verify | Defaults |
| Public async methods end with `Async` | analyzer | No sync-over-async — VSTHRD200 (requires `Microsoft.VisualStudio.Threading.Analyzers`) |
| Don't use `async void` | analyzer | No sync-over-async — VSTHRD100 |
| Don't use `.Result` / `.Wait()` / `.GetAwaiter().GetResult()` on the request path | analyzer | No sync-over-async — VSTHRD002/103 |
| Don't do async work in constructors or sync DI factory methods | verify | No sync-over-async |
| Don't discard tasks in the handler (`_ = DoAsync()`); use `background-work` / `messaging` for post-response work | verify | No sync-over-async |
| `ConfigureAwait` per repo convention (omit in Api/Application/Infrastructure for ASP.NET; `ConfigureAwait(false)` only in reusable library code) | analyzer | ConfigureAwait — CA2007/VSTHRD111 |
| Don't spray `ConfigureAwait(false)` on every await "for performance" | verify | ConfigureAwait |
| Bound concurrency for concurrent I/O (`SemaphoreSlim`, chunked `Task.WhenAll`, `Parallel.ForEachAsync` with `MaxDegreeOfParallelism`) | verify | Parallelism |
| Never use one `DbContext` (or other non-thread-safe scoped service) from multiple tasks at once | verify | Parallelism |
| Don't run unbounded `WhenAll` over a large list | verify | Parallelism |
