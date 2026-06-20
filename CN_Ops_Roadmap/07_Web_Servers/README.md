# 07 · Web 服务器 (Nginx)

> Nginx 是互联网基础设施的基石，也是每一位运维工程师必须掌握的核心技能。"Nginx 是运维的第二门语言"——这句话一点不夸张，反向代理、负载均衡、HTTPS、静态资源服务，几乎每个互联网公司都在用。我刚入行的时候，第一个独立负责的生产环境就是 Nginx 集群，那时候踩了不少坑，也希望这一章能帮你少走弯路。

---

## 🎯 学习目标

读完本章并完成所有实战练习后，你应该能够：

1. **独立部署 Nginx** —— 从源码编译到 yum/apt 安装，掌握两种安装方式及其适用场景
2. **配置虚拟主机** —— 基于域名、端口、IP 的三种虚拟主机配置方式，server_name 匹配优先级
3. **搭建反向代理** —— proxy_pass、proxy_set_header、X-Forwarded-For 透传，理解代理链路中的 IP 问题
4. **实现负载均衡** —— upstream 模块配置，轮询/加权/IP_hash/least_conn 四种算法，健康检查参数
5. **配置 HTTPS 全链路** —— SSL 证书申请（Let's Encrypt）、Nginx SSL 参数调优、HTTP/2 开启、HSTS 安全头
6. **性能调优** —— worker_processes、worker_connections、keepalive、gzip、proxy_cache 等核心参数
7. **日志分析与切割** —— access_log 格式定制、error_log 级别、logrotate 自动切割
8. **安全加固** —— 隐藏版本号、限制请求方法、防 DDoS（limit_req/limit_conn）、防盗链
9. **URL 重写与重定向** —— return、rewrite 指令，301/302 重定向场景，try_files 优雅降级
10. **WebSocket 代理** —— Upgrade 和 Connection 头处理，长连接超时配置
11. **Nginx 与 Lua 扩展** —— OpenResty 入门，用 Lua 实现灰度发布、限流、鉴权
12. **故障排查** —— 常见 502/503/504 错误诊断，stub_status 监控模块，日志定位问题
13. **高可用架构** —— Nginx + Keepalived 双机热备，避免单点故障
14. **容器化部署** —— 编写 Nginx Dockerfile，docker-compose 编排，K8s Ingress Nginx 配置
15. **最佳实践总结** —— 生产环境 Nginx 配置规范，我踩过的 10 个坑及解决方案

---

## 📺 推荐视频教程

以下是我精选的 B 站高质量 Nginx 教程，按学习顺序排列：

