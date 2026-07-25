# Rate limiting sketches

## Partition by user or IP

```csharp
builder.Services.AddRateLimiter(options =>
{
    options.RejectionStatusCode = StatusCodes.Status429TooManyRequests;

    options.AddPolicy("per-user", httpContext =>
    {
        var userId = httpContext.User.FindFirstValue(ClaimTypes.NameIdentifier);
        var key = userId ?? httpContext.Connection.RemoteIpAddress?.ToString() ?? "unknown";

        return RateLimitPartition.GetFixedWindowLimiter(key, _ => new FixedWindowRateLimiterOptions
        {
            Window = TimeSpan.FromMinutes(1),
            PermitLimit = 120, // example — set per service
        });
    });

    options.OnRejected = async (context, ct) =>
    {
        context.HttpContext.Response.Headers.RetryAfter = "60";
        // write Problem Details via your standard 429 path
        await Results.Problem(statusCode: 429, title: "Too Many Requests").ExecuteAsync(context.HttpContext);
    };
});

// Exempt probes when mapping limiter globally
// app.MapHealthChecks(...); // outside limited group
```

Numbers are illustrative — pick budgets in the target repo.
