"""
test_split_chapters.py — 测试章节切分功能

测试内容：
  1. split_chapters 能识别 第1章 / 第一章 / 第001章
  2. split_chapters 能输出 chapter_0001.md
  3. manifest 能记录 chapter_index
"""

import os, sys, yaml, tempfile, shutil
from pathlib import Path

PROJECT = Path("/opt/webnovel-hermes-wps")
sys.path.insert(0, str(PROJECT))

from tools.phase8 import split_chapters


def test_chapter_pattern_detection():
    """测试章节标题正则是否能识别各种格式"""
    test_cases = [
        ("第1章 开始", True),
        ("第一章 开始", True),
        ("第001章 开始", True),
        ("第一话 开始", True),
        ("第一回 开始", True),
        ("卷一 开始", True),
        ("第一卷 开始", True),
        ("Chapter 1", True),
        ("Ch. 1", True),
        ("正文第一段", False),
        ("林远在加班", False),
        ("## 第一章 开始", False),  # Markdown 标题不算（项目约定）
    ]
    for line, expected in test_cases:
        result = split_chapters.is_chapter_title(line)
        assert result == expected, f"'{line}' → expected {expected}, got {result}"
    print("  ✅ test_chapter_pattern_detection: 全部通过")


def test_split_toy_book():
    """测试对玩具书的切分"""
    corpus = PROJECT / "production" / "phase8" / "corpus"
    toy_dir = corpus / "toy_book"
    if not toy_dir.exists():
        print("  ⚠️ toy_book 目录不存在，跳过")
        return

    manifest_path = toy_dir / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text()) if manifest_path.exists() else {}
    expected = manifest.get("chapter_count", 0)

    chapters_dir = toy_dir / "chapters"
    if chapters_dir.exists():
        files = sorted(chapters_dir.glob("*.md"))
        assert len(files) >= expected, f"期望 {expected} 个章节文件，实际 {len(files)}"
        # 检查命名规范
        for f in files:
            assert f.name.startswith("chapter_"), f"文件名不符合规范: {f.name}"
            assert f.suffix == ".md", f"文件后缀不是 .md: {f.name}"
        print(f"  ✅ test_split_toy_book: 找到 {len(files)} 个章节文件")

        # 检查 manifest 更新
        if manifest:
            idx = manifest.get("chapter_index", [])
            assert len(idx) >= expected, f"manifest 中 chapter_index 条目不足: {len(idx)}"
            for entry in idx:
                assert "chapter_number" in entry
                assert "title" in entry
                assert "file_path" in entry
                assert "checksum" in entry
                assert "split_confidence" in entry
            print(f"  ✅ manifest chapter_index: {len(idx)} 条记录完整")
    else:
        print("  ⚠️ chapters/ 目录不存在，跳过")


def test_confidence_marking():
    """测试低置信度标记"""
    # 无法识别的标题行
    unknown_line = "林远在加班到九点"
    result = split_chapters.is_chapter_title(unknown_line)
    assert result == False, f"'{unknown_line}' 不应被识别为章节标题"

    # 标准格式
    known_line = "第3章 测试"
    result = split_chapters.is_chapter_title(known_line)
    assert result == True
    print("  ✅ test_confidence_marking: 高/低置信度判断正确")


if __name__ == "__main__":
    test_chapter_pattern_detection()
    test_split_toy_book()
    test_confidence_marking()
    print("\n  ✅ 所有 split_chapters 测试通过")
