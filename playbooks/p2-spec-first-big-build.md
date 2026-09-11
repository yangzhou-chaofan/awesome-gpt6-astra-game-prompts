# P2 · Spec-First Big Build 🏗️

> **难度 ★★** · 大于一把流的项目（完整 RPG / 开放世界 / 多系统）不要一次 prompt 写完 —— 先让它写规格书，再照规格施工。多来源案例验证的稳态做法。

## 玩法是什么

两段式：
1. **规格段**：让模型把需求整理成 `SPEC.md` 并**存进项目目录**（不是聊天消息）；
2. **施工段**：新会话/新指令让它读 SPEC 按章施工，验收锚在 SPEC 编号上。

案例出处：TripoGrowthLab 精选里的 "THE FULL SPEC. SAVE IT AS A FILE..." 模板；xianyu110 合并清单中多个大型 3D 项目采用同一骨架。

## 什么时候用

- 项目超过 1 个核心循环（有存档/多关卡/多系统）
- 上下文会跨多个会话（今天做一半明天继续）
- 需要回滚或换模型版本重跑（SPEC 是版本化的真理源）

## Prompt 模板

**第一段 · 生成规格**

```text
We are building <PROJECT>. Before any code, write the full spec.

Output: save as SPEC.md in the project folder (not as a chat message).

SPEC.md must contain, numbered:
1. One-line fantasy / player promise
2. Core loops (max 3), each with input → feedback → reward
3. Systems list with dependencies (what blocks what)
4. Milestones M1..Mn, each independently playable
5. Acceptance checks per milestone (can-fail statements)
6. Asset & data formats (file names, schemas)
7. Out-of-scope list (what we are NOT building)

Rules: prefer small and finished over big and rough. Any system not in the
spec does not exist. After writing SPEC.md, stop and wait for review.
```

**第二段 · 按规格施工**

```text
/goal build this in <ENGINE>, read SPEC.md and follow it exactly,
especially sections <N> and <M>. Work only inside the project folder.
Ship milestone <Mi> first; run its acceptance checks and paste results
before moving on.
```

## 变量

| 变量 | 说明 |
|---|---|
| `<PROJECT>` | 一句话项目定义 |
| `<ENGINE>` | three.js / Unity / Godot（Unity/Godot 需 Computer Use 或 MCP） |
| `<N>, <M>` | 施工时最关键的两个章节号（一般是核心循环 + 验收） |
| `<Mi>` | 当前里程碑 |

## 翻车点

- **SPEC 写完不落盘**：模型把 SPEC 输出在聊天里，下个会话就丢 —— "save as a file, not as a chat message" 是硬约束。
- **施工段自由发挥**：锚定章节号（"sections 9 and 10"）并要求"spec 外不存在"。
- **里程碑不可玩**：M1 必须是能跑的最小切片，否则中途无法验收。
