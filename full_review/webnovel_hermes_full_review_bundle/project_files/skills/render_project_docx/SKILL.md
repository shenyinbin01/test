# Skill 名称: render_project_docx

## 所属流程环节
同步摘要

## 适用场景
项目有已完成的章节需要导出为可读文档格式时。

## 输入
- 项目路径 /data/webnovel-lab/workspace/novels/{project_name}/
- .story-system 目录下的全部素材
- templates/wps/projection_template.md

## 输出

## 示例输入

参见 SKILL.md 中的输入说明

## 示例输出

参见 SKILL.md 中的输出说明
- /data/webnovel-lab/workspace/novels/{project_name}/exports/{book_title}_main.docx
- /data/webnovel-lab/workspace/novels/{project_name}/exports/{book_title}_main.md

## 执行步骤
1. 读取 MASTER_SETTING 获取书名、章节信息
2. 收集所有最终正文（manuscript/chapters/ 目录）
3. 按章节顺序排列
4. 使用 python-docx 生成中文 DOCX
5. 同时生成 Markdown 版本
6. 写入 exports 目录

## 质量标准
- 中文不乱码
- 章节标题使用 Heading 1
- 首行缩进 2 字符
- 如 python-docx 不可用，降级为纯 Markdown

## 常见失败情况
- python-docx 未安装：提示 pip install python-docx，降级为 Markdown
- 中文字体缺失：使用系统默认中文字体

## 禁止事项
- 禁止修改 manuscript/ 下的源文件
- 禁止生成空的 DOCX

## 示例输出
exports/人生价格标签_main.docx — 包含项目封面和已完成章节
