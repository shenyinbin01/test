#!/usr/bin/env python3
"""
analyze_sentence_rhythm.py — 句式节奏分析工具

用途：对章节正文做轻量级句式和段落节奏分析。
不调用 LLM，不修改正文，不读取 WPS，不修改 .story-system。

输入：--input 章节正文文件路径
输出：--output YAML 报告路径

统计指标：
  - total_chars, total_paragraphs, total_sentences
  - avg_sentence_length, sentence_length_variance
  - paragraph_length_distribution
  - dialogue_ratio, action_sentence_ratio, inner_monologue_ratio
  - abstract_emotion_density
  - repeated_sentence_starts, similar_sentence_patterns
  - risk_flags, suggestions
"""

import os, sys, re, argparse
from pathlib import Path
from collections import Counter

# 抽象情绪词列表（非具体小说剧情规则，仅作统计用）
ABSTRACT_EMOTION_WORDS = [
    "震惊", "愤怒", "难以置信", "复杂", "沉重", "痛苦", "绝望",
    "激动", "恐惧", "不安", "意识到", "明白", "觉得", "仿佛", "似乎",
    "感慨", "感叹", "无奈", "悲哀", "愤怒", "委屈", "困惑", "迷茫",
    "惊讶", "惊喜", "温暖", "感动", "紧张", "焦虑", "恐慌", "激动",
    "羞愧", "后悔", "遗憾", "欣慰", "满足",
]

ACTION_INDICATORS = [
    "走", "跑", "跳", "拿", "放", "推", "拉", "敲", "抓", "握",
    "捡", "丢", "踢", "跨", "蹲", "站", "坐", "躺", "趴", "跪",
    "转身", "回头", "低头", "抬头", "摇头", "点头", "伸手", "收手",
    "打开", "关上", "掏出", "塞进", "按下", "松开", "拧", "踩",
    "冲", "闪", "躲", "挡", "扔", "接", "递",
]

INNER_MONOLOGUE_MARKERS = [
    "想", "心想", "寻思", "琢磨", "回忆", "记得", "忘了",
    "不知道", "知道", "明白", "意识到", "觉得", "怀疑",
    "猜", "推测", "估计", "假设",
]


def count_chinese_chars(text):
    return sum(1 for c in text if '\u4e00' <= c <= '\u9fff')


def split_sentences(text):
    # 以句号、问号、感叹号、省略号、分号分割句子
    raw = re.split(r'(?<=[。！？；…])', text)
    return [s.strip() for s in raw if s.strip()]


def is_dialogue_line(line):
    return bool(re.search(r'[「」「『』""「」『』]|["""](?=[^"""]*(?:说|问|答|道|喊|叫|骂|吼|嚷|解释|回答|开口|接话|插嘴|小声|大声|低声道|轻声道|道)["""])', line))


def count_action_sentences(sentences):
    cnt = 0
    for s in sentences:
        # 动作句特征：以动词开句，或包含多个动作指示词
        clean = re.sub(r'[「」『』""]', '', s)
        for act in ACTION_INDICATORS:
            if act in clean:
                cnt += 1
                break
    return cnt


def count_monologue_sentences(sentences):
    cnt = 0
    for s in sentences:
        clean = re.sub(r'[「」『』""]', '', s)
        for marker in INNER_MONOLOGUE_MARKERS:
            if marker in clean:
                cnt += 1
                break
    return cnt


def count_emotion_words(text):
    cnt = 0
    for w in ABSTRACT_EMOTION_WORDS:
        cnt += text.count(w)
    return cnt


def analyze_sentence_starts(sentences):
    starts = []
    for s in sentences:
        clean = re.sub(r'[「「『』「」『』""」『』""]', '', s)
        words = re.findall(r'[\u4e00-\u9fff]+', clean)
        if words:
            starts.append(words[0])
    return Counter(starts)


def analyze_pattern_repeats(sentences):
    """检测相似句式重复（如连续多句以"他/她"开头）"""
    patterns = []
    for s in sentences:
        clean = re.sub(r'[「「『』「」『』""」『』""]', '', s)
        # 提取句首2-3字结构
        words = re.findall(r'[\u4e00-\u9fff]+', clean)
        if words:
            prefix = words[0][:2] if len(words[0]) >= 2 else words[0]
            patterns.append(prefix)
    return Counter(patterns)


