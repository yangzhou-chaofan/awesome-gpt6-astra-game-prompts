# Reproducibility

Every prompt in this list claims to be *reproducible*. This document defines exactly what that
claim means, because "reproducible" is the word most likely to be quietly false in a prompt list.

## The problem

A language model is not a function. Given the same prompt twice, you may get two different games.
A prompt list that ignores this is a list of anecdotes: it tells you *someone* got a good result,
not that *you* will.

There are two honest responses, and we use both:

1. **Record everything that was under the author's control.** Model, version, sampling settings,
   system prompt, tool configuration, input files. If a variable is documented, it is not a source
   of mystery.
2. **Constrain what the model is allowed to invent.** Most drift comes from under-specification.
   "Make a 3D game" leaves thousands of degrees of freedom. "A single self-contained `index.html`,
   Three.js r170+, three lanes, primitives only, no external assets" leaves very few. Fewer choices
   means the same result more often — and when it differs, the difference is small and local.

## What is guaranteed, and what is not

**Guaranteed** by following a recipe:

- the deliverable's *shape* — what files come out, what they run on, what they may not depend on;
- the *acceptance checks* — the concrete list of things that must be true of the output;
- the *degrees of freedom the author pinned* — versions, palettes, dimensions, seeds.

**Not guaranteed**:

- byte-for-byte identical output. Unless the API exposes a deterministic seed and the recipe records
  it, two runs will differ in incidental ways (variable names, exact colors).
- that a future model release behaves the same. That is why recipes carry a `model_version` and are
  never silently edited to track a new one.

A recipe fails its claim when the acceptance checks fail — not when the output looks different.

## The four clauses

### 1. Model

`model` + `model_version` identify the exact release. Astra shipped 2026-09-03; behavior will change
in later releases. A recipe is a snapshot, not a living pointer.

### 2. Settings

`temperature`, `top_p`, `seed`, `max_output_tokens`, plus any system prompt or tool config in the
body. Where the API exposes a seed, record it. Where it does not, `seed: none` **and** the recipe
must specify how the *output itself* is made deterministic — for example by requiring an in-prompt
seeded PRNG so procedural geometry is identical across runs even when the text differs.

### 3. Input

A "Before you start" section listing runtime, dependencies, assets, keys, and starting files. Hidden
state is the most common way a "reproducible" recipe turns out not to be.

### 4. Acceptance

"Expected output" names the artifacts. "Verify it worked" is a checklist of observable, fail-able
claims. "No console errors" is a check. "Looks good" is not.

## Degrees of determinism

| Level | Meaning | Example |
| --- | --- | --- |
| **D1 — exact** | Same bytes every run. | A seeded PRNG driving all geometry; no model sampling of the data. |
| **D2 — equivalent** | Same observable behavior, incidental differences allowed. | Different variable names, same game mechanics and acceptance checks passing. |
| **D3 — shaped** | Same deliverable shape, materially different content. | A different level layout each run, still playing by the stated rules. |

Recipes should state which level they target. Most code-generation recipes here target **D2**, and
those that generate procedural worlds aim for **D1 by seed** inside the output. A recipe that cannot
honestly claim at least D3 should not be in this list.

## Verification levels

| Badge | Meaning | Who set it |
| --- | --- | --- |
| 📝 `draft` | Format-complete, reviewed, not run end-to-end. | Author |
| 🧪 `community` | Ran end-to-end on the pinned version by its author. | Author |
| ✅ `tested` | Independently reproduced by someone other than the author; all checks passed. | Maintainer |

Promotion requires *reproduction by another person*. That is the mechanism by which this list stays
honest: a recipe is worth what an independent run says it is worth.

## When reality diverges

If a discovery contradicts an earlier claim — a setting that does not exist, a check that cannot
pass on the pinned version — the fix is to correct the recipe and say so, not to quietly adjust the
claim. Open an issue; recipes are versioned records and their history should be legible.
