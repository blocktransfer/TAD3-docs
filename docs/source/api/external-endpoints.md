# External Endpoints

These handlers are deployed under the public API surface. They either expose market intelligence sourced from Horizon or broker read-only access to the `PII` table for authorized operators.

## `external/federation`
- **Route**: `GET /federation?q={value}&type={NAME|PLUS|ID}`
- **Purpose**: Resolve Block Transfer federation addresses into Stellar public keys (and optionally residency metadata).
- **Auth**: None. Response varies by `type`:
  - `NAME`: Requires `{investorAccount}*BLOCKTRANSFER.COM`; returns `stellar_address` and resolved `account_id`.
  - `PLUS`: Accepts an internal account string; returns `PK` and the account's home country.
  - `ID`: Not implemented; responds with HTTP 501.
- **Failure modes**: 400 for malformed input, 404 when the account is missing, 500 on DynamoDB/Horizon errors.

## `external/getAssetInfo`
- **Route**: `GET /assets/{code}` where `{code}` is either an asset code or numeric CIK.
- **Purpose**: If `{code}` is alpha-numeric, summarizes outstanding supply for the issuer's asset by summing unrestricted balances, claimable balances, and liquidity pools. If numeric, enumerates all asset codes assigned to that CIK using `stellar.toml`.
- **Dependencies**: Horizon assets endpoint and `https://blocktransfer.com/.well-known/stellar.toml`.
- **Failure modes**: 404 when the asset or issuer cannot be resolved.

## `external/getNumOutstanding`
- **Route**: `GET /assets/{code}/outstanding`
- **Purpose**: Lightweight variant that returns the total outstanding supply as a string. Shares the same Horizon aggregation logic as `getAssetInfo` but omits TOML lookups.
- **Notes**: Returns `0` if the asset cannot be found on Horizon.

## `external/getLedgerBalances`
- **Route**: `GET /assets/{code}/balances`
- **Purpose**: Walks Horizon account and claimable balance collections, returning a JSON map keyed by account ID with `unrestricted` and optional `restricted` balances.
- **Pagination**: Iteratively follows Horizon's `_links.next` URL until all pages have been loaded.
- **Extension points**: Placeholder for adding Soroban contract-held totals once those ledgers go live.

## `external/getPII`
- **Route**: `GET /pii/{PK}`
- **Auth**: API Gateway `AWS_IAM` (the Lambda expects IAM-signed requests).
- **Purpose**: Fetches a single investor profile from the `PII` table by primary key. Returns the DynamoDB item on success; emits `404` when absent.

## `external/getBatchPII`
- **Route**: `GET /pii?PKs=PK1,PK2,...`
- **Auth**: API Gateway `AWS_IAM`.
- **Purpose**: Batch-fetch up to 100 records from `PII` using DynamoDB's `BatchGetItem`.
- **Behavior**: Responds with the raw DynamoDB items when all keys are present; returns `404` listing the missing PKs; raises `400` if the query string is absent; bubbles `500` for other failures.
