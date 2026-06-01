# Book Architect Execution Notes

## 1. 生成方式概述

Step 3 Book Architect 通过一个 Python 脚本 `tools/phase8/run_book_architect.py` 实现。脚本的核心策略是：

```
读取全量 chapter_card → 机械聚合（统计+采样）→ 聚合数据+prompt → 调 DeepSeek → 逐个交付物
```

## 2. 是否一次性输入全部 chapter_cards

**否。**

脚本虽然读取了全部 774 张 chapter_card（`load_all_cards` → `aggregate_stats`），但喂给 DeepSeek 的**不是原始 chapter_card 内容**，而是机械聚合后的统计摘要。

聚合摘要包含：
- 章节功能分布（Counter）
- 置信度分布（Counter）
- 主要角色出场频率（Top 40，含首末出场章节）
- 取样章节（头 20 章 / 1/3 处 ±10 / 2/3 处 ±10 / 尾 20 章，约 80 章的 one_sentence + chapter_function + main_events[前3] + ending_pull）
- Hook 取样（每 50 章取 1 个，共约 20 条）
- Debt 取样（每 50 章取 1 个，共约 20 条）

**774 张原始 chapter_card 从未完整进入 LLM 上下文。** LLM 看到的只是经过采样和统计的摘要。

## 3. 分批聚合

是。脚本分四段（头/1/3/2/3/尾）取样，每段约 20 章，总共约 80 章有完整的一条语句信息进入上下文。

角色出场数据是聚合后的列表（角色名 + 出场次数 + 首末章），不是完整章节内容。

## 4. 人物卡生成方式

**按人物名抽取相关章节后单独生成，但抽取的不是章节正文，而是聚合统计中的出场记录。**

具体流程：
1. `aggregate_stats` 中统计 `char_appearances`：从每张 chapter_card 的 `characters_present` 字段中提取角色名，累加出场次数，记录首末出场章号。
2. `generate_characters` 遍历 Top 15 角色，对每个角色单独调用一次 DeepSeek，传入：
   - 角色名
   - 出场次数
   - 首末出场章节
   - 通用 prompt（不含该角色的具体章节内容）

**关键缺陷：** 人物卡生成时，LLM 看不到该角色在各章的具体行为（main_events）、状态变化（protagonist_state_change）、对话（characters_present 只是名字列表）。LLM 只能靠角色名和出场次数推断人物弧光。这就导致人物卡非常单薄——缺乏情节细节支撑，只能写泛泛的角色标签。

## 5. story_bible 生成方式

`generate_bible` 函数将聚合统计（章节功能分布、置信度、角色出场排行、取样章节的 one_sentence + main_events/3 + ending_pull、hook 和 debt 取样）打包成一个 JSON 字符串，加上 prompt，一次调用 DeepSeek 生成。

**不是逐章阅读后归纳，而是基于采样和统计数据推断。**

## 6. confidence 来源

**LLM 自评。** 脚本中 `book_architect.prompt.md` 要求 LLM 输出时附带 `supporting_chapters`、`evidence_refs`、`confidence` 字段。`confidence` 值（high/medium/low）是 LLM 在生成过程中自行判断的，没有任何程序规则来校准。

这解释了为什么最终产出中 `low confidence = 0`——LLM 倾向于给自己写的所有判断标 high，缺乏客观校准机制。

## 7. 使用的脚本

1. **`tools/phase8/run_book_architect.py`** — 核心生成脚本，已复制到本审计包的 `tools_snapshot/` 目录
2. **`scripts/call_deepseek.py`** — 通用 DeepSeek API 调用脚本（通过 `--real` 参数调用真实 API）

## 8. 使用的命令

```bash
cd /opt/webnovel-hermes-wps

# 第一步：character_cards
python tools/phase8/run_book_architect.py \
  --book-id dachengqi --real \
  --skip-bible --skip-volume --skip-debts --skip-hooks

# 第二步：reverse_story_bible
python tools/phase8/run_book_architect.py \
  --book-id dachengqi --real \
  --skip-characters --skip-volume --skip-debts --skip-hooks

# 第三步：volume_structure_report
python tools/phase8/run_book_architect.py \
  --book-id dachengqi --real \
  --skip-bible --skip-characters --skip-debts --skip-hooks

# 第四步：reader_debt_lifecycle
python tools/phase8/run_book_architect.py \
  --book-id dachengqi --real \
  --skip-bible --skip-characters --skip-volume --skip-hooks

# 第五步：hook_payoff_map
python tools/phase8/run_book_architect.py \
  --book-id dachengqi --real \
  --skip-bible --skip-characters --skip-volume --skip-debts
```

## 9. 是否调用了 LLM

**是。** 所有 5 个核心交付物都调用了 DeepSeek API（`--real` 模式），共 6 次调用：
- reverse_story_bible：1 次（max_tokens=8000, timeout=300s）
- character_cards：15 次（每个角色 1 次，max_tokens=2000, timeout=180s）
- volume_structure_report：1 次（max_tokens=8000, timeout=300s）
- reader_debt_lifecycle：1 次（max_tokens=8000, timeout=300s）
- hook_payoff_map：1 次（max_tokens=8000, timeout=300s）

总计 19 次 DeepSeek API 调用。

## 10. 失败重试

脚本中 `call_llm` 参数的 `--retries 1` 表示每个 LLM 调用失败后重试 1 次。实际执行中所有调用均成功，无重试。

## 11. 角色出场数据的准确性

注意：出场次数来自 chapter_card 的 `characters_present` 字段。由于该字段是字符串列表（每章出现则计入一次），非精确角色活跃度度量。例如 chapter_card 中可能将"江离（主角）"和"江离"视为不同字符串，导致计数偏差。

但 Top 15 角色的排序相对可靠。

## 12. 核心缺陷总结

| 缺陷 | 根因 |
|------|------|
| 人物卡单薄 | 只喂了角色名+出场次数，没喂具体章节行为 |
| story_bible 泛泛 | LLM 只看到采样摘要，没看到全量 774 章数据 |
| confidence 全 high | LLM 自评，无校准 |
| reader_debt_lifecycle 压缩过度 | 只看到 20 条 debt 取样，无法判断全书债务结构 |
| hook_payoff_map 覆盖不全 | 同理，只看到 hook 取样 |
