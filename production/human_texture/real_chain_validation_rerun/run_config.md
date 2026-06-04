# Human Texture Real Chain Validation Rerun — Run Config

## 执行日期
2026-06-04

## 隔离环境

| 组别 | 目录 | 分支 | Commit |
|------|------|------|--------|
| A (baseline) | `/tmp/ht_main` | main | `980a74e672992cdb463b89fc9406151e8109a9d9` |
| B (experiment) | `/tmp/ht_exp` | experiment/human-texture-skill-pack-v0 | `4aa022991f127f4972b10841395e62a01e604505` |

## 模型与参数

| 参数 | 值 |
|------|-----|
| 模型 | deepseek-v4-pro |
| Provider | deepseek |
| Temperature | 默认（未显式覆盖） |
| max_tokens | 默认（未显式覆盖） |
| seed | **无法保证**（DeepSeek API 不支持固定 seed） |

## 执行方式
Hermes 调度，DeepSeek 生成 Planner/Writer/Reviewer 输出。DeepCode 辅助工程（worktree 准备、目录创建、提交）。

## 验证样本

| 样本 | 节点类型 | Brief 路径 |
|------|---------|-----------|
| C4 | 柳青砚关系节点 | `prompts/c4_task_brief.md` |
| C3 | 饭堂/矿洞信息露出节点 | `prompts/c3_task_brief.md` |

## A/B 一致项确认

| 项 | 一致？ |
|----|--------|
| DeepSeek 模型 | ✅ deepseek-v4-pro |
| Temperature | ✅ 默认 |
| max_tokens | ✅ 默认 |
| 输入 brief | ✅ 同一份 |
| 执行方式 | ✅ Hermes→DeepSeek |
| seed | ⚠️ 无法保证 |
| **Skill Pack** | ❌ **唯一差异：main vs experiment** |

## 干净生成确认

| 检查项 | 状态 |
|--------|------|
| 未使用 chapter_003_draft.md | ✅ |
| 未使用 chapter_004_draft.md | ✅ |
| 未使用 MVP 改写文本 | ✅ |
| 未使用 dry run 改写文本 | ✅ |
| 未使用 regression 改写文本 | ✅ |
| 只从 brief + skill 约束生成 | ✅ |
| 两组使用独立 worktree | ✅ |

## 输出路径
`/tmp/ht_exp/production/human_texture/real_chain_validation_rerun/`

提交到：`experiment/human-texture-skill-pack-v0`
