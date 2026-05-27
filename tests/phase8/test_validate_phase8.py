"""
test_validate_phase8.py — 测试校验工具

测试内容：
  1. toy_book scaffold 模式通过
  2. toy_book delivery 模式通过 (齐全)
  3. delivery 模式缺失交付物必须 FAIL
  4. check 辅助函数
"""

import os, sys, json, tempfile, shutil
from pathlib import Path

PROJECT = Path("/opt/webnovel-hermes-wps")
sys.path.insert(0, str(PROJECT))


def test_validate_toy_book_scaffold():
    """toy_book scaffold 模式必须通过"""
    sys.argv = ["validate_phase8.py", "--book-id", "toy_book", "--mode", "scaffold"]
    from tools.phase8.validate_phase8 import main
    try:
        main()
    except SystemExit as e:
        assert e.code == 0, f"toy_book scaffold 应通过, exit={e.code}"


def test_validate_toy_book_delivery():
    """toy_book delivery 模式必须通过（7个核心交付物补齐后）"""
    sys.argv = ["validate_phase8.py", "--book-id", "toy_book", "--mode", "delivery"]
    from tools.phase8.validate_phase8 import main
    try:
        main()
    except SystemExit as e:
        assert e.code == 0, f"toy_book delivery 应通过, exit={e.code}"


def test_validate_delivery_fails_on_missing():
    """delivery 模式缺失核心交付物必须 FAIL"""
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        # 搭建 phase8 骨架（只有 corpus，没有 reverse_assets）
        phase8 = tmp / "production" / "phase8"
        (phase8 / "schemas").mkdir(parents=True)
        (phase8 / "templates").mkdir(parents=True)
        (phase8 / "prompts").mkdir(parents=True)
        (phase8 / "corpus" / "empty_book" / "chapters").mkdir(parents=True)
        (phase8 / "corpus" / "empty_book" / "chapter_cards").mkdir(parents=True)
        (phase8 / "audit").mkdir(parents=True)
        (phase8 / "reverse_assets").mkdir(parents=True)
        (phase8 / "craft_assets" / "candidate").mkdir(parents=True)
        (phase8 / "craft_assets" / "approved").mkdir(parents=True)
        (phase8 / "craft_assets" / "rejected").mkdir(parents=True)
        (phase8 / "skill_injection").mkdir(parents=True)
        (phase8 / "validation").mkdir(parents=True)

        # 最小化 source_meta
        import yaml
        meta = {"source_id": "empty_book", "title": "Empty", "author": "test",
                "source_type": "original_script", "permission_status": "own_work",
                "allowed_operations": {"ingest": True, "compress": True, "distill_craft": False,
                                       "quote": False, "train_model": False},
                "do_not_copy": True}
        (phase8 / "corpus" / "empty_book" / "source_meta.yaml").write_text(yaml.dump(meta))

        # 最小化 manifest
        manifest = {"book_id": "empty_book", "title": "Empty", "chapter_count": 0,
                    "chapter_index": [], "status": "initialized"}
        (phase8 / "corpus" / "empty_book" / "manifest.yaml").write_text(yaml.dump(manifest))

        sys.argv = ["validate_phase8.py", "--book-id", "empty_book", "--mode", "delivery", "--project-root", str(tmp)]
        from tools.phase8.validate_phase8 import main
        try:
            main()
        except SystemExit as e:
            assert e.code != 0, "delivery 模式下缺失交付物应失败"

            # 验证 JSON 报告包含缺失项
            report_path = phase8 / "validation" / "empty_book" / "validation_report.json"
            if report_path.exists():
                report = json.loads(report_path.read_text())
                assert not report["passed"]
                error_text = json.dumps(report["errors"])
                assert "reverse_story_bible" in error_text or "chapter_fact_audit_report" in error_text


def test_validate_missing_book():
    """不存在的书应失败"""
    sys.argv = ["validate_phase8.py", "--book-id", "nonexistent_book", "--mode", "scaffold"]
    from tools.phase8.validate_phase8 import main
    try:
        main()
    except SystemExit as e:
        assert e.code != 0, "不存在的书应失败"


def test_check_function():
    """测试 check 辅助函数"""
    from tools.phase8.validate_phase8 import check
    assert check(True, "测试通过") == True
    assert check(False, "测试失败") == False


if __name__ == "__main__":
    test_validate_toy_book_scaffold()
    test_validate_toy_book_delivery()
    test_validate_delivery_fails_on_missing()
    test_validate_missing_book()
    test_check_function()
    print("\n  ✅ 所有 validate_phase8 测试通过")
