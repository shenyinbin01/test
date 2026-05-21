#!/usr/bin/env python3
"""
validate_project.py — 深度项目结构验证脚本
检查：
  - 必需目录和文件存在
  - Schema YAML 可解析且包含必需字段
  - SKILL.md 包含全部必需章节
  - 脚本文件存在
  - Prompt 文件完整性
  - deai_rules 文件完整性
  - Demo 输出完整性
  - demo_result.json / validation_report.json 可解析
"""

import sys
import os
import json
from pathlib import Path


CODE_ROOT = Path("/opt/webnovel-hermes-wps")
DATA_ROOT = Path("/data/webnovel-lab") if Path("/data/webnovel-lab").exists() else Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))


def check_exists(path, kind, context=""):
    exists = path.exists()
    size = path.stat().st_size if exists else 0
    return {"path": str(path), "kind": kind, "exists": exists, "size_bytes": size, "context": context}


def validate_schemas():
    """检查 Schema: 存在、YAML 可解析、包含必需字段"""
    results = []
    schema_dir = CODE_ROOT / "schemas"
    required_schemas = [
        "master_setting.schema.yaml",
        "runtime_canon.schema.yaml",
        "chapter_outline.schema.yaml",
        "chapter_beat.schema.yaml",
        "review_report.schema.yaml",
        "chapter_commit.schema.yaml",
    ]
    
    for fname in required_schemas:
        f = schema_dir / fname
        if not f.exists():
            results.append({"file": fname, "exists": False, "error": "文件不存在"})
            continue
        
        try:
            import yaml
            data = yaml.safe_load(f.read_text())
            if not data or not isinstance(data, dict):
                results.append({"file": fname, "exists": True, "parsable": False, "error": "YAML 内容为空或非对象"})
                continue
            
            top_key = list(data.keys())[0]
            top_val = data[top_key]
            
            # 检查字段: type, required, fields
            has_type = isinstance(top_val, dict) and "type" in top_val
            has_required = isinstance(top_val, dict) and "required" in top_val
            has_fields = isinstance(top_val, dict) and "fields" in top_val
            
            results.append({
                "file": fname,
                "exists": True,
                "parsable": True,
                "top_key": top_key,
                "has_type": has_type,
                "has_required": has_required,
                "has_fields": has_fields,
                "size": f.stat().st_size,
            })
        except Exception as e:
            results.append({"file": fname, "exists": True, "parsable": False, "error": str(e)})
    
    return results


def validate_skills():
    """检查每个 SKILL.md 包含全部必需章节"""
    results = []
    skills_dir = CODE_ROOT / "skills"
    required_sections = [
        "# Skill 名称",
        "## 所属流程环节",
        "## 适用场景",
        "## 输入",
        "## 输出",
        "## 执行步骤",
        "## 质量标准",
        "## 常见失败情况",
        "## 禁止事项",
        "## 示例输入",
        "## 示例输出",
    ]
    
    for d in sorted(skills_dir.iterdir()):
        if not d.is_dir():
            continue
        skill_md = d / "SKILL.md"
        if not skill_md.exists():
            results.append({"skill": d.name, "has_skilmd": False, "missing_sections": ["SKILL.md 不存在"]})
            continue
        
        content = skill_md.read_text()
        missing = [s for s in required_sections if s not in content]
        results.append({
            "skill": d.name,
            "has_skilmd": True,
            "size_bytes": len(content),
            "missing_sections": missing,
            "complete": len(missing) == 0,
        })
    
    return results


def validate_prompts():
    """检查 Prompt 文件完整性"""
    prompt_dir = CODE_ROOT / "templates" / "prompts"
    required = [
        "story_bible.md", "chapter_outline.md", "preflight_context.md",
        "chapter_beat.md", "chapter_writer.md", "chapter_review.md",
        "humanize.md", "chapter_commit.md", "projection.md",
    ]
    results = []
    for fname in required:
        f = prompt_dir / fname
        results.append(check_exists(f, "file", f"Prompt: {fname}"))
    return results


def validate_deai_rules():
    """检查 deai_rules 文件完整性"""
    rules_dir = CODE_ROOT / "templates" / "deai_rules"
    required = [
        "general_ai_flavor.md", "chinese_webnovel_style.md",
        "dialogue_rules.md", "action_scene_rules.md", "examples.md",
    ]
    results = []
    for fname in required:
        f = rules_dir / fname
        results.append(check_exists(f, "file", f"Rule: {fname}"))
    return results


def validate_scripts():
    """检查脚本文件完整性"""
    scripts_dir = CODE_ROOT / "scripts"
    required = [
        "env_check.py", "validate_project.py", "call_deepseek.py",
        "render_docx.py", "sync_wps.py", "run_demo.py",
    ]
    results = []
    for fname in required:
        f = scripts_dir / fname
        results.append(check_exists(f, "file", f"Script: {fname}"))
    return results


def validate_demo_output():
    """检查 Demo 输出完整性"""
    demo_dir = DATA_ROOT / "demo_output"
    if not demo_dir.exists():
        return {"exists": False, "error": "demo_output 目录不存在", "demo_result_md": False, "demo_result_json": False, "validation_report_json": False, "validation_passed": False}
    
    demo_md = demo_dir / "demo_result.md"
    demo_json = demo_dir / "demo_result.json"
    val_json = demo_dir / "validation_report.json"
    
    result = {
        "exists": True,
        "demo_result_md": demo_md.exists(),
        "demo_result_json": demo_json.exists(),
        "validation_report_json": val_json.exists(),
        "validation_passed": False,
    }
    
    # 检查 JSON 可解析
    result["demo_result_parsable"] = True
    result["validation_report_parsable"] = True
    for name, f in [("demo_result.json", demo_json), ("validation_report.json", val_json)]:
        if f.exists():
            try:
                data = json.loads(f.read_text())
                if name == "validation_report.json":
                    result["validation_passed"] = data.get("passed", False)
            except json.JSONDecodeError:
                key = name.replace(".json", "").replace("-", "_")
                result[f"{key}_parsable"] = False
                result["validation_passed"] = False
    
    return result


