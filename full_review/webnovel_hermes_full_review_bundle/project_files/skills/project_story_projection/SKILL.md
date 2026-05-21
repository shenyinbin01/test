# Skill 名称: project_story_projection

## 所属流程环节
验收检查

## 适用场景
章节提交后，生成面向用户的"项目状态投影"文件。

## 输入
- MASTER_SETTING.yaml
- runtime_canon.yaml
- 所有已提交的 chapter_commit
- 最新章节正文
- templates/prompts/projection.md

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/.webnovel/state.yaml

## 执行步骤
1. 读取 MASTER_SETTING 获取项目概览
2. 读取 runtime_canon 获取已发生事件
3. 读取最新 commit 获取变更摘要
4. 整理为面向用户可读的状态概览
5. 写入 state.yaml

## 质量标准
- 角色状态有对比感（与上章对比）
- 不使用 YAML/JSON 技术符号展示给用户
- 每个部分不超过 200 字

## 常见失败情况
- 数据源不一致：优先使用 runtime_canon，fallback 到 commit
- 缺少 commit 记录：仅基于 MASTER_SETTING 生成

## 禁止事项
- 禁止输出未经 commit 确认的规划内容
- 禁止加"AI 生成"标记或免责声明

## 示例输出
state.yaml — 显示林砚 (价格: 归零边缘)，当前线索: 父亲医疗费、能力起源
