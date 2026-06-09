# 上一轮 real_chain_validation 作废说明

## 作废对象

`production/human_texture/real_chain_validation/`（commit `4aa0229`）

## 作废原因

上一轮 real_chain_validation 在生成 baseline Writer 输出时，可能参考了仓库中已有的章节草稿（`chapter_003_draft.md`、`chapter_004_draft.md`）以及 MVP/dry run/regression 的已有改写文本作为隐式模板。

这违反了 A/B 验证的核心原则：两组应只差 Skill Pack 分支，不能引入"已有正文作为参考"这个额外变量。

## 本轮改进

1. 使用独立 worktree 隔离两个分支（`/tmp/ht_main`、`/tmp/ht_exp`）
2. 只从干净 brief 出发生成，不参考任何已有正文
3. 输出路径独立：`production/human_texture/real_chain_validation_rerun/`

## 旧产物状态

- 旧产物保留在 `real_chain_validation/`，不删除
- 旧产物**不作为 PR #1 验收依据**
- 本轮 `real_chain_validation_rerun/` 才是正式验收依据

## 日期

2026-06-04
