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

## Upload gates (handler sketch)

```csharp
const long MaxBytes = 5 * 1024 * 1024;
var allowed = new HashSet<string>(StringComparer.OrdinalIgnoreCase) { "image/jpeg", "image/png" };

if (file.Length is <= 0 or > MaxBytes)
    return new ValidationFailed(...);

if (!allowed.Contains(file.ContentType)) // also validate sniffed type when needed
    return new ValidationFailed(...);

await using var stream = file.OpenReadStream();
var key = $"users/{userId}/avatar/{Guid.CreateVersion7()}";
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