def analyze(input_path, output_path):
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    text = input_file.read_text(encoding="utf-8")

    # 基础统计
    total_chars = len(text)
    cn_chars = count_chinese_chars(text)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    total_paragraphs = len(paragraphs)

    sentences = split_sentences(text)
    total_sentences = len(sentences)

    # 句长统计
    sentence_lengths = [len(s) for s in sentences]
    avg_sentence_length = round(sum(sentence_lengths) / max(len(sentence_lengths), 1), 1)

    # 方差判断
    if len(sentence_lengths) > 1:
        mean = sum(sentence_lengths) / len(sentence_lengths)
        variance = sum((x - mean) ** 2 for x in sentence_lengths) / len(sentence_lengths)
        if variance < 20:
            variance_level = "low（句式过于平均）"
        elif variance < 60:
            variance_level = "medium"
        else:
            variance_level = "high（句式丰富度好）"
    else:
        variance = 0
        variance_level = "N/A"

    # 段落长度分布
    para_sentence_counts = []
    for p in paragraphs:
        para_sents = split_sentences(p)
        para_sentence_counts.append(len(para_sents))

    para_dist = Counter(para_sentence_counts)
    para_dist_sorted = dict(sorted(para_dist.items()))

    # 段落长度方差（用于判断段落节奏是否太整齐）
    if len(para_sentence_counts) > 1:
        para_mean = sum(para_sentence_counts) / len(para_sentence_counts)
        para_variance = sum((x - para_mean) ** 2 for x in para_sentence_counts) / len(para_sentence_counts)
        para_std = round(para_variance ** 0.5, 2)
    else:
        para_std = 0

    # 对话占比
    dialogue_lines = [p for p in paragraphs if is_dialogue_line(p)]
    dialogue_chars = sum(len(p) for p in dialogue_lines)
    dialogue_ratio = round(dialogue_chars / max(total_chars, 1), 3)

    # 动作句占比
    action_sent_count = count_action_sentences(sentences)
    action_sentence_ratio = round(action_sent_count / max(total_sentences, 1), 3)

    # 心理描写占比
    mono_sent_count = count_monologue_sentences(sentences)
    inner_monologue_ratio = round(mono_sent_count / max(total_sentences, 1), 3)

    # 抽象情绪词密度
    emotion_count = count_emotion_words(text)
    abstract_emotion_density = round(emotion_count / max(cn_chars, 1) * 1000, 2)

    # 重复句首
    start_counter = analyze_sentence_starts(sentences)
    repeated_starts = {k: v for k, v in start_counter.items() if v >= 3}
    repeated_sentence_starts_high = len(repeated_starts) > 3

    # 相似句式
    pattern_counter = analyze_pattern_repeats(sentences)
    repeated_patterns = {k: v for k, v in pattern_counter.items() if v >= 3}
    similar_sentence_patterns_high = len(repeated_patterns) > 3

    # 风险标签
    risk_flags = []
    suggestions = []

    if variance_level.startswith("low"):
        risk_flags.append("sentence_rhythm_too_flat")
        suggestions.append("增加短句（3-8字）和长句（25+字）的交替，打破句式平均化")

    if para_std < 0.8 and total_paragraphs > 5:
        risk_flags.append("paragraph_length_too_uniform")
        suggestions.append("段落长度过于均匀，建议用单段一句或长段铺陈制造节奏落差")

    if dialogue_ratio < 0.1:
        risk_flags.append("dialogue_ratio_too_low")
        suggestions.append("对话占比偏低，考虑增加角色之间的直接交流")

    if action_sentence_ratio < 0.15:
        risk_flags.append("action_sentence_ratio_too_low")
        suggestions.append("动作句占比偏低，信息多通过旁白传递而非动作承载")

    if abstract_emotion_density > 5:
        risk_flags.append("abstract_emotion_density_high")
        suggestions.append("抽象情绪词密度偏高，建议用具体动作和身体反应替代情感标签")

    if repeated_sentence_starts_high:
        risk_flags.append("repeated_sentence_start_high")
        suggestions.append("句首重复偏多，建议交替主语开句和动作/状语开句")

    if similar_sentence_patterns_high:
        risk_flags.append("similar_sentence_patterns_high")
        suggestions.append("相似句式重复偏多，建议增加句式变化")

    # 构建报告
    report = {
        "source_file": str(input_file),
        "total_chars": total_chars,
        "chinese_chars": cn_chars,
        "total_paragraphs": total_paragraphs,
        "total_sentences": total_sentences,
        "avg_sentence_length": avg_sentence_length,
        "sentence_length_variance": {
            "value": round(variance, 1),
            "level": variance_level,
        },
        "paragraph_length_distribution": {
            "sentences_per_paragraph": para_dist_sorted,
            "std_dev": para_std,
        },
        "dialogue_ratio": dialogue_ratio,
        "action_sentence_ratio": action_sentence_ratio,
        "inner_monologue_ratio": inner_monologue_ratio,
        "abstract_emotion_density": abstract_emotion_density,
        "repeated_sentence_starts": dict(repeated_starts),
        "similar_sentence_patterns": dict(repeated_patterns),
        "risk_flags": risk_flags,
        "suggestions": suggestions,
    }

    # 写 YAML
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # 手动构建 YAML 而非使用 yaml 模块，减少依赖
    lines = []
    lines.append(f"source_file: {str(input_file)}")
    lines.append(f"total_chars: {total_chars}")
    lines.append(f"chinese_chars: {cn_chars}")
    lines.append(f"total_paragraphs: {total_paragraphs}")
    lines.append(f"total_sentences: {total_sentences}")
    lines.append(f"avg_sentence_length: {avg_sentence_length}")
    lines.append("sentence_length_variance:")
    lines.append(f"  value: {round(variance, 1)}")
    lines.append(f"  level: {variance_level}")
    lines.append("paragraph_length_distribution:")
    lines.append("  sentences_per_paragraph:")
    for k, v in para_dist_sorted.items():
        lines.append(f"    {k}: {v}")
    lines.append(f"  std_dev: {para_std}")
    lines.append(f"dialogue_ratio: {dialogue_ratio}")
    lines.append(f"action_sentence_ratio: {action_sentence_ratio}")
    lines.append(f"inner_monologue_ratio: {inner_monologue_ratio}")
    lines.append(f"abstract_emotion_density: {abstract_emotion_density}")
    lines.append("repeated_sentence_starts:")
    for k, v in sorted(repeated_starts.items(), key=lambda x: -x[1]):
        lines.append(f"  {k}: {v}")
    lines.append("similar_sentence_patterns:")
    for k, v in sorted(repeated_patterns.items(), key=lambda x: -x[1]):
        lines.append(f"  {k}: {v}")
    lines.append("risk_flags:")
    for f in risk_flags:
        lines.append(f"  - {f}")
    lines.append("suggestions:")
    for s in suggestions:
        lines.append(f"  - {s}")

    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  ✅ 分析报告已写入: {output_file}")

    # 打印摘要
    print(f"  📊 章节统计:")
    print(f"    总字数: {total_chars} | 中文字数: {cn_chars}")
    print(f"    段落数: {total_paragraphs} | 句子数: {total_sentences}")
    print(f"    平均句长: {avg_sentence_length} | 句长方差: {variance_level}")
    print(f"    段落句数标准差: {para_std}")
    print(f"    对话占比: {dialogue_ratio} | 动作句占比: {action_sentence_ratio}")
    print(f"    心理描写占比: {inner_monologue_ratio}")
    print(f"    抽象情绪词密度: {abstract_emotion_density}/千字")
    print(f"    风险标志: {len(risk_flags)} 个")

    return report


def main():
    parser = argparse.ArgumentParser(description="句式节奏分析工具")
    parser.add_argument("--input", required=True, help="章节正文文件路径")
    parser.add_argument("--output", required=True, help="YAML 报告输出路径")
    args = parser.parse_args()

    try:
        analyze(args.input, args.output)
        print()
        print("  ✅ 句式节奏分析完成")
    except FileNotFoundError as e:
        print(f"  ❌ {e}")
        sys.exit(1)
    except Exception as e:
        print(f"  ❌ 分析失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
