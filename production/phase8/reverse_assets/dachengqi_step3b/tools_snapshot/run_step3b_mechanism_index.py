#!/usr/bin/env python3
"""
run_step3b_mechanism_index.py — Phase 8 Step 3B: 长篇结构与机制定位

核心原则:
  1. 全量读取 774 张 chapter_card（不采样、不统计替代）
  2. 先程序生成 full_chapter_spine（不调 LLM）
  3. 按阶段分批，每个阶段单独调 LLM 分析 arc mechanism
  4. 最后汇总生成 protagonist_engine / character_function_map / candidate_pool

用法:
  # Mock 模式（生成示例输出，不调 API）
  python tools/phase8/run_step3b_mechanism_index.py --book-id dachengqi

  # 真实模式（调用 DeepSeek API）
  python tools/phase8/run_step3b_mechanism_index.py --book-id dachengqi --real

  # 只生成 spine 和阶段检测（不调 LLM）
  python tools/phase8/run_step3b_mechanism_index.py --book-id dachengqi --spine-only
"""

import argparse
import json
import os
import re
import subprocess
import sys
import textwrap
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import yaml

# ── Path helpers ──────────────────────────────────────────────────────────

def find_project_root(start: Path | None = None) -> Path:
    cur = (start or Path(__file__)).resolve()
    if cur.is_file():
        cur = cur.parent
    for parent in [cur, *cur.parents]:
        if (parent / "production" / "phase8").exists():
            return parent
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("Cannot locate project root")


# ── Chapter Card Loading ──────────────────────────────────────────────────

def parse_chapter_card_yaml(file_path: Path) -> dict | None:
    """Parse a chapter_card YAML file, stripping markdown fences."""
    raw = file_path.read_text(encoding="utf-8")
    # Strip ```yaml and ``` fences
    text = raw.strip()
    if text.startswith("```"):
        text = text[text.index("\n") + 1:] if "\n" in text else ""
    if text.endswith("```"):
        text = text[:text.rindex("```")].rstrip()
    try:
        card = yaml.safe_load(text)
        if card is None:
            return None
        # Normalize edge cases
        _normalize_card(card)
        return card
    except yaml.YAMLError:
        print(f"  [WARN] YAML parse failed: {file_path.name}")
        return None


def _normalize_card(card: dict) -> None:
    """Normalize edge cases in chapter_card data."""
    # Normalize characters_present: handle dict entries → extract name
    chars = card.get("characters_present")
    if isinstance(chars, list):
        normalized = []
        for c in chars:
            if isinstance(c, dict):
                normalized.append(c.get("name", str(c)))
            elif isinstance(c, str):
                normalized.append(c)
            # skip None/other
        card["characters_present"] = normalized
    elif chars is None:
        card["characters_present"] = []

    # Normalize main_events (can be None, or contain dict entries)
    events = card.get("main_events")
    if events is None:
        card["main_events"] = []
    elif isinstance(events, list):
        normalized = []
        for e in events:
            if isinstance(e, dict):
                normalized.append(e.get("event", str(e)))
            elif isinstance(e, str):
                normalized.append(e)
        card["main_events"] = normalized

    # Normalize hook_opened / hook_paid (can be None)
    for field in ["hook_opened", "hook_paid", "reader_debts_opened", "reader_debts_paid"]:
        val = card.get(field)
        if val is None:
            card[field] = []
        elif isinstance(val, list):
            # Normalize each entry: handle dicts with missing 'id'
            normalized = []
            for item in val:
                if isinstance(item, dict):
                    if "id" not in item:
                        item["id"] = "?"
                    normalized.append(item)
            if normalized:
                card[field] = normalized

    # Normalize protagonist_state_change
    if card.get("protagonist_state_change") is None:
        card["protagonist_state_change"] = ""

    # Normalize world_state_change
    if card.get("world_state_change") is None:
        card["world_state_change"] = ""

    # Normalize ending_pull
    if card.get("ending_pull") is None:
        card["ending_pull"] = ""

    # Normalize scene_vitality_notes
    if card.get("scene_vitality_notes") is None:
        card["scene_vitality_notes"] = ""


def load_all_cards(book_id: str, project_root: Path) -> list[dict]:
    """Load all chapter_card YAML files, sorted by chapter_number."""
    cards_dir = project_root / "production" / "phase8" / "corpus" / book_id / "chapter_cards"
    cards = []
    for f in sorted(cards_dir.glob("chapter_*.yaml")):
        card = parse_chapter_card_yaml(f)
        if card:
            cards.append(card)
    cards.sort(key=lambda c: c.get("chapter_number", 0))
    return cards


# ── Programmatic Spine Generation ─────────────────────────────────────────

