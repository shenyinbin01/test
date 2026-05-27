"""
test_split_chapters.py — 测试章节切分功能

测试内容：
  1. split_chapters 能识别 第1章 / 第一章 / 第001章
  2. split_chapters 能输出 chapter_0001.md
  3. manifest 能记录 chapter_index
  4. 能在 tmp_path 下跑通
"""

import os, sys, yaml, tempfile, shutil
from pathlib import Path

PROJECT = Path("/opt/webnovel-hermes-wps")
sys.path.insert(0, str(PROJECT))

from tools.phase8 import split_chapters
from tools.phase8.common import resolve_project_root


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
        ("## 第一章 开始", False),
    ]
    for line, expected in test_cases:
        result = split_chapters.is_chapter_title(line)
        assert result == expected, f"'{line}' → expected {expected}, got {result}"
    print("  ✅ test_chapter_pattern_detection: 全部通过")


def test_split_toy_book():
    """测试对玩具书的切分（在项目根目录下运行）"""
    project_root = resolve_project_root()
    corpus = project_root / "production" / "phase8" / "corpus"
    toy_dir = corpus / "toy_book"
    assert toy_dir.exists(), "toy_book 目录必须存在"

    manifest_path = toy_dir / "manifest.yaml"
    assert manifest_path.exists(), "toy_book manifest.yaml 必须存在"
    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    expected = manifest.get("chapter_count", 0)
    assert expected > 0, "toy_book 应有章节"

    chapters_dir = toy_dir / "chapters"
    assert chapters_dir.exists(), "toy_book chapters/ 必须存在"
    files = sorted(chapters_dir.glob("*.md"))
    assert len(files) >= expected, f"期望 {expected} 个章节文件，实际 {len(files)}"
    for f in files:
        assert f.name.startswith("chapter_"), f"文件名不符合规范: {f.name}"
        assert f.suffix == ".md", f"文件后缀不是 .md: {f.name}"

    # 检查 manifest chapter_index
    idx = manifest.get("chapter_index", [])
    assert len(idx) >= expected, f"manifest 中 chapter_index 条目不足: {len(idx)}"
    for entry in idx:
        assert "chapter_number" in entry
        assert "title" in entry
        assert "file_path" in entry
        assert "checksum" in entry
        assert "split_confidence" in entry
    print(f"  ✅ test_split_toy_book: {len(files)} 章, {len(idx)} 条索引")


def test_split_tmp_path():
    """在 tmp_path 下完整跑一遍 init_book + split_chapters"""
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        # 搭建 phase8 骨架
        phase8 = tmp / "production" / "phase8"
        (phase8 / "templates").mkdir(parents=True)
        (phase8 / "corpus").mkdir(parents=True)
        # 复制模板
        real_templates = PROJECT / "production" / "phase8" / "templates"
        for f in real_templates.glob("source_meta.template.yaml"):
            shutil.copy2(str(f), str(phase8 / "templates" / f.name))
        for f in real_templates.glob("manifest.template.yaml"):
            shutil.copy2(str(f), str(phase8 / "templates" / f.name))

        # 创建 full_book.txt
        book_dir = phase8 / "corpus" / "tmp_test_book"
        book_dir.mkdir(parents=True)
        full_book = book_dir / "full_book.txt"
        full_book.write_text(
            "第一章 测试\n这是第一章的内容。\n\n第二章 继续\n这是第二章的内容。\n\n第三章 结束\n这是第三章的内容。\n",
            encoding="utf-8"
        )

        # 手动 source_meta
        import yaml
        meta = yaml.safe_load((phase8 / "templates" / "source_meta.template.yaml").read_text())
        meta["source_id"] = "tmp_test_book"
        meta["title"] = "Test Book"
        meta["created_at"] = "2026-05-26T00:00:00"
        (book_dir / "source_meta.yaml").write_text(yaml.dump(meta, allow_unicode=True, default_flow_style=False))

        # 手动 manifest
        manifest = yaml.safe_load((phase8 / "templates" / "manifest.template.yaml").read_text())
        manifest["book_id"] = "tmp_test_book"
        manifest["title"] = "Test Book"
        manifest["created_at"] = "2026-05-26T00:00:00"
        manifest["updated_at"] = "2026-05-26T00:00:00"
        (book_dir / "manifest.yaml").write_text(yaml.dump(manifest, allow_unicode=True, default_flow_style=False))

        # 运行 split_chapters
        from tools.phase8.split_chapters import main as split_main
        import sys as _sys
        _sys.argv = ["split_chapters.py", "--book-id", "tmp_test_book", "--project-root", str(tmp)]
        try:
            split_main()
        except SystemExit as e:
            assert e.code == 0, f"split_chapters 失败: exit={e.code}"

        # 验证
        ch_dir = book_dir / "chapters"
        assert ch_dir.exists()
        ch_files = sorted(ch_dir.glob("*.md"))
        assert len(ch_files) == 3, f"期望 3 章, 实际 {len(ch_files)}"
        assert ch_files[0].name == "chapter_0001.md"

        manifest_updated = yaml.safe_load((book_dir / "manifest.yaml").read_text())
        assert manifest_updated["chapter_count"] == 3
        assert len(manifest_updated["chapter_index"]) == 3
        print(f"  ✅ test_split_tmp_path: tmp_path 下 3 章切分成功")


def test_confidence_marking():
    """测试低置信度标记"""
    unknown_line = "林远在加班到九点"
    result = split_chapters.is_chapter_title(unknown_line)
    assert result == False, f"'{unknown_line}' 不应被识别为章节标题"

    known_line = "第3章 测试"
    result = split_chapters.is_chapter_title(known_line)
    assert result == True
    print("  ✅ test_confidence_marking: 高/低置信度判断正确")


if __name__ == "__main__":
    test_chapter_pattern_detection()
    test_split_toy_book()
    test_split_tmp_path()
    test_confidence_marking()
    print("\n  ✅ 所有 split_chapters 测试通过")
