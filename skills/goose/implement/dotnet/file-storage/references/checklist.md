| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Object storage (S3/R2/Azure Blob/MinIO) is the default for user/app binaries; SQL BYTEA/varbinary is banned for large blobs | verify | Where bytes live |
| Application depends on a storage port (`IFileStorage`); Infrastructure owns the SDK | verify | Where bytes live |
| Kestrel `MaxRequestBodySize` and FormOptions `MultipartBodyLengthLimit` are both configured, in sync | regression-test | Upload — read the built host config in a test, assert both are set and consistent |
| Allowlist content types/extensions — don't trust `Content-Type` or filename alone | verify | Upload — Content and keys |
| Disallowed content-types are rejected at upload | regression-test | Upload — unit test against the allowlist check |
| Upload never uses the client filename as the storage key (path traversal) — generate a safe key | regression-test | Upload — unit test uploading `../../etc/passwd`, assert the generated key is safe |
| Stream to the port; don't load multi-MB files into `byte[]` "for convenience" | verify | Upload |
| Authorize first (ownership/policy), then stream via API or issue a short-TTL signed URL | verify | Download and authz |
| Private buckets by default for user data — no public containers for private attachments | verify | Download and authz |
| Don't store large binaries in Postgres "just for now" | verify | Don't |
| Don't use forever-lived signed URLs for private objects | verify | Don't |
| Don't put AWS/Azure SDK types in Application/Domain | verify | Don't |
