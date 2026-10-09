---
id: astra-post-2107977713415864782
title: "Atoll Jelly interactive WebGPU lagoon diorama"
author: "Vib3Coded"
author_url: "https://x.com/vib3coded"
original_post: "https://x.com/vib3coded/status/2107977713415864782"
posted_on: "2026-10-07"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/26a174daf232bd730bc6ad1d.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, threejs]
---

# Atoll Jelly interactive WebGPU lagoon diorama

**[Vib3Coded](https://x.com/vib3coded)** · 2026-10-07 · [original post ↗](https://x.com/vib3coded/status/2107977713415864782)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/26a174daf232bd730bc6ad1d.jpg)

## Prompt

```text
Build "Atoll Jelly" — one self-contained HTML file, native WebGPU + WGSL, sim in plain JS, no external requests. An entry in the editorial "MATERIAL STUDIES" series of interactive jelly dioramas: a square cut-out block of turquoise jelly lagoon in the Maldives with a palm islet, a jetty of overwater bungalows, a seaplane that runs its own day, and reef life under the jelly.

PAGE: warm paper (#ece9e3), ink #241f1d, accent #12a2a6, italic serif H1 "Atoll / Jelly.", eyebrow "MATERIAL STUDIES", caption "Six bungalows on stilts, a seaplane that comes and goes, and eagle rays gliding through the jelly below." Status pill "WEBGPU · LIVE". Right glass panel: "THE LAGOON" with three dark buttons "Seaplane", "Feed the fish", "Float ring", a thin meter, tally "Landings · Fed · Afloat"; "FLAVOUR" swatches Turquoise / Sapphire / Lime; sliders Firmness, Wave damping, Tide (±10 cm); Reset · Pause · Reset view. Bottom-left "HOW TO PLAY": "Stir the lagoon. Feed the fish. Wave the seaplane off." + one grey line of gestures. Mobile bottom sheet, touch orbit/pinch, WebGPU fallback card, no scroll, no console errors.

SCENE (block 5.2², sea level 1.3): white-sand lagoon ~0.3 deep sloping into a deep "blue hole" near the front corner; eight coral heads (bumps) dressed with brain corals, branching corals and sea fans in pink/purple/orange/yellow/teal that sway slightly; a sandy islet in the back-left corner (beach ring, low wooded hump, gummy shrubs, two thatched parasols with loungers) with 8 lush coconut palms (16 arching pinnate fronds each + dry hanging fronds); an open lobby pavilion under a big hipped thatch roof. A plank jetty on thin stilts runs from the islet diagonally across the lagoon with low lamp posts; five bungalows hang off it on alternating sides plus a larger one at the end: plank decks on stilts, pale timber huts with glass doors to the sea, hipped thatched roofs (banded straw texture), plunge pool, two loungers, a steel ladder into the water. A floating seaplane pontoon with a tiny thatched shade, linked to the islet's south beach by a stilted walk. Block cut faces show candy strata (sand, shell band, caramel, chocolate) under translucent jelly walls.

WATER (as "Island Jelly"): linear shallow-water sim (168² staggered grid, 120 Hz, √(g·depth) wave speed, small surface tension, damping), finger stirring, block tilting with slosh, floating bodies hand displaced volume back to the sea, splash craters + bubbles, a foam field (white water that fades and laces), caustics, light shafts, refraction, Beer–Lambert flavour absorption, shoreline lace.

SEAPLANE (twin-engine floatplane: white with teal cheatline, high wing with teal tips, struts, twin floats, 3-bladed propellers spinning in the vertex shader): a fixed daily loop — wait at the pontoon → pivot 180° on its floats → taxi out → take-off run (spray) → climb → a racetrack circuit around the diorama at ~3.1 height with banking → approach → touchdown with crater, white water and a jolt → landing run → turn → taxi back to the pontoon. On water it rides the jelly: four float samples set height, pitch and roll; its floats push volume into the sim (wake) and foam. "Seaplane" button: leave now if waiting, or hurry the circuit to land early. Counts landings.

REEF LIFE: 42 boids fish in four colour kinds (yellow tang, blue with yellow tail, black-white banded, orange with white bars), schooling with their own kind, wandering, kept in the water (off the floor, under the surface, out of the shallows
```

- Original post: https://x.com/vib3coded/status/2107977713415864782
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
