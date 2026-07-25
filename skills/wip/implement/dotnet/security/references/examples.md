# Security examples

Sketches for Goose defaults. Adapt names to the target repo.

## Authenticated-by-default (minimal APIs)

```csharp
builder.Services.AddAuthentication().AddJwtBearer(/* … */);
builder.Services.AddAuthorization(options =>
{
    options.FallbackPolicy = new AuthorizationPolicyBuilder()
        .RequireAuthenticatedUser()
        .Build();
});

var app = builder.Build();
app.UseAuthentication();
app.UseAuthorization();

var api = app.MapGroup("/api/v1").RequireAuthorization();

api.MapGet("/cards", ListCardsAsync); // authenticated via group + fallback

app.MapGet("/alive", () => Results.Ok())
    .AllowAnonymous(); // explicit opt-out (health)
```

## JWT validation (authority + audience + lifetime + signing)

```csharp
builder.Services.AddAuthentication().AddJwtBearer(options =>
{
    options.Authority = builder.Configuration["Auth:Authority"];
    options.Audience = builder.Configuration["Auth:Audience"];
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ValidateIssuerSigningKey = true,
    };
});
```

Prefer IdP metadata via `Authority` over baking signing keys into appsettings when the IdP supports it.

## ICurrentUser port (Application) + Infra bind

```csharp
// Application (port)
public interface ICurrentUser
{
    Guid Id { get; }
    bool IsAuthenticated { get; }
}

// Infrastructure
public sealed class HttpCurrentUser(IHttpContextAccessor accessor) : ICurrentUser
{
    public bool IsAuthenticated =>
        accessor.HttpContext?.User.Identity?.IsAuthenticated == true;

    public Guid Id
    {
        get
        {
            var raw = accessor.HttpContext?.User.FindFirstValue(ClaimTypes.NameIdentifier)
                ?? throw new InvalidOperationException("Missing nameidentifier claim.");
            return Guid.Parse(raw);
        }
    }
}

// DI (Infra / host)
builder.Services.AddHttpContextAccessor();
builder.Services.AddScoped<ICurrentUser, HttpCurrentUser>();
```

Handlers depend on `ICurrentUser`, not `IHttpContextAccessor`.

## Ownership check (never trust body user id)

```csharp
public async Task<Result> Handle(SettleRequest request, CancellationToken ct)
{
    var card = await _db.CreditCards.SingleOrDefaultAsync(c => c.Id == request.CardId, ct);
    if (card is null) return new NotFound(...);
    if (card.OwnerId != _currentUser.Id) return new Forbidden(...);
    // …
}
```

Never: `if (request.UserId == _currentUser.Id)` using a client-supplied user id as the source of truth for authorization.

## CORS — loose non-prod, tight prod

```csharp
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        if (builder.Environment.IsDevelopment())
        {
            policy.AllowAnyOrigin().AllowAnyHeader().AllowAnyMethod();
            return;
        }

        var origins = builder.Configuration.GetSection("Cors:Origins").Get<string[]>() ?? [];
        policy.WithOrigins(origins)
            .AllowAnyHeader()
            .AllowAnyMethod();
        // .AllowCredentials() only when cookie browser clients need it —
        // and then origins must be explicit (never AllowAnyOrigin + credentials).
    });
});
```

## Cookie auth + antiforgery (mutating endpoints)

```csharp
builder.Services.AddAuthentication()
    .AddCookie(options =>
    {
        options.Cookie.HttpOnly = true;
        options.Cookie.SecurePolicy = CookieSecurePolicy.SameAsRequest; // Always outside Dev
        options.Cookie.SameSite = SameSiteMode.Lax;
    });

builder.Services.AddAntiforgery();

// For APIs that use cookies: validate antiforgery on POST/PUT/PATCH/DELETE
// (header/form token pattern your host already uses — Razor, SPA header, etc.)
```

JWT-only APIs: skip the antiforgery pipeline; don’t cargo-cult CSRF tokens onto Bearer APIs.

## SSRF — don’t invent open fetch

```csharp
// Don't add helpers like:
// Task<HttpResponseMessage> FetchUserUrl(string url) => _http.GetAsync(url);

// If product explicitly requires import-from-URL:
// - allowlist hosts from config
// - https only
// - resolve DNS and reject private / link-local / metadata ranges
// - do not follow redirects off the allowlist
```
