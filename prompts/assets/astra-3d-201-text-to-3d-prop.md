---
id: astra-3d-201
title: Text → Low-Poly Prop (GLB)
category: assets
slug: text-to-3d-prop
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.4
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: Blender 4.x CLI
stack: Blender 4.x
difficulty: intermediate
verified: draft
tags: [blender, gltf, glb, low-poly, procedural-modeling, assets]
license: CC0-1.0
---

# Text → Low-Poly Prop (GLB)

> Describe a prop, get a Blender script that builds it procedurally and exports a game-ready GLB —
> no hand-modelling, no downloaded models.

## What you get

A `build_prop.py` script. Run it headless with Blender and it constructs a low-poly prop from
primitives, applies sensible UVs and a flat material palette, and exports a `.glb` plus a validation
report. This is the reproducible alternative to asking a model for a mesh: the *script* is the
artifact, so the geometry is inspectable and parameterised.

## Before you start

- **Runtime:** Blender 4.x, invoked headless (`blender --background --python build_prop.py`).
- **Dependencies:** none beyond Blender.
- **Assets / inputs:** none.
- **Model access:** plain chat completion (optionally with code-execution to run Blender).

## The prompt

```text
You are a technical artist writing Blender Python. Produce a script `build_prop.py` that builds a
low-poly treasure chest procedurally and exports it as a game-ready GLB.

Hard requirements
- Blender 4.x Python API only. No add-ons. The script must run headless:
  `blender --background --python build_prop.py`.
- Declare parameters at the top: WIDTH, DEPTH, HEIGHT, PLANK_COUNT, HAS_LID, BEVEL, SEED.
  Derive all geometry from these; no magic numbers buried in the body.
- Build from primitives (cubes, cylinders), combining them with clean topology. Target 300-800
  triangles for the whole prop.
- Use a small seeded PRNG for any variation (plank jitter). The same SEED must produce identical
  vertices. No random module usage without a fixed seed.

Materials and UVs
- 3-4 flat-coloured materials (wood_dark, wood_light, metal, metal_dark) assigned per face region.
  No textures, no image baking.
- Smart UV project the final mesh, then pack islands. Report the resulting UV bounds in the log.

Export
- Apply all modifiers and transforms before export.
- Export GLB to `out/chest.glb` with +Y up, correct scale (1 unit = 1 metre), and materials embedded.
- After export, validate by re-importing the GLB into a fresh scene and printing:
  triangle count, material names, bounding box dimensions, and whether the mesh is manifold.
- Fail loudly (non-zero exit) if the triangle count exceeds 1200 or the mesh is not manifold.

Structure
- Organise the script into functions: parameters, build_body, build_lid, add_details, assign_materials,
  unwrap_and_pack, apply_and_export, validate. A `if __name__ == "__main__":` block runs them in order.
- Print a one-line summary at the end: file path, triangles, materials, bbox.

Output
- Output ONLY the full contents of build_prop.py in one code block. No explanation before or after.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.4` | Modeling scripts tolerate a little stylistic latitude; the export contract keeps them honest. |
| `seed` | `4242` | API seed; the *geometry* seed is the in-script `SEED`. |
| `max_output_tokens` | `6000` | Fits the script and its validation block. |

## Expected output

- `build_prop.py` — one script, roughly 250–450 lines.
- Running it produces `out/chest.glb` and a printed validation summary.

## Verify it worked

- [ ] `blender --background --python build_prop.py` exits 0 and writes `out/chest.glb`.
- [ ] The printed triangle count is between 300 and 800.
- [ ] Re-running with the same `SEED` produces an identical file (compare a hash of the GLB).
- [ ] Changing `SEED` jitters the planks; changing `PLANK_COUNT` adds planks.
- [ ] The re-import check reports a manifold mesh and 3–4 named materials.
- [ ] The GLB opens in a glTF viewer with correct scale and +Y up.
- [ ] Deliberately setting an impossible triangle budget makes the script exit non-zero.

## Tune it

- **`PLANK_COUNT`, `BEVEL`, `HAS_LID`** — the shape dials.
- **Triangle budget** — raise it for more detail, but keep the fail-loud check meaningful.

## Where it drifts

- **Blender API drift.** 3.x vs. 4.x changed several operator signatures (`bpy.ops.mesh.primitive_*`,
  UV packing). The script is pinned to 4.x; on another version it should fail loudly rather than
  silently produce an empty file. Run the validation check before trusting output.
- **`bpy.ops` context errors in background mode.** Operators need a valid context; the model often
  writes code that only works in the GUI. The headless requirement is the guard — if it does not run
  with `--background`, it is not accepted.
- **Un-applied modifiers.** Exported GLB keeps pre-modifier geometry. The "apply all modifiers before
  export" requirement prevents it; verify by re-importing.
- **Non-deterministic output.** `random` used without seeding, or dict ordering. The GLB hash check
  catches it.

## Provenance

- Technique: original; procedural modelling + headless export is a standard technical-art pattern,
  framed here so the *script* is the reproducible deliverable.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
