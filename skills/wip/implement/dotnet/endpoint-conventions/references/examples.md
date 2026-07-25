# Endpoint convention sketches

## Thin Minimal API group

```csharp
var v1 = app.MapGroup("/api/v1")
    .RequireAuthorization();

var customers = v1.MapGroup("/customers");

customers.MapPost("/", async (
    CreateCustomerRequest body,
    ICreateCustomerRequestHandler handler,
    LinkGenerator links,
    HttpContext http,
    CancellationToken ct) =>
{
    var result = await handler.Handle(body, ct);
    return result switch
    {
        Ok<CreateCustomerResponse> ok =>
            Results.Created(
                links.GetUriByName(http, "GetCustomer", new { id = ok.Value.Id })!,
                ok.Value),
        var failure => ToHttp(failure) // shared Problem Details mapper
    };
});

customers.MapGet("/{id:guid}", async (
    Guid id,
    IGetCustomerRequestHandler handler,
    CancellationToken ct) =>
{
    var result = await handler.Handle(new GetCustomerRequest(new CustomerId(id)), ct);
    return ToHttp(result);
}).WithName("GetCustomer");
```

## QUERY search (body filters)

```csharp
customers.MapMethods("/", [HttpMethods.Query], async (
    SearchCustomersRequest body,
    ISearchCustomersRequestHandler handler,
    CancellationToken ct) =>
{
    var result = await handler.Handle(body, ct);
    return ToHttp(result);
});
```

`SearchCustomersRequest` carries filters, sort, and pagination fields (`cursor`/`limit` or `page`/`pageSize`).

## Pagination envelope

```csharp
public sealed record Page<T>(
    IReadOnlyList<T> Items,
    string? NextCursor,
    string? PrevCursor,
    int? Page,
    int? PageSize,
    int? TotalCount);
```

Cursor response: set `Items` + `NextCursor`.  
Offset response: set `Items` + `Page` + `PageSize` (+ `TotalCount` if requested).  
Never set both `NextCursor` and `Page` for the same call’s *request* mode — response may leave unused fields null.

## Scalar (not Swagger UI)

```csharp
builder.Services.AddOpenApi();

// …
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi(); // e.g. /openapi/v1.json
    app.MapScalarApiReference(options =>
    {
        options
            .WithTitle("MyProduct API")
            .WithTheme(ScalarTheme.Mars)
            .WithDefaultHttpClient(ScalarTarget.CSharp, ScalarClient.HttpClient);
        // optional: options.WithOpenApiRoutePattern("/openapi/{documentName}.json");
    });
}
```

Browse `/scalar`. Point `launchSettings.json` `launchUrl` at `scalar` when you want Dev to open the reference.
