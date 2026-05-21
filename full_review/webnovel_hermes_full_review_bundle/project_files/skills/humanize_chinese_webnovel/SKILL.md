# Skill 名称: humanize_chinese_webnovel

## 所属流程环节
降 AI 腔 + 对白优化

## 适用场景
审稿发现 AI 腔过重时，对正文进行针对性去 AI 腔改写。

## 输入
- 待改正文 chapter_{N}_draft.md
- 审稿报告 chapter_{N}_review.yaml
- templates/deai_rules/（完整规则库）
- templates/prompts/humanize.md

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/manuscript/polished/chapter_{N}_polished.md
- 改写说明（嵌入 polished 文件顶部）

## 执行步骤
1. 读取审稿报告，重点关注 ai_flavor_level 的 issue/suggestion
2. 读取 deai_rules 逐条对照原文
3. 逐句检查禁止句式（仿佛、似乎、他感到、总结性旁白等）
4. 发现 AI 腔句式：删除或替换为具体动作/对话
5. 检查对话差异化：确保每个角色口吻可区分
6. 写入 polished 目录

## 质量标准
- 改写后 ai_flavor_level ≤ 4
- 改写不改变核心情节推进
- 不改掉原创性强的句子

## 常见失败情况
- 改完更 AI 腔了：回退到原始 draft，只做局部替换
- 对话仍同质化：针对每个角色分别重写 2-3 句典型台词

## 禁止事项
- 禁止删除推进情节的核心内容
- 禁止改成文绉绉的古风
- 禁止在正文中解释为什么这样改

## 示例输出
polished/chapter_001_polished.md — 减少 80% AI 句式，对话加口吻差异
