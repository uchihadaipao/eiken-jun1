# 长期记忆

## 英検准1级听力点读工具
- **用途**: 英検准1级2023年第3回听力点读练习工具
- **状态**: 全部完成（Part 1/2/3）
- **更新时间**: 2026-03-22

### 文件结构
- **音频**: Part1_Question_01~12.mp3, Part2_Article_A~F.mp3, Part3_Situation_G~K.mp3
- **JSON**: transcripts/Question_01~12.json, Article_A~F.json, Situation_G~K.json
- **HTML**: players/player_01~12.html, player_Article_A~F.html, player_Situation_G~K.html
- **Markdown**: notion/Question_01~12.md, Article_A~F.md, Situation_G~K.md

### 功能特性
- 单句循环（setInterval高频检测）
- 只看译文模式
- 隐藏答案功能
- 倍速切换（1.0x/1.2x）
- 1.0秒前移缓冲（防掐头）

### Part 1 (会話)
- 12番对话
- 文件名格式: "第X番"

### Part 2 (短文理解)
- 6篇短文 A-F
- 内容涵盖: 堤丰神话、动物工具、爱迪生娃娃、约旦小麦、卫星电话、非法捕鱼

### Part 3 (実戦会話)
- 5个情境 G-K
- 场景涵盖: 学校旅行通知、讲座介绍、火车广播、牙医预约、酒店推荐

### 新增功能 (2026-03-22)
- **导出Notion功能**：点击"📤 导出Notion"按钮，一键生成更新后的Markdown文件
- 导出内容包含：校准状态(✅/❌)、更新后的时间戳
- 下载文件后覆盖到 notion/ 目录即可更新

### Bug修复 (2026-03-22 晚)
- **导出Notion报错问题**：修复了模板字符串语法错误（player_01.html缺少反引号）
- **缺失函数问题**：为22个播放器文件添加了缺失的 `exportToNotion()` 函数定义
- 所有23个播放器文件现已包含完整的导出功能
- **导出无反应问题**：修复重复变量声明、模板字符串语法等JS错误
- **导出状态提示**：添加"⏳ 正在生成文件..."和"✅ 导出完成！"提示
