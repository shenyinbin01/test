# Skill 名称: generate_chapter_outline

## 所属流程环节
大纲规划 + 章节规划

## 适用场景
Story Bible 生成完毕后，为整个项目或当前卷生成前 N 章的章节大纲。

## 输入
- MASTER_SETTING.yaml
- 规划章节数量 N
- templates/prompts/chapter_outline.md（Prompt 模板）

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/outlines/chapters_001_{N}.yaml

## 执行步骤
1. 读取 MASTER_SETTING.yaml 获取角色和世界观
2. 加载 chapter_outline.md 模板
3. 调用 DeepSeek 或使用 mock 数据生成 N 章大纲
4. 写入 outlines/chapters_001_{N}.yaml
5. 验证每章包含 number, title, conflict, hook

## 质量标准
- 每章必须有不同的核心冲突
- 每章钩子必须让人想读下一章
- 章节之间必须有情节连续性

## 常见失败情况
- 生成章节内容重复：重新规划，每章指定不同冲突领域
- 钩子软弱：基于 deai_rules 修正钩子强度

## 禁止事项
- 禁止在无 Story Bible 的情况下生成大纲
- 禁止生成超过项目合理章节数的规划
- 禁止生成与世界观矛盾的冲突

## 示例输出
outlines/chapters_001_030.yaml — 30 章大纲，每章有冲突和钩子
