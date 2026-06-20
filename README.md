# <div align="center">⚙️ Ops Engineering Roadmap</div>

<div align="center">

**From zero to architect · Full-stack learning path for Ops / DevOps / SRE**

[![Stars](https://img.shields.io/github/stars/vinson-lee01/ops-engineering-roadmap?style=flat&label=Star)](https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers)
[![Forks](https://img.shields.io/github/forks/vinson-lee01/ops-engineering-roadmap?style=flat&label=Fork)](https://github.com/vinson-lee01/ops-engineering-roadmap/network/members)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green?style=flat&logo=creative-commons&logoColor=white)](https://creativecommons.org/licenses/by-sa/4.0/)

</div>

---

## Why this roadmap

Most ops learning paths list tool names but don't tell you **what order to learn**, **how deep to go**, or **how things connect** in real work.

This roadmap comes from hands-on practice at cloud vendors + internet companies, organized into three stages:

```
Can work independently → Can design architecture → Can define team standards
```

Each module marks **the depth actually used in production** — not a textbook table of contents.

| Dimension | This Roadmap |
|-----------|-------------|
| Language | **CN & EN maintained separately**, not machine-translated |
| Content | **15KB+ per module** with real production notes |
| Difference | CN: Aliyun/TencentCloud/Compliance/Base-lining · EN: AWS/GCP/SRE Book体系 |

---

## Learning Path

```
Foundation (Mo 1-3)          Growth (Mo 4-9)              Advanced (Mo 10-18)
┌──────────────┐             ┌──────────────────┐         ┌───────────────────┐
│ Linux Basics  │ ──────────▶ │ Docker / K8s     │ ──────▶ │ Architecture      │
│ Shell Script  │             │ CI/CD Pipeline   │         │ SLO System        │
│ Network/DNS   │             │ Prometheus Stack │         │ Multi-cloud/FinOps │
│ Nginx Deploy  │             │ ELK Logging      │         │ Service Mesh      │
└──────────────┘             └──────────────────┘         └───────────────────┘
```

> Each stage ends with **verifiable deliverables** — not "learned", but "can build".

---

# <div align="center">🇨🇳 中文版 · CN Version</div>

> **适用场景**：国内企业运维 · 应届求职 · 国产云环境（阿里云 / 腾讯云 / 华为云）· 等保合规 / 基线核查

<div align="center">

[进入中文版目录 →](./CN_Ops_Roadmap/)

</div>

| # | 模块 | 核心内容 | 关键产出 |
|---:|------|---------|---------|
| 01 | [Linux 基础](./CN_Ops_Roadmap/01_Linux_Basics/) | 系统管理 · 文件权限 · 进程管理 · 内核参数调优 · systemd | 能独立管理 50+ 台服务器的日常运维 |
| 02 | [Shell 编程](./CN_Ops_Roadmap/02_Shell_Scripting/) | Bash 编程 · awk/sed/grep 文本处理 · crontab 自动化 · 脚本健壮性 | 写出生产级自动化脚本，覆盖日志轮转 / 备份 / 告警 |
| 03 | [网络基础](./CN_Ops_Roadmap/03_Network_Basics/) | TCP/IP 协议栈 · DNS 解析链路 · iptables/firewalld · tcpdump/wireshark 抓包 | 排查网络延迟 / 连接超时 / DNS 劫持类故障 |
| 04 | [Docker 容器](./CN_Ops_Roadmap/04_Container_Docker/) | 镜像构建优化 · Dockerfile 最佳实践 · Compose 编排 · 网络 & 存储驱动 | 从零搭建容器化应用，镜像体积缩减 60%+ |
| 05 | [Nginx 实战](./CN_Ops_Roadmap/05_Web_Server_Nginx/) | 反向代理 · 负载均衡算法 · HTTPS / HTTP2 · 性能调优 · access_log 分析 | 承载万级 QPS 的 Web 接入层 |
| 06 | [MySQL 数据库](./CN_Ops_Roadmap/06_Database_MySQL/) | SQL 调优 · 主从复制 / GTID · 备份策略（逻辑 / 物理）· 慢查询定位 | 设计数据库高可用方案，恢复能力验证通过 |
| 07 | [Kubernetes](./CN_Ops_Roadmap/07_Container_Orchestration_K8s/) | 架构原理 · Pod 生命周期 · Deployment / StatefulSet · Service / Ingress · PV & 存储 | 在 K8s 上跑起一套有状态服务（含数据库）|
| 08 | [CI/CD 流水线](./CN_Ops_Roadmap/08_CICD_Jenkins_GitLab/) | Pipeline as Code · GitLab CI / Jenkinsfile · 制品管理 · 安全扫描卡点 | 代码提交到上线全自动化，耗时 < 10 分钟 |
| 09 | [监控体系](./CN_Ops_Roadmap/09_Monitoring_ElasticStack/) | Prometheus + Grafana · 指标设计 · 告警分级 / 抑制 / 静默 · ELK 日志 | 故障发现时间 MTTD < 5 分钟，根因定位有据可查 |
| 10 | [公有云 & 云原生](./CN_Ops_Roadmap/10_Cloud_Native/) | 阿里云/腾讯云实战 · Terraform IaC · Ansible 配置管理 · **等保2.0合规** · **国产化替代** · **基线扫描** | 用阿里云/腾讯云搭建符合等保三级要求的架构 |
| 11 | [SRE 工程化](./CN_Ops_Roadmap/11_SRE_Principles_Practices/) | SLO / SLI / SLA 定义 · Error Budget · 故障复盘（5 Whys）· 容量规划 | 建立团队可用性目标体系和复盘机制 |
| 12 | [Terraform IaC](./CN_Ops_Roadmap/12_IaC_Terraform/) | HCL 语言 · Resource / Data Source · Provider 抽象 · State 管理 · 模块化 | 基础设施代码化，一次 review 即可知变更全貌 |

---

# <div align="center">🌍 English Version</div>

> **For**: Site Reliability Engineers · Platform Engineers · DevOps Practitioners · Cloud-native teams working with AWS / GCP / Azure

<div align="center">

[Enter EN directory →](./EN_Global_SRE/)

</div>

| # | Module | Key Topics | What You Can Build |
|---:|--------|-----------|-------------------|
| 01 | [Linux Basics](./EN_Global_SRE/01_Linux_Fundamentals/) | System administration · Permissions · Process management · Kernel tuning · systemd | Manage 50+ production servers independently |
| 02 | [Shell Scripting](./EN_Global_SRE/03_Shell_Automation/) | Bash programming · Text processing (awk/sed/grep) · Automation patterns · Defensive scripting | Production-grade automation scripts for rotation / backup / alerting |
| 03 | [Networking](./EN_Global_SRE/02_Networking/) | TCP/IP stack · DNS resolution chain · firewalls · Packet analysis (tcpdump) | Troubleshoot latency / timeout / DNS issues at protocol level |
| 04 | [Docker](./EN_Global_SRE/04_Container_Docker/) | Image optimization · Dockerfile best practices · Compose · Network & storage drivers | Containerize applications with 60%+ image size reduction |
| 05 | [Nginx](./EN_Global_SRE/07_Web_Servers/) | Reverse proxy · Load balancing algorithms · HTTPS / HTTP2 · Performance tuning | Web tier handling 10k+ QPS |
| 06 | [MySQL](./EN_Global_SRE/09_Database/) | Query optimization · Replication / GTID · Backup strategies · Slow query analysis | Design HA database solution with verified recovery capability |
| 07 | [Kubernetes](./EN_Global_SRE/05_Kubernetes/) | Architecture · Pod lifecycle · Deployments / StatefulSets · Services / Ingress · Persistence | Run stateful workloads on K8s (including databases) |
| 08 | [CI/CD](./EN_Global_SRE/06_CI_CD/) | Pipeline as Code · GitLab CI / Jenkinsfile · Artifact management · Security gates | Full automated deploy pipeline, sub-10-minute lead time |
| 09 | [Monitoring](./EN_Global_SRE/08_Monitoring_Observability/) | Prometheus + Grafana · Metric design · Alert routing / silencing / inhibition · ELK stack | MTTD < 5 min, root cause traceable from metrics and logs |
| 10 | [Cloud Native & IaC](./EN_Global_SRE/10_Cloud_Native_IaC/) | AWS / Azure / GCP实战 · Terraform · Ansible · Service Mesh · FinOps | Production-grade multi-cloud infrastructure |
| 11 | [SRE Handbook](./EN_Global_SRE/11_SRE_Handbook/) | **SLO/SLI Engineering** · Incident Command System · Blameless Postmortem · On-call Excellence · Toil Elimination · Chaos Engineering · Capacity Planning | Establish availability targets, error budgets, and blameless culture |
| 12 | [Interview Prep](./EN_Global_SRE/12_Interview_Prep/) | Behavioral questions · System design · Technical deep-dives · Compensation negotiation | Confidently pass SRE interviews at FAANG-tier companies |

---

## Resources

| Type | Description | Link |
|------|------------|------|
| 📖 Books | Curated reading list for Ops / SRE / Cloud-native | [View List](./resources/books.md) |
| 🌐 Communities | Active technical communities & forums | [Communities](./resources/communities.md) |
| 🧪 Hands-on Labs | Free online lab environments | [Labs](./resources/online-labs.md) |
| 🔥 Discovery | Daily curated GitHub projects worth watching | [中文](./resources/trending_zh.md) · [English](./resources/trending_en.md) |

---

## Contributing

- Content issue or outdated info → [Open Issue](https://github.com/vinson-lee01/ops-engineering-roadmap/issues)
- Great project or resource to share → [Pull Request](https://github.com/vinson-lee01/ops-engineering-roadmap/pulls)

---

<div align="center">

If this roadmap helps you, consider giving it a Star ⭐

[![Stars](https://img.shields.io/github/stars/vinson-lee01/ops-engineering-roadmap?style=social)](https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers)

</div>
