# CLRTY Exchange Readiness Control Checklist

This document is the public exchange-readiness control index for CLRTY security, compliance, operations, liquidity, and integration review.

Use this document with the canonical security policy:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

## Status Key

| Status | Meaning |
|--------|---------|
| Active | Public process or repository control exists in this security program. |
| Evidence required | CLRTY must attach deployment logs, test output, runbooks, signed reports, or other proof before claiming completion. |
| External attestation required | Requires a third-party audit, legal memo, SOC 2 report, exchange confirmation, or similar independent artifact. |
| Operational readiness | Requires launch-day staffing, monitoring, service-level process, or incident response procedure. |

This checklist does not claim that every control is complete. It provides the listing-ready register used to track evidence, owners, and exchange follow-up.

## Pillar 1: Core Technical and Security

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 1 | Source code verification: publish and verify all contracts on block explorers or CLRTY-native explorers. | Explorer URLs, verified source hashes, release tags. | Evidence required |
| 2 | Third-party security audit: obtain a comprehensive smart contract or runtime audit. | Signed report from CertiK, OpenZeppelin, or equivalent reviewer. | External attestation required |
| 3 | Audit remediation: implement and document all audit findings. | Remediation matrix, commits, retest report. | Evidence required |
| 4 | Penetration testing: perform off-chain API and infrastructure stress tests. | Scope letter, test report, remediation notes. | External attestation required |
| 5 | Private key management: deploy HSM, hardware wallet, or multisig controls for treasury funds. | Custody architecture, signer policy, recovery procedure. | Evidence required |
| 6 | Admin and governance access: require multisig approval for owner or admin functions. | Governance config, signer threshold, transaction examples. | Evidence required |
| 7 | Circuit breakers: implement emergency pause or freeze controls where applicable. | Pause control documentation, test transaction, operator runbook. | Evidence required |
| 8 | Gas optimization: audit and reduce cost for primary user functions. | Benchmark report, before/after measurements. | Evidence required |
| 9 | Upgradeability path: define and test proxy-admin or runtime upgrade procedures if upgradeable. | Upgrade plan, testnet rehearsal, governance approval path. | Evidence required |
| 10 | Reentrancy guards: ensure state-changing functions use non-reentrant controls where relevant. | Static analysis output, audit notes, code references. | Evidence required |
| 11 | Event emission: every critical transaction emits events for off-chain monitoring. | Event schema, indexer tests, explorer examples. | Evidence required |
| 12 | ChainID and network config: use unique production-ready network identifiers. | Chain manifest, genesis configuration, RPC metadata. | Evidence required |
| 13 | Timestamp and block dependencies: remove unsafe reliance on manipulable timing parameters. | Static analysis output, review notes. | Evidence required |
| 14 | Overflow and underflow protection: use modern arithmetic safety in Solidity, Rust, or runtime modules. | Compiler settings, audit notes, dependency versions. | Evidence required |
| 15 | Wallet compatibility: test MetaMask, WalletConnect, Ledger, and Trezor flows where supported. | Compatibility matrix, screenshots, signed test transactions. | Evidence required |
| 16 | Node stability: public and private RPC nodes handle high-concurrency requests. | Load-test report, RPC latency and error-rate data. | Evidence required |
| 17 | Explorer functionality: explorer decodes and displays token metadata correctly. | Explorer screenshots, API responses, metadata schema. | Evidence required |
| 18 | Finality checks: consensus provides definitive transaction finality. | Consensus documentation, finality metrics, reorg policy. | Evidence required |
| 19 | Snapshot testing: validate token balance snapshots for airdrop or migration mechanics. | Snapshot scripts, checksums, dry-run output. | Evidence required |
| 20 | Emergency recovery: document and test recovery of stuck tokens or assets. | Recovery runbook, tabletop exercise notes. | Evidence required |

