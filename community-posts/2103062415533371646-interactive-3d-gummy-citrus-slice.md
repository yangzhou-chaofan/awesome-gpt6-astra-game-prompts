---
id: astra-post-2103062415533371646
title: "Interactive 3D gummy citrus slice"
author: "Vib3Coded"
author_url: "https://x.com/vib3coded"
original_post: "https://x.com/vib3coded/status/2103062415533371646"
posted_on: "2026-09-24"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/d0918b52d28c7f04dd734dd4.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab]
---

# Interactive 3D gummy citrus slice

**[Vib3Coded](https://x.com/vib3coded)** · 2026-09-24 · [original post ↗](https://x.com/vib3coded/status/2103062415533371646)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/d0918b52d28c7f04dd734dd4.jpg)

## Prompt

```text
Create a beautiful, interactive 3D gummy citrus slice using WebGPU. Deliver the complete experience in one standalone HTML file with embedded JavaScript and WGSL shaders.

This must be a real-time 3D simulation, not a video, image, or looping animation.

APPEARANCE

Create a thick, semicircular orange slice with translucent, juicy flesh, eight distinct segments, delicate internal membranes, tiny bubbles, a pale pith layer, and a soft orange rind.

Make it look like premium gummy candy: saturated color, glossy highlights, light passing through the flesh, convincing refraction, and soft contact shadows. Avoid excessive bloom, washed-out colors, or a hard plastic appearance.

Use a warm, light studio background and a clean editorial interface with generous whitespace. Add the large italic serif title “Citrus Jelly.” Keep controls compact and the slice clearly visible.

SOFT-BODY PHYSICS

The jelly feel is the most important part.

- Grab any part of the slice with a mouse or finger.
- Pull, lift, stretch, twist, and release it.
- Make deformation local: pulling one edge should stretch nearby flesh while the rest follows naturally.
- After release, the slice should wobble, overshoot, and gradually recover its original shape.
- Include gravity, inertia, damping, ground collisions, and soft bouncing.
- Preserve volume approximately and prevent the mesh from collapsing or turning inside out.
- Make the rind slightly firmer than the flesh.
- Internal segments, membranes, and bubbles must follow the deformation without floating outside the body.

Use a stable volumetric soft-body solver, such as a tetrahedral mesh with XPBD constraints. Do not imitate softness by scaling or rotating the entire object.

CONTROLS

Include three color presets: Orange, Lemon, and Ruby.

Add:
- Firmness slider.
- Internal damping slider.
- “Give it a nudge” button.
- Reset button.
- Quarter-speed checkbox.
- Show mesh checkbox.
- Pause/resume button.

Display small live readouts for mass, percentage of rest volume, and kinetic energy.

TECHNICAL REQUIREMENTS

Use genuine WebGPU rendering with WGSL shaders. Generate all geometry and visual details procedurally, without imported models or image files.

Keep simulation updates independent of rendering frame rate. Support desktop and touch devices. Show a clear fallback message if WebGPU is unavailable.

Test strong dragging, repeated releases, all controls, and narrow screens. Fix unstable physics, broken geometry, and visual artifacts before delivering the finished HTML.

The result should feel like a tiny, tactile candy experiment that is genuinely satisfying to play with.
```

- Original post: https://x.com/vib3coded/status/2103062415533371646
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
