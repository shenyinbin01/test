# webnovel-hermes-wps 全项目复审包

## 项目名称

- webnovel-hermes-wps

## 本包用途

- 全项目复审包

## 当前阶段

- 阶段二修复后全量复审

## 本包包含

- 项目文件
- 脚本
- Schema
- Prompt
- deai_rules
- Skill
- Demo workspace
- Demo output
- 验证日志
- 脱敏 WPS 状态文件

## 本包不包含

- 真实 .env
- /etc/webnovel/ 下密钥
- GitHub token
- WPS token/cookie/password
- DeepSeek API Key
- .git
- __pycache__
- *.pyc

## 本轮验证命令

- python scripts/env_check.py
- python scripts/validate_project.py
- python scripts/run_demo.py
- python scripts/render_docx.py
- python scripts/sync_wps.py --dry-run
- python -m compileall scripts

## 明确声明

- 本轮没有执行真实 WPS 上传。
- 本轮没有执行 DeepSeek 真实调用。
- sync_wps.py 仅以 dry-run 方式验证。
- 若需要真实上传，必须单独显式执行 --real。

## 主控方复审重点

- sync_wps.py 是否已经修复假阳性
- validate_project.py 是否具备可验收性检查
- run_demo.py 是否形成中文网文 Demo 闭环
- Schema / Prompt / Skill 是否足够支撑后续阶段
- 是否仍存在模板化、空文件、假通过、过度乐观报告
- 是否存在敏感信息泄露风险
