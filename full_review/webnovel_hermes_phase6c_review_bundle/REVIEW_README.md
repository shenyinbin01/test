# Phase 6C 复审包 — WPS 项目化管理

> 生成日期: 2026-05-26（v3 尾修 final）
> 项目: webnovel-hermes-wps / price_tag_life (人生价格标签)

---

## 复审内容

1. 本地 WPS 项目投影（publish / story_bible / wiki / index / archive）
2. WPS 项目同步工具（sync_wps_project.py / validate_wps_project.py）
3. 命令执行日志（dry-run + real 均通过）
4. 阶段报告

## 关键状态

| 项目 | 状态 | 说明 |
|------|------|------|
| 本地投影生成（16 文件） | ✅ 完成 | publish / story_bible / wiki / index / archive |
| dry-run 同步 | ✅ 通过 | 4 个文档计划同步，未调用 kdocs-cli |
| **real 同步** | **✅ 通过** | **4/4 文档上传成功，business_code=0** |
| 安全扫描 | ✅ 通过 | 无真实 WPS URL / file_id / folder_id / token 泄露 |

## 结构

```
command_logs/           — 所有验证命令的输出日志（含 real 成功日志）
project_files/          — 代码和文档
phase6c_outputs/        — 投影文件和状态文件（含 real 记录）
manifest.txt            — 文件清单（自动生成）
file_tree.txt           — 目录树（自动生成）
security_scan.log       — 安全扫描结果（分类扫描）
```

## 注意事项

- real 同步已通过 `python3 scripts/sync_wps_project.py --real` 执行，4/4 成功
- 所有状态文件已脱敏，无真实 WPS URL/file_id/folder_id 在复审包中
- Token 已写入 Hermes 永久记忆，防止丢失
- 建议使用 agentuser 直跑而非 sudo
