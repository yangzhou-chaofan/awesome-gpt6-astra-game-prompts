---
id: astra-3d-102
title: Seeded Procedural Terrain
category: systems
slug: procedural-terrain
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 7000
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, terrain, noise, seeded, deterministic]
license: CC0-1.0
---

# Seeded Procedural Terrain

> Deterministic terrain from a seed: same seed, same hills, every time — with biomes and a water line.

## What you get

`index.html`, self-contained: a seeded noise implementation, fBm terrain with configurable octaves,
height-based vertex colouring, a water plane, and a live GUI to change the seed and octaves and watch
the terrain rebuild. The reproducible world generator the other level recipes build on.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js and lil-gui via CDN import map (the GUI is optional; say so if omitted).
- **Assets / inputs:** none.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior graphics engineer. Build a seeded procedural terrain generator in one self-contained
index.html for Three.js.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. Terrain generated in code.

Noise
- Implement 2D simplex (or improved Perlin) noise YOURSELF in the file. No external noise library.
- Implement a seeded PRNG (e.g. mulberry32) and derive the noise permutation table from it, so the
  noise field itself is a pure function of the seed.

Terrain
- fBm: sum 4-8 octaves with configurable lacunarity (2.0) and gain (0.5), exposing `SEED`, `OCTAVES`,
  `FREQUENCY`, `AMPLITUDE` as constants at the top.
- A 256x256 grid over a 200x200-unit world, built as one BufferGeometry with computed vertex normals.
- Height-based vertex colours: sand near the water line, grass, rock, and snow above a threshold.
- A semi-transparent water plane at a fixed height with a gentle vertex ripple.

Interaction
- A small control panel (lil-gui or hand-rolled) to change SEED, OCTAVES, FREQUENCY and
  AMPLITUDE and rebuild the terrain immediately.

Determinism (the point of this recipe)
- Given the same SEED and parameters, the geometry must be identical on every reload. Document this in
  a comment. No use of Math.random() anywhere in generation.

Engineering
- requestAnimationFrame for the water animation; terrain rebuild is on demand, not per frame.
- Dispose of the previous geometry when rebuilding.
- Handle resize and devicePixelRatio. No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments naming the noise and
  fBm stages.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | Noise implementations are easy to get subtly wrong; keep it low. |
| `seed` | `4242` | API seed; the terrain seed lives in the prompt as `SEED`. |
| `max_output_tokens` | `7000` | Noise + fBm + geometry + GUI. |

## Expected output

- `index.html` — one file, roughly 450–700 lines.
- A self-contained noise implementation and a seeded permutation table — no `<script src>` to a noise
  library.

## Verify it worked

- [ ] Terrain renders with distinct sand, grass, rock and snow bands.
- [ ] Water sits at a fixed level and ripples gently.
- [ ] Reloading with the same `SEED` reproduces the terrain **byte-identically** (compare a height sample).
- [ ] Changing `SEED` produces completely different terrain.
- [ ] Increasing `OCTAVES` adds visible detail; decreasing it smooths the terrain.
- [ ] Rebuilding repeatedly does not grow memory (geometry disposed).
- [ ] No `Math.random()` appears in the generation path.
- [ ] Console is clean.

## Tune it

- **`OCTAVES`** — detail vs. cost. 6 is a good default.
- **`AMPLITUDE`** — dramatic mountains vs. rolling plains.

## Where it drifts

- **`Math.random()` sneaking into generation.** The single most common way "seeded" terrain is not
  seeded. The byte-identical reload check is the guard — sample one vertex height and compare.
- **Seeded permutation but unseeded gradient offsets.** The noise table is seeded, yet a per-call
  random offset remains. Again caught by the reload comparison.
- **fBm that normalises incorrectly.** Terrain flattens or clips as octaves change. Check that
  amplitude stays stable when `OCTAVES` changes.
- **Normals not recomputed after rebuild.** Lighting looks wrong on the new terrain. Part of the
  "dispose and rebuild" requirement.

## Provenance

- Technique: original; simplex/Perlin and fBm are standard, and the seeded-permutation trick is the
  reproducibility contribution.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
