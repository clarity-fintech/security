# Security Program Scope

This scope describes systems CLRTY currently accepts coordinated vulnerability disclosure reports for.

## In Scope

| Category | Examples | Priority |
|----------|----------|----------|
| CLRTY-1 L1 | Native `uclrty`, genesis/listing manifests, governance and settlement code | Critical |
| Public API | `clrty-api`, REST/RPC endpoints, account registration, wallet, node, and listing routes | Critical |
| Clarity Fortress | Developer walkthrough, faucet, explorer, playground, node onboarding | High |
| PRISM CLI | `clrt` commands, account flows, pack downloads, terminal workflows | High |
| Wallet Integration | SDKs, asset registry, zero-friction kit, downloadable packs | High |
| Node Deployment Kit | Node registration, heartbeat, DePIN/operator scripts | High |
| Developer Kit | SDKs, examples, install docs, integration templates | Medium |
| Research Kit | Data packs, simulation outputs, institutional disclosure artifacts | Medium |
| Security docs | Policy, audit gates, public trust and listing documentation | Medium |

## Vulnerability Classes of Interest

- Unauthorized transfer, balance mutation, minting, burning, or supply drift.
- Authentication, authorization, or access-control bypass.
- Governance, timelock, multisig, or emergency-control bypass.
- Exposure of private keys, tokens, credentials, or sensitive user data.
- Remote code execution, command injection, path traversal, or unsafe deserialization.
- Download integrity failures, checksum mismatch, or supply-chain compromise.
- API logic bugs that affect wallet, node, listing, settlement, or account flows.
- Cross-site scripting, open redirect, or session issues in CLRTY-operated web surfaces.

## Out of Scope

- Social engineering, phishing, spam, or impersonation.
- Physical attacks, coercion, or attacks against employees, vendors, or users.
- Denial-of-service, load testing, or resource exhaustion without written approval.
- Automated scanner output without a reproducible security impact.
- Issues requiring compromised devices, browsers, wallets, or dependencies outside CLRTY control.
- Third-party services unless the vulnerability is caused by CLRTY configuration or integration code.
- Public disclosure before CLRTY has validated and remediated the issue.

## Authorization Limits

Research must be limited to accounts, wallets, nodes, devices, data, and systems you own or are explicitly authorized to test.
