---
id: astra-post-2109323105617281235
title: "Plush Octopus Interactive WebGPU Experience"
author: "shmopix"
author_url: "https://x.com/shmopixbzn"
original_post: "https://x.com/shmopixbzn/status/2109323105617281235"
posted_on: "2026-10-11"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/6fb254c15356c4448959274f.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, webgpu]
---

# Plush Octopus Interactive WebGPU Experience

**[shmopix](https://x.com/shmopixbzn)** · 2026-10-11 · [original post ↗](https://x.com/shmopixbzn/status/2109323105617281235)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/6fb254c15356c4448959274f.jpg)

## Prompt

```text
Build “Plush Octopus”, a single-file interactive WebGPU experience with a WebGL 2 fallback.
Design: Use a warm ivory background, muted coral and sage accents, thin borders, generous whitespace, and a large italic serif title: “Plush / Octopus.” Add the small kicker “Material Studies / No. 022.” Keep text minimal and the UI in English. No studio branding. Place the octopus on the left and a compact control panel on the right. Make the layout responsive for mobile.
Octopus: Create the entire toy procedurally—no imported 3D models. Give it a softly sagging mantle, eight tapered curling arms, heavy-lidded button eyes, a small side siphon, and two rows of cream-colored suckers beneath each arm. Use soft velvet shading with subtle directional nap and gentle blush waves. Avoid harsh speckles or flickering surface noise.
Physics: Make it feel like a lightly stuffed, jelly-like plush. The mantle should squash, spread sideways while preserving volume, and wobble briefly after release. Use a surface-net mesh driven by an XPBD soft-body lattice. Keep deformation centered so it cannot create unwanted sideways motion. Arms should bend smoothly and retain their shape like soft wire, with stable length constraints even during fast dragging. Include gravity, floor friction, and breakable sucker adhesion.
Interactions:
Hand: Lift, squash, release, and bend individual arms. Held arms gradually wrap around the hand.
Finger: Attract an arm; tapping the mantle makes the octopus briefly startle and pale.
Brush: Stroke the velvet to change its nap.
Actions: Crawl, Hide, Reach, Blush, Smooth nap, Reset.
Sliders: Stuffing, Wire stiffness, Grip.
Palettes: Coral, Dusk, Sea glass.
Include quarter-speed and mesh toggles, a live status indicator, and compact Mass, Volume, Grip, and Blushes readouts.
Animation and rendering: Add slow breathing, occasional blinking, and independent tip movement. Use fixed simulation steps with render interpolation and smoothly blended behaviors. Motion must settle naturally without perpetual rocking, snapping, stretching, or tube-frame flips.
Render one continuous, soft floor shadow that follows the body and arms. Prevent visible circular shadow stamps, dark overlap patches, and depth artifacts. Shadows should broaden and fade as the octopus rises.
Deliver one self-contained HTML file. Aim for smooth 60 fps on capable devices and test idle stability, extreme arm pulls, squash-and-release, lifting, behavior transitions, and mobile input.
```

- Original post: https://x.com/shmopixbzn/status/2109323105617281235
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
