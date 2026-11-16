# 内容核验与待办（2026-11-16）

## 已核实来源

- Google Scholar：用户在本次对话确认 `https://scholar.google.com/citations?user=6l5RGSkAAAAJ&hl=zh-CN`，已配置为真实个人学术主页。

- ScrapMem：<https://arxiv.org/abs/2605.03804>、<https://github.com/changjiale444/ScrapMem>。作者 Jiale Chang、Yuxiang Ren。仓库明确写 KDD 2027 Research Track；接收状态也由用户提供。arXiv 为预印本链接，不充当 ACM 出版链接。暂无 ACM DOI、单独项目主页。
- Survey：<https://holmeshu.github.io/On-Device-Agent-Memory-Survey/>，官网 `assets/cite.bib`、`assets/taxonomy.webp`、官方 PDF 与 GitHub reading list。14 位作者均保留；没有会议接收信息，标注 Survey / Preprint。
- SPECGAN：用户提供的出版商排版 PDF 首页，完整作者为 Jiale Chang, Shuxin Zhu, Hongfeng Yu, Shichao Wu, Rong Mu, Huanliang Xu, Zhaoyu Zhai；卷 357，文章号 127711，DOI `10.1016/j.saa.2026.127711`，2026-03-22 available online。官网 DOI 解析访问结果见链接检测报告。BibTeX 按 PDF 元数据转录，非宣称官方导出。PDF 未复制到公开目录。
- 荣誉与教育：用户需求和本地 CV。原始 CV 与早期保研文章出现排名差异，网站未显示排名、GPA 或个人隐私字段。
- 具身项目结果：32 个三层场景、768 条任务、32/32 可达性验证、87.5% 成功率来自 CV，项目详情已标为作者报告的初步结果；未生成虚构实验图。

## 待确认

1. ScrapMem 的最终 ACM DOI、正式 proceedings 元数据和单独项目页（如有）。
2. SPECGAN 接收月份仍未知，News 继续显示 `2026 · Month TBD`；上线日期不等同接收日期。可公开的作者稿 PDF、代码链接待补。
3. Survey 的 arXiv / DOI（如后续申请）；当前仅使用官网 PDF 和官方 BibTeX。
4. 奖项日期除名称内的 2025 外均未知，因此未添加月份和获奖次数；不将研究起止时间误写为获奖或接收日期。
5. 厦大正式入学时间待确认，始终标注 Incoming，不推断已取得硕士学位。
6. 具身项目的系统架构图、实验协议、基线、完整结果表、视频及公开仓库待补。

News 的 `date` 对于年份记录使用年初作为**内部排序键**，通过 `displayDate` 与 `uncertainDate` 禁止输出伪造月日，并将无月份记录放在精确日期记录之后。
