# Skill Injection Plan — Phase 8 → Phase 7 Sandbox

## Injection Strategy

20 approved craft patterns grouped by target role. Each role receives a curated overlay prompt that injects the relevant patterns as **guidance lenses** — the role still executes its core skill normally, but now has access to extracted structural knowledge from the reference work.

## Role Assignment

### Planner (webnovel_planner) — 7 patterns

| Pattern | ID | Injection Mode |
|---------|-----|---------------|
| 认知碾压式爽点 | DCQG-C001 | World rule: protagonist cognitive advantage in setting |
| 压力源内化 | DCQG-C009 | Character design: internalized stakes beyond external threats |
| 多重介入身份 | DCQG-C011 | Plot architecture: layered protagonist roles per arc |
| 世界观揭秘驱动 | DCQG-C012 | Structure: reveal-based arc planning |
| 多线并行织网 | DCQG-C017 | Outline: subplot weaving rules |
| 冲突螺旋升级 | DCQG-C010 | Conflict design: escalation pattern per volume |
| 降维打击式引入 | DCQG-C014 | Pacing: when to introduce new world mechanics |

### Writer (webnovel_writer) — 7 patterns

| Pattern | ID | Injection Mode |
|---------|-----|---------------|
| 认知碾压式爽点 | DCQG-C001 | Scene writing: "show the gap" pattern |
| 伪装身份 | DCQG-C006 | Scene design: identity play beats |
| 外部任务触发器 | DCQG-C004 | Chapter opening: quest-driven momentum |
| 历史沉浸揭秘 | DCQG-C008 | Exposition: embedded reveal pattern |
| 镜像反派 | DCQG-C003 | Antagonist design: reflection-based villain |
| 主角作为导师 | DCQG-C007 | Relationship writing: mentor dynamics |
| 规则解构式破局 | DCQG-C002 | Climax writing: rule-aware breakthroughs |

### Reviewer (webnovel_reviewer) — 4 patterns

| Pattern | ID | Injection Mode |
|---------|-----|---------------|
| 短钩快兑/长钩慢兑 | DCQG-C005 | Audit: hook payoff pacing check |
| 情感锚点 | DCQG-C013 | Audit: emotional beats per chapter |
| 喜剧调剂 | DCQG-C018 | Audit: tonal variety check |
| 终极代价与取舍 | DCQG-C020 | Audit: climax cost verification |

### Polisher (webnovel_polisher) — 4 patterns

| Pattern | ID | Injection Mode |
|---------|-----|---------------|
| 认知碾压式爽点 | DCQG-C001 | Polish: cognitive contrast sharpening |
| 理念冲突/价值观辩论 | DCQG-C015 | Polish: dialogue depth enhancement |
| 规则系统漏洞利用 | DCQG-C021 | Polish: cleverness amplification |
| 尾声初心回归 | DCQG-C022 | Polish: ending emotional resonance |

### Not injected (2 patterns — medium confidence, post-climax only)

| Pattern | ID | Reason |
|---------|-----|--------|
| 终极代价与取舍 | DCQG-C020 | Reviewer-only; full application needs complete arc |
| 尾声初心回归 | DCQG-C022 | Polisher-only; validation is single-chapter |

## Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Pattern over-application (every chapter uses every pattern) | Medium | Overlay prompts specify "use 1-2 patterns per output, not all" |
| Templating (outputs feel formulaic) | Medium | Overlay asks roles to "apply selectively, ignore when not relevant" |
| Original contamination | Low | All 20 cards verified: positive examples are de-originalized |
| Medium-confidence pattern noise | Low | Only inject C009/C013/C020/C022 in applicable roles |
| Phase 7 skill divergence | Low | Overlays are additive prompts, don't replace core skill instructions |

## Validation Scope

**Sandbox story brief**: Original short story (sci-fi/fantasy crossover), single chapter ~3000字. Protagonist: time-sensitive detective (can see 10 seconds into the future). Setting: near-future cyberpunk city with hidden magical underground. Core conflict: protagonist discovers their ability has a previously unknown cost.

**Why this works**: Small enough for single-chapter validation; abstract enough to test pattern transfer (no reliance on xianxia tropes); diverse enough to exercise multiple pattern types (cognitive advantage = 10s precognition, rule system = ability cost, reader pull = mystery reveal).
