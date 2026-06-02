# Phase 8 — Next Stage Recommendation

## 前提
Phase 8 已完成《大乘期》单书闭环。已确认整书拆解→技法蒸馏→Skill Pack 注入→正向验证这条链路可行。
**以下为建议，不执行。**

---

## 建议一: 新书拆解流水线产品化

### 目标
让下一本合法小说输入后，可以自动跑到 Step 5 或 Step 6 候选状态，减少主控方中途干预。

### 要做
1. **固化 book_id 参数**: Step 1~5 的所有路径和命名以 `{book_id}` 参数化
2. **固化 task_templates**: 为每个 Step 生成标准化任务模板（Step 3B/4/5/6 已有模板，需审查和统一格式）
3. **固化 status.yaml**: 每本书一个 status 文件跟踪各步骤状态
4. **固化验收报告格式**: 每个 Step 的验收标准模板化
5. **固化 quality_report 校验脚本**: chapter_card 完整性/YAML 解析率/字段非空率自动校验
6. **减少手动 curator 干预**: 探索 curator 审核规则的程序化——contamination_risk 枚举值校验、forbidden_original_elements 去原作化检查、status 字段一致性检查

### 预期效果
新书输入后:
- Step 1-2: 程序自动（章节切分 + chapter_card 生成）
- Step 3B: 程序生成 spine + 阶段边界检测，LLM 按阶段调用（固化 prompt）
- Step 4-5: LLM 蒸馏 + 程序化 curator 校验 → 人工最终审核
- Step 6: 沙盒正向验证（固化 overlay prompt 生成 + 创意链调用）

---

## 建议二: 多书技法库分层管理

### 目标
建立分层技法库，不每拆一本书就修改 Skill Pack。

### 架构

```
technique_library/
├── book_patterns/
│   └── dachengqi/               # 《大乘期》20 张
│   └── {next_book}/             # 下一本书的技法
│
├── genre_patterns/              # ≥2 本书交叉验证后升级
│   ├── xianxia/
│   └── ...
│
├── universal_patterns/          # ≥3 本书/跨类型验证
│
├── style_profiles/              # 特定风格/语调配置
│
└── project_patterns/            # 当前创作项目专用
    └── {project_name}/
```

### 流程
1. 新书拆解 → 技法入库 `book_patterns/{book_id}/`
2. 两书交叉验证 → 共同技法升级到 `genre_patterns/`
3. 三书以上/跨类型验证 → 升级到 `universal_patterns/`
4. 当前创作项目 → 从技法库选择适用技法，组装 `project_patterns/`
5. Skill Pack 注入来源: **project_patterns**，不是 raw book_patterns

### 核心原则
- **不要每拆一本书就直接修改 Skill Pack**
- 先入库，经过跨书验证后再决定是否注入
- Skill Pack 不应继续无限堆技法

---

## 建议三: 第二本书验证

### 目标
选择一本合法的同类型或相邻类型爆款，验证:
1. 当前拆解流程是否可复用
2. 《大乘期》提炼出的 20 张技法中，哪些跨书成立
3. 哪些技法应升级为 genre_patterns
4. 哪些技法应保留为 book_patterns（仅《大乘期》有效）

### 选书建议
- **同类型**（仙侠/修真）: 验证技法在同类型内的迁移性
- **相邻类型**（玄幻/高武）: 验证技法在相邻类型中的边界
- 优先选择已完成、有明确章节结构的作品

### 验证重点
- 对比 candidate_pool 重叠率（两本书各自蒸馏出的技法有多少交集）
- 对比 approved_patterns 的 contamination_risk 分布
- 对比正向验证链的评分趋势

### 预期产出
- 两本书的技法交叉报告
- 第一批 genre_patterns
- 第一批 book_patterns 归档
- 流程改进建议

---

## 总优先级

| 优先级 | 建议 | 理由 |
|--------|------|------|
| P0 | 新书拆解流水线产品化 | 不产品化，每本书的边际成本不会下降 |
| P1 | 第二本书验证 | 不验证，不知道哪些技法是 universal |
| P2 | 多书技法库分层管理 | 不急着建库——先有第二本书的技法才能交叉 |
