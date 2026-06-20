# 08 · Monitoring & Observability

> **Learning Context**: "You can't fix what you can't measure" isn't just a saying — it's the operational reality of every production system. Monitoring tells you *when* something is wrong; observability helps you understand *why*. In this module, you'll build a complete observability stack: Prometheus pulling metrics, Grafana visualizing them, the ELK stack aggregating logs, and OpenTelemetry tying distributed traces together. By the end, you'll be able to design monitoring systems that actually page you when something actionable is happening — and give you the data to debug it quickly.

---

## 🎯 Learning Objectives

- [ ] Deploy Prometheus with proper scrape configs, service discovery, and retention settings
- [ ] Write effective PromQL queries: rate(), histogram_quantile(), predict_linear()
- [ ] Design and implement recording rules and alerting rules
- [ ] Configure Alertmanager with routing trees, inhibition rules, and notification integrations
- [ ] Build actionable Grafana dashboards with variables, annotations, and thresholds
- [ ] Deploy the ELK stack (Elasticsearch, Logstash/Filebeat, Kibana) for centralized logging
- [ ] Implement structured (JSON) logging across applications for better log analysis
- [ ] Set up OpenTelemetry Collector and instrument an app with traces
- [ ] Understand the three pillars: metrics (what), logs (why), traces (where)
- [ ] Implement SLO-based alerting with error budget burn rates
- [ ] Deploy long-term metrics storage: Thanos, Mimir, or Victoria Metrics
- [ ] Configure log rotation, retention policies, and storage optimization
- [ ] Build a runbook culture: every alert links to a diagnostic playbook
- [ ] Understand black-box vs white-box monitoring and when to use each
- [ ] Set up synthetic monitoring (blackbox exporter) for user-journey checks

---

## 📺 Recommended Video Courses

