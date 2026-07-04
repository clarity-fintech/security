#!/usr/bin/env python3
"""Create or refresh the CLRTY security/exchange-readiness page in Notion."""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "docs/NOTION_EXCHANGE_READINESS_PAGE.md"
DEFAULT_TITLE = "CLRTY Exchange Readiness / Security Evidence Register"
NOTION_VERSION = "2022-06-28"


def notion_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_request(method: str, url: str, token: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=notion_headers(token), method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            return json.loads(res.read().decode())
    except urllib.error.HTTPError as exc:
        err = exc.read().decode()
        raise RuntimeError(f"Notion {exc.code}: {err}") from exc


def rich_text(content: str) -> list[dict]:
    return [{"type": "text", "text": {"content": content[:2000]}}] if content else []


def text_block(block_type: str, content: str) -> dict:
    return {"object": "block", "type": block_type, block_type: {"rich_text": rich_text(content)}}


def code_block(content: str) -> dict:
    return {
        "object": "block",
        "type": "code",
        "code": {"rich_text": rich_text(content[:2000]), "language": "markdown"},
    }


def flush_buffer(blocks: list[dict], buffer: list[str], as_code: bool = False) -> None:
    if not buffer:
        return
    content = "\n".join(buffer).strip()
    if content:
        blocks.append(code_block(content) if as_code else text_block("paragraph", content))
    buffer.clear()


def markdown_to_blocks(markdown: str) -> list[dict]:
    blocks: list[dict] = []
    paragraph: list[str] = []
    code: list[str] = []
    table: list[str] = []
    in_code = False

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        if line.startswith("```"):
            flush_buffer(blocks, paragraph)
            flush_buffer(blocks, table, as_code=True)
            if in_code:
                flush_buffer(blocks, code, as_code=True)
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code.append(line)
            continue
        if not line.strip():
            flush_buffer(blocks, paragraph)
            flush_buffer(blocks, table, as_code=True)
            continue
        if line.startswith("|"):
            flush_buffer(blocks, paragraph)
            table.append(line)
            continue
        flush_buffer(blocks, table, as_code=True)

        if line.startswith("# "):
            flush_buffer(blocks, paragraph)
            blocks.append(text_block("heading_1", line[2:].strip()))
        elif line.startswith("## "):
            flush_buffer(blocks, paragraph)
            blocks.append(text_block("heading_2", line[3:].strip()))
        elif line.startswith("### "):
            flush_buffer(blocks, paragraph)
            blocks.append(text_block("heading_3", line[4:].strip()))
        elif line.startswith("- "):
            flush_buffer(blocks, paragraph)
            blocks.append(text_block("bulleted_list_item", line[2:].strip()))
        elif re.match(r"^\d+\. ", line):
            flush_buffer(blocks, paragraph)
            blocks.append(text_block("numbered_list_item", re.sub(r"^\d+\. ", "", line).strip()))
        else:
            paragraph.append(line)

    flush_buffer(blocks, paragraph)
    flush_buffer(blocks, table, as_code=True)
    flush_buffer(blocks, code, as_code=True)
    return blocks


def list_page_blocks(token: str, page_id: str) -> list[dict]:
    results: list[dict] = []
    cursor = None
    while True:
        url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        resp = notion_request("GET", url, token)
        results.extend(resp.get("results", []))
        if not resp.get("has_more"):
            return results
        cursor = resp.get("next_cursor")


def discover_child_page(token: str, parent_page_id: str, title: str) -> str:
    for block in list_page_blocks(token, parent_page_id):
        if block.get("type") == "child_page" and block.get("child_page", {}).get("title") == title:
            return block.get("id", "")
    return ""


def clear_page_children(token: str, page_id: str) -> None:
    for block in list_page_blocks(token, page_id):
        block_id = block.get("id")
        if block_id:
            notion_request("PATCH", f"https://api.notion.com/v1/blocks/{block_id}", token, {"archived": True})


def append_children(token: str, page_id: str, blocks: list[dict]) -> None:
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    for idx in range(0, len(blocks), 100):
        notion_request("PATCH", url, token, {"children": blocks[idx : idx + 100]})


def create_child_page(token: str, parent_page_id: str, title: str) -> str:
    resp = notion_request(
        "POST",
        "https://api.notion.com/v1/pages",
        token,
        {
            "parent": {"page_id": parent_page_id},
            "properties": {"title": [{"type": "text", "text": {"content": title[:200]}}]},
        },
    )
    return resp["id"]


def main() -> int:
    token = os.environ.get("NOTION_TOKEN", "").strip()
    parent_page_id = (
        os.environ.get("NOTION_SECURITY_PARENT_PAGE_ID", "").strip()
        or os.environ.get("NOTION_DATA_CENTER_PAGE_ID", "").strip()
    )
    page_id = os.environ.get("NOTION_SECURITY_PAGE_ID", "").strip()
    title = os.environ.get("NOTION_SECURITY_PAGE_TITLE", DEFAULT_TITLE).strip() or DEFAULT_TITLE
    source = Path(os.environ.get("NOTION_SECURITY_MARKDOWN", str(DEFAULT_SOURCE))).expanduser()

    if not token:
        print("[security-notion] SKIP: set NOTION_TOKEN", file=sys.stderr)
        return 0
    if not source.is_file():
        print(f"[security-notion] ERROR: missing markdown source {source}", file=sys.stderr)
        return 1
    if not page_id and not parent_page_id:
        print(
            "[security-notion] SKIP: set NOTION_SECURITY_PAGE_ID or NOTION_DATA_CENTER_PAGE_ID",
            file=sys.stderr,
        )
        return 0

    if not page_id and parent_page_id:
        page_id = discover_child_page(token, parent_page_id, title)
    created = False
    if not page_id:
        page_id = create_child_page(token, parent_page_id, title)
        created = True
        print(f"[security-notion] created page id (set NOTION_SECURITY_PAGE_ID): {page_id}")

    blocks = markdown_to_blocks(source.read_text())
    clear_page_children(token, page_id)
    append_children(token, page_id, blocks)
    action = "created" if created else "updated"
    print(f"[security-notion] OK {action} page={page_id} blocks={len(blocks)} source={source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
