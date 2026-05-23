#!/usr/bin/env python3
"""
run_demo.py — 一键跑通"人生价格标签"Demo
默认 mock 模式，不调用 DeepSeek 真实 API。
输出: demo_result.md, demo_result.json, validation_report.json
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime


CODE_ROOT = Path(os.environ.get("WEBNOVEL_CODE_ROOT", "/opt/webnovel-hermes-wps"))
DATA_ROOT = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))

# ── Demo 种子数据 ──────────────────────────────────────────────

DEMO_PROJECT = {
    "project_name": "price_tag_life",
    "book_title": "人生价格标签",
    "genre": "都市脑洞",
    "core_idea": "主角是普通外卖员，能看到每个人的人生价格标签",
    "target_reader": "男频爽文读者",
    "style_preference": "快节奏、强钩子、口语化、爽点明确",
}

DEMO_MASTER_SETTING = {
    "project": {
        "name": "price_tag_life",
        "genre": "都市脑洞",
        "core_idea": "主角是普通外卖员，能看到每个人的人生价格标签。标签不是财富，而是人生价值、潜力、风险、选择代价的综合显影。",
        "target_reader": "男频爽文读者",
        "style_preference": "快节奏、强钩子、口语化",
    },
    "characters": [
        {
            "name": "林砚",
            "age": 24,
            "identity": "外卖员",
            "personality": "克制、敏感、观察力强，不圣母但有底线",
            "motivation": "父亲病重欠债，急需钱",
            "arc": "从被动受压→主动利用能力改变命运",
            "initial_price_tag": "归零边缘",
            "price_tag_meaning": "当前人生价值和风险的显影",
        }
    ],
    "world": {
        "background": "现代都市，主角所在城市经济压力大，外卖行业竞争激烈",
        "rules": [
            "标签只显示当前状态，不直接显示完整未来",
            "标签会误导，必须结合现实判断",
            "每次强行窥探能力会带来头痛或短暂失明",
            "标签变化不等于命运确定",
            "标签和财富不完全相关",
        ],
        "factions": ["外卖平台系统", "医院/医疗体系", "隐藏设定（待后续展开）"],
    },
    "outline": {
        "total_chapters": 30,
        "current_arc": "能力觉醒期（1-10章）",
        "key_arcs": [
            "觉醒与试错（1-10章）",
            "成长与博弈（11-20章）",
            "真相与抉择（21-30章）",
        ],
    },
}

DEMO_CHAPTER_001 = {
    "number": 1,
    "title": "归零",
    "conflict": "林砚急需钱，但还不知道标签真正代表什么",
    "hook": "父亲头顶价格即将归零，逼迫主角必须立刻理解并使用能力",
    "emotion_arc": "压抑→好奇→震惊→压迫→紧迫",
    "scenes": [
        {
            "order": 1,
            "title": "接单",
            "narrative_function": "hook",
            "pov": "林砚",
            "location": "外卖站点/街头",
            "emotion_target": "压抑和疲惫",
            "conflict_type": "人与系统",
            "dialogue_ratio": 0.3,
            "length": 400,
            "key_lines": ["手机又响了。", "这个月第三张催缴单。"],
        },
        {
            "order": 2,
            "title": "第一次看见",
            "narrative_function": "build",
            "pov": "林砚",
            "location": "写字楼电梯口",
            "emotion_target": "困惑和好奇",
            "conflict_type": "人与自我",
            "dialogue_ratio": 0.2,
            "length": 500,
            "key_lines": ["老人头顶浮着一排数字。", "他停了一下。"],
        },
        {
            "order": 3,
            "title": "反差",
            "narrative_function": "conflict",
            "pov": "林砚",
            "location": "客户家",
            "emotion_target": "震惊和困惑",
            "conflict_type": "人与人",
            "dialogue_ratio": 0.5,
            "length": 500,
            "key_lines": ["光鲜体面的客户，头顶价格在快速下跌。", "\"您的外卖。\" 他尽量让自己看起来正常。"],
        },
        {
            "order": 4,
            "title": "第一次失误",
            "narrative_function": "climax_payoff",
            "pov": "林砚",
            "location": "回程路上",
            "emotion_target": "挫败和反思",
            "conflict_type": "人与系统",
            "dialogue_ratio": 0.1,
            "length": 400,
            "key_lines": ["他以为标签代表财富。", "结果判断错了。"],
        },
        {
            "order": 5,
            "title": "医院",
            "narrative_function": "cliffhanger",
            "pov": "林砚",
            "location": "医院缴费窗口",
            "emotion_target": "绝望和紧迫",
            "conflict_type": "人与系统",
            "dialogue_ratio": 0.3,
            "length": 400,
            "key_lines": ["他爸头顶的价格正在归零。", "不是钱的问题。"],
        },
    ],
}

DEMO_REVIEW = {
    "chapter_number": 1,
    "dimensions": {
        "tension": {"score": 7, "issue": "开头压抑感铺垫稍长", "suggestion": "接单场景可以更短，直接进电梯遇到老人"},
        "pacing": {"score": 6, "issue": "第三、四场景之间过渡有一点拖", "suggestion": "客户家出来后直接切到路上想事情"},
        "dialogue": {"score": 5, "issue": "老人和客户的对话口吻差异不够明显", "suggestion": "老人用更短促的句子，客户用更礼貌但冷淡的语气"},
        "character_consistency": {"score": 8, "issue": "基本一致", "suggestion": "林砚的克制性格在对话中还可以更明显"},
        "hook": {"score": 9, "issue": "章尾归零钩子强", "suggestion": "保留"},
        "world_consistency": {"score": 8, "issue": "世界观初步建立", "suggestion": "可以增加一个标签闪烁的细节暗示能力不稳定"},
        "emotion_delivery": {"score": 6, "issue": "部分情绪用'他感到'句式表达", "suggestion": "替换为具体动作"},
        "prose_quality": {"score": 6, "issue": "部分句子偏长", "suggestion": "动作场景多用短句"},
        "readability": {"score": 7, "issue": "整体可读", "suggestion": "去 AI 腔后更好"},
        "ai_flavor_level": {"score": 6, "issue": "多处使用'他感到''仿佛''似乎'，对话略显模板化", "suggestion": "参考 deai_rules/examples.md 逐句改写"},
    },
    "verdict": {
        "passed": False,
        "overall_score": 6.5,
        "critical_issues": [
            "ai_flavor_level 6/10，超过通过线 4/10",
            "部分情绪使用'他感到'句式，需改写",
        ],
        "minor_issues": [
            "老人和客户对话口吻差异不够",
            "开头接单场景可再紧凑",
        ],
    },
}

DEMO_POLISHED_EXCERPT = """林砚把手机按灭，拧转油门。

