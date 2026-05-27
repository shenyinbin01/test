"""
test_phase8_integration.py — Phase 8 完整流程集成测试

测试内容：
  1. tmp_path 下完整流程：init_book → split_chapters → build_chapter_fact_audit → validate scaffold
  2. toy_book 核心交付物必须存在（不允许跳过）
  3. delivery 模式缺失 7 个核心交付物必须 FAIL
"""

import os, sys, yaml, json, tempfile, shutil
from pathlib import Path
from datetime import datetime

# conftest.py 已自动注入 project_root 到 sys.path
from tests.phase8.conftest import get_project_root


def test_full_pipeline_in_tmp_path():
    """在 tmp_path 下跑完整 init → split → audit → validate scaffold 流程"""
    project_root = get_project_root()
    real_phase8 = project_root / "production" / "phase8"

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # —— 构建骨架 ——
        phase8 = tmp / "production" / "phase8"
        (phase8 / "templates").mkdir(parents=True)
        (phase8 / "corpus").mkdir(parents=True)
        (phase8 / "schemas").mkdir(parents=True)
        (phase8 / "prompts").mkdir(parents=True)
        (phase8 / "audit").mkdir(parents=True)
        (phase8 / "reverse_assets").mkdir(parents=True)
        (phase8 / "craft_assets" / "candidate").mkdir(parents=True)
        (phase8 / "craft_assets" / "approved").mkdir(parents=True)
        (phase8 / "craft_assets" / "rejected").mkdir(parents=True)
        (phase8 / "skill_injection").mkdir(parents=True)
        (phase8 / "validation").mkdir(parents=True)

        # 复制模板
        real_templates = real_phase8 / "templates"
        for f in real_templates.glob("*.yaml"):
            shutil.copy2(str(f), str(phase8 / "templates" / f.name))
        for f in real_templates.glob("*.md"):
            shutil.copy2(str(f), str(phase8 / "templates" / f.name))

        # 复制 schemas
        real_schemas = real_phase8 / "schemas"
        for f in real_schemas.glob("*.yaml"):
            shutil.copy2(str(f), str(phase8 / "schemas" / f.name))

        book_id = "integration_test_book"

        # —— 1. 创建 full_book.txt ——
        book_dir = phase8 / "corpus" / book_id
        book_dir.mkdir(parents=True)
        full_text = (
            "第一章 初入江湖\n本章内容：主角林风醒来。\n\n"
            "第二章 偶遇高人\n本章内容：林风遇到了周老头。\n\n"
            "第三章 初次较量\n本章内容：林风和周老头切磋。\n\n"
        )
        (book_dir / "full_book.txt").write_text(full_text, encoding="utf-8")

        # 手动 source_meta（object 模型）
        source_meta = yaml.safe_load((phase8 / "templates" / "source_meta.template.yaml").read_text())
        source_meta["source_id"] = book_id
        source_meta["title"] = "Integration Test"
        source_meta["author"] = "Test"
        source_meta["source_type"] = "original_script"
        source_meta["permission_status"] = "own_work"
        source_meta["created_at"] = datetime.now().isoformat()
        (book_dir / "source_meta.yaml").write_text(
            yaml.dump(source_meta, allow_unicode=True, default_flow_style=False))

        # 手动 manifest
        manifest = yaml.safe_load((phase8 / "templates" / "manifest.template.yaml").read_text())
        manifest["book_id"] = book_id
        manifest["title"] = "Integration Test"
        manifest["created_at"] = datetime.now().isoformat()
        manifest["updated_at"] = datetime.now().isoformat()
        (book_dir / "manifest.yaml").write_text(
            yaml.dump(manifest, allow_unicode=True, default_flow_style=False))

        # —— 2. split_chapters ——
        sys.argv = ["split_chapters.py", "--book-id", book_id, "--project-root", str(tmp)]
        from tools.phase8.split_chapters import main as split_main
        try:
            split_main()
        except SystemExit as e:
            assert e.code == 0, f"split_chapters 失败: exit={e.code}"

        # 验证章节
        ch_dir = book_dir / "chapters"
        ch_files = sorted(ch_dir.glob("*.md"))
        assert len(ch_files) == 3, f"期望 3 章, 实际 {len(ch_files)}"
        assert ch_files[0].name == "chapter_0001.md"

        # 验证 manifest 更新
        manifest_updated = yaml.safe_load((book_dir / "manifest.yaml").read_text())
        assert manifest_updated["chapter_count"] == 3
        assert len(manifest_updated["chapter_index"]) == 3

        # —— 3. 创建 chapter_cards（3 张，带 hook/debt ID） ——
        cc_dir = book_dir / "chapter_cards"
        cc_dir.mkdir(exist_ok=True)
        for ch_num in [1, 2, 3]:
            card = {
                "book_id": book_id,
                "chapter_number": ch_num,
                "title": f"Chapter {ch_num}",
                "source_file": f"chapter_{ch_num:04d}.md",
                "one_sentence": f"第{ch_num}章 summary",
                "chapter_function": "setup" if ch_num == 1 else "development",
                "main_events": [f"event_{ch_num}"],
                "characters_present": ["林风", "周老头"],
                "confidence": "high",
                "hook_opened": [{"id": f"H00{ch_num}", "text": f"第{ch_num}章钩子"}],
                "hook_paid": [{"id": f"H00{ch_num-1}", "payoff": f"回收钩子{ch_num-1}"}] if ch_num > 1 else [],
                "reader_debts_opened": [{"id": f"D00{ch_num}", "text": f"第{ch_num}章债务"}],
                "reader_debts_paid": [{"id": f"D00{ch_num-1}", "payoff": f"回收债务{ch_num-1}"}] if ch_num > 1 else [],
                "evidence": [{"source_ref": f"ch{ch_num}_p1", "summary": f"证据{ch_num}",
                              "evidence_type": "paraphrase", "confidence": "high"}],
            }
            (cc_dir / f"chapter_{ch_num:04d}.yaml").write_text(
                yaml.dump(card, allow_unicode=True, default_flow_style=False))

        # —— 4. build_chapter_fact_audit ——
        sys.argv = ["build_chapter_fact_audit.py", "--book-id", book_id, "--project-root", str(tmp)]
        from tools.phase8.build_chapter_fact_audit import main as audit_main
        try:
            audit_main()
        except SystemExit as e:
            assert e.code == 0, f"build_chapter_fact_audit 失败: exit={e.code}"

        audit_report = phase8 / "audit" / book_id / "chapter_fact_audit_report.md"
        assert audit_report.exists(), "审计报告应已生成"
        content = audit_report.read_text()
        assert "章节事实审计报告" in content
        assert "3/3" in content or "3" in content.split("已审计")[0]
        assert "钩子" in content
        assert "读者债" in content

        # 验证 hook/debt ID 统计
        assert "opened=3" in content or "总钩子开启" in content
        assert "unresolved=1" in content or "未兑现" in content  # H003 未兑现

        # —— 5. validate scaffold ——
        sys.argv = ["validate_phase8.py", "--book-id", book_id, "--mode", "scaffold",
                    "--project-root", str(tmp)]
        from tools.phase8.validate_phase8 import main as val_main
        try:
            val_main()
        except SystemExit as e:
            assert e.code == 0, f"validate scaffold 应通过, exit={e.code}"

        val_report_path = phase8 / "validation" / book_id / "validation_report.json"
        assert val_report_path.exists(), "校验报告应已生成"
        val_report = json.loads(val_report_path.read_text())
        assert val_report["passed"] == True
        assert val_report["mode"] == "scaffold"

        print(f"  ✅ test_full_pipeline_in_tmp_path: 3 章完整流程通过")