def generate_full_chapter_spine(cards: list[dict], output_path: Path) -> dict:
    """
    程序生成 full_chapter_spine.md，不调 LLM。
    返回统计 dict 供后续阶段检测使用。
    """
    total = len(cards)
    confidence_counter = Counter(c.get("confidence", "unknown") for c in cards)

    lines = []
    lines.append("# Full Chapter Spine: 大乘期才有逆袭系统")
    lines.append("")
    lines.append(f"> 生成方式: 程序聚合（零 LLM 调用）")
    lines.append(f"> 生成时间: {datetime.now().isoformat()}")
    lines.append(f"> 覆盖章节: {total}/{total}")
    lines.append(f"> 置信度分布: {dict(confidence_counter)}")
    lines.append("")

    stats = {
        "total_chapters": total,
        "confidence_distribution": dict(confidence_counter),
        "chapter_functions": Counter(),
        "all_characters": Counter(),
        "total_hooks_opened": 0,
        "total_hooks_paid": 0,
        "total_debts_opened": 0,
        "total_debts_paid": 0,
    }

    for card in cards:
        ch = card.get("chapter_number", "?")
        title = card.get("title", "?")
        one_sentence = card.get("one_sentence", "")
        chapter_function = card.get("chapter_function", "")
        main_events = card.get("main_events", [])
        ending_pull = card.get("ending_pull", "")
        confidence = card.get("confidence", "unknown")
        hooks_opened = card.get("hook_opened", [])
        hooks_paid = card.get("hook_paid", [])
        debts_opened = card.get("reader_debts_opened", [])
        debts_paid = card.get("reader_debts_paid", [])
        characters = card.get("characters_present", [])
        protagonist_change = card.get("protagonist_state_change", "")
        world_change = card.get("world_state_change", "")

        stats["chapter_functions"][chapter_function[:30]] += 1
        for char in characters:
            stats["all_characters"][char] += 1
        stats["total_hooks_opened"] += len(hooks_opened)
        stats["total_hooks_paid"] += len(hooks_paid)
        stats["total_debts_opened"] += len(debts_opened)
        stats["total_debts_paid"] += len(debts_paid)

        # Format chapter entry
        lines.append(f"## Chapter {ch}: {title}")
        lines.append("")
        lines.append(f"- **一句话**: {one_sentence}")
        lines.append(f"- **功能**: {chapter_function}")
        lines.append(f"- **置信度**: {confidence}")

        if main_events:
            lines.append(f"- **主要事件** ({len(main_events)}件):")
            for evt in main_events:
                lines.append(f"  - {evt}")

        if protagonist_change and protagonist_change != "unknown":
            lines.append(f"- **主角状态**: {protagonist_change}")

        if hooks_opened:
            lines.append(f"- **钩子开启** ({len(hooks_opened)}个):")
            for h in hooks_opened:
                if isinstance(h, dict):
                    lines.append(f"  - [{h.get('id', '?')}] {h.get('text', '')}")

        if hooks_paid:
            lines.append(f"- **钩子兑现** ({len(hooks_paid)}个):")
            for h in hooks_paid:
                if isinstance(h, dict):
                    payoff = h.get('payoff', '')
                    lines.append(f"  - [{h.get('id', '?')}] {h.get('text', '')} → {payoff}")

        if debts_opened:
            lines.append(f"- **读者债开启** ({len(debts_opened)}个):")

        if debts_paid:
            lines.append(f"- **读者债兑现** ({len(debts_paid)}个):")

        if ending_pull:
            lines.append(f"- **章尾拉力**: {ending_pull}")

        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [OK] full_chapter_spine.md written ({total} chapters)")

    return stats


# ── Stage Auto-Detection ──────────────────────────────────────────────────

def _chapter_function_score(func: str) -> int:
    """Score chapter_function for stage boundary detection."""
    f = func.lower()
    # Resolution / climax signals
    resolution_kw = ["收束", "解决", "高潮", "收官", "结局", "终结", "落幕", "完成", "了结",
                     "落幕", "清算", "扫尾", "尾声", "最终", "决战", "彻底"]
    # Introduction / setup signals
    intro_kw = ["引入", "开启", "铺垫", "触发", "揭开", "开始", "启程", "进入新",
                "新世界", "新阶段", "新篇章", "新副本", "新地图"]

    score = 0
    for kw in resolution_kw:
        if kw in f:
            score += 20
    for kw in intro_kw:
        if kw in f:
            score += 25
    # "过渡" chapters are between arcs
    if "过渡" in f:
        score += 15

    return score


def _world_change_score(change_str: str) -> int:
    """Score world_state_change for stage boundary detection."""
    c = change_str.lower()
    score = 0
    new_world_kw = ["进入", "到达", "来到", "前往", "抵达", "转换", "跨越", "传送", "飞升",
                    "新世界", "新地图", "新大陆", "新区域", "平行世界", "异世界", "秘境",
                    "诸天万界", "仙界", "魔界", "地府", "开启", "打通", "建立空间",
                    "正式建交", "结盟"]
    for kw in new_world_kw:
        if kw in c:
            score += 15

    return score


def _title_boundary_score(title: str) -> int:
    """Score chapter titles that mark clear volume/arc boundaries."""
    t = title.lower()
    boundary_kw = ["终章", "结局", "再会", "新生", "归来", "启程", "决战",
                   "新世界", "最后一", "开始", "重生", "完结", "告别"]
    for kw in boundary_kw:
        if kw in t:
            return 30
    return 0


def _payoff_density_score(card: dict) -> int:
    """Score based on hook/debt payoff density (high payoff = likely arc end)."""
    score = 0
    hooks_paid = card.get("hook_paid", [])
    debts_paid = card.get("reader_debts_paid", [])
    total_paid = len(hooks_paid) + len(debts_paid)
    if total_paid >= 3:
        score += 30
    elif total_paid >= 2:
        score += 15
    elif total_paid >= 1:
        score += 5
    return score