望江路 18 号。他没看导航——这条街他跑了大半年，闭着眼都知道哪栋楼有几个门洞。

电梯停在六楼，门开的时候走廊里站着一个穿灰中山装的老人，正低头看手机。林砚往旁边让了让，余光扫过去——他愣住了。

老人头顶浮着一排数字。

不是贴在墙上那种，是悬在半空中，像是透明投影又像是视网膜上的残影。他眨了一下眼，数字还在。

302 的门开了。一个穿衬衫戴手表的男人站在门口，冲他点了下头。林砚把餐递过去，视线落在那人头顶——又是一排数字，但和老人的完全不一样。

老人的数字大得离谱。这个人的数字却在往下掉，像沙漏一样一粒一粒地碎。

林砚攥紧了手机。

他爸还躺在医院里。"""

DEMO_COMMIT = {
    "chapter_number": 1,
    "commit_type": "initial",
    "previous_version": None,
    "current_version": "v1",
    "changes": {
        "plot_events": [
            "林砚在送外卖途中第一次看见人生价格标签",
            "发现老人头顶价格异常高、客户价格在下跌",
            "判断失误——标签不代表财富",
            "在医院看见父亲头顶价格即将归零",
        ],
        "character_updates": [
            "林砚：发现能力，处于困惑和试错阶段",
            "父亲（未具名）：价格归零边缘，病重",
        ],
        "world_updates": [
            "价格标签规则初步显露：与财富不完全相关",
            "能力有代价：使用后头痛",
        ],
        "dialogue_signatures": [
            "客户含蓄表达：'这附近最近不太平'（伏笔）",
            "老人简短回应，暗示价格标签和人的选择有关（伏笔）",
        ],
    },
    "affected_elements": {
        "characters": ["林砚", "父亲"],
        "threads": ["能力起源", "父亲医疗费", "价格标签真相"],
        "foreshadowing": [
            "第4段提及'老人好像认识他'，暗示老人可能知道更多",
            "客户提及'不太平'为后续事件铺垫",
        ],
    },
    "canon_sync": {"synced": False, "canon_version": "待更新"},
}

DEMO_RUNTIME_CANON = {
    "version": "v1",
    "current_chapter": 1,
    "last_updated": datetime.now().isoformat(),
    "timeline": [
        {
            "chapter": 1,
            "event": "林砚在送餐过程中首次看见人生价格标签，通过老人和客户的对比意识到标签不代表财富。在医院缴费窗口看见父亲头顶价格归零。",
            "impact": "主角获得能力认知，但处于试错阶段。父亲状况成为核心驱动力。",
            "involved": ["林砚"],
        }
    ],
    "character_states": {
        "林砚": {
            "status": "发现能力，负债压力大",
            "price_tag": "归零边缘",
            "notable_changes": ["首次使用能力", "判断失误一次"],
        }
    },
    "active_threads": [
        {"thread": "能力起源和真相", "status": "open", "last_chapter": 1},
        {"thread": "父亲医疗费", "status": "open", "last_chapter": 1},
        {"thread": "价格标签的规则", "status": "open", "last_chapter": 1},
    ],
}

DEMO_STATE_PROJECTION = {
    "project": {
        "name": "人生价格标签",
        "genre": "都市脑洞",
        "current_chapter": 1,
        "total_planned": 30,
        "current_arc": "觉醒与试错（1-10章）",
    },
    "character_status": [
        {
            "name": "林砚",
            "price_tag": "归零边缘",
            "summary": "24岁外卖员，刚发现能看到价格标签的能力，在医院面对父亲即将归零的价格。"
        }
    ],
    "threads": [
        {"name": "能力起源", "status": "待探索"},
        {"name": "父亲医疗费", "status": "紧迫"},
        {"name": "价格标签真相", "status": "刚发现"},
    ],
    "latest_chapter_summary": "林砚在送外卖时第一次看见价格标签。他发现穿中山装的老人价格高得离谱，光鲜的客户价格却在下跌。他以为标签代表财富，判断失误。章尾在医院看见父亲头顶价格即将归零。",
}


# ── 文件操作 ──────────────────────────────────────────────

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    return path


def write_yaml(path, data):
    import yaml
    Path(path).write_text(
        yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )


def write_json(path, data):
    Path(path).write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# ── 步骤函数 ──────────────────────────────────────────────

def step_create_project(project_dir):
    """创建项目目录和 project.yaml"""
    ensure_dir(project_dir)
    ensure_dir(project_dir / ".story-system")
    ensure_dir(project_dir / ".story-system" / "chapter_commits")
    ensure_dir(project_dir / ".webnovel" / "context")
    ensure_dir(project_dir / ".webnovel" / "state")
    ensure_dir(project_dir / "outlines" / "beats")
    ensure_dir(project_dir / "manuscript" / "drafts")
    ensure_dir(project_dir / "manuscript" / "polished")
    ensure_dir(project_dir / "manuscript" / "chapters")
    ensure_dir(project_dir / "reviews")
    ensure_dir(project_dir / "wps")
    ensure_dir(project_dir / "exports")

    write_yaml(project_dir / "project.yaml", DEMO_PROJECT)
    return {"step": "create_project", "status": "ok", "path": str(project_dir / "project.yaml")}


def step_generate_bible(project_dir):
    """生成 MASTER_SETTING.yaml"""
    write_yaml(project_dir / ".story-system" / "MASTER_SETTING.yaml", DEMO_MASTER_SETTING)
    return {"step": "generate_bible", "status": "ok (mock)", "path": str(project_dir / ".story-system" / "MASTER_SETTING.yaml")}


def step_generate_outline(project_dir):
    """生成前 30 章大纲"""
    chapters = []
    for i in range(1, 31):
        chapters.append({
            "number": i,
            "title": f"第{i}章",
            "conflict": f"冲突{i}" if i > 1 else "林砚急需钱，但还不知道标签真正代表什么",
            "hook": f"钩子{i}" if i > 1 else "父亲头顶价格即将归零",
        })
    outlines = {
        "project": "price_tag_life",
        "total_outlined": 30,
        "overview": "前 30 章：觉醒与试错(1-10) → 成长与博弈(11-20) → 真相与抉择(21-30)",
        "chapters": chapters,
    }
    write_yaml(project_dir / "outlines" / "chapters_001_030.yaml", outlines)
    return {"step": "generate_outline", "status": "ok (mock)", "path": str(project_dir / "outlines" / "chapters_001_030.yaml")}


def step_build_context(project_dir):
    """生成 chapter_001 写作上下文"""
    context = """# 第1章写作上下文

