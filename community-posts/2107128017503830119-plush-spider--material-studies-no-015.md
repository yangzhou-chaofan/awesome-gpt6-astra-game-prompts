---
id: astra-post-2107128017503830119
title: "Plush Spider — Material Studies No. 015"
author: "Vib3Coded"
author_url: "https://x.com/vib3coded"
original_post: "https://x.com/vib3coded/status/2107128017503830119"
posted_on: "2026-10-05"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/ed63d889a696121e88eaebbb.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, 3d]
---

# Plush Spider — Material Studies No. 015

**[Vib3Coded](https://x.com/vib3coded)** · 2026-10-05 · [original post ↗](https://x.com/vib3coded/status/2107128017503830119)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/ed63d889a696121e88eaebbb.jpg)

## Prompt

```text
Build "Plush Spider" — Material Studies No. 015.

Format and style:
- A single self-contained HTML file on native WebGPU, fully procedural (no assets, no libraries).
- The same editorial style as the series: serif masthead, side specimen panel, live readouts, "Inside the experiment" notes.

The specimen: a cute plush spider sitting on a table.
- The body is one signed distance field:
  - a big round abdomen with knitted-looking stripes;
  - a smaller head-and-chest tucked into it, with two fuzzy cheeks;
  - a paler underside.
- The face:
  - two big glossy bead eyes on white felt discs;
  - a row of four tiny bead eyes above them;
  - blushing cheeks, an embroidered smile and two little felt fangs.
- Eight posable plush legs, four a side, sewn on along the chest. They are striped like socks, end in pale little feet, and have a wire inside.

Physics — body:
- XPBD soft body on a hex-cell lattice: co-rotational shape matching plus tetrahedral volume, 60 Hz, 6 substeps.
- Gravity and floor friction. The seat keeps its footing.
- The toy slowly rights itself toward the heading it last walked (posture with a yaw).
- The abdomen breathes: its cells' rest shapes and rest volumes swell.

Physics — legs:
- Each leg is an XPBD rod chain from a hip embedded in the body lattice to the toe.
- A blended pose in the body's frame (sit, stand, hang, curl, wave) pulls each point toward its target: firmly at the hip, less toward the toe. So the legs hold their shape but sag and swing.
- The wire is plastic: when the hand bends a leg past its give, the pose itself takes the new shape and the leg stays bent until "Straighten legs".
- Spheres riding the body keep the legs off it. Toes grip the table. The finger pushes the legs aside.
- Pulling a leg further than it reaches tows the spider by that hip.

Behaviour:
- Walking:
  - the body rises onto its legs with a height controller;
  - it is led toward a goal with a weak pull and turns to face it;
  - toes are drawn to footholds on the table;
  - an alternating four-and-four gait lifts the set that has fallen furthest behind and sets it down ahead, with a little arc;
  - it wanders on its own now and then.
- Curl up (button or a finger poke): the legs hug up over its back, the spider rolls away from the touch as a ball (no footing, no rolling resistance), then unrolls and rights itself.
- Hang on silk:
  - a springy thread that only pulls, from an anchor high above to a patch of the back;
  - it is reeled up off the table, swings when pushed, and its legs paddle the air;
  - pressing again lowers it back to the table.
- Wave: one front leg is raised and wiggles.
- With the Finger tool, the spider scuttles over to the finger.

Rendering:
- Shell fur: base plus N instanced shells, alpha-to-coverage under 4× MSAA.
  - The fur lie is carried by the deformation gradient, with a damped-spring tip lag.
  - Kajiya–Kay highlights, velvet sheen, a comb tool.
- Regions painted in rest space: abdomen stripes, pale underside, short pile around the felt eye discs, cheeks, smile groove, stitched seams round the hips.
- Legs are drawn each frame as plush tubes:
  - swept along a Catmull–Rom curve through each rod with a parallel-transport frame;
  - a slight knee bulge and a rounded little foot;
  - banded colour and a shorter pile.
- A thin glinting silk thread.
- Soft PCSS key-light shadows, contact occlusion on the studio floor, Khronos PBR Neutral tone mapping.
- NaN-safe WGSL: clamped pow and smoothstep, clamped post.

```

- Original post: https://x.com/vib3coded/status/2107128017503830119
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
