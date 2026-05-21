# webnovel-hermes-wps 阶段三复审包

## 项目
- webnovel-hermes-wps — 中文网文生产系统

## 阶段三目标
为《人生价格标签》Demo 的 3 个关键节点（story_bible / chapter_beat / humanize）启用 DeepSeek 真实 API 调用，形成可审计的真实调用最小闭环。

## 本包包含
- 项目文件（scripts, docs, prompts）
- 阶段三 mock/real 输出
- deepseek_calls.jsonl 日志
- 验证命令日志
- 安全扫描报告

## 安全声明
- 不包含真实 .env
- 不包含 /etc/webnovel/ 下密钥
- 不包含真实 WPS file_id/doc_link/folder_id/link_id
- 不包含 DeepSeek API Key
- 不包含 __pycache__ / *.pyc / .git
- deepseek_calls.jsonl 已通过安全检查（无 sk-/Authorization/API Key）

