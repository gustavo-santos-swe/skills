---
name: file-storage
description: Uploads, blobs, streaming, and object storage from .NET. Use when adding or changing file upload/download, S3/Azure Blob/disk storage, or large payload streaming in ASP.NET.
disable-model-invocation: true
metadata:
  area: wip
---

# File Storage

Status: **stub** — topic list below is what to define later. Keep SKILL.md short; deep samples → `references/`.

## When to use

- Upload/download endpoints; storing binaries outside the DB; streaming large files.
- **`implement`** loading this pack for a .NET change that touches files/blobs.

## Topics to fill (checklist)

### Where bytes live
- Object storage (S3/Blob) vs disk vs DB (DB almost never for blobs)
- Naming/key layout; multi-env buckets/containers

### Upload path
- Multipart / size limits; content-type allowlist
- Virus/malware scan — required or not
- Direct-to-storage (presigned URL) vs via API

### Download path
- Streaming vs buffering; range requests
- Authz on the object (not just the URL being “hard to guess”)
- Signed URLs — TTL and scope

### Metadata & lifecycle
- What we store in DB (key, hash, size, content-type) vs in the bucket
- Retention, delete, soft-delete of objects
- Orphan cleanup jobs (→ background-work)

### Security
- Path traversal; content sniffing; SSRF if fetching remote URLs
- Align with security + endpoint-conventions

### Testing
- How we fake storage in tests; Testcontainers for MinIO/Azurite?

## Don't

- Don't store large binaries in Postgres/SQL “just for now.”
- Don't trust client-provided content-type/filename without allowlisting.
- Don't expose public buckets for private user data.

## References

Optional: `references/` for provider adapters. Bucket names/secrets stay in the target repo / configuration.
