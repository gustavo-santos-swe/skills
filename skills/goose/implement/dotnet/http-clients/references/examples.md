# HTTP clients sketches

## Typed client + resilience

```csharp
services.AddOptions<OpeniOptions>()
    .Bind(configuration.GetSection("OpenFinance:Openi"))
    .ValidateDataAnnotations()
    .ValidateOnStart();

services.AddHttpClient<IOpeniClient, OpeniClient>((sp, client) =>
    {
        var o = sp.GetRequiredService<IOptions<OpeniOptions>>().Value;
        client.BaseAddress = new Uri(o.BaseUrl);
    })
    .AddHttpMessageHandler<OpeniAuthHandler>()
    .AddStandardResilienceHandler();
```

## Unit: substitute the port

```csharp
var openi = Substitute.For<IOpeniClient>();
openi.GetAccountAsync(Arg.Any<string>(), Arg.Any<CancellationToken>())
    .Returns(new OpeniAccountDto(/* … */));
```

Don’t `new HttpClient()` inside the handler under test.
