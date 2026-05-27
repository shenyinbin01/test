"""
conftest.py — Phase 8 测试公共配置
"""

import shutil
from pathlib import Path


def build_tmp_phase8(tmp_path, toy_full_book_text=None):
    """
    在 tmp_path 下搭建最小 phase8 骨架，返回 project_root。
    """
    project_root = tmp_path / "project"
    phase8 = project_root / "production" / "phase8"

    (phase8 / "schemas").mkdir(parents=True)
    (phase8 / "templates").mkdir(parents=True)
    (phase8 / "prompts").mkdir(parents=True)
    (phase8 / "corpus").mkdir(parents=True)
    (phase8 / "audit").mkdir(parents=True)
    (phase8 / "reverse_assets").mkdir(parents=True)
    (phase8 / "craft_assets" / "candidate").mkdir(parents=True)
    (phase8 / "craft_assets" / "approved").mkdir(parents=True)
    (phase8 / "craft_assets" / "rejected").mkdir(parents=True)
    (phase8 / "skill_injection").mkdir(parents=True)
    (phase8 / "validation").mkdir(parents=True)

    # Copy schemas from real project
    real_schemas = Path("/opt/webnovel-hermes-wps") / "production" / "phase8" / "schemas"
    if real_schemas.exists():
        for f in real_schemas.glob("*.yaml"):
            shutil.copy2(str(f), str(phase8 / "schemas" / f.name))

    # Copy templates from real project
    real_templates = Path("/opt/webnovel-hermes-wps") / "production" / "phase8" / "templates"
    if real_templates.exists():
        for f in real_templates.glob("*.yaml"):
            shutil.copy2(str(f), str(phase8 / "templates" / f.name))
        for f in real_templates.glob("*.md"):
            shutil.copy2(str(f), str(phase8 / "templates" / f.name))

    return project_root
