# Renderer Skill Changelog

## v0 — 2026-06-10 (snapshot at ch001_v1 generation)

### 快照说明

此版本是生成 `production/renderer_skill_lab/inbox/expansions/ch001_v1.md` 时实际使用的 Renderer Skill。事后未做任何美化或补充。

### 规则来源

| 规则 | 来源 |
|------|------|
| 规则一（事件驱动开场） | 用户任务指令第六节 + webnovel_writer SKILL.md 规则一 |
| 规则二（场景优先于说明） | 用户任务指令第六节"优先写"清单 |
| 规则三（字数 2500-3500） | 用户任务指令第五节字数要求 |
| 禁止 8 种写法 | 用户任务指令第六节"严格避免"清单 |
| 禁止项 | 用户任务指令第五节 + 第六节汇总 |

### 与下游 Skill 的关系

此 Renderer Skill 在生成 ch001_v1 时叠加了以下非 Renderer Skill Lab 资产：
- `/home/agentuser/.hermes/skills/webnovel/webnovel_writer/SKILL.md`（通用网文写作约束）
- Phase 8 `reverse_story_bible.md`（世界观连续性确认）

因此 ch001_v1 不是纯 Renderer Skill v0 产物。详见 `cases/ch001/00_generation_manifest.md`。

### 已知局限

- 未定义章节结构（场景数、节奏分布）
- 未定义角色声音区分规则
- 未定义网文钩子/爽点密度要求
- 未定义信息露出规范

以上将在后续 Skill Delta 提取中补充。
