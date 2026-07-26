# Security-check hunt list

Use as a **prompt for investigation**, not a pass/fail essay. Skip categories with no surface in scope. Report only high-confidence items after tracing.

## Secrets and config

- Secrets committed or logged (keys, tokens, connection strings, private keys)
- Debug flags / verbose errors exposing internals in prod paths
- Dangerous defaults left on (open CORS + credentials, auth disabled)

## AuthN / sessions

- Missing or broken authentication on new/changed endpoints
- Weak token/session handling (unsigned JWT accept, eternal tokens, tokens in URLs/logs)
- Password/crypto misuse if in diff (MD5/SHA1 for passwords, homemade crypto)

## AuthZ / tenancy

- Missing authorization on sensitive operations
- IDOR / trusting client-supplied `userId` / `tenantId` as authority
- Privilege escalation (role from body, “acting as” without server check)

## Injection and command

- SQL/NoSQL/LDAP built with string concat of untrusted input
- OS/shell/exec with untrusted input
- Template/SSTI sinks if relevant

## XSS / HTML (web)

- Unescaped user HTML (`dangerouslySetInnerHTML`, `v-html`, `|safe`, etc.) with untrusted data
- Note framework auto-escape; only flag real bypasses

## SSRF / outbound

- User-controlled URLs/hosts in server-side fetches
- Server-controlled base URLs from config are usually **not** SSRF

## Files and paths

- Path traversal on upload/download
- Unvalidated file type/size where relevant
- Zip/archive bombs only if in scope and clearly mishandled

## Deserialization / data

- Unsafe deserialize of untrusted payloads
- Mass assignment of privileged fields if binder is wide open

## CSRF / cookies (browser session apps)

- Cookie session mutating endpoints without antiforgery when required by the host model
- JWT Bearer APIs: don’t demand cookie CSRF theater

## Dependencies (when new/changed)

- New packages with surprising install scripts or known critical issues (quick check; not a full SCA product)
- Unexpected privilege in CI/deps changes in the diff

## Business logic (when in diff)

- Clear abuse cases: replay, race on balances, coupon double-spend - only if evidenced in code, not imagined
