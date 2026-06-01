# Step 3B Input Coverage Report

> 生成时间: 2026-06-01T15:00:00
> 生成方式: 程序聚合（基于 Step 3B 脚本的输入/输出日志）

## 1. 输入源

| 输入文件 | 状态 | 说明 |
|----------|------|------|
| `production/phase8/corpus/dachengqi/chapter_cards/` | ✅ 已读取（774/774） | 全量 YAML 文件 |
| `production/phase8/audit/dachengqi/chapter_fact_audit_report.md` | ✅ 已读取 | 用于参考验证 |
| `production/phase8/audit/dachengqi/chapter_card_quality_report.md` | ✅ 已读取 | 用于参考验证 |
| 旧 Step 3 volume_structure_report.md | ✅ 仅参考阶段划分思路 | 不依赖内容 |
| 旧 reverse_story_bible / character_cards / reader_debt_lifecycle / hook_payoff_map | ❌ 未使用 | 严格禁止 |

## 2. 覆盖率总览

| 维度 | 数值 |
|------|------|
| chapter_card 总数 | 774 |
| 实际读取 chapter_card 数量 | 774 |
| full_chapter_spine 覆盖章节数 | 774 |
| refined_volume_structure 覆盖章节数 | 774 |
| arc_mechanism_index 阶段机制-覆盖章节数 | 774 |
| 未进入任何阶段的章节数 | 0 |
| 只被统计未进入机制分析的章节数 | 0 |
| 是否存在"读取全量但只喂采样"的情况 | **否** |

## 3. 各阶段覆盖明细

| 阶段 | 章节范围 | 章节数 | 进入 LLM 方式 |
|------|----------|--------|--------------|
| S01 | 1-95 | 95 | 该95章完整 chapter_card 数据 + spine |
| S02 | 96-196 | 101 | 该101章完整 chapter_card 数据 + spine |
| S03 | 197-289 | 93 | 该93章完整 chapter_card 数据 + spine |
| S04 | 290-386 | 97 | 该97章完整 chapter_card 数据 + spine |
| S05 | 387-452 | 66 | 该66章完整 chapter_card 数据 + spine |
| S06 | 453-482 | 30 | 该30章完整 chapter_card 数据 + spine |
| S07 | 483-577 | 95 | 该95章完整 chapter_card 数据 + spine |
| S08 | 578-638 | 61 | 该61章完整 chapter_card 数据 + spine |
| S09 | 639-675 | 37 | 该37章完整 chapter_card 数据 + spine |
| S10 | 676-757 | 82 | 该82章完整 chapter_card 数据 + spine |
| S11 | 758-774 | 17 | 该17章完整 chapter_card 数据 + spine |

### 3.1 跨阶段汇总（LLM 一次输入全量）

| 产物 | 输入章节范围 | 章节数 | 输入内容 |
|------|-------------|--------|---------|
| refined_volume_structure | 1-774 | 774 | 全量774章 spine 摘要（每章一行） + 阶段边界 |
| protagonist_engine | 1-774 | 774 | 全量 spine 摘要 + 11阶段分析摘要 |
| character_function_map | 1-774 | 774 | 全量 spine 摘要 + 人物出场统计 |
| candidate_pool | 1-774 | 774 | 11阶段分析完整内容 |

## 4. 阶段检测逻辑

阶段边界由程序基于以下 signals 自动检测（非人工、非随机）：
- `chapter_function` 变化（如"引入"→"推进"→"揭示"→"高潮"→"过渡"）
- `world_state_change` 变化
- `protagonist_state_change` 密集度
- 主角出场频率变化
- 主要角色出场变化
- hook/debt 开启-兑现模式变化
- chapter_number 连续性保证

检测参数：min_stages=11, max_stages=15, max_chapters_per_stage=160

## 5. 验证口径

| 检查项 | 结果 |
|--------|------|
| full_chapter_spine 覆盖 774/774 | ✅ 是 |
| refined_volume_structure 覆盖 774/774 | ✅ 是 |
| 每章归属到某个阶段 | ✅ 是 |
| 不存在"随机采样"冒充 | ✅ 是 |
| 不存在"只喂统计摘要不喂数据" | ✅ 否——arc_mechanism 喂的是完整 chapter_card 数据 |
