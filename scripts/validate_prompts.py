#!/usr/bin/env python3
"""Validate every prompt recipe against schema/prompt.schema.json.

Dependency-free (no PyYAML) so it runs identically on a laptop and in CI.

    python3 scripts/validate_prompts.py

Exit code 0 = all good, 1 = at least one error. Warnings do not fail the build.
"""

from __future__ import annotations

import json
import re
import sys

from _frontmatter import (
    CATEGORIES,
    PROMPTS_DIR,
    REQUIRED_HEADINGS,
    ROOT,
    iter_prompts,
)

SCHEMA = json.loads((ROOT / "schema" / "prompt.schema.json").read_text(encoding="utf-8"))
REQUIRED = SCHEMA["required"]
PROPS = SCHEMA["properties"]

FILENAME_RE = re.compile(r"^(?P<id>astra-3d-[0-9]{3})-(?P<slug>[a-z0-9-]+)\.md$")
FENCE_RE = re.compile(r"```[a-zA-Z]*\n.+?\n```", re.DOTALL)


def _is_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def check_against_schema(meta: dict) -> list[str]:
    """Minimal JSON-Schema subset: required, type, enum, const, pattern, bounds."""
    errors: list[str] = []

    for key in REQUIRED:
        if key not in meta:
            errors.append(f"missing required key '{key}'")

    for key, value in meta.items():
        spec = PROPS.get(key)
        if spec is None:
            errors.append(f"unknown key '{key}' (additionalProperties: false)")
            continue
        if value is None:
            if key != "seed":
                errors.append(f"'{key}' is null; omit it or give a value")
            continue

        if "enum" in spec and value not in spec["enum"]:
            errors.append(f"'{key}' must be one of {spec['enum']}, got {value!r}")
        if spec.get("type") == "string" and not isinstance(value, str):
            errors.append(f"'{key}' must be a string, got {type(value).__name__}")
            continue
        if "pattern" in spec and isinstance(value, str) and not re.fullmatch(spec["pattern"], value):
            errors.append(f"'{key}' does not match /{spec['pattern']}/: {value!r}")
        if spec.get("type") == "number" and not _is_number(value):
            errors.append(f"'{key}' must be a number, got {type(value).__name__}")
        if spec.get("type") == "integer" and not _is_int(value):
            errors.append(f"'{key}' must be an integer, got {type(value).__name__}")
        if "minimum" in spec and _is_number(value) and value < spec["minimum"]:
            errors.append(f"'{key}' must be >= {spec['minimum']}, got {value}")
        if "maximum" in spec and _is_number(value) and value > spec["maximum"]:
            errors.append(f"'{key}' must be <= {spec['maximum']}, got {value}")
        if spec.get("type") == "array":
            if not isinstance(value, list):
                errors.append(f"'{key}' must be an inline array, got {type(value).__name__}")
            else:
                if len(value) < spec.get("minItems", 0):
                    errors.append(f"'{key}' needs at least {spec['minItems']} item(s)")
                if spec.get("uniqueItems") and len(set(value)) != len(value):
                    errors.append(f"'{key}' has duplicate items")
                item_spec = spec.get("items", {})
                for item in value:
                    if item_spec.get("type") == "string" and not isinstance(item, str):
                        errors.append(f"'{key}' items must be strings, got {item!r}")
                    elif "pattern" in item_spec and isinstance(item, str):
                        if not re.fullmatch(item_spec["pattern"], item):
                            errors.append(f"'{key}' item {item!r} does not match /{item_spec['pattern']}/")

    # 'seed' is oneOf integer | "none"
    if "seed" in meta and meta["seed"] is not None:
        if not (_is_int(meta["seed"]) or meta["seed"] == "none"):
            errors.append("'seed' must be a non-negative integer or the string \"none\"")
        elif isinstance(meta["seed"], int) and meta["seed"] < 0:
            errors.append("'seed' must be >= 0")

    return errors


def check_identity(path, meta: dict) -> list[str]:
    errors: list[str] = []
    match = FILENAME_RE.match(path.name)
    if not match:
        errors.append(
            f"filename must look like <id>-<slug>.md, e.g. astra-3d-001-endless-runner.md (got {path.name!r})"
        )
        return errors
    if meta.get("id") != match.group("id"):
        errors.append(f"id {meta.get('id')!r} does not match filename prefix {match.group('id')!r}")
    if meta.get("slug") != match.group("slug"):
        errors.append(f"slug {meta.get('slug')!r} does not match filename suffix {match.group('slug')!r}")
    if meta.get("category") != path.parent.name:
        errors.append(
            f"category {meta.get('category')!r} does not match folder {path.parent.name!r}"
        )
    return errors


def check_body(text: str) -> list[str]:
    errors: list[str] = []
    cursor = -1
    for heading in REQUIRED_HEADINGS:
        idx = text.find(heading)
        if idx == -1:
            errors.append(f"missing required heading {heading!r}")
        elif idx < cursor:
            errors.append(f"heading {heading!r} is out of order")
        else:
            cursor = idx
    prompt_section = text.find("## The prompt")
    if prompt_section != -1 and "```" not in text[prompt_section:]:
        errors.append("'## The prompt' section has no fenced code block")
    if not FENCE_RE.search(text):
        errors.append("no fenced code block found anywhere in the file")
    return errors


def check_verification(meta: dict) -> list[str]:
    errors: list[str] = []
    status = meta.get("verified")
    if status in ("tested", "community"):
        for key in ("verified_by", "verified_on"):
            if not meta.get(key):
                errors.append(f"'{key}' is required when verified is {status!r}")
    return errors


def main() -> int:
    seen_ids: dict[str, str] = {}
    errors_by_file: list[tuple[str, list[str]]] = []
    warnings: list[tuple[str, list[str]]] = []
    checked = 0

    for path, meta, text in iter_prompts():
        rel = path.relative_to(ROOT).as_posix()
        if "__error__" in meta:
            errors_by_file.append((rel, [meta["__error__"]]))
            continue
        checked += 1
        errors: list[str] = []
        errors += check_against_schema(meta)
        errors += check_identity(path, meta)
        errors += check_body(text)
        errors += check_verification(meta)

        pid = meta.get("id")
        if isinstance(pid, str):
            if pid in seen_ids:
                errors.append(f"duplicate id {pid!r}, also in {seen_ids[pid]}")
            else:
                seen_ids[pid] = rel

        file_warnings: list[str] = []
        if meta.get("verified") == "draft":
            file_warnings.append("still a draft; reproduce it to promote to community/tested")

        if errors:
            errors_by_file.append((rel, errors))
        if file_warnings:
            warnings.append((rel, file_warnings))

    for rel, msgs in errors_by_file:
        print(f"\033[31mFAIL\033[0m {rel}")
        for msg in msgs:
            print(f"      - {msg}")
    for rel, msgs in warnings:
        print(f"\033[33mWARN\033[0m {rel}")
        for msg in msgs:
            print(f"      - {msg}")

    print()
    if errors_by_file:
        print(f"✗ {checked} recipes checked · {len(errors_by_file)} with errors")
        return 1
    print(f"✓ {checked} recipes checked · all valid · {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
