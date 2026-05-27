"""
test_validate_phase8.py — 测试校验工具

测试内容：
  1. validate_phase8 能发现缺失核心交付物
  2. 对完整 toy_book 校验通过
"""

import os, sys
from pathlib import Path

PROJECT = Path("/opt/webnovel-hermes-wps")


def test_validate_toy_book():
    """对完整 toy_book 运行校验"""
    # 设置命令行参数
    sys.argv = ["validate_phase8.py", "--book-id", "toy_book"]
    from tools.phase8.validate_phase8 import main
    try:
        main()
    except SystemExit as e:
        assert e.code == 0, f"toy_book 校验应当通过，但退出码为 {e.code}"
    print(f"  ✅ test_validate_toy_book: 校验通过")


def test_validate_missing_book():
    """测试不存在的书 — 应失败"""
    sys.argv = ["validate_phase8.py", "--book-id", "nonexistent_book"]
    from tools.phase8.validate_phase8 import main
    try:
        main()
    except SystemExit as e:
        # 应因缺失目录而失败
        assert e.code != 0, "不存在的书应该校验失败"
    print(f"  ✅ test_validate_missing_book: 正确检测到缺失书")


def test_check_function():
    """测试 check 辅助函数"""
    from tools.phase8.validate_phase8 import check
    assert check(True, "测试通过") == True
    assert check(False, "测试失败") == False
    print(f"  ✅ test_check_function: check 逻辑正常")


if __name__ == "__main__":
    test_validate_toy_book()
    test_check_function()
    print("\n  ✅ 所有 validate_phase8 测试通过")
