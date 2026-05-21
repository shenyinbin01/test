# Skill 名称: sync_project_to_wps

## 所属流程环节
同步输出

## 适用场景
DOCX 生成后，需要即时同步到 Kdocs 以供用户在线查看/编辑。

## 输入
- DOCX 文件路径
- /etc/webnovel/.env（可选，WPS 配置）
- kdocs-cli（预先认证）

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/wps/doc_meta.yaml
- /data/webnovel-lab/workspace/novels/{project_name}/wps/sync_log.jsonl

## 执行步骤
1. 检查 kdocs-cli 是否可用（which kdocs-cli）
2. 检查 /etc/webnovel/.env 是否有 WPS 配置
3. 如果条件具备：使用 kdocs-cli drive upload-file 上传
4. 如果条件不具备：记录 dry-run 日志，不失败
5. 写入 doc_meta.yaml 记录文档信息
6. 写入 sync_log.jsonl 记录同步时间和结果

## 质量标准
- 不输出认证信息到日志
- 失败时保留本地 DOCX
- 同步记录完整可追溯

## 常见失败情况
- kdocs-cli 未认证：提示用户先执行 kdocs-cli auth set-token
- WPS 上传失败：记录错误信息到 sync_log.jsonl
- .env 不存在：降级为 dry-run

## 禁止事项
- 禁止在日志中打印 Token 或 Cookie
- 禁止在同步失败后删除本地文件
- 禁止覆盖 WPS 上已有的同名文档

## 示例输出
doc_meta.yaml — file_id, upload_time, doc_link
sync_log.jsonl — 每次同步记录一条 JSON
