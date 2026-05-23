# deepcode_safe_refactor

## 用途

执行小步、安全、可回滚的工程重构。

## 适用任务

当 Hermes 明确给出具体改造目标，例如"把 validate_phase4.py 中的禁止词抽到 canon_patterns.yaml"时，调用本 Skill。

## 输入

- Hermes 下发的具体任务单
- AGENTS.md
- docs/deepcode_onboarding.md
- docs/deepcode_repo_audit.md，如果存在
- 需要修改的文件列表
- 验收标准

## 输出

- 修改后的代码或配置
- docs/refactor_log_{timestamp}.md

## 允许读取的内容

- 任务相关文件
- AGENTS.md
- docs/
- .story-system/
- scripts/

## 允许写入的内容

- Hermes 任务单明确允许修改的文件
- docs/refactor_log_{timestamp}.md

## 禁止行为

1. 不允许修改任务单未授权的文件。
2. 不允许删除 run_chapter_pipeline.py。
3. 不允许大规模重写 pipeline。
4. 不允许改变 WPS 同步链路。
5. 不允许把创作规则继续写进 Python 常量。
6. 不允许把密钥写进代码仓库。
7. 不允许改小说正文，除非任务明确要求。
8. 不允许进行产品架构决策。

## 执行步骤

1. 读取 Hermes 任务单。
2. 确认允许修改的文件范围。
3. 记录修改前文件状态。
4. 如果项目使用 git，先检查 git status。
5. 小步修改。
6. 每改一个文件，记录改动原因。
7. 不做任务范围外优化。
8. 运行最小必要验证。
9. 生成 docs/refactor_log_{timestamp}.md。

## docs/refactor_log_{timestamp}.md 必须包含

# DeepCode 安全重构日志

## 1. 任务目标
## 2. 修改文件
## 3. 新增文件
## 4. 未修改但检查过的文件
## 5. 具体改动说明
## 6. 验证命令
## 7. 验证结果
## 8. 风险点
## 9. 回滚建议

## 验收标准

1. 只修改授权文件。
2. 没有删除可运行 pipeline。
3. 没有新增未授权架构。
4. 有 refactor log。
5. 有验证结果。

## 失败处理

如果任务单不清楚，停止并向 Hermes 请求澄清。
如果测试失败，报告失败原因，不继续扩大修改范围。
