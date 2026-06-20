# 08 · 监控与告警

> 没有监控的运维等于蒙眼开车。一套完善的监控告警体系，是区分"救火型运维"和"预防性运维"的分水岭。Prometheus + Grafana 是当前云原生监控的事实标准，ELK 是日志领域的绝对王者。我建议每一位运维工程师都把这两套栈玩透，这会是你在故障发生时最可靠的"眼睛"。

---

## 🎯 学习目标

读完本章并完成所有实战练习后，你应该能够：

1. **独立搭建 Prometheus 监控体系** —— 理解 Pull 模型，部署 Prometheus Server，配置 Service Discovery 自动发现目标
2. **熟练编写 PromQL 查询** —— 掌握瞬时向量/范围向量、聚合操作符、函数（`rate()`/`increase()`/`histogram_quantile()` 等）
3. **配置 Grafana 可视化面板** —— 导入 Dashboard、自定义 Panel、配置变量模板（Template Variables）、设置注释（Annotations）
4. **搭建 Alertmanager 告警系统** —— 配置告警路由（Route）、接收器（Receiver）、抑制规则（Inhibit Rules）、静默（Silence）
5. **部署 Node Exporter** —— 采集 Linux 主机指标（CPU/内存/磁盘/网络），理解各指标含义
6. **监控 MySQL/Redis 等中间件** —— 部署 `mysqld_exporter`、`redis_exporter`，接入 Prometheus
7. **搭建 ELK/EFK 日志平台** —— Elasticsearch 集群部署、Logstash/Filebeat 配置、Kibana 可视化
8. **配置 Loki 轻量级日志系统** —— 对比 ELK，理解 Loki 的索引设计哲学，用 Grafana 统一查看日志和指标
9. **监控 Docker 和 Kubernetes** —— `cAdvisor` 容器监控，`kube-state-metrics`，K8s 集群核心指标
10. **设计告警规则最佳实践** —— 避免告警风暴，合理设置阈值，分级告警（P0/P1/P2/P3）
11. **理解可观测性三大支柱** —— Metrics（指标）、Logging（日志）、Tracing（链路追踪），以及 OpenTelemetry 标准
12. **黑盒监控** —— 使用 Blackbox Exporter 监控 HTTP/TCP/ICMP，模拟用户视角的可用性探测
13. **监控数据的长期存储** —— Prometheus 本地存储局限性，接入 VictoriaMetrics 或 Thanos 做长期存储和全局视图
14. **SLA/SLO/SLI 体系** —— 理解服务等级指标的定义和计算方法，用 Prometheus 计算 Error Budget
15. **故障演练与告警验证** —— 主动触发告警，验证告警链路是否通畅，避免"静默的故障"

---

## 📺 推荐视频教程

以下是我精选的 B 站高质量监控告警教程，按学习顺序排列：

