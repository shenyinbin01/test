# Skill 名称: review_chapter

## 所属流程环节
连贯性检查 + 验收检查 + 钩子/爽点/风格评估

## 适用场景
章节草稿完成后，从十个维度评估质量，决定是否进入润色阶段。

## 输入
- 待审草稿 chapter_{N}_draft.md
- 该章的 chapter_outline 和 chapter_beat
- templates/deai_rules/
- templates/prompts/chapter_review.md

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/reviews/chapter_{N}_review.yaml

## 执行步骤
1. 读取草稿正文
2. 读取 outline 和 beat 作为对比基准
3. 加载 chapter_review.md 模板
4. 依次评估 tension, pacing, dialogue, character_consistency, hook,
   world_consistency, emotion_delivery, prose_quality, readability, ai_flavor_level
5. 每个维度给出 score（1-10）+ issue（具体原文摘录）+ suggestion（修改建议）
6. 给出 verdict：passed / failed + overall_score + critical_issues + minor_issues
7. 写入 reviews/chapter_{N}_review.yaml

## 质量标准
- 每个 issue 必须有具体的原文摘录
- ai_flavor_level ≤ 4 才通过
- 没通过必须有 critical_issues

## 常见失败情况
- 审稿过于笼统：要求每个 issue 必须引用原文
- 评分偏差：与 deai_rules 逐条对照确认

## 禁止事项
- 禁止只说"写得不错"不指出问题
- 禁止只打分不写修改建议

## 示例输出
reviews/chapter_001_review.yaml — 10 维度评分，ai_flavor_level=6，未通过，需润色
