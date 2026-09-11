# P6 · Co-Creative Design Partner 🎨

> **难度 ★** · 不下完整 spec，先让模型当策划，你当制作人拍板 —— "Design a game with me"。适合还不知道要做什么的阶段（案例：Windhaven 沿海冒险、Mini World 亲子探索）。

## 玩法是什么

对话式共建：模型提案 → 你砍/留 → 模型细化 → 落成可玩版本。Prompt 的关键是**留下你的决策权**并要求它一次只推进一层。

## Prompt 模板

```text
Design a game with me. Do not write code yet.

Round 1 — you propose: 3 game concepts, each 2 sentences (fantasy + core loop).
Wait for my pick.

Round 2 — I pick one. You expand ONLY that one: pillars (max 3), core loop
diagram in text, session length, and the riskiest assumption.

Round 3 — we pressure-test the risk. Then, and only then, you produce the
full build prompt for <ENGINE>.

One round per message. Ask me before deciding anything that changes scope.
```

## 翻车点

- **模型一路狂奔**：不设 round 限制时它会把设计+实现一口气做完，中间不给你拍板点 —— "Wait for my pick" 每个 round 都要写。
- **提案同质化**：要"3 个互相不同的方向"，而不是同一玩法三个皮。
- **过早进入实现**：明确 "Do not write code yet"。
