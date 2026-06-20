# 🇨🇳 CN_Ops_Roadmap — 中文版运维学习路线图

> 面向国内运维工程师、SRE、DevOps 从业者，从零基础到架构师的完整学习路线。
> 所有资料均为本人实际使用过、筛选过的，拒绝「收藏即学会」的链接堆。

---

## 🗺️ 学习路线总览

```
入门（1-2 月）       进阶（3-6 月）        高级（7-12 月）      专家（13-24 月）
─────────────    ──────────────      ───────────────      ────────────────
Linux 基础          Docker 容器          Kubernetes            Service Mesh
Shell 脚本          Nginx 调优          CI/CD 流水线         多集群管理
计算机网络          MySQL/Redis          Prometheus 监控        FinOps 成本优化
Git 版本控制        ELK 日志平台         Terraform/IaC        SRE 体系建设
                                      阿里云/腾讯云实战
```

---

## 📚 模块导航

以下 12 个模块按学习顺序排列，建议不要跳级。每个模块都包含：视频教程、推荐书籍、在线资源、核心知识点、实战命令、故障排查、面试题目。

| # | 模块 | 一句话描述 | 学习周期 | 难度 |
|---|------|-----------|----------|------|
| 01 | **[Linux 基础](./01_Linux_Basics/)** | 一切的基础，不会 Linux 当不了运维 | 3-4 周 | ⭐ |
| 02 | **[计算机网络](./02_Networking/)** | 运维的网络基本功，TCP/IP 抓包必会 | 2-3 周 | ⭐⭐ |
| 03 | **[Shell 脚本](./03_Shell_Scripting/)** | 自动化运维的核心技能，Bash + Python | 2-3 周 | ⭐⭐ |
| 04 | **[Docker 容器](./04_Container_Docker/)** | 容器化入门，镜像、网络、存储 | 2-3 周 | ⭐⭐ |
| 05 | **[Kubernetes](./05_Kubernetes/)** | 容器编排，现代运维的核心技能 | 4-6 周 | ⭐⭐⭐ |
| 06 | **[CI/CD](./06_CI_CD/)** | 持续集成/部署，Jenkins、GitLab CI、GitHub Actions | 3-4 周 | ⭐⭐⭐ |
| 07 | **[Web 服务器](./07_Web_Servers/)** | Nginx 反向代理、负载均衡、性能调优 | 2-3 周 | ⭐⭐ |
| 08 | **[监控告警](./08_Monitoring/)** | Prometheus + Grafana，让系统看得见 | 3-4 周 | ⭐⭐⭐ |
| 09 | **[数据库管理](./09_Database/)** | MySQL、Redis、MongoDB，数据的生命线 | 3-4 周 | ⭐⭐⭐ |
| 10 | **[云原生](./10_Cloud_Native/)** | 阿里云、腾讯云、Terraform、Istio | 4-6 周 | ⭐⭐⭐⭐ |
| 11 | **[DevOps 实践](./11_DevOps_Practice/)** | DevOps 文化、GitOps、SRE 指标 | 2-3 周 | ⭐⭐ |
| 12 | **[面试突击](./12_Interview_Prep/)** | 面试题、场景设计、系统设计 | 持续 | ⭐⭐⭐ |

---

## 🎯 不同目标的学习重点

### 我想入行运维（零基础）
```
必学：01 → 02 → 03 → 04 → 07 → 08
选学：09（MySQL 基础）
目标：能独立管理服务器、搭建 LNMP、配置监控
```

### 我想进阶到高级运维
```
必学：05（K8s）→ 06（CI/CD）→ 08（深入）→ 10（云原生）
选学：11（DevOps 实践）
目标：能设计架构、主导容器化改造
```

### 我想转 SRE
```
必学：08（监控）→ 11（SRE 实践）→ 05（深入）→ 10（深入）
选学：03（Python 自动化）
目标：能建立 SRE 体系、制定 SLO、做故障复盘
```