| # | 教程标题 | UP 主 | 播放量 | 难度 | 链接 |
|---|---------|-------|--------|------|------|
| 1 | Nginx 入门到实战（全套） | 黑马程序员 | 280.5万 | ⭐ 入门 | [BV1PV411e7F4](https://www.bilibili.com/video/BV1PV411e7F4) |
| 2 | Nginx 反向代理与负载均衡 | 尚硅谷 | 156.2万 | ⭐⭐ 基础 | [BV1zJ411N7Ad](https://www.bilibili.com/video/BV1zJ411N7Ad) |
| 3 | Nginx HTTPS 配置实战 | 腾讯云开发者 | 42.8万 | ⭐⭐ 基础 | [BV1Xx411c7mD](https://www.bilibili.com/video/BV1Xx411c7mD) |
| 4 | Nginx 性能调优深度解析 | 马哥 Linux | 38.6万 | ⭐⭐⭐ 进阶 | [BV1HT4y1m74K](https://www.bilibili.com/video/BV1HT4y1m74K) |
| 5 | OpenResty 从入门到实战 | 张开涛（原拍拍贷架构师） | 25.3万 | ⭐⭐⭐⭐ 高级 | [BV1Ux411A7pF](https://www.bilibili.com/video/BV1Ux411A7pF) |
| 6 | Nginx 模块开发与架构解析 | 陶辉（深入理解 Nginx 作者） | 18.9万 | ⭐⭐⭐⭐⭐ 专家 | [BV1ot4y1X7PZ](https://www.bilibili.com/video/BV1ot4y1X7PZ) |
| 7 | 千万级并发 Nginx 架构实战 | 架构师必备 | 31.2万 | ⭐⭐⭐⭐ 高级 | [BV1gK4y1a71T](https://www.bilibili.com/video/BV1gK4y1a71T) |
| 8 | Nginx + Keepalived 高可用 | 老男孩教育 | 22.7万 | ⭐⭐⭐ 进阶 | [BV1xK4y1Y7Jx](https://www.bilibili.com/video/BV1xK4y1Y7Jx) |

---

## 📖 推荐书籍

| # | 书名 | 作者 | 豆瓣评分 | 推荐理由 |
|---|------|------|---------|---------|
| 1 | 《深入理解 Nginx（第2版）》 | 陶辉 | 9.1 | 源码级分析，Nginx 模块开发必读，我当时入门就是看的这本，虽然有点深但值得反复看 |
| 2 | 《Nginx高性能Web服务器详解》 | 苗泽 | 8.3 | 中文最佳实战指南，配置示例丰富，适合快速上手 |
| 3 | 《Nginx Cookbook》 | Derek DeJonghe | 8.7 | O'Reilly 出品，短小精悍的配方式手册，遇到问题翻一翻 |
| 4 | 《Nginx完全开发指南》 | 罗剑锋 | 8.5 | 涵盖 OpenResty 和 Lua 扩展，适合想深入 Nginx 生态的工程师 |
| 5 | 《Mastering Nginx 2nd Edition》 | Dimitri Aivaliotis | 8.4 | 英文原版，调优和架构设计讲得很透彻，建议有一定基础后阅读 |
| 6 | 《Nginx 实战》 | 张宜成 | 8.0 | 轻量级实战手册，适合 1-2 年运维同学快速补齐 Nginx 技能 |

---

## 🌐 在线参考资源

| # | 资源名称 | 类型 | 链接 | 特色说明 |
|---|---------|------|------|---------|
| 1 | Nginx 官方文档（中文） | 官方文档 | [nginx.org/cn/docs](http://nginx.org/cn/docs/) | 最权威的参考，我遇到参数不理解时第一选择 |
| 2 | Nginx 配置可视化工具 | 在线工具 | [nginx.viraptor.me](https://nginx.viraptor.me) | 生成合规的 nginx.conf，新手友好 |
| 3 | Nginx Beginner's Guide | 官方教程 | [nginx.com/resources/wiki](https://www.nginx.com/resources/wiki/start/) | 官方入门指南，英文但非常清晰 |
| 4 | OpenResty 官方文档 | 官方文档 | [openresty.org/cn](https://openresty.org/cn/) | OpenResty 中文文档，Lua 扩展必看 |
| 5 | Nginx 一线实战（极客时间） | 付费课程 | [time.geekbang.org](https://time.geekbang.org) | 陶辉主讲，和《深入理解 Nginx》配套 |
| 6 | Nginx 配置最佳实践 | GitHub | [github.com/h5bp/server-configs-nginx](https://github.com/h5bp/server-configs-nginx) | h5bp 维护的 Nginx 配置模板，直接可用 |
| 7 | Nginx Prometheus Exporter | 监控 | [github.com/nginxinc/nginx-prometheus-exporter](https://github.com/nginxinc/nginx-prometheus-exporter) | 将 Nginx 指标暴露给 Prometheus |
| 8 | Let's Encrypt 官方 | 工具文档 | [certbot.eff.org](https://certbot.eff.org) | 免费 SSL 证书申请，certbot 使用指南 |
| 9 | Nginx 故障排查手册 | 中文社区 | [wiki.jikexueyuan.com/project/nginx](https://wiki.jikexueyuan.com/project/nginx/) | 极客学院整理的 Nginx 百科，中文友好 |
| 10 | Awesome Nginx | GitHub 合集 | [github.com/freebsdchina/awesome-nginx](https://github.com/freebsdchina/awesome-nginx) | Nginx 生态资源大全，模块/工具/教程一应俱全 |

---

## 📝 核心知识点清单

### 第一阶段：Nginx 基础与安装（10 个知识点）

1. **Nginx 架构模型** —— Master-Worker 进程模型，Event-Driven 异步非阻塞 I/O，对比 Apache prefork/worker 模式的理解
2. **源码编译安装** —— `./configure` 参数详解（`--prefix`、`--with-http_ssl_module`、`--with-http_v2_module`、`--with-http_stub_status_module`），编译参数选择对性能的影响
3. **yum/apt 快速安装** —— `yum install nginx` vs 源码安装的场景选择，官方 yum 源配置（避免系统自带版本过旧）
4. **配置文件结构** —— `nginx.conf` 全局块/events块/http块/server块/location块的层级关系，include 指令组织多文件配置的最佳实践
5. **虚拟主机配置** —— `server_name` 匹配规则（精确匹配 > 通配符前缀 > 通配符后缀 > 正则），基于域名/端口/IP 的三种虚拟主机
6. **location 匹配规则** —— `=` 精确匹配、`^~` 前缀匹配、`~` 正则匹配、`~*` 不区分大小写正则，匹配优先级和实际踩坑案例
7. **静态资源服务** —— `root` vs `alias` 的区别（root 会拼接 location 路径，alias 不会），`autoindex` 目录浏览，过期时间控制
8. **MIME 类型配置** —— `types` 指令和 `default_type`，为什么 CSS/JS 有时会被下载而不是加载
9. **日志系统** —— `access_log` 和 `error_log` 配置，自定义日志格式（`log_format`），`$request_time` vs `$upstream_response_time` 的区别
10. **Nginx 信号控制** —— `nginx -s reload/stop/quit/reopen`，`kill -HUP` 实现平滑重启，`kill -USR1` 重新打开日志文件

### 第二阶段：反向代理与负载均衡（12 个知识点）

11. **proxy_pass 配置精髓** —— URL 后面带 `/` 和不带 `/` 的天壤之别（我见过太多人踩这个坑），代理路径拼接规则详解
12. **请求头透传** —— `proxy_set_header Host $host`、`X-Real-IP $remote_addr`、`X-Forwarded-For $proxy_add_x_forwarded_for`，多层代理下的真实 IP 获取
13. **upstream 负载均衡** —— upstream 块定义后端服务器组，`server` 指令的 `weight`、`max_fails`、`fail_timeout`、`backup` 参数详解
14. **负载均衡算法** —— 轮询（默认）、加权轮询（`weight`）、`ip_hash`（会话保持）、`least_conn`（最少连接）、`hash $request_uri`（一致性哈希）
15. **健康检查机制** —— Nginx 被动健康检查（`max_fails` + `fail_timeout`），主动健康检查（Nginx Plus 或 `nginx_upstream_check_module` 第三方模块）
16. **proxy 超时控制** —— `proxy_connect_timeout`、`proxy_send_timeout`、`proxy_read_timeout`，504 Gateway Timeout 的常见原因
17. **SSL/TLS 代理** —— `proxy_ssl_*` 系列指令，Nginx 终止 SSL 后转发给后端 HTTP（SSL Offloading），减少后端压力
18. **缓存代理** —— `proxy_cache` 配置，`proxy_cache_path` 定义缓存 zone，`proxy_cache_valid` 按状态码设置缓存时间，`proxy_cache_bypass` 绕过缓存
19. **gzip 压缩** —— `gzip on`、`gzip_types`、`gzip_comp_level`，压缩与代理缓存的配合，什么内容不该压缩（图片/视频已压缩过）
20. **连接池优化** —— `proxy_http_version 1.1`、`proxy_set_header Connection ""`、`keepalive` 连接保活，减少 TCP 建连开销
21. **限流防护** —— `limit_req_zone` + `limit_req` 漏桶算法限流，`limit_conn_zone` + `limit_conn` 并发连接限制，防止 CC 攻击
22. **访问控制** —— `allow`/`deny` IP 白名单，`auth_basic` 基础认证，`satisfy` 指令实现 IP 或密码的或逻辑

### 第三阶段：HTTPS 与安全加固（10 个知识点）

23. **SSL/TLS 基础** —— TLS 握手过程，对称加密 vs 非对称加密，为什么 TLS 1.2 以下不安全
24. **证书申请与配置** —— Let's Encrypt 免费证书（`certbot`），商用证书（DigiCert/GlobalSign），证书链完整性，`ssl_certificate` 配置注意事项
25. **Nginx SSL 参数调优** —— `ssl_protocols TLSv1.2 TLSv1.3`、`ssl_ciphers` 密码套件选择、`ssl_prefer_server_ciphers on`、`ssl_session_cache` 会话复用
26. **HTTP/2 开启** —— `listen 443 ssl http2`，HTTP/2 多路复用优势，握手延迟降低，是否需要关闭 TLS 1.0/1.1
27. **HTTP 强制跳转 HTTPS** —— `return 301 https://$server_name$request_uri;` vs `rewrite ^(.*)$ https://$host$1 permanent;`，前者性能更好
28. **HSTS 安全头** —— `add_header Strict-Transport-Security "max-age=31536000" always;`，防止 SSL Stripping 攻击，预加载列表（HSTS Preload）
29. **安全头配置** —— `X-Frame-Options`、`X-Content-Type-Options`、`X-XSS-Protection`、`Content-Security-Policy`，OWASP 安全头规范
30. **防盗链** —— `valid_referers` + `rewrite`，防止别人直接引用你的图片/视频资源，节省带宽
31. **隐藏 Nginx 版本号** —— `server_tokens off;`，防止攻击者根据版本号针对性利用已知漏洞
32. **Web 应用防火墙（WAF）** —— Nginx + ModSecurity 或 OpenResty + lua-resty-waf，防护 SQL 注入/XSS/CC 攻击

### 第四阶段：高级特性与性能调优（13 个知识点）

33. **Worker 进程优化** —— `worker_processes auto;`（Auto 等于 CPU 核数），`worker_cpu_affinity` 绑核，`worker_rlimit_nofile` 文件描述符限制
34. **连接数调优** —— `worker_connections`（单个 worker 最大连接数），总并发 = worker_processes × worker_connections，`ulimit -n` 系统级配合
35. **keepalive 调优** —— `keepalive_timeout`、`keepalive_requests`，长连接复用减少 TCP 开销，移动端网络下的调优建议
36. **sendfile + tcp_nopush** —— `sendfile on;`、`tcp_nopush on;`、`tcp_nodelay on;`，零拷贝和 TCP 发包优化，为什么这三个要配合使用
37. **proxy_buffering** —— `proxy_buffering on/off`，缓冲区大小设置（`proxy_buffer_size`、`proxy_buffers`），大文件下载场景的特殊处理
38. **open_file_cache** —— 缓存文件元信息（fd、大小、修改时间），减少 stat() 系统调用，`open_file_cache_errors` 也要开启
39. **try_files 指令** —— 优雅的前端路由支持（SPA 应用），`try_files $uri $uri/ /index.html;`，比 rewrite 性能更好
40. **rewrite 规则** —— `last` vs `break` vs `redirect` vs `permanent`，正则表达式捕获组，避免死循环（Nginx 最多 10 次内部重定向）
41. **Nginx 变量系统** —— 内置变量（`$uri`、`$args`、`$http_user_agent` 等），`set` 指令自定义变量，`map` 指令做条件映射
42. **Lua 扩展（OpenResty）** —— `content_by_lua_file`、`access_by_lua_block`，用 Lua 实现灰度发布、AB 测试、动态封禁 IP
43. **Nginx 监控** —— `stub_status` 模块开启（`active`、`accepts`、`handled`、`requests`、`reading`、`writing`、`waiting`），接入 Prometheus + Grafana
44. **日志切割** —— `logrotate` 配置（`/etc/logrotate.d/nginx`），`postrotate` 里执行 `kill -USR1`，防止日志文件过大
45. **Nginx + Keepalived** —— VRRP 协议，双机热备配置，VIP 漂移，脑裂问题及解决

### 第五阶段：容器化与生产实践（10 个知识点）

46. **Nginx Docker 镜像选择** —— `nginx:alpine`（推荐，体积小）vs `nginx:latest`，自定义 Dockerfile 的最佳实践
47. **Nginx Ingress Controller** —— K8s 中的 Nginx，对比原生 Nginx 的配置差异，`ingress-nginx` 注解（annotations）配置
48. **配置模板与自动化** —— `consul-template` 动态生成 upstream，`Jinja2` 模板管理 Nginx 配置，避免手动改配置的繁琐和出错
49. **灰度发布支持** —— 基于 `split_clients` 的流量切分，或 OpenResty + Lua 实现更灵活的灰度策略
50. **大文件上传** —— `client_max_body_size`、`client_body_buffer_size`、`client_body_temp_path`，超时时间配合调整
51. **跨域（CORS）配置** —— `add_header 'Access-Control-Allow-Origin'`，复杂请求（PUT/DELETE）的 OPTIONS 预检处理
52. **WebSocket 代理** —— `proxy_http_version 1.1`、`proxy_set_header Upgrade $http_upgrade`、`proxy_set_header Connection "upgrade"`，`proxy_read_timeout` 延长避免断开
53. **Nginx 单元测试** —— `Test::Nginx`（Perl 模块），配置变更前的自动化测试，防止上线踩坑
54. **故障案例库** —— 502 Bad Gateway（后端挂了/upstream 配置错误）、503 Service Temporarily Unavailable（限流触发）、504 Gateway Timeout（后端响应超时）、403 Forbidden（权限/SELinux）
55. **Nginx 配置审查清单** —— 我整理的一份生产环境上线前检查清单，涵盖安全、性能、可用性三个维度，建议每次上线前过一遍

---

## 💻 实战命令/配置示例

以下是我日常运维中最常用的 Nginx 配置片段，每个都加了详细注释：

### 示例 1：完整的主配置文件结构（nginx.conf）

```nginx
# ==================== 全局块 ====================
# 设置 worker 进程数，auto 表示等于 CPU 核数
worker_processes auto;

# 指定 Nginx 进程 PID 文件位置
pid /var/run/nginx.pid;

# 错误日志路径和级别（debug/info/notice/warn/error/crit/alert/emerg）
error_log /var/log/nginx/error.log warn;

# worker 进程最大可打开的文件描述符数
worker_rlimit_nofile 65535;

# ==================== events 块 ====================
events {
    # 使用 epoll 多路复用模型（Linux 2.6+ 推荐）
    use epoll;
    
    # 单个 worker 进程允许的最大连接数
    # 总并发 = worker_processes × worker_connections
    worker_connections 10240;
    
    # 允许一个 worker 进程同时接受多个网络连接
    multi_accept on;
}

# ==================== http 块 ====================
http {
    # 引入 MIME 类型定义
    include /etc/nginx/mime.types;
    
    # 默认 MIME 类型（当文件类型未匹配时）
    default_type application/octet-stream;
    
    # 开启高效文件传输模式（零拷贝）
    sendfile on;
    
    # 在一个数据包中发送所有头文件（仅 sendfile 开启时有效）
    tcp_nopush on;
    
    # 禁用 Nagle 算法，小包立即发送（提高实时性）
    tcp_nodelay on;
    
    # keepalive 超时时间（客户端连接保持时间）
    keepalive_timeout 65;
    
    # keepalive 请求数上限（超过后断开重连）
    keepalive_requests 1000;
    
    # 开启 gzip 压缩
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;  # 压缩级别 1-9，6 是性价比最高的
    gzip_types text/plain text/css text/xml text/javascript 
               application/json application/javascript application/xml+rss;
    
    # 关闭 Nginx 版本号显示（安全加固）
    server_tokens off;
    
    # 引入所有站点配置（虚拟主机）
    include /etc/nginx/conf.d/*.conf;
}
```

### 示例 2：反向代理 + 负载均衡 + HTTPS 完整配置

```nginx
# 定义上游服务器组（负载均衡后端）
upstream api_backend {
    # 最少连接算法（适合请求处理时间差异大的场景）
    least_conn;
    
    # 后端服务器，weight 是权重，max_fails 是最大失败次数
    # fail_timeout 是熔断时间，backup 是备份服务器（主服务器都挂了才启用）
    server 10.0.1.101:8080 weight=5 max_fails=3 fail_timeout=30s;
    server 10.0.1.102:8080 weight=3 max_fails=3 fail_timeout=30s;
    server 10.0.1.103:8080 weight=2 max_fails=3 fail_timeout=30s;
    server 10.0.1.104:8080 backup;
    
    # 保持 32 个到后端的空闲 keepalive 连接（减少 TCP 建连开销）
    keepalive 32;
}

# ==================== HTTP 强制跳转 HTTPS ====================
server {
    listen 80;
    listen [::]:80;
    server_name api.example.com;
    
    # 301 永久重定向到 HTTPS（return 比 rewrite 性能更好）
    return 301 https://$server_name$request_uri;
}

# ==================== HTTPS 主服务 ====================
server {
    # 监听 443 端口，开启 SSL 和 HTTP/2
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name api.example.com;
    
    # SSL 证书配置
    ssl_certificate     /etc/nginx/ssl/api_example_com_fullchain.pem;  # 全链路证书（含中间证书）
    ssl_certificate_key /etc/nginx/ssl/api_example_com.key;
    
    # TLS 协议和密码套件（禁用不安全的 TLS 1.0/1.1）
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;  # TLS 1.3 不需要服务端密码偏好
    
    # SSL 会话复用（减少 TLS 握手开销）
    ssl_session_cache shared:SSL:10m;  # 共享内存 10MB，约可存 4 万个会话
    ssl_session_timeout 1d;
    
    # 安全头配置
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;  # HSTS
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    
    # ==================== 反向代理核心配置 ====================
    location / {
        # 转发到 upstream 定义的后端组
        proxy_pass http://api_backend;
        
        # 透传必要的请求头
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # 使用 HTTP/1.1 连接后端（支持 keepalive）
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        
        # 超时控制（单位：秒）
        proxy_connect_timeout 5;   # 连接后端超时
        proxy_send_timeout 60;     # 向后端发送请求超时
        proxy_read_timeout 60;     # 等待后端响应超时（影响长连接接口）
        
        # 关闭代理缓冲（适合实时性要求高的接口；如果接口响应大，开启更好）
        # proxy_buffering off;
        
        # 如果开启缓冲，设置缓冲区大小
        proxy_buffer_size 16k;
        proxy_buffers 16 16k;
    }
    
    # ==================== 健康检查端点（供负载均衡器探测） ====================
    location /health {
        access_log off;
        return 200 "OK\n";
        add_header Content-Type text/plain;
    }
    
    # ==================== 拒绝访问 .git 等敏感目录 ====================
    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
    }
}
```

### 示例 3：静态资源服务器（含缓存和 CORS）

```nginx
server {
    listen 80;
    server_name static.example.com;
    
    # 静态文件根目录
    root /data/static;
    
    # 全局访问日志关闭（静态资源日志量大，酌情开启）
    access_log off;
    
    # ==================== 图片资源（设置长期缓存） ====================
    location ~* \.(jpg|jpeg|png|gif|ico|webp|avif)$ {
        # 过期时间 30 天（用户再次访问时直接从浏览器缓存读取）
        expires 30d;
        add_header Cache-Control "public, immutable";
        add_header Access-Control-Allow-Origin *;  # 允许跨域引用
        
        # 尝试原路径，不存在则返回 404
        try_files $uri =404;
    }
    
    # ==================== CSS/JS 资源（设置缓存，但加版本号时可用） ====================
    location ~* \.(css|js)$ {
        expires 7d;
        add_header Cache-Control "public";
    }
    
    # ==================== 字体文件（CORS 必须配置，否则跨域加载失败） ====================
    location ~* \.(woff|woff2|ttf|eot|otf)$ {
        expires 30d;
        add_header Access-Control-Allow-Origin *;
    }
    
    # ==================== 防盗链（仅允许 example.com 引用图片） ====================
    location ~* \.(jpg|jpeg|png|gif)$ {
        valid_referers none blocked *.example.com example.com;
        if ($invalid_referer) {
            return 403;
            # 或者返回一张"防盗链"提示图：rewrite ^ /anti-leech.jpg last;
        }
    }
}
```

### 示例 4：Nginx 限流配置（防 CC 攻击）

```nginx
# 定义限流 zone：限制每个 IP 每秒最多 10 个请求，突发 20 个
# zone=mylimit:10m 表示共享内存 10MB，约可存 16 万个 IP 的状态
limit_req_zone $binary_remote_addr zone=mylimit:10m rate=10r/s;

# 限制每个 IP 的并发连接数为 20
limit_conn_zone $binary_remote_addr zone=perip:10m;

server {
    location /api/ {
        # 应用限流：burst=20 允许排队 20 个请求，nodelay 表示排队请求立即处理
        limit_req zone=mylimit burst=20 nodelay;
        
        # 应用并发限制
        limit_conn perip 20;
        
        # 超过限制时返回 429 状态码（Too Many Requests）
        limit_req_status 429;
        limit_conn_status 429;
        
        proxy_pass http://api_backend;
    }
}
```

### 示例 5：Nginx 日志格式定制 + logrotate 配置

```nginx
# 在 http 块中定义自定义日志格式
http {
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for" '
                    'upstream: $upstream_addr rt=$request_time urt=$upstream_response_time';
    
    access_log /var/log/nginx/access.log main;
}
```

```bash
# /etc/logrotate.d/nginx —— 日志切割配置
/var/log/nginx/*.log {
    daily                 # 每天切割
    missingok             # 日志文件不存在时不报错
    rotate 30             # 保留 30 天的日志
    compress              # 切割后的日志压缩
    delaycompress         # 延迟一天压缩（方便查昨天的日志）
    notifempty            # 空文件不切割
    create 0640 nginx adm  # 新日志文件权限
    sharedscripts
    postrotate
        # 发送 USR1 信号让 Nginx 重新打开日志文件
        [ -f /var/run/nginx.pid ] && kill -USR1 $(cat /var/run/nginx.pid)
    endscript
}
```

### 示例 6：Nginx stub_status 监控配置

```nginx
# 仅允许内网访问的监控端点
server {
    listen 127.0.0.1:8080;
    server_name localhost;
    
    location /nginx_status {
        stub_status on;
        allow 127.0.0.1;     # 仅允许本机
        allow 10.0.0.0/8;    # 允许内网
        deny all;              # 其余拒绝
        access_log off;
    }
}
```

### 示例 7：Nginx + Keepalived 高可用配置（简要）

```bash
# Keepalived 配置（/etc/keepalived/keepalived.conf）
vrrp_instance VI_1 {
    state MASTER            # 另一台配 BACKUP
    interface eth0
    virtual_router_id 51
    priority 100            # MASTER 优先级高（如 100），BACKUP 低（如 50）
    advert_int 1
    
    authentication {
        auth_type PASS
        auth_pass 1111      # 主备密码要一致
    }
    
    virtual_ipaddress {
        10.0.0.100/24       # VIP（虚拟 IP），对外提供服务的 IP
    }
}
```

### 示例 8：OpenResty Lua 实现灰度发布

```nginx
# 基于 Cookie 的灰度发布（命中特定 Cookie 的用户走新版本）
location / {
    access_by_lua_block {
        -- 获取用户 Cookie 中的 gray_flag
        local cookie_gray = ngx.var.cookie_gray_flag
        
        -- 如果 Cookie 中标记了灰度用户，转发到灰度环境
        if cookie_gray == "true" then
            ngx.var.backend = "http://gray_backend"
        else
            ngx.var.backend = "http://prod_backend"
        end
    }
    
    proxy_pass $backend;
}
```

### 示例 9：Nginx 配置文件语法检查与重载

```bash
# 检查 Nginx 配置文件语法（非常重要！改配置后先检查再重载）
nginx -t

# 输出示例（正确）：
# nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
# nginx: configuration file /etc/nginx/nginx.conf test is successful

# 平滑重载配置（不中断服务）
nginx -s reload

# 查看 Nginx 进程状态
ps aux | grep nginx

# 查看 Nginx 监听的端口
ss -tlnp | grep nginx
```

### 示例 10：Nginx Prometheus 监控 Exporter 配置

```yaml
# prometheus.yml 中添加 Nginx 监控
scrape_configs:
  - job_name: 'nginx'
    static_configs:
      - targets: ['localhost:8080']
    metrics_path: /metrics
    # 需要先部署 nginx-prometheus-exporter，并配置 stub_status 或 nginx-plus-api
```

---

## 🧪 实战项目

### 项目 1：搭建高可用 Nginx 反向代理集群

**项目目标**：为内部 Web 服务搭建一套高可用、可扩展的反向代理集群，支持 HTTPS 终止、负载均衡、健康检查。

**步骤**：

1. **准备环境** —— 准备 2 台 Nginx 服务器（master + backup）+ 3 台后端应用服务器
2. **安装 Nginx** —— 两台 Nginx 均采用源码编译安装，开启 `http_ssl_module`、`http_v2_module`、`http_stub_status_module`
3. **配置 upstream 负载均衡** —— 使用 `least_conn` 算法，配置 `max_fails=3`、`fail_timeout=30s` 健康检查
4. **申请 SSL 证书** —— 使用 certbot 申请 Let's Encrypt 免费证书，配置自动续期（crontab）
5. **配置 Keepalived** —— VRRP 协议实现 VIP 漂移，MASTER 优先级 100，BACKUP 优先级 50
6. **开启 stub_status** —— 配置监控端点，接入 Prometheus + Grafana
7. **配置 logrotate** —— 防止 access 日志撑满磁盘
8. **压测验证** —— 使用 `wrk` 或 `ab` 进行压测，验证负载均衡和健康检查是否生效
9. **故障演练** —— 手动停止一台后端，观察流量是否自动切换；重启 Nginx master，观察 VIP 是否漂移

**验收标准**：HTTPS 访问正常、负载均衡按权重分发、后端挂掉自动摘除、Nginx 重启不中断连接。

---

### 项目 2：基于 OpenResty 的 API 网关原型

**项目目标**：用 OpenResty 搭建一个轻量级 API 网关，支持鉴权、限流、灰度发布、日志上报。

**步骤**：

1. **安装 OpenResty** —— `yum install openresty`（先加官方源），验证 `openresty -v`
2. **Lua 鉴权模块** —— 编写 `access_by_lua_file` 脚本，验证请求中的 JWT Token（使用 `lua-resty-jwt` 库）
3. **限流模块** —— 基于 `lua-resty-limit-traffic` 实现更灵活的限流（支持按 IP、按 API Key、按路径）
4. **灰度发布** —— 基于 `ngx.var.cookie_*` 或 `ngx.req.get_headers()` 实现灰度流量调度
5. **日志上报** —— 用 `log_by_lua` 将请求日志异步上报到 Kafka（使用 `lua-resty-kafka`）
6. **监控集成** —— 暴露 Prometheus 格式的 metrics 端点，接入 Grafana 看板

**验收标准**：未带 Token 的请求返回 401、限流触发返回 429、灰度用户路由到新版本、请求日志正确上报 Kafka。

---

## 🔧 常见故障排查

### 故障 1：502 Bad Gateway

**现象**：访问网站返回 502，Nginx error_log 中出现 `connect() failed (111: Connection refused)`

**诊断步骤**：
```
# 1. 检查后端服务是否运行
systemctl status backend-service

# 2. 检查后端端口是否监听
ss -tlnp | grep 8080

# 3. 从 Nginx 服务器测试后端连通性
curl -v http://10.0.1.101:8080/health

# 4. 检查 upstream 配置中的 IP 和端口是否正确
nginx -t && cat /etc/nginx/conf.d/upstream.conf

# 5. 检查防火墙/安全组是否放行
iptables -L -n | grep 8080
```

**解决方案**：启动后端服务 / 修正 upstream 中的 IP:Port / 放行防火墙端口。

---

### 故障 2：504 Gateway Timeout

**现象**：接口请求超过一定时间后返回 504，用户侧表现为"转圈后报错"。

**诊断步骤**：
```
# 1. 检查 Nginx 错误日志
tail -f /var/log/nginx/error.log | grep "timeout"

# 2. 查看 proxy_read_timeout 当前配置
grep proxy_read_timeout /etc/nginx/conf.d/*.conf

# 3. 在后端服务器上检查慢查询/慢接口
# 如果是 Java 应用：jstack 查看线程栈
# 如果是 MySQL：slow_query_log 查看慢 SQL
```

**解决方案**：
- 如果是后端确实慢：优化接口性能（加索引、加缓存、异步化）
- 如果是 Nginx 超时太短：调大 `proxy_read_timeout`（如从 60s 调到 300s）
- 如果是长轮询/长连接接口：考虑用 WebSocket 替代 HTTP 轮询

---

### 故障 3：HTTPS 证书过期或证书链不完整

**现象**：浏览器提示"您的连接不是私密连接"，或 Android 客户端报证书验证失败。

**诊断步骤**：
```
# 1. 检查证书过期时间
openssl x509 -in /etc/nginx/ssl/cert.pem -noout -dates

# 2. 检查证书链是否完整（是否包含了中间证书）
openssl verify -CAfile /etc/ssl/certs/ca-bundle.crt /etc/nginx/ssl/cert.pem

# 3. 用 SSL Labs 在线检测（最全面）
# 访问：https://www.ssllabs.com/ssltest/analyze.html?d=你的域名
```

**解决方案**：
- 证书过期：立即续期（`certbot renew`），必要时先临时换回 HTTP 避免完全不可用
- 证书链不完整：将 `fullchain.pem`（服务器证书 + 中间证书）配置到 `ssl_certificate`，而不是只用 `cert.pem`

---

### 故障 4：Nginx  worker_connections 不够用

**现象**：访问量上来后 Nginx 返回 500，error_log 中出现 `worker_connections are not enough`

**诊断步骤**：
```
# 1. 查看当前 Nginx 并发连接数
curl http://localhost:8080/nginx_status

# 2. 计算理论最大并发
# 理论并发 = worker_processes × worker_connections
# 如果开了反向代理，每个客户端连接对应 2 个连接（客户端→Nginx、Nginx→后端）
# 所以实际并发要除以 2

# 3. 检查系统级文件描述符限制
ulimit -n
cat /proc/sys/fs/file-max
```

**解决方案**：
```nginx
# nginx.conf 中调大
worker_rlimit_nofile 65535;  # 放在最外层（events 块之前）

events {
    worker_connections 10240;  # 调大（默认 1024）
}
```
```bash
# 同时修改系统级限制
# /etc/security/limits.conf 添加：
# * soft nofile 65535
# * hard nofile 65535
```

---

### 故障 5：URL 重写导致重定向循环

**现象**：浏览器提示"重定向次数过多"，ERR_TOO_MANY_REDIRECTS。

**诊断步骤**：
```
# 1. 用 curl -v 查看重定向链
curl -v http://example.com/foo

# 2. 检查 rewrite 规则（常见错误：重写后的 URL 再次匹配原 location）
# 例如：
# location / {
#     rewrite ^(.*)$ /index.php?url=$1 last;  # 错误！last 会重新匹配 location /
# }
```

**解决方案**：改用 `break`（不在重新匹配 location）或调整 `location` 匹配条件，或者改用 `try_files`（性能更好，逻辑更清晰）。

---

## 💼 面试高频题

### 1. Nginx 的 master 和 worker 进程分别做什么？为什么采用多进程模型而不是多线程？

**答案要点**：
- Master 进程：读取配置、管理 worker 进程（启动/停止/重载）、绑定端口
- Worker 进程：实际处理请求，独立进程互不干扰
- 多进程优势：稳定性高（一个 worker 崩溃不影响其他 worker）、无锁设计（避免多线程竞争）、利用多核 CPU

---

### 2. Nginx 反向代理中，如何获取用户的真实 IP？

**答案要点**：
- Nginx 侧：配置 `proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;`
- 应用侧：从 `X-Forwarded-For` 头取第一个 IP（最左边的），注意防伪造（可信代理链中才可信）
- 如果经过多层代理：X-Forwarded-For 格式为 `客户端IP, 代理1IP, 代理2IP`，取第一个
- 更安全的方案：在边缘 Nginx 用 `real_ip_header X-Forwarded-For` + `set_real_ip_from` 设置可信代理段

---

### 3. Nginx 的 location 匹配优先级是怎样的？

**答案要点**：
`=` 精确匹配 > `^~` 前缀匹配 > `~`/`~*` 正则匹配 > 普通前缀匹配 > `/` 通用匹配
关键点：`last` 和 `break` 的区别；正则匹配是按配置文件中的顺序，第一个匹配即停止。

---

### 4. Nginx 如何实现负载均衡？有哪些算法？

**答案要点**：
- 配置 `upstream` 块，里面定义多个 `server`
- 算法：轮询（默认）、加权轮询（weight）、ip_hash（会话保持）、least_conn（最少连接）、hash 一致性哈希
- 健康检查：被动（`max_fails`+`fail_timeout`），主动（需要第三方模块或 Nginx Plus）

---

### 5. Nginx 和 Apache 的核心区别是什么？

**答案要点**：
- Nginx：事件驱动、异步非阻塞、一个 worker 处理多个连接、内存占用低、适合高并发静态资源
- Apache：多进程/多线程、阻塞 I/O、每个连接一个进程/线程、内存占用高、但 .htaccess 灵活
- 实际生产中常组合使用：Nginx 做前端代理，Apache 做后端（需要 .htaccess 的场景）

---

### 6. 如何优化 Nginx 性能应对高并发场景？

**答案要点**：
- `worker_processes auto`、`worker_connections` 调大
- 开启 `sendfile`、`tcp_nopush`、`tcp_nodelay`
- 开启 `gzip` 压缩
- 开启 `proxy_cache` 减少后端请求
- 开启 `keepalive` 减少 TCP 建连
- 系统级：调整 `ulimit -n`、`net.core.somaxconn`、`net.ipv4.tcp_tw_reuse`

---

### 7. HTTPS 配置中，如何兼顾安全性和兼容性？

**答案要点**：
- 协议：`ssl_protocols TLSv1.2 TLSv1.3;`（老浏览器可能需要保留 TLSv1.1）
- 密码套件：优先 ECDHE（完美前向保密），参考 Mozilla SSL Config Generator
- HSTS：开启但首次部署建议先不设 `includeSubDomains`，避免子域名出问题
- OCSP Stapling：开启（`ssl_stapling on;`），减少客户端验证证书状态的延迟

---

### 8. Nginx 的 proxy_cache 和浏览器缓存有什么区别？如何配合？

**答案要点**：
- Nginx proxy_cache：缓存后端响应，减少后端压力，作用在服务端
- 浏览器缓存：通过 `Cache-Control` / `Expires` 头控制，减少客户端请求，作用在客户端
- 配合方式：静态资源设置长 `Cache-Control`（如 `max-age=2592000`），Nginx 层可不缓存或短期缓存；API 接口不缓存或按需缓存

---

## 📈 进阶学习路径

```
Nginx 基础
  ↓
反向代理 + 负载均衡
  ↓
HTTPS 全链路配置
  ↓
性能调优（系统 + Nginx 参数）
  ↓
OpenResty / Lua 扩展开发
  ↓
Nginx 模块开发（C 语言）
  ↓
大规模 Nginx 集群管理（配置中心、自动化变更）
  ↓
Service Mesh（Istio）—— 云原生时代的"高级反向代理"
```

**推荐下一步学习**：
- 如果偏运维方向：深入学习 **Keepalived + Nginx 高可用** 和 **Nginx 配置自动化管理**
- 如果偏开发方向：学习 **OpenResty** 和 **Nginx C 模块开发**
- 如果偏架构方向：学习 **Service Mesh（Envoy/Istio）**，理解现代微服务流量管理

---

[← 返回中文版首页](../README.md)
