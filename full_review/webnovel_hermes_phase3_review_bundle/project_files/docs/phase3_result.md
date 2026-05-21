# 阶段三结果报告

> 生成时间：2026-05-21 CST
> 项目：webnovel-hermes-wps

---

## 一、执行结论

**状态：已完成**

一句话总结：阶段三实现了《人生价格标签》Demo 的 3 个关键节点（story_bible / chapter_beat / humanize）对 DeepSeek 真实 API 的真实调用闭环，mock 模式完全保留，真实调用只通过显式 `--real` 触发。

---

## 二、本轮实际完成内容

1. **call_deepseek.py 改造** — 统一 DeepSeek 调用封装，支持全部命令行参数（--mock/--real/--system-prompt/--input/--output/--log/--temperature/--max-tokens/--timeout/--retries/--task-name），支持重试和结构化日志
2. **run_demo.py 改造** — 支持 --phase3 --mock/--real/--steps/--output-root，默认行为不变（阶段二 mock 流程），新增 phase3_story_bible/chapter_beat/humanize 3 个步骤函数
3. **validate_phase3.py 新增** — mock/real 双模式验证，含 deepseek_calls.jsonl 安全检查（sk-/Authorization/API Key）
4. **validate_project.py 兼容调整** — 新增 phase3_status，不影响阶段二 passed 逻辑
5. **Prompt 调整** — story_bible.md / chapter_beat.md / humanize.md 输出格式改为 JSON，明确围绕《人生价格标签》设定
6. **Mock 输出** — /data/webnovel-lab/demo_output/phase3_mock_run/ 8 个文件
7. **Real 输出** — /data/webnovel-lab/demo_output/phase3_real_run/ 8 个文件
8. **日志输出** — /data/webnovel-lab/demo_output/phase3_logs/deepseek_calls.jsonl

---

## 三、改动文件清单

| 文件 | 操作 | 改动说明 |
|------|------|----------|
| scripts/call_deepseek.py | 修改 | 完整参数支持、重试、结构化日志、安全脱敏、加载 Hermes config |
| scripts/run_demo.py | 修改 | 新增 --phase3 分支、3 个阶段三步骤函数、argparse 入口 |
| scripts/validate_phase3.py | 新增 | mock/real 双模式验证、安全检查 |
| scripts/validate_project.py | 修改 | 新增 phase3_status 检测，不影响阶段二 |
| templates/prompts/story_bible.md | 修改 | 输出格式 JSON，明确项目设定 |
| templates/prompts/chapter_beat.md | 修改 | 输出格式 JSON，明确场景字段 |
| templates/prompts/humanize.md | 修改 | 输出格式 JSON，明确改写要求 |
| docs/phase2_final_acceptance.md | 新增 | 阶段二封版记录 |

---

## 四、DeepSeek 调用说明

- **是否真实调用 DeepSeek：是**
- **调用节点：story_bible, chapter_beat, humanize**
- **使用模型：deepseek-chat（deepseek-v4-flash）**
- **是否发生失败：否（3/3 全部成功）**
- **是否有重试：首次调用即成功，未触发重试**
- **输出保存在：** /data/webnovel-lab/demo_output/phase3_real_run/
- **日志保存在：** /data/webnovel-lab/demo_output/phase3_logs/deepseek_calls.jsonl
- **是否确认未泄露 API Key：是（日志中无 sk-、Authorization、API Key）**

---

## 五、验证命令与结果

| 命令 | 结果 |
|------|------|
| python scripts/env_check.py | ✅ 通过 (EXIT 0) |
| python scripts/validate_project.py | ✅ 通过 (EXIT 0, 0 errors) |
| python -m compileall scripts | ✅ 全部编译通过 |
| python scripts/run_demo.py --phase3 --mock | ✅ 通过 (EXIT 0) |
| python scripts/validate_phase3.py --mode mock | ✅ 通过 (EXIT 0) |
| python scripts/run_demo.py --phase3 --real | ✅ 通过 (EXIT 0, 3/3 节点成功) |
| python scripts/validate_phase3.py --mode real | ✅ 通过 (EXIT 0) |
| python scripts/sync_wps.py --dry-run | ✅ 通过 (EXIT 0) |

---

## 六、输出文件

**Mock 输出（/data/webnovel-lab/demo_output/phase3_mock_run/）：**
- story_bible_mock.md, story_bible_mock.json
- chapter_beat_mock.md, chapter_beat_mock.json
- humanize_mock.md, humanize_mock.json
- phase3_mock_summary.md, phase3_mock_summary.json

**Real 输出（/data/webnovel-lab/demo_output/phase3_real_run/）：**
- story_bible_real.md, story_bible_real.json
- chapter_beat_real.md, chapter_beat_real.json
- humanize_real.md, humanize_real.json
- phase3_real_summary.md, phase3_real_summary.json

**日志（/data/webnovel-lab/demo_output/phase3_logs/）：**
- deepseek_calls.jsonl（3 条记录）
- phase3_run.log
- phase3_validation.json

---

## 七、安全检查

- 是否检查 sk-：是（validate_phase3.py real 模式包含 sk- 检查）
- 是否检查 Authorization：是
- 是否检查 token：是（call_deepseek.py 日志过滤）
- 是否检查 cookie：是
- 是否检查 password：是
- 是否检查 API Key：是
- 是否确认复审包不包含 /etc/webnovel/.env：是
- 是否确认没有真实 WPS 上传：是（仅 dry-run）

---

## 八、已知风险

- DeepSeek 输出 JSON 结构可能不稳定，后续需要加强格式约束
- real 调用有成本（约 0.5-2 元/次）
- 网络失败可能影响 real 调用
- 模型输出质量不稳定，需要人工审核

---

## 九、未完成项

- 完整章节生成不在阶段三范围内（阶段四目标）
- WPS real 同步不在阶段三范围内（阶段五目标）
- 多项目/多章节批量生产不在阶段三范围内

---

## 十、验收项对照表

| 验收项 | 是否达成 | 说明 |
|--------|---------|------|
| mock 模式仍可运行 | 是 | run_demo.py 默认行为不变，--phase3 --mock 通过 |
| real 模式必须显式 --real | 是 | 无 --real 时默认 mock |
| Story Bible 真实调用完成 | 是 | DeepSeek 调用成功，输出保存 |
| Chapter Beat 真实调用完成 | 是 | DeepSeek 调用成功，输出保存 |
| Humanize 真实调用完成 | 是 | DeepSeek 调用成功，输出保存 |
| DeepSeek API Key 未泄露 | 是 | 日志无 sk-/Authorization/API Key |
| deepseek_calls.jsonl 已生成 | 是 | 3 条记录，含 task/success/时间戳 |
| validate_phase3.py 可运行 | 是 | --mode mock 和 --mode real 均通过 |
| WPS 未真实上传 | 是 | 仅执行 sync_wps.py --dry-run |
| 阶段三可提交主控方审计 | 是 | 复审包已准备 |

---

## 十一、最终结论

**最终状态：已完成**

**是否建议主控方审计：是**

**是否建议进入阶段四：视主控方审计结果而定**

**阶段四建议任务标题：** 阶段四：单项目三章小说生产闭环
