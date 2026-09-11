<div align="center">

# 🕹️ Awesome GPT-6 Astra · Game Prompts

### One prompt. One playable 3D game.

**26 reproducible recipes · 103 real community cases (101 with previews) · 6 playbooks · 93 creators credited**

[🚀 Start here](#-start-here) · [🏆 Featured](#-featured--worth-studying) · [🖼️ Gallery](#️-gallery) · [🎮 Games](#-games-21) · [🧪 Recipes](#-reproducible-recipes--26) · [📖 Playbooks](#-playbooks) · [🌐 Web viewer](site/index.html)

[![validate](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml)
[![license: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![model: gpt-6-astra](https://img.shields.io/badge/model-gpt--6--astra-6f42c1.svg)](https://platform.openai.com/docs/models)

</div>

---

**GPT-6 Astra** (OpenAI, released 2026-09-03) made *"describe a game, get a playable build"* real. Within its first week the community produced hundreds of working games, worlds and films from single prompts — most published on X with the prompt in the post or the replies. This repo is the organized version of that week:

| Layer | What it gives you | Where |
|---|---|---|
| 🖼️ **Cases** | See what others made — real previews, X provenance, verbatim prompts | `community-posts/` · `showcase/` |
| 🧪 **Recipes** | Reproduce it yourself — pinned model version, settings, inputs, acceptance checks | `prompts/` |
| 📖 **Methods** | Turn *your* idea into a working prompt — reusable play patterns | `playbooks/` · `skills/` |

**Sourcing rule:** X is the record of truth. Every case links back to its original post; prompts are only ever collected from the post itself or its replies. Aggregated from 10 community awesome-lists, deduplicated by post URL, every entry credited. Snapshot: 2026-09-11.

---

## 🚀 Start here

| I want to… | Do this |
|---|---|
| **See what's possible** | Scroll to the [Gallery](#️-gallery) — click any image to jump to the original X post |
| **Copy a prompt that worked** | Open any case → the `Prompt` section is the author's verbatim text |
| **Reproduce a result reliably** | Run [astra-3d-001 Endless Runner](prompts/full-games/astra-3d-001-endless-runner.md) — the smoke test for the whole recipe list |
| **Build my own idea** | Pick a pattern from [Playbooks](#-playbooks) — six battle-tested ways to assemble a prompt |
| **Explore interactively** | Open the [web viewer](site/index.html) or browse [10 playable worlds](#-playable-worlds--try-in-browser) |

---

## 🏆 Featured — worth studying

*Not just "looks good" — each pick comes with the specific thing it teaches.*

| | Case | What it teaches |
|---|---|---|
| ⭐ | [**Browser Flight Simulator with a Complete Flight Loop**](community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md) | Textbook acceptance chain: START → ACCELERATE → TAKE OFF → FLY → LAND → SCORE → PLAY AGAIN — and the prompt tells the model to test the whole loop itself and fix what breaks. |
| ⭐ | [**Windhaven Coastal Fantasy Adventure Game**](community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md) | The long-narrative prompt: art style → world → camera → negative constraints (no UI, no text, no logos) in one block that carries the whole build. |
| ⭐ | [**Three.js dark-fantasy action RPG**](community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md) | Best balance of mood and systems: how gothic-ruins imagery turns into executable requirements. |
| ⭐ | [**Rebuilding Lego 1999 Racers**](community-posts/2096438110095585753-rebuilding-lego-1999-racers.md) | Remastering pattern: memory points of the original give the model an alignment target — nostalgia plus modern feel. |
| ⭐ | [**Mini World 3D exploration game**](community-posts/2096641728497275011-mini-world-3d-exploration-game.md) | Designing for a real person (his 4-year-old son): zoom, camera and difficulty constraints written as playability. |
| ⭐ | [**Kaiju city battle**](community-posts/2096251574918013135-kaiju-city-battle.md) | Multiplayer-style city battle with a playable build — proof a single prompt can carry combat rules. |
| ⭐ | [**A crab game with action-driven mechanics**](community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md) | Action-driven mechanics with physics feedback; playable build included. |
| ⭐ | [**Beats Pokémon FireRed looking only at the screen**](showcase/entries/只看屏幕通关火红.md) | Computer-use boundary case: zero game APIs, 18h12m of pure screen-reading |
| ⭐ | [**Built a game, then played, recorded and edited it**](showcase/entries/我让-gpt-6-astra-做了个游戏然后让它自己玩自己录屏再剪一段开发实录.md) | Build → self-play → self-record → self-edit: a fully automated content pipeline |

---

## 🖼️ Gallery

*All real community output. Click an image for the original X post; "prompt & provenance" carries the author's verbatim prompt. 🌟 = playable in browser.*

<table>
<tr><td align="center" width="33%"><a href="https://x.com/adxtyahq/status/2096236137266512181"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/bbb03f5650350e6b4a323f0dd76f98d1abb0cbe94896f2dbe24d68c4bfbf8ce8.jpg" width="100%" alt="Full Flight-Sim Loop"/></a><br/><b>Full Flight-Sim Loop</b> · take off → fly → land → score<br/><a href="community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/HiltonMisia/status/2096637091627364531"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ad164224745a34f4bcd14af8ec14fe0d7a6cf7203a80ea7544106dd1b76dc8f7.jpg" width="100%" alt="Dark-Fantasy ARPG"/></a><br/><b>Dark-Fantasy ARPG</b> · one prompt, one complete action RPG<br/><a href="community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/tripoai/status/2096629506047955327"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e3304eeb4bf4186f9a57768af5e1962741c3dce44ed5aace2aef04585d0e69ca.jpg" width="100%" alt="Windhaven Adventure"/></a><br/><b>Windhaven Adventure</b> · long-narrative prompt showcase<br/><a href="community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md">📜 prompt &amp; provenance</a></td></tr>
<tr><td align="center" width="33%"><a href="https://x.com/EngMoElgaraihy/status/2096438110095585753"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e14b00869191181ad52fe51c4e0a57d3ad72c405802c16cb36147a9b5d613143.jpg" width="100%" alt="LEGO Racers Remaster"/></a><br/><b>LEGO Racers Remaster</b> · 1999 classic, rebuilt in 3D<br/><a href="community-posts/2096438110095585753-rebuilding-lego-1999-racers.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/majidmanzarpour/status/2096251574918013135"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8f55d646820e4f1f0b98d00cdc85125c79f19093abe73bc0cecdfbf2e2365e50.webp" width="100%" alt="Kaiju City Battle"/></a><br/><b>Kaiju City Battle</b> · live battle · playable 🌟<br/><a href="community-posts/2096251574918013135-kaiju-city-battle.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/zeuuss_01/status/2096337879173591171"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b357895cffa990ebc6d5404e59b1f2371a45536a5cabca80b976c590192d8338.webp" width="100%" alt="Beach Crab Action Game"/></a><br/><b>Beach Crab Action Game</b> · physics-driven · playable 🌟<br/><a href="community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md">📜 prompt &amp; provenance</a></td></tr>
</table>

**[→ All 21 games](#-games-21) · [→ 3D worlds](#️-3d-worlds--modeling) · [→ Videos](#-prompt-to-video) · [→ Playable worlds](#-playable-worlds--try-in-browser)**

---

## 🎮 Games (21)

| Preview | Case | Author | Play |
|---|---|---|---|
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b357895cffa990ebc6d5404e59b1f2371a45536a5cabca80b976c590192d8338.webp" width="150"/> | [A crab game with action-driven mechanics](community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md) 🌟 | [@zeuuss_01](https://x.com/zeuuss_01) | [▶ play](https://beach-crab-game.netlify.app/) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8f55d646820e4f1f0b98d00cdc85125c79f19093abe73bc0cecdfbf2e2365e50.webp" width="150"/> | [Kaiju city battle](community-posts/2096251574918013135-kaiju-city-battle.md) 🌟 | [@majidmanzarpour](https://x.com/majidmanzarpour) | [▶ play](https://stormcolossus.netlify.app/) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/bbb03f5650350e6b4a323f0dd76f98d1abb0cbe94896f2dbe24d68c4bfbf8ce8.jpg" width="150"/> | [Browser Flight Simulator with a Complete Flight Loop](community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md) | [@adxtyahq](https://x.com/adxtyahq) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/2b020e0fc8275195843fe93dfea7923e440940671c21060866aa6fd429e471e9.webp" width="150"/> | [Browser city game with a supplied character](community-posts/2096398839830008292-browser-city-game-with-a-supplied-character.md) | [@djrio_vr](https://x.com/djrio_vr) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b00b0f3011c9f77412b6212bff0efb0fc453cefca3af7186267fabb90c0536f0.webp" width="150"/> | [Complete Three.js puzzle level](community-posts/2096505740643246231-complete-three-js-puzzle-level.md) | [@TvWoo](https://x.com/TvWoo) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/9188a5a53301b71d404af1d10d6baf4e44585869cc933918118ae2180cf3c1ab.jpg" width="150"/> | [Interactive Robot Pet on a Workbench](community-posts/2097004192627933279-interactive-robot-pet-on-a-workbench.md) | [@zeuuss_01](https://x.com/zeuuss_01) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/177462bb87e3089acbf23e2e6f58e75e4fa5cb7291601fdce6da2a3fb5f2b6af.webp" width="150"/> | [Komorebi river kayaking](community-posts/2096244208533455049-komorebi-river-kayaking.md) | [@ItsmeAjayKV](https://x.com/ItsmeAjayKV) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/2b65a179759aadacaa8dcf78ecfd45f3e7dcd04b4d1f535bc553c3d9f7505f2d.jpg" width="150"/> | [LEGO Minifig Game Asset with Blender MCP](community-posts/2096766465730847059-lego-minifig-game-asset-with-blender-mcp.md) | [@_simonsmith](https://x.com/_simonsmith) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/30b921728503d9086c9f52adbcc90a3fa3dc568cb7e85903172fc1c5295cb279.jpg" width="150"/> | [Mini World 3D exploration game](community-posts/2096641728497275011-mini-world-3d-exploration-game.md) | [@weijianzhang_](https://x.com/weijianzhang_) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/eceebf1bdd5561e25fada5daec055473bd5506cf272760a5a08a8b4ad111988c.webp" width="150"/> | [Mobile-playable Unity rally game](community-posts/2096556692842348826-mobile-playable-unity-rally-game.md) | [@kevinkern](https://x.com/kevinkern) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/756d0d4859c6a3bec065b9594d7fed7544101b6f6b6fb1e331bbfee059e84738.jpg" width="150"/> | [Photorealistic Editable Dragon Reconstruction in Blender](community-posts/2096335588727349434-photorealistic-editable-dragon-reconstruction-in-blender.md) | [@doomdave](https://x.com/doomdave) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/a50398d5761279d4c67fa425f175dd71bdd68472435b1df9f4c8e703c7edb035.jpg" width="150"/> | [Playroom: Retro 3D Browser Arcade](community-posts/2097339176094195899-playroom-retro-3d-browser-arcade.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/66b6fe9a782625a1d13bf79872857593fecf604421e40eb8cfd67c212ad0b695.webp" width="150"/> | [Railway network simulation game](community-posts/2096362653480562751-railway-network-simulation-game.md) | [@tomkrcha](https://x.com/tomkrcha) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e14b00869191181ad52fe51c4e0a57d3ad72c405802c16cb36147a9b5d613143.jpg" width="150"/> | [Rebuilding Lego 1999 Racers](community-posts/2096438110095585753-rebuilding-lego-1999-racers.md) | [@EngMoElgaraihy](https://x.com/EngMoElgaraihy) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/36b98467e6157525383fbc35526f9c07f2cadf9f16b1559da917bb3cc5fc4eca.jpg" width="150"/> | [Recreate League of Legends as a Web Game](community-posts/2097336230078013598-recreate-league-of-legends-as-a-web-game.md) | [@liyue_ai](https://x.com/liyue_ai) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/36b98467e6157525383fbc35526f9c07f2cadf9f16b1559da917bb3cc5fc4eca.jpg" width="150"/> | [Recreate a Mini 3D Game Inspired by League of Legends](community-posts/2097320830602809682-recreate-a-mini-3d-game-inspired-by-league-of-legends.md) | [@LufzzLiz](https://x.com/LufzzLiz) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/0ba729978213ae4955dbc48dc1842a22c3ccfe72d686a037cf599fba60a214dd.webp" width="150"/> | [The Quiet Crossing exploration quest](community-posts/2096574297703637111-the-quiet-crossing-exploration-quest.md) | [@Motion_Viz](https://x.com/Motion_Viz) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ad164224745a34f4bcd14af8ec14fe0d7a6cf7203a80ea7544106dd1b76dc8f7.jpg" width="150"/> | [Three.js dark-fantasy action RPG](community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md) | [@HiltonMisia](https://x.com/HiltonMisia) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/9467608cd8acae08c8272517d7c6605284f8073c38eefd78221597d07dfe93db.webp" width="150"/> | [Trading-card battle game loop](community-posts/2096555856204644550-trading-card-battle-game-loop.md) | [@FaryaBlender3D](https://x.com/FaryaBlender3D) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e3304eeb4bf4186f9a57768af5e1962741c3dce44ed5aace2aef04585d0e69ca.jpg" width="150"/> | [Windhaven Coastal Fantasy Adventure Game](community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/67349df6f55e75c5acee30371c715c3ec04b9ae5c26c628e71d3afb3aae6c9e0.webp" width="150"/> | [Wright Flyer through a Japanese forest](community-posts/2096467585785286808-wright-flyer-through-a-japanese-forest.md) | [@thebuggeddev](https://x.com/thebuggeddev) | — |

---

## 🧱 3D Worlds & Modeling

*Blender ×36 · Three.js ×33 · voxels, shaders, WebGPU, Unreal, Unity.*

<details>
<summary><b>🖼️ Browse 3D cases (31 thumbnails)</b></summary>

| Preview | Case | Author |
|---|---|---|
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ea082ba0b96ce2048a717565f743d1448c4bef031ad0585dcdb75aced928fad8.jpg" width="130"/> | [3D render of an X picture](community-posts/2096338836854804782-3d-render-of-an-x-picture.md) | [@MattJamesBoyle](https://x.com/MattJamesBoyle) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3e060bfb3bf3973f0efb048cacbdc625fe879b8bca0cb46c2bb8fd367eb75268.jpg" width="130"/> | [A 12-Second Forest Road in Blender](community-posts/2096986557244723371-a-12-second-forest-road-in-blender.md) | [@Jomolos](https://x.com/Jomolos) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3dac0cf4428bc4a32bd1418c62a971bc75be632f3e10e918ba9b45800f364ba2.webp" width="130"/> | [A house modeled from scratch in Blender](community-posts/2096576154337734865-a-house-modeled-from-scratch-in-blender.md) | [@mizkun](https://x.com/mizkun) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/76eeeaa8710b4767fb99c09689e3a0b87ba770495f026e34ea34cb2b5f1f76fc.webp" width="130"/> | [Apartment sketch to rendered interiors](community-posts/2096566686266597754-apartment-sketch-to-rendered-interiors.md) | [@WorldEverett](https://x.com/WorldEverett) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3388e9e5e8f519fb22f67c35c98f5038335da857c0a1b8883c406c6e14c36c4a.webp" width="130"/> | [Assemble and animate generated 3D assets](community-posts/2096481425050743048-assemble-and-animate-generated-3d-assets.md) | [@Stefan_3D_AI](https://x.com/Stefan_3D_AI) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/721eed98f68b8ad4264b4fbd922b185c7e6501834c9aa828a0b3b369fba5ff28.jpg" width="130"/> | [Backrooms-inspired Blender VHS scene](community-posts/2097534290112188602-backrooms-inspired-blender-vhs-scene.md) | [@chrisfirst](https://x.com/chrisfirst) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/d13ca069743cb65e0501484737d96a1fbde81927026e9b8837b149ece9b0693d.webp" width="130"/> | [Blender models with Unity VFX](community-posts/2096560142871658589-blender-models-with-unity-vfx.md) | [@CST_negi](https://x.com/CST_negi) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b6d2405bd8f8e5cd9543cde67c0c3719a2e7b5ac38c080cca7336d0f7c1ec1d1.jpg" width="130"/> | [Building a Comedy Scene of a Robotic Arm Chasing a Cat with GPT-6 Astra and Blender](community-posts/2097675660873605422-building-a-comedy-scene-of-a-robotic-arm-chasing-a-cat-with.md) | [@TanLuAI](https://x.com/TanLuAI) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/1712c53120622f0ba430f5985562bd6eb307621c1a4466ef9d2cf26c99b81716.jpg" width="130"/> | [Character Concept to Rigged 3D Model and Cartoon](community-posts/2096342420543660277-character-concept-to-rigged-3d-model-and-cartoon.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/0203a375c4a0f77f1fae00d9c8c9173739b940debd87bf4144d4f375ccc8c12e.jpg" width="130"/> | [Create and render a black hole in Blender](community-posts/2096391653669953761-create-and-render-a-black-hole-in-blender.md) | [@JohnKlerAI](https://x.com/JohnKlerAI) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/a8ee5a495643a02333b8f904a4d46c26f8211b6ba6ecb40ba3b2521387e81571.jpg" width="130"/> | [Edit a Blender scene for knurled posts and PCB fit](community-posts/2096990373813858591-edit-a-blender-scene-for-knurled-posts-and-pcb-fit.md) | [@rboyd](https://x.com/rboyd) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/aed224d4a25ce9c0d436ebd4d2bfb7fadb211bdf624364e3f7905a0dbec1546f.jpg" width="130"/> | [Folding Carton Animation from a Dieline](community-posts/2096612394281603144-folding-carton-animation-from-a-dieline.md) | [@Salmaaboukarr](https://x.com/Salmaaboukarr) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/bffeb201cd39ed86178dd22e30bda1ea70e4ff92902307d88ba66700e21dcd32.jpg" width="130"/> | [Hogwarts 3D scene](community-posts/2096907617117540478-hogwarts-3d-scene.md) | [@HiltonMisia](https://x.com/HiltonMisia) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8528f6aaa8b6070a8c1e3732f0791feac42ed1ba7d0c23cc85c7c9e0212600a1.png" width="130"/> | [Improve a 3D Model’s Facial Features in Blender Using a Reference Image](community-posts/2097313247116341424-improve-a-3d-models-facial-features-in-blender-using-a-refer.md) | [@carlos_olivera](https://x.com/carlos_olivera) |

*…and 17 more in [showcase/entries/](showcase/README.md).*

</details>

---

## 🎬 Prompt-to-Video

| Case | Author | Preview |
|---|---|---|
| [Witch's First Flight — 15s Generated Shot Script](community-posts/2095873015007592679-witch-s-first-flight-15s-generated-shot-script.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/witch-first-flight.webp" width="130"/> |
| [AdCar TV — In-Repo One-Shot Launch Video](community-posts/2096258259459964963-adcar-tv-in-repo-one-shot-launch-video.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/adcar-tv.webp" width="130"/> |
| [T Cells — One Sentence, Five Minutes](community-posts/2095659170661904804-t-cells-one-sentence-five-minutes.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/t-cells.webp" width="130"/> |
| [High-Speed Parkour Motion Previz](community-posts/2096096560690209130-high-speed-parkour-motion-previz.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/parkour-previz.webp" width="130"/> |

> Full video-prompt methodology (Remotion, HyperFrames, shot scripts): [LuxRealGrowth/awesome-astra-video-prompts](https://github.com/LuxRealGrowth/awesome-astra-video-prompts).

---

## 🕸️ Web & Interactive

| Case | Author | Preview |
|---|---|---|
| [Endless Miniature Street in Three.js WebGPU](community-posts/2096956214680965501-endless-miniature-street-in-three-js-webgpu.md) | [@creativedash](https://x.com/creativedash) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/c2aa4cd5daf5e1bc8f71051db13c08e7f52359b5a5aaf7b813b72d474117897e.jpg" width="130"/> |
| [Create an Interactive Soft-Body Slime with Three.js and WebGPU](community-posts/2096793432987464010-create-an-interactive-soft-body-slime-with-three-js-and-webg.md) | [@Delroy715](https://x.com/Delroy715) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/080a768b7958082811553a4d1a4c865caeee6e542e68fe0ba9e32ed478233342.jpg" width="130"/> |
| [Interactive jelly lemon tree](community-posts/2097065330728128920-interactive-jelly-lemon-tree.md) | [@vib3coded](https://x.com/vib3coded) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/19fa5b36caaf4663987e99892e3cb3babcc452cbe50e1ef2f6108a859d3eba36.jpg" width="130"/> |

---

## 🌍 Playable Worlds — try in browser

*Ten one-prompt builds you can open right now. No install, no build step.*

| World | Creator | Open |
|---|---|---|
| [Surface-climbing procedural insect](community-posts/2096460081982304546-surface-climbing-procedural-insect.md) | [@leo_xiaolei](https://x.com/leo_xiaolei) | [▶ open world](https://threerocks.github.io/web-3d-pages/) |
| [Cluj-Napoca Union Square in voxels](community-posts/2096262733259837681-cluj-napoca-union-square-in-voxels.md) | [@danmana](https://x.com/danmana) | [▶ open world](https://piata-unirii.vercel.app/runs/gpt-astra-xhigh-01/) |
| [Interactive Lorenz attractor](community-posts/2096572156453028193-interactive-lorenz-attractor.md) | [@juyeam](https://x.com/juyeam) | [▶ open world](https://tiny-worlds-juyeam.juyeam.chatgpt.site/chaos) |
| [Interactive miniature of Seoul](community-posts/2096557555086725159-interactive-miniature-of-seoul.md) | [@synabreu](https://x.com/synabreu) | [▶ open world](https://seoul-3d-atlas.synabreu.chatgpt.site/) |
| [Totality Engine: Cinematic Eclipse Cathedral](community-posts/2096593372311941143-totality-engine-cinematic-eclipse-cathedral.md) | [@Chris_Wozniczek](https://x.com/Chris_Wozniczek) | [▶ open world](https://chris-website-theta.vercel.app/astra-xhigh-totality-engine.html) |
| [Personal room as an interactive portfolio](community-posts/2096506357868642342-personal-room-as-an-interactive-portfolio.md) | [@kalanyei](https://x.com/kalanyei) | [▶ open world](https://room.kalan.dev/) |
| [Interactive dual-ring energy core](community-posts/2096551010089263181-interactive-dual-ring-energy-core.md) | [@oneruofeng](https://x.com/oneruofeng) | [▶ open world](https://orbital-core-showcase.wangruofeng007.workers.dev/) |
| [One Piece-inspired sailing world](community-posts/2096518775042707700-one-piece-inspired-sailing-world.md) | [@yash_yk45](https://x.com/yash_yk45) | [▶ open world](https://one-piece-sea-world.vercel.app/) |

---

## 🧪 Reproducible Recipes (26)

*Cases prove it can happen once. Recipes make it happen again — every recipe pins four things:*

| Clause | What's pinned |
|---|---|
| **Model** | `gpt-6-astra`, version pinned to the exact release date (2026-09-03) |
| **Settings** | temperature / top_p / seed / max_output_tokens — all recorded |
| **Input** | runtime, dependencies, starting files, assets — everything needed before the prompt runs |
| **Acceptance** | expected artifacts + a pass/fail checklist + "Where it drifts" failure modes |

<details>
<summary><b>📋 Full index — 26 recipes in 5 categories</b></summary>

<!-- BEGIN INDEX -->
> **26** prompts · 5 categories · targeting `gpt-6-astra` (2026-09-03).

The initial batch ships as **📝 draft** — format-complete and reviewed, but not yet independently reproduced. Run one and record it to promote it to 🧪 community.

### 🎮 Full games — one prompt, a playable game

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-001` | [Endless Runner](prompts/full-games/astra-3d-001-endless-runner.md) | Three.js | beginner | 📝 draft |
| `astra-3d-002` | [First-Person Explorer](prompts/full-games/astra-3d-002-first-person-explorer.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-003` | [Tower Defense](prompts/full-games/astra-3d-003-tower-defense.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-004` | [Top-Down Arena Shooter](prompts/full-games/astra-3d-004-topdown-arena-shooter.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-005` | [Voxel Sandbox](prompts/full-games/astra-3d-005-voxel-sandbox.md) | Three.js | advanced | 📝 draft |
| `astra-3d-006` | [Physics Marble Platformer](prompts/full-games/astra-3d-006-marble-platformer.md) | Three.js + Rapier | advanced | 📝 draft |

### ⚙️ Systems — drop-in gameplay machinery

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-101` | [Character Controller](prompts/systems/astra-3d-101-character-controller.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-102` | [Seeded Procedural Terrain](prompts/systems/astra-3d-102-procedural-terrain.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-103` | [Enemy AI State Machine](prompts/systems/astra-3d-103-enemy-fsm-ai.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-104` | [Inventory & Pickups](prompts/systems/astra-3d-104-inventory-and-pickups.md) | Three.js | beginner | 📝 draft |
| `astra-3d-105` | [Third-Person Camera Rig](prompts/systems/astra-3d-105-third-person-camera.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-106` | [Save / Load System](prompts/systems/astra-3d-106-save-load-system.md) | Three.js | beginner | 📝 draft |
| `astra-3d-107` | [Object Pooling & Culling](prompts/systems/astra-3d-107-object-pooling.md) | Three.js | advanced | 📝 draft |
| `astra-3d-108` | [Deterministic Replay Harness](prompts/systems/astra-3d-108-deterministic-replay.md) | Three.js | advanced | 📝 draft |

### 🧱 Assets — geometry, rigs and textures as code

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-201` | [Text → Low-Poly Prop (GLB)](prompts/assets/astra-3d-201-text-to-3d-prop.md) | Blender 4.x | intermediate | 📝 draft |
| `astra-3d-202` | [Procedural PBR Texture Set](prompts/assets/astra-3d-202-pbr-texture-set.md) | Canvas / WebGL | intermediate | 📝 draft |
| `astra-3d-203` | [Rigged Character from a Prompt](prompts/assets/astra-3d-203-rigged-character.md) | Blender 4.x | advanced | 📝 draft |
| `astra-3d-204` | [Modular Kit-Bash Set](prompts/assets/astra-3d-204-modular-kitbash.md) | Blender 4.x | intermediate | 📝 draft |
| `astra-3d-205` | [Texture Atlas Packer](prompts/assets/astra-3d-205-texture-atlas.md) | Node / Sharp | beginner | 📝 draft |

### 🗺️ Levels & worlds

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-301` | [Seeded Procedural Dungeon](prompts/levels/astra-3d-301-procedural-dungeon.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-302` | [Procedural City Block](prompts/levels/astra-3d-302-procedural-city.md) | Three.js | advanced | 📝 draft |
| `astra-3d-303` | [Navmesh from Level Geometry](prompts/levels/astra-3d-303-navmesh-baker.md) | Three.js | advanced | 📝 draft |
| `astra-3d-304` | [Wave / Spawn Director](prompts/levels/astra-3d-304-spawn-director.md) | Three.js | intermediate | 📝 draft |

### 🖥️ UI & HUD

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-401` | [HUD, Menus & Pause Screen](prompts/ui/astra-3d-401-hud-and-menus.md) | HTML / CSS | beginner | 📝 draft |
| `astra-3d-402` | [Radial & Context Menu System](prompts/ui/astra-3d-402-radial-menu.md) | HTML / CSS | intermediate | 📝 draft |
| `astra-3d-403` | [Settings & Accessibility Panel](prompts/ui/astra-3d-403-settings-panel.md) | HTML / CSS | beginner | 📝 draft |
<!-- END INDEX -->

</details>

> **Cases vs. recipes:** the case layers (`community-posts/`, `showcase/`) promise *this really happened* — they never claim reproducibility. The recipe layer (`prompts/`) promises *you can reproduce this* — all four clauses or it doesn't get in. Entries cross-reference each other.

---

## 📖 Playbooks

*A recipe shows what a prompt looks like. A playbook shows how to assemble one for **your** idea — six patterns distilled from 103 cases, each with a paste-ready template, a variable table, and known failure modes.*

| | Playbook | One-liner | Difficulty |
|---|---|---|---|
| 🎈 | **[One-Shot Arcade](playbooks/p1-one-shot-arcade.md)** | One prompt → one self-contained arcade game ([real case: Mosswing](https://mosswing-quiet-flight.jack-514.chatgpt.site/), built in 21 min) | ★ |
| 🏗️ | **[Spec-First Big Build](playbooks/p2-spec-first-big-build.md)** | Make the model write `SPEC.md` first, then build against it — how large projects stay on rails | ★★ |
| 🕹️ | **[Remaster Classic](playbooks/p3-remaster-classic.md)** | Remake an old game: nostalgia recognition × modern game-feel | ★★ |
| 🤖 | **[Computer-Use Player](playbooks/p4-computer-use-player.md)** | Give the model hands — it plays the game itself | ★★★ |
| 🧪 | **[Playable World Diorama](playbooks/p5-playable-world-diorama.md)** | Any place → explorable 3D miniature | ★★ |
| 🎨 | **[Co-Creative Design Partner](playbooks/p6-co-creative-design.md)** | Let the model be the game designer first, coder second | ★ |

**Companion skill:** [`skills/astra-playbook`](skills/astra-playbook/SKILL.md) — routes a one-line idea to the right output form, fills an eight-block prompt frame, attaches acceptance checks.

### The pattern behind every playbook

Community prompts that reproduce share a contract, and it is worth internalizing once:

1. **Grant autonomy explicitly** — *"I won't answer clarifying questions. Judge the result yourself."*
2. **Name the deliverable exactly** — *one `index.html`, opens by double-click, no build step.*
3. **Set the judging bar** — *"complete and finished beats big and rough; I'm grading game-feel, not a feature list."*
4. **Bound thepermissions** — write only in the project folder, no sudo, list dependencies before installing.
5. **Demand honesty about uncertainty** — *"if a detail can't be verified, mark it estimated — don't invent it."*

---

## 🌐 Browse the ecosystem

| Resource | What's inside |
|---|---|
| **[site/index.html](site/index.html)** | Browsable web viewer (catalog-driven) |
| **[CATALOG.md](CATALOG.md)** | 28 ecosystem entries — games / 3D / web / video / apps / agents / engineering / research — tiered ⭐ featured / ✦ notable / · community |
| **[showcase/README.md](showcase/README.md)** | The 103-case data layer with categories and editors' picks ([data.json](showcase/data.json)) |
| **[community-posts/](community-posts)** | All 103 posts: frontmatter (author, X URL, media, license) + verbatim prompt + provenance |

---

## 🤝 Contribute

| Way | Value | How |
|---|---|---|
| 🖼️ **Submit a case** | Surface new play patterns | PR into `community-posts/` — one post per file, frontmatter template in [CONTRIBUTING](CONTRIBUTING.md) |
| 🧪 **Reproduce a recipe** | Promotes 📝 draft → 🧪 community — **the most valuable contribution right now** | Run any recipe, log the run in its Provenance |
| ⭐ **Add a recipe** | Grow the reproducible library | Start from the [template](templates/PROMPT_TEMPLATE.md), honor the [contract](docs/REPRODUCIBILITY.md), CI must pass |
| 🐛 **Report drift** | Keep recipes honest when the model updates | Open a [drift issue](.github/ISSUE_TEMPLATE/prompt-drift.yml) with the new model version |

---

<div align="center">

**Snapshot 2026-09-11** · X posts are the record of truth; awesome-lists are aggregation channels only ·
All work © its original creators, credited per entry · Unofficial community project, not affiliated with or endorsed by OpenAI

[CC0-1.0](LICENSE) · Made with 🕹️ by the community

</div>