## Pillar 2: Tokenomics and Economics

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 21 | Total supply verification: confirm circulating versus total supply math is immutable or governed. | Token manifest, genesis allocation, supply proof. | Evidence required |
| 22 | Vesting schedules: program and audit automated vesting and cliff contracts or modules. | Vesting contract/module source, schedule table, audit notes. | Evidence required |
| 23 | Inflationary controls: hardcode or DAO-govern emission caps. | Monetary policy, governance rules, simulation output. | Evidence required |
| 24 | Burn mechanism: verify burn address or module is unspendable if burns exist. | Burn proof, address derivation, transaction samples. | Evidence required |
| 25 | Liquidity locking: use a trusted audited locker for team or initial liquidity where applicable. | Locker URL, lock duration, beneficiary details. | External attestation required |
| 26 | Tax and fee logic: reflection or tax logic must execute atomically if used. | Code review, test coverage, swap-and-liquify proof. | Evidence required |
| 27 | Oracle reliability: price feeds must include validity, fallback, and delay-tolerant logic. | Oracle config, fallback tests, stale-feed handling. | Evidence required |
| 28 | Slippage tolerance: DEX interfaces use configurable slippage logic. | UI/API settings, transaction tests. | Evidence required |
| 29 | Treasury management: define and test multisig movement of treasury assets. | Treasury policy, signer matrix, transaction runbook. | Evidence required |
| 30 | Staking and rewards APR: validate APY calculations mathematically. | Formula review, simulation sheet, edge-case tests. | Evidence required |

## Pillar 3: Exchange Compliance

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 31 | Legal opinion: obtain a token status memo. | Counsel-signed memo or exchange-ready legal summary. | External attestation required |
| 32 | AML policy: draft and implement anti-money-laundering policy. | AML policy, owner, update cadence. | External attestation required |
| 33 | KYC process: define identity verification workflow for platform users. | KYC vendor/process documentation, escalation policy. | External attestation required |
| 34 | Travel Rule compliance: capture originator and beneficiary data where required. | Data model, vendor integration, jurisdictional trigger policy. | External attestation required |
| 35 | Sanctions filtering: screen addresses against OFAC and other sanctions lists. | Vendor/config evidence, sample alert, escalation runbook. | External attestation required |
| 36 | Risk disclosure: publish clear public protocol and token risks. | Public risk statement URL, review history. | Evidence required |
| 37 | Jurisdictional mapping: document excluded countries and restricted regions. | Jurisdiction matrix, enforcement mechanism. | External attestation required |
| 38 | Privacy policy: update website data collection, cookies, and retention terms. | Public privacy policy URL, DPO review. | Evidence required |
| 39 | Terms of service: publicly host legally vetted terms. | Public terms URL, counsel review date. | External attestation required |
| 40 | Tax reporting tools: provide transaction exports in CSV or API formats. | Export sample, API docs, data retention policy. | Evidence required |
| 41 | Contact information: provide verified DPO or privacy contact. | DPO contact, privacy inbox, response SLA. | Evidence required |
| 42 | Entity registration: provide proof of company registration. | Certificate of incorporation or equivalent. | External attestation required |
| 43 | Proof of reserves: define methodology for public custody verification if applicable. | Reserve policy, attestation model, wallet list. | External attestation required |
| 44 | SOC 2 compliance: prepare or obtain Type 2 reports if acting as a custodian. | SOC 2 readiness report or final report. | External attestation required |
| 45 | Regulatory updates: create periodic compliance reporting process. | Compliance calendar, owner, report template. | Operational readiness |

## Pillar 4: Operational and Integration Readiness

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 46 | API documentation: publish REST and WebSocket docs for market data, price, and volume. | API docs URL, OpenAPI spec, example responses. | Evidence required |
| 47 | Market maker agreement: sign with reputable liquidity provider. | Executed agreement or exchange-confirmed provider letter. | External attestation required |
| 48 | Listing application preparation: organize logos, descriptions, whitepapers, and social links. | Listing kit folder, checksums, owner contact. | Evidence required |
| 49 | Listing fee escrow: budget and secure listing fees or market-making deposits. | Finance approval, escrow confirmation where applicable. | External attestation required |
| 50 | Wallet integration for CEX: define deposit and withdrawal technical specifications. | Exchange integration guide, address format, memo/tag rules. | Evidence required |
| 51 | Node maintenance: staff 24/7 technical coverage for mainnet day. | On-call schedule, escalation matrix. | Operational readiness |
| 52 | Communication channel: establish direct channel with exchange listing managers. | Slack, Telegram, Discord, or email thread confirmation. | Operational readiness |
| 53 | Monitoring and alerting: alert on unusual transaction volume and node downtime. | Alert rules, dashboard URLs, test alert evidence. | Evidence required |
| 54 | Status page: launch a public status dashboard. | Public status page URL, incident policy. | Evidence required |
| 55 | Help desk: staff launch-day user support. | Support channels, macros, staffing schedule. | Operational readiness |
| 56 | Bug bounty program: launch public vulnerability disclosure or bounty program. | This repository and future bounty platform link. | Active |
| 57 | Version control: tag and audit all production code in Git. | Release tags, signed commits, audit mapping. | Evidence required |
| 58 | Database backups: validate off-chain recovery protocols. | Backup schedule, restore test report. | Evidence required |
| 59 | Server hardening: disable unnecessary ports and services. | Hardening baseline, scan output, exception list. | Evidence required |
| 60 | Deployment scripts: maintain repeatable CI/CD deployment pipelines. | CI workflows, deployment logs, rollback procedure. | Evidence required |

