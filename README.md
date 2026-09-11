# awesome-gpt6-astra-game-prompts

> A curated, **reproducible** collection of prompts that turn **GPT-6 Astra** into playable 3D games.

[![validate](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml)
[![license: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![model: GPT-6 Astra](https://img.shields.io/badge/model-gpt--6--astra-6f42c1.svg)](https://platform.openai.com/docs/models)

GPT-6 Astra shipped on **2026-09-03**. There are already excellent `awesome-gpt-image-*` prompt
lists for still images — but nothing for the harder problem: getting a language model to emit a
**game that actually runs**. This list is that missing library.

It is not a list of clever one-liners. Every entry is a **recipe**: a pinned model version, the
exact settings, the exact input, the artifacts you should get back, and a checklist to prove it
worked. Reproducible means the next person gets an equivalent result.

---

## What "reproducible" means here

A prompt is only in this list if it satisfies the **reproducibility contract** — four things,
all present:

| Clause | What it pins down |
| --- | --- |
| **Model** | The exact model and version the result was produced with (`gpt-6-astra`, dated), because behavior drifts between releases. |
| **Settings** | System prompt, temperature, top-p, seed (where supported), tool configuration, and output budget. |
| **Input** | Everything needed before the prompt runs — runtime, deps, starting files, assets. |
| **Acceptance** | The artifacts expected back, plus a pass/fail checklist a human or CI can actually run. |

Randomness is not the enemy of reproducibility — *undocumented* randomness is. Where a prompt
produces procedural output, it takes a **seed** and records it. Where a model has no seed control,
the recipe constrains the degrees of freedom tightly enough that the acceptance checks pass.

See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for the full rationale and the three
verification levels.

---

## Contents

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

---

## 🕹️ Showcase & Playbooks（新增）

本项目在 `prompts/`（可复现配方）之外新增两层，不改变原有可复现契约：

| 目录 | 是什么 | 数据 |
|---|---|---|
| [`showcase/`](showcase/README.md) | **X 真实玩法案例**：115 条，34 条带 prompt 原文，全部回链 X 原帖。分类 + 推荐榜。 | [`showcase/data.json`](showcase/data.json) |
| [`playbooks/`](playbooks/README.md) | **玩法配方手册（skill 层）**：6 个可复用套路，从案例提炼，含模板/变量/翻车点 | 纯 markdown |
| [`web/`](web/index.html) | **网页端**：消费 `showcase/data.json` 的案例馆页面（repo 与网页共建） | 静态页 |

收录原则（详见 [showcase/README.md](showcase/README.md)）：**X 是唯一 record source**；prompt 只可能来自
帖子里或帖子下面；没有 prompt 也照收；从所有 awesome list 聚合、按原帖去重；分类 + 推荐优先于大而全。

---

## Quick start

```bash
git clone https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts.git
cd awesome-gpt6-astra-game-prompts

# pick a recipe
cat prompts/full-games/astra-3d-001-endless-runner.md

# paste its "The prompt" block into GPT-6 Astra with the listed settings,
# then verify the result against its acceptance checklist.
```

Most full-game recipes produce a **single self-contained `index.html`**. Save it, double-click it,
and you are playing. No install, no build step, no server.

---

## Anatomy of an entry

Every file in `prompts/` follows the same shape:

```markdown
---
id: astra-3d-001
title: Endless Runner
category: full-games
slug: endless-runner
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: Three.js
difficulty: beginner
verified: tested
verified_by: yangzhou-chaofan
verified_on: 2026-09-10
tags: [threejs, webgl, arcade, endless-runner, single-file]
license: CC0-1.0
---

# Endless Runner

> One sentence on what you get.

## What you get        — the deliverable and why it is worth using
## Before you start    — inputs, runtime, assets, anything to install
## The prompt          — the exact text to paste, in one fenced block
## Settings            — the frontmatter settings, explained
## Expected output     — artifacts and their shape
## Verify it worked    — a pass/fail acceptance checklist
## Tune it             — the one or two variables worth changing
## Where it drifts     — known failure modes and how the recipe avoids them
## Provenance          — where the technique came from
```

The frontmatter is machine-checked. `scripts/validate_prompts.py` runs in CI on every pull request
and fails the build if a field is missing, an id is duplicated, a slug disagrees with its filename,
or a category disagrees with its folder.

---

## Verification levels

| Badge | Meaning |
| --- | --- |
| ✅ **tested** | A maintainer ran the recipe on the pinned model version and every acceptance check passed. Logged in `Provenance`. |
| 🧪 **community** | Submitted and run by a contributor, not yet reproduced by a maintainer. Still must satisfy the reproducibility contract. |
| 📝 **draft** | Format-complete and reviewed, but not yet run end-to-end. Marked clearly so nobody is misled. |

A prompt graduates from draft → community → tested by being *reproduced by someone other than its
author*. That is the whole point of the list.

---

## Repository layout

```
.
├── prompts/                 # the recipes, grouped by category
│   ├── full-games/
│   ├── systems/
│   ├── assets/
│   ├── levels/
│   └── ui/
├── schema/prompt.schema.json  # machine-readable frontmatter contract
├── scripts/
│   ├── validate_prompts.py    # CI: checks every recipe against the schema
│   └── build_index.py         # regenerates the tables in this README
├── templates/PROMPT_TEMPLATE.md
├── docs/REPRODUCIBILITY.md    # what the contract means, in depth
├── CONTRIBUTING.md
└── .github/                   # CI, issue forms, PR template
```

---

## Contributing

New recipes are very welcome — especially reproductions of existing ones on your own machine,
which is what promotes a prompt from *community* to *tested*. Start with
[`templates/PROMPT_TEMPLATE.md`](templates/PROMPT_TEMPLATE.md) and read
[`CONTRIBUTING.md`](CONTRIBUTING.md). Run the validator before you push:

```bash
python3 scripts/validate_prompts.py
```

---

## Disclaimer

This is an unofficial, community project. It is **not affiliated with or endorsed by OpenAI**.

Model identifiers, context limits, pricing and API parameter names change quickly. Every recipe
here records the exact version it was verified against (`model_version` in the frontmatter) — treat
that as a historical record, not a claim about the current API. Before running anything, confirm
model names and supported parameters against the official documentation. If a newer release changes
behavior, open an issue and *add* a recipe for it rather than silently editing the existing one.

## License

Released under [CC0-1.0](LICENSE) — public domain. Take the recipes, remix them, ship them, no
attribution required. (Attribution is still nice.)
