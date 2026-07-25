# Security sketches

## Host policy + handler ownership

```csharp
// Host
app.MapPost("/api/v1/cards/{cardId}/settle", SettleAsync)
    .RequireAuthorization("User");

// Handler
public async Task<Result> Handle(SettleRequest request, CancellationToken ct)
{
    var card = await _db.CreditCards.SingleOrDefaultAsync(c => c.Id == request.CardId, ct);
    if (card is null) return new NotFound(...);
    if (card.OwnerId != _currentUser.Id) return new Forbidden(...);
    // …
}
```

Never: `if (request.UserId == …)` using a user id from the body as the source of truth.

## JWT API (sketch)

```csharp
builder.Services.AddAuthentication().AddJwtBearer(options =>
{
    options.Authority = builder.Configuration["Auth:Authority"];
    options.Audience = builder.Configuration["Auth:Audience"];
    options.TokenValidationParameters.ValidateAudience = true;
});
builder.Services.AddAuthorization();
```
