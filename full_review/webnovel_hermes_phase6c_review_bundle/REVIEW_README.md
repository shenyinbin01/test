# Phase 6C 复审包 — WPS 项目化管理

> 生成日期: 2026-05-26（v2 尾修版）
> 项目: webnovel-hermes-wps / price_tag_life (人生价格标签)

---

## 复审内容

1. 本地 WPS 项目投影（publish / story_bible / wiki / index / archive）
2. WPS 项目同步工具（sync_wps_project.py / validate_wps_project.py）
3. 命令执行日志（dry-run 通过，real skipped）
4. 阶段报告（修复了与事实不一致的状态记录）

## 关键状态

| 项目 | 状态 | 说明 |
|------|------|------|
| 本地投影生成（16 文件） | ✅ 完成 | publish / story_bible / wiki / index / archive |
| dry-run 同步 | ✅ 通过 | 4 个文档计划同步，未调用 kdocs-cli |
| **real 同步** | **⏸ skipped** | **未通过 Phase 6C 工具（sync_wps_project.py）执行** |
| 手动上传 | 不计入工具验收 | 4 个 docx 由操作员手动上传至 WPS「小说」文件夹 |
| 安全扫描 | ✅ 通过 | 无真实 WPS URL / file_id / folder_id / token 泄露 |

## 结构

```
command_logs/           — 所有验证命令的输出日志（含 real 跳过说明）
project_files/          — 代码和文档
phase6c_outputs/        — 投影文件和状态文件（仅 dry_run 记录）
manifest.txt            — 文件清单（自动生成）
file_tree.txt           — 目录树（自动生成）
security_scan.log       — 安全扫描结果（分类扫描）
```

## 注意事项

- real 同步未通过 Phase 6C 工具执行（原因：sudo 环境下 kdocs-cli 不可用）
- 4 个 docx 已在上一轮由操作员手动通过 kdocs-cli 上传至 WPS，但手动操作不计入工具验收
- 所有状态文件已脱敏（[REDACTED]），仅记录 dry_run
- 如需正式验收 real 同步，需先修复 sync_wps_project.py 在受限环境下的运行能力
- 修复后执行：`sudo env PATH=$PATH:/home/agentuser/.local/bin python3 scripts/sync_wps_project.py --project price_tag_life --real`