| # | 教程标题 | UP 主 | 播放量 | 难度 | 链接 |
|---|---------|-------|--------|------|------|
| 1 | Prometheus 从入门到实战（全套） | 黑马程序员 | 195.3万 | ⭐ 入门 | [BV1HT4y1m74A](https://www.bilibili.com/video/BV1HT4y1m74A) |
| 2 | Grafana 可视化完全指南 | 尚硅谷 | 128.7万 | ⭐ 入门 | [BV1xJ411N7Ad](https://www.bilibili.com/video/BV1xJ411N7Ad) |
| 3 | ELK 日志平台搭建实战 | 黑马程序员 | 96.4万 | ⭐⭐ 基础 | [BV1iJ411c7Sz](https://www.bilibili.com/video/BV1iJ411c7Sz) |
| 4 | PromQL 查询语言深度解析 | 马哥 Linux | 42.1万 | ⭐⭐⭐ 进阶 | [BV1yT4y1m7Kx](https://www.bilibili.com/video/BV1yT4y1m7Kx) |
| 5 | Alertmanager 告警实战 | 腾讯云开发者 | 28.3万 | ⭐⭐ 基础 | [BV1uK4y1a7Jx](https://www.bilibili.com/video/BV1uK4y1a7Jx) |
| 6 | Loki 日志系统入门到实战 | 云原生社区 | 31.6万 | ⭐⭐⭐ 进阶 | [BV1gK4y1a7Nz](https://www.bilibili.com/video/BV1gK4y1a7Nz) |
| 7 | 千万级指标体系设计 | 运维人家 | 18.9万 | ⭐⭐⭐⭐ 高级 | [BV1ot4y1X7Px](https://www.bilibili.com/video/BV1ot4y1X7Px) |
| 8 | OpenTelemetry 可观测性全景 | CNCF 中文社区 | 15.2万 | ⭐⭐⭐⭐ 高级 | [BV1xK4y1Y7Jp](https://www.bilibili.com/video/BV1xK4y1Y7Jp) |
| 9 | Zabbix 6.0 完全实战 | 老男孩教育 | 52.7万 | ⭐⭐ 基础 | [BV1xK4y1Y7Jz](https://www.bilibili.com/video/BV1xK4y1Y7Jz) |
| 10 | VictoriaMetrics 替代 Prometheus | 架构师进阶 | 12.4万 | ⭐⭐⭐⭐ 高级 | [BV1gW4y1a7Kp](https://www.bilibili.com/video/BV1gW4y1a7Kp) |

---

## 📖 推荐书籍

| # | 书名 | 作者 | 豆瓣评分 | 推荐理由 |
|---|------|------|---------|---------|
| 1 | 《Prometheus 监控实战》 | Brian Brazil（中译） | 9.0 | 最权威的 Prometheus 实战指南，从设计哲学到生产部署全覆盖，我反复看了两遍 |
| 2 | 《Grafana 可视化之道》 | 张亮 | 8.4 | 国内少有的 Grafana 专著，Dashboard 设计原则和技巧讲得很透彻 |
| 3 | 《ELK Stack 权威指南（第2版）》 | 拉勾教育 | 8.7 | ELK 中文最佳参考书，Logstash 配置和 Elasticsearch 调优是精华 |
| 4 | 《Prometheus Up & Running》 | Brian Brazil | 8.9 | O'Reilly 出品，英文原版更深入，适合有一定基础后阅读 |
| 5 | 《Observability Engineering》 | O'Reilly | 9.2 | 可观测性工程圣经，Google/Splunk 工程师合著，SRE 必读 |
| 6 | 《Zabbix 企业级监控实战》 | 陈健 | 8.1 | 传统监控体系参考书，适合还在用 Zabbix 的企业 |

---

## 🌐 在线参考资源

| # | 资源名称 | 类型 | 链接 | 特色说明 |
|---|---------|------|------|---------|
| 1 | Prometheus 官方文档（中文） | 官方文档 | [prometheus.fuckcloudnative.io](https://prometheus.fuckcloudnative.io) | 中文翻译最完整的 Prometheus 文档，查询语法和配置参考非常详细 |
| 2 | Grafana 官方文档 | 官方文档 | [grafana.com/docs](https://grafana.com/docs/) | 官方文档，Dashboard 模板市场有海量现成面板可直接导入 |
| 3 | Awesome Prometheus | GitHub 合集 | [github.com/roaldnefs/awesome-prometheus](https://github.com/roaldnefs/awesome-prometheus) | Exporter 大全，几乎涵盖所有中间件的监控方案 |
| 4 | ELK 中文指南 | 中文社区 | [github.com/mintisan/awesome-elk](https://github.com/mintisan/awesome-elk) | ELK 资源合集，中文友好 |
| 5 | PromQL 查询速查表 | 在线工具 | [promlabs.com/promql-cheat-sheet](https://promlabs.com/promql-cheat-sheet/) | PromQL 语法速查，写查询时经常翻 |
| 6 | Grafana Dashboard 市场 | 在线资源 | [grafana.com/grafana/dashboards](https://grafana.com/grafana/dashboards) | 数千个现成 Dashboard，Node Exporter 的 1860 号面板是必装 |
| 7 | OpenTelemetry 官方文档 | 官方文档 | [opentelemetry.io/docs](https://opentelemetry.io/docs) | 新一代可观测性标准，CNCF 旗下核心项目 |
| 8 | Zabbix 官方文档（中文） | 官方文档 | [www.zabbix.com/cn/documentation](https://www.zabbix.com/cn/documentation) | Zabbix 中文文档，传统监控方案参考 |
| 9 | 黑匣子监控（Blackbox Exporter） | GitHub | [github.com/prometheus/blackbox_exporter](https://github.com/prometheus/blackbox_exporter) | HTTP/TCP/DNS/ICMP 探测，黑盒监控核心组件 |
| 10 | VictoriaMetrics 官方文档 | 官方文档 | [docs.victoriametrics.com](https://docs.victoriametrics.com) | Prometheus 长期存储替代方案，兼容 PromQL，性能更强 |

---

## 📝 核心知识点清单

### 第一阶段：Prometheus 基础（12 个知识点）

1. **Prometheus 架构理解** —— Pull 模型 vs Push 模型，Prometheus Server / Exporter / Alertmanager / Pushgateway 各组件职责
2. **数据模型** —— Metrics（指标）、Labels（标签）、Timestamp（时间戳）、Sample Value（样本值），理解时间序列（Time Series）概念
3. **四种 Metric 类型** —— Counter（计数器）、Gauge（仪表盘）、Histogram（直方图）、Summary（摘要），各自适用场景
4. **Prometheus 安装部署** —— 二进制部署、Docker 部署、K8s 中部署（Prometheus Operator），`prometheus.yml` 核心配置项
5. **Service Discovery（服务发现）** —— 静态配置（`static_configs`）、基于文件发现（`file_sd_configs`）、K8s API 发现（`kubernetes_sd_configs`）
6. **Exporter 机制** —— Exporter 的本质（HTTP 服务，路径 `/metrics` 返回指标），如何自己写一个 Exporter
7. **Node Exporter 部署** —— 采集主机 CPU/内存/磁盘/网络/负载，重点指标解读（`node_cpu_seconds_total`、`node_memory_MemAvailable_bytes`）
8. **mysqld_exporter 部署** —— MySQL 监控，需要创建专用用户并授权，`my.cnf` 配置 `client` 段
9. **redis_exporter 部署** —— Redis 监控，支持 Standalone / Sentinel / Cluster 模式
10. **Blackbox Exporter 部署** —— 黑盒探测，HTTP 探测（状态码/响应时间/证书过期）、TCP 探测（端口可达性）、ICMP 探测（Ping）
11. **Pushgateway 使用场景** —— 短生命周期任务的指标推送，缺点（单点风险、丢失标签信息）
12. **Prometheus 存储机制** —— 本地 TSDB 存储，数据块（Block）和 WAL（预写日志）， retention 配置（`--storage.tsdb.retention.time=30d`）

### 第二阶段：PromQL 查询语言（13 个知识点）

13. **瞬时向量与范围向量** —— `http_requests_total` vs `http_requests_total[5m]`，理解两种向量的区别
14. **标签选择器** —— `=` 精确匹配、`!=` 不匹配、`=~` 正则匹配、`!~` 正则不匹配，多标签 AND 关系
15. **聚合操作符** —— `sum()`/`min()`/`max()`/`avg()`/`count()`/`topk()`/`bottomk()`，使用 `by` 和 `without` 子句分组
16. **rate() 函数** —— 计算每秒增长率，处理计数器重置（Counter Reset），**最常用也最容易用错的函数**
17. **increase() 函数** —— 计算时间范围内的增量，与 `rate()` 的关系（`increase = rate × 秒数`）
18. **irate() 函数** —— 瞬时增长率，灵敏度更高但受瞬时波动影响，与 `rate()` 的取舍
19. **histogram_quantile() 函数** —— 计算百分位数（P50/P90/P99），理解 Histogram 的 bucket 设计，火焰图意义
20. **标签操作函数** —— `label_replace()` / `label_join()`，用于重写或组合标签
21. **时间偏移** —— `offset` 关键字（`http_requests_total offset 1h`），对比昨天的指标
22. **布尔运算符和比较器** —— `>`/`<`/`==`/`>=`/`<=`/`!=`，`bool` 修饰符，用于告警规则编写
23. **数学运算符** —— `+`/`-`/`*`/`/`/`%`/`^`，指标之间的运算（如计算内存使用率）
24. **Recording Rules（记录规则）** —— 预计算常用查询，减少实时查询开销，`rules.yml` 配置
25. **PromQL 性能优化** —— 减少高基数（High Cardinality）标签、避免 `rate()` 套 `rate()`、合理使用 Recording Rules

### 第三阶段：Grafana 可视化与告警（12 个知识点）

26. **Grafana 安装与初始化** —— 二进制安装、Docker 安装、配置文件（`grafana.ini`）关键参数
27. **数据源配置** —— 添加 Prometheus 数据源，配置 `Scrape interval` 与 Prometheus 一致，`Query timeout` 设置
28. **Panel 类型选择** —— Time series（时序图，最常用）、Stat（单值大屏）、Gauge（仪表盘）、Bar chart（柱状图）、Heatmap（热力图）、Table（表格）
29. **变量模板（Template Variables）** —— `label_values()` 查询提取标签值，`regex` 过滤，`multi-value` 多选，`all` 全选，级联变量
30. **Dashboard 导入** —— 从 Grafana.com 导入（ID 方式），从 JSON 文件导入，导入后如何修改适配自己的环境
31. **Annotation（注释）** —— 在图上标记部署事件、告警事件，关联 Prometheus 数据源或 GraphQL
32. **Alert（告警）配置** —— Grafana 内置告警 vs Prometheus Alertmanager 告警的选择，Grafana 8+ 统一告警架构
33. **Alertmanager 配置结构** —— `global`（全局配置）、`route`（告警路由）、`receivers`（接收器）、`inhibit_rules`（抑制规则）
34. **告警路由（Route）** —— 基于标签的告警分发（如：`team=backend` 发给后端群，`severity=critical` 打电话）
35. **接收器（Receiver）** —— 邮件（`email_configs`）、钉钉（`webhook_configs` + 钉钉机器人）、企业微信、Slack、PagerDuty
36. **抑制规则（Inhibit Rules）** —— 当高等级告警触发时，抑制低等级同类告警，避免告警风暴
37. **静默（Silence）** —— 维护窗口期间静默特定告警，通过 Web UI 或 API 配置

### 第四阶段：日志监控（ELK + Loki）（10 个知识点）

38. **ELK Stack 架构** —— Elasticsearch（存储和搜索）、Logstash（采集和过滤）、Kibana（可视化）、Beats（轻量采集器）
39. **Elasticsearch 核心概念** —— Index（索引）、Document（文档）、Mapping（映射）、Shard（分片）、Replica（副本）
40. **Elasticsearch 集群部署** —— 单节点 vs 多节点，Discovery Seed Hosts 配置，`cluster.initial_master_nodes` 初始化
41. **Filebeat 部署与配置** —— 比 Logstash Forwarder 更轻量，`filebeat.yml` 中 `inputs` 和 `outputs` 配置，Module 快速启用（如 `filebeat modules enable nginx`）
42. **Logstash 管道配置** —— `input`（输入）、`filter`（过滤）、`output`（输出）三阶段，grok 正则解析日志
43. **grok 过滤器** —— 预定义 pattern（`%{COMMONAPACHELOG}`），自定义 pattern，调试 grok 表达式（Grok Debugger 在线工具）
44. **Kibana 使用** —— Discover（日志检索）、Dashboard（日志可视化）、Alert（日志告警），KQL（Kibana Query Language）语法
45. **Loki 架构与优势** —— 不对日志内容做全文索引，只对元数据（标签）索引，存储成本远低于 ELK，适合大规模日志
46. **Loki 部署** —— `loki-config.yaml` 配置，Schema 版本选择（v11+ 推荐），S3/GCS 作为长期存储
47. **LogQL 查询语言** —— 类似 PromQL 的日志查询语法，`|= "error"` 过滤包含 error 的日志，`| json` 解析 JSON 日志

### 第五阶段：可观测性与进阶（10 个知识点）

48. **可观测性三大支柱** —— Metrics（指标，回答"系统有多健康"）、Logging（日志，回答"发生了什么"）、Tracing（链路追踪，回答"请求在哪里慢"）
49. **OpenTelemetry 标准** —— CNCF 可观测性统一标准，OTLP 协议，Collector 部署，替代传统的 Jaeger/Zipkin 客户端
50. **Jaeger / Zipkin 链路追踪** —— 微服务调用链可视化，Span 和 Trace 的概念，与 Prometheus 的集成
51. **SLA/SLO/SLI 体系** —— SLI（服务等级指标，如可用性 99.9%）、SLO（目标，如月度可用率 ≥ 99.9%）、SLA（对用户的承诺），Error Budget 计算
52. **Prometheus 高可用方案** —— 简单 HA（双写）、Thanos（全局查询 + 长期存储）、VictoriaMetrics（更高效的替代方案）
53. **Thanos 架构** —— Sidecar（边车）、Store（存储网关）、Query（全局查询）、Compactor（压缩）、Ruler（全局告警）
54. **VictoriaMetrics 优势** —— 相比 Prometheus 更省内存、查询更快、支持全局复制、兼容 PromQL，单节点可替代整套 Thanos
55. **监控告警最佳实践** —— 告警分层（P0 打电话、P1 钉钉、P2 邮件）、避免告警疲劳、每个告警都要有 runbook
56. **监控指标体系设计** —— USE 方法（Utilization/Saturation/Errors，适用于资源监控）、RED 方法（Rate/Errors/Duration，适用于服务监控）

---

## 💻 实战命令/配置示例

### 示例 1：Prometheus 主配置文件（prometheus.yml）

```yaml
# ==================== 全局配置 ====================
global:
  scrape_interval: 15s       # 抓取间隔（默认 1m）
  evaluation_interval: 15s   # 告警规则评估间隔
  external_labels:
    monitor: 'prometheus'    # 外部标签，多 Prometheus 实例时区分来源

# ==================== 告警管理器地址 ====================
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - localhost:9093   # Alertmanager 地址

# ==================== 告警规则文件 ====================
rule_files:
  - "rules/*.yml"            # 加载所有告警规则

# ==================== 抓取配置（核心） ====================
scrape_configs:
  # --------- 监控 Prometheus 自身 ---------
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # --------- 监控主机（Node Exporter）---------
  - job_name: 'node'
    file_sd_configs:          # 基于文件的动态发现（推荐！避免频繁改主配置）
      - files:
          - 'targets/node/*.json'
        refresh_interval: 5m

  # --------- 监控 MySQL ---------
  - job_name: 'mysql'
    static_configs:
      - targets: ['10.0.1.101:9104', '10.0.1.102:9104']

  # --------- 黑盒监控（HTTP 探测）---------
  - job_name: 'blackbox_http'
    metrics_path: /probe
    params:
      module: [http_2xx]     # Blackbox Exporter 中定义的模块名
    static_configs:
      - targets:
          - https://example.com
          - https://api.example.com/health
    relabel_configs:
      # 将 target 参数传递给 blackbox_exporter 的 target 参数
      - source_labels: [__address__]
        target_label: __param_target
      # 将探测结果关联到原始 target 标签
      - source_labels: [__param_target]
        target_label: instance
      # 真正的抓取目标改为 blackbox_exporter 地址
      - target_label: __address__
        replacement: localhost:9115
```

### 示例 2：Node Exporter 的 systemd 服务文件

```ini
# /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter for Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
# --web.listen-address 指定监听端口（默认 9100）
# --collector.systemd 开启 systemd 服务状态采集（可选）
ExecStart=/usr/local/bin/node_exporter \
  --web.listen-address=:9100 \
  --collector.systemd \
  --collector.processes

# 防止 OOM
OOMScoreAdjust=-1000
# 自动重启
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 示例 3：常用 PromQL 查询示例

```promql
# ==================== 主机监控 ====================
# CPU 使用率（排除 iowait）
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 内存使用率
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# 磁盘使用率（排除 tmpfs/proc 等虚拟文件系统）
100 - (node_filesystem_avail_bytes{fstype!="tmpfs",fstype!="devtmpfs"} / node_filesystem_size_bytes{fstype!="tmpfs",fstype!="devtmpfs"} * 100)

# 网络吞吐量（入方向，单位：字节/秒）
rate(node_network_receive_bytes_total{device!="lo"}[5m])

# ==================== MySQL 监控 ====================
# 慢查询速率（条/秒）
rate(mysql_slow_queries[5m])

# 连接使用率
mysql_global_status_threads_connected / mysql_global_variables_max_connections * 100

# InnoDB Buffer Pool 命中率（> 99% 为健康）
(1 - (rate(mysql_innodb_buffer_pool_reads[5m]) / rate(mysql_innodb_buffer_pool_read_requests[5m]))) * 100

# ==================== 黑盒监控 ====================
# HTTPS 证书剩余天数（< 30 天告警）
(probe_ssl_earliest_cert_expiry - time()) / 86400

# HTTP 探测成功率（按目标分组）
sum(rate(probe_success[5m])) by (instance)
```

### 示例 4：告警规则示例（rules/alerts.yml）

```yaml
groups:
  - name: 主机告警
    rules:
      # 告警 1：CPU 使用率过高
      - alert: 主机CPU使用率过高
        expr: |
          100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m                    # 持续 5 分钟才触发（避免抖动）
        labels:
          severity: warning        # 告警等级：critical/warning/info
          team: ops
        annotations:
          summary: "主机 {{ $labels.instance }} CPU 使用率超过 80%"
          description: "当前值：{{ $value }}%，已持续 5 分钟"

      # 告警 2：内存使用率过高
      - alert: 主机内存使用率过高
        expr: |
          (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100 > 90
        for: 5m
        labels:
          severity: critical
          team: ops
        annotations:
          summary: "主机 {{ $labels.instance }} 内存使用率超过 90%"

      # 告警 3：磁盘使用率过高
      - alert: 磁盘使用率过高
        expr: |
          100 - (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"} * 100) > 85
        for: 10m
        labels:
          severity: warning
          team: ops
        annotations:
          summary: "主机 {{ $labels.instance }} 根分区使用率超过 85%"

      # 告警 4：HTTPS 证书即将过期
      - alert: HTTPS证书即将过期
        expr: (probe_ssl_earliest_cert_expiry - time()) / 86400 < 30
        labels:
          severity: warning
          team: ops
        annotations:
          summary: "域名 {{ $labels.instance }} 的 SSL 证书将在 30 天内过期"
```

### 示例 5：Alertmanager 配置文件（alertmanager.yml）

```yaml
global:
  # 邮件告警配置
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alert@example.com'
  smtp_auth_username: 'alert@example.com'
  smtp_auth_password: 'your_password'

# 告警路由（树形结构，从上到下匹配）
route:
  group_by: ['alertname', 'team']   # 按告警名和 team 标签分组
  group_wait: 10s                    # 组内第一个告警等待 10s 再发送（合并窗口）
  group_interval: 5m                 # 组内新告警发送间隔
  repeat_interval: 4h               # 告警重复发送的间隔（防止一直发）
  receiver: 'default-receiver'       # 默认接收器
  routes:
    # 路由 1：P0 严重告警，打电话 + 短信
    - match:
        severity: critical
      receiver: 'p0-oncall'
      continue: true                 # 继续匹配后续路由（一个告警可触发多个接收器）
    # 路由 2：数据库相关告警，发给 DBA 团队
    - match:
        team: dba
      receiver: 'dba-dingtalk'

# 接收器定义
receivers:
  - name: 'default-receiver'
    email_configs:
      - to: 'ops-team@example.com'
        send_resolved: true          # 告警恢复时也发邮件

  - name: 'p0-oncall'
    webhook_configs:
      - url: 'https://hooks.dingtalk.com/robot/send?access_token=xxx'
        send_resolved: true

  - name: 'dba-dingtalk'
    webhook_configs:
      - url: 'https://hooks.dingtalk.com/robot/send?access_token=yyy'
        send_resolved: true

# 抑制规则：当主机宕机告警触发时，抑制该主机上的其他告警（避免告警风暴）
inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match_re:
      severity: 'warning|info'
    equal: ['instance']              # 同一实例的告警才抑制
```

### 示例 6：Filebeat 配置文件（filebeat.yml）

```yaml
filebeat.inputs:
  # 采集 Nginx 访问日志
  - type: log
    enabled: true
    paths:
      - /var/log/nginx/access.log
    fields:
      log_type: nginx_access
    json.keys_under_root: true      # 如果日志是 JSON 格式，直接解析到顶层

  # 采集应用错误日志
  - type: log
    enabled: true
    paths:
      - /var/log/myapp/*.log
    fields:
      log_type: app_error
    multiline.pattern: '^\d{4}-\d{2}-\d{2}'  # 多行合并（Java 异常栈）
    multiline.negate: true
    multiline.match: after

# 输出到 Logstash（推荐，可以做过滤）
output.logstash:
  hosts: ["10.0.1.100:5044"]

# 或者直接输出到 Elasticsearch（简单场景）
# output.elasticsearch:
#   hosts: ["localhost:9200"]
#   index: "filebeat-%{+yyyy.MM.dd}"
```

### 示例 7：Loki 查询示例（LogQL）

```logql
# 查找包含 "error" 的日志（最近 1 小时）
{job="myapp"} |= "error" 

# 查找包含 "error" 但不包含 "timeout" 的日志
{job="myapp"} |= "error" != "timeout"

# 解析 JSON 日志并筛选 status >= 500 的请求
{job="nginx"} | json | status >= 500

# 统计最近 5 分钟内错误日志数量（类似 PromQL）
count_over_time({job="myapp"} |= "error" [5m])

# 按 level 分组统计日志条数
sum by (level) (count_over_time({job="myapp"} | json [5m]))
```

### 示例 8：Grafana CLI 常用命令

```bash
# 安装 Grafana（CentOS/Almalinux）
yum install -y grafana

# 启动 Grafana
systemctl enable --now grafana-server

# CLI：列出已安装的插件
grafana-cli plugins ls

# CLI：安装常用插件（饼图、时钟、Zabbix 数据源）
grafana-cli plugins install grafana-piechart-panel
grafana-cli plugins install grafana-clock-panel
grafana-cli plugins install alexanderzobnin-zabbix-datasource

# 重启使插件生效
systemctl restart grafana-server

# 重置 admin 密码（忘记密码时）
grafana-cli admin reset-admin-password new_password
```

### 示例 9：Blackbox Exporter 配置文件

```yaml
# blackbox.yml
modules:
  http_2xx:                    # HTTP 探测模块
    prober: http
    timeout: 5s
    http:
      valid_http_versions: ["HTTP/1.1", "HTTP/2"]
      no_follow_redirects: false
      preferred_ip_protocol: "ip4"

  tcp_connect:                # TCP 端口探测
    prober: tcp
    timeout: 3s

  icmp_ping:                  # ICMP Ping 探测
    prober: icmp
    timeout: 3s
    icmp:
      preferred_ip_protocol: "ip4"
```

### 示例 10：Prometheus 空间不足处理

```bash
# 查看 Prometheus 数据目录大小
du -sh /var/lib/prometheus/

# 手动删除旧数据（谨慎！）
# 正确方式：修改启动参数调整保留时间
# --storage.tsdb.retention.time=30d

# 查看 Prometheus TSDB 状态
curl http://localhost:9090/api/v1/status/tsdb

# 查看当前抓取目标状态（哪些 target 掉线了）
curl http://localhost:9090/api/v1/targets | jq
```

---

## 🧪 实战项目

### 项目 1：搭建完整的 Prometheus + Grafana 监控体系

**项目目标**：为 20 台服务器的生产环境搭建一套完整的监控告警体系，覆盖主机、MySQL、Redis、Nginx、黑盒监控。

**步骤**：

1. **部署 Prometheus** —— 二进制部署，配置 `prometheus.yml`，设置 systemd 自启动
2. **部署 Node Exporter** —— 所有 20 台服务器安装 Node Exporter，用 `file_sd_configs` 实现自动发现
3. **部署 Grafana** —— 安装 Grafana，添加 Prometheus 数据源，导入 Node Exporter Dashboard（ID: 1860）
4. **配置 MySQL/Redis 监控** —— 部署 `mysqld_exporter` 和 `redis_exporter`，在 Grafana 中导入对应 Dashboard
5. **部署 Blackbox Exporter** —— 配置 HTTP/TCP 探测，监控所有对外的 Web 服务可用性
6. **配置 Alertmanager** —— 配置钉钉/企业微信告警，设置告警路由和抑制规则
7. **编写自定义告警规则** —— CPU/内存/磁盘/证书过期/MySQL 主从延迟等核心告警
8. **压测验证** —— 用 `stress` 工具压测 CPU，验证告警是否按时触发；停止一台后端，验证告警恢复通知

**验收标准**：所有 Target 在 Prometheus Web UI 中状态为 UP、Grafana Dashboard 数据正常展示、告警触发后 1 分钟内收到通知。

---

### 项目 2：搭建 ELK 日志平台

**项目目标**：为 Nginx + 应用服务搭建统一的日志采集、存储、查询平台，支持按关键词检索和日志告警。

**步骤**：

1. **部署 Elasticsearch 集群** —— 3 节点，配置 `discovery.seed_hosts` 和 `cluster.initial_master_nodes`
2. **部署 Kibana** —— 连接 Elasticsearch，配置中文界面（`i18n.locale: "zh-CN"`）
3. **部署 Filebeat** —— 在每台应用服务器安装 Filebeat，配置 Nginx 日志和应用日志的采集
4. **部署 Logstash（可选）** —— 如果需要对日志做复杂过滤/富化，在 Filebeat 和 Elasticsearch 之间加 Logstash
5. **配置 Index Pattern** —— 在 Kibana 中创建 Index Pattern，开始检索日志
6. **配置日志告警** —— 当错误日志中出现特定关键词（如 `OutOfMemoryError`）时，触发告警发送到钉钉
7. **配置 ILM（索引生命周期管理）** —— 自动删除 30 天前的日志，防止磁盘被撑满

**验收标准**：Kibana Discover 中能检索到各服务的日志、日志告警能正常触发、历史日志按 ILM 策略自动清理。

---

## 🔧 常见故障排查

### 故障 1：Prometheus Target 状态为 DOWN

**现象**：Prometheus Web UI（Status → Targets）中，部分 Target 显示为 DOWN，报错 `context deadline exceeded` 或 `connection refused`。

**诊断步骤**：
```bash
# 1. 从 Prometheus 服务器测试目标端口连通性
curl -v http://10.0.1.101:9100/metrics

# 2. 检查目标服务器的防火墙
iptables -L -n | grep 9100
firewall-cmd --list-all

# 3. 检查 Exporter 服务是否运行
systemctl status node_exporter

# 4. 查看 Exporter 监听地址（是否只监听了 127.0.0.1）
ss -tlnp | grep 9100
# 如果显示 127.0.0.1:9100，需要改为 0.0.0.0:9100
```

**解决方案**：启动 Exporter 服务 / 放行防火墙端口 / 修改 Exporter 监听地址为 `0.0.0.0`。

---

### 故障 2：Grafana Panel 显示 "No data"

**现象**：Grafana Dashboard 中部分 Panel 显示 "No data"，但 Prometheus 中有数据。

**诊断步骤**：
```
# 1. 点击 Panel 标题 → Inspect → Query，查看 PromQL 查询结果
# 2. 检查时间范围（右上角）是否覆盖了数据时间
# 3. 检查数据源是否选对（Panel 右上角 → Query 里的数据源下拉框）
# 4. 在 Prometheus Web UI 中直接执行相同的 PromQL，确认是否有结果
```

**解决方案**：调整时间范围 / 修正 PromQL（常见错误：标签名拼写错误、指标名错误）/ 检查数据源配置。

---

### 故障 3：告警不触发或重复触发

**现象**：设置了告警规则，但达到阈值后没有收到告警；或者告警恢复后还在一直发。

**诊断步骤**：
```bash
# 1. 查看 Prometheus Web UI → Alerts，看告警规则状态
#    状态说明：Inactive（未触发）、Pending（等待 for 时间）、Firing（已触发）

# 2. 检查 for 持续时间是否设置过长
# 3. 查看 Alertmanager 状态
curl http://localhost:9093/api/v2/status

# 4. 查看 Alertmanager 是否收到了告警
curl http://localhost:9093/api/v2/alerts | jq
```

**解决方案**：
- 不触发：检查 `for` 时长、检查 PromQL 是否正确、检查 Alertmanager 路由配置
- 重复触发：调整 `repeat_interval`（默认 1h，建议改为 4h 或更长）

---

### 故障 4：Elasticsearch 集群状态为 Red

**现象**：Kibana 或 `curl 'localhost:9200/_cluster/health'` 返回 `"status":"red"`，部分索引无法写入。

**诊断步骤**：
```bash
# 1. 查看集群健康状态
curl 'localhost:9200/_cluster/health?pretty'

# 2. 查看哪些索引是 Red
curl 'localhost:9200/_cat/indices?v' | grep red

# 3. 查看未分配的分片原因
curl 'localhost:9200/_cat/shards?h=index,shard,prirep,state,unassigned.reason' | grep UNASSIGNED
```

**常见原因及解决方案**：
- 磁盘空间不足：`curl 'localhost:9200/_cat/allocation?v'` 查看，清理磁盘或增加节点
- 节点下线导致副本无法分配：等待节点恢复，或临时设置 `index.number_of_replicas: 0`
- 脑裂问题：检查 `discovery.zen.minimum_master_nodes` 配置（ES 7.x 之前）

---

### 故障 5：Prometheus 磁盘空间耗尽

**现象**：Prometheus 服务器磁盘使用率 100%，Prometheus 进程可能被 OOM 或退出。

**诊断步骤**：
```bash
# 1. 查看磁盘使用情况
df -h

# 2. 查看 Prometheus 数据目录大小
du -sh /var/lib/prometheus/

# 3. 查看保留策略
ps aux | grep prometheus | grep retention
```

**解决方案**：
```bash
# 临时：手动删除旧数据（不推荐，用下面调整保留时间的方式）
systemctl stop prometheus
rm -rf /var/lib/prometheus/wal/*   # 慎用！会丢失近期数据

# 正确方式：调整 Prometheus 启动参数
# --storage.tsdb.retention.time=15d  （从 30d 改为 15d）
# --storage.tsdb.retention.size=100GB （限制总大小，Prometheus 2.39+ 支持）

systemctl edit prometheus  # 添加覆盖参数后重启
```

---

## 💼 面试高频题

### 1. Prometheus 的 Pull 模型和 Push 模型各有什么优缺点？

**答案要点**：
- Pull 优点：主动控制抓取频率、Exporter 无状态易于水平扩展、可以通过 `/metrics` 直接调试
- Pull 缺点：防火墙复杂环境下难以穿透、短生命周期任务无法 Pull
- Push（Pushgateway）优点：适合批处理任务、FaaS/Serverless 场景
- Push 缺点：Pushgateway 单点风险、丢失标签信息、不适合作长期监控

---

### 2. rate() 和 irate() 的区别是什么？使用场景？

**答案要点**：
- `rate()`：计算指定时间范围内的每秒平均增长率，平滑瞬时波动，适合告警和趋势图
- `irate()`：只取时间范围内最后两个样本点计算瞬时增长率，灵敏度高，适合短期波动监控
- 告警规则推荐用 `rate()`（避免抖动触发误告警），实时监控面板可用 `irate()`

---

### 3. PromQL 中 Counter 类型的指标如何正确使用？

**答案要点**：
- Counter 只增不减（除非重启重置），不能直接用原始值做监控
- 必须用 `rate()` 或 `increase()` 计算增长率
- 错误示例：`http_requests_total > 1000`（永远为真，Counter 一直增长）
- 正确示例：`rate(http_requests_total[5m]) > 10`（每秒请求数超过 10）

---

### 4. Alertmanager 的抑制规则（Inhibit Rules）是什么？解决什么问题？

**答案要点**：
- 抑制规则：当某个高等级告警触发时，抑制与之相关的低等级告警
- 解决问题：避免告警风暴（如主机宕机触发 CPU/内存/磁盘/服务 所有告警）
- 配置关键：`source_match`（触发抑制的告警）、`target_match`（被抑制的告警）、`equal`（必须相同的标签）

---

### 5. Elasticsearch 中的分片（Shard）和副本（Replica）怎么设置？

**答案要点**：
- 分片：数据水平拆分，搜索并行度更高，但分片过多会增加开销
- 副本：高可用和负载均衡，但不占用主分片资源
- 经验公式：每个分片大小建议在 10GB-50GB 之间；分片总数不要超过 `节点数 × 每节点 CPU 核数`
- 重要：索引创建后分片数不能修改，副本数可以动态调整

---

### 6. Loki 和 ELK 的核心区别是什么？适用场景？

**答案要点**：
- ELK：对日志全文建立倒排索引，查询快但存储成本高（通常 1:3 压缩比）
- Loki：只对标签（元数据）建立索引，不对日志内容索引，存储成本极低（1:20+ 压缩比）
- Loki 适用：大规模日志、成本敏感、主要通过标签过滤后查看日志
- ELK 适用：需要对日志内容做全文搜索、复杂的日志分析场景

---

### 7. 如何设计一个好的监控告警体系（避免告警疲劳）？

**答案要点**：
- 告警分层：P0（打电话）、P1（钉钉/企微）、P2（邮件）、P3（不告警，只记录）
- 每个告警都要有 runbook（处理手册），否则没必要告警
- 使用 `for` 字段避免抖动，合理设置阈值（不要设得太敏感）
- 定期审查告警（哪些告警从来不处理？说明阈值有问题）
- 关键指标：SLA 达成情况、Error Budget 消耗速度

---

### 8. SLA/SLO/SLI 的定义和计算方法？

**答案要点**：
- SLI（Service Level Indicator）：服务等级指标，如可用性（成功请求/总请求）
- SLO（Service Level Objective）：目标值，如月度可用性 ≥ 99.9%
- SLA（Service Level Agreement）：对客户的承诺，通常有赔偿条款
- Error Budget = 1 - SLO，如 99.9% 的 SLO 对应 0.1% 的 Error Budget
- 计算：用 Prometheus 记录成功请求数，按月聚合计算可用性是否达标

---

## 📈 进阶学习路径

```
监控基础（Linux 基础监控）
  ↓
Prometheus + Grafana（云原生监控核心）
  ↓
PromQL 精通 + 告警规则编写
  ↓
ELK / Loki 日志平台
  ↓
链路追踪（Jaeger / Zipkin / OpenTelemetry）
  ↓
可观测性统一平台（Metrics + Logging + Tracing 三合一）
  ↓
大规模监控架构（Thanos / VictoriaMetrics / M3DB）
  ↓
SRE 体系（SLA/SLO/Error Budget / 事故复盘）
```

**推荐下一步学习**：
- 如果偏运维方向：深入学习 **Thanos/VictoriaMetrics** 和 **大规模 Prometheus 架构设计**
- 如果偏开发方向：学习 **OpenTelemetry** 和 **自定义 Exporter 开发**
- 如果偏 SRE 方向：学习 **SRE Workbook（Google）** 和 **事故管理流程**

---

[← 返回中文版首页](../README.md)
