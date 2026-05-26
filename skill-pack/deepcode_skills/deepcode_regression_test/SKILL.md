# deepcode_regression_test

## 用途

在代码修改后执行回归测试，确认现有链路没有被破坏。

## 适用任务

任何涉及 scripts/、validators、pipeline、WPS 同步、.story-system 的改动完成后，都应执行本 Skill。

## 输入

- Hermes 下发的测试目标
- 修改文件列表
- 预期通过的命令
- 项目路径

## 输出

- docs/regression_result_{timestamp}.md

## 允许读取的内容

- 项目全部代码
- logs/
- docs/
- .story-system/
- .webnovel/

## 允许写入的内容

- docs/regression_result_{timestamp}.md
- 测试日志文件

## 禁止行为

1. 不允许修改业务代码。
2. 不允许修复测试失败。
3. 不允许自动重写 pipeline。
4. 不允许同步 WPS，除非任务明确要求。
5. 不允许删除测试产物，除非是明确的临时文件。

## 执行步骤

1. 读取 Hermes 测试任务。
2. 确认本次需要验证的内容。
3. 运行指定测试命令。
4. 如果没有指定命令，按项目默认顺序运行：
   - python scripts/validate_project.py，如果存在
   - python scripts/validate_canon_consistency.py，如果存在
   - python scripts/validate_phase4.py，如果存在
   - python scripts/render_docx.py 的最小测试，如果安全
5. 记录每条命令、退出码、输出摘要。
6. 生成 regression_result。

## docs/regression_result_{timestamp}.md 必须包含

# DeepCode 回归测试报告

## 1. 测试目标
## 2. 测试环境
## 3. 测试命令
## 4. 通过项
## 5. 失败项
## 6. 失败日志位置
## 7. 是否影响现有 pipeline
## 8. 是否影响 WPS 输出
## 9. 建议下一步

## 验收标准

1. 报告存在。
2. 每条测试命令有结果。
3. 失败项不能被隐藏。
4. DeepCode 不得在本 Skill 中直接修复代码。

## 失败处理

如果测试命令不存在，报告"命令不存在"，不要猜测。
如果测试失败，停止并把失败原因交给 Hermes 决策。
