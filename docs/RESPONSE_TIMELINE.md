# Security Response Timeline

CLRTY uses a severity-based response process for coordinated vulnerability disclosure.

## Severity Matrix

| Severity | Examples |
|----------|----------|
| Critical | Loss of funds, unauthorized mint/supply mutation, private key exposure, governance bypass, production RCE |
| High | Authentication bypass, privilege escalation, sensitive data exposure, pack integrity compromise, exploitable API logic bug |
| Medium | Limited cross-site scripting, non-critical authorization issue, misleading security metadata, moderate data exposure |
| Low | Hardening issue, low-impact misconfiguration, documentation inconsistency with security relevance |

## Target Timeline

| Severity | Acknowledgment | Triage | Mitigation / Fix |
|----------|----------------|--------|------------------|
| Critical | 24 hours | 72 hours | Immediate mitigation, followed by coordinated patch |
| High | 48 hours | 5 business days | Prioritized patch or mitigation plan |
| Medium | 5 business days | 10 business days | Scheduled patch or documented risk acceptance |
| Low | 10 business days | 20 business days | Backlog, documentation update, or hardening task |

These are target timelines, not guarantees. CLRTY may adjust based on deployment status, exploit activity, third-party dependencies, chain/network conditions, legal obligations, or exchange-listing requirements.

## Process

1. Intake and acknowledgment.
2. Reproduction and severity classification.
3. Containment if active risk exists.
4. Patch, configuration change, documentation fix, or compensating control.
5. Regression test or audit review.
6. Coordinated disclosure after remediation where appropriate.

## Emergency Handling

If a report indicates active exploitation, loss-of-funds risk, key exposure, or governance compromise, CLRTY may activate emergency controls, circuit breakers, custody procedures, or temporary service restrictions while the issue is investigated.