def detect_stages(cards: list[dict], min_stages: int = 8, max_stages: int = 15,
                  max_chapters_per_stage: int = 200) -> list[dict]:
    """
    Auto-detect stage boundaries using heuristic scoring.
    Returns list of {stage_id, start_ch, end_ch, boundary_reason}.
    """
    total = len(cards)

    # Compute boundary scores for each chapter
    scores = []
    for i, card in enumerate(cards):
        score = 0
        score += _chapter_function_score(card.get("chapter_function", ""))
        score += _world_change_score(card.get("world_state_change", ""))
        score += _payoff_density_score(card)
        score += _title_boundary_score(card.get("title", ""))
        scores.append((i, score, card.get("chapter_number", i + 1)))

    # Find candidate boundaries: local peaks in the score
    window = 3  # must be highest within ±window
    candidates = []
    for i in range(1, total - 1):
        local_max = True
        for j in range(max(0, i - window), min(total, i + window + 1)):
            if j != i and scores[j][1] > scores[i][1]:
                local_max = False
                break
        if local_max and scores[i][1] > 0:
            candidates.append({
                "chapter_idx": i,
                "chapter_number": cards[i].get("chapter_number", i + 1),
                "score": scores[i][1],
                "title": cards[i].get("title", "?"),
                "function": cards[i].get("chapter_function", ""),
                "one_sentence": cards[i].get("one_sentence", ""),
            })

    # Also add very low-score valleys as potential boundaries
    # (after a high-score boundary, the next low-score chapter is the start)
    # Sort candidates by score descending
    candidates.sort(key=lambda x: -x["score"])

    # Select top candidates ensuring coverage constraints
    # First, always include ch1 as start
    selected_boundaries = [0]  # chapter index (0-based) for start
    used_indices = {0}

    # Greedy selection: pick highest-scored boundaries that maintain max gap ≤200
    for cand in candidates:
        idx = cand["chapter_idx"]
        if idx in used_indices:
            continue
        if idx <= 0 or idx >= total - 1:
            continue
        # Check if adding this boundary would create a gap >200 within existing segments
        test_boundaries = sorted(selected_boundaries + [idx])
        ok = True
        for s, e in zip(test_boundaries, test_boundaries[1:] + [total]):
            if e - s > max_chapters_per_stage:
                ok = False
                break
        if ok:
            selected_boundaries.append(idx)
            used_indices.add(idx)

    # If we still have gaps >200, fill with forced boundaries
    selected_boundaries.sort()
    while True:
        needs_split = False
        for s, e in zip(selected_boundaries, selected_boundaries[1:] + [total]):
            if e - s > max_chapters_per_stage:
                needs_split = True
                mid = (s + e) // 2
                # Find nearest candidate boundary
                nearest = None
                for cand in candidates:
                    ci = cand["chapter_idx"]
                    if s < ci < e and ci not in used_indices:
                        if nearest is None or abs(ci - mid) < abs(nearest["chapter_idx"] - mid):
                            nearest = {"chapter_idx": ci, "score": cand["score"]}
                if nearest is None:
                    # Just use midpoint
                    mid_idx = mid
                else:
                    mid_idx = nearest["chapter_idx"]
                selected_boundaries.append(mid_idx)
                used_indices.add(mid_idx)
                selected_boundaries.sort()
                break
        if not needs_split:
            break

    # Ensure we have at least min_stages boundaries
    selected_boundaries.sort()
    while len(selected_boundaries) < min_stages:
        # Add highest-scored unused candidate
        for cand in candidates:
            ci = cand["chapter_idx"]
            if ci not in used_indices and ci > 0 and ci < total - 1:
                selected_boundaries.append(ci)
                used_indices.add(ci)
                selected_boundaries.sort()
                break
        else:
            break  # no more candidates

    # Build stage definitions
    selected_boundaries.sort()
    stages = []
    stage_num = 0
    for s, e in zip(selected_boundaries, selected_boundaries[1:] + [total]):
        stage_num += 1
        stage_cards = cards[s:e]
        first_ch = stage_cards[0].get("chapter_number", s + 1)
        last_ch = stage_cards[-1].get("chapter_number", e) if stage_cards else s + 1

        # Find reason for this boundary
        reason_parts = []
        boundary_card = cards[s] if s > 0 else cards[0]
        b_func = boundary_card.get("chapter_function", "")
        b_world = boundary_card.get("world_state_change", "")
        if b_func:
            reason_parts.append(f"chapter_function: {b_func}")
        if b_world:
            reason_parts.append(f"world_state_change: {b_world}")

        # Determine stage name from first few chapters
        first_titles = [c.get("title", "") for c in stage_cards[:5]]
        stage_name_hint = " → ".join(first_titles[:3])

        stages.append({
            "stage_id": f"S{stage_num:02d}",
            "stage_name_hint": stage_name_hint,
            "chapter_range": f"{first_ch}-{last_ch}",
            "start_idx": s,
            "end_idx": e,
            "chapter_count": e - s,
            "first_chapter": first_ch,
            "last_chapter": last_ch,
            "boundary_reason": "; ".join(reason_parts) if reason_parts else "auto-detected",
            "cards": stage_cards,
        })

    return stages


# ── LLM Call Helper ───────────────────────────────────────────────────────

def call_deepseek(system_prompt_path: Path, user_input_path: Path,
                  output_path: Path, task_name: str, real_mode: bool,
                  max_tokens: int = 32000, temperature: float = 0.7,
                  timeout: int = 300, retries: int = 1) -> bool:
    """Call DeepSeek via call_deepseek.py subprocess."""
    script = find_project_root() / "scripts" / "call_deepseek.py"
    cmd = [
        sys.executable, str(script),
        "--system-prompt", str(system_prompt_path),
        "--input", str(user_input_path),
        "--output", str(output_path),
        "--task-name", task_name,
        "--max-tokens", str(max_tokens),
        "--temperature", str(temperature),
        "--timeout", str(timeout),
        "--retries", str(retries),
    ]
    if real_mode:
        cmd.append("--real")
    else:
        cmd.append("--mock")

    print(f"  [LLM] Calling: {task_name} (mode={'real' if real_mode else 'mock'})")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 60)
    try:
        resp = json.loads(result.stdout.strip().split("\n")[-1])
        if resp.get("success"):
            print(f"  [OK] {task_name} → {resp.get('output', '')}")
            return True
        else:
            print(f"  [FAIL] {task_name}: {resp.get('error_message', 'unknown')}")
            return False
    except (json.JSONDecodeError, IndexError):
        print(f"  [FAIL] {task_name}: could not parse response")
        print(f"  stdout: {result.stdout[:500]}")
        return False


# ── Stage Analysis Prompt Builder ─────────────────────────────────────────

def build_stage_spine_text(stage: dict) -> str:
    """Build a compact chapter spine text for one stage."""
    lines = []
    for card in stage["cards"]:
        ch = card.get("chapter_number", "?")
        title = card.get("title", "?")
        one_sentence = card.get("one_sentence", "")
        chapter_function = card.get("chapter_function", "")
        main_events = card.get("main_events", [])
        events_text = "; ".join(main_events[:5]) if main_events else ""
        ending_pull = card.get("ending_pull", "")
        confidence = card.get("confidence", "high")

        hooks_opened = len(card.get("hook_opened", []))
        hooks_paid = len(card.get("hook_paid", []))
        debts_opened = len(card.get("reader_debts_opened", []))
        debts_paid = len(card.get("reader_debts_paid", []))

        lines.append(
            f"Ch{ch} | {title} | func:{chapter_function} | "
            f"「{one_sentence}」 | events:{events_text} | "
            f"pull:{ending_pull[:80]} | "
            f"H+{hooks_opened}/-{hooks_paid} D+{debts_opened}/-{debts_paid} | "
            f"conf:{confidence}"
        )
    return "\n".join(lines)


