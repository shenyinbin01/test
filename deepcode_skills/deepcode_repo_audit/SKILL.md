# deepcode_repo_audit

## 用途

审查当前仓库结构、Python 文件职责、硬编码规则、越界逻辑和架构风险。

## 适用任务

当 Hermes 需要了解当前代码是否跑偏、哪些文件越界、哪些规则仍硬编码时，调用本 Skill。

## 输入

- AGENTS.md
- docs/deepcode_onboarding.md
- scripts/
- skills/
- .story-system/
- .webnovel/
- run_chapter_pipeline.py
- run_demo.py
- validate_phase4.py
- validate_canon_consistency.py
- sync_wps.py
- render_docx.py

## 输出

- docs/deepcode_repo_audit.md

## 允许读取的内容

- 项目代码和文档
- .story-system/
- .webnovel/

## 允许写入的内容

- docs/deepcode_repo_audit.md

## 禁止行为

1. 不允许修改代码。
2. 不允许修复问题。
3. 不允许重构。
4. 不允许生成小说。
5. 不允许同步 WPS。
6. 不允许删除文件。

## 执行步骤

1. 列出当前 Python 文件。
2. 对每个 Python 文件判断用途。
3. 将 Python 文件分类为：
   - 合理工具层
   - 可疑越界
   - 明确越界
4. 检查是否存在硬编码：
   - 禁止词
   - 锚点
   - 章节目标
   - Prompt 模板
   - 角色职责
   - pipeline 节点
5. 检查角色型 Skill 是否存在：
   - webnovel-planner
   - webnovel-writer
   - webnovel-reviewer
   - webnovel-polisher
   - webnovel-state-manager
   - webnovel-wps-sync
6. 检查 .story-system 是否完整：
   - MASTER_SETTING.yaml
   - runtime_canon.yaml
   - reader_debts.yaml
   - canon_patterns.yaml
   - chapter_commits/
   - audit_log.jsonl
7. 检查 WPS 项目化状态。
8. 生成 docs/deepcode_repo_audit.md。

## docs/deepcode_repo_audit.md 必须包含

# DeepCode 仓库审查报告

## 1. 当前 Python 文件列表及用途
## 2. 合理工具层文件
## 3. 可疑越界文件
## 4. 明确越界文件
## 5. 硬编码规则清单
## 6. 角色 Skill 落地状态
## 7. .story-system 完整性检查
## 8. WPS 同步与项目化检查
## 9. 架构风险
## 10. 建议修复顺序

## 验收标准

1. docs/deepcode_repo_audit.md 存在。
2. 报告必须具体到文件名。
3. 报告必须区分"工具层"和"越界逻辑"。
4. 报告不得修改任何代码。

## 失败处理

如果无法读取某个文件，报告中标注"未读取"并说明原因。
