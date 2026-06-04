# Human Texture Real Chain Validation — Run Config

## 执行日期
2026-06-04

## 模型与参数

| 参数 | 值 |
|------|-----|
| 模型 | deepseek-v4-pro |
| Provider | deepseek |
| Temperature | 默认（未显式覆盖） |
| max_tokens | 默认（未显式覆盖） |
| 执行方式 | Hermes 调度，Hermes（运行于 DeepSeek）生成 Planner/Writer/Reviewer 输出 |
| seed 一致性 | **无法保证** — DeepSeek API 不支持固定 seed 参数，A/B 两组先后调用 |

## 分支信息

| 组别 | 分支 | Skill Pack 版本 | Human Texture |
|------|------|----------------|---------------|
| A (baseline) | main | 原始版本（规则 1-4，14 维度） | ❌ 关闭 |
| B (experiment) | experiment/human-texture-skill-pack-v0 | 实验版本（规则 1-5，14 维度 + HT gate） | ✅ 开启 |

## 验证样本

| 样本 | 节点 | 验证重点 |
|------|------|----------|
| C4 | 柳青砚关系节点 | 苏衍撒谎、羞耻/回避、柳青砚失望、关系债 |
| C3 | 饭堂/矿洞信息露出节点 | 信息载体、场景阻力、非系统公告式揭示 |

## 任务格式
每样本每组均执行：
1. Planner → 生成 chapter beat
2. Writer → 生成正文草稿（目标 2500-3000 字）
3. Reviewer → 生成审稿报告

## 约束
- 不启动 Polisher 链路
- 不从 corpus/dachengqi 读取
- 不修改 Phase 8 craft_assets
- 不新增 approved_patterns
- DeepCode/Codex 不参与正文生成

## A/B 差异确认
两组唯一差异：Skill Pack 分支（main vs experiment/human-texture-skill-pack-v0）
- Planner: 实验分支可输出 human_texture block
- Writer: 实验分支执行规则五（Human Texture compact brief）
- Reviewer: 实验分支执行 Human Texture gate
