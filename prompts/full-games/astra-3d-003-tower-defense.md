---
id: astra-3d-003
title: Tower Defense
category: full-games
slug: tower-defense
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 8000
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, webgl, strategy, tower-defense, grid, single-file]
license: CC0-1.0
---

# Tower Defense

> A complete grid-based 3D tower defense: build turrets, survive waves, lose lives, restart.

## What you get

`index.html`, self-contained. A fixed path across a grid, three turret types with distinct cost,
range and fire rate, projectiles with travel time, money, lives, escalating waves, and win/lose
overlays. This is the recipe that most often exposes whether a model can hold *systems* together
rather than just render a scene.

## Before you start

- **Runtime:** any modern browser.
- **Dependencies:** none; Three.js via CDN import map.
- **Assets / inputs:** none. The path and waves are defined in code.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior Three.js engineer. Build a complete 3D tower defense game in ONE self-contained index.html.

Deliverable
- A single `index.html` that runs by double-clicking it. No build step, no server.
- Three.js r170+ via an import map from a CDN. No external assets.

Map
- A 16x16 grid rendered as tiles. Mark a fixed, hard-coded path from the spawn tile to the base tile
  (list the path tiles as an array of [x, z] coordinates in the code). Non-path tiles are buildable.
- The base sits at the end of the path; enemies reaching it cost the player a life.

Turrets
- Three types with distinct behaviour and cost:
  1. Gun — cheap, fast, low damage, short range.
  2. Cannon — expensive, slow, high damage, splash on impact.
  3. Frost — medium cost, slows enemies in range instead of damaging them.
- Click a buildable tile to open a small build menu; pick a type; the turret appears and money is
  deducted. Hovering a tile highlights it. Clicking an existing turret shows an upgrade or sell option.
- Targeting: each turret fires at the nearest enemy within its range. Projectiles travel over time
  and apply damage on arrival; cannon projectiles damage all enemies within a splash radius.

Enemies and waves
- Enemies follow the path from spawn to base.
- Enemies have health, speed and a per-type colour. Frost slows them for a duration.
- Killing an enemy grants money. Reaching the base costs a life (start with 10).
- Waves escalate in enemy count and health. Provide a "Next wave" button and a short countdown.

State and UI
- A HUD shows money, lives, current wave, and remaining enemies.
- A win overlay when all defined waves are cleared; a lose overlay when lives hit 0. Both offer restart.
- Start with enough money to build one or two turrets.

Determinism
- Declare `const SEED = 4242;` and drive any randomness (e.g. minor enemy speed variation) from a small
  seeded PRNG you implement yourself. Wave composition itself should be hard-coded, not random.

Engineering
- requestAnimationFrame with a delta-time clock; all rates are per second.
- Separate concerns: grid/map, waves, enemies, turrets, projectiles, economy, UI, rendering.
- Handle resize and devicePixelRatio. No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with brief comments per subsystem.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | Many interacting systems; low temperature keeps the interfaces between them stable. |
| `seed` | `4242` | API seed plus an in-prompt `SEED` for any minor variation. |
| `max_output_tokens` | `8000` | This is the largest of the full-game recipes; do not starve it. |

## Expected output

- `index.html` — one file, roughly 600–900 lines.
- The path coordinate array is present and hard-coded, not generated randomly.

## Verify it worked

- [ ] The grid and the path are visible on load, with spawn and base marked.
- [ ] Clicking a buildable tile opens the build menu; building deducts the correct cost.
- [ ] Turrets fire only when an enemy is within range, and hit nothing otherwise.
- [ ] Projectiles visibly travel; damage lands on arrival, not at fire time.
- [ ] Frost slows enemies; cannon applies splash damage to more than one enemy.
- [ ] Killing an enemy grants money; an enemy reaching the base costs exactly one life.
- [ ] The HUD money/lives/wave values track the game state with no drift.
- [ ] Win and lose overlays appear on their conditions and restart resets all state.
- [ ] Console is clean.

## Tune it

- **Starting money and wave table** at the top of the script — the balance dials.
- **Turret range/fire-rate numbers** — the fastest way to change difficulty without touching logic.

## Where it drifts

- **Turrets that damage instantly instead of via projectiles.** The prompt's "projectiles travel over
  time" requirement is the guard; without it many outputs collapse to hitscan and lose the feel.
- **Money or lives drifting out of sync with the HUD.** Usually caused by updating the HUD only in the
  render loop and the state elsewhere. The "tracks with no drift" check catches it.
- **Enemies cutting corners.** Path-following implemented by lerping to the base rather than stepping
  through the tile list. Verify enemies actually visit every path tile.
- **Splash damage ignored.** Cannon becomes a reskinned gun. Place two enemies close together and
  confirm both take damage.

## Provenance

- Technique: original; classic tower-defense decomposition, tightened for deterministic waves.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
