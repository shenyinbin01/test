# Phase 8: 整本书逆向压缩与技法蒸馏系统

## 定义

Phase 8 是整本书逆向压缩与技法蒸馏系统。
它的目标不是写读后感，也不是仿写原作，而是从合法来源完整小说中反推出人能审计的故事工程资产，并将可复用技法反哺现有 Planner / Writer / Reviewer / Polisher。

## 七个核心交付物

1. **chapter_fact_audit_report.md** — 逐章事实审计表，老板能看懂的章节级压缩证据
2. **reverse_story_bible.md** — 逆向故事圣经，从正文反推的故事工程蓝图
3. **character_cards/** — 人物工程卡，不写人设，写人物在故事中的功能和弧线
4. **volume_structure_report.md** — 分卷结构报告，展示全书节奏、高潮、压力系统
5. **reader_debt_lifecycle.md / hook_payoff_map.md** — 读者债生命周期和钩子兑现地图
6. **craft_assets_candidate_report.md** — 技法资产候选报告，从原作中蒸馏的可复用技法
7. **skill_injection_plan.md** — Skill 反哺方案，将 approved 技法注入正式写作链路

> 机器层文件（如 chapter_card.yaml、manifest.yaml、schema）只是底层证据。
> Phase 8 的主验收对象是人能审计的故事工程资产。

## 核心原则

1. **整本书是最小有效认知单位。** 只看单章无法判断故事结构。
2. **章节只是工程处理单元。** 所有核心判断必须基于整本书视角。
3. **所有核心判断必须能追溯 evidence。** 每个结论都要能说清来自哪一章哪一段。
4. **无证据内容必须标 unknown。** 不能脑补，不能假装知道。
5. **不复制原作表达、人物、桥段、设定、专属机制。** 只抽取抽象结构和技法。
6. **技法资产必须先进入 candidate，经审核后才能进入 approved。**
7. **Writer 不得接触原文、原作证据、未审核技法。**
8. **Reviewer 必须检查技法落实和原作污染风险。**

## MVP 流程

```text
source_meta + full_book
→ split chapters
→ manifest
→ chapter_cards
→ chapter_fact_audit_report
→ reverse_story_bible
→ character_cards
→ volume_structure_report
→ reader_debt_lifecycle / hook_payoff_map
→ craft_assets_candidate_report
→ approved / rejected
→ skill_injection_plan
→ validation_report
```

## 目录结构

```text
production/phase8/
├── README.md
├── input/                # 原始输入存放
├── corpus/               # 处理中的语料（每本书一个子目录）
├── audit/                # 审计报告（每本书一个子目录）
├── reverse_assets/       # 逆向工程资产（每本书一个子目录）
├── craft_assets/         # 技法资产（candidate / approved / rejected）
├── skill_injection/      # Skill 反哺方案
├── validation/           # 校验报告
├── schemas/              # 所有 schema 定义
├── templates/            # 所有 template 定义
├── prompts/              # LLM prompt 模板
└── examples/             # toy 示例
```

## 安全约束

- Writer 禁止接触原文
- Writer 禁止接触 source evidence
- Writer 禁止接触 candidate 技法
- 只有 approved 技法能注入正式写作链路
- 任何技法卡必须包含「原作污染风险」评估
- 任何技法卡必须包含「禁止复制内容」声明
