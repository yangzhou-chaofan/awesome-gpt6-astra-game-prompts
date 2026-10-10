---
id: astra-post-2108336611796615233
title: "Pirate Jelly interactive WebGPU diorama"
author: "Vib3Coded"
author_url: "https://x.com/vib3coded"
original_post: "https://x.com/vib3coded/status/2108336611796615233"
posted_on: "2026-10-08"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/3e11594c7ee5498702d6d86b.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, webgpu]
---

# Pirate Jelly interactive WebGPU diorama

**[Vib3Coded](https://x.com/vib3coded)** · 2026-10-08 · [original post ↗](https://x.com/vib3coded/status/2108336611796615233)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/3e11594c7ee5498702d6d86b.jpg)

## Prompt

```text
Create a self-contained interactive WebGPU/WGSL page "Pirate Jelly" — part of a "Material Studies" series of jelly dioramas. Single HTML file, no external models, textures, fonts or libraries; everything procedural. English UI.

LOOK & LAYOUT
- A square block of translucent jelly sea (≈5.2 × 5.2 units) standing on a paper-studio floor; the camera looks in at the front corner at ~27°. The block's cut faces show candy strata (chocolate bedrock, caramel clay, a shell band, vanilla sand); the sea surface and walls refract and tint what's behind them, with caustics on the sea floor, light shafts, a tinted caustic shadow on the floor, foam lace on the shoreline and a bright meniscus on the cut edges.
- A small tropical island toward the back: sandy beach, a cove facing the viewer, a mossy jungle hump with ~9 gummy palms (ringed caramel trunks, translucent fronds that flutter), lumpy gummy bushes with flowers, ferns, beach grass, rocks around the shore.
- SKULL ROCK at the island's west tip, standing in the shallows: a cartoon skull sculpted as a signed-distance field (cranium, cheekbones, jaws, deep eye sockets, heart-shaped nose, crack on the crown, rock strata and noise, moss on top, a wet band at the waterline), meshed with surface nets; two rows of separate box teeth set into a carved grin. At night its eye sockets glow like a candle-lit cave.
- A PIRATE SHIP riding at anchor in front of the island, seen at three-quarters from the stern: black hull with an ochre gunport strake, red bottom, gunports with cannons, raised quarterdeck with lit stern windows and a stern lantern, three masts (square courses and topsails on fore and main, a gaff sail on the mizzen, a jib to the bowsprit), shrouds and stays, and a Jolly Roger (skull and crossed bones drawn procedurally in the shader) streaming aft. Her anchor chain runs from the bow down through the jelly to an anchor lying on the sea floor.
- The camp on the cove beach: a campfire (stone ring, teepee of logs with glowing ends, embers, a tripod with a pot, two seating logs), an iron-bound treasure chest under a leaning palm with a hinged lid and a heap of gold and gems inside, a shovel in a sand heap, barrels, a crate, a pyramid of round shot, a rum bottle, a rowing boat pulled up with its bow on the sand, and an "X" scored in the sand.
- On the sea floor: the bow half of an old wreck lying on its side with ribs showing and its broken mast beside it, swaying kelp, a few doubloons, bubbles caught in the jelly.

SIMULATION
- Linear shallow-water waves on a staggered grid with a little surface tension (springy jelly); the block can be tipped and the sea sloshes and the jelly wobbles (shear + squash).
- The ship floats on 10 buoyancy points (heave, pitch, roll), is pushed by a gently veering offshore breeze, held by an elastic anchor rode at the bow, and weathervanes into the wind. Her displaced volume is handed back to the sea, so she makes a wake.
- Rigid bodies: cannonballs (dense, fly in a clean arc, punch a crater, sink and roll on the floor), barrels (float on their side), doubloons (flutter down and settle flat). All interact with the sea (buoyancy, drag, splashes, bubbles), the terrain, the skull, the props, the palm trunks and the ship's hull.
- One particle system: fire flames (additive), embers, woodsmoke, muzzle flash, white gunsmoke, sea spray, sand puffs, gold glints over the open chest, fireflies at night.

INTERACTION
- Tap the ship → fire the next gun on the side facing the viewer (b
```

- Original post: https://x.com/vib3coded/status/2108336611796615233
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
