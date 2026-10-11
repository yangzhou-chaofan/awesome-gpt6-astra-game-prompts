---
id: astra-post-2108912941328154844
title: "Interactive 3D cloth simulation on a chrome sphere"
author: "EvoLink.ai"
author_url: "https://x.com/EvoLinkAi"
original_post: "https://x.com/EvoLinkAi/status/2108912941328154844"
posted_on: "2026-10-10"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/6c2eee2aa58464b61bb23a79.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, physics]
---

# Interactive 3D cloth simulation on a chrome sphere

**[EvoLink.ai](https://x.com/EvoLinkAi)** · 2026-10-10 · [original post ↗](https://x.com/EvoLinkAi/status/2108912941328154844)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/6c2eee2aa58464b61bb23a79.jpg)

## Prompt

```text
Build a polished, interactive 3D cloth simulation for a visual comparison between AI coding models.

The central visual: a square piece of fabric drops onto a stationary chrome sphere. We repeat the exact same drop with progressively denser cloth meshes, showing how the deformation changes.

Create a working browser application using Three.js and TypeScript/JavaScript. Implement and run it in the current workspace. Complete the project autonomously, test it, and fix problems before finishing.

VISUAL DIRECTION

Aim for a premium, oddly satisfying 3D animation: one large, clearly visible subject, beautiful fabric, convincing contact, and restrained studio lighting.

Use a 16:9 composition. The finished recording will be stacked with two other recordings inside a vertical 9:16 video, so everything must remain legible when reduced to one-third of a phone screen.

Scene:
- A stationary, polished chrome sphere above a matte dark charcoal floor.
- A square of rich coral-red satin fabric suspended horizontally above it.
- Fabric side length approximately 2.6 times the sphere diameter, so the edges can drape around the sphere.
- A large soft key light, gentle fill, and a subtle rim light.
- Broad studio reflections that make the chrome readable.
- Soft contact shadows and visible folds.
- A restrained dark background, with strong separation between fabric, sphere, and floor.

The fabric should look like woven satin, not rubber, liquid, foil, or plastic. Use subtle texture and restrained sheen. Render both sides correctly.

Choose a fixed, slightly elevated three-quarter camera angle that reveals the sphere’s top and the hanging fabric edges. Keep the subject large while leaving enough room for the initial drop.

No camera orbit during the automatic showcase. No decorative dashboard, branding, model names, introductory splash screen, or unnecessary text.

REAL CLOTH SIMULATION

Use a real-time physical simulation. A position-based or extended position-based dynamics solver is appropriate, but choose an implementation you can make reliable and performant.

The motion must emerge from gravity, constraints, and collision handling.

Do not:
- Replace the cloth with a prerecorded video.
- Use a shader wave or a canned vertex animation as a substitute for simulation.
- Animate vertices toward a precomputed draped shape.
- Display arbitrary face counts unrelated to the mesh.
- Swap in a high-resolution cloth while displaying a low-resolution label.

Implement:
- Gravity.
- Structural constraints that resist stretching.
- Shear resistance.
- Bending resistance.
- Damping.
- Stable sphere and floor collisions.
- A small collision margin that prevents visible intersections without making the cloth float.
- Consistent simulation timing independent of rendering frame rate.

The cloth is completely free when released: do not pin its corners.

Use the same physical dimensions and target material properties at every mesh density. Account for mesh spacing when setting masses and constraints so changing the mesh density does not arbitrarily change total mass or fabric stiffness.

Use the same deterministic initial setup at every level. A small fixed offset or rotation relative to the sphere is acceptable to create attractive asymmetric folds, but keep it identical across all runs.

Prioritize preventing the cloth from cutting through the sphere. At coarse mesh resolutions, checking only vertices is insufficient: an edge or triangle can intersect the sphere while
```

- Original post: https://x.com/EvoLinkAi/status/2108912941328154844
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