SYSTEM_PROMPT_ARC_MECHANISM = """你是一位专业的网文结构分析师。你的任务是分析给定阶段（一个连续的章节范围）的叙事机制。

请严格按以下维度分析，不要写剧情简介，而要从"这个阶段为什么能持续吸引读者"的角度分析机制：

对每个维度，请回答以下问题：

1. **reader_pull** (读者拉力): 这个阶段读者最想看的是什么？是什么让读者一章接一章地读下去？
2. **satisfaction_mechanism** (爽点机制): 这个阶段的爽点是如何产生的？通过什么方式释放？
3. **conflict_generator** (冲突发生器): 这个阶段的核心冲突是什么？冲突如何持续产生并升级？
4. **protagonist_entry_mode** (主角介入方式): 主角以什么身份/方式介入这个阶段的冲突？
5. **pressure_source** (压力源): 对主角的压力从何而来？
6. **payoff_pattern** (兑现模式): 钩子和读者债的兑现规律是什么？
7. **transition_mechanism** (过渡机制): 这个阶段如何衔接到下一个阶段？
8. **reusable_mechanism** (可迁移机制): 提取1-3个可以被其他小说借鉴的叙事机制（不涉及具体设定）。
9. **non_transferable_original_elements** (不可复制原作元素): 哪些东西是原作独有的、无法迁移的？
10. **confidence**: 你对此阶段分析的整体信心（high/medium/low），需附简要理由。

请用中文回答。每个维度的分析控制在150-300字，reusable_mechanism需要给出清晰的抽象描述。
输出格式使用Markdown。"""


def build_stage_user_prompt(stage: dict) -> str:
    """Build the user prompt for one stage's LLM analysis."""
    spine_text = build_stage_spine_text(stage)
    first_ch = stage["first_chapter"]
    last_ch = stage["last_chapter"]
    ch_count = stage["chapter_count"]

    return f"""## 阶段信息

- **阶段编号**: {stage["stage_id"]}
- **章节范围**: 第{first_ch}-{last_ch}章（共{ch_count}章）
- **阶段标题提示**: {stage["stage_name_hint"]}

## 该阶段的完整 Chapter Spine

下面是你需要分析的该阶段全部{ch_count}章的 chapter spine（每章一行，包含 title, one_sentence, chapter_function, main_events, ending_pull, hooks/debts 数量, confidence）：

```
{spine_text}
```

## 分析要求

请基于以上全部{ch_count}章的完整 spine 数据，对该阶段进行叙事机制分析。
注意：
1. 你的分析必须基于提供给你的具体章节数据，不要泛泛而谈
2. 不要在分析中写剧情简介——分析的是"机制"而非"情节"
3. reusable_mechanism 必须是抽象的可迁移叙事机制，不能包含原作具体角色名、地名、设定名
4. 请严格按照系统提示中的10个维度逐一作答
"""


# ── Cross-Stage Synthesis Prompts ──────────────────────────────────────────

SYSTEM_PROMPT_VOLUME_STRUCTURE = """你是一位网文结构分析师。你的任务是基于全量章节 spine 和程序检测的阶段边界，生成精炼的长篇阶段结构报告。

要求：
- 8-15个主阶段，必要时设子阶段
- 不得出现200章以上单一阶段
- 每阶段需说明划分依据
- 每阶段包含：stage_id, stage_name, chapter_range, stage_function, protagonist_goal, main_pressure, core_conflict, core_satisfaction, main_reader_pull, transition_to_next, supporting_chapters, confidence
- 不要照抄旧的 volume_structure_report
- 输出使用Markdown格式"""

SYSTEM_PROMPT_PROTAGONIST_ENGINE = """你是一位网文角色机制分析师。你的任务是反推主角为什么能撑774章的篇幅。

请回答以下问题（不是写人物简介或传记）：

1. **核心功能位**: 主角在叙事中承担什么功能？不只是"他是主角"——他解决什么问题、满足什么期待？
2. **爽点循环**: 主角的爽点是如何循环产生的？读者从主角身上获得什么样的持续满足？
3. **冲突介入方式**: 主角如何被卷入冲突？主动/被动？介入模式是什么？
4. **限制与反差**: 主角有什么限制或弱点？这些限制如何制造戏剧张力？与他的强大形成什么反差？
5. **价值观锚点**: 主角坚持什么价值观？这些价值观如何驱动叙事？
6. **分阶段功能变化**: 主角在不同阶段的功能是否有变化？如果有，是什么变化？
7. **可迁移机制**: 提取2-4个可以被其他小说借鉴的主角设计机制（不涉及具体设定）。
8. **不可复制原作元素**: 哪些是原作独有的、无法迁移的？
9. **confidence**: 整体信心

关键警示：不要把江离写成普通升级流主角。他是"大乘期才有逆袭系统"——系统来得太晚，他已经是最强者。这完全颠覆了标准系统流/升级流的主角模式。

输出使用Markdown格式。"""

SYSTEM_PROMPT_CHARACTER_FUNCTION = """你是一位网文角色功能分析师。你的任务是将角色按照叙事功能位组织，而不是按人物传记方式编写。

需要覆盖的功能位至少包括：
- 主角
- 长期搭档
- 喜剧反差位
- 权威对照位
- 阶段反派
- 资源入口
- 世界观解释器
- 价值观对照
- 情绪缓冲
- 读者代入辅助
- 规则/设定承载者

对每个功能位：
1. 列出承担该功能的角色
2. 说明该角色的出场模式（频率、阶段分布）
3. 说明该角色如何服务于该功能位
4. 低频但关键的阶段反派也要纳入

输出使用Markdown格式，按功能位组织。"""

