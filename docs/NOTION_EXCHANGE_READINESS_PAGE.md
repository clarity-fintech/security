# CLRTY Exchange Readiness / Security Evidence Register

This page is the Notion-ready security, compliance, liquidity, operational, and testing evidence register for CLRTY exchange integration. It mirrors the public security repository and is intended to live under the same VIS CLARITY PnL / CLRTY DATA CENTER Notion workspace used for metrics.

Canonical GitHub repository:

```text
https://github.com/clarity-fintech/security
```

Canonical security policy:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

Security contact:

```text
security@clarity-fintech.com
```

Full 100-control public checklist:

```text
https://github.com/clarity-fintech/security/blob/main/docs/EXCHANGE_READINESS_CHECKLIST.md
```

Five-pillar market launch checklist:

```text
https://github.com/clarity-fintech/security/blob/main/docs/MARKET_LAUNCH_EXCHANGE_LISTING_100.md
```

Notion sync command from the main CLRTY project:

```bash
python3 scripts/metrics/sync_notion_security.py
```

## Notion Placement

Create or sync this page under the existing metrics page:

```text
VIS CLARITY PnL / CLRTY DATA CENTER
```

The sync script uses:

```text
NOTION_TOKEN
NOTION_DATA_CENTER_PAGE_ID
NOTION_SECURITY_PAGE_ID
NOTION_SECURITY_PAGE_TITLE
```

`NOTION_SECURITY_PAGE_ID` is optional. If it is absent, the script searches for or creates a child page titled `CLRTY Exchange Readiness / Security Evidence Register` under `NOTION_DATA_CENTER_PAGE_ID`.

## Notion Usage

Create a Notion page named:

```text
CLRTY Exchange Readiness / Security Evidence Register
```

Recommended properties:

| Property | Type | Suggested value |
|----------|------|-----------------|
| Owner | Person | Security / Compliance lead |
| Status | Select | Evidence gathering |
| Public URL | URL | `https://github.com/clarity-fintech/security/blob/main/docs/EXCHANGE_READINESS_CHECKLIST.md` |
| Security policy URL | URL | `https://github.com/clarity-fintech/security/blob/main/SECURITY.md` |
| Contact | Email | `security@clarity-fintech.com` |
| Last reviewed | Date | Current review date |

Use the GitHub repository as the source of truth. Use Notion for owner assignment, due dates, attachments, and private evidence that should not be committed publicly.

## Status Key

| Status | Meaning |
|--------|---------|
| Active | Public process or repository control exists. |
| Evidence required | Attach deployment logs, tests, runbooks, signed reports, or screenshots before marking complete. |
| External attestation required | Requires auditor, counsel, SOC 2, market maker, exchange, or compliance vendor evidence. |
| Operational readiness | Requires staffing, monitoring, launch-day process, or incident response procedure. |

## Live CLRTY-1 Chain Validation Snapshot

Current live-version asset identity:

| Field | Value |
|-------|-------|
| Asset | CLRTY |
| Chain | `clrty-1` |
| Denom | `uclrty` |
| Kind | Native L1 |
| Decimals | `9` |
| Max supply | `16,000,000 CLRTY` |
| Contract address | Not publicly disclosed; no public wrapped-token address is claimed |

Latest local/simulated CLRTY-1 stress result:

| Battery | Result |
|---------|--------|
| Genesis verification | PASS |
| L-DNET WORM stress | PASS, 50/50 |
| Fuzz stress | PASS |
| Nano stress | PASS |
| Bridge connection audit | PASS |
| Arbitrage core | PASS |
| L1 concurrency simulation | PASS, 50 simulated blocks |
| Fork-swap bounded stress | PASS, 25 iterations |

Evidence report:

```text
docs/CLRTY1_LIVE_CHAIN_STRESS_REPORT.md
```

Machine-readable evidence:

```text
var/compliance/clrty1_live_chain_stress_summary.json
var/compliance/clrty1_live_endpoint_probe.json
```

Live endpoint note: no configured `CLRTY_API_URL`, `CLRTY_API_BASE`, or `CLRTY_L1_RPC` HTTP endpoint was present during this run, so the battery validates the repository-backed CLRTY-1 chain model and local/simulated stress paths. Hosted RPC saturation testing remains a separate operator-approved gate.

