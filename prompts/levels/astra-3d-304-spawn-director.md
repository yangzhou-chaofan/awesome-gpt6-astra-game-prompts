---
id: astra-3d-304
title: Wave / Spawn Director
category: levels
slug: spawn-director
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.35
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, pacing, waves, spawning, director, seeded, level-design]
license: CC0-1.0
---

# Wave / Spawn Director

> A pacing system that decides *what* spawns, *when* and *where* — with an intensity curve you can
> tune, and seeded so a run is reproducible.

## What you get

`index.html`, self-contained: a spawn director with a budget-based wave system, an intensity curve
with tension and release, spawn-point selection that avoids the player's view, and a debug graph
showing the live intensity. A top-down arena stands in for the game.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior systems designer. Build a wave/spawn director in one self-contained index.html for
Three.js, with a small arena to demonstrate it.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- Declare `const SEED = 4242;`; every decision uses a seeded PRNG you implement yourself. No Math.random().

Enemy archetypes (data-driven, defined in one table)
- grunt, brute, archer — each with { cost, hp, speed, threat }. Adding an entry to the table must be the
  only change needed to introduce a new enemy type.

Budget and waves
- Each wave has a budget that grows with the wave number (exposed as a curve: BASE_BUDGET and
  BUDGET_GROWTH). The director spends the budget by selecting archetypes whose combined threat matches
  a target intensity, never exceeding the budget.
- Between waves, an intermission with a countdown. A "wave preview" shows what is coming, so the player
  can prepare. (Showing the plan is a design choice the recipe requires.)

Intensity curve (the core of the recipe)
- Maintain a live intensity value from waves, enemy threat near the player, and time since the last
  spawn. The director must implement distinct pressure and relief phases: after a peak, guarantee a
  lull by suppressing high-cost spawns for a period.
- A "director state" enum: BUILDUP, PEAK, RELIEF, RESET, driven by the intensity value, and displayed.

Spawning
- At least 4 spawn points around the arena. Choose a spawn point that (a) is out of the player's view
  where possible and (b) is not on top of another enemy. Document the scoring.
- Never spawn more than MAX_ALIVE enemies at once; queue the rest.

Debug
- A rolling graph of intensity over time, with phase bands shaded and the current phase labelled, plus
  counters for budget spent and queued spawns.

Engineering
- requestAnimationFrame with a delta clock. The director is a state machine independent of rendering.
- Separate: archetype table, budget/spending, intensity, phase machine, spawn selection, queue, graph.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments per stage.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.35` | Pacing is partly taste; the budget and phase contract is not. |
| `seed` | `4242` | API seed; run seed is in-file `SEED`, so an identical run is reproducible. |
| `max_output_tokens` | `6000` | Director plus arena plus graph. |

## Expected output

- `index.html` — one file, roughly 400–600 lines.
- One archetype table, a budget-spending routine, an intensity value, and a four-state phase machine.

## Verify it worked

- [ ] Waves spawn enemies whose combined cost does not exceed the wave budget.
- [ ] Previewed enemies match what actually spawns.
- [ ] After a PEAK phase, there is a visible RELIEF lull with no high-cost spawns.
- [ ] The intensity graph shows a repeating rise-and-fall, not a flat line.
- [ ] Spawns occur away from the player's view where possible and never on top of another enemy.
- [ ] `MAX_ALIVE` is never exceeded; extra enemies queue and spawn as slots free.
- [ ] The same `SEED` reproduces the same sequence of waves and spawns on reload.
- [ ] Adding a fourth entry to the archetype table makes it appear without other code changes.
- [ ] Console is clean.

## Tune it

- **`BUDGET_GROWTH`** — how fast waves escalate.
- **Peak/relief thresholds** — how pronounced the tension cycle is.

## Where it drifts

- **Budget ignored.** The director spawns "a few more each wave" and the intensity curve is decorative.
  The budget check and the preview-matches-reality check expose it.
- **No relief phase.** Intensity climbs monotonically and the game becomes exhausting. The requirement
  to suppress high-cost spawns after a peak is the guard; the graph makes it visible.
- **Spawning in the player's view.** Breaks immersion and feels unfair. The spawn-selection scoring
  requirement addresses it; test by facing one spawn corner.
- **Unseeded decisions.** `Math.random()` in archetype selection. The same-seed reload check catches it.
- **Data-driven claim not honoured.** Adding an archetype needs code edits elsewhere. The table-only
  requirement is the test.

## Provenance

- Technique: original; "AI director" pacing ideas (in the vein of L4D's director) reduced to a budget +
  intensity model that is easy to reason about and reproduce.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