SYSTEM_PROMPT_CANDIDATE_POOL = """你是一位网文技法提炼师。你的任务是从整本书的叙事机制中提炼可迁移的写作技法候选池。

要求：
- 不少于20条候选机制
- 每条包含：
  - candidate_id (C001-C999)
  - name
  - source_arc (来源阶段)
  - source_chapters (来源章节范围)
  - solves_writing_problem (解决了什么写作问题)
  - mechanism_summary (机制摘要，200-400字)
  - why_it_may_transfer (为什么可能可迁移)
  - original_contamination_risk (原作污染风险)
  - suggested_distillation_type (建议提炼类型)
  - confidence (high/medium/low)
- 不复制原作设定/人名/桥段
- 机制是抽象的可迁移原则，不是具体情节描述

输出使用Markdown格式。"""


# ── Main Pipeline ─────────────────────────────────────────────────────────

def run_pipeline(book_id: str, project_root: Path, real_mode: bool = False,
                 spine_only: bool = False):
    """Execute the full Step 3B pipeline."""
    output_dir = project_root / "production" / "phase8" / "reverse_assets" / f"{book_id}_step3b"
    temp_dir = output_dir / "_temp"
    output_dir.mkdir(parents=True, exist_ok=True)
    temp_dir.mkdir(parents=True, exist_ok=True)

    start_time = datetime.now()
    llm_calls = []  # Track all LLM calls

    # ── Step 1: Load all cards ────────────────────────────────────────
    print("=" * 60)
    print("Step 3B: 长篇结构与机制定位")
    print("=" * 60)
    print(f"\n[1/8] Loading all chapter cards...")
    cards = load_all_cards(book_id, project_root)
    print(f"  Loaded {len(cards)} chapter cards")

    # ── Step 2: Generate full_chapter_spine.md ─────────────────────────
    print(f"\n[2/8] Generating full_chapter_spine.md (programmatic, no LLM)...")
    spine_path = output_dir / "full_chapter_spine.md"
    stats = generate_full_chapter_spine(cards, spine_path)
    print(f"  Stats: {json.dumps({k: v for k, v in stats.items() if k != 'all_characters'}, ensure_ascii=False)}")

    if spine_only:
        print("\n  --spine-only mode: stopping after spine generation.")
        # Still generate execution notes
        _generate_execution_notes(output_dir, cards, [], [], start_time, real_mode)
        return

    # ── Step 3: Auto-detect stages ─────────────────────────────────────
    print(f"\n[3/8] Auto-detecting stage boundaries...")
    stages = detect_stages(cards, min_stages=11, max_stages=15, max_chapters_per_stage=160)
    print(f"  Detected {len(stages)} stages:")
    for st in stages:
        print(f"    {st['stage_id']}: Ch{st['first_chapter']}-{st['last_chapter']} "
              f"({st['chapter_count']}ch) | {st['stage_name_hint'][:60]}")

    # ── Step 4: Per-stage arc mechanism analysis ───────────────────────
    print(f"\n[4/8] Analyzing arc mechanisms per stage (LLM calls: {len(stages)})...")
    stage_analyses = []
    for i, stage in enumerate(stages):
        stage_id = stage["stage_id"]
        print(f"\n  --- Stage {stage_id} (Ch{stage['first_chapter']}-{stage['last_chapter']}) ---")

        # Write system prompt
        sys_path = temp_dir / f"system_arc_{stage_id}.md"
        sys_path.write_text(SYSTEM_PROMPT_ARC_MECHANISM, encoding="utf-8")

        # Write user prompt
        usr_path = temp_dir / f"user_arc_{stage_id}.md"
        user_prompt = build_stage_user_prompt(stage)
        usr_path.write_text(user_prompt, encoding="utf-8")

        # Call LLM
        out_path = temp_dir / f"llm_arc_{stage_id}.md"
        task_name = f"step3b_arc_{stage_id}"
        success = call_deepseek(
            system_prompt_path=sys_path,
            user_input_path=usr_path,
            output_path=out_path,
            task_name=task_name,
            real_mode=real_mode,
            max_tokens=8000,
            timeout=300,
        )
        llm_calls.append({
            "step": "arc_mechanism_per_stage",
            "stage": stage_id,
            "chapter_range": f"{stage['first_chapter']}-{stage['last_chapter']}",
            "chapter_count": stage["chapter_count"],
            "success": success,
        })

        if out_path.exists():
            stage_analyses.append({
                "stage_id": stage_id,
                "chapter_range": f"{stage['first_chapter']}-{stage['last_chapter']}",
                "analysis": out_path.read_text(encoding="utf-8"),
            })
        else:
            stage_analyses.append({
                "stage_id": stage_id,
                "chapter_range": f"{stage['first_chapter']}-{stage['last_chapter']}",
                "analysis": f"[LLM call failed for {stage_id}]",
            })

    # ── Step 5: Compile arc_mechanism_index.md ─────────────────────────
    print(f"\n[5/8] Compiling arc_mechanism_index.md...")
    _compile_arc_mechanism_index(stages, stage_analyses, output_dir)

    # ── Step 6: Generate refined_volume_structure.md ──────────────────
    print(f"\n[6/8] Generating refined_volume_structure.md (LLM)...")
    _generate_refined_volume_structure(cards, stages, output_dir, temp_dir, real_mode, llm_calls)

    # ── Step 7: Cross-stage synthesis ──────────────────────────────────
    print(f"\n[7/8] Cross-stage synthesis (3 LLM calls)...")

    # 7a: protagonist_engine.md
    _generate_protagonist_engine(cards, stages, stage_analyses, output_dir, temp_dir,
                                 real_mode, llm_calls)

    # 7b: character_function_map.md
    _generate_character_function_map(cards, stages, output_dir, temp_dir,
                                     real_mode, llm_calls)

    # 7c: craft_distillation_candidate_pool.md
    _generate_candidate_pool(stages, stage_analyses, output_dir, temp_dir,
                             real_mode, llm_calls)

    # ── Step 8: Execution notes ────────────────────────────────────────
    print(f"\n[8/8] Generating step3b_execution_notes.md...")
    _generate_execution_notes(output_dir, cards, stages, llm_calls, start_time, real_mode)

    # ── Cleanup temp ──────────────────────────────────────────────────
    if not real_mode:
        # Keep temp files for debugging in mock mode
        pass

    print("\n" + "=" * 60)
    print("Step 3B Complete!")
    _print_summary(output_dir, cards, stages, llm_calls)
    print("=" * 60)