### 我在准备面试
```
直奔：12（面试突击）
配合复习：01、05、08 的核心知识点
刷： [devops-exercises](https://github.com/bregman-arie/devops-exercises)
```

---

## 📺 中文优质视频教程 Top 10

以下是本人亲自筛选的 B 站优质教程，按质量排序：

| # | 教程 | UP 主 | 播放量 | 适合阶段 |
|---|------|-------|--------|---------|
| 1 | [韩顺平 Linux 教程](https://www.bilibili.com/video/BV1Sv411r7vd) | 韩顺平 | 1000万+ | 入门 |
| 2 | [狂神说 Docker](https://www.bilibili.com/video/BV1og4y1q7M4) | 狂神说 | 300万+ | 进阶 |
| 3 | [狂神说 K8s](https://www.bilibili.com/video/BV1GT4y1A756) | 狂神说 | 200万+ | 高级 |
| 4 | [尚硅谷 Jenkins](https://www.bilibili.com/video/BV1kJ411p7mA) | 尚硅谷 | 80万+ | 高级 |
| 5 | [黑马 Linux 运维](https://www.bilibili.com/video/BV1mW411i7Kn) | 黑马程序员 | 150万+ | 入门 |
| 6 | [IT 老齐 Nginx](https://www.bilibili.com/video/BV1ZJ411Y7M7) | IT 老齐 | 60万+ | 进阶 |
| 7 | [腾讯云开发者社区视频](https://www.bilibili.com/video/BV1Pe411Y7SF) | 腾讯云 | 30万+ | 高级 |
| 8 | [Lambda  DevOps](https://www.bilibili.com/video/BV1FJ411Y7MF) | Lambda | 20万+ | 高级 |
| 9 | [Prometheus 监控实战](https://www.bilibili.com/video/BV1Hg411t7qL) | 极客时间 | 10万+ | 高级 |
| 10 | [Python 自动化运维](https://www.bilibili.com/video/BV1gW41137qf) | 修炼之路 | 50万+ | 进阶 |

---

## 🌐 在线实验平台

不用自己买服务器，直接在线练：

| 平台 | 特点 | 费用 |
|------|------|------|
| [Killercoda](https://killercoda.com/) | K8s、Linux 免费实验环境 | 免费 |
| [Play with Docker](https://labs.play-with-docker.com/) | Docker 在线实验 | 免费 |
| [Play with K8s](https://labs.play-with-k8s.com/) | K8s 在线实验 | 免费 |
| [Qwiklabs](https://www.qwiklabs.com/) | GCP 实验，含金量高 | 付费 |
| [阿里云实验](https://www.aliyun.com/product/ecs/experiment) | 国内云实验 | 部分免费 |

---

## 💻 我的实验环境建议

学运维不动手等于没学。以下是我推荐的练习环境：

### 方案 A：本地虚拟机（免费）
- 软件：VirtualBox（免费）或 VMware Workstation
- 配置：3 台 CentOS 7/8 虚拟机，每台 2C4G
- 练习内容：Linux 基础、网络配置、Shell 脚本、Docker 单机

### 方案 B：云服务器（推荐，￥30/月）
- 平台：阿里云/腾讯云轻量应用服务器
- 配置：2C4G，3 台
- 优势：有公网 IP，可以练负载均衡、Nginx 反向代理等真实场景

### 方案 C：在线实验（最省事）
- Killercoda + Play with Docker/K8s
- 不用配置环境，打开网页就能练
- 适合碎片时间学习

---

## 🔗 相关资源

- [返回首页](../README.md)
- [English Version (EN_Global_SRE)](../EN_Global_SRE/)
- [GitHub 热门仓库实时发现](../resources/trending.md)
- [我的 CSDN 博客](https://jiubana1.blog.csdn.net/)

---

<p align="right">
  <sub>vinson-lee · 云域A</sub>
</p>