## 当前状态
- 上一章结束时：无（第1章）
- 林砚：24岁外卖员，父亲住院欠债，刚收工
- 待解决线索：无（开局）

## 注意事项
1. 林砚的性格是克制、敏感——不要写成热血冲动型
2. 能力初次出现要让人有真实感，不要写成系统文面板
3. 标签不是财富，这一点要在本章结尾读者才能完全理解

## 去AI腔提醒
- 最容易出现："他感到震惊""他意识到"
- 替换方向：用具体动作（手指停在按钮上、手机掉落）"""
    Path(project_dir / ".webnovel" / "context" / "chapter_001_context.md").write_text(context, encoding="utf-8")
    return {"step": "build_context", "status": "ok (mock)", "path": str(project_dir / ".webnovel" / "context" / "chapter_001_context.md")}


def step_generate_beat(project_dir):
    """生成 chapter_001 beat"""
    write_yaml(project_dir / "outlines" / "beats" / "chapter_001.yaml", DEMO_CHAPTER_001)
    return {"step": "generate_beat", "status": "ok (mock)", "path": str(project_dir / "outlines" / "beats" / "chapter_001.yaml")}


def step_write_draft(project_dir):
    """写第1章草稿"""
    draft = """# 第1章 归零

手机又震了一下。

林砚低头看了一眼——新订单，望江路18号302室。他拧转油门，电动车在晚高峰的车流里钻出一条路。

