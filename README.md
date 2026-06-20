<p align="center">
  <a href="https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers"><img src="https://img.shields.io/badge/⭐%20Star%20这个仓库-blue?style=for-the-badge" alt="Star"></a>
  <img src="https://img.shields.io/badge/Status-每日更新-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/语言-中英双语-red?style=for-the-badge" alt="CN+EN">
  <img src="https://img.shields.io/badge/DevOps-Learning-2496ED?style=for-the-badge&logo=docker" alt="DevOps">
</p>

<div align="center">

# ⚙️ Ops Engineering Roadmap

### 从零基础到架构师：Linux · Docker · Kubernetes · CI/CD · 监控 · 云原生
#### 🇨🇳 中文版 + 🌍 English | 每日更新热门发现 | 500+ 精选资源

[![GitHub stars](https://img.shields.io/github/stars/vinson-lee01/ops-engineering-roadmap?style=social)](https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vinson-lee01/ops-engineering-roadmap?style=social)](https://github.com/vinson-lee01/ops-engineering-roadmap/network/members)

</div>

<p align="center">
  <a href="#-中文版">🇨🇳 中文版</a> ·
  <a href="#-english">🌍 English</a> ·
  <a href="#-学习路线图">🗺️ 路线图</a> ·
  <a href="#-必学资源">⭐ 必学资源</a> ·
  <a href="#-好书推荐">📚 书单</a> ·
  <a href="./CN_Ops_Roadmap/">📁 中文资料</a> ·
  <a href="./EN_Global_SRE/">📁 English</a> ·
  <a href="./resources/trending.md">📡 每日发现</a>
</p>

---

## 关于这个仓库

我是 vinson-lee，一名云运维从业者。

过去几年，从管几台物理机开始，一路做到几百台集群、容器化、K8s、CI/CD 全链路。踩过的坑太多，积累的笔记也不少。

这个仓库把我工作中学过、用过的好东西整理了出来，做成一份从零基础到架构师的学习路线图。每一份资料我都自己翻过一遍。

有国内最接地气的 B 站教程、中文文档，也有国外一线 SRE 团队的实战手册。中英文各自独立，根据你的情况挑着看就好。

### 📊 仓库数据

| 指标 | 说明 |
|------|------|
| **学习方向** | 12 大模块（中文） + 12 大模块（英文），覆盖运维全栈 |
| **资源数量** | 500+ 精选资源（教程、工具、书籍、社区） |
| **更新频率** | 每日更新 GitHub 热门发现 |
| **适用人群** | 运维工程师 / DevOps / SRE / 云架构师 / 转行自学 |

> 更多工作笔记见我的 CSDN 博客：[云域A](https://jiubana1.blog.csdn.net/)

---

## 🗺️ 学习路线图

这份路线图是我根据真实运维晋升路径整理的。每个阶段都有明确的目标和产出。

### 🏁 第一阶段：入门（第1-2月）

> Linux 基础 → Shell 脚本 → 计算机网络 → Git 版本控制
>
> **目标**：能独立管理 20 台服务器，写自动化脚本

### 🚀 第二阶段：进阶（第3-6月）

> Docker 容器 → Nginx/Tomcat → MySQL/Redis → Zabbix
>
> **目标**：能搭建完整的 Web 服务栈，处理常见故障

### 🔥 第三阶段：高级（第7-12月）

> Kubernetes → CI/CD → Prometheus+Grafana → Terraform
>
> **目标**：能设计高可用架构，主导容器化改造

### ☁️ 第四阶段：专家（第13-24月）

> Service Mesh → Multi-Cluster → FinOps → SRE 实践
>
> **目标**：能带团队，制定运维规范，把控系统稳定性

---

## 🇨🇳 中文版

**适合：** 国内运维、应届求职、转行自学

**特点：** 阿里云/腾讯云实战为主、B 站优质教程、掘金/CSDN 高分文章、国内大厂落地经验

| # | 模块 | 核心内容 | 学习周期 |
|---|------|---------|----------|
| 01 | **[Linux 基础](./CN_Ops_Roadmap/01_Linux_Basics/)** | CentOS/Ubuntu 系统管理、文件权限、进程管理、软件包管理、内核参数调优 | 3-4 周 |
| 02 | **[计算机网络](./CN_Ops_Roadmap/02_Networking/)** | TCP/IP 协议栈、DNS、HTTP/HTTPS、负载均衡、网络排障、抓包分析 | 2-3 周 |
| 03 | **[Shell 脚本](./CN_Ops_Roadmap/03_Shell_Scripting/)** | Bash 编程、awk/sed 文本处理、Python 运维脚本、自动化任务 | 2-3 周 |
| 04 | **[Docker 容器](./CN_Ops_Roadmap/04_Container_Docker/)** | 镜像构建、Dockerfile、Docker Compose、镜像仓库、容器网络 | 2-3 周 |
| 05 | **[Kubernetes](./CN_Ops_Roadmap/05_Kubernetes/)** | Pod/Service/Deployment、Ingress、Helm、Operator、集群管理 | 4-6 周 |
| 06 | **[CI/CD](./CN_Ops_Roadmap/06_CI_CD/)** | Jenkins Pipeline、GitLab CI、GitHub Actions、蓝绿/金丝雀部署 | 3-4 周 |
| 07 | **[Web 服务器](./CN_Ops_Roadmap/07_Web_Servers/)** | Nginx 反向代理、负载均衡、HTTPS 配置、性能调优、Tomcat 调优 | 2-3 周 |
| 08 | **[监控告警](./CN_Ops_Roadmap/08_Monitoring/)** | Prometheus + Grafana、Zabbix、ELK 日志平台、告警规则设计 | 3-4 周 |
| 09 | **[数据库管理](./CN_Ops_Roadmap/09_Database/)** | MySQL 安装配置、备份恢复、主从复制、Redis 缓存、MongoDB | 3-4 周 |
| 10 | **[云原生](./CN_Ops_Roadmap/10_Cloud_Native/)** | 阿里云/腾讯云实战、Terraform、Ansible、Istio、服务网格 | 4-6 周 |
| 11 | **[DevOps 实践](./CN_Ops_Roadmap/11_DevOps_Practice/)** | DevOps 文化、GitOps、ChatOps、安全加固、SRE 指标 | 2-3 周 |
| 12 | **[面试突击](./CN_Ops_Roadmap/12_Interview_Prep/)** | Linux 面试题、Docker/K8s 面试题、场景设计题、系统设计 | 持续 |

👉 **[进入中文版资料库 →](./CN_Ops_Roadmap/)**

---

## 🌍 English Version

**For:** DevOps/SRE engineers prepping for global roles or certifications

**Features:** AWS/Azure/GCP docs, RHCE prep, GitHub trending tools, hands-on SRE guides

| # | Module | Core Topics | Est. Time |
|---|--------|------------|----------|
| 01 | **[Linux Fundamentals](./EN_Global_SRE/01_Linux_Fundamentals/)** | System architecture, kernel, performance tuning, troubleshooting, LVM | 3-4 weeks |
| 02 | **[Networking](./EN_Global_SRE/02_Networking/)** | TCP/IP deep dive, DNS, HTTP/2 & HTTP/3, load balancing, network debugging | 2-3 weeks |
| 03 | **[Shell & Automation](./EN_Global_SRE/03_Shell_Automation/)** | Advanced Bash, Python for Ops, Go for infrastructure, cron automation | 2-3 weeks |
| 04 | **[Docker Containers](./EN_Global_SRE/04_Container_Docker/)** | Multi-stage builds, security best practices, orchestration, registry management | 2-3 weeks |
| 05 | **[Kubernetes](./EN_Global_SRE/05_Kubernetes/)** | Architecture, Operators, CRDs, RBAC, PodSecurity, Helm, GitOps | 4-6 weeks |
| 06 | **[CI/CD](./EN_Global_SRE/06_CI_CD/)** | Jenkins, GitHub Actions, ArgoCD, GitOps workflows, secrets management | 3-4 weeks |
| 07 | **[Web Servers](./EN_Global_SRE/07_Web_Servers/)** | Nginx internals, HAProxy, Traefik, API Gateway patterns, performance | 2-3 weeks |
| 08 | **[Monitoring & Observability](./EN_Global_SRE/08_Monitoring_Observability/)** | Prometheus, Grafana, ELK, OpenTelemetry, alerting strategy | 3-4 weeks |
| 09 | **[Database](./EN_Global_SRE/09_Database/)** | MySQL optimization, PostgreSQL, Redis clusters, MongoDB, backup strategies | 3-4 weeks |
| 10 | **[Cloud Native & IaC](./EN_Global_SRE/10_Cloud_Native_IaC/)** | Terraform, Ansible, Pulumi, Crossplane, Service Mesh, multi-cloud | 4-6 weeks |
| 11 | **[SRE Handbook](./EN_Global_SRE/11_SRE_Handbook/)** | Google SRE principles, SLI/SLO/SLA, incident management, postmortems | 3-4 weeks |
| 12 | **[Interview Prep](./EN_Global_SRE/12_Interview_Prep/)** | System design, troubleshooting scenarios, behavioral, cloud certifications | Ongoing |

👉 **[Enter English Resources →](./EN_Global_SRE/)**

---

### 📡 实时发现 — GitHub 热门仓库

除了上面的系统学习路线，我还定期整理 GitHub 上最新涌现的高质量开源仓库，覆盖 **DevOps、AI/MLOps、Linux、数据库、监控、云原生、安全、运维开发** 八大方向。

这些仓库按 Star 排序，都是近期活跃、文档完善、值得深入研究的项目。可以作为学习路线的补充，发现新工具和新思路。

👉 **[查看最新发现 →](./resources/trending.md)**

---

## ⭐ 我筛选的必学资源

以下是我从几百个资源里筛出来的精华，每个都亲自翻过。按「必看程度」排序。

### 🇨🇳 中文 5 个必看

| # | 资源 | Star | 简介 |
|---|------|------|------|
| 1 | [韩顺平 Linux 教程](https://www.bilibili.com/video/BV1Sv411r7vd) | B站 1000万+ | 国内 80% Linux 初学者的入门课，讲得细，适合零基础 |
| 2 | [guangzhengli/k8s-tutorials](https://github.com/guangzhengli/k8s-tutorials) | 5.8k | 最好的中文 K8s 教程，从 Pod 到 Helm 循序渐进 |
| 3 | [jaywcjlove/linux-command](https://github.com/jaywcjlove/linux-command) | 36k | Linux 命令速查手册，中文最全最方便，每天翻两遍 |
| 4 | [dunwu/linux-tutorial](https://github.com/dunwu/linux-tutorial) | 6.8k | Linux 运维全面教程，含 Shell 脚本实战，适合进阶 |
| 5 | [mingongge/BestSRE](https://github.com/mingongge/BestSRE) | 高赞 | 运维打怪升级进阶成神之路，面试题和实战都有 |

### 🌍 English Top 5

| # | Resource | Star | Description |
|---|----------|------|-------------|
| 1 | [bregman-arie/devops-exercises](https://github.com/bregman-arie/devops-exercises) | 82k | 2600+ DevOps 面试题，拿来就练，面试前必刷 |
| 2 | [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | 357k | 交互式 DevOps 路线图，可视化学习路径 |
| 3 | [bregman-arie/devops-resources](https://github.com/bregman-arie/devops-resources) | 9.5k | DevOps 全栈资源清单，覆盖工具、书籍、课程 |
| 4 | [dastergon/awesome-sre](https://github.com/dastergon/awesome-sre) | 13k | SRE 资源大合集，论文、博客、工具一应俱全 |
| 5 | [Google SRE Books](https://sre.google/books/) | 免费 | Google SRE 官方手册，网上能找到中文翻译版 |

---

## 📚 好书推荐

书是要读的，光看视频不行。以下这些是我觉得真正有价值的。

### 中文

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《鸟哥的 Linux 私房菜》 | 鸟哥 | 入门 | 经典中的经典，零基础首选，有些版本旧但原理不变 |
| 《Linux 运维之道 (第2版)》 | 丁明一 | 进阶 | 实战性强，有大量生产环境案例 |
| 《大型网站运维：从系统管理到 SRE》 | 肖力 | 进阶 | 从传统运维到 SRE 的转型指南，适合有经验的 |
| 《Kubernetes 权威指南》 | 龚正等 | 高级 | 国内 K8s 最系统的书，配合官网文档一起看 |
| 《Prometheus 监控实战》 | 罗梦宇 | 高级 | 国内少有的 Prometheus 深度好书，有中文案例 |

### English

| Title | Author | Level | Comment |
|-------|--------|-------|---------|
| Site Reliability Engineering | Betsy Beyer et al. (Google) | Intermediate | The SRE bible. Read it once a year. |
| The Site Reliability Workbook | Google SRE team | Intermediate | Companion to SRE book, with real examples. |
| Linux Performance | Brendan Gregg | Advanced | Performance tuning bible. Every serious ops engineer needs this. |
| The DevOps Handbook | Gene Kim et al. | Intermediate | Good for understanding DevOps culture and practices. |
| Kubernetes in Action (2nd Ed.) | Marko Lukša | Intermediate | Best K8s book bar none. Read it with a cluster handy. |
| Terraform: Up & Running (3rd Ed.) | Yevgeniy Brikman | Advanced | Infrastructure as Code done right. |
| Designing Data-Intensive Applications | Martin Kleppmann | Advanced | Not ops-specific but every senior engineer should read this. |

---

## 🛠️ 技术栈覆盖

这个仓库覆盖的技能栈，基本上也是一线互联网公司对运维/DevOps 工程师的要求。

<p align="center">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnu-bash&logoColor=white" alt="Bash">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" alt="Kubernetes">
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white" alt="Jenkins">
  <img src="https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white" alt="Nginx">
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white" alt="Prometheus">
  <img src="https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white" alt="Grafana">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white" alt="Terraform">
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat&logo=ansible&logoColor=white" alt="Ansible">
  <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white" alt="Go">
  <img src="https://img.shields.io/badge/ELK-005571?style=flat&logo=elastic-stack&logoColor=white" alt="ELK">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white" alt="AWS">
  <img src="https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoft-azure&logoColor=white" alt="Azure">
  <img src="https://img.shields.io/badge/GCP-4285F4?style=flat&logo=google-cloud&logoColor=white" alt="GCP">
</p>

---

## 💡 学习建议

1. **不要跳阶段**。Linux 不熟就别碰 K8s，基础不牢地动山摇。
2. **边学边练**。每学一个命令就在服务器上跑一遍，光看不练等于没看。
3. **搭一套自己的实验环境**。用虚拟机或云服务器，把学到的东西都部署一遍。
4. **遇到问题先自己排查**。学会看日志、查文档，这是运维最核心的能力。
5. **关注社区动态**。GitHub Trending、掘金、InfoQ 每天刷一刷。
6. **英语要跟上**。好的文档和开源项目大多是英文的。

---

## 📝 关于

有计划持续更新。GitHub 热门仓库我会定期浏览，把有价值的加到[实时发现](./resources/trending.md)页面。

发现链接挂了或者有好的资源推荐，直接提 Issue 或 PR，我会及时处理。

内容基于 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 共享，转载请注明出处。

---

<p align="center">
  <sub>vinson-lee（云域A）· 专注云运维，输出真实工作案例</sub>
</p>

---

> 如果这个仓库对你有帮助，欢迎 Star ⭐ — 这样每次更新你都能看到，也能让更多人发现这份路线。
>
> 有好的资源推荐？直接提 Issue 或 PR，一起把它做得更好。

<p align="center">
  <a href="https://github.com/vinson-lee01/ops-engineering-roadmap/stargazers">
    <img src="https://img.shields.io/github/stars/vinson-lee01/ops-engineering-roadmap?style=social" alt="Stars">
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/vinson-lee01/ops-engineering-roadmap/network/members">
    <img src="https://img.shields.io/github/forks/vinson-lee01/ops-engineering-roadmap?style=social" alt="Forks">
  </a>
</p>
