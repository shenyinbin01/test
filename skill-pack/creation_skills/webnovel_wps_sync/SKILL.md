---
name: webnovel_wps_sync
description: "webnovel-hermes-wps WPS 同步角色 Skill — 调用 WPS 项目化工具链（build / sync / validate），生成 WPS 投影，执行 dry-run 或 real 同步。不修改正文，不修改 .story-system，不生成章节，不运行 Writer / Reviewer / Polisher。"
tags: ["webnovel", "wps", "sync", "projection", "phase7"]
---

# webnovel_wps_sync Skill

## 用途

将 .story-system 真源和 .webnovel 投影层的内容，通过 WPS 项目化工具链同步到 WPS 线上文档。保证 WPS 文档始终反映当前故事状态。

## 适用场景

1. 新章节通过验收后，需要将更新同步到 WPS
2. 需要刷新 WPS 投影文件（Story Bible / Wiki / Volume 投影）
3. 需要检查 WPS 同步状态（dry-run）
4. 阶段交付前做最终 WPS 同步验证

## 输入

| 输入 | 路径模式 | 必需 |
|------|----------|------|
| WPS doc_meta | `wps/doc_meta.yaml` | ✅ |
| 真源文件 | `.story-system/` | ✅ |
| 投影文件 | `.webnovel/projection/` | ✅ |
| build 脚本 | `scripts/build_wps_project_projection.py` | ✅ |
| sync 脚本 | `scripts/sync_wps_project.py` | ✅ |
| validate 脚本 | `scripts/validate_wps_project.py` | ✅ |
| 环境变量 | `/etc/webnovel/.env` 或 Hermes 传入 | ✅ |

## 输出

| 输出 | 路径 |
|------|------|
| 本地 WPS 投影 | `wps_projection/` |
| doc_meta（更新后） | `wps/doc_meta.yaml` |
| sync_log | `wps/sync_log.jsonl` |
| validate 结果 | `wps/validate_wps_project_result.yaml` |

## 允许读取路径

- `wps/`
- `wps_projection/`（如存在）
- `.story-system/`
- `.webnovel/projection/`
- `scripts/build_wps_project_projection.py`
- `scripts/sync_wps_project.py`
- `scripts/validate_wps_project.py`
- `/etc/webnovel/.env`（如存在）
- `templates/prompts/projection.md`（可选）

## 允许写入路径

- `wps/`
- `wps_projection/`

## 禁止行为

1. 不改正文
2. 不改 .story-system（包括 runtime_canon、reader_debts、MASTER_SETTING）
3. 不生成章节
4. 不生成 chapter_commit
5. 不运行 Writer / Reviewer / Polisher
6. 不从 WPS 反向导入内容
7. WPS 失败时不删除本地投影文件
8. 不跳过 dry-run 直接 real 同步（除非用户明确要求 real）

## 执行步骤

### dry-run 模式（默认）

1. 读取 doc_meta.yaml，确认 WPS 项目配置
2. 读取 .story-system 真源
3. 运行 `scripts/build_wps_project_projection.py` 生成本地投影
4. 运行 `scripts/validate_wps_project.py` 检查投影完整性
5. 输出 validate 结果到 `wps/validate_wps_project_result.yaml`
6. 记录 dry-run 结果到 `wps/sync_log.jsonl`
7. 向 Hermes 报告投影文件列表和 validate 结果
8. 不同步 WPS

### real 模式（仅当用户明确要求）

1. 先执行 dry-run 步骤 1-7
2. 如 dry-run 全部通过，运行 `scripts/sync_wps_project.py`
3. 更新 `wps/doc_meta.yaml`（同步时间、状态）
4. 记录 real 结果到 `wps/sync_log.jsonl`
5. 回传 WPS 文档链接

## 失败处理

1. doc_meta.yaml 不存在 → 停止并报告，要求先初始化 WPS 配置
2. build 脚本失败 → 停止，保留已有投影文件
3. validate 未通过 → 停止，不执行 real 同步
4. sync 脚本失败 → 停止，不更新 doc_meta
5. 网络错误 → 重试最多 2 次
6. 环境变量文件不存在 → 停止并报告

## 验收标准

1. dry-run 模式生成本地投影文件
2. validate 全部通过
3. sync_log 有条目记录
4. 未修改任何正文文件
5. 未修改 .story-system 任何文件
6. 未运行 Writer / Reviewer / Polisher
7. real 模式（如执行）返回 WPS 文档链接
8. WPS 失败时本地投影保留

## 与其他 Skill 的关系

- **webnovel_state_manager**: WpsSync 在 StateManager 之后执行；StateManager 更新真源和投影，WpsSync 将投影同步到 WPS
- **webnovel_planner / webnovel_writer / webnovel_reviewer / webnovel_polisher / detect_webnovel_ai_flavor**: WpsSync 与这些 Skill 无直接交互，在它们全部完成后执行
