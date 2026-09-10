#!/usr/bin/env python3
"""Regenerate the contents index between the markers in README.md.

    python3 scripts/build_index.py            # rewrite README.md in place
    python3 scripts/build_index.py --check    # exit 1 if README.md is stale (CI)

The tables are generated from the prompt frontmatter, so the README can never
silently disagree with the recipes on disk.
"""

from __future__ import annotations

import sys

from _frontmatter import CATEGORIES, ROOT, VERIFIED_BADGE, iter_prompts

README = ROOT / "README.md"
BEGIN = "<!-- BEGIN INDEX -->"
END = "<!-- END INDEX -->"
MODEL_VERSION = "2026-09-03"


def collect() -> tuple[dict[str, list], int]:
    by_category: dict[str, list] = {cat: [] for cat in CATEGORIES}
    total = 0
    for path, meta, _ in iter_prompts():
        if "__error__" in meta or meta.get("category") not in by_category:
            continue
        by_category[meta["category"]].append((meta, path))
        total += 1
    for entries in by_category.values():
        entries.sort(key=lambda pair: pair[0]["id"])
    return by_category, total


def render() -> str:
    by_category, total = collect()
    lines = [
        f"> **{total}** prompts · {len(CATEGORIES)} categories · targeting "
        f"`gpt-6-astra` ({MODEL_VERSION}).",
        "",
        "The initial batch ships as **📝 draft** — format-complete and reviewed, but not yet "
        "independently reproduced. Run one and record it to promote it to 🧪 community.",
        "",
    ]
    for category, heading in CATEGORIES.items():
        entries = by_category.get(category, [])
        lines.append(f"### {heading}")
        lines.append("")
        if not entries:
            lines.append("_No prompts yet — [add one](CONTRIBUTING.md)._")
            lines.append("")
            continue
        lines.append("| ID | Prompt | Stack | Difficulty | Verified |")
        lines.append("| --- | --- | --- | --- | --- |")
        for meta, path in entries:
            rel = path.relative_to(ROOT).as_posix()
            badge = VERIFIED_BADGE.get(meta["verified"], meta["verified"])
            lines.append(
                f"| `{meta['id']}` | [{meta['title']}]({rel}) | {meta['stack']} "
                f"| {meta['difficulty']} | {badge} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    body = render()
    text = README.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        print(f"✗ README.md is missing the {BEGIN} / {END} markers")
        return 1
    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    updated = f"{head}{BEGIN}\n{body}{END}{tail}"

    if "--check" in sys.argv:
        if updated != text:
            print("✗ README.md index is stale — run: python3 scripts/build_index.py")
            return 1
        print("✓ README.md index is up to date")
        return 0

    if updated == text:
        print("✓ README.md index already up to date")
        return 0
    README.write_text(updated, encoding="utf-8")
    print("✓ README.md index regenerated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
