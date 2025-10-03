# IssuerLink Flows

IssuerLink enables issuer operators to authenticate with a desktop console by pairing a mobile wallet (Ed25519 signer) to a web session. The Lambdas in `issuerlink/` orchestrate QR code distribution, signature verification, and session authorization.

## Happy-path flow
1. **Request QR** (`issuerlink/getLoginQR`)
   - **Route**: `POST /issuerlink/login`
   - Generates a 7200-second session nonce tied to the caller's source IP and stores it in the `issuerSessions` table. Returns a deep link string (`bt.issuer://link?s=...&ip=...`) that the mobile app encodes into a QR.
2. **Sign and submit** (`issuerlink/verifyUser`)
   - **Route**: `POST /issuerlink/verify`
   - Mobile app posts `{ token, sig, PK }` where `token` encodes the session ID and desktop IP. The handler:
     - Validates the Ed25519 signature with the claimed Stellar public key.
     - Confirms the PK exists in the `PII` table and is not restricted.
     - Confirms the session exists, matches the desktop IP, and records the user profile under the session record.
     - Gathers issuer accounts the PK signs for by enumerating Horizon signer relationships and annotating weight-based authority levels.
     - Returns `{ isAuthorized: true, context: { self, issuers } }` or rejects with `isAuthorized: false`.
3. **Authorize subsequent requests** (`issuerlink/sessionLambdaAuthorizerHOT`)
   - **Route**: Lambda authorizer attached to protected routes.
   - Reads the session token from the `Authorization` header, loads the session from `issuerSessions`, verifies both the stored `valid` flag and the caller IP, then injects the previously stored `user` and `issuers` context into API Gateway.

## Tables & schema
- `issuerSessions` primary key: `PK` (session ID). Attributes include `IP`, `TTL`, `verified`, `valid`, and any user context captured during verification.
- Session TTL is 7200 seconds from QR creation; clients should refresh before the record expires.

## Error handling
- Any signature mismatch or session/IP mismatch raises `PermissionError`, producing `isAuthorized: false` without leaking details.
- DynamoDB or Horizon failures bubble up as JSON error strings so operational logs capture the cause. Harden the API Gateway responses to avoid exposing internals in production.

## Roadmap callouts
- Session validation still uses bespoke JSON in the `Authorization` header; future work should migrate to WalletConnect or a signed JWT with CSRF protection.
- `verifyUser` contains TODOs for encoding a secure cookie and persisting issuer context atomically—plan to wire those before broad rollout.
