#!/usr/bin/env python3
"""
canon_rules_loader.py — canon 规则统一加载器

优先读取顺序：
1. .story-system/canon_patterns.yaml（项目级规则）
2. templates/default_canon_patterns.yaml（默认 fallback）
3. 两个都不存在则报错

两个 validator（validate_canon_consistency.py 和 validate_phase4.py）
必须调用此加载器，不再各自维护内联 fallback 常量。

如果必须保留 fallback，只能保留在 templates/default_canon_patterns.yaml。
"""

import os
import sys
from pathlib import Path

# 数据根目录（可被环境变量覆盖）
DATA_ROOT = Path(os.environ.get(
    "WEBNOVEL_DATA_ROOT",
    "/data/webnovel-lab"
))

# 代码根目录（用于定位 templates/）
CODE_ROOT = Path(os.environ.get(
    "WEBNOVEL_CODE_ROOT",
    "/opt/webnovel-hermes-wps"
))

# 默认项目名
DEFAULT_PROJECT = "price_tag_life"


def _find_story_system_patterns(project: str = None) -> Path:
    """定位 .story-system/canon_patterns.yaml 的完整路径"""
    proj = project or DEFAULT_PROJECT
    return DATA_ROOT / "workspace" / "novels" / proj / ".story-system" / "canon_patterns.yaml"


def _find_template_patterns() -> Path:
    """定位 templates/default_canon_patterns.yaml"""
    return CODE_ROOT / "templates" / "default_canon_patterns.yaml"


def load_canon_patterns(project: str = None, verbose: bool = True) -> dict:
    """
    加载 canon 规则，返回结构化 dict。

    返回字段：
        forbidden_patterns: list[str]
        wide_patterns: dict
        required_anchors: list[str]
        negation_prefixes: list[str]
        source: str  # 指示实际加载的文件路径

    加载顺序：
        1. .story-system/canon_patterns.yaml
        2. templates/default_canon_patterns.yaml
        3. 都不存在 → 抛出 FileNotFoundError
    """
    import yaml

    # 尝试 1：项目级 .story-system
    story_path = _find_story_system_patterns(project)
    if story_path.exists():
        try:
            data = yaml.safe_load(story_path.read_text(encoding="utf-8"))
            forbidden = data.get("forbidden_patterns", [])
            wide = data.get("wide_patterns", {})
            anchors = data.get("required_anchors", [])
            negation = data.get("negation_prefixes", [])

            if verbose:
                print(f"  [canon_rules_loader] 从 .story-system 加载规则: "
                      f"forbidden={len(forbidden)}, wide={len(wide)}, "
                      f"anchors={len(anchors)}, negation={len(negation)}")
                print(f"  [canon_rules_loader] 规则源: {story_path}")

            return {
                "forbidden_patterns": forbidden,
                "wide_patterns": wide,
                "required_anchors": anchors,
                "negation_prefixes": negation,
                "source": str(story_path),
            }
        except Exception as e:
            if verbose:
                print(f"  [canon_rules_loader] ⚠️ .story-system 加载失败: {e}，尝试模板 fallback")

    # 尝试 2：模板默认规则
    template_path = _find_template_patterns()
    if template_path.exists():
        try:
            data = yaml.safe_load(template_path.read_text(encoding="utf-8"))
            forbidden = data.get("forbidden_patterns", [])
            wide = data.get("wide_patterns", {})
            anchors = data.get("required_anchors", [])
            negation = data.get("negation_prefixes", [])

            if verbose:
                print(f"  [canon_rules_loader] 从模板 fallback 加载规则: "
                      f"forbidden={len(forbidden)}, wide={len(wide)}, "
                      f"anchors={len(anchors)}, negation={len(negation)}")
                print(f"  [canon_rules_loader] 规则源: {template_path}")

            return {
                "forbidden_patterns": forbidden,
                "wide_patterns": wide,
                "required_anchors": anchors,
                "negation_prefixes": negation,
                "source": str(template_path),
            }
        except Exception as e:
            if verbose:
                print(f"  [canon_rules_loader] ⚠️ 模板 fallback 加载失败: {e}")

    # 都不存在
    msg = (
        f"[canon_rules_loader] ❌ 未找到 canon 规则文件\n"
        f"  查找路径 1 (项目级): {story_path}\n"
        f"  查找路径 2 (模板): {template_path}\n"
        f"  请创建其中一个文件。"
    )
    raise FileNotFoundError(msg)


if __name__ == "__main__":
    # CLI 快速测试
    import argparse
    parser = argparse.ArgumentParser(description="canon 规则统一加载器 — 测试用")
    parser.add_argument("--project", default=DEFAULT_PROJECT, help="项目名")
    parser.add_argument("--quiet", action="store_true", help="不输出详细信息")
    args = parser.parse_args()

    try:
        result = load_canon_patterns(project=args.project, verbose=not args.quiet)
        print(f"\n  ✅ 规则加载成功")
        print(f"  规则源: {result['source']}")
        print(f"  forbidden_patterns: {len(result['forbidden_patterns'])} 条")
        print(f"  wide_patterns: {len(result['wide_patterns'])} 条")
        print(f"  required_anchors: {len(result['required_anchors'])} 条")
        print(f"  negation_prefixes: {len(result['negation_prefixes'])} 条")
    except FileNotFoundError as e:
        print(f"\n  ❌ {e}")
        sys.exit(1)
