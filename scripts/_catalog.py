"""Shared loader and presentation constants for the catalog layer.

Mirrors ``_frontmatter.py`` for the recipe layer: the catalog frontmatter is the
same restricted flat-map YAML subset, so both layers reuse one dependency-free
parser.
"""

from __future__ import annotations

from pathlib import Path

from _frontmatter import FrontmatterError, parse_frontmatter  # noqa: F401

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "catalog" / "entries"

# category folder -> heading used in CATALOG.md (order = display order)
CATEGORIES = {
    "games": "\U0001f3ae Games \u2014 playable games & prototypes",
    "3d": "\U0001f9f1 3D \u2014 modelling, Blender & spatial work",
    "web": "\U0001f578\ufe0f Web \u2014 sites, HTML & interfaces",
    "video": "\U0001f3ac Video \u2014 prompt-to-video & motion",
    "apps": "\U0001f4e6 Apps \u2014 tools, utilities & products",
    "agent": "\U0001f5b1\ufe0f Agent \u2014 computer use & automation",
    "engineering": "\u2699\ufe0f Engineering \u2014 hardware, CAD & the physical world",
    "research": "\U0001f52c Research \u2014 benchmarks, guides & official docs",
    "prompts": "\U0001f4dd Prompts \u2014 libraries & prompt tooling",
}

TIER_ORDER = ["featured", "notable", "community"]

TIER_BADGE = {
    "featured": "\u2b50 featured",
    "notable": "\u2726 notable",
    "community": "\u00b7 community",
}

KIND_LABEL = {
    "collection": "collection",
    "work": "work",
    "tool": "tool",
    "skill": "skill",
    "guide": "guide",
    "official": "official",
}


def iter_entries():
    """Yield ``(path, meta)`` for every catalog entry, sorted by path.

    On a malformed file ``meta`` is ``{"__error__": "<message>"}``.
    """
    for path in sorted(ENTRIES_DIR.glob("*/*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text)
        except FrontmatterError as exc:
            meta = {"__error__": str(exc)}
        yield path, meta