def run():
    errors = []
    warnings = []
    
    # 1. 必需目录
    required_dirs_check = [
        check_exists(CODE_ROOT / "skills", "dir", "14 skills"),
        check_exists(CODE_ROOT / "schemas", "dir", "6 schemas"),
        check_exists(CODE_ROOT / "scripts", "dir", "6 scripts"),
        check_exists(CODE_ROOT / "templates" / "prompts", "dir", "9 prompts"),
        check_exists(CODE_ROOT / "templates" / "deai_rules", "dir", "5 rules"),
        check_exists(CODE_ROOT / "templates" / "wps", "dir", "WPS templates"),
        check_exists(CODE_ROOT / "docs", "dir", "docs"),
    ]
    for d in required_dirs_check:
        if not d["exists"]:
            errors.append(f"缺少目录: {d['path']}")
    
    # 2. 必需文件
    required_files_check = [
        check_exists(CODE_ROOT / "README.md", "file", "README"),
        check_exists(CODE_ROOT / ".env.example", "file", "env example"),
    ]
    for f in required_files_check:
        if not f["exists"]:
            errors.append(f"缺少文件: {f['path']}")
    
    # 3. Schemas
    schemas = validate_schemas()
    for s in schemas:
        if not s.get("exists", False):
            errors.append(f"Schema 缺失: {s['file']}")
        elif not s.get("parsable", False):
            errors.append(f"Schema 解析失败: {s['file']}: {s.get('error', '')}")
        else:
            if not s.get("has_type"):
                errors.append(f"Schema {s['file']} 缺少 type 字段")
            if not s.get("has_required"):
                errors.append(f"Schema {s['file']} 缺少 required 字段")
            if not s.get("has_fields"):
                errors.append(f"Schema {s['file']} 缺少 fields 字段")
    
    # 4. Scripts
    scripts = validate_scripts()
    for s in scripts:
        if not s["exists"]:
            errors.append(f"脚本缺失: {s['path']}")
    
    # 5. Prompts
    prompts = validate_prompts()
    for p in prompts:
        if not p["exists"]:
            errors.append(f"Prompt 缺失: {Path(p['path']).name}")
    
    # 6. deai_rules
    rules = validate_deai_rules()
    for r in rules:
        if not r["exists"]:
            errors.append(f"Rule 缺失: {Path(r['path']).name}")
    
    # 7. Skills
    skills = validate_skills()
    for s in skills:
        if not s["has_skilmd"]:
            errors.append(f"SKILL.md 缺失: {s['skill']}")
        elif not s["complete"]:
            errors.append(f"Skill {s['skill']} 缺少章节: {', '.join(s['missing_sections'])}")
    
    # 8. Demo 输出
    demo = validate_demo_output()
    if not demo.get("exists", False):
        errors.append("demo_output 目录不存在")
    else:
        if not demo.get("demo_result_md"):
            errors.append("demo_result.md 缺失")
        if not demo.get("demo_result_json"):
            errors.append("demo_result.json 缺失")
        if not demo.get("validation_report_json"):
            errors.append("validation_report.json 缺失")
        if demo.get("demo_result_parsable") is False:
            errors.append("demo_result.json 不是合法 JSON")
        if demo.get("validation_report_parsable") is False:
            errors.append("validation_report.json 不是合法 JSON")
        if not demo.get("validation_passed"):
            errors.append("validation_report.json 中 passed 不为 true")
    
    # 9. 阶段三状态检测（不影响 passed）
    phase3_mock_dir = DATA_ROOT / "demo_output" / "phase3_mock_run"
    phase3_real_dir = DATA_ROOT / "demo_output" / "phase3_real_run"
    phase3_log_dir = DATA_ROOT / "demo_output" / "phase3_logs"
    
    report = {
        "code_root": str(CODE_ROOT),
        "data_root": str(DATA_ROOT),
        "required_dirs": required_dirs_check,
        "required_files": required_files_check,
        "schemas": schemas,
        "scripts": scripts,
        "prompts": prompts,
        "deai_rules": rules,
        "skills": skills,
        "demo_output": demo,
        "total_errors": len(errors),
        "errors": errors,
        "warnings": warnings,
        "passed": len(errors) == 0,
        "file_counts": {
            "schema_files": len(schemas),
            "script_files": len(scripts),
            "prompt_files": len(prompts),
            "rule_files": len(rules),
            "skill_files": len(skills),
        },
        "checked_categories": [
            "directories", "readme", "env_example", "schemas",
            "scripts", "prompts", "deai_rules", "skills", "demo_output",
        ],
        "phase3_status": {
            "mock_output_detected": phase3_mock_dir.exists() and any(phase3_mock_dir.iterdir()),
            "real_output_detected": phase3_real_dir.exists() and any(phase3_real_dir.iterdir()),
            "logs_detected": phase3_log_dir.exists() and any(phase3_log_dir.iterdir()),
        },
    }
    
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    result = run()
    sys.exit(0 if result["passed"] else 1)
