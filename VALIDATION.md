# 验证结果

2026-11-16，本地 Node / Yarn 4.13.0。

- 上游模板原始生产构建：成功。
- `yarn test:types`（Astro check + TypeScript）：成功，0 errors，0 warnings；上游代码仍有 Astro hints。
- `yarn lint:ci`：成功。
- `yarn test`：6 个测试文件、83 项测试通过，包含新增的草稿隔离回归检查。
- `yarn build`：成功，18 个 HTML 页面；Pagefind 生成 18 页全文索引。
- `node scripts/verify-output.mjs`：成功，364 处本地路径引用、主要路由、外链属性、日期精度、作者加粗、示例草稿排除及首篇博客的 RSS / sitemap / 首页入口均通过。
- GitHub Pages：canonical / sitemap / 资源均使用 `https://changjiale444.github.io` 根路径，没有模板 `/as-folio` 前缀。
- 浏览器 QA：1440px 桌面、390px 手机；深浅色切换、菜单展开/跳转、Journal / Preprint 筛选、BibTeX 展开、搜索 `optical` 返回 ScrapMem 均正常。
- 手机首页、论文页、博客页、研究项目详情：scrollWidth 等于 viewport，未见横向溢出；首页无失效图片。
- News 生产显示：`2026.11`、`2026.10`、`2026 · Month TBD`，没有将内部日期排序键误作实际月日。
- Google Scholar：用户补充后已接入首页、网站社交配置和 Person JSON-LD，实际 GET 返回 HTTP 200，并在浏览器确认按钮目标。
- 公开 CV：重新生成一页公开版并渲染检查，无原简历的电话、年龄、性别、政治面貌、求职意向、私人地址。
- 博客：保研经验文章已由用户确认加入首页、博客列表、分类标签、RSS、sitemap 与全文搜索；发布指南继续保留为草稿，不生成公开路由。9 张配图已接入并采用 lazy loading。
- `start-local.command`：通过 zsh 语法检查，使用锁定 Yarn CLI，并兼容当前电脑的 Codex Node 运行时。

没有创建远程仓库、没有提交或推送、没有发布到 GitHub Pages 或 Sites。

## 首页第二版：侧栏与轻交互

- 桌面首页采用 220px 个人资料栏与学术正文分栏，头像位于姓名上方；手机上头像位于姓名左侧。
- 个人资料栏整合 Email、GitHub、Google Scholar、CV 与当前区块导航。只有可完整容纳时才吸附侧栏；展开研究图谱后高度变化会重新计算。
- 动效只包括轻微卡片悬停、外链箭头反馈、一次性内容淡入及展开图谱的节点呼吸效果；遵循 prefers-reduced-motion。
- MAC 官网链接已加入资料栏、About Me、教育经历、研究经历列表和具身项目详情；不在整张项目链接内部嵌套外链。
- 18 页构建与 Pagefind 索引成功，外链属性与本地资源检查通过；83 项单元测试通过。
