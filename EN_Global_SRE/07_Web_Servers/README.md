# 07 · Web Servers & Reverse Proxies

> **Learning Context**: Every request from a user's browser eventually hits a web server or reverse proxy before reaching your application. Whether you're running a simple blog or a global microservices platform, understanding how web servers work — and how to tune them — is non-negotiable for any ops engineer. Nginx alone powers over 30% of all websites, and the patterns you learn here (load balancing, TLS termination, caching, rate limiting) apply universally across HAProxy, Traefik, Caddy, and cloud load balancers. This module takes you from "I can install Nginx" to "I can design and operate production-grade ingress architectures."

---

## 🎯 Learning Objectives

- [ ] Configure Nginx as a high-performance reverse proxy with upstream pooling
- [ ] Implement production-grade TLS (TLS 1.3, HSTS, OCSP stapling, certificate automation)
- [ ] Tune Nginx worker processes, connection handling, and buffer sizes for high concurrency
- [ ] Set up layer 7 load balancing with multiple algorithms (round-robin, least_conn, ip_hash, consistent hashing)
- [ ] Configure advanced rate limiting and DDoS mitigation (limit_req, limit_conn, geo-based rules)
- [ ] Implement multi-tier caching strategies (proxy_cache, fastcgi_cache, micro-caching)
- [ ] Deploy HAProxy for TCP/HTTP load balancing with health checks and stats
- [ ] Set up Traefik as a dynamic, container-native ingress proxy with Let's Encrypt automation
- [ ] Design API Gateway patterns (authentication, request transformation, circuit breaking)
- [ ] Configure WebSocket proxying and gRPC pass-through
- [ ] Implement blue-green and canary deployment patterns at the proxy layer
- [ ] Master access log analysis and performance metrics extraction
- [ ] Harden web server security (headers, WAF integration, request size limits)

---

## 📺 Recommended Video Courses

