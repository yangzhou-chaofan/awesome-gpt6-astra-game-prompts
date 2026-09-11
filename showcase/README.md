# 🕹️ Showcase — X 上的 GPT-6 Astra 玩法案例

> **115 条案例 · 34 条带 prompt 原文** · 抓取 2026-09-11 · 每条可回链 X 原帖

本目录与 [`prompts/`](../prompts/) 互补，不改变其可复现契约：`prompts/` 是**配方**（模型版本+参数+输入+验收），
这里收录的是**真实案例** —— 证明玩法成立、给出原帖上下文，并在作者公开时附上 prompt 原文。

## 收录原则

1. **X 是唯一 record source。** 每条必须回链 X 原帖；awesome lists 只是发现渠道（见文末致谢）。
2. **Prompt 只有两处来源：帖子里，或帖子下面。** 作者公开即原文照录。
3. **没有 prompt 也照收。** 案例先证明'玩法存在'；prompt 后补，或激励读者蹲作者 / 自己复现。
4. **从所有 awesome list 聚合，按原帖去重。** 同帖多清单收录 → 合并一条，出处全保留。
5. **分类 + 推荐优先于大而全。** 见 🏆 推荐榜。
6. **网页与 repo 共建。** 数据在 [data.json](data.json)，网页端直接消费；改 repo 即改网页。

## 🏆 推荐榜（编辑精选）

| 案例 | 分类 | 推荐理由 |
|---|---|---|
| [Windhaven Coastal Fantasy Adventure Game](entries/windhaven-coastal-fantasy-adventure-game.md) | 🗺️ Adventure & RPG | 长叙事 prompt：风格→世界→镜头→负面约束，一段扛住全案 |
| [Three.js dark-fantasy action RPG](entries/threejs-dark-fantasy-action-rpg.md) | 🗺️ Adventure & RPG | 单 prompt 出完整 ARPG：氛围与玩法系统的平衡最好 |
| [语音通关《杀戮尖塔 2》](entries/语音通关杀戮尖塔-2.md) | 🤖 Agent Plays | Computer Use 边界案例：零游戏 API，全靠看屏幕 |
| [我让 GPT-6 Astra 做了个游戏，然后让它自己玩、自己录屏，再剪一段开发实录。](entries/我让-gpt-6-astra-做了个游戏然后让它自己玩自己录屏再剪一段开发实录.md) | 🤖 Agent Plays | 做→自玩→自录→自剪，全自动内容管线 |
| [Rebuilding Lego 1999 Racers](entries/rebuilding-lego-1999-racers.md) | 🎈 Arcade & Action | 完整游戏复刻 + 怀旧对比，可复现性强 |
| [Mini World 3D exploration game](entries/mini-world-3d-exploration-game.md) | 🧪 Simulation & Interactive Toys | 为真人设计（4岁孩子）：视角/缩放/难度约束即上手性 |
| [Grand Theft Auto Game with San Andreas Charact](entries/grand-theft-auto-game-with-san-andreas-characters-.md) | 🧪 Simulation & Interactive Toys | 极短 prompt 出复杂结果 —— 反差标杆 |

## 分类总览

