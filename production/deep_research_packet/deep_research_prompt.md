# 可直接复制给 Deep Research 的 Prompt

请基于我上传的资料包，做一份关于“工程化网文创作系统”的深度研究报告。

## 上传资料说明

资料包来自当前项目仓库中的规划和设计文档，已经压缩整理。请注意：资料包内的内容是当前项目判断，不是外部研究结论。你的任务是基于公开资料、相关理论和相邻工程实践，对这些判断做支持、反例、风险和改进方向的审计。

不要要求我上传小说正文、raw corpus 或原作原文。不要把任务理解成生成小说正文、模仿具体作者、作者复刻或作者指纹工程。

## 项目框架摘要

项目目标是构建工程化网文创作系统：用工程化保证产能，但避免滑向低质投喂、套路堆叠和内容农场化。当前顶层原则是：

人物有私心，行动有主权，作者不抢戏，读者能解压，细节轻轻漏。

作者退半步，人物漏半拍，读者补半截。

钩子负责把人拉进来，真东西负责让人留下来。

当前框架有两条主线。

主线 A：当前生成链路增强，包括人物质感（Human Texture）：解决人物不像功能件的问题；作品声音 / 作者站位（Work Voice）：解决正文里谁在讲故事、讲述者站在哪里的问题；角色主动感 / 行动主权（Character Agency）：解决人物是否自己推动局面的问题；活人浅痕 / 活人漏痕（Live Leakage）：解决人物是否有轻微、不刻意的活人痕迹；读者代入感 / 读者解压（Reader Immersion）：解决读者是否有参与判断、脑补和期待空间。

主线 B：角色驱动叙事引擎（Agentic Narrative Engine）：先让世界和角色运行，再把事件结果叙述成正文。候选组件包括 IP 宇宙、世界状态、角色 agents、场景仿真、事件日志、叙述渲染器和审核门禁。它是长线研究，不立即替换当前 production pipeline。

## 研究问题

1. 这套分层是否合理？是否有缺层、重叠、顺序错误？
2. 人物质感（Human Texture）与叙事理论、人物塑造理论、写作教学中的哪些概念相邻？
3. 作品声音 / 作者站位（Work Voice）与 narrator、focalization、narrative voice、implied author 等理论如何对应？
4. 角色主动感 / 行动主权（Character Agency）与 agency、character motivation、dramatic action、game AI agent、interactive storytelling 有什么关系？
5. 活人浅痕 / 活人漏痕（Live Leakage）是否有相邻概念，例如 incidental detail、embodied action、microgesture、behavioral residue、acting performance？
6. 读者代入感 / 读者解压（Reader Immersion）与 suspense、curiosity gap、reader response theory、transportation theory、narrative engagement 有什么关系？
7. 角色驱动叙事引擎（Agentic Narrative Engine）与 emergent narrative、drama management、AI director、multi-agent simulation、interactive fiction 有哪些相似与差异？
8. 当前 AI 写作工具、互动叙事工具、游戏叙事系统、创作辅助工具中，有哪些相邻实践？
9. 这套系统最大的工程风险是什么？
10. 这套系统最大的创作风险是什么？
11. 如何避免工程化创作系统滑向“更高级的套路生成器”？
12. 哪些模块应该优先做 MVP？
13. 如果只能做一个 1-scene MVP，应该怎么设计？
14. 哪些判断可能是错的？
15. 哪些外部理论或工程路线可能推翻我们的当前假设？

## 禁止事项

不要生成小说正文。不要模仿具体作者。不要要求上传原文语料。不要把目标理解成作者指纹或作者复刻。不要只给泛泛写作建议。不要把网文简单等同于低质套路内容。不要否认爽点、节奏、钩子在类型文中的必要性。不要把工程化与真诚创作简单对立。不要把角色驱动叙事引擎（Agentic Narrative Engine）理解成自由多 agent 聊天跑飞。不要把活人浅痕 / 活人漏痕（Live Leakage）理解成多加细节。不要把读者代入感 / 读者解压（Reader Immersion）理解成解释读者应该怎么想。不要把作品声音 / 作者站位（Work Voice）理解成作者出来讲课。不要把角色主动感 / 行动主权（Character Agency）理解成主角永远主动出击。

## 期望输出

请输出：

1. 执行摘要。
2. 项目框架评估。
3. 每个模块的理论参照。
4. 每个模块的相邻工程实践。
5. 主要风险清单。
6. MVP 优先级建议。
7. 推荐验证实验。
8. 反对意见与失败可能。
9. 可纳入路线图的建议。
10. 参考来源清单，并在正文中引用来源。

请做批判性审计，不要只顺着项目设想说好话。请明确区分：外部资料支持、外部资料反例、你的推断、项目当前判断。
