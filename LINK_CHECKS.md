# 外部资源核验

核验日期：2026-11-16。只读取资源，没有向外部网站上传个人资料或发布内容。

| 资源 | 结果 | 依据 |
| --- | --- | --- |
| https://scholar.google.com/citations?user=6l5RGSkAAAAJ&hl=zh-CN | HTTP 200 | 用户确认的个人链接，实际 GET |
| https://mac.xmu.edu.cn/ | 可访问 | 用户提供，官网确认为 Xiamen University MAC / Media Analytics & Computing Laboratory |
| https://github.com/changjiale444 | HTTP 200 | curl 实际 GET |
| https://github.com/changjiale444/ScrapMem | 可访问 | 官方 README，作者与 KDD 2027 Research Track 描述 |
| https://arxiv.org/abs/2605.03804 | 可访问 | 官方页面，Jiale Chang / Yuxiang Ren，摘要和 PDF |
| https://holmeshu.github.io/On-Device-Agent-Memory-Survey/ | HTTP 200 | 实际下载官网 HTML |
| 官网 assets/cite.bib | HTTP 200 | 原文保存于 my-assets，14 位作者 |
| 官网 assets/taxonomy.webp | HTTP 200 | 下载并用于论文缩略图 |
| 官网 assets/on-device-agent-memory-survey.pdf | HTTP 200 | curl 实际 GET |
| https://doi.org/10.1016/j.saa.2026.127711 | HTTP 200 | 重定向到 Elsevier linkinghub，PII S1386142526002829；DOI 与用户提供 PDF 一致 |
| https://naproxen-network.github.io/ | HTTP 200 | 仅读取布局参考 |
| https://aaaaazbx.github.io/ | HTTP 200 | 仅读取排版参考 |

没有为缺失的 ACM DOI、综述 arXiv、具身代码或视频创建猜测 URL。所有公开 HTML 中的外部链接均验证包含新标签页和 noopener noreferrer。
