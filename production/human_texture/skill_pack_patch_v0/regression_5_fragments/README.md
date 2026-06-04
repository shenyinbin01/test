# Human Texture Patch v0 Five-Fragment Regression

日期：2026-06-04

分支：`experiment/human-texture-skill-pack-v0`

## 目标

验证实验分支中的 Planner / Writer / Reviewer / Polisher 最小 Human Texture prompt patch，是否能在 5 个已验证片段中稳定复现 compact packet dry run 的效果。

本轮是模拟回归测试，不运行完整五章生成，不启动正式 Polisher 链路，不合并 `main`。

## 被测 patch

- Planner：可生成轻量 `human_texture` block，每章最多 2-3 个 `focus_fields`。
- Writer：把字段转成行为、误读、场景阻力、选择或后果，不逐项显性解释字段。
- Reviewer：输出 `human_texture_review`，判断 `pass_to_polisher` / `return_to_planner` / `return_to_writer`。
- Polisher：gate 未过不得润色；gate 通过后只允许压缩说明、调整句势、保留已有余味。

## 测试片段

1. C4 柳青砚关系节点
2. C3 饭堂 / 矿洞信息露出节点
3. C5 群体公告 / 规则公布节点
4. C4 情绪残留 / 情绪代价节点
5. C4 章尾钩子压过人味节点

## 输出文件

- `planner_blocks.yaml`
- `writer_outputs.md`
- `reviewer_outputs.md`
- `polisher_boundary_check.md`
- `regression_scores.md`
- `regression_result_report.md`

## 通过标准

- 5 个片段中至少 4 个 B 版 Human Texture 平均分 >= 3.8。
- 5 个片段均保留原剧情功能。
- Writer 未逐项显性写字段。
- 未出现明显篇幅膨胀。
- Reviewer 能正确定位退回层级。
- Polisher 没有被要求补人物私心、关系债、信息载体或后果。
- patch 没有干扰既有十四维度 Reviewer 判断。
- Human Texture 没有退化成风景、比喻、口语化或装饰性细节。

## 总结

本轮 5 个片段均通过回归：5/5 B 版平均分 >= 3.8，均保留原剧情功能。Reviewer gate 能稳定分层，Polisher boundary 清晰。建议创建 PR 进入人工审查；暂不建议直接合并 `main`，需先做人工审查和一次真实链路五片段复跑。
