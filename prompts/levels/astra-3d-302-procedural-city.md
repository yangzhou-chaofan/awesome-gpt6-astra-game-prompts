---
id: astra-3d-302
title: Procedural City Block
category: levels
slug: procedural-city
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.4
top_p: 0.9
seed: 4242
max_output_tokens: 8000
runtime: modern browser
stack: Three.js
difficulty: advanced
verified: draft
tags: [threejs, city, procedural, buildings, roads, seeded, level-generation]
license: CC0-1.0
---

# Procedural City Block

> A seeded city generator: road grid, zoned lots, massed buildings with setbacks, all in one file and
> reproducible from a single integer.

## What you get

`index.html`, self-contained: a road network with intersections, blocks subdivided into lots by zone
(downtown / residential / industrial), buildings extruded with floor bands and rooftops, street
furniture, and a day/night toggle. One `SEED` reproduces the whole city.

## Before you start

- **Runtime:** modern browser with WebGL2.
- **Dependencies:** Three.js and lil-gui (optional) via CDN import map.
- **Assets / inputs:** none; buildings are boxes.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior procedural-generation engineer. Build a seeded procedural city block generator in one
self-contained index.html for Three.js.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- Declare `const SEED = 4242;` and drive ALL randomness from a seeded PRNG you implement yourself. No
  Math.random(). Same seed -> identical city.

Layout
- A road grid over a 1000x1000-unit area with a configurable block size (default 80 units) and road
  width (default 12). Roads are flat quads; intersections are explicit.
- Subdivide each city block into lots with a seeded lot-splitting pass. Lot sizes vary; some lots are
  reserved as parks or parking.
- Assign each block a zone by distance from the centre: downtown (tall), residential (short, more
  numerous), industrial (wide, low). Document the zoning rule.

Buildings
- Mass each building from a footprint extruded upward, with floor bands every floor height, a distinct
  roof (flat, pitched, or mechanical), and setback tiers for downtown towers.
- Vary height within a zone using the seeded PRNG. Target 300-1500 buildings total.
- Merge all building geometry into as few BufferGeometries as possible (e.g. instanced or merged by
  material) so the whole city renders without per-building draw calls.

Detail
- Street furniture: lamps, trees and hydrants placed on sidewalk strips, also seeded.
- A day/night toggle that changes the sun angle, sky colour and building window emissive intensity.

Engineering
- requestAnimationFrame with a delta clock; optionally slow orbit camera to show the city.
- Regeneration disposes previous geometry. A GUI exposes SEED, BLOCK_SIZE and a "regenerate" button.
- Separate: PRNG, road grid, lot subdivision, zoning, massing, furniture, materials, rendering.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments per stage.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.4` | The most aesthetic of the level recipes; some latitude is wanted. |
| `seed` | `4242` | API seed; city seed is in-file `SEED`. |
| `max_output_tokens` | `8000` | The largest level output; truncation leaves a broken file. |

## Expected output

- `index.html` — one file, roughly 650–1000 lines.
- Merged/instanced building geometry and a zone assignment driven by distance from centre.

## Verify it worked

- [ ] A city renders: road grid, blocks, buildings of varying height, street furniture.
- [ ] Reloading with the same `SEED` reproduces an identical city.
- [ ] A different seed gives a different but still plausible city.
- [ ] Downtown blocks are visibly taller than residential blocks.
- [ ] No two buildings overlap their neighbours or the roads (spot-check several).
- [ ] Draw calls stay low while rendering 1000+ buildings (check `renderer.info.render.calls`).
- [ ] The day/night toggle visibly changes lighting and window glow.
- [ ] Regenerating repeatedly does not grow memory.
- [ ] Console is clean.

## Tune it

- **`BLOCK_SIZE`** — city grain; smaller feels dense, larger feels suburban.
- **Zoning radii** — how quickly the skyline falls off.

## Where it drifts

- **Buildings overlapping roads.** Lot subdivision that forgets to inset by the road width. Spot-check
  intersections; the check is visual but decisive.
- **Per-building draw calls.** The model builds a `Mesh` per building and the city crawls at 1500
  buildings. The merge/instance requirement and the `renderer.info` check are the guard.
- **Triangles exploding.** Too much rooftop and window detail. Watch the reported triangle count and
  reduce floor bands if needed.
- **Seeded PRNG consumed in a non-deterministic order.** If generation order depends on object
  iteration, the same seed gives different cities. The identical-reload check catches it.
- **Unrealistic uniform heights.** No zoning, all buildings the same height. The zoning rule and the
  downtown-vs-residential check address it.

## Provenance

- Technique: original, drawing on well-known city-generation approaches (road grid -> blocks -> lots ->
  massing); the pinned seed and draw-call discipline are the reproducibility contributions.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
