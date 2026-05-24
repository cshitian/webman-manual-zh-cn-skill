---
name: webman-manual-zh-cn
description: 面向 webman v2 中文手册的检索与答疑技能；用于安装、路由、请求/响应、中间件、视图、静态文件、session、异常、日志、配置、多应用、协程、数据库、队列、插件、进程、升级、排障、命令行操作（start/stop/reload/restart/status/php webman）、class not found、端口冲突、composer 依赖、代码模板（控制器/模型/中间件/WebSocket/进程/路由/定时任务/CRUD）等。
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

## 命令速查

### 服务生命周期

| 场景 | 命令 | 说明 |
|---|---|---|
| 开发环境启动 | `php start.php start` | 前台模式，日志直接输出终端 |
| 生产环境启动 | `php start.php start -d` | 守护模式 |
| 停止服务 | `php start.php stop` | 正常停止 |
| 强制停止 | `php start.php stop -g` | 正常停止无效时使用 |
| 重启服务 | `php start.php restart -d` | 配置/进程/依赖变更后使用 |
| 重载代码 | `php start.php reload` | 普通业务代码变更后使用，无停机 |
| 查看状态 | `php start.php status` | 检查进程运行状态 |
| 查看连接 | `php start.php connections` | 调试连接数、WebSocket 等 |

> reload vs restart：业务代码（控制器/模型/服务）改后用 reload；Composer 依赖、config/process.php、config/server.php、.env、队列注册、进程注册、bootstrap 改后用 restart。

### 生成代码 (php webman)

需要先安装 `composer require webman/console`，完整清单见 `references/zh-cn/plugin/console.md`。

| 命令 | 说明 |
|---|---|
| `php webman make:controller UserController` | 生成控制器 |
| `php webman make:model User` | 生成模型 |
| `php webman make:crud --table=users` | 生成完整 CRUD |
| `php webman make:middleware Auth` | 生成中间件 |
| `php webman make:command user:list` | 生成控制台命令 |
| `php webman make:process MyProcess` | 生成自定义进程 |
| `php webman make:bootstrap MyBootstrap` | 生成启动初始化类 |
| `php webman route:list` | 列出所有路由 |
| `php webman version` | 查看版本 |

### 构建与部署

| 命令 | 说明 |
|---|---|
| `php webman build:phar` | 打包为 PHAR |
| `php webman build:bin 8.2` | 打包为独立二进制 |
| `php webman install` | 运行安装脚本 |
| `php webman fix-disable-functions` | 修复禁用函数 |

### Composer

| 命令 | 说明 |
|---|---|
| `composer install --no-dev --optimize-autoloader` | 生产依赖安装 |
| `composer dump-autoload` | 刷新自动加载（class not found 时先试） |
| `composer require webman/console` | 安装命令行组件 |

### 队列

| 命令 | 说明 |
|---|---|
| `php webman redis-queue:consumer send-mail` | 生成 Redis 队列消费者 |
| `php start.php restart -d` | 队列消费者变更后必须 restart |

### 排障常见命令

| 场景 | 命令 |
|---|---|
| class not found | `composer dump-autoload && php start.php restart -d` |
| 端口冲突 | `lsof -i:8787` / `ss -ntlp \| grep 8787` |
| 代码变更不生效 | `php start.php reload` |
| reload 不生效 | `php start.php restart -d` |
| 查看日志 | `tail -f runtime/logs/webman.log` |

详细排障流程见：`references/zh-cn/others/process.md`、`plugin/console.md`。

## 代码模板

### 控制器（RESTful）

```php
<?php
namespace app\controller;

use support\Request;
use support\Response;

class UserController
{
    public function index(Request $request): Response
    {
        $users = \app\model\User::paginate($request->get('limit', 15));
        return json(['code' => 0, 'msg' => 'success', 'data' => $users]);
    }

    public function store(Request $request): Response
    {
        $data = $request->post();
        // 验证略，详见 references/zh-cn/controller.md
        $user = \app\model\User::create($data);
        return json(['code' => 0, 'msg' => 'success', 'data' => $user]);
    }

    public function show(Request $request, $id): Response
    {
        $user = \app\model\User::find($id);
        if (!$user) return json(['code' => 404, 'msg' => '不存在'], 404);
        return json(['code' => 0, 'msg' => 'success', 'data' => $user]);
    }

    public function update(Request $request, $id): Response
    {
        $user = \app\model\User::find($id);
        if (!$user) return json(['code' => 404, 'msg' => '不存在'], 404);
        $user->update($request->post());
        return json(['code' => 0, 'msg' => 'success', 'data' => $user]);
    }

    public function destroy(Request $request, $id): Response
    {
        $user = \app\model\User::find($id);
        if (!$user) return json(['code' => 404, 'msg' => '不存在'], 404);
        $user->delete();
        return json(['code' => 0, 'msg' => 'success']);
    }
}
```

