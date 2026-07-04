# CLRTY Security Policy

This repository is the canonical security policy and coordinated vulnerability disclosure page for the CLRTY ecosystem.

Use this URL for exchange, listing, vendor, and institutional questionnaire fields that request a Bug Bounty or Security Policy page:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

## Reporting a Vulnerability

Report suspected vulnerabilities privately by email:

```text
security@clarity-fintech.com
```

Do not open a public GitHub issue for a live vulnerability. Include enough detail for the CLRTY security team to reproduce and assess the issue:

- Affected product, repository, endpoint, contract, CLI command, or document.
- Steps to reproduce, proof of concept, logs, screenshots, or transaction hashes.
- Expected impact and whether user funds, private data, governance, signing keys, or infrastructure availability are affected.
- Your preferred contact method for follow-up.

## Supported Surfaces

The current security reporting scope covers:

| Surface | Examples |
|---------|----------|
| CLRTY-1 L1 | Native `uclrty`, settlement, governance, launch manifests |
| `clrty-api` | Public REST/RPC surfaces, account registration, wallet and node routes |
| Clarity Fortress | Developer walkthrough, faucet, explorer, playground, node onboarding |
| PRISM CLI | `clrt` account, pack, wallet, chain, and terminal flows |
| Wallet Integration | Registry, wallet SDK, zero-friction listing kit, access packs |
| Node Deployment Kit | Operator scripts, node registration, heartbeat, DePIN onboarding |
| Developer SDKs | TypeScript, Go, Rust, examples, and integration docs |

Third-party platforms, hosted infrastructure outside CLRTY control, social engineering, physical attacks, spam, and denial-of-service testing are out of scope unless explicitly authorized in writing.

## Security Response Targets

| Severity | Initial acknowledgment | Triage target | Remediation target |
|----------|------------------------|---------------|--------------------|
| Critical | 24 hours | 72 hours | Immediate mitigation, then coordinated fix |
| High | 48 hours | 5 business days | Prioritized fix or mitigation plan |
| Medium | 5 business days | 10 business days | Scheduled fix |
| Low | 10 business days | 20 business days | Backlog or documentation update |

The CLRTY security team may accelerate or extend timelines based on exploitability, deployment state, third-party dependencies, and audit requirements.

## Rewards and Bug Bounty Status

CLRTY currently operates a coordinated vulnerability disclosure program. Paid bounty awards are discretionary until a formal bounty schedule is published through an approved platform or governance process.

Do not rely on any reward unless it is confirmed in writing by CLRTY before or during triage.

## Exchange Readiness References

For broader exchange-listing, compliance, liquidity, operational, and technical readiness review, use the public readiness register:

```text
https://github.com/clarity-fintech/security/blob/main/docs/EXCHANGE_READINESS_CHECKLIST.md
```

For CLRTY-1 live-version chain validation and stress evidence, use:

```text
https://github.com/clarity-fintech/security/blob/main/docs/CLRTY1_LIVE_CHAIN_STRESS_REPORT.md
```

For the five-pillar market launch and exchange listing checklist, use:

```text
https://github.com/clarity-fintech/security/blob/main/docs/MARKET_LAUNCH_EXCHANGE_LISTING_100.md
```

Focused evidence registers are also available for core technical security and exchange compliance:

- `docs/CORE_TECHNICAL_SECURITY.md`
- `docs/EXCHANGE_COMPLIANCE.md`

For Notion, listing data rooms, or internal launch tracking, mirror:

```text
https://github.com/clarity-fintech/security/blob/main/docs/NOTION_EXCHANGE_READINESS_PAGE.md
```

Notion sync setup for the same Data Center page used by CLRTY metrics:

```text
https://github.com/clarity-fintech/security/blob/main/docs/NOTION_SYNC_SETUP.md
```

## Safe Harbor

CLRTY intends to work constructively with good-faith researchers who:

- Report vulnerabilities privately and promptly.
- Avoid privacy violations, data destruction, service disruption, extortion, or public disclosure before remediation.
- Test only against systems they own or are explicitly authorized to test.
- Stop testing and notify CLRTY immediately if sensitive data, keys, funds, or live infrastructure are exposed.

Good-faith research that follows this policy will be treated as authorized activity to the extent permitted by applicable law and CLRTY's ability to control the affected system.

## Audit and Governance References

Security reports are reviewed alongside CLRTY's existing audit and governance controls:

- Security audit completion gates: `docs/audit/SECURITY_AUDIT_COMPLETION_GATES.md`
- Audit data room: `docs/audit/audit_data_room.md`
- CLRTY-1 mass defense architecture: `docs/security/CLRTY1_MDA.md`
- CLRTY-1 mass security doctrine: `docs/security/CLRTY1_MSD.md`
- Risk disclosure statement: `docs/compliance/data_room/legal_templates/risk_disclosure_statement.md`

## Public Disclosure

Public disclosure should occur only after CLRTY confirms a fix or mitigation is deployed, affected parties are notified where necessary, and any legal or exchange-listing obligations are satisfied.
