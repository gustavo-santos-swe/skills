# Serialization sketches

## Host JSON options

```csharp
builder.Services.ConfigureHttpJsonOptions(options =>
{
    options.SerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;
    options.SerializerOptions.Converters.Add(new JsonStringEnumConverter());
});

// Controllers (if used):
builder.Services.AddControllers()
    .AddJsonOptions(o =>
    {
        o.JsonSerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;
        o.JsonSerializerOptions.Converters.Add(new JsonStringEnumConverter());
    });
```

Register NodaTime converters for Instant/LocalDate with the same options instance your host uses.

## DTO vs entity

```csharp
// Good — response DTO
public sealed record CardResponse(Guid Id, string Name, decimal AvailableLimit, string Currency);

// Bad — return tracked entity with navigations
return Results.Ok(card);
```
