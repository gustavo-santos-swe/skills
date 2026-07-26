# File storage sketches

## Port (Application)

```csharp
public interface IFileStorage
{
    Task<string> UploadAsync(Stream content, string contentType, string key, CancellationToken ct);
    Task<Stream> OpenReadAsync(string key, CancellationToken ct);
    Task DeleteAsync(string key, CancellationToken ct);
    // Optional: Task<Uri> CreateReadSasAsync(string key, TimeSpan ttl, CancellationToken ct);
}
```

## Dual host size limits

```csharp
const long MaxBytes = 5 * 1024 * 1024;

builder.WebHost.ConfigureKestrel(o => o.Limits.MaxRequestBodySize = MaxBytes);
builder.Services.Configure<FormOptions>(o =>
{
    o.MultipartBodyLengthLimit = MaxBytes;
});
```

## Minimal API form binding + antiforgery

```csharp
// File + fields → [FromForm] on form-bound params
api.MapPost("/avatars", async (
    [FromForm] IFormFile file,
    [FromForm] string? caption,
    IUploadAvatarHandler handler,
    CancellationToken ct) => /* … */);

// JWT API with UseAntiforgery() in the pipeline:
api.MapPost("/avatars", …).DisableAntiforgery();

// Cookie-auth upload: do NOT DisableAntiforgery — send the token
```

## Upload gates (handler sketch)

```csharp
const long MaxBytes = 5 * 1024 * 1024;
var allowed = new HashSet<string>(StringComparer.OrdinalIgnoreCase) { "image/jpeg", "image/png" };

if (file.Length is <= 0 or > MaxBytes)
    return new ValidationFailed(...);

if (!allowed.Contains(file.ContentType)) // also validate sniffed type when needed
    return new ValidationFailed(...);

// Never: Path.Combine(root, file.FileName)
await using var stream = file.OpenReadStream();
var key = $"users/{userId}/avatar/{Guid.CreateVersion7()}.jpg";
await _storage.UploadAsync(stream, file.ContentType, key, ct);
// persist metadata row with key, size, content-type, owner
```

## Download

```csharp
var meta = await _db.Attachments.SingleOrDefaultAsync(a => a.Id == id, ct);
if (meta is null) return new NotFound(...);
if (meta.OwnerId != currentUser.Id) return new Forbidden(...);

// stream via API or short-lived SAS — never public bucket + guessable key
```