## Listing Questionnaire Answers

Bug bounty / security policy URL:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

Exchange readiness checklist:

```text
https://github.com/clarity-fintech/security/blob/main/docs/EXCHANGE_READINESS_CHECKLIST.md
```

Market launch / exchange listing checklist:

```text
https://github.com/clarity-fintech/security/blob/main/docs/MARKET_LAUNCH_EXCHANGE_LISTING_100.md
```

Core technical security register:

```text
https://github.com/clarity-fintech/security/blob/main/docs/CORE_TECHNICAL_SECURITY.md
```

Exchange compliance register:

```text
https://github.com/clarity-fintech/security/blob/main/docs/EXCHANGE_COMPLIANCE.md
```

## Phase 1: Core Technical and Security

Use this section for controls 1-20 in the exchange listing data room.

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 1 | Source code verification: publish and verify all contracts or runtime source on block explorers or CLRTY-native explorers. | Explorer links, release tags, source hashes, compiler/runtime versions. |
| 2 | Third-party security audit: obtain comprehensive smart contract, runtime, or critical infrastructure audit. | Signed audit report, scope, auditor, date, residual-risk summary. |
| 3 | Audit remediation: implement and document all audit findings. | Remediation matrix, fix commits, retest report, accepted-risk signoff. |
| 4 | Penetration testing: perform off-chain API and infrastructure stress tests. | Scope letter, methodology, test report, remediation notes. |
| 5 | Private key management: deploy HSM, hardware wallet, MPC, or multisig controls for treasury funds. | Custody policy, signer matrix, recovery procedure. |
| 6 | Admin and governance access: require multisig approval for owner or admin functions. | Governance config, signer threshold, transaction examples. |
| 7 | Circuit breakers: implement emergency pause or freeze controls where applicable. | Pause runbook, trigger policy, test transaction. |
| 8 | Gas optimization: audit and reduce gas or execution costs for primary user functions. | Benchmark report, before/after cost profile. |
| 9 | Upgradeability path: define and test proxy-admin, governance, or runtime upgrade procedures. | Upgrade plan, staging rehearsal, rollback path. |
| 10 | Reentrancy guards: validate state-changing functions against reentrancy and cross-call hazards. | Static analysis output, test vectors, audit notes. |
| 11 | Event emission: validate that every critical transaction emits indexable events. | Event schema, indexer tests, explorer examples. |
| 12 | ChainID and network config: ensure unique production-ready network identifiers. | Chain manifest, genesis hash, RPC metadata. |
| 13 | Timestamp and block dependencies: remove unsafe reliance on manipulable timing parameters. | Static analysis output, code review notes. |
| 14 | Overflow and underflow protection: confirm modern arithmetic safety. | Compiler/runtime settings, checked math review, dependency versions. |
| 15 | Wallet compatibility: test MetaMask, WalletConnect, Ledger, and Trezor where supported. | Compatibility matrix, screenshots, signed test transactions. |
| 16 | Node stability: verify public and private RPC nodes can handle high-concurrency requests. | Load-test report, latency/error-rate data, mitigation plan. |
| 17 | Explorer functionality: ensure explorer decodes and displays token metadata correctly. | Explorer screenshots, API responses, metadata schema. |
| 18 | Finality checks: confirm consensus provides definitive transaction finality. | Finality metrics, reorg policy, exchange confirmation guidance. |
| 19 | Snapshot testing: validate token balance snapshots for airdrops or migrations. | Snapshot scripts, checksums, dry-run output. |
| 20 | Emergency recovery: document and test recovery for stuck tokens or assets. | Recovery runbook, tabletop notes, restore logs. |

Focused public register:

```text
https://github.com/clarity-fintech/security/blob/main/docs/CORE_TECHNICAL_SECURITY.md
```

