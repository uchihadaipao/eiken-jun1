---
name: pdf-rename
overview: 将3个PDF文件按统一格式重命名，格式为：英检级别_年份_第几回_类型.pdf
todos:
  - id: rename-question-pdf
    content: 将 2023-3-1ji-1pkyu.pdf 重命名为 准1级_2023年_第3回_题目.pdf
    status: completed
  - id: rename-script-pdf
    content: 将 2023-3-1ji-script-1pkyu.pdf 重命名为 准1级_2023年_第3回_听力原文.pdf
    status: completed
  - id: rename-answer-pdf
    content: 将 2023-3-P1-F.pdf 重命名为 准1级_2023年_第3回_答案.pdf
    status: completed
  - id: verify-rename
    content: 验证重命名结果，确认所有文件名称正确
    status: completed
    dependencies:
      - rename-question-pdf
      - rename-script-pdf
      - rename-answer-pdf
---

## 用户需求

将文件夹中的PDF文件重命名为规范格式，包含英检级别、年份、回数、类型信息。

## 文件对应关系

| 原文件名 | 新文件名 | 说明 |
| --- | --- | --- |
| 2023-3-1ji-1pkyu.pdf | 准1级_2023年_第3回_题目.pdf | 听力题目 |
| 2023-3-1ji-script-1pkyu.pdf | 准1级_2023年_第3回_听力原文.pdf | 听力原文 |
| 2023-3-P1-F.pdf | 准1级_2023年_第3回_答案.pdf | 整套题答案 |


## 整理目标

使文件名更加规范清晰，便于识别文件内容类型。

## 技术方案

本任务为简单的文件重命名操作，无需技术实现。

## 执行方式

- 使用系统命令 `mv` 或文件管理器进行文件重命名
- 按顺序依次执行3个文件的重命名操作
- 完成后验证文件列表确认重命名成功