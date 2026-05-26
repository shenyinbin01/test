# deepcode_project_onboarding

## 用途

让 DeepCode 在正式改代码前完成项目入职，理解项目目标、当前架构、角色分工、代码边界和风险点。

## 适用任务

当 DeepCode 第一次接入项目，或 AGENTS.md / 项目架构发生重大调整后，必须先执行本 Skill。

## 输入

- AGENTS.md
- README.md
- docs/
- scripts/
- skills/
- .story-system/
- .webnovel/
- run_chapter_pipeline.py
- run_demo.py
- validate_phase4.py
- validate_canon_consistency.py
- render_docx.py
- sync_wps.py

## 输出

- docs/deepcode_onboarding.md

## 允许读取的内容

- 项目根目录下所有文档、脚本、配置、Skill、Schema
- .story-system/
- .webnovel/

## 允许写入的内容

- docs/deepcode_onboarding.md

## 禁止行为

1. 不允许修改 Python 代码。
2. 不允许修改 pipeline。
3. 不允许修改 .story-system。
4. 不允许修改 WPS 同步逻辑。
5. 不允许生成小说内容。
6. 不允许创建新架构。
7. 不允许删除任何文件。

## 执行步骤

1. 阅读 AGENTS.md，确认当前分工。
2. 阅读 README.md，理解项目目标。
3. 扫描 scripts/，列出主要 Python 工具文件。
4. 扫描 skills/，列出现有 Hermes Skill。
5. 扫描 .story-system/，理解故事真源结构。
6. 扫描 .webnovel/，理解投影层结构。
7. 重点阅读 run_chapter_pipeline.py，判断它承担了哪些调度职责。
8. 重点阅读 validate_phase4.py 和 validate_canon_consistency.py，判断是否存在硬编码规则。
9. 重点阅读 render_docx.py 和 sync_wps.py，理解 WPS 输出链路。
10. 生成 docs/deepcode_onboarding.md。

## docs/deepcode_onboarding.md 必须包含

# DeepCode 项目入职文档

## 1. 项目目标
## 2. 当前架构
## 3. 角色分工
## 4. Python 工具层边界
## 5. .story-system 真源原则
## 6. .webnovel 投影层说明
## 7. WPS 输出链路说明
## 8. 当前高风险文件
## 9. 当前禁止行为
## 10. DeepCode 后续接活规则
## 11. 建议的回归测试方式

## 验收标准

1. docs/deepcode_onboarding.md 存在。
2. 文档包含以上 11 个章节。
3. DeepCode 没有修改任何 Python 文件。
4. DeepCode 没有修改 .story-system。
5. DeepCode 没有运行小说生成 pipeline。

## 失败处理

如果缺少关键文件，必须在报告中列出，不允许猜测。
如果读取文件失败，必须说明失败路径和原因。
