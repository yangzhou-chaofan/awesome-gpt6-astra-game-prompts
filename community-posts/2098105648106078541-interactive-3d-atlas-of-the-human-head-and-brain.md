---
id: astra-post-2098105648106078541
title: "Interactive 3D atlas of the human head and brain"
author: "BuBBliK"
author_url: "https://x.com/k1rallik"
original_post: "https://x.com/k1rallik/status/2098105648106078541"
posted_on: "2026-09-10"
media_type: image
media_url: "https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/1251cdb60d51985d09d2870c9866d104d26bf152875bc50a1c46eb047a11be63.jpg"
live_demo: ""
source_list: "unknown"
source_list_url: "https://github.com/unknown"
source_license: MIT
tags: [gpt-6-astra, unknown]
---

# Interactive 3D atlas of the human head and brain

**[BuBBliK](https://x.com/k1rallik)** · 2026-09-10 · [original post ↗](https://x.com/k1rallik/status/2098105648106078541)

![preview](https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/1251cdb60d51985d09d2870c9866d104d26bf152875bc50a1c46eb047a11be63.jpg)

## Prompt

```text
Build a complete interactive 3D atlas of the human head and brain. Deliver a working application, not a mockup. Make reasonable decisions independently, implement it, test it, and visually verify the result.

Use Three.js and real, appropriately licensed Z-Anatomy / BodyParts3D meshes. Include the skull, teeth, facial muscles, brain, eyes, cranial nerves, arteries, veins, and available supporting membranes. Preserve their original anatomical relationships. Aim for hundreds of individually selectable structures, report the actual imported count, and retain source attribution.

Create a clean, light interface with a pale grey background, white rounded panels, restrained blue-grey accents, and readable typography. Keep the model large, with a structure panel on the left, camera tools on the right, search at the top, and an explosion slider below. Use English throughout.

Make the anatomy progressively explorable:
Head → system → region → individual named structures.
For example: Brain → Cerebrum → Left hemisphere → Frontal lobe → individual structures.

Animate assembly and disassembly. Preserve source positions when assembled; arrange exploded groups in clearly separated layouts with readable labels. Indicate normalized scale and paginate large collections.

Include:
- Free rotation, wheel/pinch zoom, and camera presets.
- Disassembly slider and Shift + wheel control.
- Independent visibility switches for groups and individual parts.
- Group opacity, undo, restore all, and reset.
- Anatomical search, click-to-inspect, focus, isolation, and parent navigation.
- Anatomical colours, porcelain, wireframe, and transparent modes.
- Adjustable sagittal, axial, and coronal clipping planes with reverse direction.
- Labels, automatic exploration, fullscreen, and PNG export.
- A guided journey from the complete head into the brain and its networks.

Keep hidden structures hidden across layout and material changes. Explain that clipping planes produce open display cuts, not medical scans. Do not invent anatomy or claim clinical validation.

Deliver a standalone HTML containing the application and processed geometry, working offline without a server. Also provide clean source files, pinned dependencies, a lockfile, portable build scripts, an English README, and required licences and attribution. Exclude credentials, local machine paths, dependencies, and unrelated files.

Test geometry integrity, hierarchy membership, visibility, undo, and layout spacing. Inspect the running application in a browser, exercise the controls, check for console errors, and fix visual overlaps before delivering.
```

## Provenance

- Original post: https://x.com/k1rallik/status/2098105648106078541
- Upstream list: [unknown](https://github.com/unknown) (MIT)

_Prompt text and preview collected from the public community post; all rights remain with the original author._