等红灯的时候他看了一眼银行余额。四位数的欠款，三位数的余额。他按掉屏幕，没再看。

六分钟后他站在一栋老式写字楼的电梯里。楼层数字一格一格往上跳。电梯门开的时候走廊里站着一个穿灰中山装的老人，正低头看手机。

林砚本来没在意。但他从老人身边经过时，余光扫到老人头顶——那里浮着一排数字。

不是贴墙上的那种。是悬在半空中，像是透明投影，又像是视网膜上的残影。他眨了一下眼，数字还在。

他停了一下。

---

302的门开了。一个三十多岁的男人站在门口，衬衫袖口卷到小臂，手表的表盘在灯光下闪了一下。

"您的外卖。"林砚把袋子递过去。

那人接过袋子的时候，林砚的视线落在他头顶——又是一排数字。

和老人完全不一样。

老人的数字大得离谱。这个人的数字却在往下掉，像是沙漏里的沙子，一粒一粒地从末尾消失。

林砚攥紧了手机。

---

回去的路上他脑子里一直在转。那些数字什么意思？为什么老人那么高、客户那么低？客户穿得好、住得好、还有那块表——怎么可能是穷人？

所以数字代表钱？老人穿中山装不像有钱人，但他数字高。

那数字到底代表什么？

他骑到半路，手机又响了。不是新订单——是医院发来的缴费提醒。

他拐了个弯往医院骑。

---

缴费窗口的护士头也没抬："尾号3847，住院费还差两万三。"

林砚掏出手机。余额不够。他还想说什么，余光扫过窗口旁边的病房门口——他爸正躺在里面，隔着玻璃能看到监护仪的绿线一跳一跳。

然后他看见了他爸头顶的数字。

它在慢慢归零。

不是钱的问题。

"""

    Path(project_dir / "manuscript" / "drafts" / "chapter_001_draft.md").write_text(draft.strip(), encoding="utf-8")
    return {"step": "write_draft", "status": "ok (mock)", "path": str(project_dir / "manuscript" / "drafts" / "chapter_001_draft.md")}


def step_review(project_dir):
    """审稿"""
    write_yaml(project_dir / "reviews" / "chapter_001_review.yaml", DEMO_REVIEW)
    return {"step": "review", "status": "ok (mock)", "path": str(project_dir / "reviews" / "chapter_001_review.yaml")}


def step_polish(project_dir):
    """润色"""
    polished = f"""## 改写说明

