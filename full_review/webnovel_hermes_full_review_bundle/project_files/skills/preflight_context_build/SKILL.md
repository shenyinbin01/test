# Skill 名称: preflight_context_build

## 所属流程环节
连贯性检查 + 对白优化

## 适用场景
写某一章之前，从现有素材中提取最重要的写作上下文。

## 输入
- MASTER_SETTING.yaml
- runtime_canon.yaml（如有）
- 待写章节的 chapter_outline
- templates/prompts/preflight_context.md

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/.webnovel/context/chapter_{N}_context.yaml 或 .md

## 执行步骤
1. 读取 MASTER_SETTING 获取角色、世界观
2. 读取 runtime_canon 获取已发生事件和角色当前状态
3. 读取待写章节的 outline
4. 提取角色一致性检查要点
5. 提取设定一致性检查要点
6. 提取去 AI 腔重点提醒
7. 写入 context 文件

## 质量标准
- 不超过 800 字
- 每条提醒必须有具体场景对应

## 常见失败情况
- runtime_canon 不存在：只基于 MASTER_SETTING 构建
- context 过长：裁剪最相关的前 3 条提醒

## 禁止事项
- 禁止写入未确认的未来规划
- 禁止替代 chapter_beat

## 示例输出
context/chapter_001_context.md — 标注林砚当前心态、能力紧张状态、父亲住院背景
