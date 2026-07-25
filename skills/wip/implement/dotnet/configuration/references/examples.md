# Configuration sketches

## Bind typed options

```csharp
builder.Services
    .AddOptions<StripeOptions>()
    .Bind(builder.Configuration.GetSection("Stripe"))
    .ValidateDataAnnotations()
    .ValidateOnStart();
```

## Local `.env` (optional, untracked)

```csharp
// Host only — never commit .env
builder.Configuration.AddDotNetEnv(".env");
```

## Feature toggle on options

```csharp
public sealed class OpenFinanceOptions
{
    public bool EnableBillSync { get; init; } // default false in appsettings
}
```

```csharp
if (!_options.Value.EnableBillSync)
    return; // risky path off until explicitly enabled per env
```