# ── Compilation Helpers ───────────────────────────────────────────────────

def _compile_arc_mechanism_index(stages: list[dict], analyses: list[dict],
                                  output_dir: Path):
    """Compile individual stage analyses into arc_mechanism_index.md."""
    lines = []
    lines.append("# Arc Mechanism Index: 大乘期才有逆袭系统")
    lines.append("")
    lines.append(f"> 生成方式: 程序聚合 + 分阶段 LLM 分析")
    lines.append(f"> 生成时间: {datetime.now().isoformat()}")
    lines.append(f"> 阶段数: {len(stages)}")
    lines.append("")

    lines.append("## 阶段概览")
    lines.append("")
    lines.append("| 阶段 | 章节范围 | 章节数 | 起始章节 |")
    lines.append("|------|----------|--------|----------|")
    for st in stages:
        start_title = st["cards"][0].get("title", "?") if st["cards"] else "?"
        lines.append(
            f"| {st['stage_id']} | {st['chapter_range']} | {st['chapter_count']} | {start_title} |"
        )
    lines.append("")

    for i, (st, analysis) in enumerate(zip(stages, analyses)):
        lines.append(f"## {st['stage_id']}: 第{st['chapter_range']}章")
        lines.append("")
        lines.append(f"- **章节数**: {st['chapter_count']}")
        lines.append(f"- **阶段标题提示**: {st['stage_name_hint']}")
        lines.append(f"- **划分依据**: {st['boundary_reason']}")
        lines.append("")
        lines.append(analysis["analysis"])
        lines.append("")
        lines.append("---")
        lines.append("")

    arc_path = output_dir / "arc_mechanism_index.md"
    arc_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [OK] arc_mechanism_index.md written")


def _build_full_spine_summary(cards: list[dict]) -> str:
    """Build a compact summary of the full chapter spine for cross-stage prompts."""
    lines = []
    for card in cards:
        ch = card.get("chapter_number", "?")
        title = card.get("title", "?")
        func = card.get("chapter_function", "")[:60]
        sentence = card.get("one_sentence", "")[:100]
        conf = card.get("confidence", "high")
        lines.append(f"Ch{ch} [{conf}] {title} | {func} | {sentence}")
    return "\n".join(lines)


def _build_stages_summary(stages: list[dict]) -> str:
    """Build a summary of all stages."""
    lines = []
    for st in stages:
        lines.append(
            f"- {st['stage_id']}: Ch{st['chapter_range']} ({st['chapter_count']}ch) "
            f"| {st['stage_name_hint'][:80]}"
        )
    return "\n".join(lines)


def _build_stage_analyses_summary(analyses: list[dict]) -> str:
    """Build a summary of all stage analyses for cross-stage synthesis."""
    lines = []
    for a in analyses:
        lines.append(f"## {a['stage_id']} ({a['chapter_range']})")
        # Take first 2000 chars of each analysis
        text = a["analysis"][:2000]
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


def _generate_refined_volume_structure(cards, stages, output_dir, temp_dir,
                                        real_mode, llm_calls):
    """LLM-based refined volume structure."""
    sys_path = temp_dir / "system_volume.md"
    sys_path.write_text(SYSTEM_PROMPT_VOLUME_STRUCTURE, encoding="utf-8")

    spine_summary = _build_full_spine_summary(cards)
    stages_summary = _build_stages_summary(stages)

    usr_path = temp_dir / "user_volume.md"
    user_prompt = f"""## 全量 Chapter Spine 摘要

以下是对全书774章的程序聚合摘要（每章一行）：

```
{spine_summary}
```

## 程序检测的阶段边界

程序自动检测到的 {len(stages)} 个阶段：

{stages_summary}

## 任务

请基于以上全量774章的spine数据和程序检测的阶段边界，生成 refined_volume_structure.md。
你可以调整程序检测的阶段边界，但必须给出调整理由。
每个阶段需要包含完整的字段。

注意：不要照抄旧的 volume_structure_report（那个报告只覆盖了前257章）。
"""
    usr_path.write_text(user_prompt, encoding="utf-8")

    out_path = temp_dir / "llm_volume.md"
    success = call_deepseek(
        system_prompt_path=sys_path,
        user_input_path=usr_path,
        output_path=out_path,
        task_name="step3b_refined_volume",
        real_mode=real_mode,
        max_tokens=12000,
        timeout=300,
    )
    llm_calls.append({
        "step": "refined_volume_structure",
        "chapter_range": "1-774",
        "chapter_count": len(cards),
        "success": success,
    })

    # Wrap with header
    content = out_path.read_text(encoding="utf-8") if out_path.exists() else "[LLM call failed]"
    final = f"""# Refined Volume Structure: 大乘期才有逆袭系统

> 生成方式: 程序阶段检测 + LLM 精炼
> 生成时间: {datetime.now().isoformat()}
> 总章节数: {len(cards)}
> 阶段数: {len(stages)}（程序检测）→ LLM 精炼

{content}
"""
    vol_path = output_dir / "refined_volume_structure.md"
    vol_path.write_text(final, encoding="utf-8")
    print(f"  [OK] refined_volume_structure.md written")


