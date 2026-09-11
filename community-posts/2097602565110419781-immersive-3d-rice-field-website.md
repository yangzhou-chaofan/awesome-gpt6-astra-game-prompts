---
id: astra-post-2097602565110419781
title: "Immersive 3D rice-field website"
author: "YouWare"
author_url: "https://x.com/YouWareAI"
original_post: "https://x.com/YouWareAI/status/2097602565110419781"
posted_on: "2026-09-09"
media_type: image
media_url: "https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/00a3d885b9462dcaa8cd54c0109462182b6382ea9924e0239258d2b2c51ad744.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, image, threejs, tripo]
---

# Immersive 3D rice-field website

**[YouWare](https://x.com/YouWareAI)** · 2026-09-09 · [original post ↗](https://x.com/YouWareAI/status/2097602565110419781)

![preview](https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/00a3d885b9462dcaa8cd54c0109462182b6382ea9924e0239258d2b2c51ad744.jpg)

## Prompt

```text
Build an immersive 3D rice-field website that runs in the browser, with the theme:
“A sea of green / Wind through the rice fields.”
Complete the code, install the necessary dependencies, and launch a preview. Do not stop at a proposal or implementation plan.

1. Visual Direction

The overall atmosphere should feel natural, peaceful, and refined, like an interactive landscape website with cohesive art direction.

The scene should include:

Foreground: clearly distinguishable slender leaves, curved stems, and a few drooping rice panicles.

Midground: a continuous rice field extending into the distance, with sufficient density and natural variations in spacing.
Background: an irregular tree line, layered low hills, and subtle atmospheric perspective.
Sky: soft gray-blue tones, subtle cloud variation, and a natural transition at the horizon.
Position the default camera slightly above the rice panicles, looking across the field toward the distant hills.
The sky should occupy approximately one-third of the frame, with the rice field dominating the composition.
Use primarily deep green, olive green, and yellow-green vegetation colors. Avoid fluorescent green.
Vary the height, orientation, curvature, and color of the rice plants naturally.

2. Animation Requirements
Wind must appear as continuous waves traveling laterally across the field:
Keep the roots mostly fixed, with progressively stronger movement toward the leaf tips and panicles.
Plants in the same area should move coherently while retaining individual variation.

Combine slow, large-scale wind waves with subtle local disturbances.

Avoid making all plants sway in perfect synchronization. Avoid translating entire plants or causing leaves to flicker.

Use a gentle default breeze that remains comfortable to watch over time.
3. Interaction Requirements
Provide simple controls that genuinely affect the scene:
Wind-speed slider: smoothly adjust the strength and speed of the wind animation.
Lighting modes: Morning, Afternoon, and Golden Hour. Coordinate changes to the sky, light direction, color temperature, and fog color.

View modes: Open Field and Among the Rice, with smooth camera transitions.

Pause/Resume: pause and resume the environmental animation.

Mouse movement may produce a very subtle camera response, but it should not cause dizziness.
Do not continuously rotate the camera through large angles by default.
4. Interface Design
Use a full-screen scene with an interface overlaid on top:
Top left: a small VERDANT wordmark.

Bottom left: the serif heading “A sea of green.”
Below it, the smaller subtitle “Nothing to do. Just follow the breeze.”
Bottom right: a compact, semi-transparent dark-green control panel.

Keep text legible, provide generous spacing, and avoid obstructing the main landscape with controls.

Controls must remain usable on narrow screens without overlapping.

5. Technology and Performance
Use Three.js. If an existing project is available, retain its build environment.
Use instancing and GPU vertex animation to handle large amounts of vegetation.
Avoid creating a separate draw object for every plant or updating every plant on the CPU each frame.
Reduce vegetation detail at greater distances and apply a reasonable pixel-ratio cap.
Prefer procedural geometry and materials to ensure reliable asset loading.
The scene must render in real time. Do not use a full landscape image or video as the main scene.
Model names and comparison labels will be added in post-production; do not include them in the scene.
6. Completion Criteria
After implementation, use the available browser tools to verify that:
The initial view renders correctly, with no obvious console errors.

Every control genuinely affects the scene.

The foreground, midground, and background have distinguishable depth and layering.
The rice plants are more than simple upright green lines.
Wind movement is continuous and natural, without obvious uniform repetition.
Camera transitions are smooth, and the interface remains usable on narrow screens.
If you cannot perform a particular check, state that clearly.
Finally, provide startup instructions and a summary of the features actually implemented.
```

## Provenance

- Original post: https://x.com/YouWareAI/status/2097602565110419781
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts) (MIT)

_Prompt text and preview collected from the public community post above; all rights remain with the original author._
