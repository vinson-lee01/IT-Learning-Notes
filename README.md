<div align="center">

# ⚙️ Ops Engineering Roadmap

### 从零基础到生产架构师 · From Zero to Production Architect

<br>

[![GitHub stars](https://img.shields.io/github/stars/vinson-lee01/ops-engineering-roadmap?style=for-the-badge&logo=github&color=yellow)](https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vinson-lee01/ops-engineering-roadmap?style=for-the-badge&logo=github&color=blue)](https://github.com/vinson-lee01/ops-engineering-roadmap/network/members)

<br>

[![🇨🇳 中文版](https://img.shields.io/badge/%F0%9F%87%A8%F0%9F%87%B3_%E4%B8%AD%E6%96%87%E7%89%88-%E8%BF%9B%E5%85%A5%E4%B8%AD%E6%96%87%E7%89%88-blue?style=for-the-badge)](./CN_Ops_Roadmap/)
[![🌍 English](https://img.shields.io/badge/%F0%9F%8C%8D_English-Enter_EN_Version-orange?style=for-the-badge)](./EN_Global_SRE/)

</div>

---

## 📖 关于本路线图

市面上大多数运维学习路线只列工具名，不讲顺序、不讲深度、不讲在生产环境中怎么串联使用。

**这份路线图不一样：**

- ✅ **基于真实生产经验** — 来自云厂商和大型互联网公司的实际运维场景
- ✅ **明确学习深度** — 每个模块都标注了生产环境需要掌握的程度
- ✅ **可验证的产出** — 不是"学过了"，而是"能做出来"
- ✅ **中英双轨独立维护** — 不是机器翻译，针对国内外不同场景

### 18 个月后，你能做到

| 现在 | 18 个月后 |
|:---|:---|
| 故障靠猜 | MTTD < 5分钟，根因有据可查 |
| 手动登服务器 | 全自动化，提交代码即上线 |
| 不知道学什么 | 清晰的阶段目标 + 可验证的产出 |
| 面试说不清楚 | 能用真实项目讲架构决策 |

---

## 🗺️ 学习路径总览

<table>
<tr align="center">
<td width="30%">

**阶段一**
独立胜任日常工作
*Month 1~6*

</td>
<td width="5%">

→

</td>
<td width="30%">

**阶段二**
能够设计系统架构
*Month 7~12*

</td>
<td width="5%">

→

</td>
<td width="30%">

**阶段三**
定义团队标准与规范
*Month 13~18+*

</td>
</tr>
</table>

### 📚 阶段一：基础夯实（Month 1~6）

```
Linux 基础 → Shell 编程 → 网络基础 → Docker 容器 → Nginx 实战 → MySQL 数据库
```

**学习产出：** 独立管理 50+ 台服务器日常运维，能写生产级自动化脚本

### 🔧 阶段二：技术深化（Month 7~12）

```
Kubernetes → CI/CD 流水线 → 监控体系 → 公有云 & 云原生
```

**学习产出：** 代码提交到上线全自动化，耗时 < 10 分钟；MTTD < 5 分钟

### 🚀 阶段三：架构与工程化（Month 13~18+）

```
SRE 工程化 → Terraform IaC → 多云架构 → 团队规范建设
```

**学习产出：** 建立团队可用性目标体系与 SRE 文化

---

## 🇨🇳 中文版路线图

**适用场景：** 国内企业运维 · 应届求职 · 阿里云/腾讯云/华为云 · 等保合规 · 基线核查

**[→ 进入中文版完整目录](./CN_Ops_Roadmap/)**

<details>
<summary><b>点击展开完整模块列表（12个模块）</b></summary>

| # | 模块 | 核心内容 |
|:---|:---|:---|
| 01 | [Linux 基础](./CN_Ops_Roadmap/01_Linux_Basics/) | 系统管理 · 文件权限 · 进程管理 · 内核调优 |
| 02 | [Shell 编程](./CN_Ops_Roadmap/02_Shell_Scripting/) | Bash 编程 · awk/sed/grep · 自动化脚本 |
| 03 | [网络基础](./CN_Ops_Roadmap/03_Network_Basics/) | TCP/IP · DNS · iptables · 抓包分析 |
| 04 | [Docker 容器](./CN_Ops_Roadmap/04_Container_Docker/) | 镜像优化 · Dockerfile · Compose |
| 05 | [Nginx 实战](./CN_Ops_Roadmap/05_Web_Server_Nginx/) | 反向代理 · 负载均衡 · HTTPS 调优 |
| 06 | [MySQL 数据库](./CN_Ops_Roadmap/06_Database_MySQL/) | SQL 调优 · 主从复制 · 备份策略 |
| 07 | [Kubernetes](./CN_Ops_Roadmap/07_Container_Orchestration_K8s/) | 架构原理 · Pod 生命周期 · Service/Ingress |
| 08 | [CI/CD 流水线](./CN_Ops_Roadmap/08_CICD_Jenkins_GitLab/) | Pipeline as Code · GitLab CI · 安全扫描 |
| 09 | [监控体系](./CN_Ops_Roadmap/09_Monitoring_ElasticStack/) | Prometheus+Grafana · ELK 日志 |
| 10 | [公有云 & 云原生](./CN_Ops_Roadmap/10_Cloud_Native/) | 阿里云/腾讯云 · Terraform · **等保2.0** · **基线扫描** |
| 11 | [SRE 工程化](./CN_Ops_Roadmap/11_SRE_Principles_Practices/) | SLO/SLI/SLA · Error Budget · 故障复盘 |
| 12 | [Terraform IaC](./CN_Ops_Roadmap/12_IaC_Terraform/) | HCL · State 管理 · 模块化 |

</details>

---

## 🌍 English Version

**For:** Site Reliability Engineers · Platform Engineers · DevOps Practitioners · Cloud-native teams

**[→ Enter English Version](./EN_Global_SRE/)**

<details>
<summary><b>Click to expand full module list (12 modules)</b></summary>

| # | Module | Key Topics |
|:---|:---|:---|
| 01 | [Linux Fundamentals](./EN_Global_SRE/01_Linux_Fundamentals/) | System admin · Permissions · Processes · Kernel tuning |
| 02 | [Networking](./EN_Global_SRE/02_Networking/) | TCP/IP stack · DNS chain · Firewalls · Packet analysis |
| 03 | [Shell & Automation](./EN_Global_SRE/03_Shell_Automation/) | Bash scripting · Text processing · Cron patterns |
| 04 | [Docker](./EN_Global_SRE/04_Container_Docker/) | Image optimization · Dockerfile best practices · Compose |
| 05 | [Kubernetes](./EN_Global_SRE/05_Kubernetes/) | Architecture · Pod lifecycle · Deployments · Ingress |
| 06 | [CI/CD](./EN_Global_SRE/06_CI_CD/) | Pipeline as Code · GitLab CI · Security gates |
| 07 | [Nginx](./EN_Global_SRE/07_Web_Servers/) | Reverse proxy · Load balancing · HTTPS/HTTP2 |
| 08 | [Monitoring & Observability](./EN_Global_SRE/08_Monitoring_Observability/) | Prometheus+Grafana · Metric design · ELK |
| 09 | [MySQL](./EN_Global_SRE/09_Database/) | Query optimization · Replication · Backups |
| 10 | [Cloud Native & IaC](./EN_Global_SRE/10_Cloud_Native_IaC/) | AWS/GCP/Azure · Terraform · Service Mesh |
| 11 | [SRE Handbook](./EN_Global_SRE/11_SRE_Handbook/) | **SLO/SLI Engineering** · Incident Command · Blameless Postmortem |
| 12 | [Interview Prep](./EN_Global_SRE/12_Interview_Prep/) | System design · Tech deep-dives · Compensation |

</details>

---

## 🔥 每日发现 · Daily Discovery

> 每天自动发现 GitHub 上优质的运维/SRE/DevOps 相关项目

<div align="center">

**[🇨🇳 查看中文精选 →](./resources/trending_zh.md)** 　·　 **[🌍 View English Picks →](./resources/trending_en.md)**

</div>

---

## 📚 资源中心

| 资源 | 说明 | 链接 |
|:---|:---|:---|
| 📖 书单 | 运维/SRE/云原生精选书单 | [查看 →](./resources/books.md) |
| 🌐 社区 | 活跃技术社区与论坛 | [查看 →](./resources/communities.md) |
| 🧪 实验 | 免费在线实验环境 | [查看 →](./resources/online-labs.md) |

---

## 🤝 参与贡献

发现问题或有优质资源推荐？

- 🐛 提交问题 → [Open an Issue](https://github.com/vinson-lee01/ops-engineering-roadmap/issues)
- 💡 分享资源 → [Submit a PR](https://github.com/vinson-lee01/ops-engineering-roadmap/pulls)

---

<br>

<div align="center">

### ⭐ 如果这个路线图对你有帮助，欢迎 Star 支持

你的 Star 是我持续更新的动力 🙏

<br>

**Maintained by [vinson-lee](https://github.com/vinson-lee01)**
*CSDN 博客：[云域A](https://blog.csdn.net/weixin_49256755)*

</div>