## Pillar 5: Testing and Launch Simulation

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 61 | Load testing: simulate 10x peak traffic on dApp, API, bridge, or RPC surfaces. | Load-test report, throughput and error data. | Evidence required |
| 62 | UX testing: independent users complete onboarding-to-swap or onboarding-to-account flow. | UX notes, completion rates, fixes. | Evidence required |
| 63 | Error handling: UI provides actionable errors for failed transactions. | QA checklist, screenshots, test cases. | Evidence required |
| 64 | Gas estimation: calibrate gas estimators for wallet integration. | Wallet test matrix, estimator logs. | Evidence required |
| 65 | Mobile responsiveness: dApp flows work on standard mobile browsers. | Device matrix, screenshots, issue log. | Evidence required |
| 66 | Cross-browser testing: validate Chrome, Brave, and Firefox. | Browser matrix, automated or manual QA evidence. | Evidence required |
| 67 | Wallet connection persistence: connection state survives refresh where appropriate. | Test cases, session behavior notes. | Evidence required |
| 68 | Network switching: dApp can trigger switch-network requests. | Wallet screenshots, chain metadata. | Evidence required |
| 69 | Edge case transactions: test very low and very high balance scenarios. | Test vectors, transaction logs. | Evidence required |
| 70 | Double-spend protection: all multi-step actions execute atomically. | Design notes, race-condition tests. | Evidence required |
| 71 | Latency sensitivity: test high-latency and mobile network conditions. | Network simulation output, UX mitigation notes. | Evidence required |
| 72 | Front-end security: check for XSS and Content Security Policy issues. | CSP config, scan output, remediation notes. | Evidence required |
| 73 | Dependency audits: scan npm, Rust, Go, Python, and container dependencies. | Audit reports, lockfile review. | Evidence required |
| 74 | Final mainnet simulation: dry run in dedicated staging or testnet environment. | Runbook, timestamped logs, signoff. | Evidence required |
| 75 | Recovery test: restore node or database from backup. | Restore log, RTO/RPO notes, operator signoff. | Evidence required |

## Pillar 6: Liquidity and Market Operations

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 76 | Liquidity launch plan: define CEX, DEX, OTC, and treasury liquidity responsibilities. | Liquidity plan, owners, launch calendar. | External attestation required |
| 77 | Market surveillance: monitor wash trading, spoofing, abnormal spreads, and suspicious volume. | Surveillance vendor/process, alert examples. | Operational readiness |
| 78 | Spread and depth targets: establish target depth and spread ranges for launch pairs. | Market maker KPI sheet, exchange pair targets. | External attestation required |
| 79 | Deposit and withdrawal readiness: rehearse exchange deposit and withdrawal flows. | Dry-run transaction IDs, exchange confirmation. | Evidence required |
| 80 | Liquidity incident escalation: define actions for broken markets, halted deposits, or stuck withdrawals. | Incident playbook, owner matrix. | Operational readiness |
| 81 | Price feed publication: publish reliable price, volume, and supply inputs for listing platforms. | API docs, data source map, freshness SLA. | Evidence required |
| 82 | Listing asset metadata: validate logo, ticker, decimals, asset type, and chain metadata. | Listing kit, metadata manifest, checksum file. | Evidence required |

