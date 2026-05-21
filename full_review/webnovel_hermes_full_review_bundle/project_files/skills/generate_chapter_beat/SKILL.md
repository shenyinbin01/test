# Skill 名称: generate_chapter_beat

## 所属流程环节
章节规划

## 适用场景
有了章节大纲和写作上下文后，将一章拆解为具体的场景序列。

## 输入
- chapter_outline（单章大纲）
- preflight_context
- templates/prompts/chapter_beat.md

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/outlines/beats/chapter_{N}.yaml

## 执行步骤
1. 读取该章的 chapter_outline
2. 读取 preflight_context
3. 加载 chapter_beat.md 模板
4. 调用 DeepSeek 或 mock 生成场景序列
5. 写入 beats/chapter_{N}.yaml
6. 验证至少 4 个场景，每个场景有明确叙事功能

## 质量标准
- 每章 4-6 个场景
- 每个场景有明确叙事功能
- 情绪曲线有起伏
- 高潮在倒数第 2 或倒数第 3 个场景

## 常见失败情况
- 场景数不足：重新规划，插入过渡场景
- 情绪曲线平：调整场景顺序，制造落差

## 禁止事项
- 禁止所有场景同一种冲突类型
- 禁止高潮在最后一个场景

## 示例输出
beats/chapter_001.yaml — 5 个场景，从接单开始到章尾医院归零标签
