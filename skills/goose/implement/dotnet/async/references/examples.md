# Async sketches

## Token through the use case

```csharp
public interface ICreateCustomerRequestHandler
{
    Task<Result<CreateCustomerResponse>> Handle(
        CreateCustomerRequest request,
        CancellationToken cancellationToken);
}

// endpoint
app.MapPost("/customers", async (
    CreateCustomerRequest body,
    ICreateCustomerRequestHandler handler,
    CancellationToken ct) =>
{
    var result = await handler.Handle(body, ct);
    return ToHttp(result);
});
```

## Bounded fan-out (no shared DbContext)

```csharp
async Task<IReadOnlyList<Quote>> FetchQuotes(
    IEnumerable<string> symbols,
    IHttpClientFactory httpClientFactory,
    CancellationToken ct)
{
    const int maxConcurrent = 8;
    using var gate = new SemaphoreSlim(maxConcurrent);
    var tasks = symbols.Select(async symbol =>
    {
        await gate.WaitAsync(ct);
        try
        {
            var client = httpClientFactory.CreateClient("quotes");
            // each call is independent — not a scoped DbContext
            return await client.GetFromJsonAsync<Quote>($"/{symbol}", ct);
        }
        finally
        {
            gate.Release();
        }
    });

    var results = await Task.WhenAll(tasks);
    return results.Where(r => r is not null).Cast<Quote>().ToList();
}
```

For EF work in parallel, create a **new scope** (and thus a new `DbContext`) per task — or keep it sequential.

## Banned on the request path

```csharp
// don't
var x = handler.Handle(req).Result;
handler.Handle(req).Wait();
_ = SendEmailAsync(msg); // discarded — use background-work
```
