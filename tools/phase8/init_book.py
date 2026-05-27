#!/usr/bin/env python3
"""
init_book.py — 初始化一本书的 Phase 8 工作目录。

用法:
  python tools/phase8/init_book.py \\
    --book-id toy_book \\
    --title "Toy Book" \\
    --source production/phase8/examples/toy_book/full_book.txt \\
    --genre "都市脑洞" \\
    --language "zh-CN"

输出:
  production/phase8/corpus/{book_id}/
    source_meta.yaml
    full_book.txt (copy)
    manifest.yaml

不做章节分析，不调用大模型。
"""

import os, sys, json, yaml, shutil
from pathlib import Path
from datetime import datetime

PROJECT = Path("/opt/webnovel-hermes-wps")
PHASE8 = PROJECT / "production" / "phase8"
TEMPLATES = PHASE8 / "templates"
CORPUS = PHASE8 / "corpus"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="初始化一本书的 Phase 8 工作目录")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--source", required=True, help="full_book.txt 路径")
    parser.add_argument("--genre", default="")
    parser.add_argument("--language", default="zh-CN")
    args = parser.parse_args()

    book_id = args.book_id
    target = CORPUS / book_id
    if target.exists():
        print(f"❌ 目录已存在: {target}")
        sys.exit(1)

    source_path = Path(args.source)
    if not source_path.exists():
        print(f"❌ 源文件不存在: {source_path}")
        sys.exit(1)

    # 创建目录
    (target / "chapters").mkdir(parents=True, exist_ok=True)
    (target / "chapter_cards").mkdir(parents=True, exist_ok=True)

    # 复制 full_book.txt
    shutil.copy2(str(source_path), str(target / "full_book.txt"))
    print(f"  ✅ full_book.txt 已复制")

    # 生成 source_meta.yaml
    meta = yaml.safe_load((TEMPLATES / "source_meta.template.yaml").read_text())
    meta["source_id"] = book_id
    meta["title"] = args.title
    meta["genre"] = args.genre
    meta["language"] = args.language
    meta["created_at"] = datetime.now().isoformat()
    (target / "source_meta.yaml").write_text(
        yaml.dump(meta, allow_unicode=True, default_flow_style=False, sort_keys=False)
    )
    print(f"  ✅ source_meta.yaml 已生成")

    # 生成初始 manifest.yaml
    manifest = yaml.safe_load((TEMPLATES / "manifest.template.yaml").read_text())
    manifest["book_id"] = book_id
    manifest["title"] = args.title
    manifest["source_meta_path"] = str(target / "source_meta.yaml")
    manifest["full_book_path"] = str(target / "full_book.txt")
    manifest["genre"] = args.genre
    manifest["language"] = args.language
    manifest["created_at"] = datetime.now().isoformat()
    manifest["updated_at"] = datetime.now().isoformat()
    (target / "manifest.yaml").write_text(
        yaml.dump(manifest, allow_unicode=True, default_flow_style=False, sort_keys=False)
    )
    print(f"  ✅ manifest.yaml 已生成")

    print(f"\n  ✅ 初始化完成: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
