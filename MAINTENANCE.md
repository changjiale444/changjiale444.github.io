# 本地维护与发布

项目基于 MIT 许可的 [as-folio](https://github.com/dadangnh/as-folio)，保留原生 Astro 6、Tailwind v4、内容集合、BibTeX 解析、MDX、数学公式、Mermaid、TOC、阅读进度、RSS、Pagefind 与主题切换。原始素材在项目上级目录，开发项目在 `website/`。

## 启动

需要 Node.js 24+ 和 Yarn 4.13.0：

```sh
cd '/Users/cjl/科研/个人主页/website'
corepack enable
yarn install --immutable
yarn dev
```

访问 <http://localhost:4321/>。生产预览用 `yarn build && yarn preview`；Pagefind 全文索引在生产构建生成，开发模式提供标题/关键词搜索。

当前电脑可直接执行，无需先配置 PATH：

```sh
cd '/Users/cjl/科研/个人主页/website'
./start-local.command
```

启动脚本优先使用系统 Node，否则使用当前 Codex 自带 Node；Yarn 4.13.0 已保存在 `.yarn/releases/`。首次缺少 node_modules 时自动安装锁定依赖。

## 修改内容

- **About Me**：`src/data/about.mdx`。
- **姓名、联系链接、SEO、导航、功能开关**：`src/config/site.ts`。
- **教育、荣誉、研究经历、首页文案**：`src/config/profile.ts`。
- **论文**：向 `src/data/papers.bib` 添加条目。`selected` 控制推荐意图，首页按文件顺序展示选中条目；列表按年份排序。类型使用 `inproceedings` / `article` / `misc`，分别对应 Conference / Journal / Preprint。`preview` 是 `public/assets/img/publication_preview/` 内的文件名；`html` 是 Paper 链接，`code` 是仓库，`website` 是独立 Project 地址。无真实链接就省略字段。作者以 ` and ` 分隔，完整保留；Jiale Chang 自动加粗。
- **News**：创建 `src/content/announcements/*.md`，示例：

```yaml
---
date: 2026-11-01
displayDate: '2026.11'
uncertainDate: false
---
A short update with a verified [resource](https://example.org).
```

  未知月份用 `displayDate: '2026 · Month TBD'`、`uncertainDate: true`。内部日期仅排序，不会作为精确月日输出。超过五条显示 Show All / Show Less。
- **研究项目**：`src/content/projects/embodied.md`。加入正式架构图、实验结果、视频或代码时注明来源与状态。
- **博客**：复制 `src/content/posts/publishing-guide.md`，修改标题、日期、摘要、tags、categories。支持 `.md` / `.mdx`、中英文、`math: true`、`mermaid: true`、`toc: true`。确认内容后改 `draft: false`。草稿不输出公开 HTML、RSS、搜索或标签路径。
- **保研文章**：`admission-memoir.md` 已作为首篇正式博客加入网站，9 张 WebP 配图位于 `public/assets/blog/admission/`，文章路由为 `/blog/admission-memoir/`。
- **CV**：页面读取 `src/data/cv.yml`。下载文件是 `public/assets/pdf/jiale-chang-cv.pdf`；两者独立，修改履历时同步更新。不要上传含私人信息的原始 CV。

## 检查

```sh
yarn test:types
yarn lint:ci
yarn test
yarn build
node scripts/verify-output.mjs
```

## GitHub Pages（尚未发布）

1. 用户确认后，在自己的 GitHub 新建 `changjiale444.github.io` 仓库。
2. 将本目录作为仓库内容，保留 LICENSE。当前 origin 指向上游模板；推送前务必改为自己的仓库，不能推送到模板上游。
3. GitHub 仓库 Settings → Pages → Source 选择 GitHub Actions。
4. 仓库 Actions Variables 设置 `ASTRO_SITE=https://changjiale444.github.io`，`ASTRO_BASE` 留空（或 `/`）。配置文件已有同样默认值。
5. 推送 `main` 后 `.github/workflows/deploy.yml` 自动构建并发布，目标 <https://changjiale444.github.io/>。
6. 每次修改通过 CI 后部署。`my-assets/` 被忽略；不要强制添加私人原件。

部署通过 `.github/workflows/deploy.yml` 执行：检查、测试和静态构建完成后将产物作为 Pages artifact 上传；构建产物不会进入 Git 历史。

## 首页布局

桌面为左资料栏、右学术内容；手机头像位于姓名左侧。`src/config/site.ts` 中 `homepage.showPortrait` 可隐藏头像，`homepage.subtleEffects` 可关闭轻交互。`src/config/profile.ts` 中 `macLab` 管理实验室名称和官网地址。About Me 与项目 Markdown 中的实验室链接随内容独立维护。