## Phase 2: Tokenomics and Economics

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 21 | Total supply verification. | Token manifest, genesis allocation, supply proof. |
| 22 | Vesting schedules. | Vesting source, schedule table, audit notes. |
| 23 | Inflationary controls. | Monetary policy, governance rules, simulation output. |
| 24 | Burn mechanism. | Burn proof, address derivation, transaction samples. |
| 25 | Liquidity locking. | Locker URL, lock duration, beneficiary details. |
| 26 | Tax or fee logic. | Code review, test coverage, atomic execution proof. |
| 27 | Oracle reliability. | Oracle config, fallback tests, stale-feed handling. |
| 28 | Slippage tolerance. | UI/API settings, transaction tests. |
| 29 | Treasury management. | Treasury policy, signer matrix, transaction runbook. |
| 30 | Staking and rewards APR validation. | Formula review, simulation sheet, edge-case tests. |

## Phase 3: Exchange Compliance

Use this section for controls 31-45 in the exchange listing data room.

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 31 | Legal opinion: obtain a memo regarding the token's security status. | Counsel-signed memo or exchange-ready legal summary. |
| 32 | AML policy: draft and implement an Anti-Money Laundering policy. | AML policy, owner, review cadence, escalation path. |
| 33 | KYC process: define identity verification workflow for platform users. | KYC vendor/process documentation, exception handling. |
| 34 | Travel Rule compliance: capture originator and beneficiary data where required. | Data model, vendor integration, trigger policy. |
| 35 | Sanctions filtering: screen addresses against OFAC and other sanctions lists. | Vendor/config evidence, sample alert, escalation runbook. |
| 36 | Risk disclosure: create clear public token and protocol risk statements. | Public risk statement URL, approval date, review owner. |
| 37 | Jurisdictional mapping: document excluded countries and regions. | Jurisdiction matrix, enforcement mechanism, update cadence. |
| 38 | Privacy policy: update public website data collection and cookies terms. | Public privacy policy URL, DPO/privacy review. |
| 39 | Terms of service: publicly host legally vetted terms. | Public terms URL, counsel review date. |
| 40 | Tax reporting tools: provide CSV/API transaction exports. | Export sample, API docs, retention policy. |
| 41 | Contact information: provide verified DPO or privacy contact. | DPO/privacy inbox, compliance contact, response SLA. |
| 42 | Entity registration: provide proof of company registration. | Certificate of incorporation or equivalent. |
| 43 | Proof of reserves: define custody verification methodology if applicable. | Reserve policy, wallet list policy, attestation model. |
| 44 | SOC 2 compliance: prepare or obtain Type 2 report if acting as custodian. | SOC 2 readiness report or final report. |
| 45 | Regulatory updates: create periodic compliance reporting process. | Compliance calendar, named owner, report template. |

Focused public register:

```text
https://github.com/clarity-fintech/security/blob/main/docs/EXCHANGE_COMPLIANCE.md
```

## Phase 4: Operational and Integration Readiness

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 46 | API documentation for REST/WebSocket market data. | API docs URL, OpenAPI spec, example responses. |
| 47 | Market maker agreement. | Executed agreement or provider confirmation. |
| 48 | Listing application preparation. | Listing kit, logos, descriptions, whitepaper, social links. |
| 49 | Listing fee escrow. | Finance approval, escrow confirmation where applicable. |
| 50 | Wallet integration for CEX. | Deposit/withdrawal specifications, address format, memo/tag rules. |
| 51 | Node maintenance. | 24/7 on-call schedule, escalation matrix. |
| 52 | Communication channel. | Exchange manager channel confirmation. |
| 53 | Monitoring and alerting. | Alert rules, dashboard URLs, test alert evidence. |
| 54 | Status page. | Public status page URL, incident policy. |
| 55 | Help desk. | Support channels, macros, staffing schedule. |
| 56 | Bug bounty program. | This repository and future bounty platform link. |
| 57 | Version control. | Production tags, signed commits, audit mapping. |
| 58 | Database backups. | Backup schedule, restore test report. |
| 59 | Server hardening. | Hardening baseline, scan output, exception list. |
| 60 | Deployment scripts. | CI workflows, deployment logs, rollback procedure. |

