#!/usr/bin/env python3
"""Validate every catalog entry against schema/catalog.schema.json.

Dependency-free (no PyYAML, no jsonschema) so it runs identically on a laptop and
in CI, exactly like scripts/validate_prompts.py.

    python3 scripts/validate_catalog.py

Exit code 0 = all good, 1 = at least one error.
"""

from __future__ import annotations

import json
import re
import sys

from _catalog import CATEGORIES, ENTRIES_DIR, ROOT
from _frontmatter import PROMPTS_DIR  # noqa: F401  (keeps parity of imports)

SCHEMA = json.loads((ROOT / "schema" / "catalog.schema.json").read_text(encoding="utf-8"))
REQUIRED = SCHEMA["required"]
PROPS = SCHEMA["properties"]

FILENAME_RE = re.compile(r"^(?P<id>astra-cat-[0-9]{3})-(?P<slug>[a-z0-9-]+)\.md$")
ID_RE = re.compile(PROPS["id"]["pattern"])
DATE_RE = re.compile(PROPS["added"]["pattern"])
TAG_RE = re.compile("^[a-z0-9][a-z0-9-]*$")
REQUIRED_HEADINGS = ["## What it is", "## Why it's recommended", "## Source & credit"]

errors: list[str] = []
warnings: list[str] = []
seen_ids: dict[str, str] = {}


def _err(rel: str, msg: str) -> None:
    errors.append(f"{rel}: {msg}")


def _check_string_array(rel: str, meta: dict, key: str) -> None:
    value = meta.get(key)
    if value is None:
        if key in PROPS and key not in REQUIRED:
            return
    if not isinstance(value, list):
        _err(rel, f"{key!r} must be an inline array")
        return
    for item in value:
        if not isinstance(item, str) or not TAG_RE.match(item):
            _err(rel, f"{key!r} has invalid item {item!r} (lowercase, hyphens only)")


def check(path, meta: dict) -> None:
    rel = path.relative_to(ROOT).as_posix()

    if "__error__" in meta:
        _err(rel, meta["__error__"])
        return

    for key in REQUIRED:
        if key not in meta:
            _err(rel, f"missing required key {key!r}")

    m = FILENAME_RE.match(path.name)
    if not m:
        _err(rel, "filename must be <id>-<slug>.md where id is astra-cat-NNN")
    else:
        if meta.get("id") != m.group("id"):
            _err(rel, f"id {meta.get('id')!r} does not match filename id")
    ident = meta.get("id")
    if isinstance(ident, str):
        if not ID_RE.match(ident):
            _err(rel, f"id {ident!r} does not match {PROPS['id']['pattern']}")
        if ident in seen_ids:
            _err(rel, f"duplicate id {ident!r} (also in {seen_ids[ident]})")
        else:
            seen_ids[ident] = rel

    if meta.get("category") != path.parent.name:
        _err(rel, f"category {meta.get('category')!r} must match folder {path.parent.name!r}")
    if meta.get("category") not in CATEGORIES:
        _err(rel, f"unknown category {meta.get('category')!r}")

    for key in ("kind", "tier", "source_platform"):
        enum = PROPS[key]["enum"]
        if meta.get(key) not in enum:
            _err(rel, f"{key} {meta.get(key)!r} not in {enum}")

    url = meta.get("source_url")
    if not isinstance(url, str) or not re.match(PROPS["source_url"]["pattern"], url):
        _err(rel, f"source_url {url!r} must be an absolute http(s) URL")

    if not isinstance(meta.get("has_prompt"), bool):
        _err(rel, "has_prompt must be true or false")

    added = meta.get("added")
    if not isinstance(added, str) or not DATE_RE.match(added):
        _err(rel, f"added {added!r} must be YYYY-MM-DD")

    for key in ("title", "author"):
        value = meta.get(key)
        if not isinstance(value, str) or not value.strip():
            _err(rel, f"{key} must be a non-empty string")

    _check_string_array(rel, meta, "tags")
    if isinstance(meta.get("tags"), list) and not meta["tags"]:
        _err(rel, "tags must not be empty")
    _check_string_array(rel, meta, "signals")

    if "stars" in meta and (not isinstance(meta["stars"], int) or isinstance(meta["stars"], bool)):
        _err(rel, "stars must be an integer")

    body = path.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        if heading not in body:
            _err(rel, f"missing section {heading!r}")


def main() -> int:
    paths = list(ENTRIES_DIR.glob("*/*.md"))
    if not paths:
        print("\u2717 no catalog entries found")
        return 1
    for path, meta in __import__("_catalog").iter_entries():
        check(path, meta)

    for warning in warnings:
        print(f"\u26a0 {warning}")
    for error in errors:
        print(f"\u2717 {error}")
    if errors:
        print(f"\n\u2717 {len(errors)} error(s) across {len(paths)} entries")
        return 1
    print(f"\u2713 {len(paths)} catalog entries valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
