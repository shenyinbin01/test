# webnovel-hermes-wps Skill Pack

项目：爱马仕 × WPS 网文自动创作链路  
GitHub: https://github.com/shenyinbin01/test

## 目录结构

```
skill-pack/
├── README.md                    ← 本文件
├── AGENTS.md                    ← 项目架构总纲（指向 /AGENTS.md）
├── creation_skills/             ← 小说创作角色 Skill（Hermes 调用）
│   ├── webnovel-reviewer/       ← 十维度审稿 Skill
│   ├── webnovel-polisher/       ← 去 AI 味润色 Skill
│   └── detect-ai-flavor/        ← AI 味检测 Skill
├── deepcode_skills/             ← DeepCode 编码代理 Skill
│   ├── deepcode-project-onboarding/
│   ├── deepcode-repo-audit/
│   ├── deepcode-safe-refactor/
│   ├── deepcode-regression-test/
│   └── deepcode-engineering-report/
└── mapping.md                   ← 实际文件路径 ↔ skill pack 映射
```

## Skill 数量

| 类型 | 数量 | 状态 |
|------|------|------|
| 创作角色 Skill | 3 | ✅ 已实现 |
| DeepCode 编程 Skill | 5 | ✅ 已实现 |
| 已定义但未实现 | 3 | ⚠️ 等待实现 |

### 已定义但未实现的 Skill（AGENTS.md §5.1）

| Skill | 职责 | 状态 |
|-------|------|------|
| webnovel-planner | Story Bible、大纲、章节 Beat | ❌ 未实现 |
| webnovel-writer | 根据 Beat 写正文草稿 | ❌ 未实现 |
| webnovel-state-manager | 更新 runtime_canon、reader_debts、state.yaml | ❌ 未实现 |
| webnovel-wps-sync | 渲染 DOCX、同步 WPS | ❌ 未实现 |

> 注：以上 4 个 Skill 已在架构文档中定义职责边界但尚未以独立 SKILL.md 文件形式存在。

## 审核要点

1. Skill 职责边界是否清晰？
2. 输入/输出路径是否合理？
3. 禁止行为是否充分？
4. 执行步骤是否可操作？
5. 与 AGENTS.md 分工是否一致？
6. 已实现 vs 待实现 Skill 的划分是否合理？
