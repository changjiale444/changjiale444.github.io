---
title: 'Writing a research note / 发布指南'
date: 2026-11-16
description: 'An unpublished example for Markdown, math, code, and diagrams.'
tags: [writing, research]
categories: [Research Notes]
draft: true
math: true
mermaid: true
toc: true
---
## 如何发布
复制此文件，修改标题、日期、摘要、标签及正文，检查所有内容后把 `draft: true` 改为 `draft: false`。草稿不会生成公开路由，也不会进入搜索和 RSS。

## Math
Memory retrieval can be written as $p(m \mid q)$.

## Code
```python
def retrieve(query, memory):
    return memory.search(query)
```

## Diagram
```mermaid
graph LR
  Observation --> Memory
  Memory --> Retrieval
  Retrieval --> Action
```

## Images
图片放入 `public/assets/blog/`，引用方式：`![描述](/assets/blog/example.webp)`。
