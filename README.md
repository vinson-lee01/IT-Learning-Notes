<div align="center">

# ⚙️ Ops Engineering Roadmap

### From Zero to Production Architect
### A Comprehensive Learning Path for Ops · DevOps · SRE

<br>

[![GitHub stars](https://img.shields.io/github/stars/vinson-lee01/ops-engineering-roadmap?style=for-the-badge&logo=github&color=yellow)](https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vinson-lee01/ops-engineering-roadmap?style=for-the-badge&logo=github&color=blue)](https://github.com/vinson-lee01/ops-engineering-roadmap/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/vinson-lee01/ops-engineering-roadmap?style=for-the-badge&logo=github&color=green)](https://github.com/vinson-lee01/ops-engineering-roadmap)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green?style=for-the-badge&logo=creative-commons&logoColor=white)](https://creativecommons.org/licenses/by-sa/4.0/)

<br>

[![CN Version](https://img.shields.io/badge/🇨🇳%20中文版-跳转到中文版-blue?style=for-the-badge)](./CN_Ops_Roadmap/README.md)
[![EN Version](https://img.shields.io/badge/🌍%20English%20Version-Go%20to%20EN-orange?style=for-the-badge)](./EN_Global_SRE/README.md)

</div>

---

## 📖 About This Roadmap

Most online learning paths for operations engineers share a common problem: **they list tools without explaining the order, depth, or how they connect in real production environments.**

This roadmap is built differently. It is written from hands-on experience at cloud vendors and large-scale internet companies, structured around three progressive stages:

<div align="center">

```
         Stage 1                    Stage 2                   Stage 3
┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────┐
│   Can work          │   │   Can design        │   │   Can define        │
│   independently     │──▶│   architecture       │──▶│   team standards    │
└─────────────────────┘   └─────────────────────┘   └─────────────────────┘
```

</div>

Every module explicitly marks **the depth needed in real production work** — not a textbook table of contents.

| | |
|:--|:--|
| **Language** | CN & EN maintained independently — not machine-translated |
| **Content** | 15KB+ production notes per module |
| **CN Focus** | Aliyun / Tencent Cloud / Compliance / Baseline / Localization |
| **EN Focus** | AWS / GCP / SRE Book methodology / Global best practices |

---

## 🗺️ Learning Path Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Learning Timeline                           │
│                                                                     │
│  Month 1-3 (Foundation)          Month 4-9 (Growth)                 │
│  ┌──────────────────┐            ┌────────────────────────────────┐│
│  │ · Linux Basics    │           │ · Docker / K8s                   ││
│  │ · Shell Scripting │──────────▶│ · CI/CD Pipeline                 ││
│  │ · Networking      │           │ · Prometheus + Grafana           ││
│  │ · Nginx Deploy    │           │ · ELK Stack                      ││
│  └──────────────────┘           └────────────────────────────────┘│
│                                           │                         │
│                                           ▼                         │
│                                Month 10-18 (Advanced)                 │
│                                ┌────────────────────────────────┐   │
│                                │ · Architecture Design           │   │
│                                │ · SLO / Error Budget System      │   │
│                                │ · Multi-cloud / FinOps           │   │
│                                │ · Service Mesh / Chaos Eng.      │   │
│                                └────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

> Each stage concludes with **verifiable deliverables** — not "studied", but "can build".

---

<div align="center">

# 🇨🇳 中文版

### 国内运维工程师完整成长路径

*适用：国内企业运维 · 应届求职 · 国产云（阿里云/腾讯云/华为云）· 等保合规 / 基线核查*

**[→ 进入中文版完整目录](./CN_Ops_Roadmap/)**

</div>

<table>
<tr>
  <td width="50"><strong>#</strong></td>
  <td width="220"><strong>模块</strong></td>
  <td><strong>核心内容</strong></td>
  <td width="260"><strong>学习产出</strong></td>
</tr>
<tr>
  <td align="center"><code>01</code></td>
  <td><a href="./CN_Ops_Roadmap/01_Linux_Basics/"><b>Linux 基础</b></a></td>
  <td>系统管理 · 文件权限 · 进程管理 · 内核调优 · systemd</td>
  <td>独立管理 50+ 台服务器日常运维</td>
</tr>
<tr>
  <td align="center"><code>02</code></td>
  <td><a href="./CN_Ops_Roadmap/02_Shell_Scripting/"><b>Shell 编程</b></a></td>
  <td>Bash 编程 · awk/sed/grep · crontab 自动化 · 脚本健壮性</td>
  <td>生产级自动化脚本（日志轮转/备份/告警）</td>
</tr>
<tr>
  <td align="center"><code>03</code></td>
  <td><a href="./CN_Ops_Roadmap/03_Network_Basics/"><b>网络基础</b></a></td>
  <td>TCP/IP · DNS 解析链路 · iptables · tcpdump/wireshark</td>
  <td>排查网络延迟/超时/DNS 劫持类故障</td>
</tr>
<tr>
  <td align="center"><code>04</code></td>
  <td><a href="./CN_Ops_Roadmap/04_Container_Docker/"><b>Docker 容器</b></a></td>
  <td>镜像优化 · Dockerfile 最佳实践 · Compose · 网络存储</td>
  <td>容器化应用，镜像体积缩减 60%+</td>
</tr>
<tr>
  <td align="center"><code>05</code></td>
  <td><a href="./CN_Ops_Roadmap/05_Web_Server_Nginx/"><b>Nginx 实战</b></a></td>
  <td>反向代理 · 负载均衡 · HTTPS/HTTP2 · 性能调优</td>
  <td>承载万级 QPS 的 Web 接入层</td>
</tr>
<tr>
  <td align="center"><code>06</code></td>
  <td><a href="./CN_Ops_Roadmap/06_Database_MySQL/"><b>MySQL 数据库</b></a></td>
  <td>SQL 调优 · 主从复制/GTID · 备份策略 · 慢查询</td>
  <td>设计 HA 数据库方案，恢复能力验证通过</td>
</tr>
<tr>
  <td align="center"><code>07</code></td>
  <td><a href="./CN_Ops_Roadmap/07_Container_Orchestration_K8s/"><b>Kubernetes</b></a></td>
  <td>架构原理 · Pod 生命周期 · Deployment · Service/Ingress</td>
  <td>在 K8s 上跑起有状态服务（含数据库）</td>
</tr>
<tr>
  <td align="center"><code>08</code></td>
  <td><a href="./CN_Ops_Roadmap/08_CICD_Jenkins_GitLab/"><b>CI/CD 流水线</b></a></td>
  <td>Pipeline as Code · GitLab CI · 制品管理 · 安全扫描</td>
  <td>代码提交到上线全自动化，耗时 &lt; 10 分钟</td>
</tr>
<tr>
  <td align="center"><code>09</code></td>
  <td><a href="./CN_Ops_Roadmap/09_Monitoring_ElasticStack/"><b>监控体系</b></a></td>
  <td>Prometheus+Grafana · 指标设计 · 告警体系 · ELK 日志</td>
  <td>MTTD &lt; 5 分钟，根因定位有据可查</td>
</tr>
<tr>
  <td align="center"><code>10</code></td>
  <td><a href="./CN_Ops_Roadmap/10_Cloud_Native/"><b>公有云 &amp; 云原生</b></a></td>
  <td>阿里云/腾讯云 · Terraform IaC · <b>等保2.0</b> · <b>国产化替代</b> · <b>基线扫描</b></td>
  <td>搭建符合等保三级要求的云架构</td>
</tr>
<tr>
  <td align="center"><code>11</code></td>
  <td><a href="./CN_Ops_Roadmap/11_SRE_Principles_Practices/"><b>SRE 工程化</b></a></td>
  <td>SLO/SLI/SLA · Error Budget · 故障复盘 · 容量规划</td>
  <td>建立团队可用性目标体系和复盘机制</td>
</tr>
<tr>
  <td align="center"><code>12</code></td>
  <td><a href="./CN_Ops_Roadmap/12_IaC_Terraform/"><b>Terraform IaC</b></a></td>
  <td>HCL · Resource/Data Source · State 管理 · 模块化</td>
  <td>基础设施代码化，变更全貌一目了然</td>
</tr>
</table>

---

<div align="center">

# 🌍 English Version

### Complete SRE / DevOps Career Path

*For: Site Reliability Engineers · Platform Engineers · DevOps Practitioners · Cloud-native teams (AWS/GCP/Azure)*

**[→ Enter English Version](./EN_Global_SRE/)**

</div>

<table>
<tr>
  <td width="50"><strong>#</strong></td>
  <td width="260"><strong>Module</strong></td>
  <td><strong>Key Topics</strong></td>
  <td width="280"><strong>What You Build</strong></td>
</tr>
<tr>
  <td align="center"><code>01</code></td>
  <td><a href="./EN_Global_SRE/01_Linux_Fundamentals/"><b>Linux Fundamentals</b></a></td>
  <td>System admin · Permissions · Processes · Kernel tuning · systemd</td>
  <td>Manage 50+ production servers independently</td>
</tr>
<tr>
  <td align="center"><code>02</code></td>
  <td><a href="./EN_Global_SRE/03_Shell_Automation/"><b>Shell &amp; Automation</b></a></td>
  <td>Bash scripting · Text processing · Cron patterns · Defensive scripts</td>
  <td>Production-grade automation (rotation/backup/alerting)</td>
</tr>
<tr>
  <td align="center"><code>03</code></td>
  <td><a href="./EN_Global_SRE/02_Networking/"><b>Networking</b></a></td>
  <td>TCP/IP stack · DNS chain · Firewalls · Packet analysis</td>
  <td>Troubleshoot latency/timeout/DNS at protocol level</td>
</tr>
<tr>
  <td align="center"><code>04</code></td>
  <td><a href="./EN_Global_SRE/04_Container_Docker/"><b>Docker</b></a></td>
  <td>Image optimization · Dockerfile best practices · Compose</td>
  <td>Containerize apps with 60%+ image size reduction</td>
</tr>
<tr>
  <td align="center"><code>05</code></td>
  <td><a href="./EN_Global_SRE/07_Web_Servers/"><b>Nginx</b></a></td>
  <td>Reverse proxy · Load balancing · HTTPS/HTTP2 · Tuning</td>
  <td>Web tier handling 10k+ QPS</td>
</tr>
<tr>
  <td align="center"><code>06</code></td>
  <td><a href="./EN_Global_SRE/09_Database/"><b>MySQL</b></a></td>
  <td>Query optimization · Replication/GTID · Backups · Slow queries</td>
  <td>Design HA database with verified recovery</td>
</tr>
<tr>
  <td align="center"><code>07</code></td>
  <td><a href="./EN_Global_SRE/05_Kubernetes/"><b>Kubernetes</b></a></td>
  <td>Architecture · Pod lifecycle · Deployments · Ingress · Storage</td>
  <td>Run stateful workloads on K8s (including DBs)</td>
</tr>
<tr>
  <td align="center"><code>08</code></td>
  <td><a href="./EN_Global_SRE/06_CI_CD/"><b>CI/CD</b></a></td>
  <td>Pipeline as Code · GitLab CI · Artifact mgmt · Security gates</td>
  <td>Full automated deploy, sub-10-minute lead time</td>
</tr>
<tr>
  <td align="center"><code>09</code></td>
  <td><a href="./EN_Global_SRE/08_Monitoring_Observability/"><b>Monitoring &amp; Observability</b></a></td>
  <td>Prometheus+Grafana · Metric design · Alerting · ELK</td>
  <td>MTTD &lt; 5 min, root cause traceable</td>
</tr>
<tr>
  <td align="center"><code>10</code></td>
  <td><a href="./EN_Global_SRE/10_Cloud_Native_IaC/"><b>Cloud Native &amp; IaC</b></a></td>
  <td>AWS/GCP/Azure · Terraform · Ansible · Service Mesh · FinOps</td>
  <td>Production-grade multi-cloud infrastructure</td>
</tr>
<tr>
  <td align="center"><code>11</code></td>
  <td><a href="./EN_Global_SRE/11_SRE_Handbook/"><b>SRE Handbook</b></a></td>
  <td><b>SLO/SLI Engineering</b> · Incident Command · Blameless Postmortem · On-call · Toil Elimination · Chaos Engineering · Capacity Planning</td>
  <td>Establish availability targets, error budgets, blameless culture</td>
</tr>
<tr>
  <td align="center"><code>12</code></td>
  <td><a href="./EN_Global_SRE/12_Interview_Prep/"><b>Interview Prep</b></a></td>
  <td>Behavioral questions · System design · Tech deep-dives · Compensation</td>
  <td>Confidently pass SRE interviews at tier-1 companies</td>
</tr>
</table>

---

## 📚 Resources

<div align="center">

| Resource | Description | Link |
|:---|:---|:---|
| 📖 **Books** | Curated reading list for Ops / SRE / Cloud-native | [View →](./resources/books.md) |
| 🌐 **Communities** | Active technical communities & forums | [View →](./resources/communities.md) |
| 🧪 **Hands-on Labs** | Free online lab environments | [View →](./resources/online-labs.md) |
| 🔥 **Daily Discovery** | Curated GitHub projects worth watching | [中文 →](./resources/trending_zh.md) · [EN →](./resources/trending_en.md) |

</div>

---

## 🤝 Contributing

Found an issue or have a great resource to share?

- 🐛 **Report issues** → [Open an Issue](https://github.com/vinson-lee01/ops-engineering-roadmap/issues)
- 💡 **Share resources** → [Submit a PR](https://github.com/vinson-lee01/ops-engineering-roadmap/pulls)

---

<br>

<div align="center">

### ⭐ If this roadmap helps you, please consider giving it a Star

It takes a second and helps more people discover it.

<br>

[![Star this repo](https://img.shields.io/github/stars/vinson-lee01/ops-engineering-roadmap?style=social)](https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers)

<br><br>

<sub>Last curated: June 2026 &nbsp;|&nbsp; Maintained by <a href="https://github.com/vinson-lee01">@vinson-lee01</a></sub>

</div>