详见 `references/zh-cn/controller.md`。

### 模型（Eloquent）

```php
<?php
namespace app\model;

use support\Model;

class User extends Model
{
    protected $table = 'users';
    protected $primaryKey = 'id';
    protected $fillable = ['name', 'email', 'password', 'status'];
    protected $hidden = ['password', 'deleted_at'];
    protected $casts = ['status' => 'integer', 'created_at' => 'datetime', 'updated_at' => 'datetime'];

    public function profile() { return $this->hasOne(UserProfile::class); }
    public function orders() { return $this->hasMany(Order::class); }
    public function roles() { return $this->belongsToMany(Role::class, 'user_roles'); }

    public function setPasswordAttribute($value)
    {
        $this->attributes['password'] = password_hash($value, PASSWORD_DEFAULT);
    }
}
```

详见 `references/zh-cn/db/model.md`。

### 中间件

```php
<?php
namespace app\middleware;

use Webman\MiddlewareInterface;
use Webman\Http\Response;
use Webman\Http\Request;

class AuthMiddleware implements MiddlewareInterface
{
    public function process(Request $request, callable $next): Response
    {
        $token = $request->header('Authorization');
        if (empty($token)) return json(['code' => 401, 'msg' => '请先登录'], 401);
        // 验证 token 逻辑…
        return $next($request);
    }
}
```

详见 `references/zh-cn/middleware.md`。

### WebSocket 服务

```php
<?php
namespace app\websocket;

use Workerman\Connection\TcpConnection;

class Chat
{
    public function onConnect(TcpConnection $connection) { echo "新连接: {$connection->id}\n"; }

    public function onMessage(TcpConnection $connection, $data)
    {
        $msg = json_decode($data, true);
        foreach ($connection->worker->connections as $conn) {
            $conn->send(json_encode([
                'type' => 'message',
                'from' => $connection->uid ?? 'anonymous',
                'content' => $msg['content'] ?? '',
                'time' => date('Y-m-d H:i:s')
            ]));
        }
    }

    public function onClose(TcpConnection $connection) { echo "连接关闭: {$connection->id}\n"; }
}
```

`config/process.php` 配置：

```php
<?php
return [
    'websocket' => [
        'handler' => app\websocket\Chat::class,
        'listen' => 'websocket://0.0.0.0:8282',
        'count' => 4,
    ],
];
```

详见 `references/zh-cn/others/process.md`。

### 自定义进程 + 定时任务

```php
<?php
namespace process;

use Workerman\Timer;

class Task
{
    public function onWorkerStart()
    {
        Timer::add(60, function () {
            \app\model\Session::where('expire_time', '<', time())->delete();
        });
    }
}
```

`config/process.php` 配置：

```php
<?php
return [
    'task' => [
        'handler' => process\Task::class,
        'count' => 1,
    ],
];
```

详见 `references/zh-cn/process.md`。

### 路由配置

```php
<?php
use Webman\Route;

Route::get('/', fn($r) => response('Hello Webman'));
Route::resource('/users', app\controller\UserController::class);
Route::group('/api', function () {
    Route::post('/login', [app\controller\AuthController::class, 'login']);
    Route::post('/logout', [app\controller\AuthController::class, 'logout']);
})->middleware([app\middleware\CorsMiddleware::class]);
Route::get('/user/{id:\d+}', [app\controller\UserController::class, 'show'])->name('user.show');
```

详见 `references/zh-cn/route.md`。

## 参考资料
- `references/zh-cn/README.md`：项目概览。
- `references/zh-cn/SUMMARY.md`：官方目录映射。
- `references/zh-cn/`：源手册的完整镜像。