## Phase 5: Testing and Launch Simulation

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 61 | Load testing at 10x peak traffic. | Load-test report, throughput and error data. |
| 62 | UX testing for onboarding-to-swap or onboarding-to-account flow. | UX notes, completion rates, fixes. |
| 63 | Error handling. | QA checklist, screenshots, failed transaction cases. |
| 64 | Gas estimation. | Wallet test matrix, estimator logs. |
| 65 | Mobile responsiveness. | Device matrix, screenshots, issue log. |
| 66 | Cross-browser testing. | Chrome, Brave, and Firefox QA evidence. |
| 67 | Wallet connection persistence. | Session behavior tests. |
| 68 | Network switching. | Wallet screenshots, chain metadata. |
| 69 | Edge case transactions. | Test vectors, transaction logs. |
| 70 | Double-spend protection. | Race-condition tests, atomic execution notes. |
| 71 | Latency sensitivity. | Network simulation output, mitigation notes. |
| 72 | Front-end security. | CSP config, XSS scan output, remediation notes. |
| 73 | Dependency audits. | npm, Rust, Go, Python, and container audit reports. |
| 74 | Final mainnet simulation. | Staging/testnet dry-run logs and signoff. |
| 75 | Recovery test. | Node/database restore log, RTO/RPO notes. |

## Phase 6: Liquidity and Market Operations (76-82)

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 76 | Liquidity launch plan. | CEX/DEX/OTC/treasury liquidity plan and launch calendar. |
| 77 | Market surveillance. | Surveillance vendor/process and alert examples. |
| 78 | Spread and depth targets. | Market maker KPI sheet and exchange pair targets. |
| 79 | Deposit and withdrawal readiness. | Dry-run transaction IDs and exchange confirmation. |
| 80 | Liquidity incident escalation. | Incident playbook and owner matrix. |
| 81 | Price feed publication. | API docs, data source map, freshness SLA. |
| 82 | Listing asset metadata. | Logo, ticker, decimals, asset type, chain metadata, checksums. |

## Phase 7: Custody, Treasury, and Governance Controls (83-88)

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 83 | Treasury wallet register. | Approved treasury, reserve, liquidity, and operations wallet inventory. |
| 84 | Signer onboarding and offboarding. | Identity, device, access lifecycle, and offboarding checklist. |
| 85 | Governance proposal controls. | Review, simulation, approval, and execution runbook. |
| 86 | Timelock policy. | Delay windows, sensitive action policy, exception path. |
| 87 | Emergency signer recovery. | Recovery tabletop notes and backup verification. |
| 88 | Treasury reconciliation. | On-chain balance reconciliation and variance policy. |

## Phase 8: Data Room and Listing Evidence (89-94)

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 89 | Exchange data room index. | Security, legal, technical, market, and operational artifact map. |
| 90 | Whitepaper and litepaper control. | Current public document URLs, version history, approvals. |
| 91 | Audit evidence map. | Finding-to-remediation matrix, commit links, retest notes. |
| 92 | Public communications pack. | Exchange-approved descriptions, social links, and brand guide. |
| 93 | Questionnaire answer bank. | Reusable due diligence answers, owner, review date. |
| 94 | Evidence retention policy. | Retention duration, storage location, access controls. |

## Phase 9: Incident Response and Business Continuity (95-97)

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 95 | Security incident response plan. | Severity model, roles, containment actions, tabletop exercise. |
| 96 | Exchange incident notification. | Exchange notification template, contact list, approval flow. |
| 97 | Public disclosure process. | Coordinated disclosure policy, legal review, changelog process. |

## Phase 10: Post-Listing Monitoring and Governance (98-100)

| ID | Task | Evidence to attach in Notion |
|----|------|------------------------------|
| 98 | Post-listing health reviews. | 24-hour, 7-day, and 30-day liquidity/node/support review templates. |
| 99 | Ongoing dependency and vulnerability management. | Scheduled scans, issue triage, remediation SLA. |
| 100 | Periodic exchange reporting. | Supply, compliance, security, and operations reporting calendar. |

## Evidence Handling Rules

- Public policies, general checklists, and questionnaire URLs belong in GitHub.
- Private legal opinions, entity documents, KYC/vendor evidence, SOC 2 reports, market maker agreements, and exchange correspondence belong in private Notion or data-room attachments.
- Do not mark a control complete until the evidence artifact exists and an owner has reviewed it.
- Do not publish secrets, private keys, wallet signer identities, private customer data, or non-public exchange correspondence.
