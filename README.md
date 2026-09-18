<div align="center">

# 🕹️ Awesome GPT-6 Astra · Game Prompts

### One prompt. One playable 3D game.

**26 reproducible recipes · 306 real community cases (307 with previews) · 6 playbooks · 206+ creators credited**

[🚀 Start here](#-start-here) · [🏆 Featured](#-featured--worth-studying) · [🖼️ Gallery](#️-gallery) · [🎮 Games](#-games-21) · [🧪 Recipes](#-reproducible-recipes--26) · [📖 Playbooks](#-playbooks) · [🌐 Web viewer](site/index.html)

[![validate](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml)
[![license: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![model: gpt-6-astra](https://img.shields.io/badge/model-gpt--6--astra-6f42c1.svg)](https://platform.openai.com/docs/models)

</div>

---

**Go to:** [Featured](#-featured--worth-studying) · [Gallery](#️-gallery) ·
[Games](#-games-38) · [3D Worlds](#-3d-worlds--modeling-59) · [Videos](#-prompt-to-video-4) ·
[Web](#️-web--interactive-3) · [More](#-more-creations-104) · [Playable Worlds](#-playable-worlds--try-in-browser) ·
[Recipes](#-reproducible-recipes--26) · [Playbooks](#-playbooks) ·
[Learning path](#-learning-path--from-viral-moment-to-your-own-build) · [FAQ](#-faq)

**GPT-6 Astra** (OpenAI, released 2026-09-03) made *"describe a game, get a playable build"* real. Within its first week the community produced hundreds of working games, worlds and films from single prompts — most published on X with the prompt in the post or the replies. This repo is the organized version of that week:

| Layer | What it gives you | Where |
|---|---|---|
| 🖼️ **Cases** | See what others made — real previews, X provenance, verbatim prompts | `community-posts/` · `showcase/` |
| 🧪 **Recipes** | Reproduce it yourself — pinned model version, settings, inputs, acceptance checks | `prompts/` |
| 📖 **Methods** | Turn *your* idea into a working prompt — reusable play patterns | `playbooks/` · `skills/` |

**Sourcing rule:** X is the record of truth. Every case links back to its original post; prompts are only ever collected from the post itself or its replies. Aggregated from 10 community awesome-lists, deduplicated by post URL, every entry credited. Snapshot: 2026-09-17.

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
<tr><td align="center" width="33%"><a href="https://x.com/adxtyahq/status/2096236137266512181"><img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/bbb03f5650350e6b4a323f0dd76f98d1abb0cbe94896f2dbe24d68c4bfbf8ce8.jpg" width="100%" alt="Full Flight-Sim Loop"/></a><br/><b>Full Flight-Sim Loop</b> · take off → fly → land → score<br/><a href="community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/HiltonMisia/status/2096637091627364531"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ad164224745a34f4bcd14af8ec14fe0d7a6cf7203a80ea7544106dd1b76dc8f7.jpg" width="100%" alt="Dark-Fantasy ARPG"/></a><br/><b>Dark-Fantasy ARPG</b> · one prompt, one complete action RPG<br/><a href="community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/tripoai/status/2096629506047955327"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e3304eeb4bf4186f9a57768af5e1962741c3dce44ed5aace2aef04585d0e69ca.jpg" width="100%" alt="Windhaven Adventure"/></a><br/><b>Windhaven Adventure</b> · long-narrative prompt showcase<br/><a href="community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md">📜 prompt &amp; provenance</a></td></tr>
<tr><td align="center" width="33%"><a href="https://x.com/EngMoElgaraihy/status/2096438110095585753"><img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/e14b00869191181ad52fe51c4e0a57d3ad72c405802c16cb36147a9b5d613143.jpg" width="100%" alt="LEGO Racers Remaster"/></a><br/><b>LEGO Racers Remaster</b> · 1999 classic, rebuilt in 3D<br/><a href="community-posts/2096438110095585753-rebuilding-lego-1999-racers.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/majidmanzarpour/status/2096251574918013135"><img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/8f55d646820e4f1f0b98d00cdc85125c79f19093abe73bc0cecdfbf2e2365e50.webp" width="100%" alt="Kaiju City Battle"/></a><br/><b>Kaiju City Battle</b> · live battle · playable 🌟<br/><a href="community-posts/2096251574918013135-kaiju-city-battle.md">📜 prompt &amp; provenance</a></td><td align="center" width="33%"><a href="https://x.com/zeuuss_01/status/2096337879173591171"><img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/b357895cffa990ebc6d5404e59b1f2371a45536a5cabca80b976c590192d8338.webp" width="100%" alt="Beach Crab Action Game"/></a><br/><b>Beach Crab Action Game</b> · physics-driven · playable 🌟<br/><a href="community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md">📜 prompt &amp; provenance</a></td></tr>
</table>

**[→ All 21 games](#-games-21) · [→ 3D worlds](#️-3d-worlds--modeling) · [→ Videos](#-prompt-to-video) · [→ Playable worlds](#-playable-worlds--try-in-browser)**

---

## 🎮 Games ()

| Preview | Case | Author | Play |
|---|---|---|---|
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/70b44657a0a3c5d782e2efb4.webp" width="150"/> | [A crab game with action-driven mechanics](community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md) 🌟 | [@zeuuss_01](https://x.com/zeuuss_01) | [▶ play](https://beach-crab-game.netlify.app/) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/8f55d646820e4f1f0b98d00cdc85125c79f19093abe73bc0cecdfbf2e2365e50.webp" width="150"/> | [Kaiju city battle](community-posts/2096251574918013135-kaiju-city-battle.md) 🌟 | [@majidmanzarpour](https://x.com/majidmanzarpour) | [▶ play](https://stormcolossus.netlify.app/) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/5f9d00fa8df2ee60ff67bb08.jpg" width="150"/> | [A Godot Roguelike Level](community-posts/2096494840431386950-a-godot-roguelike-level.md) | [@op7418](https://x.com/op7418) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/9c5eb5837d58826d7b9853df.webp" width="150"/> | [ASTRA WRITES THE GAME. HIGGSFIELD DRESSES IT. YOU JUST PLA](community-posts/2096937327645929938-astra-writes-the-game-higgsfield-dresses-it-you-just-play.md) | [@rimtoln](https://x.com/rimtoln) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/0b9840db698fe043ee094cd0.jpg" width="150"/> | [Anti-Gravity Combat Racer](community-posts/2095967568825582044-anti-gravity-combat-racer.md) | [@superalesha](https://x.com/superalesha) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/899da72afc28d785b886e899.jpg" width="150"/> | [Arena Zero iPhone Fighting Game](community-posts/2097470354897740109-arena-zero-iphone-fighting-game.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/45e895ac5f265217d1138e79.jpg" width="150"/> | [Browser 3D Game Prototype](community-posts/2095599934766764338-browser-3d-game-prototype.md) | [@theo](https://x.com/theo) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/bbb03f5650350e6b4a323f0dd76f98d1abb0cbe94896f2dbe24d68c4bfbf8ce8.jpg" width="150"/> | [Browser Flight Simulator with a Complete Flight Loop](community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md) | [@adxtyahq](https://x.com/adxtyahq) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/2b020e0fc8275195843fe93dfea7923e440940671c21060866aa6fd429e471e9.webp" width="150"/> | [Browser city game with a supplied character](community-posts/2096398839830008292-browser-city-game-with-a-supplied-character.md) | [@djrio_vr](https://x.com/djrio_vr) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/1b0a0e0d771ec99d49118ede.jpg" width="150"/> | [Build a 3D racer](community-posts/2098749876620415165-build-a-3d-racer.md) | [@JulianGoldieSEO](https://x.com/JulianGoldieSEO) | — |
| <img src="https://media.beatapi.io/prompt-gallery/gpt-6-astra-3d/build-a-finished-polished-kart-racer-in-roblox-studio-via-roblox-mcp-331665/poster-d1c280380f15.webp" width="150"/> | [Build a finished, polished kart racer in Roblox Studio via](community-posts/2096219700879331665-build-a-finished-polished-kart-racer-in-roblox-studio-via-ro.md) | [@givros](https://x.com/givros) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/d52c089f5972d0a383f9ac10.jpg" width="150"/> | [Catan-Style Three.js Board Game](community-posts/2097291240672993773-catan-style-threejs-board-game.md) | [@MengTo](https://x.com/MengTo) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/7e9044729ae7ad9173285a0c.webp" width="150"/> | [Complete Three.js puzzle level](community-posts/2096505740643246231-complete-three-js-puzzle-level.md) | [@TvWoo](https://x.com/TvWoo) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/21904f58bcbe320a86b7881bbcbba52e5e94243b88f3860ec995769456b5f505.jpg" width="150"/> | [Create an Animated 3D Environment and Game Character from ](community-posts/2099850721646784894-create-an-animated-3d-environment-and-game-character-from-re.md) | [@aiehon_aya](https://x.com/aiehon_aya) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/34aee4eb542310f21c27d1ed.jpg" width="150"/> | [DEVICE: A Photorealistic 3D Puzzle Game That Uses the Smar](community-posts/2098715488369152087-device-a-photorealistic-3d-puzzle-game-that-uses-the-smartph.md) | [@00Nekonet](https://x.com/00Nekonet) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/03a76db9ff42fea9b4e045fe.jpg" width="150"/> | [Fighting Game Animation Test](community-posts/2097446904942780699-fighting-game-animation-test.md) | [@YuK1_Game](https://x.com/YuK1_Game) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/984b38b94a2fa412e680bc69.jpg" width="150"/> | [From Game to Trailer](community-posts/2096213835460084184-from-game-to-trailer.md) | [@MengTo](https://x.com/MengTo) | — |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2095597293734895622/img/5NhZlESAfUkJTy4C.jpg" width="150"/> | [Halo-Inspired Tesana FPS](community-posts/2095598026916049024-halo-inspired-tesana-fps.md) | [@VikiingAI](https://x.com/VikiingAI) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/02156c8d65cef573167a1718.jpg" width="150"/> | [Interactive Robot Pet on a Workbench](community-posts/2097004192627933279-interactive-robot-pet-on-a-workbench.md) | [@zeuuss_01](https://x.com/zeuuss_01) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/177462bb87e3089acbf23e2e6f58e75e4fa5cb7291601fdce6da2a3fb5f2b6af.webp" width="150"/> | [Komorebi river kayaking](community-posts/2096244208533455049-komorebi-river-kayaking.md) | [@ItsmeAjayKV](https://x.com/ItsmeAjayKV) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/f4380ec584040f8724bf2fd1.jpg" width="150"/> | [LEGO Minifig Game Asset with Blender MCP](community-posts/2096766465730847059-lego-minifig-game-asset-with-blender-mcp.md) | [@_simonsmith](https://x.com/_simonsmith) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/e9ce5d7cce591b1f1f595788.jpg" width="150"/> | [Mini World 3D exploration game](community-posts/2096641728497275011-mini-world-3d-exploration-game.md) | [@weijianzhang_](https://x.com/weijianzhang_) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/44750d3bd7f52b50be85c4ae.webp" width="150"/> | [Mobile-playable Unity rally game](community-posts/2096556692842348826-mobile-playable-unity-rally-game.md) | [@kevinkern](https://x.com/kevinkern) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/756d0d4859c6a3bec065b9594d7fed7544101b6f6b6fb1e331bbfee059e84738.jpg" width="150"/> | [Photorealistic Editable Dragon Reconstruction in Blender](community-posts/2096335588727349434-photorealistic-editable-dragon-reconstruction-in-blender.md) | [@doomdave](https://x.com/doomdave) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/87bdfaa39a38fdfb7b63bde1e513fb3958b3e57885066c2c715852966b94ff03.jpg" width="150"/> | [Playable 3D Obstacle Course](community-posts/2099419671481249851-playable-3d-obstacle-course.md) | [@heyDhavall](https://x.com/heyDhavall) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/f7beaa2f75393d632176cc10919ee4221cbba7b354677e202925812162b1e0e2.jpg" width="150"/> | [Playable 3D browser shore-district slice](community-posts/2099172061092381027-playable-3d-browser-shore-district-slice.md) | [@Lummox_eth](https://x.com/Lummox_eth) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/a50398d5761279d4c67fa425f175dd71bdd68472435b1df9f4c8e703c7edb035.jpg" width="150"/> | [Playroom: Retro 3D Browser Arcade](community-posts/2097339176094195899-playroom-retro-3d-browser-arcade.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/967dfc7a1c658ef0de5a7eb3.webp" width="150"/> | [Railway network simulation game](community-posts/2096362653480562751-railway-network-simulation-game.md) | [@tomkrcha](https://x.com/tomkrcha) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/87bc9860646be12ec6795420.jpg" width="150"/> | [Rebuilding Lego 1999 Racers](community-posts/2096438110095585753-rebuilding-lego-1999-racers.md) | [@EngMoElgaraihy](https://x.com/EngMoElgaraihy) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/e8c8c4308f432de79fda78db.jpg" width="150"/> | [Recreate League of Legends as a Web Game](community-posts/2097336230078013598-recreate-league-of-legends-as-a-web-game.md) | [@liyue_ai](https://x.com/liyue_ai) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/e8c8c4308f432de79fda78db.jpg" width="150"/> | [Recreate a Mini 3D Game Inspired by League of Legends](community-posts/2097320830602809682-recreate-a-mini-3d-game-inspired-by-league-of-legends.md) | [@LufzzLiz](https://x.com/LufzzLiz) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/4c50a72b08ad356961bf91c6.jpg" width="150"/> | [Skybound browser flight game](community-posts/2098739181510164652-skybound-browser-flight-game.md) | [@Kanojiyaaakash1](https://x.com/Kanojiyaaakash1) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/09544f1dda48f4288384850cffc3a8d4127273075bba899a6d5691ac2c90d730.jpg" width="150"/> | [The Cyclops’ Island isometric 3D browser game](community-posts/2099414001851449430-the-cyclops-island-isometric-3d-browser-game.md) | [@jasoncjs_](https://x.com/jasoncjs_) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/0fdc6114c0fac5c9aaafcb98.webp" width="150"/> | [The Quiet Crossing exploration quest](community-posts/2096574297703637111-the-quiet-crossing-exploration-quest.md) | [@Motion_Viz](https://x.com/Motion_Viz) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/1f8a0a705ea873d9e8779ff6.jpg" width="150"/> | [Three.js dark-fantasy action RPG](community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md) | [@HiltonMisia](https://x.com/HiltonMisia) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/6eb56538afa56aaa61ffae63.webp" width="150"/> | [Trading-card battle game loop](community-posts/2096555856204644550-trading-card-battle-game-loop.md) | [@FaryaBlender3D](https://x.com/FaryaBlender3D) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/529e5d19ae7a87b6297845b0.jpg" width="150"/> | [Windhaven Coastal Fantasy Adventure Game](community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/6812a5ff5e602b40a1cb6ac8.webp" width="150"/> | [Wright Flyer through a Japanese forest](community-posts/2096467585785286808-wright-flyer-through-a-japanese-forest.md) | [@thebuggeddev](https://x.com/thebuggeddev) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/b357895cffa990ebc6d5404e59b1f2371a45536a5cabca80b976c590192d8338.webp" width="150"/> | [A crab game with action-driven mechanics](community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md) 🌟 | [@zeuuss_01](https://x.com/zeuuss_01) | [▶ play](https://beach-crab-game.netlify.app/) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/8f55d646820e4f1f0b98d00cdc85125c79f19093abe73bc0cecdfbf2e2365e50.webp" width="150"/> | [Kaiju city battle](community-posts/2096251574918013135-kaiju-city-battle.md) 🌟 | [@majidmanzarpour](https://x.com/majidmanzarpour) | [▶ play](https://stormcolossus.netlify.app/) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/bbb03f5650350e6b4a323f0dd76f98d1abb0cbe94896f2dbe24d68c4bfbf8ce8.jpg" width="150"/> | [Browser Flight Simulator with a Complete Flight Loop](community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md) | [@adxtyahq](https://x.com/adxtyahq) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/2b020e0fc8275195843fe93dfea7923e440940671c21060866aa6fd429e471e9.webp" width="150"/> | [Browser city game with a supplied character](community-posts/2096398839830008292-browser-city-game-with-a-supplied-character.md) | [@djrio_vr](https://x.com/djrio_vr) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b00b0f3011c9f77412b6212bff0efb0fc453cefca3af7186267fabb90c0536f0.webp" width="150"/> | [Complete Three.js puzzle level](community-posts/2096505740643246231-complete-three-js-puzzle-level.md) | [@TvWoo](https://x.com/TvWoo) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/9188a5a53301b71d404af1d10d6baf4e44585869cc933918118ae2180cf3c1ab.jpg" width="150"/> | [Interactive Robot Pet on a Workbench](community-posts/2097004192627933279-interactive-robot-pet-on-a-workbench.md) | [@zeuuss_01](https://x.com/zeuuss_01) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/177462bb87e3089acbf23e2e6f58e75e4fa5cb7291601fdce6da2a3fb5f2b6af.webp" width="150"/> | [Komorebi river kayaking](community-posts/2096244208533455049-komorebi-river-kayaking.md) | [@ItsmeAjayKV](https://x.com/ItsmeAjayKV) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/2b65a179759aadacaa8dcf78ecfd45f3e7dcd04b4d1f535bc553c3d9f7505f2d.jpg" width="150"/> | [LEGO Minifig Game Asset with Blender MCP](community-posts/2096766465730847059-lego-minifig-game-asset-with-blender-mcp.md) | [@_simonsmith](https://x.com/_simonsmith) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/30b921728503d9086c9f52adbcc90a3fa3dc568cb7e85903172fc1c5295cb279.jpg" width="150"/> | [Mini World 3D exploration game](community-posts/2096641728497275011-mini-world-3d-exploration-game.md) | [@weijianzhang_](https://x.com/weijianzhang_) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/eceebf1bdd5561e25fada5daec055473bd5506cf272760a5a08a8b4ad111988c.webp" width="150"/> | [Mobile-playable Unity rally game](community-posts/2096556692842348826-mobile-playable-unity-rally-game.md) | [@kevinkern](https://x.com/kevinkern) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/756d0d4859c6a3bec065b9594d7fed7544101b6f6b6fb1e331bbfee059e84738.jpg" width="150"/> | [Photorealistic Editable Dragon Reconstruction in Blender](community-posts/2096335588727349434-photorealistic-editable-dragon-reconstruction-in-blender.md) | [@doomdave](https://x.com/doomdave) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/a50398d5761279d4c67fa425f175dd71bdd68472435b1df9f4c8e703c7edb035.jpg" width="150"/> | [Playroom: Retro 3D Browser Arcade](community-posts/2097339176094195899-playroom-retro-3d-browser-arcade.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/66b6fe9a782625a1d13bf79872857593fecf604421e40eb8cfd67c212ad0b695.webp" width="150"/> | [Railway network simulation game](community-posts/2096362653480562751-railway-network-simulation-game.md) | [@tomkrcha](https://x.com/tomkrcha) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/e14b00869191181ad52fe51c4e0a57d3ad72c405802c16cb36147a9b5d613143.jpg" width="150"/> | [Rebuilding Lego 1999 Racers](community-posts/2096438110095585753-rebuilding-lego-1999-racers.md) | [@EngMoElgaraihy](https://x.com/EngMoElgaraihy) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/36b98467e6157525383fbc35526f9c07f2cadf9f16b1559da917bb3cc5fc4eca.jpg" width="150"/> | [Recreate League of Legends as a Web Game](community-posts/2097336230078013598-recreate-league-of-legends-as-a-web-game.md) | [@liyue_ai](https://x.com/liyue_ai) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/36b98467e6157525383fbc35526f9c07f2cadf9f16b1559da917bb3cc5fc4eca.jpg" width="150"/> | [Recreate a Mini 3D Game Inspired by League of Legends](community-posts/2097320830602809682-recreate-a-mini-3d-game-inspired-by-league-of-legends.md) | [@LufzzLiz](https://x.com/LufzzLiz) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/0ba729978213ae4955dbc48dc1842a22c3ccfe72d686a037cf599fba60a214dd.webp" width="150"/> | [The Quiet Crossing exploration quest](community-posts/2096574297703637111-the-quiet-crossing-exploration-quest.md) | [@Motion_Viz](https://x.com/Motion_Viz) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ad164224745a34f4bcd14af8ec14fe0d7a6cf7203a80ea7544106dd1b76dc8f7.jpg" width="150"/> | [Three.js dark-fantasy action RPG](community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md) | [@HiltonMisia](https://x.com/HiltonMisia) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/9467608cd8acae08c8272517d7c6605284f8073c38eefd78221597d07dfe93db.webp" width="150"/> | [Trading-card battle game loop](community-posts/2096555856204644550-trading-card-battle-game-loop.md) | [@FaryaBlender3D](https://x.com/FaryaBlender3D) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e3304eeb4bf4186f9a57768af5e1962741c3dce44ed5aace2aef04585d0e69ca.jpg" width="150"/> | [Windhaven Coastal Fantasy Adventure Game](community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/67349df6f55e75c5acee30371c715c3ec04b9ae5c26c628e71d3afb3aae6c9e0.webp" width="150"/> | [Wright Flyer through a Japanese forest](community-posts/2096467585785286808-wright-flyer-through-a-japanese-forest.md) | [@thebuggeddev](https://x.com/thebuggeddev) | — |

---

## 🧱 3D Worlds & Modeling (59)

*Blender ×66 · Three.js ×42 · voxels, shaders, WebGPU, Unreal, Unity — the largest category.*

| Preview | Case | Author |
|---|---|---|
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/ea082ba0b96ce2048a717565f743d1448c4bef031ad0585dcdb75aced928fad8.jpg" width="130"/> | [3D render of an X picture](community-posts/2096338836854804782-3d-render-of-an-x-picture.md) | [@MattJamesBoyle](https://x.com/MattJamesBoyle) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3e060bfb3bf3973f0efb048cacbdc625fe879b8bca0cb46c2bb8fd367eb75268.jpg" width="130"/> | [A 12-Second Forest Road in Blender](community-posts/2096986557244723371-a-12-second-forest-road-in-blender.md) | [@Jomolos](https://x.com/Jomolos) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3dac0cf4428bc4a32bd1418c62a971bc75be632f3e10e918ba9b45800f364ba2.webp" width="130"/> | [A house modeled from scratch in Blender](community-posts/2096576154337734865-a-house-modeled-from-scratch-in-blender.md) | [@mizkun](https://x.com/mizkun) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/76eeeaa8710b4767fb99c09689e3a0b87ba770495f026e34ea34cb2b5f1f76fc.webp" width="130"/> | [Apartment sketch to rendered interiors](community-posts/2096566686266597754-apartment-sketch-to-rendered-interiors.md) | [@WorldEverett](https://x.com/WorldEverett) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/3388e9e5e8f519fb22f67c35c98f5038335da857c0a1b8883c406c6e14c36c4a.webp" width="130"/> | [Assemble and animate generated 3D assets](community-posts/2096481425050743048-assemble-and-animate-generated-3d-assets.md) | [@Stefan_3D_AI](https://x.com/Stefan_3D_AI) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/721eed98f68b8ad4264b4fbd922b185c7e6501834c9aa828a0b3b369fba5ff28.jpg" width="130"/> | [Backrooms-inspired Blender VHS scene](community-posts/2097534290112188602-backrooms-inspired-blender-vhs-scene.md) | [@chrisfirst](https://x.com/chrisfirst) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/d13ca069743cb65e0501484737d96a1fbde81927026e9b8837b149ece9b0693d.webp" width="130"/> | [Blender models with Unity VFX](community-posts/2096560142871658589-blender-models-with-unity-vfx.md) | [@CST_negi](https://x.com/CST_negi) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b6d2405bd8f8e5cd9543cde67c0c3719a2e7b5ac38c080cca7336d0f7c1ec1d1.jpg" width="130"/> | [Building a Comedy Scene of a Robotic Arm Chasing a Cat with GPT-6 Astra and Blender](community-posts/2097675660873605422-building-a-comedy-scene-of-a-robotic-arm-chasing-a-cat-with.md) | [@TanLuAI](https://x.com/TanLuAI) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/1712c53120622f0ba430f5985562bd6eb307621c1a4466ef9d2cf26c99b81716.jpg" width="130"/> | [Character Concept to Rigged 3D Model and Cartoon](community-posts/2096342420543660277-character-concept-to-rigged-3d-model-and-cartoon.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/0203a375c4a0f77f1fae00d9c8c9173739b940debd87bf4144d4f375ccc8c12e.jpg" width="130"/> | [Create and render a black hole in Blender](community-posts/2096391653669953761-create-and-render-a-black-hole-in-blender.md) | [@JohnKlerAI](https://x.com/JohnKlerAI) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/a8ee5a495643a02333b8f904a4d46c26f8211b6ba6ecb40ba3b2521387e81571.jpg" width="130"/> | [Edit a Blender scene for knurled posts and PCB fit](community-posts/2096990373813858591-edit-a-blender-scene-for-knurled-posts-and-pcb-fit.md) | [@rboyd](https://x.com/rboyd) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/aed224d4a25ce9c0d436ebd4d2bfb7fadb211bdf624364e3f7905a0dbec1546f.jpg" width="130"/> | [Folding Carton Animation from a Dieline](community-posts/2096612394281603144-folding-carton-animation-from-a-dieline.md) | [@Salmaaboukarr](https://x.com/Salmaaboukarr) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/bffeb201cd39ed86178dd22e30bda1ea70e4ff92902307d88ba66700e21dcd32.jpg" width="130"/> | [Hogwarts 3D scene](community-posts/2096907617117540478-hogwarts-3d-scene.md) | [@HiltonMisia](https://x.com/HiltonMisia) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8528f6aaa8b6070a8c1e3732f0791feac42ed1ba7d0c23cc85c7c9e0212600a1.png" width="130"/> | [Improve a 3D Model’s Facial Features in Blender Using a Reference Image](community-posts/2097313247116341424-improve-a-3d-models-facial-features-in-blender-using-a-refer.md) | [@carlos_olivera](https://x.com/carlos_olivera) |

*…and 17 more in [showcase/entries/](showcase/README.md).*

</details>

---

## 🎬 Prompt-to-Video (4)

| Case | Author | Preview |
|---|---|---|
| [T Cells — One Sentence, Five Minutes](community-posts/2095659170661904804-t-cells-one-sentence-five-minutes.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/t-cells.webp" width="130"/> |
| [Witch's First Flight — 15s Generated Shot Script](community-posts/2095873015007592679-witch-s-first-flight-15s-generated-shot-script.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/witch-first-flight.webp" width="130"/> |
| [High-Speed Parkour Motion Previz](community-posts/2096096560690209130-high-speed-parkour-motion-previz.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/parkour-previz.webp" width="130"/> |
| [AdCar TV — In-Repo One-Shot Launch Video](community-posts/2096258259459964963-adcar-tv-in-repo-one-shot-launch-video.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/adcar-tv.webp" width="130"/> |
| [Witch's First Flight — 15s Generated Shot Script](community-posts/2095873015007592679-witch-s-first-flight-15s-generated-shot-script.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/witch-first-flight.webp" width="130"/> |
| [AdCar TV — In-Repo One-Shot Launch Video](community-posts/2096258259459964963-adcar-tv-in-repo-one-shot-launch-video.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/adcar-tv.webp" width="130"/> |
| [T Cells — One Sentence, Five Minutes](community-posts/2095659170661904804-t-cells-one-sentence-five-minutes.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/t-cells.webp" width="130"/> |
| [High-Speed Parkour Motion Previz](community-posts/2096096560690209130-high-speed-parkour-motion-previz.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/parkour-previz.webp" width="130"/> |

> Full video-prompt methodology (Remotion, HyperFrames, shot scripts): [LuxRealGrowth/awesome-astra-video-prompts](https://github.com/LuxRealGrowth/awesome-astra-video-prompts).

---

## 🕸️ Web & Interactive (3)

| Case | Author | Preview |
|---|---|---|
| [Create an Interactive Soft-Body Slime with Three.js and](community-posts/2096793432987464010-create-an-interactive-soft-body-slime-with-three-js-and-webg.md) | [@Delroy715](https://x.com/Delroy715) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/080a768b7958082811553a4d1a4c865caeee6e542e68fe0ba9e32ed478233342.jpg" width="130"/> |
| [Endless Miniature Street in Three.js WebGPU](community-posts/2096956214680965501-endless-miniature-street-in-three-js-webgpu.md) | [@creativedash](https://x.com/creativedash) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/c2aa4cd5daf5e1bc8f71051db13c08e7f52359b5a5aaf7b813b72d474117897e.jpg" width="130"/> |
| [Interactive jelly lemon tree](community-posts/2097065330728128920-interactive-jelly-lemon-tree.md) | [@vib3coded](https://x.com/vib3coded) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/19fa5b36caaf4663987e99892e3cb3babcc452cbe50e1ef2f6108a859d3eba36.jpg" width="130"/> |
| [Endless Miniature Street in Three.js WebGPU](community-posts/2096956214680965501-endless-miniature-street-in-three-js-webgpu.md) | [@creativedash](https://x.com/creativedash) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/c2aa4cd5daf5e1bc8f71051db13c08e7f52359b5a5aaf7b813b72d474117897e.jpg" width="130"/> |
| [Create an Interactive Soft-Body Slime with Three.js and WebGPU](community-posts/2096793432987464010-create-an-interactive-soft-body-slime-with-three-js-and-webg.md) | [@Delroy715](https://x.com/Delroy715) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/080a768b7958082811553a4d1a4c865caeee6e542e68fe0ba9e32ed478233342.jpg" width="130"/> |
| [Interactive jelly lemon tree](community-posts/2097065330728128920-interactive-jelly-lemon-tree.md) | [@vib3coded](https://x.com/vib3coded) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/19fa5b36caaf4663987e99892e3cb3babcc452cbe50e1ef2f6108a859d3eba36.jpg" width="130"/> |

---

## 📦 More creations (104)

*The long tail: interactive portfolios, room dioramas, product stories, data-viz toys and other
one-prompt builds that don't fit the four categories above. Showing 30 —
[browse all in the web viewer](site/index.html).*

| Preview | Case | Author |
|---|---|---|
| <img src="" width="120"/> | [](community-posts/README.md) | — |
| <img src="" width="120"/> | [](community-posts/SOURCES.md) | — |
| <img src="https://media.beatapi.io/prompt-gallery/gpt-6-astra-3d/20-m-bed-desk-sofa-kitchen-409988/poster-327f41c77cab.webp" width="120"/> | [20 m². Bed, desk, sofa, kitchen.](community-posts/2096377743701409988-20-m²-bed-desk-sofa-kitchen.md) | [@groovestreetgen](https://x.com/groovestreetgen) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/28a462ad372dbb45b012ec3ff118fd94ca6ea7ae6ea0a26320ab4bee839dfd63.jpg" width="120"/> | [3D Apple-style heart and smiling emoji](community-posts/2099751278234767673-3d-apple-style-heart-and-smiling-emoji.md) | [@Just_sharon7](https://x.com/Just_sharon7) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2095619198437240836/img/S3arJYTi2akNREnW.jpg" width="120"/> | [3D Product Mockup Studio](community-posts/2095619319690400253-3d-product-mockup-studio.md) | [@joshmillgate](https://x.com/joshmillgate) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2098689349462466560/img/qeLFqQFtAn3R5FUa.jpg" width="120"/> | [3D Scan Patch for Printing](community-posts/2098690472193695756-3d-scan-patch-for-printing.md) | [@toyoshi](https://x.com/toyoshi) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/6b76cf5a4a0feefa91cafe184567430f78b75607a7a2347c64807100431ebcac.jpg" width="120"/> | [3D world full of very high skyscrapers](community-posts/2099487024256589970-3d-world-full-of-very-high-skyscrapers.md) | [@MohdBilalArshad](https://x.com/MohdBilalArshad) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8dcd8f7d1406525c0a56e16bf3bc2591fb0191c1e4226f74cc364b4daa841efd.webp" width="120"/> | [A 2D logo becomes an animated character](community-posts/2096559197999501724-a-2d-logo-becomes-an-animated-character.md) | [@anthonyriera](https://x.com/anthonyriera) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2095611898968547328/img/EKCYWcJTBrAMT4e6.jpg" width="120"/> | [A Listing Becomes a Film](community-posts/2095612137582526615-a-listing-becomes-a-film.md) | [@realYunfanYe](https://x.com/realYunfanYe) |
| <img src="https://media.beatapi.io/prompt-gallery/gpt-6-astra-3d/a-trick-that-improved-my-3d-results-with-gpt-6-astra-a-373286/image-9a88a5a41613.webp" width="120"/> | [A trick that improved my 3D results with GPT 6 Astra](community-posts/2096920387896373286-a-trick-that-improved-my-3d-results-with-gpt-6-astra-a-lot.md) | [@tiagomanel](https://x.com/tiagomanel) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2095673008803241987/img/rkGOb6E0-oOUi5ka.jpg" width="120"/> | [ABYSSAL: The Living Deep](community-posts/2095673885605630429-abyssal-the-living-deep.md) | [@emollick](https://x.com/emollick) |
| <img src="https://media.beatapi.io/prompt-gallery/gpt-6-astra-3d/agi-is-here-381458/poster-bfa5a808b9d4.webp" width="120"/> | [AGI is here.](community-posts/2097076033564381458-agi-is-here.md) | [@KushDaddyOG101](https://x.com/KushDaddyOG101) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096580463288803328/img/_S5-VDnQ9RJh9URY.jpg" width="120"/> | [Afterlight Robot World](community-posts/2096584624432374151-afterlight-robot-world.md) | [@anshuc](https://x.com/anshuc) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096004824751890434/img/fW0IV1fAgJ3b7i-D.jpg" width="120"/> | [Afterlight · 45 分钟 3D 游戏](community-posts/2096008083826725132-afterlight-45-分钟-3d-游戏.md) | [@anshuc](https://x.com/anshuc) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096364962629431296/img/xB4kNtDvFHHRftRZ.jpg" width="120"/> | [Age of Empires IV on Apple Silicon](community-posts/2096365209111724235-age-of-empires-iv-on-apple-silicon.md) | [@marc_ibrahim](https://x.com/marc_ibrahim) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2098077790042214400/img/dssFiraBPXuLCRGM.jpg" width="120"/> | [Antibody Developability Explorer](community-posts/2098078245350518884-antibody-developability-explorer.md) | [@andrewaiginin](https://x.com/andrewaiginin) |
| <img src="https://media.beatapi.io/prompt-gallery/gpt-6-astra-3d/asked-gpt-6-astra-to-build-an-interactive-3d-visualization-of-a-028703/poster-e1ecd05e7217.webp" width="120"/> | [Asked GPT-6 Astra to build an interactive 3D visuali](community-posts/2096441229341028703-asked-gpt-6-astra-to-build-an-interactive-3d-visualization-o.md) | [@HeyDhruvv](https://x.com/HeyDhruvv) |
| <img src="https://media.beatapi.io/prompt-gallery/gpt-6-astra-3d/asked-gpt-6-astra-to-recreate-the-titanic-s-final-night-290438/poster-001a573ff035.webp" width="120"/> | [Asked GPT-6 Astra to recreate the Titanic’s final ni](community-posts/2096490252865290438-asked-gpt-6-astra-to-recreate-the-titanics-final-night.md) | [@choblin29](https://x.com/choblin29) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2097430424205295616/img/3DRzerCx-p39fz32.jpg" width="120"/> | [Ass Bench: Self-Improving 3D Cheeks](community-posts/2097431364270248104-ass-bench-self-improving-3d-cheeks.md) | [@developedbyed](https://x.com/developedbyed) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096209195934838784/img/BQsIkf9d-zjmHrmR.jpg" width="120"/> | [Astra Launch Motion Film](community-posts/2096209514248958161-astra-launch-motion-film.md) | [@athrix_codes](https://x.com/athrix_codes) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096192501153705984/img/Owwdv3C08sVR0vOg.jpg" width="120"/> | [Astra Plays Slay the Spire 2](community-posts/2096195104809873710-astra-plays-slay-the-spire-2.md) | [@coolish](https://x.com/coolish) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2097560639455514624/img/IBFogCwcmIJtgTlc.jpg" width="120"/> | [Astra-Rigged Three.js Character](community-posts/2097561634076016774-astra-rigged-threejs-character.md) | [@SimonasLTU1](https://x.com/SimonasLTU1) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096062838892814336/img/ME5ZS6OhoEsNAfH6.jpg" width="120"/> | [Astral War](community-posts/2096079660605997264-astral-war.md) | [@0xRishi](https://x.com/0xRishi) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/71207bef30c1d03e3a6d1b9901b86283ff784be11dbe153eb9d9243cd1b2a1bc.jpg" width="120"/> | [Autonomous Model Railway With Collision Avoidance](community-posts/2099362575339372780-autonomous-model-railway-with-collision-avoidance.md) | [@free_ai_guides](https://x.com/free_ai_guides) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/15b86aef756eda74957965d57ff6104a61d7fcc04cad37581a49726ef5f363aa.webp" width="120"/> | [Bioluminescent deep-sea landing page](community-posts/2096269057544831175-bioluminescent-deep-sea-landing-page.md) | [@himanshubuildss](https://x.com/himanshubuildss) |
| <img src="https://pbs.twimg.com/media/HR_63SwawAAKETQ.jpg" width="120"/> | [Birthday Rarity Explorer](community-posts/2098671802574840117-birthday-rarity-explorer.md) | [@adriannalakatos](https://x.com/adriannalakatos) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096943524281286656/img/5zywNFWnlxigq4FG.jpg" width="120"/> | [Boeing 777 Landing Sim](community-posts/2096946420234207459-boeing-777-landing-sim.md) | [@LuminaBench](https://x.com/LuminaBench) |
| <img src="https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/da595232495fdcdcd646614361e119ff7b780672c6c697364c0197cc19302fd1.webp" width="120"/> | [Browser racing physics in C# and WASM](community-posts/2096258619574513880-browser-racing-physics-in-c-and-wasm.md) | [@achepta_tm](https://x.com/achepta_tm) |
| <img src="https://pbs.twimg.com/amplify_video_thumb/2096980056065314816/img/_duxg6slMRbzLtu1.jpg" width="120"/> | [Bubble Wrap Simulator](community-posts/2096980188126986533-bubble-wrap-simulator.md) | [@crtvTeknologist](https://x.com/crtvTeknologist) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/a8bbf8917e9f19971a1ed3976735efde583ae25e4dedf23df3e71f16f775b59a.jpg" width="120"/> | [Build THE LAST GATE: A Crowd Runner with Math Gates](community-posts/2097678911882809407-build-the-last-gate-a-crowd-runner-with-math-gates.md) | [@KeWai386772](https://x.com/KeWai386772) |


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

## 🎓 Learning path — from viral moment to your own build

New here? This is the shortest path from "cool demo" to "my own playable build":

| Step | Do this | Time |
|---|---|---|
| 1️⃣ **Watch** | Scroll the [Gallery](#️-gallery) and [Playable Worlds](#-playable-worlds--try-in-browser) — see what one prompt produces | 10 min |
| 2️⃣ **Copy** | Open any case → copy the verbatim prompt → run it in GPT-6 Astra | 15 min |
| 3️⃣ **Reproduce** | Pick [astra-3d-001 Endless Runner](prompts/full-games/astra-3d-001-endless-runner.md) — the smoke-test recipe with an acceptance checklist | 30 min |
| 4️⃣ **Understand** | Read the [five-clause pattern](#-learning-path--from-viral-moment-to-your-own-build) every working prompt shares | 10 min |
| 5️⃣ **Create** | Take a [playbook](#-playbooks), plug in your idea, ship your own game — then PR it back here | a weekend |

**Milestone:** 100 cases were added in the first two weeks. The recipes layer needs reproducers —
running one recipe and logging the result is the single most valuable contribution right now.

---

## ❓ FAQ

**Where do the prompts come from?**
Only two places: the X post itself, or its replies. We never reconstruct prompts from results, and
cases without a public prompt are still included — the case proves the play pattern exists.

**Why isn't every entry reproducible?**
Two different promises. Cases (this really happened, here's the proof) vs. recipes (you can run this
again — model version, settings, inputs and acceptance checks all pinned). Never mix them: an
awesome-list full of "reproducible" claims without checklists is just vibes.

**A preview image is broken — why?**
Upstream lists reorganize their assets. All previews are now mirrored into
[`assets/previews/`](assets/previews) in this repo, so links stay alive. Report any straggler.

**Can I use these prompts commercially?**
The prompts are what authors chose to share publicly; the *outputs* belong to their creators.
Recipes are CC0. Always credit the original author when you showcase a case.

**Does this work with other models?**
Recipes pin `gpt-6-astra` because behavior drifts between models. The *pattern* (autonomy grant,
exact deliverable, judging bar, bounded permissions) transfers well — expect to retune settings.

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yangzhou-chaofan/awesome-gpt6-astra-game-prompts&type=Timeline)](https://star-history.com/#yangzhou-chaofan/awesome-gpt6-astra-game-prompts&Date)

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

**Snapshot 2026-09-17** · X posts are the record of truth; awesome-lists are aggregation channels only ·
All work © its original creators, credited per entry · Unofficial community project, not affiliated with or endorsed by OpenAI

[CC0-1.0](LICENSE) · Made with 🕹️ by the community

</div>
