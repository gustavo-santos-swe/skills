# DI sketches

## Composition root

```csharp
builder.Services.AddApplication();
builder.Services.AddInfrastructure(builder.Configuration);
builder.Services.AddSingleton(TimeProvider.System);
```

## Infrastructure submethods

```csharp
public static class InfrastructureServiceCollectionExtensions
{
    public static IServiceCollection AddInfrastructure(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        services.AddPersistence(configuration);
        services.AddStripe(configuration);
        return services;
    }

    public static IServiceCollection AddPersistence(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        services.AddDbContext<AppDbContext>(/* … */);
        return services;
    }

    public static IServiceCollection AddStripe(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        services.AddOptions<StripeOptions>()
            .Bind(configuration.GetSection("Stripe"))
            .ValidateDataAnnotations()
            .ValidateOnStart();

        services.AddHttpClient<IStripeGateway, StripeGateway>((sp, client) =>
        {
            var opts = sp.GetRequiredService<IOptions<StripeOptions>>().Value;
            client.BaseAddress = new Uri(opts.BaseUrl);
        });

        return services;
    }
}
```

## Application handlers (explicit or scan)

```csharp
services.AddScoped<ICreateCustomerRequestHandler, CreateCustomerRequestHandler>();
// or agreed Scrutor scan for I*RequestHandler → Scoped
```

## Banned

```csharp
// don't — captive dependency
services.AddSingleton<IHostedThing>(); // that injects DbContext

// don't — during registration
services.BuildServiceProvider();

// don't — app code service location
public class Foo(IServiceProvider sp) {
    public void Bar() => sp.GetRequiredService<IBar>().Do();
}
```
