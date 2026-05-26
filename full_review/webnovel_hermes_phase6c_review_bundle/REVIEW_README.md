# Phase 6C 复审包 — WPS 项目化管理

> 生成日期: 2026-05-26
> 项目: webnovel-hermes-wps / price_tag_life (人生价格标签)

---

## 复审内容

1. 本地 WPS 项目投影（publish / story_bible / wiki / index / archive）
2. WPS 项目同步工具（sync_wps_project.py / validate_wps_project.py）
3. 命令执行日志
4. 阶段报告

## 结构

```
command_logs/           — 所有验证命令的输出日志
project_files/          — 代码和文档
phase6c_outputs/        — 投影文件和状态文件
manifest.txt            — 文件清单（自动生成）
file_tree.txt           — 目录树（自动生成）
security_scan.log       — 安全扫描结果
```

## 注意事项

- real 同步因 WPS_FOLDER_ID 未配置跳过
- 所有状态文件已脱敏（[REDACTED]）
- 配置 WPS 认证后：`python scripts/sync_wps_project.py --project price_tag_life --real`