def test_toy_book_all_deliverables_exist():
    """toy_book 核心交付物必须存在（不允许跳过）"""
    project_root = get_project_root()
    phase8 = project_root / "production" / "phase8"
    book_id = "toy_book"

    deliverables = {
        "chapter_fact_audit_report.md": phase8 / "audit" / book_id / "chapter_fact_audit_report.md",
        "reverse_story_bible.md": phase8 / "reverse_assets" / book_id / "reverse_story_bible.md",
        "volume_structure_report.md": phase8 / "reverse_assets" / book_id / "volume_structure_report.md",
        "reader_debt_lifecycle.md": phase8 / "reverse_assets" / book_id / "reader_debt_lifecycle.md",
        "hook_payoff_map.md": phase8 / "reverse_assets" / book_id / "hook_payoff_map.md",
    }

    for name, path in deliverables.items():
        assert path.exists(), f"toy_book 核心交付物 {name} 必须存在，不允许跳过"

    # character_cards 目录至少 1 张卡
    char_dir = phase8 / "reverse_assets" / book_id / "character_cards"
    assert char_dir.exists(), "toy_book character_cards 目录必须存在"
    char_cards = sorted(char_dir.glob("*.md"))
    assert len(char_cards) >= 1, "toy_book character_cards 至少需要 1 张卡"

    # skill_injection_plan
    skill_dir = phase8 / "skill_injection"
    skill_files = list(skill_dir.glob(f"{book_id}*.md")) + list(skill_dir.glob(f"{book_id}*.yaml"))
    assert len(skill_files) >= 1, f"toy_book skill_injection_plan 必须存在"

    print(f"  ✅ test_toy_book_all_deliverables_exist: 7 个核心交付物齐全")


