# webman-manual-zh-cn-skill

一个面向 Codex / OpenAI Skills 的 webman v2 中文手册技能。

它把 `webman-php/webman-manual` 仓库中的 `resource/doc/zh-cn` 手册整理为技能引用资料，并提供一个本地检索脚本，方便 AI 在回答 webman 安装、路由、中间件、数据库、插件、队列、升级和排障问题时先查官方中文手册。

## 适用场景

- 让 Codex 在排查 webman 项目问题时优先参考官方中文手册。
- 查询 webman v2 的路由、请求、响应、中间件、配置、多应用、协程等基础功能。
- 查询数据库、Redis、Cache、队列、组件、基础插件、应用插件等章节。
- 给团队或个人的 AI 编程环境增加 webman 专用知识。

## 安装

把本仓库克隆到 Codex skills 目录，并确保目录名是 `webman-manual-zh-cn`。

Windows:

```powershell
git clone https://github.com/cshitian/webman-manual-zh-cn-skill `
  $env:USERPROFILE\.codex\skills\webman-manual-zh-cn
```

macOS / Linux:

```bash
git clone https://github.com/cshitian/webman-manual-zh-cn-skill \
  ~/.codex/skills/webman-manual-zh-cn
```

如果你是下载 zip，也可以手动解压到：

```text
~/.codex/skills/webman-manual-zh-cn
```

Windows 对应路径通常是：

```text
C:\Users\<用户名>\.codex\skills\webman-manual-zh-cn
```

安装后重新开启一个 Codex 会话，让技能元数据重新加载。

## 使用方式

直接点名技能：

```text
用 webman-manual-zh-cn 技能查一下：webman 怎么配置路由？
```

排查项目问题：

```text
用 webman-manual-zh-cn 技能排查这个 webman 启动错误：...
```

也可以在项目的 `AGENTS.md` 中加入约定：

```markdown
## Webman 排查规则
- 排查 webman 项目的安装、启动、路由、中间件、数据库、插件、队列、配置、升级或运行时报错时，先使用 `webman-manual-zh-cn` 技能。
- 先查官方手册 references，再结合当前项目代码判断。
- 不确定章节时，使用技能里的 `scripts/search_webman_docs.py <关键词>` 检索。
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

- `SKILL.md`：技能触发描述、使用流程和主题导航。
- `references/zh-cn/`：webman v2 中文手册 Markdown 镜像。
- `scripts/search_webman_docs.py`：本地关键词检索脚本。
- `agents/openai.yaml`：Codex UI 元数据。

## 验证

检查检索脚本：

```bash
python scripts/search_webman_docs.py 路由 --limit 2
```

预期会返回 `route.md` 等相关章节。

如果你的环境有 Codex skill-creator 的校验脚本，可以运行：

```bash
python -X utf8 <path-to-skill-creator>/scripts/quick_validate.py ~/.codex/skills/webman-manual-zh-cn
```

Windows 中文环境建议加 `-X utf8`，避免校验脚本按 GBK 读取中文 `SKILL.md`。

## 文档来源

手册内容来源于：

```text
https://github.com/webman-php/webman-manual/tree/master/resource/doc/zh-cn
```

本仓库只是把中文手册整理为 AI skill 形式，便于本地 AI 编程助手按需查阅。文档版权、署名和许可请以原仓库为准。
