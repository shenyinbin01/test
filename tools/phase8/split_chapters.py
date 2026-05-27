#!/usr/bin/env python3
"""
split_chapters.py — 根据章节标题规则切分 full_book.txt。

支持的中文章节标题格式：
  - 第1章 / 第01章 / 第001章
  - 第一章 / 第一话 / 第一回
  - 卷一 / 第一卷

用法:
  python tools/phase8/split_chapters.py --book-id toy_book --project-root .

输出:
  production/phase8/corpus/{book_id}/chapters/chapter_0001.md
  ...
  并更新 manifest.yaml（chapter_count, chapter_index, word_count, checksum）
"""

import os, sys, re, yaml, hashlib
from pathlib import Path
from datetime import datetime

from tools.phase8.common import resolve_project_root

# 支持的中文章节标题正则
CHAPTER_PATTERNS = [
    re.compile(r'^第[0-9零一二三四五六七八九十百千]+章'),   # 第1章 / 第一章
    re.compile(r'^第[0-9零一二三四五六七八九十百千]+话'),   # 第一话
    re.compile(r'^第[0-9零一二三四五六七八九十百千]+回'),   # 第一回
    re.compile(r'^第[0-9零一二三四五六七八九十百千]+节'),   # 第一节
    re.compile(r'^卷[一二三四五六七八九十零0-9]+'),          # 卷一 / 卷1
    re.compile(r'^第[0-9零一二三四五六七八九十百千]+卷'),   # 第一卷
    re.compile(r'^Chapter\s+\d+', re.IGNORECASE),            # Chapter 1
    re.compile(r'^Ch\.?\s*\d+', re.IGNORECASE),               # Ch.1 / Ch 1
]


def is_chapter_title(line):
    """判断一行是否为章节标题"""
    stripped = line.strip()
    if not stripped:
        return False
    for pat in CHAPTER_PATTERNS:
        if pat.match(stripped):
            return True
    return False


def extract_chapter_number(line):
    """尝试从章节标题中提取章节号"""
    stripped = line.strip()
    for pat in CHAPTER_PATTERNS:
        m = pat.match(stripped)
        if m:
            return m.group(), "high"
    return stripped, "low"


def compute_checksum(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    import argparse
    parser = argparse.ArgumentParser(description="切分 full_book.txt 为单章文件")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--project-root", default=None, help="项目根目录，默认自动查找")
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    corpus = project_root / "production" / "phase8" / "corpus"

    book_dir = corpus / args.book_id
    if not book_dir.exists():
        print(f"❌ 书籍目录不存在: {book_dir}")
        sys.exit(1)

    source = book_dir / "full_book.txt"
    if not source.exists():
        print(f"❌ full_book.txt 不存在: {source}")
        sys.exit(1)

    chapters_dir = book_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    # 读取全文
    text = source.read_text(encoding="utf-8")
    lines = text.split("\n")

    # 查找章节标题行
    chapter_starts = []
    for i, line in enumerate(lines):
        if is_chapter_title(line):
            title, confidence = extract_chapter_number(line)
            chapter_starts.append((i, line.strip(), confidence))

    if not chapter_starts:
        print("❌ 未找到任何章节标题，无法切分")
        sys.exit(1)

    # 切分
    quality_flags = []
    chapter_index = []
    for idx, (start_line, title, confidence) in enumerate(chapter_starts):
        end_line = chapter_starts[idx + 1][0] if idx + 1 < len(chapter_starts) else len(lines)
        chapter_text = "\n".join(lines[start_line:end_line]).strip()
        chapter_num = idx + 1
        filename = f"chapter_{chapter_num:04d}.md"
        filepath = chapters_dir / filename
        filepath.write_text(chapter_text, encoding="utf-8")

        checksum = compute_checksum(chapter_text)
        word_count = len(chapter_text)

        entry = {
            "chapter_number": chapter_num,
            "title": title,
            "file_path": str(filepath),
            "word_count": word_count,
            "checksum": checksum,
            "split_confidence": confidence,
        }
        chapter_index.append(entry)
        print(f"  ✅ {filename} ({word_count} chars, confidence={confidence})")

        if confidence == "low":
            quality_flags.append(f"ch{chapter_num}:low_split_confidence")

    # 更新 manifest.yaml
    manifest_path = book_dir / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    manifest["chapter_count"] = len(chapter_index)
    manifest["chapter_index"] = chapter_index
    manifest["status"] = "chapters_split"
    if quality_flags:
        manifest["quality_flags"] = quality_flags
    manifest["updated_at"] = datetime.now().isoformat()

    manifest_path.write_text(
        yaml.dump(manifest, allow_unicode=True, default_flow_style=False, sort_keys=False)
    )
    print(f"\n  ✅ manifest.yaml 已更新: {len(chapter_index)} 章")
    if quality_flags:
        print(f"  ⚠️  质量标记: {quality_flags}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