| 分类 | 条目 | 带Prompt | 说明 |
|---|---|---|---|
| 🎈 **[Arcade & Action](#arcade-action)** | 47 | 8 | 上手即玩的一把流：跑酷、射击、平台、节奏。看手感约束怎么写 |
| 🧪 **[Simulation & Interactive Toys](#sim-toy)** | 28 | 14 | 城市 / 飞行 / 物理沙盘与互动玩具。少约束换稳定涌现 |
| 🗺️ **[Adventure & RPG](#adventure-rpg)** | 15 | 9 | 任务、探索、成长。看 prompt 如何承载叙事与系统设计 |
| ⚔️ **[Multiplayer & Battle](#multiplayer-battle)** | 16 | 2 | 对战、卡牌、共斗。单 prompt 能不能扛住规则博弈 |
| 🤖 **[Agent Plays](#agent-plays)** | 9 | 1 | 模型亲自上手玩游戏 —— Computer Use 的边界在哪 |

---

<a id="arcade-action"></a>
## 🎈 Arcade & Action (47)

> 上手即玩的一把流：跑酷、射击、平台、节奏。看手感约束怎么写

| 案例 | 作者 | Prompt | 原帖 |
|---|---|---|---|
| ⭐ [Rebuilding Lego 1999 Racers](entries/rebuilding-lego-1999-racers.md) | [:@EngMoElgaraihy](https://x.com/EngMoElgaraihy) | ✅ | [↗](https://x.com/EngMoElgaraihy/status/2096438110095585753) |
| [A crab game with action-driven mechanics](entries/a-crab-game-with-action-driven-mechanics.md) | [:@zeuuss_01](https://x.com/zeuuss_01) | ✅ | [↗](https://x.com/zeuuss_01/status/2096337879173591171) |
| [AGI is 100% solved](entries/agi-is-100-solved.md) | [:@higgsfield_ai](https://x.com/higgsfield_ai) | ✅ | [↗](https://x.com/higgsfield_ai/status/2096342420543660277) |
| [Complete Three.js puzzle level](entries/complete-threejs-puzzle-level.md) | [:@TvWoo](https://x.com/TvWoo) | ✅ | [↗](https://x.com/TvWoo/status/2096505740643246231) |
| [LEGO Minifig Game Asset with Blender MCP](entries/lego-minifig-game-asset-with-blender-mcp.md) | [:@_simonsmith](https://x.com/_simonsmith) | ✅ | [↗](https://x.com/_simonsmith/status/2096766465730847059) |
| [Playable D4-inspired apartment](entries/playable-d4-inspired-apartment.md) | [:@Swery65](https://x.com/Swery65) | ✅ | [↗](https://x.com/Swery65/status/2096413869841473930) |
| [Rig and animate a digitigrade mech in Godot](entries/rig-and-animate-a-digitigrade-mech-in-godot.md) | [:@om_patel5](https://x.com/om_patel5) | ✅ | [↗](https://x.com/om_patel5/status/2097123382852829230) |
| [Rotatable 3D shogi board](entries/rotatable-3d-shogi-board.md) | [:@hatukougara](https://x.com/hatukougara) | ✅ | [↗](https://x.com/hatukougara/status/2096579856133947507) |
| [1 shotted this w/ GPT-6 Astra](entries/1-shotted-this-w-gpt-6-astra.md) | [:@d4m1n](https://x.com/d4m1n) | — | [↗](https://x.com/d4m1n/status/2096258259459964963) |
| [11–20：视频、UI、游戏与创作工具](entries/1120视频ui游戏与创作工具.md) | [:@cat_shark_L1011](https://x.com/cat_shark_L1011) | — | [↗](https://x.com/cat_shark_L1011/status/2096215847438291002) |
| [20 m². Bed, desk, sofa, kitchen](entries/20-m²-bed-desk-sofa-kitchen.md) | [:@groovestreetgen](https://x.com/groovestreetgen) | — | [↗](https://x.com/groovestreetgen/status/2096377743701409988) |
| [a couple of weeks ago I built a 3d morphogen](entries/a-couple-of-weeks-ago-i-built-a-3d-morphogenesis-h.md) | [:@andreasxirtus](https://x.com/andreasxirtus) | — | [↗](https://x.com/andreasxirtus/status/2095794528410124515) |
| [A trick that improved my 3D results with GPT](entries/a-trick-that-improved-my-3d-results-with-gpt-6-ast.md) | [:@tiagomanel](https://x.com/tiagomanel) | — | [↗](https://x.com/tiagomanel/status/2096920387896373286) |
| [Afterlight](entries/afterlight.md) | [:@anshuc](https://x.com/anshuc) | — | [↗](https://x.com/anshuc/status/2096008083826725132) |
| [Afterlight Robot World](entries/afterlight-robot-world.md) | [:@anshuc](https://x.com/anshuc) | — | [↗](https://x.com/anshuc/status/2096584624432374151) |
| [AGI怕是真的要来了！！](entries/agi怕是真的要来了.md) | [:@rionaifantasy](https://x.com/rionaifantasy) | — | [↗](https://x.com/rionaifantasy/status/2096163579925770671) |
| [asked GPT 6 Astra to recreate the 2017 Roblo](entries/asked-gpt-6-astra-to-recreate-the-2017-roblox-anth.md) | [:@LeftWingFash](https://x.com/LeftWingFash) | — | [↗](https://x.com/LeftWingFash/status/2097193662283161673) |
| [Asked GPT-6 Astra to build an interactive 3D](entries/asked-gpt-6-astra-to-build-an-interactive-3d-visua.md) | [:@HeyDhruvv](https://x.com/HeyDhruvv) | — | [↗](https://x.com/HeyDhruvv/status/2096441229341028703) |
| [Asked GPT-6 Astra to recreate the Titanic’s ](entries/asked-gpt-6-astra-to-recreate-the-titanics-final-n.md) | [:@choblin29](https://x.com/choblin29) | — | [↗](https://x.com/choblin29/status/2096490252865290438) |
| [Blender to Unreal House](entries/blender-to-unreal-house.md) | [:@Dimillian](https://x.com/Dimillian) | — | [↗](https://x.com/Dimillian/status/2095596700815516004) |
| [Browser 3D Game Prototype](entries/browser-3d-game-prototype.md) | [:@theo](https://x.com/theo) | — | [↗](https://x.com/theo/status/2095599934766764338) |
| [Build a finished, polished kart racer in Rob](entries/build-a-finished-polished-kart-racer-in-roblox-stu.md) | [:@givros](https://x.com/givros) | — | [↗](https://x.com/givros/status/2096219700879331665) |
| [Fighting Game Animation Test](entries/fighting-game-animation-test.md) | [:@YuK1_Game](https://x.com/YuK1_Game) | — | [↗](https://x.com/YuK1_Game/status/2097446904942780699) |
| [Fort Worth Stockyards Map](entries/fort-worth-stockyards-map.md) | [:@dfwstrategy](https://x.com/dfwstrategy) | — | [↗](https://x.com/dfwstrategy/status/2097346335712137483) |
| [From Game to Trailer](entries/from-game-to-trailer.md) | [:@MengTo](https://x.com/MengTo) | — | [↗](https://x.com/MengTo/status/2096213835460084184) |
| [Gave GPT-6 Astra a watch photo. It built thi](entries/gave-gpt-6-astra-a-watch-photo-it-built-this-in-bl.md) | [:@Golfrrr69](https://x.com/Golfrrr69) | — | [↗](https://x.com/Golfrrr69/status/2096670690912997618) |
| [GPT-6 Astra + Higgsfield + Blender + Cinema ](entries/gpt-6-astra-higgsfield-blender-cinema-4d-a-new-era.md) | [:@XenStudiosUK](https://x.com/XenStudiosUK) | — | [↗](https://x.com/XenStudiosUK/status/2097064044146397560) |
| [GPT-6 Astra 连续运行 8h 的成果（还在继续制作影片中……](entries/gpt-6-astra-连续运行-8h-的成果还在继续制作影片中.md) | [:@ZHO_ZHO_ZHO](https://x.com/ZHO_ZHO_ZHO) | — | [↗](https://x.com/ZHO_ZHO_ZHO/status/2096195128927093076) |
| [Hatsune Miku Pixel Art](entries/hatsune-miku-pixel-art.md) | [:@suemaruuuuuuX](https://x.com/suemaruuuuuuX) | — | [↗](https://x.com/suemaruuuuuuX/status/2096212351502721361) |
| [I asked @openai GPT 6 Astra to create 3d pri](entries/i-asked-openai-gpt-6-astra-to-create-3d-printable-.md) | [:@sgtpatel](https://x.com/sgtpatel) | — | [↗](https://x.com/sgtpatel/status/2096685771688194118) |
| [I asked GPT 6 Astra to model the starting vi](entries/i-asked-gpt-6-astra-to-model-the-starting-village-.md) | [:@JeffDraws](https://x.com/JeffDraws) | — | [↗](https://x.com/JeffDraws/status/2096380719572627798) |
| [I asked GPT-6 Astra to build a complete CAD/](entries/i-asked-gpt-6-astra-to-build-a-complete-cadcammes-.md) | [:@alfonsotames](https://x.com/alfonsotames) | — | [↗](https://x.com/alfonsotames/status/2096698742439112766) |
| [Interactive 3D Ankle Atlas](entries/interactive-3d-ankle-atlas.md) | [:@Emanuel_Andre7](https://x.com/Emanuel_Andre7) | — | [↗](https://x.com/Emanuel_Andre7/status/2096528986390085696) |
| [Interactive Hidden-Book Photo](entries/interactive-hidden-book-photo.md) | [:@rohancalum](https://x.com/rohancalum) | — | [↗](https://x.com/rohancalum/status/2097009625627500814) |
| [Interactive Model Railroad](entries/interactive-model-railroad.md) | [:@nickfromlater](https://x.com/nickfromlater) | — | [↗](https://x.com/nickfromlater/status/2097355845524726084) |
| [Knicks Tip-In 3D Replay](entries/knicks-tip-in-3d-replay.md) | [:@Flynnjamm](https://x.com/Flynnjamm) | — | [↗](https://x.com/Flynnjamm/status/2096663293901578438) |
| [Metal Slug Dream Loop Remake](entries/metal-slug-dream-loop-remake.md) | [:@ashen_one](https://x.com/ashen_one) | — | [↗](https://x.com/ashen_one/status/2097539441900261645) |
| [Microduck Assembly Lab](entries/microduck-assembly-lab.md) | [:@tspy](https://x.com/tspy) | — | [↗](https://x.com/tspy/status/2096238855519453662) |
| [Mobile Ad Game Remake](entries/mobile-ad-game-remake.md) | [:@buildingadlicio](https://x.com/buildingadlicio) | — | [↗](https://x.com/buildingadlicio/status/2096111709496680842) |
| [Photorealistic Contra Game](entries/photorealistic-contra-game.md) | [:@illscience](https://x.com/illscience) | — | [↗](https://x.com/illscience/status/2097059547328241971) |
| [Short Briefs That Still Worked](entries/short-briefs-that-still-worked.md) | [:@guuchacha149182](https://x.com/guuchacha149182) | — | [↗](https://x.com/guuchacha149182/status/2096813471463882947) |
| [Snakes and Ladders in Unreal](entries/snakes-and-ladders-in-unreal.md) | [:@higgsfield_ai](https://x.com/higgsfield_ai) | — | [↗](https://x.com/higgsfield_ai/status/2097464282829168955) |
| [ı asked GPT-6 Astra to make valorant](entries/ı-asked-gpt-6-astra-to-make-valorant.md) | [:@valohabercisi](https://x.com/valohabercisi) | — | [↗](https://x.com/valohabercisi/status/2096550643599069548) |
| [「日本アニメでよく見られる、二脚人型の、いわゆる『リアルロボット』の3Dモデルを作成して](entries/日本アニメでよく見られる二脚人型のいわゆるリアルロボットの3dモデルを作成してくださいとしてgpt-.md) | [:@hawkymisc](https://x.com/hawkymisc) | — | [↗](https://x.com/hawkymisc/status/2096797700922753410) |
| [グラディウス1のステージ1を、R-TYPEの機体で遊べるゲームを作ってください。](entries/グラディウス1のステージ1をr-typeの機体で遊べるゲームを作ってください.md) | [:@die2000](https://x.com/die2000) | — | [↗](https://x.com/die2000/status/2096101876735541488) |
| [一张图，直接变成一个能“逛”的 3D 世界](entries/一张图直接变成一个能逛的-3d-世界.md) | [:@Adam38363368936](https://x.com/Adam38363368936) | — | [↗](https://x.com/Adam38363368936/status/2096787471107551649) |
| [从作品出发，找到下一次三维创作的起点。](entries/从作品出发找到下一次三维创作的起点.md) | [:@rpnickson](https://x.com/rpnickson) | — | [↗](https://x.com/rpnickson/status/2097488440489116111) |

<a id="sim-toy"></a>
## 🧪 Simulation & Interactive Toys (28)

> 城市 / 飞行 / 物理沙盘与互动玩具。少约束换稳定涌现

| 案例 | 作者 | Prompt | 原帖 |
|---|---|---|---|
| ⭐ [Grand Theft Auto Game with San Andreas Chara](entries/grand-theft-auto-game-with-san-andreas-characters-.md) | [:@ElIngeRRC](https://x.com/ElIngeRRC) | ✅ | [↗](https://x.com/ElIngeRRC/status/2096739993217577219) |
| ⭐ [Mini World 3D exploration game](entries/mini-world-3d-exploration-game.md) | [:@weijianzhang_](https://x.com/weijianzhang_) | ✅ | [↗](https://x.com/weijianzhang_/status/2096641728497275011) |
| [Browser city game with a supplied character](entries/browser-city-game-with-a-supplied-character.md) | [:@djrio_vr](https://x.com/djrio_vr) | ✅ | [↗](https://x.com/djrio_vr/status/2096398839830008292) |
| [Browser racing physics in C and WASM](entries/browser-racing-physics-in-c-and-wasm.md) | [:@achepta_tm](https://x.com/achepta_tm) | ✅ | [↗](https://x.com/achepta_tm/status/2096258619574513880) |
| [Building a Comedy Scene of a Robotic Arm Cha](entries/building-a-comedy-scene-of-a-robotic-arm-chasing-a.md) | [:@TanLuAI](https://x.com/TanLuAI) | ✅ | [↗](https://x.com/TanLuAI/status/2097675660873605422) |
| [Interactive dual-ring energy core](entries/interactive-dual-ring-energy-core.md) | [:@oneruofeng](https://x.com/oneruofeng) | ✅ | [↗](https://x.com/oneruofeng/status/2096551010089263181) |
| [Interactive Hyperloop demo](entries/interactive-hyperloop-demo.md) | [:@hbanay98](https://x.com/hbanay98) | ✅ | [↗](https://x.com/hbanay98/status/2096250748099068377) |
| [Interactive jelly lemon tree](entries/interactive-jelly-lemon-tree.md) | [:@vib3coded](https://x.com/vib3coded) | ✅ | [↗](https://x.com/vib3coded/status/2097065330728128920) |
| [Komorebi river kayaking](entries/komorebi-river-kayaking.md) | [:@ItsmeAjayKV](https://x.com/ItsmeAjayKV) | ✅ | [↗](https://x.com/ItsmeAjayKV/status/2096244208533455049) |
| [Nuclear Explosion 3D City Simulation](entries/nuclear-explosion-3d-city-simulation.md) | [:@ashishthakur___](https://x.com/ashishthakur___) | ✅ | [↗](https://x.com/ashishthakur___/status/2096562462674079868) |
| [Playable 3D Ensemble with Audio-Synchronized](entries/playable-3d-ensemble-with-audio-synchronized-anima.md) | [:@groovestreetgen](https://x.com/groovestreetgen) | ✅ | [↗](https://x.com/groovestreetgen/status/2096354461652488562) |
| [Railway network simulation game](entries/railway-network-simulation-game.md) | [:@tomkrcha](https://x.com/tomkrcha) | ✅ | [↗](https://x.com/tomkrcha/status/2096362653480562751) |
| [Wright Flyer through a Japanese forest](entries/wright-flyer-through-a-japanese-forest.md) | [:@thebuggeddev](https://x.com/thebuggeddev) | ✅ | [↗](https://x.com/thebuggeddev/status/2096467585785286808) |
| [💥 A few chats with GPT-6 Astra turned into a](entries/a-few-chats-with-gpt-6-astra-turned-into-an-intera.md) | [:@MrLarus](https://x.com/MrLarus) | ✅ | [↗](https://x.com/MrLarus/status/2096971051334857181) |
| [Asked GPT-6 Astra to build The City Above in](entries/asked-gpt-6-astra-to-build-the-city-above-in-three.md) | [:@pankajkumar_dev](https://x.com/pankajkumar_dev) | — | [↗](https://x.com/pankajkumar_dev/status/2096795601828536826) |
| [Asteria Spaceship Explorer](entries/asteria-spaceship-explorer.md) | [:@wengsiong22](https://x.com/wengsiong22) | — | [↗](https://x.com/wengsiong22/status/2096941914906144784) |
| [Bubble Wrap Simulator](entries/bubble-wrap-simulator.md) | [:@crtvTeknologist](https://x.com/crtvTeknologist) | — | [↗](https://x.com/crtvTeknologist/status/2096980188126986533) |
| [Build a new 3D city scene for me. I want sev](entries/build-a-new-3d-city-scene-for-me-i-want-several-ty.md) | [:@AndrewWalko](https://x.com/AndrewWalko) | — | [↗](https://x.com/AndrewWalko/status/2095987508475834641) |
| [Case breakdowns](entries/case-breakdowns.md) | [:@adilinthewild](https://x.com/adilinthewild) | — | [↗](https://x.com/adilinthewild/status/2098247449026715966) |
| [Fall Guys 到 5 天 SimCity](entries/fall-guys-到-5-天-simcity.md) | [:@MatthewBerman](https://x.com/MatthewBerman) | — | [↗](https://x.com/MatthewBerman/status/2095595892464333065) |
| [Jelly Baby Playground](entries/jelly-baby-playground.md) | [:@scottstts](https://x.com/scottstts) | — | [↗](https://x.com/scottstts/status/2096364764054131119) |
| [Machining Factory Game](entries/machining-factory-game.md) | [:@chod3s](https://x.com/chod3s) | — | [↗](https://x.com/chod3s/status/2097563137784385541) |
| [Puzzles & brain games](entries/puzzles-brain-games.md) | [:@edmund5](https://x.com/edmund5) | — | [↗](https://x.com/edmund5/status/2097603093819261002) |
| [Reference-Image Aquarium Game](entries/reference-image-aquarium-game.md) | [:@TimJayas](https://x.com/TimJayas) | — | [↗](https://x.com/TimJayas/status/2095611134992945385) |
| [Rink Life](entries/rink-life.md) | [:@JakeBoyles](https://x.com/JakeBoyles) | — | [↗](https://x.com/JakeBoyles/status/2096983366327226501) |
| [Texas Jet Plant Simulation](entries/texas-jet-plant-simulation.md) | [:@konstantinsaifo](https://x.com/konstantinsaifo) | — | [↗](https://x.com/konstantinsaifo/status/2096122429319852319) |
| [Voxel Ship in a Bottle](entries/voxel-ship-in-a-bottle.md) | [:@DeryaTR_](https://x.com/DeryaTR_) | — | [↗](https://x.com/DeryaTR_/status/2095699049722581065) |
| [【AIアニメ制作共有①】](entries/aiアニメ制作共有①.md) | [:@MiraMusic_AI](https://x.com/MiraMusic_AI) | — | [↗](https://x.com/MiraMusic_AI/status/2096441679847006358) |

<a id="adventure-rpg"></a>
## 🗺️ Adventure & RPG (15)

> 任务、探索、成长。看 prompt 如何承载叙事与系统设计

| 案例 | 作者 | Prompt | 原帖 |
|---|---|---|---|
| ⭐ [Three.js dark-fantasy action RPG](entries/threejs-dark-fantasy-action-rpg.md) | [:@HiltonMisia](https://x.com/HiltonMisia) | ✅ | [↗](https://x.com/HiltonMisia/status/2096637091627364531) |
| ⭐ [Windhaven Coastal Fantasy Adventure Game](entries/windhaven-coastal-fantasy-adventure-game.md) | [:@tripoai](https://x.com/tripoai) | ✅ | [↗](https://x.com/tripoai/status/2096629506047955327) |
| [Low-poly beach treasure hunt](entries/low-poly-beach-treasure-hunt.md) | [:@sorano_concon_g](https://x.com/sorano_concon_g) | ✅ | [↗](https://x.com/sorano_concon_g/status/2096570815714414844) |
| [Mobile-playable Unity rally game](entries/mobile-playable-unity-rally-game.md) | [:@kevinkern](https://x.com/kevinkern) | ✅ | [↗](https://x.com/kevinkern/status/2096556692842348826) |
| [One Piece-inspired sailing world](entries/one-piece-inspired-sailing-world.md) | [:@yash_yk45](https://x.com/yash_yk45) | ✅ | [↗](https://x.com/yash_yk45/status/2096518775042707700) |
| [Recreate a Mini 3D Game Inspired by League o](entries/recreate-a-mini-3d-game-inspired-by-league-of-lege.md) | [:@LufzzLiz](https://x.com/LufzzLiz) | ✅ | [↗](https://x.com/LufzzLiz/status/2097320830602809682) |
| [Recreate League of Legends as a Web Game](entries/recreate-league-of-legends-as-a-web-game.md) | [:@liyue_ai](https://x.com/liyue_ai) | ✅ | [↗](https://x.com/liyue_ai/status/2097336230078013598) |
| [The Quiet Crossing exploration quest](entries/the-quiet-crossing-exploration-quest.md) | [:@Motion_Viz](https://x.com/Motion_Viz) | ✅ | [↗](https://x.com/Motion_Viz/status/2096574297703637111) |
| [Warcraft-inspired character scene in Unity](entries/warcraft-inspired-character-scene-in-unity.md) | [:@luccacerf](https://x.com/luccacerf) | ✅ | [↗](https://x.com/luccacerf/status/2096308567863079420) |
| [A Godot Roguelike Level](entries/a-godot-roguelike-level.md) | [:@op7418](https://x.com/op7418) | — | [↗](https://x.com/op7418/status/2096494840431386950) |
| [Action & arcade](entries/action-arcade.md) | [:@CtrlAltDwayne](https://x.com/CtrlAltDwayne) | — | [↗](https://x.com/CtrlAltDwayne/status/2097499157967818780) |
| [Arena Zero iPhone Fighting Game](entries/arena-zero-iphone-fighting-game.md) | [:@higgsfield_ai](https://x.com/higgsfield_ai) | — | [↗](https://x.com/higgsfield_ai/status/2097470354897740109) |
| [Rocket League Style Game](entries/rocket-league-style-game.md) | [:@LLMJunky](https://x.com/LLMJunky) | — | [↗](https://x.com/LLMJunky/status/2096028790925488452) |
| [RPGs & adventures](entries/rpgs-adventures.md) | [:@TheRohanVarma](https://x.com/TheRohanVarma) | — | [↗](https://x.com/TheRohanVarma/status/2096744577332068549) |
| [Sunwake Sailing Game](entries/sunwake-sailing-game.md) | [:@Dimillian](https://x.com/Dimillian) | — | [↗](https://x.com/Dimillian/status/2096863961203220741) |

<a id="multiplayer-battle"></a>
## ⚔️ Multiplayer & Battle (16)

> 对战、卡牌、共斗。单 prompt 能不能扛住规则博弈

| 案例 | 作者 | Prompt | 原帖 |
|---|---|---|---|
| [Kaiju city battle](entries/kaiju-city-battle.md) | [:@majidmanzarpour](https://x.com/majidmanzarpour) | ✅ | [↗](https://x.com/majidmanzarpour/status/2096251574918013135) |
| [Trading-card battle game loop](entries/trading-card-battle-game-loop.md) | [:@FaryaBlender3D](https://x.com/FaryaBlender3D) | ✅ | [↗](https://x.com/FaryaBlender3D/status/2096555856204644550) |
| [Age of Empires IV on Apple Silicon](entries/age-of-empires-iv-on-apple-silicon.md) | [:@marc_ibrahim](https://x.com/marc_ibrahim) | — | [↗](https://x.com/marc_ibrahim/status/2096365209111724235) |
| [asked GPT 6 Astra to build a knight vs mage ](entries/asked-gpt-6-astra-to-build-a-knight-vs-mage-battle.md) | [:@LexnLin](https://x.com/LexnLin) | — | [↗](https://x.com/LexnLin/status/2096799556478357923) |
| [Astral War](entries/astral-war.md) | [:@0xRishi](https://x.com/0xRishi) | — | [↗](https://x.com/0xRishi/status/2096079660605997264) |
| [Benchmarks & Cost Tests](entries/benchmarks-cost-tests.md) | [:@i](https://x.com/i) | — | [↗](https://x.com/i/status/2096030719156089029) |
| [Create a visually spectacular, highly polish](entries/create-a-visually-spectacular-highly-polished-3d-s.md) | [:@AiBattle_](https://x.com/AiBattle_) | — | [↗](https://x.com/AiBattle_/status/2096056285896536086) |
| [Experimental & multiplayer](entries/experimental-multiplayer.md) | [:@antonioleivag](https://x.com/antonioleivag) | — | [↗](https://x.com/antonioleivag/status/2096509898481651770) |
| [Godot 索尼克 Max vs Medium](entries/godot-索尼克-max-vs-medium.md) | [:@AiBattle_](https://x.com/AiBattle_) | — | [↗](https://x.com/AiBattle_/status/2095994051354919049) |
| [Gogh Strike](entries/gogh-strike.md) | [:@petergostev](https://x.com/petergostev) | — | [↗](https://x.com/petergostev/status/2096013280519016608) |
| [Halo-Inspired Tesana FPS](entries/halo-inspired-tesana-fps.md) | [:@VikiingAI](https://x.com/VikiingAI) | — | [↗](https://x.com/VikiingAI/status/2095598026916049024) |
| [Known but Unpublished](entries/known-but-unpublished.md) | [:@paojiaofty](https://x.com/paojiaofty) | — | [↗](https://x.com/paojiaofty/status/2096830622341976467) |
| [Rogue Arena Prototype](entries/rogue-arena-prototype.md) | [:@jumperz](https://x.com/jumperz) | — | [↗](https://x.com/jumperz/status/2096600055301984738) |
| [Strategy & simulation](entries/strategy-simulation.md) | [:@echo3042](https://x.com/echo3042) | — | [↗](https://x.com/echo3042/status/2096123409029886250) |
| [Universe Duel](entries/universe-duel.md) | [:@hayashimon1](https://x.com/hayashimon1) | — | [↗](https://x.com/hayashimon1/status/2096255665778069957) |
| [游戏与可玩原型](entries/游戏与可玩原型.md) | [:@imoutoftokensFR](https://x.com/imoutoftokensFR) | — | [↗](https://x.com/imoutoftokensFR/status/2096202083561054342) |

<a id="agent-plays"></a>
## 🤖 Agent Plays (9)

> 模型亲自上手玩游戏 —— Computer Use 的边界在哪

| 案例 | 作者 | Prompt | 原帖 |
|---|---|---|---|
| ⭐ [我让 GPT-6 Astra 做了个游戏，然后让它自己玩、自己录屏，再剪一段开发实录。](entries/我让-gpt-6-astra-做了个游戏然后让它自己玩自己录屏再剪一段开发实录.md) | [:@Nin19536](https://x.com/Nin19536) | — | [↗](https://x.com/Nin19536/status/2097163153276796943) |
| ⭐ [语音通关《杀戮尖塔 2》](entries/语音通关杀戮尖塔-2.md) | [:@coolish](https://x.com/coolish) | — | [↗](https://x.com/coolish/status/2096195104809873710) |
| [Create an Interactive Soft-Body Slime with T](entries/create-an-interactive-soft-body-slime-with-threejs.md) | [:@Delroy715](https://x.com/Delroy715) | ✅ | [↗](https://x.com/Delroy715/status/2096793432987464010) |
| [AGI is here](entries/agi-is-here.md) | [:@KushDaddyOG101](https://x.com/KushDaddyOG101) | — | [↗](https://x.com/KushDaddyOG101/status/2097076033564381458) |
| [ASTRA WRITES THE GAME. HIGGSFIELD DRESSES IT](entries/astra-writes-the-game-higgsfield-dresses-it-you-ju.md) | [:@rimtoln](https://x.com/rimtoln) | — | [↗](https://x.com/rimtoln/status/2096937327645929938) |
| [everyone is using GPT-6 Astra to make games.](entries/everyone-is-using-gpt-6-astra-to-make-games-i-had-.md) | [:@DeRonin_](https://x.com/DeRonin_) | — | [↗](https://x.com/DeRonin_/status/2096567918859354155) |
| [GPT-6 Astra is truly insane](entries/gpt-6-astra-is-truly-insane.md) | [:@jaykhan](https://x.com/jaykhan) | — | [↗](https://x.com/jaykhan/status/2096775247328608401) |
| [I had my “touch of AGI” moment yesterday](entries/i-had-my-touch-of-agi-moment-yesterday.md) | [:@DanielGri](https://x.com/DanielGri) | — | [↗](https://x.com/DanielGri/status/2096852983468216790) |
| [只看屏幕通关《火红》](entries/只看屏幕通关火红.md) | [:@Clad3815](https://x.com/Clad3815) | — | [↗](https://x.com/Clad3815/status/2095596013168050551) |

---

## 致谢（聚合来源）

本目录由以下 awesome list 聚合去重而来 —— 它们是发现 X 帖子的地图，record 本身永远回到 X：

- [`BeatAPI/awesome-3d-prompts`](https://github.com/BeatAPI/awesome-3d-prompts)
- [`LuxRealGrowth/awesome-astra-video-prompts`](https://github.com/LuxRealGrowth/awesome-astra-video-prompts)
- [`MartinDelophy/awesome-gpt-6-astra`](https://github.com/MartinDelophy/awesome-gpt-6-astra)
- [`TripoGrowthLab/awesome-astra-prompts`](https://github.com/TripoGrowthLab/awesome-astra-prompts)
- [`archorfight/awesome-gpt-6-astra`](https://github.com/archorfight/awesome-gpt-6-astra)
- [`carpentry-liu/awesome-astra-3d`](https://github.com/carpentry-liu/awesome-astra-3d)
- [`helloianneo/awesome-gpt6-astra`](https://github.com/helloianneo/awesome-gpt6-astra)
- [`magiccreator-ai/awesome-gpt-6-astra`](https://github.com/magiccreator-ai/awesome-gpt-6-astra)
- [`xianyu110/awesome-gpt-6-astra`](https://github.com/xianyu110/awesome-gpt-6-astra)
- [`zlxxlz1026/awesome-gpt-6-astra-casebook`](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook)

