---
id: astra-post-2110046350142235020
title: "Interactive jelly snow globe village"
author: "Paruchh"
author_url: "https://x.com/theparuchh"
original_post: "https://x.com/theparuchh/status/2110046350142235020"
posted_on: "2026-10-13"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/abc4533a9f83cc86d0e9eaa2.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, threejs]
---

# Interactive jelly snow globe village

**[Paruchh](https://x.com/theparuchh)** · 2026-10-13 · [original post ↗](https://x.com/theparuchh/status/2110046350142235020)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/abc4533a9f83cc86d0e9eaa2.jpg)

## Prompt

```text
SHAKE WELL

Build one self-contained HTML file, shake-well.html: a glass snow globe on a table with a tiny winter village inside, made of jelly. Original design only: no real brands, logos, characters or text from real products. Open it and check it runs before you finish.

THREE.JS ONLY
- All rendering goes through Three.js: import exactly three@0.180.0 from a CDN with an import map and use WebGLRenderer
- Only Three.js and its official addons (three/addons: OrbitControls, EffectComposer, bloom, depth of field, RoomEnvironment and so on). No other libraries
- No raw WebGL or WebGPU code: no getContext, no direct gl calls. Custom shaders only through Three.js materials (ShaderMaterial or onBeforeCompile)
- All physics and motion are your own plain JavaScript. No physics libraries, no external models or textures, all geometry and materials procedural

FIRST STEP, BEFORE ANYTHING ELSE
Run a shell command that creates a unique run ID and the current time, and saves both to run-log.txt next to your HTML. Print the run ID once in your reply. You will need it at the end to find your own session log.
After every major step (globe, village, room, each toy, demo), read your session log and append the running token totals and the current time to run-log.txt. If your context gets compacted, these checkpoints keep the earlier usage.

The picture matters most. It should look like a high-end product shot of a handmade collectible.

THE GLOBE
- A large glass sphere on a turned dark-walnut base with a thin brushed-brass ring. The glass is perfectly clear and thick at the edges, with two soft rectangular studio highlights and a thin bright rim where it curves away
- The globe is filled with clear liquid. The village looks slightly magnified through it, like a real lens, and bends at the edges
- A small air bubble is trapped at the very top and always slides to the highest point when the globe tilts
- About 6000 white flakes float inside, plus a few hundred tiny gold glitter specks that flash when they turn to the light

THE VILLAGE (all jelly)
- A small snowy hill fills the bottom of the globe. Every building, tree and figure is glossy translucent jelly, like gummy candy: raspberry, tangerine, lemon, mint, blueberry, grape. Light passes through and glows softly inside them, with sharp wet highlights and a few tiny frozen air bubbles in each piece
- 8 to 10 small houses with steep roofs, round windows and chimneys around a little square. In the center: a clock tower with a bell and a round clock face
- A frozen pond of pale blue jelly ice with three tiny skaters gliding in slow loops. A creek with an arched bridge. A snowman. A ring of dark-green jelly pines with white snow tips
- A tiny jelly train (engine plus three cars, round headlight) runs on a loop track around the village, forever
- Snow on roofs and ground is soft matte white, like powdered sugar, contrasting with the glossy jelly

THE ROOM
- Calm and clean, studio-like. A warm wooden tabletop, a soft contact shadow under the base, a dark dusty-blue backdrop with a few out-of-focus warm bokeh lights far behind
- Warm key light from the upper left, cool fill from the right, a rim light that outlines the glass
- The globe is centered and fills about 70% of the frame height. It must read well in a square crop and in a portrait 9:16 crop. The background stays soft so the globe pops

TOYS (small pill buttons at the bottom, minimal UI, keys 1 to 5)
1. Shake. The globe jolts and tilts, the snow explode
```

- Original post: https://x.com/theparuchh/status/2110046350142235020
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
