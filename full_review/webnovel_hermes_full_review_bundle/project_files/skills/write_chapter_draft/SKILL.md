# Skill 名称: write_chapter_draft

## 所属流程环节
章节正文生成

## 适用场景
场景规划完成，需要写出该章可读的网文正文。

## 输入
- chapter_beat（场景序列）
- preflight_context
- templates/prompts/chapter_writer.md
- templates/deai_rules/（完整规则库）

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/manuscript/drafts/chapter_{N}_draft.md

## 执行步骤
1. 读取 chapter_beat 获取场景序列
2. 读取 preflight_context 获取写作上下文
3. 加载 chapter_writer.md 模板
4. 通读 deai_rules 作为写作约束
5. 调用 DeepSeek 或 mock 生成正文
6. 写入 drafts/chapter_{N}_draft.md

## 质量标准
- 字数 2000-3000 字
- 每段对话体现口吻差异
- 章尾钩子明确
- 不使用 general_ai_flavor.md 列举的禁止句式

## 常见失败情况
- 字数不足：补充场景细节
- AI 腔明显：标记后移交 humanize_chinese_webnovel 处理

## 禁止事项
- 禁止写总结性旁白替代场景
- 禁止使用"仿佛""似乎"等模糊词汇
- 禁止章尾使用"预知后事如何"等老套结尾

## 示例输出
drafts/chapter_001_draft.md — 林砚送外卖时第一次看见价格标签