| Course | Creator | Views/Info | Level |
|--------|----------|------------|-------|
| [Prometheus Full Course](https://www.youtube.com/watch?v=hTZd RStkHc) | TechWorld with Nana | ~1.5M views | Beginner→Intermediate |
| [Grafana Dashboard Tutorial](https://www.youtube.com/watch?v=sKNZMtoSHN4) | Grafana Labs (official) | ~380k views | Intermediate |
| [PromQL Deep Dive](https://www.youtube.com/watch?v=ZZHbQM25CT零) | Prometheus Berlin | ~85k views | Advanced |
| [OpenTelemetry Explained](https://www.youtube.com/watch?v=NM5InfLStBM) | CNCF / OpenTelemetry | ~120k views | Intermediate |
| [ELK Stack Full Course](https://www.youtube.com/watch?v=B8vk8HUtJwk) | Edureka | ~450k views | Beginner→Intermediate |
| [SRE Monitoring Best Practices](https://www.youtube.com/watch?v=oBLJoUbHBFM) | Google SRE / USENIX | ~95k views | Advanced |
| [Distributed Tracing with Jaeger](https://www.youtube.com/watch?v=WRnt_aiUbYA) | Jaeger Tracing | ~60k views | Intermediate |
| [Thanos for Scale](https://www.youtube.com/watch?v=mHkW8RgrpcE) | Thanos Community | ~40k views | Advanced |

---

## 📖 Recommended Books

| Book | Author | Rating | Recommendation |
|------|--------|--------|----------------|
| **Prometheus Up & Running (2nd Ed.)** | Brian Brazil | ★★★★★ | The definitive guide — by the creator of Prometheus |
| **Observability Engineering** | Charity Majors, et al. | ★★★★★ | Modern observability thinking — a paradigm shift |
| **The Art of Monitoring** | James Turnbull | ★★★★☆ | Practical, hands-on monitoring stack build |
| **Logging in Action** | Phil Wilkins | ★★★★☆ | Deep dive into log aggregation and analysis |
| **Site Reliability Engineering (Ch. 6: Monitoring)** | Google SRE Team | ★★★★★ | Free online; the canon of monitoring philosophy |
| **Distributed Tracing in Practice** | Austin Parker, et al. | ★★★★☆ | Real-world tracing implementation patterns |
| **Elasticsearch: The Definitive Guide** | Clinton Gormley | ★★★★☆ | Essential if you run ELK — free online |

---

## 🌐 Online Resources

| Resource | Link | Stars/Info |
|----------|------|------------|
| **Prometheus Docs** | https://prometheus.io/docs | Official |
| **PromQL Cheat Sheet** | https://prometheus.io/docs/prometheus/latest/querying/basics | Official |
| **Grafana Docs** | https://grafana.com/docs | Official |
| **Grafana Dashboards (Community)** | https://grafana.com/grafana/dashboards | 10,000+ dashboards |
| **OpenTelemetry Docs** | https://opentelemetry.io/docs | Official |
| **Elasticsearch Docs** | https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html | Official |
| **awesome-prometheus** | https://github.com/roaldnefs/awesome-prometheus | ⭐3.2k |
| **awesome-observability** | https://github.com/maxday/awesome-observability | ⭐1.8k |
| **Prometheus Operator** | https://github.com/prometheus-operator/prometheus-operator | ⭐9k |
| **Jaeger Docs** | https://www.jaegertracing.io/docs | Official |

---

## 📝 Core Knowledge Checklist

### Phase 1: Monitoring Fundamentals & Prometheus Architecture

- [ ] **White-box vs black-box monitoring**: knowing what each tells you and when to use both
- [ ] **The four golden signals**: latency, traffic, errors, saturation — what to monitor first
- [ ] **Prometheus architecture**: TSDB, scrape mechanism, service discovery, query engine
- [ ] **Pull vs push model**: why Prometheus prefers pull, when to use Pushgateway
- [ ] **Metric types**: Counter (always up), Gauge (up/down), Histogram (buckets), Summary
- [ ] **Prometheus data model**: time series identified by metric name + label set
- [ ] **Cardinality explosion**: why high-cardinality labels (user_id, request_id) kill Prometheus
- [ ] **Scrape intervals**: balancing freshness vs. storage cost (15s-60s typical)
- [ ] **Service discovery**: static configs, DNS, Consul, Kubernetes API
- [ ] **Prometheus Federation**: scaling Prometheus by hierarchical data aggregation
- [ ] **Storage internals**: TSDB blocks, WAL (Write-Ahead Log), head block, compaction
- [ ] **Retention strategies**: local retention vs. remote write to long-term storage

### Phase 2: PromQL — The Query Language

- [ ] **Instant vs range queries**: understanding the difference in PromQL semantics
- [ ] **Selectors**: `http_requests_total` (all), `http_requests_total{status="200"}` (filter), `{__name__=~"http_.*"}` (regex)
- [ ] **Rate() function**: the most important function — `rate()` vs `increase()` vs raw counter
- [ ] **Histogram analysis**: `histogram_quantile(0.99, rate(bucket[5m]))` — the p99 latency query
- [ ] **Aggregation operators**: `sum()`, `avg()`, `count()`, `topk()`, `bottomk()`, `quantile()`
- [ ] **By vs without**: `sum by (service)` vs `sum without (instance)` — grouping semantics
- [ ] **Offset modifier**: `rate(http_requests[5m] offset 1h)` — compare to 1 hour ago
- [ ] **Predictive functions**: `predict_linear()` for capacity planning, `holt_winters()` for forecasting
- [ ] **Subqueries**: `max_over_time(rate(...)[5m:1m])` — nested range selectors
- [ ] **Recording rules**: pre-computing expensive queries for dashboard performance
- [ ] **Alerting rules syntax**: `expr`, `for`, `labels`, `annotations`
- [ ] **Common mistakes**: rate() on a Gauge, ignoring IRATE for counters, missing `by` clause

### Phase 3: Alertmanager & Alert Design

- [ ] **Alerting philosophy**: alert on symptoms (user-facing impact), not causes
- [ ] **Alertmanager architecture**: receives alerts, deduplicates, groups, routes, sends notifications
- [ ] **Routing trees**: route alerts based on labels (team, severity, service)
- [ ] **Inhibition rules**: suppress "disk critical" alerts when "host down" is firing
- [ ] **Silences**: muting alerts during maintenance windows
- [ ] **Notification integrations**: Slack, PagerDuty, OpsGenie, email, webhook
- [ ] **Grouping and timing**: `group_by`, `group_wait`, `group_interval`, `repeat_interval`
- [ ] **Error budget burn rate alerts**: SLO-based alerting (Google SRE method)
- [ ] **Alert fatigue prevention**: if an alert pages and isn't actionable, delete it
- [ ] **Runbook integration**: every alert should have a `runbook_url` annotation
- [ ] **Dead man's switch**: always-fire alert to detect when Alertmanager itself is down

### Phase 4: Grafana Dashboards

- [ ] **Dashboard structure**: rows, panels, variables, annotations, links
- [ ] **Panel types**: time series, stat, gauge, bar gauge, heatmap, table, logs panel
- [ ] **Templating variables**: query-based variables (`label_values()`), custom variables, chaining
- [ ] **Dashboard best practices**: golden signal panels at top, instance-level detail below
- [ ] **Thresholds and overrides**: setting visual thresholds (green/yellow/red)
- [ ] **Annotations**: marking deployments, incidents on graphs for correlation
- [ ] **Alerts from Grafana**: Grafana-managed alerts vs. Prometheus-managed alerts
- [ ] **Dashboard provisioning**: storing dashboards as code (JSON) in Git
- [ ] **Grafana Loki integration**: correlating metrics and logs in same dashboard
- [ ] **Grafana Tempo integration**: adding traces to the observability triangle
- [ ] **Dashboard permissions and folders**: organizing dashboards by team
- [ ] **Grafana Mimir / Loki data sources**: unified observability platform

### Phase 5: Logging with ELK/EFK Stack

- [ ] **Logging architecture**: shipper → buffer → indexer → storage → search UI
- [ ] **Elasticsearch fundamentals**: index, document, shard, replica, cluster health
- [ ] **Filebeat**: lightweight log shipper, modules for common log formats
- [ ] **Logstash**: parsing, filtering, transforming logs (Grok patterns, mutate, date filters)
- [ ] **Kibana**: Discover, Dashboard, Visualize — the log analysis UI
- [ ] **Structured logging**: JSON logs vs plain text — why JSON wins at scale
- [ ] **Log rotation**: `logrotate` configuration, preventing disk full scenarios
- [ ] **Index lifecycle management (ILM)**: hot → warm → cold → delete automation
- [ ] **Elasticsearch tuning**: heap size (never exceed 32GB), shard size (10-50GB optimal)
- [ ] **Fluentd/Fluent Bit**: lightweight alternatives to Logstash for Kubernetes
- [ ] **Centralized logging in K8s**: DaemonSet for log collection, sidecar pattern
- [ ] **Log retention strategy**: balancing compliance requirements with storage costs

### Phase 6: Distributed Tracing & OpenTelemetry

- [ ] **Why traces matter**: debugging across microservice boundaries
- [ ] **Trace anatomy**: trace ID, span ID, parent span ID, operations, tags, logs
- [ ] **OpenTelemetry**: unifying OpenTracing + OpenCensus, vendor-neutral standard
- [ ] **OTel Collectator**: receiving, processing, exporting telemetry data
- [ ] **Auto-instrumentation**: adding traces without code changes (Java, Python, Node.js)
- [ ] **Manual instrumentation**: creating custom spans for business logic
- [ ] **Context propagation**: passing trace context across service boundaries (W3C Trace Context)
- [ ] **Sampling strategies**: head-based vs tail-based sampling, always-on, probabilistic
- [ ] **Jaeger**: deploying the all-in-one, understanding the UI (Trace Graph, Trace Detail)
- [ ] **Tempo**: Grafana's distributed tracing backend — object storage-based, cheaper than Jaeger
- [ ] **Correlating traces with logs**: including `trace_id` in log entries
- [ ] **Correlating traces with metrics**: exemplars in Prometheus

---

## 💻 Hands-on Commands & Configuration Examples

### 1. Prometheus Configuration (`prometheus.yml`)

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: 'prod-us-east1'
    region: 'us-east1'

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

# Load alerting rules
rule_files:
  - '/etc/prometheus/rules/*.yml'
  - 'slo_rules.yml'   # SLO-based alerting

# Scrape configurations
scrape_configs:
  # Prometheus self-monitoring
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Node Exporter — system metrics
  - job_name: 'node'
    consul_sd_configs:       # Service discovery via Consul
      - server: 'consul:8500'
    relabel_configs:
      - source_labels: [__meta_consul_service_port]
        target_label: __address__
        regex: '(.*)'
        replacement: '${1}:9100'

  # Kubernetes API-based service discovery
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        regex: "true"
        action: keep
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        target_label: __metrics_path__
        regex: (.+)

  # Blackbox exporter — endpoint monitoring
  - job_name: 'blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
        - https://app.example.com/health
        - https://api.example.com/ready
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - replacement: blackbox-exporter:9115
        target_label: __address__
```

### 2. Prometheus Alerting Rules (`alerts.yml`)

```yaml
groups:
  - name: app_alerts
    rules:
      # High error rate — pages immediately
      - alert: HighErrorRate
        expr: |
          rate(http_requests_total{status=~"5.."}[5m])
          / rate(http_requests_total[5m]) > 0.05
        for: 2m
        labels:
          severity: critical
          team: backend
        annotations:
          summary: "High error rate on {{ $labels.service }}"
          description: "{{ $value | printf \"%.1f\" }}% error rate over 5 minutes"
          runbook_url: "https://wiki.example.com/runbooks/high-error-rate"

      # Latency SLO violation — warning
      - alert: HighLatency
        expr: |
          histogram_quantile(0.99,
            rate(http_request_duration_seconds_bucket[5m])
          ) > 0.5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "p99 latency exceeding 500ms SLO"

      # Error budget burn rate — SRE method
      - alert: ErrorBudgetBurn
        expr: |
          (
            (1 - (rate(http_requests_total{status=~"2.."}[30m])
                  / rate(http_requests_total[30m])))
            / (1 - 0.999)  # SLO is 99.9%
          ) > 2  # Burn rate > 2x — fast burn
        for: 5m
        labels:
          severity: critical
          notification: page
        annotations:
          summary: "Error budget burning fast — {{ $value | printf \"%.1f\" }}x rate"
```

### 3. Alertmanager Configuration (`alertmanager.yml`)

```yaml
global:
  slack_api_url: 'https://hooks.slack.com/services/XXX/YYY/ZZZ'
  smtp_smarthost: 'smtp.gmail.com:587'
  smtp_from: 'alerts@example.com'

# Route alerts based on labels
route:
  group_by: ['alertname', 'cluster', 'team']
  group_wait: 10s        # Wait to batch initial alerts
  group_interval: 10m     # How long to wait before sending again
  repeat_interval: 12h    # How often to re-send firing alerts
  receiver: 'slack-general'
  routes:
    # Critical alerts page the on-call engineer
    - match:
        severity: critical
      receiver: 'pagerduty'
      routes:
        - match:
            team: backend
          receiver: 'pagerduty-backend'
        - match:
            team: platform
          receiver: 'pagerduty-platform'

    # Warning alerts go to Slack only
    - match:
        severity: warning
      receiver: 'slack-alerts'

    # Database alerts have their own channel
    - match_re:
        service: 'mysql|postgres|redis'
      receiver: 'slack-database'

# Inhibition rules — suppress lower-severity alerts
inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'cluster', 'service']

receivers:
  - name: 'slack-general'
    slack_configs:
      - channel: '#alerts'
        title: '{{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'

  - name: 'pagerduty-backend'
    pagerduty_configs:
      - service_key: 'YOUR_PAGERDUTY_INTEGRATION_KEY'
        description: '{{ .GroupLabels.alertname }}: {{ .CommonAnnotations.summary }}'
```

### 4. PromQL Query Cookbook

```promql
# ── Basic queries ──────────────────────────────────────────

# Request rate (always use rate(), never use raw counter values)
rate(http_requests_total[5m])

# Error rate percentage
rate(http_requests_total{status=~"5.."}[5m])
/ rate(http_requests_total[5m]) * 100

# 95th percentile latency (p95)
histogram_quantile(0.95,
  rate(http_request_duration_seconds_bucket[5m])
)

# 99th percentile latency (p99) — the SLA metric
histogram_quantile(0.99,
  rate(http_request_duration_seconds_bucket[5m])
)

# CPU usage percentage per instance
100 - (avg by(instance) (
  rate(node_cpu_seconds_total{mode="idle"}[5m])
) * 100)

# Memory usage percentage
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes)
/ node_memory_MemTotal_bytes * 100

# Disk usage percentage per mount point
(node_filesystem_size_bytes - node_filesystem_free_bytes)
/ node_filesystem_size_bytes * 100

# ── Advanced queries ──────────────────────────────────────

# Predict when disk will fill up (in seconds)
predict_linear(node_filesystem_free_bytes[6h], 3600)

# Top 5 services by request rate
topk(5, rate(http_requests_total[5m]))

# Requests per second by status code
sum by (status) (rate(http_requests_total[5m]))

# Detect stuck processes (CPU at 100% for >10 minutes)
max_over_time(rate(node_cpu_seconds_total{mode!="idle"}[5m])[10m:1m]) > 0.95

# Compare current error rate to same time yesterday
rate(http_requests_total{status=~"5.."}[5m])
/ rate(http_requests_total[5m])
- (rate(http_requests_total{status=~"5.."}[5m] offset 24h)
   / rate(http_requests_total[5m] offset 24h))
```

### 5. Grafana Dashboard Provisioning (`dashboard.yml`)

```yaml
apiVersion: 1
providers:
  - name: 'default'
    orgId: 1
    folder: ''
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    allowUiUpdates: false   # Force GitOps — disable UI edits
    options:
      path: /etc/grafana/provisioning/dashboards
      foldersFromFilesStructure: true
```

### 6. Filebeat Configuration (`filebeat.yml`)

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/app/*.log
    json.keys_under_root: true    # Parse JSON logs
    json.add_error_key: true
    fields:
      env: production
      service: myapp
    fields_under_root: false

  - type: log
    enabled: true
    paths:
      - /var/log/nginx/access.log
    processors:
      - dissect:
          tokenizer: '%{client_ip} - %{user} [%{timestamp}] "%{method} %{path} %{protocol}" %{status} %{bytes} "%{referer}" "%{user_agent}"'
          field: "message"
          target_prefix: ""

# Output to Logstash (processing) or Elasticsearch (direct)
output.logstash:
  hosts: ["logstash:5044"]

# Or output directly to Elasticsearch
# output.elasticsearch:
#   hosts: ["elasticsearch:9200"]
#   index: "filebeat-%{+yyyy.MM.dd}"

processors:
  - add_host_metadata:
      when.not.contains:
        tags: forwarded
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
```

### 7. Logstash Pipeline Configuration (`pipeline.conf`)

```ruby
input {
  beats {
    port => 5044
  }
}

filter {
  # Parse JSON-formatted application logs
  if [fields][service] {
    json {
      source => "message"
      skip_on_invalid_json => true
    }
  }

  # Parse Nginx access logs
  if [fields][logtype] == "nginx_access" {
    grok {
      match => {
        "message" => '%{IPORHOST:client_ip} - %{USER:user} \[%{HTTPDATE:timestamp}\] "%{WORD:method} %{URIPATH:path} %{DATA:protocol}" %{NUMBER:status} %{NUMBER:bytes} "%{DATA:referer}" "%{DATA:user_agent}"'
      }
    }
    date {
      match => [ "timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ]
    }
    geoip {
      source => "client_ip"
    }
  }

  # Add environment tag
  mutate {
    add_field => { "environment" => "${ENV:production}" }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
    # Use ILM (Index Lifecycle Management)
    ilm_enabled => true
    ilm_rollover_alias => "logs"
    ilm_pattern => "{now/d}-000001"
  }
}
```

### 8. OpenTelemetry Collector Configuration (`otel-collector-config.yml`)

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

  prometheus:
    config:
      scrape_configs:
        - job_name: 'otel-collector'
          scrape_interval: 10s
          static_configs:
            - targets: ['localhost:8888']

processors:
  batch:
    send_batch_size: 1000
    timeout: 10s

  memory_limiter:
    check_interval: 1s
    limit_mib: 4000

  attributes:
    actions:
      - key: environment
        value: production
        action: insert

exporters:
  prometheus:
    endpoint: "0.0.0.0:8889"

  loki:
    endpoint: "http://loki:3100/loki/api/v1/push"

  jaeger:
    endpoint: "jaeger-collector:14250"
    tls:
      insecure: true

  logging:
    loglevel: info

service:
  pipelines:
    metrics:
      receivers: [otlp, prometheus]
      processors: [batch]
      exporters: [prometheus, logging]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [loki, logging]
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger, logging]
```

### 9. Docker Compose for Local Observability Stack

```yaml
version: '3.8'
services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./rules:/etc/prometheus/rules
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=30d'
      - '--web.enable-lifecycle'
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

  alertmanager:
    image: prom/alertmanager:latest
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
    command:
      - '--config.file=/etc/alertmanager/alertmanager.yml'
      - '--storage.path=/alertmanager'
    ports:
      - "9093:9093"

  node-exporter:
    image: prom/node-exporter:latest
    pid: host
    volumes:
      - /:/rootfs:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
    command:
      - '--path.rootfs=/rootfs'
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms2g -Xmx2g"
      - xpack.security.enabled=false
    volumes:
      - es_data:/usr/share/elasticsearch/data
    ports:
      - "9200:9200"

  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200

  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686"   # UI
      - "4317:4317"     # OTLP gRPC
      - "4318:4318"     # OTLP HTTP

volumes:
  prometheus_data:
  grafana_data:
  es_data:
```

### 10. Recording Rules for Dashboard Performance

```yaml
groups:
  - name: app_recording_rules
    interval: 30s
    rules:
      # Pre-compute request rate by service — faster dashboard queries
      - record: app:http_requests:rate5m
        expr: sum by (service, method, status) (rate(http_requests_total[5m]))

      # Pre-compute error rate percentage
      - record: app:http_error_rate:ratio5m
        expr: |
          sum by (service) (rate(http_requests_total{status=~"5.."}[5m]))
          / sum by (service) (rate(http_requests_total[5m]))

      # Pre-compute p99 latency
      - record: app:http_latency:p99
        expr: |
          histogram_quantile(0.99,
            sum by (service, le) (rate(http_request_duration_seconds_bucket[5m]))
          )

      # Availability SLO — used in SLO dashboards
      - record: slo:service:availability
        expr: |
          sum(rate(http_requests_total{status=~"2.."}[30m]))
          / sum(rate(http_requests_total[30m]))
```

---

## 🧪 Hands-on Projects

### Project 1: Deploy a Complete Prometheus + Grafana Stack

**Goal**: Build a production-like monitoring stack from scratch.

**Step-by-step**:

1. Deploy Prometheus using Docker Compose (use the compose file above)
2. Configure Node Exporter on 3 Linux servers; add them to Prometheus scrape config
3. Install and configure `mysqld_exporter` and `postgres_exporter` for database metrics
4. Create a custom Prometheus exporter in Python/Go that exposes a business metric (e.g., order count)
5. Import community Grafana dashboards for Node Exporter (ID: 1860) and MySQL (ID: 7362)
6. Build a custom dashboard: golden signals (latency, traffic, errors, saturation) for your app
7. Configure Alertmanager with Slack integration; set up a routing tree by team
8. Write 3 alerting rules: high error rate, low disk space, high CPU
9. Trigger each alert; verify the notification arrives in Slack with the correct runbook link
10. Set up recording rules for your top 5 most-used dashboard queries

**Verification**: All metrics visible in Grafana; alerts fire and notify correctly; dashboard loads in <2 seconds.

---

### Project 2: ELK Stack for Centralized Logging

**Goal**: Aggregate logs from multiple servers into Elasticsearch and build Kibana dashboards.

**Step-by-step**:

1. Deploy Elasticsearch + Kibana + Filebeat using Docker Compose
2. Configure Filebeat on application servers to ship `/var/log/app/*.log` to Logstash
3. Set up Logstash with Grok patterns to parse application logs (JSON preferred)
4. Create index patterns in Kibana; build a Discover view filtered to ERROR-level logs
5. Create a Kibana dashboard: error count over time, top error messages, errors by service
6. Configure Elasticsearch ILM: hot phase (0-7 days), warm (7-30 days), delete (30+ days)
7. Set up Watcher (or ElastAlert) to alert on >100 ERROR logs in 5 minutes
8. Simulate a log spike; verify Elasticsearch doesn't fall over (configure circuit breaker settings)
9. Bonus: add APM (Application Performance Monitoring) with Elastic APM Server

**Verification**: Logs from all servers appear in Kibana within 5 seconds; dashboard shows meaningful error trends.

---

### Project 3: Distributed Tracing with OpenTelemetry + Jaeger

**Goal**: Instrument a microservices application with traces and visualize them in Jaeger.

**Step-by-step**:

1. Deploy Jaeger all-in-one and OTel Collector using Docker Compose
2. Create 2 sample microservices (Python Flask or Node.js Express) that call each other
3. Add OpenTelemetry auto-instrumentation to both services
4. Configure OTLP exporter to send traces to OTel Collector
5. Generate traffic: use `curl` or `wrk` to hit the frontend service
6. Open Jaeger UI; find a trace; analyze the trace graph (which service is slow?)
7. Add a manual child span for a slow database query; add tags (user_id, query_type)
8. Correlate traces with logs: add `trace_id` and `span_id` to application log format
9. Configure tail-based sampling in OTel Collector (keep all error traces, 5% of successes)
10. Document: how you'd use traces to debug a 500ms p99 latency spike

**Verification**: Traces visible in Jaeger; each request shows the full service call chain; slow spans are identifiable.

---

## 🔧 Common Troubleshooting

### Scenario 1: Prometheus High Memory Usage / OOM Kills

**Symptoms**: Prometheus pod/process gets OOM-killed; restarts frequently.

**Diagnosis**:
```bash
# Check Prometheus memory usage
curl http://localhost:9090/api/v1/status/runtimeinfo | jq

# Check series cardinality — the #1 cause of OOM
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data.headStats'

# Find high-cardinality metrics
curl -s 'http://localhost:9090/api/v1/label/__name__/values' | jq -r '.data[]' | head -20
```

**Solutions**:
- Add `metric_relabel_configs` to drop high-cardinality labels:
```yaml
metric_relabel_configs:
  - source_labels: [user_id]
    regex: '.+'
    action: labeldrop
```
- Increase `--storage.tsdb.retention.time` judiciously; shorter retention = less memory
- Use `--storage.tsdb.max-block-chunk-segment-size` to control memory usage
- Consider federating or using Thanos/Mimir for long-term storage

---

### Scenario 2: Grafana Dashboard is Slow (Takes >10s to Load)

**Symptoms**: Dashboard panels load slowly or time out.

**Diagnosis**:
```bash
# Check which queries are slow — look at query execution time in Prometheus UI
# Open Prometheus UI → Graph → run the query → check "Time" at bottom

# Check if recording rules are in place for expensive queries
ls /etc/prometheus/rules/   # Should have recording rules for dashboard queries
```

**Solutions**:
- Create recording rules for all expensive panel queries (see example 10 above)
- Reduce dashboard time range (30d → 7d) or decrease scrape interval (15s → 30s or 60s)
- Use `$__rate_interval` instead of hard-coded `[5m]` in Grafana panel queries — handles variable scrape intervals correctly
- Limit the number of series returned: use `topk()` or `avg by()` to reduce data points
- Enable Grafana dashboard caching in Grafana settings

---

### Scenario 3: Elasticsearch Cluster Status Red / Yellow

**Symptoms**: Kibana shows "Cluster Status: Red"; some indices have unassigned shards.

**Diagnosis**:
```bash
# Check cluster health
curl -X GET "localhost:9200/_cluster/health?pretty"

# Find unassigned shards
curl -X GET "localhost:9200/_cat/shards?h=index,shard,prirep,state,unassigned.reason" | grep UNASSIGNED

# Check disk space — most common cause
curl -X GET "localhost:9200/_cat/allocation?v"
```

**Solutions**:
- **Yellow**: Replica shards unassigned (single-node cluster) — set `number_of_replicas: 0` or add nodes
- **Red**: Primary shards unassigned — usually disk space. Free up disk or add nodes
- Increase disk watermark if needed:
```json
PUT _cluster/settings
{
  "transient": {
    "cluster.routing.allocation.disk.watermark.low": "85%",
    "cluster.routing.allocation.disk.watermark.high": "90%"
  }
}
```
- If a node is truly lost: allocate empty primaries (data loss) with `cluster.routing.allocation.enable: all`

---

### Scenario 4: Alertmanager Not Sending Notifications

**Symptoms**: Alerts fire in Prometheus but no Slack/PagerDuty notification arrives.

**Diagnosis**:
```bash
# Check Alertmanager UI — are alerts reaching Alertmanager?
open http://localhost:9093  # Check "Alerts" page

# Check Alertmanager logs
docker logs alertmanager | grep -i "notify"

# Verify route matching — use Amtool
amtool config routes test --config.file=alertmanager.yml --tree
```

**Solutions**:
- Verify `alertmanager` address in `prometheus.yml` matches actual Alertmanager address
- Check routing tree: alerts must match a route to reach a receiver
- Verify Slack webhook URL is correct and Slack app has permissions
- Check `group_wait` and `group_interval` — notifications are batched, not sent immediately
- Use `amtool alert add` to manually trigger a test alert and verify the pipeline

---

### Scenario 5: Logstash Pipeline Stalled / High Queue Depth

**Symptoms**: Logs aren't appearing in Elasticsearch; Logstash has high memory usage.

**Diagnosis**:
```bash
# Check Logstash pipeline status
curl -X GET "localhost:9600/_node/pipelines?pretty"

# Check queue depth (if using persistent queues)
ls -lh /var/lib/logstash/queue/

# Check Logstash JVM heap
jstat -gcutil $(pgrep -f logstash) 1000
```

**Solutions**:
- Increase Logstash heap in `jvm.options`: `-Xms4g -Xmx4g` (set to 50% of available RAM, max 32GB)
- Enable persistent queues to handle ingestion spikes:
```yaml
queue.type: persisted
queue.max_bytes: 4gb
```
- Reduce batch size if Logstash is overwhelmed: `pipeline.batch.size: 125` (default 125, reduce to 50)
- Check Elasticsearch is not the bottleneck: check ES indexing rate and circuit breaker stats

---

## 💼 Interview Questions

### Q1: Explain the difference between metrics, logs, and traces — and when you'd use each.

**Answer**: **Metrics** are numerical measurements over time — they tell you *what* is happening (error rate is 5%, CPU is at 90%). Use them for alerting and dashboards. **Logs** are timestamped text records — they tell you *why* something happened ("Database connection pool exhausted at 14:32:01"). Use them for debugging after an alert fires. **Traces** track a request across service boundaries — they tell you *where* time is spent (the `CheckoutService` took 800ms, and 600ms was in the `PaymentService` call). Use them for performance debugging in microservices. In practice, I always start with metrics (broad overview), then use logs to drill into specific errors, and traces when the issue spans multiple services.

---

### Q2: Why does Prometheus use a pull model, and what are the drawbacks?

**Answer**: Prometheus pulls metrics from targets because it's simpler to operate: targets don't need to know where Prometheus is, firewall rules are easier (Prometheus initiates connections), and you can manually curl a `/metrics` endpoint to debug. The main drawbacks: (1) short-lived jobs (batch tasks) that disappear before Prometheus scrapes them — solved with Pushgateway (though Pushgateway has its own problems); (2) Prometheus needs network access to all targets — in network-segmented environments this requires careful planning; (3) if Prometheus falls behind, scrapes are skipped — at very high scale, push-based (Victoria Metrics, InfluxDB) can be more efficient. I generally prefer pull for service monitoring and push (via OTel Collector) for short-lived batch jobs.

---

### Q3: How do you avoid alert fatigue, and what's your philosophy on paging?

**Answer**: My rule: if it pages, it's urgent, actionable, and the on-call engineer can actually fix it. Specifically: (1) Only page on symptoms that affect users (error rate > 1%, latency p99 > SLO), never on causes ("CPU high" is a cause, not necessarily a symptom). (2) Use SLO-based alerting — page on error budget burn rate, not on individual errors. (3) Require a runbook for every page — if there's no clear action, it's a Slack alert, not a page. (4) Regularly review.alert volume — if someone is getting >2 pages/week, something is wrong with the alerting rules. (5) Use warning-level alerts for "something needs attention soon" and critical only for "users are affected now."

---

### Q4: Explain histogram_quantile() and why it's better than averaging latencies.

**Answer**: `histogram_quantile(0.99, rate(bucket[5m]))` calculates the p99 latency from Prometheus histogram buckets. This matters because averages are meaningless for latency — if 99% of requests take 10ms but 1% take 5 seconds, the average might be 50ms, which looks fine but hides a terrible user experience for that 1%. p99 (or p95, p999) tells you the worst-case experience of your percentile of users. Histograms work by counting requests into predetermined buckets (e.g., 10ms, 50ms, 100ms, 500ms, 1000ms), and `histogram_quantile()` interpolates between bucket boundaries. Important: you must configure appropriate bucket boundaries for your latency SLO — if your SLO is 200ms, ensure you have a bucket at 200ms.

---

### Q5: How would you design a monitoring system for a globally distributed application?

**Answer**: Multi-region monitoring requires: (1) **Local Prometheus per region** — don't try to centrally scrape across continents; latency and network partitions will break it. (2) **Global view via federation or Thanos** — use Thanos Sidecar + Query to get a unified query interface across regions. (3) **Regional alerting** — each region's Alertmanager handles local alerts; use inhibition rules so only the region owning the service pages. (4) **Synthetic monitoring from multiple locations** — use Blackbox Exporter or commercial tools (Pingdom, Datadog Synthetics) to check each region from multiple global points. (5) **Tag everything with `region` and `datacenter` labels** — this is critical for debugging ("is the issue in all regions or just us-east-1?"). (6) **Centralized logging with region-aware retention** — ship logs to a central Elasticsearch cluster but tag with region; consider local ELK stacks for high-volume debug logs.

---

### Q6: What are the key Elasticsearch tuning parameters for a logging cluster?

**Answer**: The most impactful settings: (1) **JVM Heap**: set to 50% of RAM, never exceed 32GB (pointer compression breaks). (2) **Shard size**: target 10-50GB per shard; too many small shards = overhead, too large = slow recovery. (3) **Index template**: set `number_of_shards` based on data volume and `number_of_replicas` based on HA needs (usually 1). (4) **ILM policy**: automate hot→warm→cold→delete to manage storage cost. (5) **Refresh interval**: increase to 30s (from default 1s) if you don't need near-real-time search — reduces segment merge overhead. (6) **Circuit breaker**: `indices.breaker.total.limit: 95%` to prevent OOM. (7) **Disk watermark**: set to 85% (low) and 90% (high) to prevent running out of disk. In my experience, getting shard count right is the #1 performance tunable — use the Rollover API to manage this automatically.

---

### Q7: How do you implement SLO-based alerting (the Google SRE method)?

**Answer**: SLO-based alerting pages based on error budget burn rate rather than individual errors. Steps: (1) Define the SLI (e.g., "99% of requests succeed") and SLO (e.g., "99.9% availability over 30 days"). (2) Calculate the error budget: 100% - 99.9% = 0.1% = ~43 minutes/month. (3) Set up multi-window, multi-burn-rate alerts: fast burn (burn rate > 2x, 1-hour window — pages immediately) and slow burn (burn rate > 1x, 6-hour window — warning). (4) Implement in Prometheus alerting rules using the `error_budget_ratio` calculation. (5) When the error budget is exhausted, the team freezes non-essential releases until reliability improves. The key insight: not every error should page — only errors that will exhaust the error budget quickly. This dramatically reduces alert fatigue while maintaining reliability.

---

### Q8: Compare OpenTelemetry vs. traditional APM agents (New Relic, Datadog).

**Answer**: OpenTelemetry is vendor-neutral, open-source — you instrument once and can send data to any backend (Jaeger, Temp, Datadog, Honeycomb). Traditional APM agents lock you into a specific vendor. OTel also unifies metrics, logs, and traces into a single standard — before OTel, OpenTracing handled traces, OpenCensus handled metrics, and never the twain shall meet. The tradeoff: OTel is newer and evolving rapidly (some components still beta), while Datadog/New Relic agents are mature and "just work." My recommendation: use OTel for instrumentation (future-proof, no vendor lock-in), but you can still send the data to Datadog if you want their UI and alerting. The OTel Collectator is the key — it receives OTel-format data and can export to 20+ backends.

---

## 📈 Advanced Learning Path

```
Junior Ops Engineer
│
├── Master Prometheus + Grafana (this module)
│
▼
Senior Ops Engineer
│
├── Thanos / Mimir for long-term metrics storage
├── OpenTelemetry deep dive — custom instrumentation
├── Elasticsearch cluster administration (shard management, hot-warm architecture)
├── SLO engineering — implementing Google SRE monitoring practices
│
▼
Platform / SRE
│
├── Building self-service observability platforms for engineering teams
├── eBPF-based observability (Cilium, Pixie, Deepflow)
├── Profiling and continuous profiling (Pyroscope, Parca)
├── Chaos engineering integration with observability (Chaos Mesh + observability)
│
▼
Architect
│
├── Multi-region observability architecture
├── Next-gen observability (eBPF, OpenMetrics, Prometheus 3.0)
├── Contributing to Prometheus / OpenTelemetry projects
└── Building observability culture (beyond tools — processes, SLO reviews)
```

**Next steps after this module**:
1. Set up Thanos for long-term Prometheus storage — understand object storage backends (S3, GCS)
2. Learn eBPF observability — Cilium Hubble for K8s network observability
3. Implement continuous profiling with Pyroscope — understand CPU and memory profiling
4. Study the Google SRE books Chapters 6 (Monitoring) and 15 (Alerting) — they're free and foundational
5. Build a personal observability project: monitor your home lab with Prometheus + Grafana + Alertmanager

---

[← Back to English Home](../README.md)
