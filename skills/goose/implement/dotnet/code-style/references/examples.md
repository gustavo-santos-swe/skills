# Code style sketches

## Prefer

```csharp
namespace Monetis.App.Application.Cards;

public sealed record CardResponse
{
    public required Guid Id { get; init; }
    public required string Name { get; init; }
}

public sealed class CreateCardRequestHandler
{
    private readonly ICardRepository _cards;

    public CreateCardRequestHandler(ICardRepository cards)
    {
        _cards = cards;
    }

    public async Task<CardResponse> HandleAsync(CreateCardRequest request, CancellationToken cancellationToken)
    {
        var labels = new List<string> { request.Label };
        labels = [request.Label]; // collection expression when the type fits
        string[] none = [];
        var card = await _cards.AddAsync(request, cancellationToken);
        return new CardResponse { Id = card.Id, Name = card.Name };
    }
}
```

## Avoid (house style)

```csharp
public sealed record CardResponse(Guid Id, string Name); // positional

public class Handler(ICardRepository cards) // primary constructor
{
}

private readonly ICardRepository cards; // no underscore
```
