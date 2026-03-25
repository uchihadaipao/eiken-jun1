#!/usr/bin/env python3
"""快速重新生成Article_B"""
import json

BASE_DIR = '/Users/yangliu/Library/CloudStorage/GoogleDrive-liuyang.livemail@gmail.com/我的云端硬盘/30_AI/WorkBuddy/英检 准1/2023年3回/听力 2 级整理'

with open(f'{BASE_DIR}/transcripts/Article_B.json', 'r') as f:
    data = json.load(f)

# Markdown
md = f'''# Article_B

**Part 2** · 答案：**{data['answer']}**

---

## 听力原文

**音频：** `{data['audio_file']}`

| 序号 | 说话人 | 时间范围 | 英文原文 | 中文翻译 |
|:----:|:------:|----------|----------|----------|
'''

for seg in data['segments']:
    time_range = f"{seg['start']}ms-{seg['end']}ms"
    md += f"| {seg['index']} | {seg['speaker']} | {time_range} | {seg['en']} | {seg['zh']} |\n"

md += '''
---

*点击时间范围可跳转到对应音频位置*
'''

with open(f'{BASE_DIR}/notion/Article_B.md', 'w') as f:
    f.write(md)

print('Article_B.md regenerated!')
