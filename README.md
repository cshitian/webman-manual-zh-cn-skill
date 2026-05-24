# webman-manual-zh-cn-skill

一个面向 AI 编程助手（OpenCode / Claude Code / Codex 等）的 webman v2 综合技能，融合了官方中文手册、命令速查和代码模板。

核心功能：
- **中文手册镜像** — 将 `webman-php/webman-manual` 仓库的 `resource/doc/zh-cn` 手册整理为 110+ 篇引用资料，并附带本地检索脚本。
- **命令速查** — 整合 `webman-command-skill` 的 CLI 操作矩阵，覆盖 start/stop/reload/restart/status 等服务生命周期管理。
- **代码模板** — 整合 `webman-php/skills` 官方最佳实践，提供控制器、模型、中间件、WebSocket、自定义进程和路由的可复用模板。

## 适用场景

- 查询 webman v2 的路由、请求、响应、中间件、配置、多应用、协程等基础功能。
- 查询数据库、Redis、Cache、队列、组件、基础插件、应用插件等章节。
- 排查 CLI 错误（class not found、端口冲突、代码不生效、reload vs restart 选择）。
- 快速获取控制器、模型、中间件、WebSocket、自定义进程等代码模板。
- 给团队或个人的 AI 编程环境增加 webman 专用知识。

## 安装

把本仓库克隆到 AI 助手的 skills 目录，确保目录名是 `webman-manual-zh-cn`。

### OpenCode

```powershell
git clone https://github.com/cshitian/webman-manual-zh-cn-skill `
  $env:USERPROFILE\.opencode\skills\webman-manual-zh-cn
```

### Claude Code / Codex

Windows:

```powershell
git clone https://github.com/cshitian/webman-manual-zh-cn-skill `
  $env:USERPROFILE\.claude\skills\webman-manual-zh-cn
```

macOS / Linux:

```bash
git clone https://github.com/cshitian/webman-manual-zh-cn-skill \
  ~/.claude/skills/webman-manual-zh-cn
```

如果你是下载 zip，也可以手动解压到对应的 skills 目录，安装后重新开启会话让技能元数据重新加载。

## 使用方式

### 查手册

```text
用 webman-manual-zh-cn 查一下：webman 怎么配置多应用路由？
用 webman-manual-zh-cn 查一下：数据库查询支持哪些方法？
```

### 问命令

```text
用 webman-manual-zh-cn：代码改了不生效，应该 reload 还是 restart？
用 webman-manual-zh-cn：class not found 怎么排查？
```

### 要代码模板

```text
用 webman-manual-zh-cn 写一个 RESTful 控制器。
用 webman-manual-zh-cn 给我一个 WebSocket 聊天室示例。
```

### 排查项目问题

```text
用 webman-manual-zh-cn 排查这个 webman 启动错误：...
```

也可以在项目的 `AGENTS.md` 中加入约定：

```markdown
## Webman 开发约定
- 查功能用法、命令操作、排障或要代码模板时，先使用 `webman-manual-zh-cn` 技能。
- 优先参考 SKILL.md 中的命令速查和代码模板章节。
- 主题不明确时，使用 `scripts/search_webman_docs.py <关键词>` 检索手册。
```

## 手动检索

技能内置了一个简单的关键词检索脚本：

```bash
python scripts/search_webman_docs.py 路由
```

限制输出数量：

```bash
python scripts/search_webman_docs.py 数据库 --limit 5
```

脚本会输出匹配的 Markdown 文件路径、标题和片段，便于快速定位章节。

## 目录结构

```text
webman-manual-zh-cn/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── index.md
│   └── zh-cn/
│       ├── SUMMARY.md
│       ├── README.md
│       ├── route.md
│       ├── db/
│       ├── plugin/
│       ├── app/
│       └── ...
└── scripts/
    └── search_webman_docs.py
```

## 技能内容

- `SKILL.md`：技能触发描述、使用流程、主题导航、命令速查、代码模板。
- `references/zh-cn/`：webman v2 中文手册 Markdown 镜像。
- `scripts/search_webman_docs.py`：本地关键词检索脚本。
- `agents/openai.yaml`：Codex UI 元数据。

## 整合来源

本技能整合了以下社区和官方仓库的内容：

- **[webman-php/webman-manual](https://github.com/webman-php/webman-manual)** — 官方中文手册全文镜像，作为参考资料的基础。
- **[0xunknownz/webman-command-skill](https://github.com/0xunknownz/webman-command-skill)** — 命令速查与决策矩阵（reload vs restart、部署流程、排障命令等），整合在 SKILL.md 的命令速查章节。
- **[webman-php/skills](https://github.com/webman-php/skills)** — 官方代码模板与最佳实践（控制器/模型/中间件/WebSocket/进程/路由），整合在 SKILL.md 的代码模板章节。

## 验证

### 检索脚本

```bash
python scripts/search_webman_docs.py 路由 --limit 2
```

预期会返回 `route.md` 等相关章节。

### SKILL.md 命令速查

检查 SKILL.md 中是否包含服务生命周期和代码生成命令章节：

```bash
grep -q "服务生命周期" SKILL.md && echo "命令速查 ✓"
grep -q "代码模板" SKILL.md && echo "代码模板 ✓"
```

## 文档来源

手册内容来源于：

```text
https://github.com/webman-php/webman-manual/tree/master/resource/doc/zh-cn
```

本仓库只是把中文手册整理为 AI skill 形式，便于本地 AI 编程助手按需查阅。文档版权、署名和许可请以原仓库为准。
