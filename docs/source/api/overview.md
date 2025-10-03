# Syndicate API Overview

The `AI-HERE-TODO` bundle contains the Lambda handlers that power the Syndicate API gateway. They are organized by function (public market data, issuer tooling, investor operations) rather than by transport layer, which makes the folder layout a good proxy for the deployed routes. Each handler is intended to run behind AWS API Gateway with minimal wrappers.

## Runtime layout
- `external/`: unauthenticated or IAM-protected public endpoints that read from Stellar Horizon and DynamoDB.
- `issuerlink/`: QR login and authorization helpers for issuer operators.
- `investors/` & `legacy/`: stateful operations that move records between the legacy book and on-ledger accounts.
- `internal/` & `configuration/`: operational utilities (scans, config stubs) that should stay behind restricted execution roles.
- `sep8/` & `sep10/`: compliance endpoints that eventually expose SEP-8 mediated approvals and SEP-10 web auth.
- `stellarSDK/` & `tests/`: Lambda layer smoke tests and monitoring hooks.

## Shared services
| Dependency            | Purpose                                                     |
| --------------------- | ----------------------------------------------------------- |
| `PII` DynamoDB table  | Stores investor profiles, account IDs, and restrictions.    |
| `legacy` DynamoDB table | Keeps pre-Stellar asset ledgers for cold conversions.      |
| `issuerSessions` DynamoDB table | Tracks issuer QR login handshakes and session state. |
| Horizon (`https://horizon.stellar.org`) | Primary source for on-ledger reads (assets, accounts, signers). |
| Issuers.Info API      | Pulls public-company metadata (CIK, reporting status).      |
| AWS Lambda (same dir) | Several handlers invoke peers directly (e.g. federation lookup). |

## Auth tiers
- **Public**: No auth; returns market data (e.g. `getLedgerBalances`). Always rate-limit at the gateway.
- **AWS_IAM**: Requires signed requests with scoped IAM policies (e.g. `getPII`, `getBatchPII`).
- **Custom**: IssuerLink QR and SEP-8 flows rely on bespoke bearer payloads and signature checks.

The following pages document each handler group, expected inputs, downstream dependencies, and failure modes so you can wire the API Gateway stage (or future framework) without spelunking through the Lambda source.
