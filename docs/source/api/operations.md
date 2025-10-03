# Operations & Compliance Functions

The remaining handlers support internal operations: onboarding investors, migrating legacy ledgers, and wiring Stellar compliance hooks (SEP-8/SEP-10). They are not intended for public exposure without additional guarantees.

## Internal scans (`internal/`)
- `scanAllAccPubKeys`: Scans the `PII` table (via the `users` index) and returns every public key. **Note**: the code references `table.scan(...)` but should call `PII_DB.scan(...)`; never expose this without pagination limits.
- `scanAllValidPubKeys`: Similar to the above but filters out records carrying a `hold` flag. Use Dynamo Streams or a materialized list to avoid table scans in production.

## Investor automation (`investors/`)
- `generateNewAccID`: Generates an 8-char base32 ID with checksum and profanity filtering, ensuring the ID is unused before returning.
- `addNewRecordPII`: Skeleton for creating new investors in DynamoDB with a conditional put on `ID`. Fields such as `DOB` and `phone` still need validation logic.
- `distributeAssetsFromLegacyAccEntryToStellar-HOT_KEYS`: Builds a Stellar transaction that converts a legacy record into claimable balances with Rule 144 predicates. Pulls holdings from the `legacy` table, investor country knowledge from `external-Federation`, and issuer status from Issuers.Info before composing the transaction XDR.

## Legacy imports (`legacy/`)
Contains helper Lambdas for marshaling pre-Stellar positions: looking up unclaimed legal names, searching legacy investors or companies, and triggering batch import jobs. All functions assume access to the `legacy` DynamoDB table and should remain hot-key restricted.

## Compliance adapters
- `sep8/betaUserTxnApprovals`: Prototype SEP-8 approval service; currently enforces custom business rules before approving transactions.
- `sep10/getWebAuthChallenge` & `sep10/postWebAuthResponseJWT`: Placeholders for SEP-10 authentication. Both functions return stub data pending the final challenge/response implementation.

## Test harness (`tests/`, `stellarSDK/`)
- Lightweight smoke tests for CloudWatch triggers (`cloudwatchExecuteDailyHoldingsSnapshots`, etc.) and Lambda layer verification (`stellarSDK/testLambdaLayer.py`). Keep them isolated from production routing and scheduled invocations.

### Operational guidance
- Wrap all non-public handlers behind IAM policies or Lambda authorizers; several scripts assume trust in the caller.
- Replace full-table scans with streamed updates before moving beyond prototype scale.
- Document DynamoDB schemas alongside the Lambdas so future maintainers can evolve them without reverse engineering calls.
