# Catalog — the discovery layer

The [`prompts/`](../prompts) recipes answer *"how do I reproduce this?"*. The catalog answers the
question that comes first: **"what is worth trying at all?"**

This is the aggregation layer. It collects GPT-6 Astra **prompts, demos, tools, skills and guides**
that are already published elsewhere — most of them first posted on X, and many of them already
indexed by other `awesome-*` lists — and turns them into one classified, credited, recommended
index with a browsable site.

It is deliberately looser than the recipe layer:

- **A prompt is optional.** A great demo with no prompt is still a valid entry. The `has_prompt`
  flag records which is which instead of pretending everything is a recipe.
- **Nothing here is claimed to be reproducible.** That standard belongs to [`prompts/`](../prompts).
  An entry in the catalog is a *pointer with an opinion*, not a guarantee.

## Where entries come from

1. **X (primary).** A post, or a prompt dropped in the replies under a post. That is where most
   GPT-6 Astra work is published first.
2. **Other `awesome-*` lists (allowed, and useful).** Aggregating an existing list is fine — the
   catalog's value is *classification, recommendation and credit*, not first possession.

Every entry **must** carry a real, public `source_url` and an `author`. If we cannot point at where
something came from, it does not go in.

## How entries are classified

Two axes, both required:

| Axis | Field | Values |
| --- | --- | --- |
| **Form** — what the output *is* | `category` | `games` · `3d` · `web` · `video` · `apps` · `agent` · `engineering` · `research` · `prompts` |
| **Kind** — what the entry *is* | `kind` | `collection` · `work` · `tool` · `skill` · `guide` · `official` |

`tags` and `signals` add searchable colour on top. The folder an entry lives in must equal its
`category`; CI enforces it.

## How "recommended" is decided

Every entry carries a `tier`:

| Tier | Badge | Meaning |
| --- | --- | --- |
| `featured` | ⭐ | Editor-picked: high signal **and** attributable **and** clearly useful to someone building with Astra. |
| `notable` | ✦ | Real traction or a clearly original contribution. |
| `community` | · | Submitted or newly surfaced, not yet vetted. |

Tiers are set by maintainers, not by star count alone — a 5-star list with 200 sourced prompts can
outrank a 1,000-star repo of links. `signal`s records the specific reasons, so a tier can always be
argued with evidence rather than vibes.

## Layout

```
catalog/
├── README.md                 # this file
└── entries/                  # one markdown file per entry, grouped by category
    ├── games/
    ├── 3d/
    ├── prompts/
    └── ...
```

Generated, never hand-edited:

- [`../CATALOG.md`](../CATALOG.md) — the index tables you see on GitHub.
- [`../site/index.html`](../site/index.html) — the browsable gallery (filter by category / tier / prompt).

## Adding an entry

```bash
# copy the shape of any existing entry, then:
python3 scripts/build_catalog.py            # regenerate CATALOG.md + site/index.html
python3 scripts/validate_catalog.py         # CI runs this too
```

Keep the body short: **What it is · Why it's recommended · Source & credit**, plus **Prompt** when
`has_prompt: true`.
