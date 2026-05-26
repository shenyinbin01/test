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
| 创作角色 Skill | 7 | ✅ 全部已实现 |
| DeepCode 编程 Skill | 5 | ✅ 全部已实现 |

### 完整创作链路

```
webnovel_planner
  → webnovel_writer
  → detect_webnovel_ai_flavor
  → webnovel_reviewer
  → webnovel_polisher
  → webnovel_state_manager
  → webnovel_wps_sync
```

参见: `docs/phase7_multirole_creation_workflow.md`

## 审核要点

1. Skill 职责边界是否清晰？
2. 输入/输出路径是否合理？
3. 禁止行为是否充分？
4. 执行步骤是否可操作？
5. 与 AGENTS.md 分工是否一致？
6. 完整 7 角色创作链路是否覆盖了全部创作流程？
7. 已定义但未实现的 Skill — 已全部补齐，不再有待实现缺口。
8. Prompt 模板与对应 Skill 的职责是否一致？
