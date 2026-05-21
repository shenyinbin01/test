# Skill 名称: create_chapter_commit

## 所属流程环节
同步摘要

## 适用场景
章节完成审稿和润色后，生成 commit 记录，为更新 runtime_canon 做准备。

## 输入
- 章节号 N
- 最终正文
- 上一版的 commit（如有）
- templates/prompts/chapter_commit.md

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/.story-system/chapter_commits/chapter_{N}_commit.yaml

## 执行步骤
1. 从最终正文提取核心情节事件
2. 对比 MASTER_SETTING 和 runtime_canon 识别角色/世界观变更
3. 提取对话中的重要信息
4. 识别新埋下的伏笔
5. 写入 commit 文件

## 质量标准
- plot_events 可被后续章节引用
- character_updates 精确到谁、什么变化
- foreshadowing 具体到段落位置

## 常见失败情况
- 角色变化识别错误：对比 MASTER_SETTING 逐项确认
- 伏笔遗漏：通读全文找出所有"没在当前章节解决"的线索

## 禁止事项
- 禁止写入未在正文中发生的事件
- 禁止预测未来变化

## 示例输出
commits/chapter_001_commit.yaml — v1, initial, 林砚发现能力+父亲价格归零
