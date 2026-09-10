---
id: astra-3d-202
title: Procedural PBR Texture Set
category: assets
slug: pbr-texture-set
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.35
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: Canvas / WebGL
difficulty: intermediate
verified: draft
tags: [textures, pbr, procedural, canvas, glsl, seamless, assets]
license: CC0-1.0
---

# Procedural PBR Texture Set

> A seeded generator that outputs a seamless albedo / normal / roughness / AO texture set for any
> material — generated in the browser, download-ready.

## What you get

`texture-lab.html`, self-contained: a per-pixel procedural generator (rusty metal by default) that
writes four channels, derives a normal map from the height, tiles seamlessly, and offers PNG download
per map plus a preview sphere lit by the maps.

## Before you start

- **Runtime:** modern browser (uses OffscreenCanvas; fallbacks to a canvas element).
- **Dependencies:** none; plain Canvas 2D / WebGL.
- **Assets / inputs:** none. The noise is code.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior technical artist. Build a procedural PBR texture generator in one self-contained
texture-lab.html. No external assets, no image libraries.

Deliverable
- One HTML file, runs on double-click. Plain Canvas 2D (or raw WebGL) only — no Three.js needed for
  generation, though a small preview sphere is allowed and may load Three.js from a CDN.

Generator
- Declare `const SEED = 4242;` and `const SIZE = 512;`. All noise derives from a seeded PRNG, so the
  output is identical on every reload. Document this.
- Implement value/fBm noise yourself. No external noise library.
- Generate a "rusty metal" material by default with parameters exposed as constants: RUST_AMOUNT,
  SCRATCH_DENSITY, PITTING, SCALE.

Outputs (four maps, all seamless and tileable)
- albedo  — base metal colour modulated by rust and scratches.
- roughness — smooth metal vs. rough rust.
- height   — a greyscale displacement used to derive the normal map.
- normal   — derived from `height` with a Sobel operator; tangent-space, +Y up.
- Tileability is mandatory: the noise must wrap at the edges. Verify by tiling the preview 3x3 with
  no visible seams.

Preview and export
- A small Three.js sphere with MeshStandardMaterial using the albedo, normal and roughness maps, lit by
  an environment/hemisphere light, plus a 3x3 tiled plane showing seams.
- A "Download" button per map that saves a PNG. Also a "Download all" that zips is NOT required —
  four separate downloads are fine.
- A reload button that regenerates at the current SEED, and controls to change SEED and SCALE live.

Engineering
- Generation in a Web Worker if available so the UI does not freeze; fall back to synchronous.
- Separate: PRNG, noise, map generation, normal derivation, preview, export.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of texture-lab.html in one code block, with comments per stage.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.35` | The pixel pipeline is exact, but material look benefits from latitude. |
| `seed` | `4242` | API seed; the texture seed is the in-file `SEED`. |
| `max_output_tokens` | `6000` | Four generators, the normal derivation, the preview and export. |

## Expected output

- `texture-lab.html` — one file, roughly 400–650 lines.
- A Sobel-derived normal map and noise that wraps at the edges.

## Verify it worked

- [ ] The preview sphere shows a rusty metal surface lit correctly.
- [ ] The 3x3 tiled plane shows **no visible seams**.
- [ ] Reloading with the same `SEED` reproduces identical maps (compare a pixel or a hash).
- [ ] Changing `SEED` changes the pattern; changing `SCALE` changes the feature size.
- [ ] Each map downloads as a valid PNG at 512x512.
- [ ] The normal map responds to light direction correctly (no inverted green channel).
- [ ] The UI stays responsive during generation.
- [ ] Console is clean.

## Tune it

- **`SCALE`** — feature size; the single most visible dial.
- **`RUST_AMOUNT`** — material identity.

## Where it drifts

- **Seams at the tile boundary.** The most common failure: noise is generated without a wrapping
  lattice. The 3x3 tiling check is the guard and it is not optional — a set with seams is unusable.
- **Inverted normal map.** Green channel flipped, so lighting looks like dents instead of bumps. The
  "responds correctly to light direction" check catches it; test with a single directional light.
- **Unseeded output.** `Math.random()` in the noise. The identical-reload check exposes it.
- **`toDataURL` on a tainted canvas.** Only if external images were loaded; this recipe forbids them,
  which is partly why it forbids them.

## Provenance

- Technique: original; procedural texture generation is well-trodden, made reproducible here by the
  pinned seed, the four-map contract, and the tiling check.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
