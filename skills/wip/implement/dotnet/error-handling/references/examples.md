# Error handling examples

Illustrative greenfield shape (.NET 11 / C# 15 unions). Adapt names to the product.

## Result union

```csharp
public sealed record Ok<T>(T Value);
public sealed record NotFound(string Code, string Message);
public sealed record ValidationFailed(string Code, IReadOnlyDictionary<string, string[]> Errors);
public sealed record Forbidden(string Code, string Message);
public sealed record Conflict(string Code, string Message);

public union Result<T>(Ok<T>, NotFound, ValidationFailed, Forbidden, Conflict);
```

## Use case

```csharp
public Result<CreditCard> GetCard(Guid id)
{
    var card = /* load */;
    if (card is null)
        return new NotFound("CreditCards.NotFound", "Credit card not found.");

    return new Ok<CreditCard>(card);
}
```

## Host mapping (sketch)

```csharp
IResult ToHttp<T>(Result<T> result) => result switch
{
    Ok<T> ok => Results.Ok(ok.Value),
    NotFound n => Results.Problem(
        title: n.Message,
        statusCode: StatusCodes.Status404NotFound,
        extensions: new Dictionary<string, object?> { ["code"] = n.Code }),
    ValidationFailed v => Results.Problem(
        title: "Validation failed",
        statusCode: StatusCodes.Status422UnprocessableEntity,
        extensions: new Dictionary<string, object?>
        {
            ["code"] = v.Code,
            ["errors"] = v.Errors
        }),
    Forbidden f => Results.Problem(
        title: f.Message,
        statusCode: StatusCodes.Status403Forbidden,
        extensions: new Dictionary<string, object?> { ["code"] = f.Code }),
    Conflict c => Results.Problem(
        title: c.Message,
        statusCode: StatusCodes.Status409Conflict,
        extensions: new Dictionary<string, object?> { ["code"] = c.Code }),
};
```

Wire this once; endpoints call `ToHttp(await handler(...))`.

## Legacy Result (existing repos)

```csharp
// Keep project types — e.g. Result<T> + Error(Code, Message, ErrorType)
// Map ErrorType → status in one place. Don't introduce unions mid-change.
```

## Feature-specific case

```csharp
public sealed record PaywallBlocked(string Code, string Plan, string Message);

// Only if Result<T> is extended for that vertical/feature:
// public union Result<T>(Ok<T>, NotFound, ValidationFailed, Forbidden, Conflict, PaywallBlocked);
```

Prefer a core case + code when HTTP mapping wouldn’t change.
