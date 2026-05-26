# deepcode_engineering_report

## 用途

生成阶段性工程报告，例如 Phase 6A、6B、6C 的结果报告。

## 适用任务

当 Hermes 要求 DeepCode 汇总某个阶段的工程结果时调用。

## 输入

- Hermes 阶段报告任务单
- 相关改动文件
- 相关日志
- 相关测试结果
- docs/refactor_log_*.md
- docs/regression_result_*.md

## 输出

- Hermes 指定的报告文件，例如：
  - docs/phase6a_state_manager_result.md
  - docs/phase6b_deai_result.md
  - docs/phase6c_wps_project_result.md

## 允许读取的内容

- docs/
- scripts/
- skills/
- .story-system/
- .webnovel/
- logs/

## 允许写入的内容

- Hermes 指定的报告文件

## 禁止行为

1. 不允许修改代码。
2. 不允许新增功能。
3. 不允许重构。
4. 不允许运行高风险 pipeline。
5. 不允许修复问题。
6. 不允许把未完成项写成已完成。

## 执行步骤

1. 读取 Hermes 报告任务单。
2. 收集相关文件状态。
3. 收集相关日志。
4. 收集测试结果。
5. 按 Hermes 指定结构生成报告。
6. 明确区分：
   - 已完成
   - 部分完成
   - 未完成
   - 失败
   - 风险
7. 写入指定报告路径。

## 报告必须包含

# 阶段工程报告

## 1. 本轮目标
## 2. 新增文件
## 3. 修改文件
## 4. 已完成事项
## 5. 部分完成事项
## 6. 未完成事项
## 7. 测试结果
## 8. 风险点
## 9. 下一步建议

## 验收标准

1. 报告文件存在。
2. 报告结构完整。
3. 没有把未完成事项伪装成完成。
4. 没有修改代码。
5. 报告能被 Hermes 用于向用户汇报。

## 失败处理

如果缺少测试结果，报告中明确写"测试结果缺失"。
如果缺少相关文件，报告中明确写"文件不存在"。
