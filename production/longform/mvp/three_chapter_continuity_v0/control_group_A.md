# Control Group A: Current Baseline

A 组代表当前逐章生成基线。

## 使用能力

- 现有 chapter beat。
- 粗粒度 runtime canon。
- 粗粒度 chapter commit / writeback。
- 常规 Reviewer / Polisher 边界。

## 不使用能力

- `chapter_card`。
- `state_delta`。
- ledger reducers。
- `scene_agency_packet`。
- Story Orchestrator Lite。
- Renderer blocker。

## 预期优势

- 成本低。
- 链路简单。
- 不容易被 schema 压硬。

## 预期失败

- 章节单看可读，但连起来断。
- 关系债容易蒸发。
- 信息状态可能错乱。
- 读者问题被遗忘或被公告式解释。
- 后果靠 summary 粗略继承。

## 评价用途

A 组不应被故意削弱。它是当前真实基线，用来判断 B / C 是否值得引入额外结构成本。
