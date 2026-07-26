---
name: file-storage
description: Use when adding or reviewing .NET file/blob upload download, object storage ports, size/type limits, or signed URLs — or when implement loads the dotnet pack for storage work.
disable-model-invocation: true
metadata:
  area: wip
---

# File Storage

Goose handbook for binaries outside the database.

**Target repo wins** if storage ports/providers are already settled (e.g. Monetis `IFileStorage` + R2/S3).

Voice: **`write-like-goose`**.

## When to use

- Upload/download endpoints; attachments; avatars; reports
- Choosing bucket vs disk vs DB; signed URLs
- **`implement`** loading this pack

## Where bytes live

| Store | Rule |
|-------|------|
| **Object storage** (S3 / R2 / Azure Blob / MinIO) | Default for user/app binaries |
| **Disk on web node** | Avoid under scale-out |
| **SQL BYTEA / varbinary** | Ban for large blobs; tiny exceptions only |

**Application** depends on a storage **port** (`IFileStorage` / similar). **Infrastructure** owns the SDK. **DB** holds metadata: key/path, size, content-type, hash, owner, timestamps — not the bytes.

## Upload

**Default:** upload through the API/handler.

### Size limits (two knobs)

Configure **both** — agents usually set only one:

| Layer | What |
|-------|------|
| **Kestrel** `MaxRequestBodySize` | Whole request body |
| **FormOptions** `MultipartBodyLengthLimit` | Multipart/form uploads |

App-level max (handler) stays the product truth; host limits must be ≥ that max. Per-endpoint `[RequestSizeLimit]` / `.DisableRequestSizeLimit()` only when streaming large blobs on purpose.

### Minimal API binding

- `IFormFile` alone binds from multipart
- Mixing file + other form fields → mark form-bound params with **`[FromForm]`** (or one `[FromForm]` DTO)
- With `UseAntiforgery()`: form uploads require antiforgery unless you **`.DisableAntiforgery()`** — safe for **JWT** APIs; **keep antiforgery** for cookie-auth uploads (**`security`**)

### Content and keys

- **Allowlist** content types / extensions — don’t trust `Content-Type` or filename alone; sniff magic bytes when risk warrants
- **Never** use the client filename as a path segment (path traversal) — generate a safe key; derive extension from validated type
- **Stream** to the port; don’t load multi‑MB files into `byte[]` “for convenience”
- **Presigned direct-to-bucket** when files are large or you need to offload the API — minting the URL still requires authz + the same allowlist/size policy
- Malware scan: product decision; if required, do it before the object is treated as trusted (often async → **`background-work`**)

## Download and authz

- **Authorize first** (ownership / policy) — obscure object keys are not security
- Then **stream** via API or issue a **short-TTL signed URL**
- **Private buckets** by default for user data; no public containers for private attachments
- Range requests when serving large downloads and clients need them

## Lifecycle

- Soft-delete or hard-delete per product rules; remove or GC the object when metadata goes away
- **Orphan cleanup** jobs for abandoned uploads → **`background-work`**
- Multi-env: separate buckets/prefixes; never point prod at a shared “dev” bucket

## Testing

- Fake/substitute the storage port in Unit tests
- Integration: Azurite / MinIO / Testcontainers when the adapter matters — don’t hit real prod buckets

## Failure modes (agent traps)

| Temptation | Why it hurts | Do instead |
|------------|--------------|------------|
| Raise only Kestrel limit | Multipart still capped | Set FormOptions too |
| Save as `file.FileName` | Path traversal | Generated key + validated extension |
| Trust `Content-Type` | Spoofed uploads | Allowlist + sniff when needed |
| Cookie upload + `DisableAntiforgery` | CSRF | Keep antiforgery on cookie hosts |
| 400 on upload, blame “file code” | Often missing antiforgery token | Check antiforgery / JWT opt-out |

## Don't

- Don’t store large binaries in Postgres “just for now”
- Don’t expose public buckets for private user data
- Don’t trust client content-type/filename without allowlisting
- Don’t use forever-lived signed URLs for private objects
- Don’t put AWS/Azure SDK types in Application/Domain

## References

- [`references/examples.md`](references/examples.md) — port, dual size limits, form binding, upload gates

## Related

- Endpoint size limits / forms → **`endpoint-conventions`** / **`security`**
- Orphan jobs → **`background-work`**
- Secrets for buckets → **`configuration`**
- Minimal API upload how-to (plugin) → Cursor **`dotnet-aspnetcore`** / `minimal-api-file-upload`
