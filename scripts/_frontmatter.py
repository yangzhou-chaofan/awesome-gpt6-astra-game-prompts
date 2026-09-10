"""Shared frontmatter parser and prompt loader.

The prompt frontmatter is a deliberately restricted subset of YAML:

* a flat map of ``key: value`` pairs -- no nested maps, no block scalars,
  no anchors, no multi-line strings;
* lists are written inline: ``tags: [threejs, webgl]``.

That restriction keeps this tooling dependency-free (no PyYAML, runs anywhere
Python 3 does) and makes the format hard to get subtly wrong. If you need a
nested structure, you need a different repository.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"

# category folder -> heading used in the README index
CATEGORIES = {
    "full-games": "\U0001f3ae Full games \u2014 one prompt, a playable game",
    "systems": "\u2699\ufe0f Systems \u2014 drop-in gameplay machinery",
    "assets": "\U0001f9f1 Assets \u2014 geometry, rigs and textures as code",
    "levels": "\U0001f5fa\ufe0f Levels & worlds",
    "ui": "\U0001f5a5\ufe0f UI & HUD",
}

VERIFIED_BADGE = {
    "tested": "\u2705 tested",
    "community": "\U0001f9ea community",
    "draft": "\U0001f4dd draft",
}

# headings every recipe body must contain, in order of appearance
REQUIRED_HEADINGS = [
    "## What you get",
    "## Before you start",
    "## The prompt",
    "## Settings",
    "## Expected output",
    "## Verify it worked",
    "## Tune it",
    "## Where it drifts",
    "## Provenance",
]


class FrontmatterError(ValueError):
    """Raised when the frontmatter block is malformed."""


def _split_inline(inner: str) -> list[str]:
    """Split an inline array body on commas that are not inside quotes."""
    parts: list[str] = []
    buf: list[str] = []
    quote: str | None = None
    for ch in inner:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch == ",":
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return parts


def _parse_scalar(raw: str):
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    low = raw.lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("null", "none", "~"):
        return None
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        pass
    return raw


def parse_frontmatter(text: str) -> dict:
    """Parse the leading ``---`` block of *text* into a flat dict."""
    if not text.lstrip().startswith("---"):
        raise FrontmatterError("file must start with a '---' frontmatter block")
    start = text.index("---") + 3
    end = text.find("\n---", start)
    if end == -1:
        raise FrontmatterError("unterminated frontmatter block")
    block = text[start:end]

    data: dict = {}
    for lineno, raw in enumerate(block.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("-"):
            raise FrontmatterError(
                f"line {lineno}: block sequences are not supported; use an inline array [a, b]"
            )
        key, sep, val = line.partition(":")
        if not sep:
            raise FrontmatterError(f"line {lineno}: expected 'key: value', got {raw!r}")
        key = key.strip()
        if not re.fullmatch(r"[a-z_][a-z0-9_]*", key):
            raise FrontmatterError(f"line {lineno}: invalid key {key!r}")
        val = val.strip()
        if val == "":
            raise FrontmatterError(f"line {lineno}: empty value for {key!r}")
        if val.startswith("["):
            if not val.endswith("]"):
                raise FrontmatterError(f"line {lineno}: unterminated inline array")
            inner = val[1:-1].strip()
            data[key] = [] if not inner else [_parse_scalar(x) for x in _split_inline(inner)]
        else:
            data[key] = _parse_scalar(val)
    return data


def iter_prompts():
    """Yield ``(path, meta, text)`` for every recipe, sorted by path.

    On a malformed file ``meta`` is ``{"__error__": "<message>"}`` so callers can
    report it without aborting the whole scan.
    """
    for path in sorted(PROMPTS_DIR.glob("*/*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text)
        except FrontmatterError as exc:
            meta = {"__error__": str(exc)}
        yield path, meta, text
