---
id: astra-post-2102300855387205871
title: "Bubble Bay: 3D Water Balloon Battle"
author: "jared"
author_url: "https://x.com/jaredliu_bravo"
original_post: "https://x.com/jaredliu_bravo/status/2102300855387205871"
posted_on: "2026-09-22"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/9b06b2ff2bb286f0b00b6184.png"
live_demo: "https://bubble-bay.tripo.page/"
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab]
---

# Bubble Bay: 3D Water Balloon Battle

**[jared](https://x.com/jaredliu_bravo)** · 2026-09-22 · [original post ↗](https://x.com/jaredliu_bravo/status/2102300855387205871)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/9b06b2ff2bb286f0b00b6184.png)

## Prompt

```text
Build Bubble Bay, a playable Three.js water-balloon arena with the familiar big-headed, short-bodied, exposed-face costume-character style of classic bubble games. Default to detailed Tripo models with an obvious Three.js geometry comparison switch that preserves the match. Use three new characters: Langya, Shantao and Tuanli. Follow the supplied new character concept/model references, preserving their silhouettes, faces, colors and outfits.

Langya is a lively human boy in a turquoise hood with one connected sideways wave crest, orange collar/cuffs, navy shorts and turquoise shoes with orange soles. Shantao is a small human girl with a dark-plum bob, a peach-pink bonnet with three short petal ornaments on each side, mint jacket, plum short overalls and pale-yellow boots. Tuanli is a chubby human boy with a broad pear-shaped body, a caramel round padded cap with cream face trim, teal short jacket, cream lower belly and navy boots. All show warm skin-colored child faces with simple dark oval eyes and tiny smiles. These are children in newly designed costumes; do not turn them into literal aquatic creatures or reuse the prior recognizable character outfits. Generate each separately through Tripo CLI with explicit tripo-p2 and independent front/back images, then bind valid biped skeletons and skins. Idle/run/jump must drive actual joints; inspect motion, correct headgear/shoe/body weighting and keep provenance accurate. If motions are locally authored, identify them as such.

Localized names: 浪芽 / 랑야 / Langya, 珊桃 / 산타오 / Shantao, 团栗 / 퇀리 / Tuanli. Starting capacity/range/speed levels: 1/1/6, 1/2/5, 2/1/4; caps: 6/7/9, 6/7/8, 9/8/8. Convert speed to 0.25 + level*0.8 world units per second; tiles are 2 units. Choosing a character assigns the other two as distinct rivals with matching profiles. Keep the same gameplay hit radius regardless of the chubby visual silhouette.

Offer 15x13 Pirate/Patrit14 by default and Village10. Preserve recognizable gold deck, yellow cargo, wooden crates, four cannons and central mast; the village has four colored housing districts, a central road, hedges and toy blocks. Use publisher maps as reference, construct runtime artwork yourself, and document small route openings needed for continuous 3D movement and AI escape. Provide bright materials, shadows, ocean scenery, clear camera follow and overview.

One player faces two cooperating AI rivals. WASD/arrows move, F places a 2.5-second bubble, Space jumps onto real platforms, Shift dashes, Q/E orbits, V changes view and Escape pauses. Cross-shaped water respects obstacles, breaks the first soft block and chains bubbles. Implement trapping, escape, enemy captures, respawns, a selectable target of 3, 6, 9 or 12 captures (default 6), or 180-second scoring, result and retry. Touch joystick and action buttons must work simultaneously.

Use six generated Tripo pickups: balloon, range potion, roller skate, throwing glove, kick boot and rescue needle. Crates drop an item 85% of the time. Conditional item weights: 30/30/30/2.5/3.5/4 percent. Gloves add three throws, capped at six. G throws a nearby bubble up to four tiles over cover, preserving its owner and original fuse, reserving its landing and showing an arc. A bubble expiring in flight lands and explodes. K slides bubbles until blocked without resetting the fuse. X uses a rescue needle, starting at one and capped at three. Show inventory and available controls clearly.

Chinese, English and Korean UI: mainland-Chin
```

- Original post: https://x.com/jaredliu_bravo/status/2102300855387205871
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