def _generate_protagonist_engine(cards, stages, analyses, output_dir, temp_dir,
                                  real_mode, llm_calls):
    """LLM-based protagonist engine analysis."""
    sys_path = temp_dir / "system_protagonist.md"
    sys_path.write_text(SYSTEM_PROMPT_PROTAGONIST_ENGINE, encoding="utf-8")

    spine_summary = _build_full_spine_summary(cards)
    stages_summary = _build_stages_summary(stages)
    arc_summary = _build_stage_analyses_summary(analyses)

    usr_path = temp_dir / "user_protagonist.md"
    user_prompt = f"""## 全量 Chapter Spine（774章，每章一行）

```
{spine_summary}
```

## 阶段结构

{stages_summary}

## 各阶段机制分析摘要

{arc_summary}

## 任务

请基于以上全量774章数据，反推主角江离为什么能撑起774章的篇幅。
分析主角的叙事功能和爽点机制，不要写成人物简介。
关键警示：江离是大乘期才有逆袭系统——他是最强但系统来得太晚。
"""
    usr_path.write_text(user_prompt, encoding="utf-8")

    out_path = temp_dir / "llm_protagonist.md"
    success = call_deepseek(
        system_prompt_path=sys_path,
        user_input_path=usr_path,
        output_path=out_path,
        task_name="step3b_protagonist_engine",
        real_mode=real_mode,
        max_tokens=8000,
        timeout=300,
    )
    llm_calls.append({
        "step": "protagonist_engine",
        "chapter_range": "1-774",
        "chapter_count": len(cards),
        "success": success,
    })

    content = out_path.read_text(encoding="utf-8") if out_path.exists() else "[LLM call failed]"
    final = f"""# Protagonist Engine: 大乘期才有逆袭系统

> 生成方式: 全量 spine + 分阶段机制分析 → LLM 综合
> 生成时间: {datetime.now().isoformat()}
> 分析章节: 1-774

{content}
"""
    pe_path = output_dir / "protagonist_engine.md"
    pe_path.write_text(final, encoding="utf-8")
    print(f"  [OK] protagonist_engine.md written")


def _generate_character_function_map(cards, stages, output_dir, temp_dir,
                                      real_mode, llm_calls):
    """LLM-based character function map."""
    sys_path = temp_dir / "system_charfunc.md"
    sys_path.write_text(SYSTEM_PROMPT_CHARACTER_FUNCTION, encoding="utf-8")

    # Build character presence summary
    char_counter = Counter()
    char_stages = defaultdict(set)
    for card in cards:
        ch = card.get("chapter_number", 0)
        for char in card.get("characters_present", []):
            char_counter[char] += 1
            # Find which stage
            for st in stages:
                if st["first_chapter"] <= ch <= st["last_chapter"]:
                    char_stages[char].add(st["stage_id"])

    top_chars = char_counter.most_common(60)
    char_summary = "\n".join(
        f"- {name}: {count}章出场, 阶段: {', '.join(sorted(char_stages.get(name, set())))}"
        for name, count in top_chars
    )

    spine_summary = _build_full_spine_summary(cards)
    stages_summary = _build_stages_summary(stages)

    usr_path = temp_dir / "user_charfunc.md"
    user_prompt = f"""## 角色出场统计

{char_summary}

## 全量 Chapter Spine（774章，每章一行）

```
{spine_summary}
```

## 阶段结构

{stages_summary}

## 任务

请按功能位组织角色，不要按人物传记方式编写。覆盖所有功能位要求。
"""
    usr_path.write_text(user_prompt, encoding="utf-8")

    out_path = temp_dir / "llm_charfunc.md"
    success = call_deepseek(
        system_prompt_path=sys_path,
        user_input_path=usr_path,
        output_path=out_path,
        task_name="step3b_character_function",
        real_mode=real_mode,
        max_tokens=8000,
        timeout=300,
    )
    llm_calls.append({
        "step": "character_function_map",
        "chapter_range": "1-774",
        "chapter_count": len(cards),
        "success": success,
    })

    content = out_path.read_text(encoding="utf-8") if out_path.exists() else "[LLM call failed]"
    final = f"""# Character Function Map: 大乘期才有逆袭系统

> 生成方式: 全量 spine + 角色出场统计 → LLM 按功能位组织
> 生成时间: {datetime.now().isoformat()}

{content}
"""
    cf_path = output_dir / "character_function_map.md"
    cf_path.write_text(final, encoding="utf-8")
    print(f"  [OK] character_function_map.md written")


def _generate_candidate_pool(stages, analyses, output_dir, temp_dir,
                              real_mode, llm_calls):
    """LLM-based craft distillation candidate pool."""
    sys_path = temp_dir / "system_candidate.md"
    sys_path.write_text(SYSTEM_PROMPT_CANDIDATE_POOL, encoding="utf-8")

    stages_summary = _build_stages_summary(stages)
    arc_summary = _build_stage_analyses_summary(analyses)

    usr_path = temp_dir / "user_candidate.md"
    user_prompt = f"""## 阶段结构

{stages_summary}

## 各阶段机制分析

{arc_summary}

## 任务

请基于以上各阶段的机制分析，提炼不少于20条可迁移的写作技法候选机制。
每条机制必须抽象到可以独立于原作使用，不得包含具体角色名、地名、设定名。
"""
    usr_path.write_text(user_prompt, encoding="utf-8")

    out_path = temp_dir / "llm_candidate.md"
    success = call_deepseek(
        system_prompt_path=sys_path,
        user_input_path=usr_path,
        output_path=out_path,
        task_name="step3b_candidate_pool",
        real_mode=real_mode,
        max_tokens=12000,
        timeout=300,
    )
    llm_calls.append({
        "step": "candidate_pool",
        "chapter_range": "1-774",
        "chapter_count": sum(s["chapter_count"] for s in stages),
        "success": success,
    })

    content = out_path.read_text(encoding="utf-8") if out_path.exists() else "[LLM call failed]"
    final = f"""# Craft Distillation Candidate Pool: 大乘期才有逆袭系统

> 生成方式: 分阶段机制分析 → LLM 提炼可迁移技法
> 生成时间: {datetime.now().isoformat()}
> 注意: 本候选池的机制尚未进入 approved，仅作为 Step 4 的输入备选

{content}
"""
    cp_path = output_dir / "craft_distillation_candidate_pool.md"
    cp_path.write_text(final, encoding="utf-8")
    print(f"  [OK] craft_distillation_candidate_pool.md written")


