"""
conftest.py — Phase 8 测试公共配置

不依赖任何固定绝对路径。通过 find_project_root 自动定位项目根目录。
"""

import os
import sys
import shutil
import yaml
from pathlib import Path
from datetime import datetime

# 自动注入 project root 到 sys.path，确保 tools.phase8 可导入
_THIS_FILE = Path(__file__).resolve()
_PROJECT = _THIS_FILE
for _p in [_THIS_FILE.parent, *_THIS_FILE.parents]:
    if (_p / "tools" / "phase8").exists():
        _PROJECT = _p
        break
    if (_p / ".git").exists():
        _PROJECT = _p
        break
sys.path.insert(0, str(_PROJECT))

from tools.phase8.common import find_project_root, resolve_project_root


def get_project_root() -> Path:
    """返回项目根目录（自动检测）"""
    return resolve_project_root()


def build_tmp_phase8(tmp_path, include_schemas=True, include_templates=True):
    """
    在 tmp_path 下搭建最小 phase8 骨架，返回 (project_root, phase8_dir)。

    不依赖任何固定绝对路径——从当前项目自动复制 schemas 和 templates。
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

    real_root = get_project_root()
    real_phase8 = real_root / "production" / "phase8"

    if include_schemas:
        real_schemas = real_phase8 / "schemas"
        if real_schemas.exists():
            for f in real_schemas.glob("*.yaml"):
                shutil.copy2(str(f), str(phase8 / "schemas" / f.name))

    if include_templates:
        real_templates = real_phase8 / "templates"
        if real_templates.exists():
            for f in real_templates.glob("*.yaml"):
                shutil.copy2(str(f), str(phase8 / "templates" / f.name))
            for f in real_templates.glob("*.md"):
                shutil.copy2(str(f), str(phase8 / "templates" / f.name))

    return project_root, phase8


def build_minimal_book(phase8_dir, book_id, title="Test Book",
                       chapter_count=0, chapter_index=None,
                       allowed_operations=None):
    """
    在 phase8_dir 下创建最小化的书籍 corpus，返回 book_dir。

    可用于测试 missing_card / missing_evidence / delivery 失败等场景。
    """
    corpus = phase8_dir / "corpus" / book_id
    corpus.mkdir(parents=True, exist_ok=True)
    (corpus / "chapters").mkdir(exist_ok=True)
    (corpus / "chapter_cards").mkdir(exist_ok=True)

    if allowed_operations is None:
        allowed_operations = {
            "ingest": True,
            "compress": True,
            "distill_craft": False,
            "quote": False,
            "train_model": False,
        }

    meta = {
        "source_id": book_id,
        "title": title,
        "author": "test",
        "source_type": "original_script",
        "permission_status": "own_work",
        "genre": "",
        "language": "zh-CN",
        "allowed_operations": allowed_operations,
        "do_not_copy": True,
        "created_at": datetime.now().isoformat(),
    }
    (corpus / "source_meta.yaml").write_text(
        yaml.dump(meta, allow_unicode=True, default_flow_style=False)
    )

    manifest = {
        "book_id": book_id,
        "title": title,
        "chapter_count": chapter_count,
        "chapter_index": chapter_index or [],
        "status": "initialized",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
    (corpus / "manifest.yaml").write_text(
        yaml.dump(manifest, allow_unicode=True, default_flow_style=False)
    )

    return corpus
