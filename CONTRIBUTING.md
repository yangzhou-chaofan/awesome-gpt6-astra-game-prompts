# Contributing to awesome-gpt6-astra-game-prompts

Thanks for helping make this the best place to find prompts that actually produce running 3D games.

There are three ways to contribute, in increasing order of value:

1. **Report drift** — a recipe no longer works on a new model release. Open an issue.
2. **Submit a prompt** — a new reproducible recipe.
3. **Reproduce a prompt** — run someone else's recipe, confirm the acceptance checks, and record it.
   This is the most valuable contribution, because it is what promotes a prompt to **tested**.

---

## The bar: the reproducibility contract

A prompt is accepted only if all four clauses are satisfied. See
[`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for the long version.

| Clause | Required in the frontmatter / body |
| --- | --- |
| **Model** | `model` and `model_version` — the exact release you ran it on. |
| **Settings** | `temperature`, `top_p`, `seed` (or `seed: none` with a note), `max_output_tokens`, and any system prompt or tool config. |
| **Input** | A "Before you start" section listing runtime, dependencies, assets, and starting files. |
| **Acceptance** | An "Expected output" section and a "Verify it worked" checklist of concrete, checkable items. |

"Works on my machine" is not a recipe. If a step is unrepeatable, say so explicitly.

---

## Adding a prompt

```bash
# 1. fork and clone
git clone git@github.com:<you>/awesome-gpt6-astra-game-prompts.git
cd awesome-gpt6-astra-game-prompts

# 2. copy the template into the right category folder, using the naming convention
cp templates/PROMPT_TEMPLATE.md prompts/full-games/astra-3d-007-my-game.md

# 3. fill it in, then validate
python3 scripts/validate_prompts.py

# 4. regenerate the README index
python3 scripts/build_index.py

# 5. commit and open a PR
```

### Naming convention

```
prompts/<category>/<id>-<slug>.md
```

- `id` — `astra-3d-<block><nnn>`, unique across the repo.
  - `0xx` full games · `1xx` systems · `2xx` assets · `3xx` levels · `4xx` UI
- `slug` — lowercase, hyphenated, must equal the `slug:` field in the frontmatter.

### Frontmatter

Copy the fields exactly from the template. `scripts/validate_prompts.py` enforces:

- required keys present (`id`, `title`, `category`, `slug`, `model`, `model_version`,
  `temperature`, `top_p`, `max_output_tokens`, `difficulty`, `verified`, `tags`, `license`)
- `id` unique and matching its pattern
- `slug` matching the filename
- `category` matching the containing folder
- `difficulty` in `{beginner, intermediate, advanced}`
- `verified` in `{tested, community, draft}`
- `license` a recognised SPDX id (this repo uses `CC0-1.0`)
- `tags` a non-empty inline array

### Verification levels

- New submissions start at **`draft`** unless you have run them end-to-end.
- If *you* ran it end-to-end on the pinned version, set **`community`** and fill in `verified_by` /
  `verified_on`.
- **`tested`** is assigned by a maintainer after an independent reproduction. Don't set it yourself.

### Prompt quality beyond format

A recipe can validate and still be a bad recipe. Reviewers look for:

- **A single deliverable.** "Make a game" produces mush. "One self-contained `index.html` that runs
  on double-click" produces something checkable.
- **Constraints that remove choices.** Naming the runtime, the Three.js version, the geometry
  palette, and the material model removes the degrees of freedom that cause drift.
- **Acceptance checks, not vibes.** "No console errors", "score increments on pickup", "60 fps on
  integrated graphics" — things that can be observed and fail.
- **Honest failure modes.** Every model has a way it fails this task. If you found it, write it into
  "Where it drifts" rather than pretending the recipe is perfect.
- **No hidden state.** If the result depends on a file, an env var, an API key or a paid tool, say so
  in "Before you start".

---

## Reporting drift

Model releases change behavior. If a recipe stops working, open an issue using the **Prompt drift**
template with:

- the recipe id
- the model version you ran
- the acceptance check that failed
- what you got instead

Do **not** silently edit an existing recipe to match a new model. Recipes are historical records
tied to a `model_version`. Add a new file (e.g. `astra-3d-001b-...`) for the new release, or open an
issue so maintainers can decide.

---

## Style

- English, plain and concrete. No marketing voice inside recipes.
- Fence the prompt text in a ```text block so it copies cleanly.
- Keep lines reasonable; the file is read in a terminal as often as on GitHub.
- Prefer numbers to adjectives: "three lanes", "12 tiles", "60 fps" — not "several", "nice", "smooth".

---

## Commits and PRs

- One recipe per PR, or one coherent batch (e.g. a category). Keep validation changes separate.
- PR title: `Add prompt: <title> (<id>)` or `Fix: <id> <what>`.
- Make sure `python3 scripts/validate_prompts.py` passes before you push. CI runs the same script.

By contributing you agree your contribution is released under [CC0-1.0](LICENSE).
