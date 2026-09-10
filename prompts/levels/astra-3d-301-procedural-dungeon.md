---
id: astra-3d-301
title: Seeded Procedural Dungeon
category: levels
slug: procedural-dungeon
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.35
top_p: 0.9
seed: 4242
max_output_tokens: 7500
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, dungeon, bsp, procedural, seeded, level-generation]
license: CC0-1.0
---

# Seeded Procedural Dungeon

> A BSP dungeon with connected rooms and corridors, generated from one integer — walk the same seed
> twice and get the same dungeon.

## What you get

`index.html`, self-contained: a BSP dungeon generator producing rooms and corridors on a tile grid,
a minimap, an overhead 3D view, and a first-person walk mode. The seed is shown on screen and can be
shared as a number.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none; geometry is boxes.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior level-generation engineer. Build a seeded procedural dungeon in one self-contained
index.html for Three.js.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- Declare `const SEED = 4242;` and `const GRID_W = 64; const GRID_H = 64;` at the top.

Generation (must be deterministic)
- Implement a seeded PRNG (mulberry32 or similar) yourself and derive ALL randomness from it. No
  Math.random() anywhere. The same SEED must produce an identical dungeon.
- Use recursive BSP splitting: split the grid into leaves down to a minimum size, carve a room in each
  leaf with random but seeded margin/padding, then connect sibling leaves with corridors between room
  centres. Document the algorithm in comments.
- Guarantee connectivity: every room must be reachable from every other. Run a flood fill from the
  first room and, if any room is unreachable, connect it; report the number of rooms and corridors.

Rendering
- Overhead 3D view: floors as one merged geometry, walls as extruded boxes around room/corridor tiles,
  a simple ceiling-less look. Use flat colours.
- A 2D minimap drawn to a canvas, showing rooms, corridors and the player.
- Toggle between overhead and first-person with a key (e.g. Tab). First person uses pointer lock with
  WASD and collision against the walls.

Determinism surface
- Display the seed and a dungeon signature (e.g. a hash of the tile grid) on screen. The same seed must
  show the same signature on reload. Expose a "new seed" button that picks a seed and regenerates.

Engineering
- requestAnimationFrame with a delta clock. Regeneration disposes previous geometry.
- Separate: PRNG, BSP generation, carving, connectivity, meshing, minimap, player/controls.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments per stage.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.35` | Generation benefits from a little variation; the connectivity contract does not. |
| `seed` | `4242` | API seed; the dungeon seed is the in-file `SEED`. |
| `max_output_tokens` | `7500` | BSP + carving + connectivity + two render modes. |

## Expected output

- `index.html` — one file, roughly 550–850 lines.
- A BSP generator, a flood-fill connectivity pass, and a displayed seed/signature.

## Verify it worked

- [ ] A dungeon renders in the overhead 3D view with rooms and connecting corridors.
- [ ] Reloading with the same `SEED` reproduces the identical layout and the same signature hash.
- [ ] A different seed gives a different layout and a different signature.
- [ ] Every room is reachable — verify by walking the dungeon in first person, or by the printed count.
- [ ] Tab switches between overhead and first person.
- [ ] First-person movement collides with walls and cannot leave the dungeon.
- [ ] Regenerating repeatedly does not grow memory.
- [ ] Console is clean.

## Tune it

- **Minimum leaf size** — more, smaller rooms vs. fewer, larger ones.
- **Room padding/margin** — how tightly rooms fill their leaves.

## Where it drifts

- **Disconnected rooms.** The single most common failure: corridors connect only some siblings. The
  explicit flood-fill connectivity pass is the guard — do not skip it because the picture looks fine.
- **Unseeded carving.** `Math.random()` used for room margins. The signature-hash reload check exposes
  it: if the hash changes on reload, the seed was not fully respected.
- **Recursion depth blowout.** BSP split without a minimum size recurses forever or produces degenerate
  slivers. The minimum-size requirement prevents it; check for 1-tile rooms.
- **Per-tile meshes.** Thousands of individual meshes tank performance. The "merged geometry" for floors
  and the memory check address it.

## Provenance

- Technique: BSP dungeon generation is standard (the classic roguelike approach); the connectivity
  guarantee and the signature hash are the reproducibility contributions.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
