# Notion Security Page Sync Setup

The CLRTY exchange-readiness security page is intended to live under the same Notion workspace and parent page as the live metrics feed:

```text
VIS CLARITY PnL / CLRTY DATA CENTER
```

Public source of truth:

```text
https://github.com/clarity-fintech/security/blob/main/docs/NOTION_EXCHANGE_READINESS_PAGE.md
```

Main CLRTY project source uploaded by the sync script:

```text
docs/security/NOTION_EXCHANGE_READINESS_PAGE.md
```

## Required Environment

Set these in the private `.env` for the main CLRTY project:

```bash
NOTION_TOKEN=ntn_...
NOTION_DATA_CENTER_PAGE_ID=39170476-0d24-804d-b75a-d141f9757285
NOTION_SECURITY_PAGE_ID=
NOTION_SECURITY_PARENT_PAGE_ID=
NOTION_SECURITY_PAGE_TITLE=CLRTY Exchange Readiness / Security Evidence Register
NOTION_SECURITY_MARKDOWN=docs/security/NOTION_EXCHANGE_READINESS_PAGE.md
```

`NOTION_SECURITY_PAGE_ID` is optional. If it is empty, the sync script searches for a child page with the configured title under `NOTION_DATA_CENTER_PAGE_ID`; if it cannot find one, it creates it.

## Sync Commands

From the main CLRTY project:

```bash
python3 scripts/metrics/sync_notion_security.py
```

or:

```bash
make data-center-security-notion
```

From this security repository:

```bash
python3 scripts/sync_notion_security.py
```

Full metrics, launch tracker, and security page sync:

```bash
make launch-sync-all
```

## Evidence Handling

- Keep public policy, checklist, and questionnaire URLs in GitHub.
- Keep legal opinions, entity documents, vendor evidence, SOC 2 reports, market maker agreements, and exchange correspondence in private Notion or data-room attachments.
- Do not publish secrets, private keys, signer identities, private user data, or non-public exchange communications.