本次改写主要针对：替换"他感到"类句式、删除解释性旁白、强化对话口吻差异。核心情节不变。

--- | REWRITTEN

{DEMO_POLISHED_EXCERPT}
"""
    Path(project_dir / "manuscript" / "polished" / "chapter_001_polished.md").write_text(polished.strip(), encoding="utf-8")
    return {"step": "polish", "status": "ok (mock)", "path": str(project_dir / "manuscript" / "polished" / "chapter_001_polished.md")}


def step_commit(project_dir):
    """生成 chapter_commit"""
    write_yaml(project_dir / ".story-system" / "chapter_commits" / "chapter_001_commit.yaml", DEMO_COMMIT)
    return {"step": "commit", "status": "ok (mock)", "path": str(project_dir / ".story-system" / "chapter_commits" / "chapter_001_commit.yaml")}


def step_finalize(project_dir):
    """生成最终正文"""
    draft_path = project_dir / "manuscript" / "drafts" / "chapter_001_draft.md"
    polished_path = project_dir / "manuscript" / "polished" / "chapter_001_polished.md"
    final_path = project_dir / "manuscript" / "chapters" / "chapter_001_final.md"

    if polished_path.exists():
        content = polished_path.read_text(encoding="utf-8")
        # 去掉改写说明和标记
        cleaned = content.split("--- | REWRITTEN")[-1].strip()
        final_path.write_text(cleaned, encoding="utf-8")
    elif draft_path.exists():
        final_path.write_text(draft_path.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        return {"step": "finalize", "status": "failed", "reason": "无草稿或润色文件"}

    return {"step": "finalize", "status": "ok", "path": str(final_path)}


def step_update_canon(project_dir):
    """更新 runtime_canon"""
    write_yaml(project_dir / ".story-system" / "runtime_canon.yaml", DEMO_RUNTIME_CANON)
    return {"step": "update_canon", "status": "ok (mock)", "path": str(project_dir / ".story-system" / "runtime_canon.yaml")}


def step_project_state(project_dir):
    """更新 .webnovel/state.yaml"""
    write_yaml(project_dir / ".webnovel" / "state.yaml", DEMO_STATE_PROJECTION)
    return {"step": "project_state", "status": "ok (mock)", "path": str(project_dir / ".webnovel" / "state.yaml")}


# ── 验证 ──────────────────────────────────────────────

def validate_demo(project_dir):
    """验证 Demo 输出完整性"""
    checks = []

    required_files = [
        "project.yaml",
        ".story-system/MASTER_SETTING.yaml",
        "outlines/chapters_001_030.yaml",
        ".webnovel/context/chapter_001_context.md",
        "outlines/beats/chapter_001.yaml",
        "manuscript/drafts/chapter_001_draft.md",
        "reviews/chapter_001_review.yaml",
        "manuscript/polished/chapter_001_polished.md",
        ".story-system/chapter_commits/chapter_001_commit.yaml",
        "manuscript/chapters/chapter_001_final.md",
        ".story-system/runtime_canon.yaml",
        ".webnovel/state.yaml",
    ]

    # 添加 Schema 检查
    schema_files = [
        "master_setting.schema.yaml",
        "runtime_canon.schema.yaml",
        "chapter_outline.schema.yaml",
        "chapter_beat.schema.yaml",
        "review_report.schema.yaml",
        "chapter_commit.schema.yaml",
    ]

    all_pass = True
    for f in required_files:
        p = project_dir / f
        exists = p.exists()
        size = p.stat().st_size if exists else 0
        checks.append({"file": f, "exists": exists, "size_bytes": size})
        if not exists:
            all_pass = False

    schema_pass = True
    for sf in schema_files:
        p = CODE_ROOT / "schemas" / sf
        exists = p.exists()
        try:
            if exists:
                import yaml
                yaml.safe_load(p.read_text())
            checks.append({"file": f"schemas/{sf}", "exists": exists, "parsable": True})
        except Exception:
            checks.append({"file": f"schemas/{sf}", "exists": exists, "parsable": False})
            schema_pass = False

    return {
        "passed": all_pass and schema_pass,
        "file_count": len(required_files) + len(schema_files),
        "all_exist": all_pass,
        "schema_ok": schema_pass,
        "detailed_checks": checks,
    }


# ── 主流程 ──────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  webnovel-hermes-wps Demo — 人生价格标签")
    print("  当前模式: mock/demo（不调用 DeepSeek API）")
    print("=" * 55)
    print()

    project_name = DEMO_PROJECT["project_name"]
    book_title = DEMO_PROJECT["book_title"]
    project_dir = DATA_ROOT / "workspace" / "novels" / project_name

    # 执行步骤
    steps = [
        step_create_project,
        step_generate_bible,
        step_generate_outline,
        step_build_context,
        step_generate_beat,
        step_write_draft,
        step_review,
        step_polish,
        step_commit,
        step_finalize,
        step_update_canon,
        step_project_state,
    ]

    results = []
    for step_fn in steps:
        name = step_fn.__name__.replace("step_", "")
        print(f"  [{name}] ... ", end="", flush=True)
        try:
            r = step_fn(project_dir)
            print(f"✅ {r.get('status', 'ok')}")
            results.append(r)
        except Exception as e:
            print(f"❌ {e}")
            results.append({"step": name, "status": "failed", "error": str(e)})

    print()

    # 验证
    print("  [validate] ... ", end="", flush=True)
    validation = validate_demo(project_dir)
    if validation["passed"]:
        print(f"✅ 通过 ({validation['file_count']} 项检查)")
    else:
        failed = [c["file"] for c in validation["detailed_checks"] if not c.get("exists", False)]
        print(f"❌ 失败: {len(failed)} 项缺失: {', '.join(failed)}")

    print()

    # 输出到 demo_output/
    demo_output_dir = ensure_dir(DATA_ROOT / "demo_output")
    demo_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # demo_result.md
    md_lines = [
        f"# Demo 结果 — {book_title}",
        "",
        f"**执行时间：** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "**模式：** mock/demo（不调用 DeepSeek API）",
        "",
        "## 执行步骤",
        "",
    ]
    for i, r in enumerate(results, 1):
        status_icon = "✅" if r.get("status", "").startswith("ok") else "❌"
        step_name = r["step"]
        extra = f" → {r.get('path', '')}" if "path" in r else ""
        md_lines.append(f"{i}. {status_icon} {step_name}{extra}")

    md_lines.extend([
        "",
        "## 验证结果",
        f"- 通过: {'是' if validation['passed'] else '否'}",
        f"- 文件检查: {validation['all_exist']}",
        f"- Schema 解析: {validation['schema_ok']}",
        "",
        "## 输出路径",
        f"- 项目目录: {project_dir}/",
        f"- Demo 输出: {demo_output_dir}/",
        "",
        "## 项目文件清单",
    ])
    for c in validation["detailed_checks"]:
        if "parsable" in c:
            md_lines.append(f"- {'✅' if c['exists'] and c['parsable'] else '❌'} schemas/{c['file']}")
        else:
            md_lines.append(f"- {'✅' if c['exists'] else '❌'} {c['file']} ({c['size_bytes']} bytes)")

    md_path = demo_output_dir / "demo_result.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"  ✅ demo_result.md → {md_path}")

    # demo_result.json
    demo_json = {
        "project": DEMO_PROJECT,
        "execution_time": datetime.now().isoformat(),
        "mode": "mock",
        "steps": results,
        "validation": validation,
    }
    json_path = demo_output_dir / "demo_result.json"
    write_json(json_path, demo_json)
    print(f"  ✅ demo_result.json → {json_path}")

    # validation_report.json
    val_path = demo_output_dir / "validation_report.json"
    write_json(val_path, validation)
    print(f"  ✅ validation_report.json → {val_path}")

    print()
    print("=" * 55)
    if validation["passed"]:
        print("  Demo 完成 ✅ — 所有文件就绪")
    else:
        print("  Demo 完成 ⚠️ — 存在未通过项")
    print("=" * 55)


if __name__ == "__main__":
    main()