| Course | Creator | Views/Info | Level |
|--------|----------|------------|-------|
| [Nginx Fundamentals](https://www.udemy.com/course/nginx-fundamentals) | Ray Villalobos (Udemy) | ~45k students | Beginner |
| [Nginx 2024 - Beginner to Advanced](https://www.youtube.com/watch?v=7VAI73roXaY) | TechWorld with Nana | ~1.2M views | Beginner→Intermediate |
| [HAProxy Essentials](https://www.youtube.com/watch?v=gPp8SjF_zXg) | HAProxy Technologies | ~180k views | Intermediate |
| [Traefik Proxy Complete Guide](https://www.youtube.com/watch?v=3eXtKFenDGw) | Traefik Labs | ~95k views | Intermediate |
| [Nginx Performance Tuning](https://www.youtube.com/watch?v=2skyMQJJWuw) | Nginx Inc. (official) | ~320k views | Advanced |
| [API Gateway Pattern in Microservices](https://www.youtube.com/watch?v=Av62xqM6Dfo) | PiggyMetrics / TechTalks | ~450k views | Intermediate |
| [Kong API Gateway Tutorial](https://www.youtube.com/watch?v=iGTZU_8avUc) | Kong Inc. | ~85k views | Intermediate |
| [Understanding Reverse Proxies](https://www.youtube.com/watch?v=QIcwerkGREk) | Hussein Nasser | ~280k views | Beginner |

---

## 📖 Recommended Books

| Book | Author | Rating | Recommendation |
|------|--------|--------|----------------|
| **Nginx HTTP Server (4th Ed.)** | Martin F. J. Smith | ★★★★☆ | The definitive admin guide — I keep this on my desk |
| **Nginx Cookbook** | Derek DeJonghe | ★★★★☆ | Short, recipe-style solutions for real problems |
| **HAProxy 2.4 Reference Guide** | Willy Tarreau et al. | ★★★★☆ | From HAProxy's creator — deep dive into internals |
| **The NGINX Handbook** | Rahul Sharma (free) | ★★★★☆ | Great free starting point, covers modern use cases |
| **Mastering NGINX 2nd Edition** | Dimitri Aivaliotis | ★★★★☆ | Advanced tuning and module development |
| **API Security in Action** | Neil Madden | ★★★★★ | Essential if you're building API gateways |
| **Cloud Native Patterns** | Cornelia Davis | ★★★★☆ | Context for why Traefik/Caddy exist in modern stacks |

---

## 🌐 Online Resources

| Resource | Link | Stars/Info |
|----------|------|------------|
| **Nginx Official Admin Guide** | https://docs.nginx.com/nginx/admin-guide | Official |
| **Nginx Blog (tech deep-dives)** | https://nginx.org/en/blog | Official |
| **HAProxy Documentation** | https://docs.haproxy.org | Official |
| **Traefik Official Docs** | https://doc.traefik.io/traefik | Official |
| **Caddy Documentation** | https://caddyserver.com/docs | Official |
| **Kong API Gateway Docs** | https://docs.konghq.com | Official |
| **awesome-nginx** | https://github.com/freebsd-engine/awesome-nginx | ⭐1.8k |
| **HAProxy Academy** | https://www.haproxy.com/blog | Articles + tutorials |
| **Nginx Config Generator** | https://nginxconfig.io | Visual config tool |
| **Let's Encrypt Docs** | https://letsencrypt.org/docs | Certbot guides |

---

## 📝 Core Knowledge Checklist

### Phase 1: Nginx Fundamentals & Architecture

- [ ] **Nginx architecture**: master process, worker processes, event-driven model, epoll/kqueue
- [ ] **Installation methods**: package manager (apt/yum), compiling from source with custom modules
- [ ] **Configuration file structure**: main context, events block, http block, server blocks, location blocks
- [ ] **Directives inheritance**: understanding how parent/child contexts work
- [ ] **Nginx vs Apache**: event-driven vs prefork MPM, resource usage comparison
- [ ] **Module system**: core modules, optional modules, third-party modules (headers-more, lua-nginx)
- [ ] **Basic server block setup**: listen directive, server_name, root, index
- [ ] **Static content serving**: efficient file serving, MIME types, autoindex
- [ ] **Directory structure best practices**: sites-available, sites-enabled, conf.d pattern
- [ ] **Reload vs restart**: `nginx -s reload` (graceful) vs `systemctl restart nginx`
- [ ] **Configuration testing**: `nginx -t` before every reload — I cannot stress this enough
- [ ] **Log formats**: custom log formats with variables, JSON logging for ELK integration

### Phase 2: Reverse Proxying & Load Balancing

- [ ] **Basic proxy_pass**: forwarding requests to backend application servers
- [ ] **Upstream block definition**: defining backend pools with multiple servers
- [ ] **Load balancing algorithms**: round-robin (default), least_conn, ip_hash, hash (consistent)
- [ ] **Weighted load balancing**: `server backend1 weight=3` for capacity-based distribution
- [ ] **Health checks**: passive health checks (`max_fails`, `fail_timeout`), active health checks (Nginx Plus / open-source workaround)
- [ ] **Connection pooling**: `keepalive` connections to backends, `proxy_http_version 1.1`
- [ ] **Request header manipulation**: `proxy_set_header X-Real-IP $remote_addr`, Host header passthrough
- [ ] **Response header modification**: adding security headers, removing backend server info
- [ ] **Timeout configuration**: `proxy_connect_timeout`, `proxy_send_timeout`, `proxy_read_timeout`
- [ ] **Buffer sizing**: `proxy_buffering`, `proxy_buffer_size`, `proxy_buffers` — critical for performance
- [ ] **Large file handling**: `client_max_body_size`, streaming proxy for file uploads
- [ ] **gRPC proxying**: `grpc_pass` directive, gRPC over HTTP/2 configuration

### Phase 3: TLS/SSL & Security

- [ ] **TLS certificate management**: Let's Encrypt with Certbot, renewal automation via cron
- [ ] **TLS configuration best practices**: TLS 1.2 minimum, TLS 1.3 preferred, cipher suite ordering
- [ ] **OCSP stapling**: reducing TLS handshake latency with `ssl_stapling on`
- [ ] **HSTS implementation**: `Strict-Transport-Security` header, preload list submission
- [ ] **SSL session caching**: `ssl_session_cache shared:SSL:10m`, session ticket configuration
- [ ] **Certificate chain completeness**: avoiding "incomplete chain" warnings
- [ ] **HTTP to HTTPS redirect**: clean 301 redirect patterns
- [ ] **Security headers**: Content-Security-Policy, X-Frame-Options, X-Content-Type-Options
- [ ] **Rate limiting**: `limit_req_zone` + `limit_req` for request rate, `limit_conn_zone` for connection limits
- [ ] **Geo-based access control**: `geo` block for country-based blocking
- [ ] **Request size limits**: `client_max_body_size`, `client_body_buffer_size`
- [ ] **WAF integration**: ModSecurity with Nginx, Cloudflare integration patterns

### Phase 4: Caching & Performance Tuning

- [ ] **Proxy caching**: `proxy_cache_path` definition, cache key configuration, cache validity rules
- [ ] **Cache purging strategies**: manual purge endpoint, cache-busting via URL versioning
- [ ] **Micro-caching**: 1-5 second caching for high-traffic endpoints (dramatic hit rate improvement)
- [ ] **FastCGI caching**: PHP-FPM specific caching with `fastcgi_cache`
- [ ] **Cache bypass conditions**: `$cookie_user`, `$args`, specific paths
- [ ] **Cache status logging**: `$upstream_cache_status` (HIT/MISS/BYPASS/EXPIRED)
- [ ] **Gzip/Brotli compression**: `gzip on`, `brotli on` (requires Nginx built with Brotli)
- [ ] **Worker process tuning**: `worker_processes auto`, `worker_connections 10240`
- [ ] **Keep-alive optimization**: `keepalive_timeout`, `keepalive_requests`
- [ ] **Open file cache**: `open_file_cache` for static file descriptor caching
- [ ] **TCP optimization**: `tcp_nopush on`, `tcp_nodelay on`, `sendfile on`
- [ ] **Rate limiting for DDoS**: combining `limit_req` with `fail2ban`

### Phase 5: HAProxy, Traefik & API Gateway Patterns

- [ ] **HAProxy architecture**: single-process event-driven, frontend/backend configuration model
- [ ] **HAProxy ACLs**: advanced routing based on headers, paths, source IP
- [ ] **HAProxy stats page**: enabling and securing the statistics dashboard
- [ ] **HAProxy SSL offloading**: terminating TLS at HAProxy layer
- [ ] **Traefik service discovery**: automatic backend detection via Docker, Kubernetes, Consul
- [ ] **Traefik middleware chain**: chaining request transformations (redirect, headers, circuit breaker)
- [ ] **Traefik TLS automation**: automatic Let's Encrypt via ACME
- [ ] **API Gateway pattern**: authentication (JWT validation), rate limiting, request/response transformation
- [ ] **Kong API Gateway**: plugin ecosystem, rate limiting plugin, key authentication
- [ ] **Caddy automatic HTTPS**: zero-config TLS with `tls on` and On-Demand TLS for wildcard
- [ ] **Blue-green deployment**: using Nginx `split_clients` or HAProxy `weight` for traffic shifting
- [ ] **Canary release pattern**: header-based or percentage-based routing to canary backends

---

## 💻 Hands-on Commands & Configuration Examples

### 1. Production-Ready Nginx Reverse Proxy (`/etc/nginx/sites-available/app.conf`)

```nginx
# Define upstream backend pool with health check settings
upstream app_backend {
    least_conn;                       # Send to backend with fewest active connections
    server 10.0.1.10:8080 max_fails=3 fail_timeout=30s;
    server 10.0.1.11:8080 max_fails=3 fail_timeout=30s;
    server 10.0.1.12:8080 max_fails=3 fail_timeout=30s backup;  # Backup only used when others fail
}

server {
    listen 443 ssl http2;
    server_name app.example.com;

    # TLS configuration — use sslparams file for maintainability
    ssl_certificate     /etc/letsencrypt/live/app.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app.example.com/privkey.pem;
    include             /etc/nginx/sslparams.conf;  # cipher suites, protocols

    # Security headers — every production site needs these
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    add_header Content-Security-Policy "default-src 'self'" always;

    # Rate limiting — 10 req/s with burst of 20
    limit_req_zone $binary_remote_addr zone=app_limit:10m rate=10r/s;
    limit_req zone=app_limit burst=20 nodelay;

    # Reverse proxy to backend
    location / {
        proxy_pass http://app_backend;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 5s;
        proxy_read_timeout 30s;
        proxy_buffering on;
        proxy_buffer_size 16k;
        proxy_buffers 16 16k;
    }

    # Health check endpoint — no rate limiting, no caching
    location /health {
        access_log off;
        return 200 "OK\n";
        add_header Content-Type text/plain;
    }
}
```

### 2. Nginx Performance Tuning (`/etc/nginx/nginx.conf` core settings)

```nginx
user nginx;
worker_processes auto;              # Match to CPU core count, 'auto' does this
worker_cpu_affinity auto;           # Bind workers to specific CPUs for cache warmth
worker_rlimit_nofile 65535;        # Match system ulimit

events {
    worker_connections 10240;       # Max concurrent connections per worker
    use epoll;                      # Linux optimal event method
    multi_accept on;                # Accept all new connections at once
}

http {
    # Basic performance
    sendfile on;                    # Zero-copy file serving
    tcp_nopush on;                  # Optimize packet sending with sendfile
    tcp_nodelay on;                 # Disable Nagle for interactive apps
    keepalive_timeout 65;           # Keep connections open for reuse
    keepalive_requests 1000;        # Max requests per keepalive connection

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # Open file cache — cache file descriptors and metadata
    open_file_cache max=10000 inactive=30s;
    open_file_cache_valid 60s;
    open_file_cache_min_uses 2;
    open_file_cache_errors on;

    # Rate limiting zones
    limit_req_zone $binary_remote_addr zone=global:10m rate=100r/s;
    limit_conn_zone $binary_remote_addr zone=addr:10m;

    # Include site configs
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

### 3. Nginx Caching Configuration

```nginx
# Define cache zone in http block
proxy_cache_path /var/cache/nginx/app
                 levels=1:2
                 keys_zone=app_cache:100m
                 max_size=10g
                 inactive=60m
                 use_temp_path=off;  # Use same filesystem for atomic file moves

server {
    location /api/ {
        proxy_pass http://backend;
        proxy_cache app_cache;
        proxy_cache_key "$scheme$request_method$host$request_uri$is_args$args";
        proxy_cache_valid 200 302 10m;
        proxy_cache_valid 404 1m;
        proxy_cache_valid any 5m;

        # Serve stale content if backend is down (huge for reliability)
        proxy_cache_use_stale error timeout http_502 http_503 http_504;

        # Add cache status header for debugging
        add_header X-Cache-Status $upstream_cache_status;
    }

    # Micro-caching for homepage — 5 second cache, dramatic hit rate improvement
    location = / {
        proxy_pass http://backend;
        proxy_cache app_cache;
        proxy_cache_valid 200 5s;
        proxy_cache_use_stale updating;  # Serve stale while refreshing
    }
}
```

### 4. HAProxy Configuration (`/etc/haproxy/haproxy.cfg`)

```haproxy
global
    log /dev/log local0
    log /dev/log local1 notice
    maxconn 4096
    daemon

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000ms
    timeout client  50000ms
    timeout server  50000ms

# Stats page — access at http://lb:8404/stats
frontend stats
    bind *:8404
    stats enable
    stats uri /stats
    stats auth admin:secure_password_here

frontend http_front
    bind *:80
    bind *:443 ssl crt /etc/haproxy/certs/  # TLS termination
    redirect scheme https if !{ ssl_fc }     # Force HTTPS

    # ACL for routing
    acl is_api  path_beg /api
    acl is_static path_end .jpg .css .js .png .gif

    use_backend static_be if is_static
    use_backend api_be if is_api
    default_backend web_be

backend web_be
    balance roundrobin
    option httpchk GET /health HTTP/1.1\r\nHost:\ localhost
    server web1 10.0.1.10:8080 check weight 50
    server web2 10.0.1.11:8080 check weight 50

backend api_be
    balance leastconn
    option httpchk GET /api/health
    server api1 10.0.2.10:3000 check
    server api2 10.0.2.11:3000 check

backend static_be
    balance roundrobin
    server static1 10.0.3.10:80 check
```

### 5. Traefik 3.x Dynamic Configuration (`traefik.yml`)

```yaml
# Static configuration
entryPoints:
  web:
    address: ":80"
    http:
      redirections:
        entryPoint:
          to: websecure
          scheme: https
  websecure:
    address: ":443"

certificatesResolvers:
  letsencrypt:
    acme:
      email: admin@example.com
      storage: /etc/traefik/acme.json
      httpChallenge:
        entryPoint: web

# Enable Dashboard
api:
  dashboard: true
  insecure: false   # Set to true only for local dev

# Docker provider — auto-detect services
providers:
  docker:
    endpoint: "unix:///var/run/docker.sock"
    exposedByDefault: false
    network: web

# Observability
metrics:
  prometheus:
    addEntryPointsLabels: true
    addServicesLabels: true

accessLog:
  filePath: "/var/log/traefik/access.log"
  format: json
```

### 6. Traefik Docker Label-Based Routing

```yaml
# docker-compose.yml — Traefik auto-configures from labels
version: '3.8'
services:
  traefik:
    image: traefik:v3.0
    command:
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./traefik.yml:/etc/traefik/traefik.yml

  app:
    image: myapp:latest
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.app.rule=Host(`app.example.com`)"
      - "traefik.http.routers.app.entrypoints=websecure"
      - "traefik.http.routers.app.tls.certresolver=letsencrypt"
      - "traefik.http.services.app.loadbalancer.server.port=8080"
      # Rate limiting middleware
      - "traefik.http.middlewares.app-ratelimit.ratelimit.average=100"
      - "traefik.http.middlewares.app-ratelimit.ratelimit.burst=50"
```

### 7. Nginx WebSocket Proxy

```nginx
location /ws/ {
    proxy_pass http://websocket_backend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;      # Critical: pass through upgrade header
    proxy_set_header Connection "upgrade";        # Critical: mark as upgrade request
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_read_timeout 86400;                     # Long timeout for persistent connections
    proxy_send_timeout 86400;
}
```

### 8. Nginx gRPC Proxy

```nginx
server {
    listen 443 ssl http2;   # gRPC requires HTTP/2
    server_name grpc.example.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        grpc_pass grpc://grpc_backend;   # or grpcs:// for TLS backend
    }

    # Route specific gRPC services
    location /com.example.v1.ApiService/ {
        grpc_pass grpc://grpc_backend;
    }
}
```

### 9. Canary Release with Nginx

```nginx
# Weighted traffic splitting using split_clients
split_clients "${remote_addr}${msec}" $variant {
    10%     canary;    # 10% of traffic goes to canary
    *       stable;    # 90% goes to stable
}

server {
    location / {
        if ($variant = "canary") {
            proxy_pass http://app_canary;
        }
        proxy_pass http://app_stable;
    }
}

# Alternative: header-based canary for internal testing
map $http_x_canary $backend {
    default       http://app_stable;
    "true"        http://app_canary;
    "internal"    http://app_canary;
}
```

### 10. Caddyfile — Modern Auto-HTTPS

```caddyfile
# Caddy automatically obtains and renews TLS certificates
app.example.com {

    # Reverse proxy with load balancing
    reverse_proxy app1:8080 app2:8080 app3:8080 {
        lb_policy least_conn
        health_uri /health
        fail_duration 10s
    }

    # Compression
    encode gzip zstd

    # Security headers
    header {
        Strict-Transport-Security "max-age=31536000"
        X-Content-Type-Options "nosniff"
        X-Frame-Options "DENY"
    }

    # Rate limiting (Caddy 2.8+)
    rate_limit {
        zone app_rate {
            key {remote_host}
            events 100
            window 1m
        }
    }
}

# Static file server with directory browsing
static.example.com {
    root * /var/www/static
    file_server browse
}
```

### 11. Log Format for ELK Integration

```nginx
# Define JSON log format for easy parsing by Logstash/Elasticsearch
log_format json_log escape=json
    '{'
    '"timestamp":"$time_iso8601",'
    '"host":"$host",'
    '"remote_addr":"$remote_addr",'
    '"x_forwarded_for":"$proxy_add_x_forwarded_for",'
    '"method":"$request_method",'
    '"uri":"$request_uri",'
    '"status":$status,'
    '"request_time":$request_time,'
    '"body_bytes_sent":$body_bytes_sent,'
    '"http_referrer":"$http_referer",'
    '"user_agent":"$http_user_agent",'
    '"upstream_addr":"$upstream_addr",'
    '"upstream_response_time":$upstream_response_time,'
    '"cache_status":"$upstream_cache_status"'
    '}';

access_log /var/log/nginx/access.log json_log;
```

### 12. Nginx SSL/TLS Hardening (`sslparams.conf`)

```nginx
# Protocols — disable old insecure versions
ssl_protocols TLSv1.2 TLSv1.3;

# Cipher suites — modern, secure ordering
ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384';
ssl_prefer_server_ciphers off;  # Prefer client ciphers for TLS1.2

# Optimizations
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;        # Disable for perfect forward secrecy

# OCSP stapling — reduces TLS handshake time for client
ssl_stapling on;
ssl_stapling_verify on;
ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;

# DNS for OCSP
resolver 8.8.8.8 1.1.1.1 valid=300s;
resolver_timeout 5s;
```

---

## 🧪 Hands-on Projects

### Project 1: Build a Production Nginx Reverse Proxy with Caching & TLS

**Goal**: Deploy Nginx as a reverse proxy for a multi-tier application with caching, rate limiting, and TLS.

**Step-by-step**:

1. Launch 3 backend app servers (can be simple Python Flask or Node.js apps that return the server hostname)
2. Install Nginx on a separate LB server; configure upstream with all 3 backends
3. Set up `least_conn` load balancing; verify with `curl` that requests distribute evenly
4. Configure Nginx caching; test with `curl -I` and check `X-Cache-Status` header
5. Set up Let's Encrypt with Certbot; configure auto-renewal via cron
6. Add rate limiting (10 req/s) and verify with `ab` or `wrk`
7. Configure JSON access logging; ship logs to a local ELK stack or Loki
8. Simulate a backend failure; verify health checks kick in and traffic routes to healthy backends
9. Benchmark with `wrk` before and after caching — document the improvement
10. Write a `nginx.conf` hardening checklist for your team

**Verification**: All 3 backends receive traffic; TLS A+ rating on SSL Labs; cached responses return in <5ms.

---

### Project 2: Multi-Proxy Comparison Lab (Nginx vs HAProxy vs Traefik)

**Goal**: Understand the strengths of each proxy by deploying all three in parallel.

**Step-by-step**:

1. Deploy the same backend application behind all three proxies
2. Configure Nginx: reverse proxy + TLS + rate limiting
3. Configure HAProxy: same backends, enable stats page, configure ACL-based routing
4. Configure Traefik: use Docker provider, auto-TLS via Let's Encrypt
5. Use `wrk` to benchmark all three under 1000 concurrent connections
6. Compare: connection handling, TLS handshake time, memory usage (`ps_mem`), config complexity
7. Document: which proxy you'd choose for which scenario and why
8. Bonus: configure circuit breaker pattern with HAProxy `observe` layer7

**Verification**: Performance comparison table; clear recommendation document for each use case.

---

### Project 3: API Gateway Pattern with Kong

**Goal**: Implement authentication, rate limiting, and request transformation at the gateway layer.

**Step-by-step**:

1. Deploy Kong API Gateway (Docker-based is fastest)
2. Configure a service and route in Kong pointing to your backend
3. Enable the `key-auth` plugin — require API keys for all requests
4. Enable the `rate-limiting` plugin — 100 req/min per consumer
5. Enable the `request-transformer` plugin — add custom headers to all upstream requests
6. Enable the `response-transformer` plugin — remove server version headers
7. Set up the `prometheus` plugin for metrics
8. Create multiple consumers; assign different rate limits to each
9. Test with `curl` using API keys; verify rate limit headers in response
10. Document your API gateway architecture with a diagram

**Verification**: Requests without API key are rejected (401); rate limits enforced per consumer; metrics visible in Prometheus.

---

## 🔧 Common Troubleshooting

### Scenario 1: "502 Bad Gateway" on Nginx Reverse Proxy

**Symptoms**: Nginx returns 502 for all requests; upstream apps appear running.

**Diagnosis**:
```bash
# Check if upstream is actually reachable from Nginx server
curl -v http://10.0.1.10:8080/health

# Check Nginx error log — this is your best friend
tail -f /var/log/nginx/error.log
# Common errors: "connect() failed (111: Connection refused)"
#                "upstream timed out (110: Connection timed out)"

# Verify Nginx can resolve upstream hostname (if using hostnames)
nslookup backend.internal
```

**Solutions**:
- If connection refused: check upstream app is listening on the correct port (`ss -tlnp | grep 8080`)
- If timeout: check firewall rules (`iptables -L` or `ufw status`), security groups
- If DNS issue: use IP addresses in upstream block, or configure `resolver` in Nginx
- If upstream is slow: increase `proxy_read_timeout` and `proxy_connect_timeout`

---

### Scenario 2: Nginx Worker Connections Exhausted Under Load

**Symptoms**: "worker_connections are not enough" in error log; new connections rejected.

**Diagnosis**:
```bash
# Check current connections
ss -s
# Check Nginx status
nginx -V 2>&1 | grep -o 'worker_connections [0-9]*'

# Check system limits
ulimit -n
cat /proc/sys/fs/file-max
```

**Solutions**:
```nginx
# In nginx.conf:
worker_processes auto;
worker_rlimit_nofile 65535;  # Must be >= worker_connections * worker_processes * 2

events {
    worker_connections 10240;  # Increase from default 768
}
```
Also increase system limits:
```bash
# /etc/security/limits.conf
nginx soft nofile 65535
nginx hard nofile 65535
```

---

### Scenario 3: TLS Handshake Timeout / Certificate Errors

**Symptoms**: Browser shows "ERR_CERT_DATE_INVALID" or "SSL protocol error".

**Diagnosis**:
```bash
# Check certificate expiry
openssl x509 -in /etc/letsencrypt/live/example.com/cert.pem -text -noout | grep "Not After"

# Test TLS handshake
openssl s_client -connect example.com:443 -servername example.com

# Check certificate chain completeness
openssl verify -CAfile /etc/letsencrypt/live/example.com/chain.pem /etc/letsencrypt/live/example.com/cert.pem
```

**Solutions**:
- Expired cert: run `certbot renew --force-renewal`
- Incomplete chain: ensure `ssl_certificate` points to `fullchain.pem`, not `cert.pem`
- Wrong SNI: ensure `server_name` matches the requested hostname exactly
- Old protocol: ensure `ssl_protocols TLSv1.2 TLSv1.3` is set

---

### Scenario 4: High Latency on Cached Content

**Symptoms**: Cached responses taking 500ms+ when they should be <10ms.

**Diagnosis**:
```bash
# Check cache status
curl -I https://app.example.com/api/data | grep X-Cache-Status

# Check cache directory permissions and disk I/O
ls -la /var/cache/nginx/
iostat -x 1  # Check disk utilization

# Verify cache key isn't too variable (each user = different cache entry)
# Check $upstream_cache_status in logs
```

**Solutions**:
- Ensure `proxy_cache_key` uses stable identifiers (not `$cookie_sessionid`)
- Set `use_temp_path=off` in `proxy_cache_path` to avoid disk copies
- Ensure `/var/cache/nginx` is on fast SSD
- Check `inactive=` parameter in cache path — cached items evicted if not accessed within this time
- Verify `proxy_cache_valid` covers your response status codes

---

### Scenario 5: HAProxy Backend Flapping (Up/Down/Up/Down)

**Symptoms**: Backends constantly marked as DOWN then healthy again in HAProxy stats.

**Diagnosis**:
```bash
# Check HAProxy health check configuration
grep -A5 "backend" /etc/haproxy/haproxy.cfg

# Manually run the health check
curl -v http://backend:8080/health

# Check HAProxy logs
tail -f /var/log/haproxy.log
```

**Solutions**:
- Health check interval too short: increase `inter` (e.g., `check inter 3000`)
- Health check endpoint too slow: optimize `/health` to be a lightweight check
- `fall` too low: increase to 3+ so brief blips don't mark backend down
- Backend slow to start: increase `rise` count to require multiple successful checks

---

## 💼 Interview Questions

### Q1: Explain the Nginx event-driven architecture and why it's more efficient than Apache's prefork MPM.

**Answer**: Nginx uses a non-blocking, event-driven architecture where a small number of worker processes (typically matching CPU cores) handle many connections concurrently using `epoll` (Linux) or `kqueue` (BSD). Each worker can handle thousands of connections because it never blocks on I/O — it asynchronously switches between connections when events occur. Apache prefork spawns a process per connection, which consumes significant memory (2-10MB per process) and context-switching overhead. Nginx's approach means serving 10,000 concurrent connections with 10-20MB total memory, while Apache would need 10,000 processes and gigabytes of RAM.

---

### Q2: How does Nginx handle TLS termination, and what's the performance impact?

**Answer**: Nginx terminates TLS at the proxy layer — the client establishes a TLS connection to Nginx, which decrypts the request and forwards it (usually unencrypted) to the backend. This offloads CPU-intensive TLS operations from application servers. Performance impact: TLS handshake adds ~1-2 RTT before data transfer; enabling HTTP/2, session resumption (`ssl_session_cache`), and OCSP stapling significantly reduces this. I've seen TLS add 50-100ms to first request, but with proper tuning (session cache, TLS 1.3 zero-RTT) this drops to near-zero for returning clients.

---

### Q3: What's the difference between `ip_hash` and `least_conn` load balancing?

**Answer**: `ip_hash` uses a hash of the client's IP address to consistently route to the same backend — useful for session persistence without a shared session store, but can cause uneven distribution if clients are behind NAT (many users appear as one IP). `least_conn` routes to the backend with the fewest active connections — better for varying request durations and more even distribution. I recommend `least_conn` for most APIs; `ip_hash` only if you have a specific session affinity requirement and can't use a shared session store or sticky cookies.

---

### Q4: How would you troubleshoot high latency in a reverse proxy setup?

**Answer**: Step 1: Check `$upstream_response_time` in Nginx logs — this tells you if the backend is slow vs. Nginx itself. Step 2: Check `$request_time` vs. `$upstream_response_time` — if they differ significantly, Nginx is the bottleneck (likely buffering or slow client). Step 3: Use `wrk` or `ab` to benchmark the backend directly (bypassing proxy) to isolate the issue. Step 4: Check Nginx `error.log` for any worker limit warnings. Step 5: Profile with `strace -c -p <nginx_worker_pid>` to see where time is spent. Step 6: Check if caching is working (`X-Cache-Status` header). The key insight: always measure each layer independently rather than guessing.

---

### Q5: Explain the Nginx `proxy_cache` mechanism and when you would (and wouldn't) use it.

**Answer**: `proxy_cache` stores backend responses on disk and serves them directly on subsequent requests without hitting the backend. Use it for: content that changes infrequently (static assets, product catalog), expensive API responses (aggregation endpoints), and to reduce backend load during traffic spikes. I particularly like "micro-caching" (5-30 second cache) for high-traffic homepages — it dramatically reduces backend load with minimal staleness. Don't use it for: personalized content (unless cache key includes user ID carefully), real-time data (stock prices, chat), or authenticated endpoints where stale data is unacceptable. Always add `$upstream_cache_status` to response headers during development — it's invaluable for debugging.

---

### Q6: How does HAProxy differ from Nginx for load balancing, and when would you choose one over the other?

**Answer**: HAProxy is purpose-built for load balancing — it has richer load-balancing algorithms (including consistent hashing), more sophisticated health checks (active HTTP checks, agent checks), better connection multiplexing, and a real-time stats API. Nginx is a web server that also does reverse proxying — it's more flexible for serving static content and has a larger module ecosystem. I choose HAProxy when: I need L4 (TCP/UDP) load balancing, complex routing rules with ACLs, or highest possible performance (HAProxy benchmarks slightly faster for pure L7 proxying). I choose Nginx when: I also need to serve static content, want built-in WAF/modules, or prefer a single tool for web server + proxy. In practice, many teams use both: HAProxy at the edge, Nginx as the application-layer reverse proxy.

---

### Q7: What are the key considerations for TLS in a microservices architecture?

**Answer**: In microservices, you have three main TLS strategies: (1) **TLS at ingress only** — simplest, encrypt only at edge, internal traffic plain HTTP. Easy but doesn't meet compliance requirements (PCI-DSS, etc.) that mandate encryption in transit. (2) **TLS everywhere (mTLS)** — every service-to-service call is encrypted. Most secure but adds latency and certificate management complexity. Istio/Linkerd can automate this. (3) **TLS at ingress + internal CA** — ingress terminates TLS; internal services use certificates from a private CA. I recommend starting with option 1 for speed, then moving to option 3 with a tool like Vault for certificate management as you scale. mTLS everywhere is ideal but has a significant operational cost — adopt it when you have the platform team to support it.

---

### Q8: How do you implement DDoS protection at the web server layer?

**Answer**: Layer 1: **Rate limiting** — `limit_req` in Nginx, `stick-table` in HAProxy to limit requests per IP. Layer 2: **Connection limiting** — `limit_conn` to prevent a single IP from consuming all worker connections. Layer 3: **Geo-blocking** — block countries you don't do business with using Nginx `geo` block or HAProxy ACLs. Layer 4: **Request size limits** — `client_max_body_size` to prevent buffer overflow attacks. Layer 5: **Fail2ban integration** — parse Nginx logs and automatically block IPs triggering too many 429/502 errors. Layer 6: **Upstream** — use Cloudflare or similar CDN to absorb volumetric attacks before they reach your server. No single layer is sufficient — I stack them and monitor for false positives (legitimate users blocked) constantly.

---

## 📈 Advanced Learning Path

```
Junior Ops Engineer
│
├── Master Nginx reverse proxy + TLS (this module)
│
▼
Senior Ops Engineer
│
├── HAProxy advanced features (stick tables, ACLs, runtime API)
├── Traefik in Kubernetes (Ingress Controller deep dive)
├── Envoy Proxy (modern service mesh data plane)
├── API Gateway patterns (Kong, Apigee, AWS API Gateway)
│
▼
Platform / SRE
│
├── Service mesh (Istio, Linkerd) — mTLS, traffic management, observability
├── CDN architecture (CloudFront, Cloudflare, Fastly) — edge caching strategies
├── Zero-trust networking — beyond perimeter-based security
├── Writing custom Nginx modules (C/OpenResty/Lua)
│
▼
Architect
│
├── Multi-region ingress design
├── Global load balancing (GSLB, Anycast)
├── Next-gen protocols (QUIC/HTTP3)
└── Contributing to Nginx/HAProxy open-source
```

**Next steps after this module**:
1. Deploy Nginx as an Ingress Controller in Kubernetes — understand how it differs from bare-metal Nginx
2. Learn Envoy Proxy — the data plane behind Istio, increasingly the standard for service mesh
3. Study TCP/IP load balancing with HAProxy — understand the L4 vs L7 tradeoffs
4. Read the Nginx architecture deep dive on their blog — understanding the internals helps with tuning
5. Set up a CDN (CloudFront or Cloudflare) in front of your Nginx — understand edge vs. origin

---

[← Back to English Home](../README.md)
