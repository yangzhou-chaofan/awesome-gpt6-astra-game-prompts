---
id: astra-3d-205
title: Texture Atlas Packer
category: assets
slug: texture-atlas
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.25
top_p: 0.9
seed: 4242
max_output_tokens: 5500
runtime: Node 20+ CLI
stack: Node / Sharp
difficulty: beginner
verified: draft
tags: [node, sharp, atlas, maxrects, texture, tooling, assets]
license: CC0-1.0
---

# Texture Atlas Packer

> A CLI that packs a folder of PNGs into a power-of-two atlas plus a JSON manifest — the unglamorous
> tool every 2D/3D asset pipeline needs.

## What you get

`pack-atlas.mjs`: reads a directory of images, packs them with a MaxRects algorithm, writes
`atlas.png` and `atlas.json` (with per-frame UV rects, trimmed bounds and pivot), and supports
padding, power-of-two constraint, rotation and a `--check` mode that verifies every input landed.

## Before you start

- **Runtime:** Node 20+.
- **Dependencies:** `sharp` for image decoding/encoding (install with `npm i sharp`). The packing
  algorithm itself must be dependency-free.
- **Assets / inputs:** a folder of PNGs, e.g. `./input`.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior tooling engineer. Write a Node 20 CLI `pack-atlas.mjs` that packs a folder of PNGs
into a texture atlas with a JSON manifest.

Deliverable
- One ESM file, `pack-atlas.mjs`, run as `node pack-atlas.mjs --in <dir> --out <dir> [options]`.
- `sharp` is the only dependency, and only for reading image sizes and writing the output PNG. The
  packing algorithm must be implemented from scratch in the file.

Packing
- Implement the MaxRects bin-packing algorithm (choose a documented heuristic — Best Short Side Fit is
  fine) and explain the choice in a comment.
- Options (with defaults): `--padding 2`, `--power-of-two true`, `--allow-rotation true`,
  `--max-size 4096`, `--trim true`.
- When `--power-of-two` is on, grow the atlas to the next power of two in both dimensions.
- Rotation: allow 90-degree rotation only if it improves the result; record the rotation in the manifest.
- If the images do not fit in `--max-size`, FAIL loudly with the list of images that did not fit.

Trimming (when `--trim`)
- Detect and remove fully transparent borders from each frame, record both the trimmed rect and the
  original size, and store a `sourceSize` and `spriteSourceSize` so an engine can reconstruct the
  original placement.

Output
- `atlas.png` in the output directory.
- `atlas.json` with: the atlas size, a `frames` map keyed by original relative filename, each with
  `{ frame: {x,y,w,h}, rotated, trimmed, spriteSourceSize: {x,y,w,h}, sourceSize: {w,h}, pivot }`,
  and a `meta` block with `image`, `size`, `scale` and `format`.
- `--check` mode: after packing, verify every input file appears in the atlas exactly once, that no
  frame overlaps another, and that every frame is inside the atlas bounds. Print PASS/FAIL and exit
  non-zero on any violation.

Structure
- Separate: CLI parsing, image loading, rect packing (pure function), compositing, manifest writing,
  verification. The packing function must be pure and take/return plain objects.
- Print a summary: input count, atlas size, occupancy percentage, and elapsed ms.

Output
- Output ONLY the full contents of pack-atlas.mjs in one code block, with comments for the algorithm
  choice and the manifest schema.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.25` | Geometry packing and manifest schema are exact. |
| `seed` | `4242` | API seed; packing is deterministic given input order (which is sorted). |
| `max_output_tokens` | `5500` | Algorithm, compositing and verification. |

## Expected output

- `pack-atlas.mjs` — one file, roughly 350–550 lines.
- A pure `pack(rects, options)` function, and a `--check` verification path.

## Verify it worked

- [ ] `node pack-atlas.mjs --in ./input --out ./out` writes `atlas.png` and `atlas.json`.
- [ ] Every input PNG appears in `frames` exactly once.
- [ ] No two frames overlap and all lie within the atlas bounds (`--check` PASS).
- [ ] With `--power-of-two`, the atlas dimensions are powers of two.
- [ ] With `--trim`, transparent borders are removed and `spriteSourceSize` reconstructs the original.
- [ ] Images that cannot fit under `--max-size` cause a loud, non-zero failure listing them.
- [ ] Input order does not change the output (sort inputs before packing).
- [ ] Occupancy percentage printed is plausible for the test set.

## Tune it

- **`--padding`** — bleeding prevention; raise for texture-filtered 3D, lower for pixel art.
- **Heuristic** (Best Short Side Fit vs. Best Area Fit) — occupancy vs. execution time.

## Where it drifts

- **Overlapping frames.** Off-by-one in the rect split is pervasive. The overlap check in `--check` is
  the whole reason that mode exists — run it.
- **Non-deterministic packing.** Directory read order differs between machines, so the atlas differs.
  The sorted-input requirement and the order-independence check fix it.
- **Trimming that loses alignment.** The frame is trimmed but `spriteSourceSize` is not written, so
  sprites render shifted. Test a sprite with an off-centre opaque region.
- **Rotation recorded but not applied.** The manifest says rotated but the pixels are not. Compare a
  rotated frame against its source by eye once.

## Provenance

- Technique: MaxRects is a published packing algorithm; the CLI shape and the `--check` contract are
  the reproducibility contribution here.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
