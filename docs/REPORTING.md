# Vulnerability Reporting Guide

Send vulnerability reports to:

```text
security@clarity-fintech.com
```

Do not disclose unresolved vulnerabilities publicly or in GitHub issues.

## Include in Your Report

- Affected CLRTY component, repository, URL, endpoint, contract, CLI command, or package.
- Reproduction steps with expected and actual behavior.
- Proof of concept, payload, logs, screenshots, transaction hashes, or relevant request/response samples.
- Impact assessment: funds, user data, signing keys, governance controls, node operations, availability, or integrity.
- Environment details such as commit hash, package version, browser, OS, chain/network, API base URL, and wallet type.
- Whether the issue is actively exploitable or already exploited.
- Your name or handle and preferred contact method.

## Sensitive Data Handling

If testing exposes secrets, private user data, signing material, unreleased code, or production infrastructure:

1. Stop testing immediately.
2. Do not copy, retain, transfer, or modify the data.
3. Report the exposure privately with enough metadata for CLRTY to locate and mitigate it.

## Report Template

```text
Title:
Reporter:
Affected surface:
Severity estimate:
Summary:
Steps to reproduce:
Expected result:
Actual result:
Impact:
Proof of concept:
Suggested remediation:
Disclosure preference:
```
