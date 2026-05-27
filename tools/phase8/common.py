"""
common.py — Phase 8 工具公共模块

提供：
  - find_project_root: 自动发现项目根目录
  - 路径常量
  - 公共辅助函数
"""

from pathlib import Path


def find_project_root(start: Path | None = None) -> Path:
    """
    从当前文件位置向上查找仓库根目录。
    判断标准：
    - 存在 production/phase8
    - 或存在 .git
    """
    cur = (start or Path(__file__)).resolve()
    if cur.is_file():
        cur = cur.parent

    for parent in [cur, *cur.parents]:
        if (parent / "production" / "phase8").exists():
            return parent
        if (parent / ".git").exists():
            return parent

    raise RuntimeError("Cannot locate project root: no production/phase8 or .git found")


def resolve_project_root(provided_root: str | None = None) -> Path:
    """统一解析 project_root：优先使用传入值，否则自动查找"""
    if provided_root:
        return Path(provided_root).resolve()
    return find_project_root()
