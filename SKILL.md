---
name: webman-manual-zh-cn
description: 面向 webman v2 中文手册的检索与答疑技能；用于安装、路由、请求/响应、中间件、视图、静态文件、session、异常、日志、配置、多应用、协程、数据库、队列、插件、进程、升级或排障等问题。
---

# webman 中文手册

## 使用方式
- 将 `references/zh-cn/SUMMARY.md` 作为总目录。
- 先读最小且最相关的文档，再补充相邻章节。
- 以手册内容为准；与记忆冲突时，优先手册。

## 主题导航
- 入门与安装: `README.md`, `attention.md`, `help.md`, `install.md`, `bt-install.md`, `directory.md`, `tutorial.md`
- HTTP 与运行时: `request.md`, `response.md`, `controller.md`, `route.md`, `middleware.md`, `view.md`, `static.md`, `session.md`, `exception.md`, `log.md`, `config.md`, `multiapp.md`, `coroutine/coroutine.md`
- 数据库: `db/tutorial.md`, `db/config.md`, `db/queries.md`, `db/model.md`, `db/relationships.md`, `db/paginator.md`, `db/migration.md`, `db/redis.md`, `db/cache.md`, `db/mongo.md`, `db/thinkorm.md`, `db/thinkcache.md`, `db/medoo.md`
- 组件: `components/*.md`
- 插件: `plugin/*.md`, `app/*.md`
- 进阶与运维: `process.md`, `di.md`, `aop.md`, `others/*.md`, `upgrade/*.md`, `thanks.md`

## 检索流程
- 主题不明确或横跨多章时，先运行 `python scripts/search_webman_docs.py <关键词>`.
- 用脚本输出的文件路径定位到具体章节，再继续阅读。
- 需要安装、配置或排障时，先看对应章节的总览页，再看子章节。

## 参考资料
- `references/zh-cn/README.md`：项目概览。
- `references/zh-cn/SUMMARY.md`：官方目录映射。
- `references/zh-cn/`：源手册的完整镜像。
