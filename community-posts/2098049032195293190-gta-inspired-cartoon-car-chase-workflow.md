---
id: astra-post-2098049032195293190
title: "GTA-inspired cartoon car chase workflow"
author: "PixVerse"
author_url: "https://x.com/PixVerse"
original_post: "https://x.com/PixVerse/status/2098049032195293190"
posted_on: "2026-09-10"
media_type: image
media_url: "https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/939609b429641e344a40ab78f01e7bf6dbfd57e8e707db7765c81ae04057ac31.jpg"
live_demo: ""
source_list: "unknown"
source_list_url: "https://github.com/unknown"
source_license: MIT
tags: [gpt-6-astra, blender, unknown]
---

# GTA-inspired cartoon car chase workflow

**[PixVerse](https://x.com/PixVerse)** · 2026-09-10 · [original post ↗](https://x.com/PixVerse/status/2098049032195293190)

![preview](https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/939609b429641e344a40ab78f01e7bf6dbfd57e8e707db7765c81ae04057ac31.jpg)

## Prompt

```text
Create an original GTA-inspired cartoon car chase using this workflow:
Design: Define one main driver, one getaway car, one pursuing car, and one urban environment. Keep their designs consistent. Plan three 4-second shots: rear tracking pursuit, side tracking through a sharp turn, and a wide exit shot.
Build in Blender: Create clean gray models and functional character and vehicle rigs. No textures or UV unwrapping are required.
Animate and test: Animate the driver, steering, wheel rotation, vehicles, and cameras. Maintain coherent travel direction and vehicle order. Fix clipping, floating wheels, sliding tires, broken poses, and hands losing contact with the steering wheel.
Render in Blender: Render frames 1–288 at 1280×720, 24 fps. Assemble actual Blender-rendered frames into a complete 12-second gray-model master. Export each shot separately and render matching gray stills as shape and composition references.
Finish with [@PixVerse](plugin://pixverse@openai-curated-remote) Plugin: Use Seedance 2.5 at 720p, processing each shot separately. Use the Blender clips as motion references and the gray stills as shape references. Define a consistent cartoon color palette in the generation prompt. Preserve camera movement, action timing, character and vehicle designs, and vehicle count.
Review and deliver: Inspect both complete videos for visual defects and continuity. Repair Blender issues and regenerate only failed Seedance shots, with at most two retries per shot. Deliver the editable .blend, the native 720p Blender gray-model video, the separately labeled 720p Seedance version, and a brief assessment of remaining limitations.
```

## Provenance

- Original post: https://x.com/PixVerse/status/2098049032195293190
- Upstream list: [unknown](https://github.com/unknown) (MIT)

_Prompt text and preview collected from the public community post; all rights remain with the original author._
