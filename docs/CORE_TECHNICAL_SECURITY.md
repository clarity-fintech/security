# Core Technical and Security Evidence Register

This page expands Phase 1 of the CLRTY exchange-readiness checklist into a focused evidence register for technical reviewers, security auditors, and exchange integration teams.

Canonical security policy:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

## Evidence Model

Each control should be backed by one or more evidence artifacts before CLRTY represents it as complete in an exchange questionnaire.

| Evidence type | Examples |
|---------------|----------|
| Public source evidence | Release tag, verified source, explorer link, public manifest |
| Test evidence | Unit tests, integration tests, load tests, snapshot tests, dry-run logs |
| Audit evidence | Third-party audit report, remediation matrix, retest report |
| Operational evidence | Runbook, signer policy, incident exercise notes, monitoring screenshot |

## Phase 1 Controls

| ID | Control | Required evidence before completion |
|----|---------|-------------------------------------|
| 1 | Source code verification | Publish and verify production source on the relevant explorer or public Git repository. Record source hash, compiler/runtime version, release tag, and explorer URL. |
| 2 | Third-party security audit | Attach a signed audit report covering smart contracts, runtime modules, bridge logic, or critical settlement code. Identify auditor, scope, report date, and residual risk. |
| 3 | Audit remediation | Maintain a finding-by-finding remediation matrix with severity, owner, fix commit, retest status, and accepted-risk signoff if any item is not fixed. |
| 4 | Penetration testing | Conduct authorized off-chain API and infrastructure testing. Preserve scope, methodology, results, remediations, and retest confirmation. |
| 5 | Private key management | Document use of HSM, hardware wallet, MPC, or multisig controls for treasury, deployer, bridge, and emergency keys. Include signer thresholds and recovery policy. |
| 6 | Admin and governance access | Require multisig or governance approval for all privileged admin actions. Document threshold, signer identity process, timelock rules, and emergency exceptions. |
| 7 | Circuit breakers | Define emergency pause or freeze controls where applicable. Include authority, triggering conditions, test transaction, and unpause governance path. |
| 8 | Gas optimization | Benchmark primary user actions and reduce avoidable gas or execution cost. Preserve before/after reports and explain any tradeoffs. |
| 9 | Upgradeability path | If code is upgradeable, document proxy-admin or runtime upgrade path. If immutable, document immutability guarantees. Test upgrade and rollback paths on staging. |
| 10 | Reentrancy guards | Validate state-changing functions against reentrancy and cross-call hazards. Attach static analysis, audit notes, and test vectors. |
| 11 | Event emission | Ensure critical transfers, mints, burns, governance actions, upgrades, pauses, and treasury movements emit indexable events. Provide event schema and indexer tests. |
| 12 | ChainID and network config | Publish production chain ID, RPC metadata, genesis hash, denomination, explorer URL, and wallet metadata. Confirm no collision with test networks. |
| 13 | Timestamp and block dependencies | Review code for insecure block timestamp or height assumptions. Document safe tolerances and replacement mechanisms. |
| 14 | Overflow and underflow protection | Confirm modern compiler/runtime arithmetic safety, checked math, or explicit validation for all supply, rewards, accounting, and settlement calculations. |
| 15 | Wallet compatibility | Test supported wallet flows across MetaMask, WalletConnect, Ledger, and Trezor where applicable. Document unsupported wallet classes clearly. |
| 16 | Node stability | Prove public and private RPC nodes withstand high concurrency. Include request rate, latency, error rate, saturation point, and mitigation plan. |
| 17 | Explorer functionality | Confirm explorer displays token metadata, balances, transactions, events, validator data, and contract/module information accurately. |
| 18 | Finality checks | Document finality assumptions, reorg handling, confirmation depth, and exchange deposit-crediting recommendation. |
| 19 | Snapshot testing | Validate snapshot scripts for airdrops, migrations, token allocation, or governance balances. Include deterministic checksums and replay process. |
| 20 | Emergency recovery | Test and document recovery for stuck tokens, halted validators, failed upgrades, corrupt nodes, unavailable RPCs, and data restoration. |

## Minimum Exchange Evidence Bundle

For a technical listing packet, CLRTY should be able to provide:

- Production chain/network manifest.
- Verified source or release-tag index.
- Audit report and remediation matrix.
- Key management and multisig policy.
- Emergency pause, recovery, and incident runbooks.
- RPC and explorer availability evidence.
- Wallet compatibility matrix.
- Finality and deposit-crediting guidance.
- Snapshot and backup validation logs.

## Relationship to the Full Checklist

These controls correspond to items 1-20 in [`EXCHANGE_READINESS_CHECKLIST.md`](EXCHANGE_READINESS_CHECKLIST.md).