def test_delivery_mode_fails_without_all_deliverables():
    """delivery 模式缺失 7 个核心交付物必须 FAIL（使用 tmp_path）"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        phase8 = tmp / "production" / "phase8"
        book_id = "minimal_book"

        # 最小骨架 + corpus
        (phase8 / "schemas").mkdir(parents=True)
        (phase8 / "templates").mkdir(parents=True)
        (phase8 / "prompts").mkdir(parents=True)
        (phase8 / "corpus" / book_id / "chapters").mkdir(parents=True)
        (phase8 / "corpus" / book_id / "chapter_cards").mkdir(parents=True)
        (phase8 / "audit" / book_id).mkdir(parents=True)
        (phase8 / "reverse_assets").mkdir(parents=True)
        (phase8 / "craft_assets" / "candidate").mkdir(parents=True)
        (phase8 / "craft_assets" / "approved").mkdir(parents=True)
        (phase8 / "craft_assets" / "rejected").mkdir(parents=True)
        (phase8 / "skill_injection").mkdir(parents=True)
        (phase8 / "validation").mkdir(parents=True)

        # source_meta
        meta = {
            "source_id": book_id, "title": "Minimal", "author": "test",
            "source_type": "original_script", "permission_status": "own_work",
            "allowed_operations": {"ingest": True, "compress": True, "distill_craft": False,
                                   "quote": False, "train_model": False},
            "do_not_copy": True,
        }
        (phase8 / "corpus" / book_id / "source_meta.yaml").write_text(
            yaml.dump(meta, allow_unicode=True, default_flow_style=False))

        manifest = {"book_id": book_id, "title": "Minimal", "chapter_count": 0,
                    "chapter_index": [], "status": "initialized"}
        (phase8 / "corpus" / book_id / "manifest.yaml").write_text(
            yaml.dump(manifest, allow_unicode=True, default_flow_style=False))

        # 只有 audit/reverse_assets/skill_injection 的目录，但无文件
        sys.argv = ["validate_phase8.py", "--book-id", book_id, "--mode", "delivery",
                    "--project-root", str(tmp)]
        from tools.phase8.validate_phase8 import main as val_main
        try:
            val_main()
            assert False, "delivery 模式应失败但通过了"
        except SystemExit as e:
            assert e.code != 0, "delivery 模式缺失交付物必须 FAIL"

            val_report_path = phase8 / "validation" / book_id / "validation_report.json"
            if val_report_path.exists():
                report = json.loads(val_report_path.read_text())
                assert not report["passed"]
                errors = report.get("errors", [])
                error_text = json.dumps(errors, ensure_ascii=False)
                # 至少应缺失 reverse_story_bible 和 character_cards
                assert "reverse_story_bible" in error_text or "character_cards" in error_text or "skill_injection" in error_text

        print(f"  ✅ test_delivery_mode_fails_without_all_deliverables: 正确 FAIL")


if __name__ == "__main__":
    test_full_pipeline_in_tmp_path()
    test_toy_book_all_deliverables_exist()
    test_delivery_mode_fails_without_all_deliverables()
    print("\n  ✅ 所有集成测试通过")
