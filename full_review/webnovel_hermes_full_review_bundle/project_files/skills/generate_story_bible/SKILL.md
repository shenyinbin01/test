# Skill 名称: generate_story_bible

## 所属流程环节
角色卡管理 + 世界观管理

## 适用场景
小说项目目录创建完毕后，生成完整的 Story Bible（角色、世界观、故事总纲）。

## 输入
- /data/webnovel-lab/workspace/novels/{project_name}/project.yaml
- templates/prompts/story_bible.md（Prompt 模板）

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/.story-system/MASTER_SETTING.yaml

## 执行步骤
1. 读取 project.yaml，提取项目基础信息
2. 加载 story_bible.md Prompt 模板
3. 调用 DeepSeek（通过 call_deepseek.py 或模拟生成种子数据）
4. 将输出解析为 YAML 并写入 MASTER_SETTING.yaml
5. 验证输出符合 master_setting.schema.yaml 的必填字段

## 质量标准
- 每个角色必须有 name, age, identity, personality, motivation, arc
- 能力规则至少 5 条，每条必须有约束力
- 故事总纲包含起承转合

## 常见失败情况
- DeepSeek 返回格式异常：回退到预设种子数据（mock 模式）
- 字段缺失：补填默认值并记录日志

## 禁止事项
- 禁止写入与 project.yaml 矛盾的数据
- 禁止生成超过 20 个角色（本阶段只需要核心角色）
- 禁止写入无法被后续章节引用的虚设定

## 示例输出
MASTER_SETTING.yaml — 包含主角林砚、世界观规则、价格标签能力限制
