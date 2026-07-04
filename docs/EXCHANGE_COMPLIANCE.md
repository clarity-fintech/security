# Exchange Compliance Evidence Register

This page expands Phase 3 of the CLRTY exchange-readiness checklist into a focused compliance evidence register for exchange listing teams, institutional reviewers, and legal/compliance owners.

Canonical security policy:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

## Important Positioning

This page is an evidence register, not a legal opinion. Items requiring counsel, regulator, auditor, compliance vendor, or SOC 2 attestation must be backed by the relevant external artifact before CLRTY represents them as complete.

## Phase 3 Controls

| ID | Control | Required evidence before completion |
|----|---------|-------------------------------------|
| 31 | Legal opinion | Obtain a legal memo addressing token status, jurisdictional considerations, transfer restrictions, and any required disclosures. Store counsel name, date, scope, and public/non-public handling rules. |
| 32 | AML policy | Maintain a written AML policy covering risk assessment, monitoring, escalation, recordkeeping, and periodic review. |
| 33 | KYC process | Define when identity verification is required, what vendor/process is used, what data is collected, and how failed or high-risk reviews are handled. |
| 34 | Travel Rule compliance | Document how originator and beneficiary information is captured, transmitted, retained, or determined not applicable for each product surface. |
| 35 | Sanctions filtering | Implement address, entity, and jurisdiction screening against OFAC and other applicable lists. Preserve vendor configuration, alert examples, and escalation runbook. |
| 36 | Risk disclosure | Publish clear public disclosures covering token volatility, technology risk, protocol risk, market risk, regulatory risk, and availability risk. |
| 37 | Jurisdictional mapping | Maintain an allowed/restricted jurisdiction matrix, supporting rationale, enforcement mechanism, and update cadence. |
| 38 | Privacy policy | Publish privacy policy covering data collection, cookies, analytics, retention, user rights, subprocessors, and contact method. |
| 39 | Terms of service | Publicly host legally reviewed terms covering acceptable use, limitations, disclosures, dispute process, and service availability. |
| 40 | Tax reporting tools | Provide exports or APIs that help users and institutions retrieve transaction history, timestamps, asset amounts, and wallet/account references. |
| 41 | Contact information | Provide verified compliance, privacy, and security contacts. If applicable, publish a DPO or privacy office contact. |
| 42 | Entity registration | Maintain proof of company formation, registered address, officers/directors as appropriate, and good-standing documents where required. |
| 43 | Proof of reserves | If CLRTY holds reserves or custodial assets, publish reserve methodology, wallet list policy, liability calculation approach, and attestation cadence. |
| 44 | SOC 2 compliance | If CLRTY acts as a custodian or handles sensitive institutional workflows, prepare a SOC 2 readiness path or obtain Type 2 reporting. |
| 45 | Regulatory updates | Maintain an update process for changes in law, exchange requirements, sanctions rules, custody posture, and public disclosures. |

## Compliance Evidence Packet

For an exchange or institutional listing review, CLRTY should assemble:

- Legal opinion or counsel-prepared legal summary.
- AML/KYC/Travel Rule policy set.
- Sanctions screening procedure and vendor evidence.
- Risk disclosure, privacy policy, and terms URLs.
- Jurisdictional restriction matrix.
- Entity registration and good-standing artifacts.
- Tax export/API documentation.
- Proof-of-reserves policy if custody or reserve claims are made.
- SOC 2 readiness or report status if custodial duties apply.
- Compliance reporting calendar and named owner.

## Public Questionnaire Answer

For a Bug Bounty, Security Policy, or Vulnerability Disclosure URL field, continue to use:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

For broader exchange-readiness evidence, use:

```text
https://github.com/clarity-fintech/security/blob/main/docs/EXCHANGE_READINESS_CHECKLIST.md
```

## Relationship to the Full Checklist

These controls correspond to items 31-45 in [`EXCHANGE_READINESS_CHECKLIST.md`](EXCHANGE_READINESS_CHECKLIST.md).