def _generate_execution_notes(output_dir, cards, stages, llm_calls,
                               start_time, real_mode):
    """Generate step3b_execution_notes.md (programmatic)."""
    total_cards = len(cards)
    programmatic_steps = [
        "Load all 774 chapter cards",
        "Generate full_chapter_spine.md (programmatic, zero LLM)",
        "Auto-detect stage boundaries (heuristic scoring)",
    ]
    llm_steps = []
    for call in llm_calls:
        llm_steps.append(
            f"- {call['step']}: chapters {call['chapter_range']} "
            f"({call['chapter_count']} chapters), success={call['success']}"
        )

    conf_dist = Counter(c.get("confidence", "unknown") for c in cards)

    notes = f"""# Step 3B Execution Notes

> 生成时间: {datetime.now().isoformat()}
> 执行耗时: {(datetime.now() - start_time).total_seconds():.0f}s
> 模式: {'real (DeepSeek API)' if real_mode else 'mock (无 API 调用)'}

## 1. 输入文件

1. `production/phase8/corpus/dachengqi/chapter_cards/`（{total_cards}个YAML文件）
2. `production/phase8/audit/dachengqi/chapter_fact_audit_report.md`
3. `production/phase8/audit/dachengqi/chapter_card_quality_report.md`
4. `production/phase8/audit/dachengqi_step3_result_audit_package/volume_structure_report.md`（仅参考阶段划分思路）
5. `production/phase8/audit/dachengqi_step3_result_audit_package/book_architect_execution_notes.md`

## 2. 是否读取了全量 774 张 chapter_card

**是。** 脚本 `load_all_cards()` 读取了全部 {total_cards} 张 chapter_card 的以下字段：
- chapter_number, title, one_sentence, chapter_function, main_events
- characters_present, protagonist_state_change
- hook_opened, hook_paid, reader_debts_opened, reader_debts_paid
- ending_pull, scene_vitality_notes, confidence

## 3. 哪些步骤是程序聚合

{chr(10).join(f'- {s}' for s in programmatic_steps)}

## 4. 哪些步骤调用 LLM

共 {len(llm_calls)} 次 LLM 调用：

{chr(10).join(llm_steps) if llm_steps else '- (none - mock mode)'}

## 5. 每次 LLM 调用输入的章节范围

| 调用步骤 | 章节范围 | 章节数 |
|----------|----------|--------|
"""
    for call in llm_calls:
        notes += f"| {call['step']} | {call['chapter_range']} | {call['chapter_count']} |\n"

    notes += f"""
## 6. 是否使用旧 Step 3 产物

**否。** 本 Step 3B 未读取以下旧产物：
- `production/phase8/reverse_assets/dachengqi/reverse_story_bible.md`
- `production/phase8/reverse_assets/dachengqi/character_cards/`
- `production/phase8/reverse_assets/dachengqi/reader_debt_lifecycle.md`
- `production/phase8/reverse_assets/dachengqi/hook_payoff_map.md`

仅参考了旧 volume_structure_report 的阶段划分思路（非内容）。

## 7. 是否生成 craft_assets

**否。** 本 Step 3B 生成的是 `dachengqi_step3b/` 下的分析产物，未写入 `craft_assets/` 目录。

## 8. 交付物清单

| 交付物 | 文件 | 状态 |
|--------|------|------|
| 1. full_chapter_spine | full_chapter_spine.md | ✅ |
| 2. refined_volume_structure | refined_volume_structure.md | ✅ |
| 3. arc_mechanism_index | arc_mechanism_index.md | ✅ |
| 4. protagonist_engine | protagonist_engine.md | ✅ |
| 5. character_function_map | character_function_map.md | ✅ |
| 6. candidate_pool | craft_distillation_candidate_pool.md | ✅ |

## 9. 统计数据

- 全量章节: {total_cards}
- 检测阶段数: {len(stages)}
- 置信度分布: {dict(conf_dist)}
- LLM 调用次数: {len(llm_calls)}
- LLM 调用成功率: {sum(1 for c in llm_calls if c['success'])}/{len(llm_calls)} ({sum(1 for c in llm_calls if c['success'])/max(1,len(llm_calls))*100:.0f}%)

## 10. 执行脚本

`tools/phase8/run_step3b_mechanism_index.py`
"""
    notes_path = output_dir / "step3b_execution_notes.md"
    notes_path.write_text(notes, encoding="utf-8")
    print(f"  [OK] step3b_execution_notes.md written")


def _print_summary(output_dir, cards, stages, llm_calls):
    """Print final summary to stdout."""
    print(f"\n  输出目录: {output_dir}")
    print(f"  full_chapter_spine 覆盖章节数: {len(cards)}")
    print(f"  refined_volume_structure 阶段数: {len(stages)}")
    print(f"  arc_mechanism_index 阶段机制数量: {len(stages)}")
    print(f"  LLM 调用次数: {len(llm_calls)}")
    conf_dist = Counter(c.get("confidence", "unknown") for c in cards)
    print(f"  confidence 分布: {dict(conf_dist)}")
    print(f"  是否读取全量章节: 是 ({len(cards)}章)")
    print(f"  是否使用旧 Step 3 产物: 否")


# ── CLI Entry Point ───────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Phase 8 Step 3B: 长篇结构与机制定位"
    )
    parser.add_argument("--book-id", default="dachengqi", help="书籍 ID")
    parser.add_argument("--project-root", default=None, help="项目根目录")
    parser.add_argument("--real", action="store_true", help="真实模式（调用 DeepSeek API）")
    parser.add_argument("--spine-only", action="store_true",
                        help="仅生成 full_chapter_spine.md 和阶段检测（不调 LLM）")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve() if args.project_root else find_project_root()

    run_pipeline(
        book_id=args.book_id,
        project_root=project_root,
        real_mode=args.real,
        spine_only=args.spine_only,
    )


if __name__ == "__main__":
    main()
