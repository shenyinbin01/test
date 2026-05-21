# webnovel-hermes-wps

中文网文创作生产系统。运行在腾讯云上的个人 AI 网文生产线。

## 项目定位

webnovel-hermes-wps **不是**通用 AI Agent 项目、不是 SaaS、不是文档管理系统。
它是面向中文网文创作流程的 Hermes / WPS / Kdocs 辅助生产系统——一条个人自用的 AI 网文生产线。

用户通过微信或文本指令下任务 → Hermes Adjunct 接收 → DeepSeek 生成内容 → 本地 .story-system 存储真源 → 渲染 DOCX → 同步到 WPS 供用户查看/编辑。

## 核心链路

```
master_setting → runtime_canon → chapter_outline → chapter_beat
     → chapter_writer → chapter_review → humanize
     → chapter_commit → projection → render_docx → sync_wps
```

1. **master_setting** — 小说项目顶层设定（书名、题材、核心脑洞、角色、势力、等级体系）
2. **runtime_canon** — 已确认正典（实际发生过的事件序列、角色当前状态）
3. **chapter_outline** — 章节大纲（章节号、标题、核心冲突、爽点、钩子、字数预算）
4. **chapter_beat** — 章节规划/节拍（场景序列、每场的叙事功能、情绪设计）
5. **chapter_writer** — 章节正文生成（根据 beat + 上下文输出正文）
6. **chapter_review** — 十维度审稿
7. **humanize** — 去 AI 腔改写
8. **chapter_commit** — 章节确认记录（变更摘要、影响到的角色/设定）
9. **projection** — .webnovel 投影（为 WPS 可读状态）
10. **render_docx** — 渲染为 DOCX
11. **sync_wps** — 同步到 WPS / Kdocs

## 目录结构

```
/opt/webnovel-hermes-wps/
├── README.md              ← 本文件
├── .env.example           ← 配置字段示例（无真实密钥）
├── skills/                ← 14 个 Skill，每个绑定网文生产环节
├── schemas/               ← 本体数据结构定义（YAML Schema）
├── templates/
│   ├── prompts/           ← DeepSeek 调用模板（system prompt）
│   ├── deai_rules/        ← 去 AI 腔规则库
│   └── wps/               ← WPS 投影模板
├── scripts/               ← 核心自动化脚本
├── docs/                  ← 阶段报告、设计文档
├── examples/              ← 示例参考
└── pipelines/             ← 串联流程（后续阶段）
```

```
/data/webnovel-lab/
├── workspace/novels/      ← 小说项目工作区（唯一故事真源）
├── exports/               ← 导出文件
├── backups/               ← 备份
└── logs/                  ← 脚本日志
```

## 核心原则

1. **WPS 只是输出载体。** 不是故事状态数据库。
2. **.story-system 是唯一故事真源。** 服务器本地保存所有结构化数据。
3. **写正文前必须先规划。** 必须有 Story Bible、章节大纲、章节规划。
4. **写正文后必须审稿、润色、生成 chapter_commit。**
5. **每一步都要产生文件和日志。** 不允许只在聊天中输出结果。
6. **不覆盖已确认章节。** 除非用户明确要求。
7. **不泄露密钥。** 不将 API Key / Token 写入仓库或日志。

## 快速开始

```bash
# 1. 环境检查
python3 scripts/env_check.py

# 2. 项目结构验证
python3 scripts/validate_project.py

# 3. 运行 Demo（mock 模式，不调用真实 API）
python3 scripts/run_demo.py
```

## Demo 说明

| 项目 | 内容 |
|------|------|
| Demo 项目 | 人生价格标签（都市脑洞爽文） |
| 当前模式 | mock/demo 模式（不调用 DeepSeek 真实 API） |
| 输出目录 | /data/webnovel-lab/demo_output/ |
| 核心脑洞 | 外卖员能看到每个人的人生价格标签 |

Demo 输出：
- demo_result.md — 可读报告
- demo_result.json — 结构化结果
- validation_report.json — 校验结果

## 验收方式

```bash
cd /opt/webnovel-hermes-wps
python scripts/env_check.py
python scripts/validate_project.py
python scripts/run_demo.py
python scripts/render_docx.py
python scripts/sync_wps.py
python -m compileall scripts
```

验收报告：/opt/webnovel-hermes-wps/docs/phase2_result.md

## 安全说明

- 不输出 DeepSeek API Key
- 不输出 kdocs-cli 认证信息
- .env.example 只写占位符，不包含任何真实密钥
- 真实密钥配置在 /etc/webnovel/.env（不在仓库中）
