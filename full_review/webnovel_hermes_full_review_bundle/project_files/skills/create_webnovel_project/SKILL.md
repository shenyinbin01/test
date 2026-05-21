# Skill 名称: create_webnovel_project

## 所属流程环节
项目初始化

## 适用场景
启动一部新小说时，创建完整的项目目录结构和初始元信息文件。

## 输入
- project_name: 项目内部名称（用于目录命名）
- book_title: 书名
- genre: 题材（如都市脑洞）
- core_idea: 一句话核心脑洞
- target_reader: 目标读者
- style_preference: 风格偏好

## 输出
- /data/webnovel-lab/workspace/novels/{project_name}/project.yaml
- /data/webnovel-lab/workspace/novels/{project_name}/README.md
- /data/webnovel-lab/workspace/novels/{project_name}/.story-system/ 目录骨架
- /data/webnovel-lab/workspace/novels/{project_name}/.webnovel/ 目录骨架

## 执行步骤
1. 校验 project_name 合法性（只含小写字母、数字、下划线）
2. 创建 novels/{project_name}/ 目录
3. 创建子目录：.story-system/, .webnovel/context/, .webnovel/state/
4. 创建 outlines/, outlines/beats/, manuscript/drafts/, manuscript/polished/, manuscript/chapters/, reviews/, wps/, exports/
5. 写入 project.yaml（含名称、类型、核心脑洞、风格偏好）
6. 在项目 README.md 中记录创建时间和项目概述

## 质量标准
- 目录结构完整可被后续的 generate_story_bible 读取
- project.yaml 内容满足 master_setting.schema.yaml 的必填字段

## 常见失败情况
- project_name 已存在：确认用户是否要覆盖或另起新名
- 权限不足：确认 agentuser 对 /data/webnovel-lab/workspace/novels/ 有写权限

## 禁止事项
- 禁止在 project.yaml 中存储真实密钥
- 禁止覆盖已存在的 project.yaml 除非用户确认
- 禁止在项目目录外创建文件

## 示例输入
project_name: "price_tag_life"
book_title: "人生价格标签"
core_idea: "主角是普通外卖员，能看到每个人的人生价格标签"

## 示例输出
/data/webnovel-lab/workspace/novels/price_tag_life/project.yaml 已创建
