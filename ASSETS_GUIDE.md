# 素材维护指南

所有原始资料收集在 `my-assets/`；该目录被 Git 忽略，**不会作为网站路径或自动发布**。包含私人信息的原始简历只能留在此处。网站实际使用 `public/assets/` 中的公开、压缩资源。

| 收集文件 | 用途与建议 | 必需 | 网站资源 |
| --- | --- | --- | --- |
| `profile/avatar.jpg` | 头像，建议正方形 600×600 或更大 | 是，已接入 | `public/assets/img/avatar.webp` |
| `profile/CV-private-source.pdf` | 原始简历，含非公开信息，不可直接复制上线 | 否 | 不公开 |
| `profile/CV.pdf` | 将来替换用的公开学术 CV，先删除电话、年龄等 | 否 | `public/assets/pdf/jiale-chang-cv.pdf`（已生成公开版） |
| `profile/bio.md` | 介绍资料备份；实际简介维护于 `src/data/about.mdx` | 否 | MDX 在构建时生成正文 |
| `papers/ScrapMem/paper.pdf` | 原始论文 | 已有 | 论文按钮优先链接 arXiv；本地公开副本位于 `public/assets/pdf/scrapmem.pdf` |
| `papers/ScrapMem/framework.pdf` | 原始方法图；已渲染 WebP | 已有 | `public/assets/img/publication_preview/scrapmem.webp` |
| `papers/SPECGAN/paper.pdf` | 出版商版本用于核实信息，不自动公开 PDF | 已有 | 公开按钮使用 DOI |
| `papers/SPECGAN/framework.jpg` | 原始框架图，建议宽度 ≥1200px | 已有 | `public/assets/img/publication_preview/specgan.webp` |
| `papers/OnDeviceMemorySurvey/paper.pdf` | 原始综述 | 已有 | 公开按钮链接官方 PDF |
| `papers/OnDeviceMemorySurvey/taxonomy.png` | 可选替换图；当前使用官网 taxonomy.webp | 否 | `public/assets/img/publication_preview/survey.webp` |
| `papers/*/thumbnail.png` | 可选手工裁剪缩略图，建议 800×500；不要裁掉关键标注 | 否 | 替换对应 WebP，并检查论文卡片 |
| `projects/embodied/overview.png` | 已确认的系统架构图，建议宽 1600px | 待补 | 加入 `public/assets/projects/` 并在项目 Markdown 引用 |
| `projects/embodied/scene1.png` | 已提供的实验室场景截图 | 已有 | `public/assets/projects/embodied.webp` |
| `projects/embodied/scene2.png` | 补充截图，建议宽 1600px | 否 | 手动复制到 `public/assets/projects/` |
| `projects/embodied/demo.mp4` | 演示视频，建议 H.264 / 720p，提供字幕 | 待补 | 确认可公开后复制，使用原生 video 标签 |
| `blog/images/` | 博客原图收集，建议 WebP 1200–1600px | 否 | 发布文章时复制所需图片至 `public/assets/blog/` |

## 替换步骤

1. 原图放入 `my-assets/`，保留源文件。
2. 确认内容可公开，导出压缩 WebP 或公开 PDF，复制到表中的 `public/assets/` 位置。
3. 若更改文件名，同步修改 `src/config/site.ts`、`src/data/papers.bib` 或内容 Markdown。
4. 执行 `yarn check && yarn lint:ci && yarn test && yarn build`，检查桌面/手机预览。

保研文章已由用户确认作为首篇博客加入网站。9 张原图保留在 `my-assets/blog/images/admission/`，网站使用 `public/assets/blog/admission/` 下的 WebP 副本，包含方向校正、尺寸压缩与描述性 Alt 文本。