## Pillar 7: Custody, Treasury, and Governance Controls

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 83 | Treasury wallet register: maintain approved treasury, reserve, liquidity, and operations wallets. | Wallet inventory, signing policy, owner approvals. | Evidence required |
| 84 | Signer onboarding and offboarding: document identity, device, and access lifecycle. | Signer policy, offboarding checklist. | Evidence required |
| 85 | Governance proposal controls: review and simulate proposals before execution. | Governance runbook, simulation output, approval logs. | Evidence required |
| 86 | Timelock policy: define delay windows for sensitive governance or admin actions. | Timelock config, exception policy. | Evidence required |
| 87 | Emergency signer recovery: test recovery if a signer, HSM, or hardware wallet is lost. | Recovery tabletop notes, backup verification. | Evidence required |
| 88 | Treasury reconciliation: reconcile on-chain treasury balances with internal records. | Reconciliation report, variance policy. | Operational readiness |

## Pillar 8: Data Room and Listing Evidence

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 89 | Exchange data room index: organize security, legal, technical, market, and operational artifacts. | Data room index, access policy, update owner. | Evidence required |
| 90 | Whitepaper and litepaper control: maintain current public token and network disclosures. | Document URLs, version history, approval log. | Evidence required |
| 91 | Audit evidence map: map each audit finding to remediation evidence. | Audit matrix, commit links, retest notes. | Evidence required |
| 92 | Public communications pack: maintain exchange-approved descriptions and social links. | Communications pack, logo files, brand guide. | Evidence required |
| 93 | Questionnaire answer bank: maintain reusable answers for exchange due diligence. | Answer bank, review owner, date of last update. | Operational readiness |
| 94 | Evidence retention policy: define how long listing evidence and logs are retained. | Retention policy, storage location, access controls. | Operational readiness |

## Pillar 9: Incident Response and Business Continuity

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 95 | Security incident response plan: define severity, roles, communication, and containment actions. | Incident runbook, escalation contacts, tabletop exercise. | Operational readiness |
| 96 | Exchange incident notification: define who notifies exchanges for halted deposits, consensus issues, or exploits. | Notification template, contact list, approval flow. | Operational readiness |
| 97 | Public disclosure process: coordinate fixes, affected-user notice, and disclosure timing. | Disclosure policy, legal review, changelog process. | Active |

## Pillar 10: Post-Listing Monitoring and Governance

| ID | Control | Evidence expectation | Status |
|----|---------|----------------------|--------|
| 98 | Post-listing health reviews: review liquidity, node health, support load, and incidents after listing. | 24-hour, 7-day, and 30-day review templates. | Operational readiness |
| 99 | Ongoing dependency and vulnerability management: keep audit cadence and dependency scans active. | Scheduled scans, issue triage, remediation SLA. | Operational readiness |
| 100 | Periodic exchange reporting: provide updated supply, compliance, security, and operations evidence. | Reporting calendar, owner, exchange distribution list. | Operational readiness |

## Primary Evidence Links

| Evidence area | Repository document |
|---------------|---------------------|
| Security policy URL | [`../SECURITY.md`](../SECURITY.md) |
| Reporting instructions | [`REPORTING.md`](REPORTING.md) |
| Security scope | [`SCOPE.md`](SCOPE.md) |
| Response targets | [`RESPONSE_TIMELINE.md`](RESPONSE_TIMELINE.md) |
| Safe harbor | [`SAFE_HARBOR.md`](SAFE_HARBOR.md) |
| Program status | [`PROGRAM_STATUS.md`](PROGRAM_STATUS.md) |
| Core technical controls | [`CORE_TECHNICAL_SECURITY.md`](CORE_TECHNICAL_SECURITY.md) |
| Exchange compliance controls | [`EXCHANGE_COMPLIANCE.md`](EXCHANGE_COMPLIANCE.md) |
| Notion-ready evidence tracker | [`NOTION_EXCHANGE_READINESS_PAGE.md`](NOTION_EXCHANGE_READINESS_PAGE.md) |
| Notion sync setup | [`NOTION_SYNC_SETUP.md`](NOTION_SYNC_SETUP.md) |
