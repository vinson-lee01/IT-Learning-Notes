# 🌍 EN_Global_SRE — DevOps & SRE Learning Roadmap

> A complete learning path from zero to architect, for DevOps/SRE engineers targeting global roles and cloud-native certifications.
> All resources curated from personal experience — no "star-and-forget" link dumps.

---

## 🗺️ Learning Path Overview

```
Beginner (1-2 months)    Intermediate (3-6 months)    Advanced (7-12 months)    Expert (13-24 months)
───────────────────    ──────────────────────    ───────────────────────    ─────────────────────────
Linux Fundamentals      Docker Containers          Kubernetes                Service Mesh
Shell & Automation     Nginx/Web Servers         CI/CD Pipelines           Multi-Cluster Mgmt
Networking            MySQL/Redis               Prometheus Monitoring       FinOps & Cost Optimization
Git Version Control   ELK Stack                Terraform/IaC             SRE Practice & Culture
                                      AWS/GCP/Azure Practical
```

---

## 📚 Module Navigation

12 modules in learning order. Each includes: video courses, recommended books, online resources, core knowledge checklist, hands-on commands, troubleshooting guide, and interview questions.

| # | Module | One-liner | Est. Time | Difficulty |
|---|--------|-----------|----------|------------|
| 01 | **[Linux Fundamentals](./01_Linux_Fundamentals/)** | Foundation of everything. No Linux = no ops career. | 3-4 weeks | ⭐ |
| 02 | **[Networking](./02_Networking/)** | TCP/IP, DNS, HTTP — the networking bedrock. | 2-3 weeks | ⭐⭐ |
| 03 | **[Shell & Automation](./03_Shell_Automation/)** | Bash + Python + Go — automate al the things. | 2-3 weeks | ⭐⭐ |
| 04 | **[Docker Containers](./04_Container_Docker/)** | Containerization 101: images, networking, storage. | 2-3 weeks | ⭐⭐ |
| 05 | **[Kubernetes](./05_Kubernetes/)** | Container orchestration — the core modern ops skil. | 4-6 weeks | ⭐⭐⭐ |
| 06 | **[CI/CD](./06_CI_CD/)** | Jenkins, GitHub Actions, ArgoCD, GitOps workflows. | 3-4 weeks | ⭐⭐⭐ |
| 07 | **[Web Servers](./07_Web_Servers/)** | Nginx internals, HAProxy, Traefik, API Gateway patterns. | 2-3 weeks | ⭐⭐ |
| 08 | **[Monitoring & Observability](./08_Monitoring_Observability/)** | Prometheus + Grafana — make your system visible. | 3-4 weeks | ⭐⭐⭐ |
| 09 | **[Database](./09_Database/)** | MySQL, PostgreSQL, Redis, MongoDB — data's lifeline. | 3-4 weeks | ⭐⭐⭐ |
| 10 | **[Cloud Native & IaC](./10_Cloud_Native_IaC/)** | Terraform, Ansible, AWS/GCP, Service Mesh. | 4-6 weeks | ⭐⭐⭐⭐ |
| 11 | **[SRE Handbook](./11_SRE_Handbook/)** | Google SRE principles, SLI/SLO/SLA, incident mgmt. | 3-4 weeks | ⭐⭐⭐ |
| 12 | **[Interview Prep](./12_Interview_Prep/)** | System design, troubleshooting scenarios, behavioral Qs. | Ongoing | ⭐⭐⭐ |

---

## 🎯 Learning Focus by Goal

### I want to break into DevOps (zero background)
```
Must-learn: 01 → 02 → 03 → 04 → 07 → 08
Optional: 09 (MySQL basics)
Goal: Manage servers independently, deploy LNMP stack, configure monitoring.
```

### I want to advance to Senior DevOps
```
Must-learn: 05 (K8s) → 06 (CI/CD) → 08 (deep dive) → 10 (Cloud Native)
Optional: 11 (DevOps Practice)
Goal: Design architecture, lead containerization migration.
```

### I want to transition to SRE
```
Must-learn: 08 (Monitoring) → 11 (SRE Handbook) → 05 (deep) → 10 (deep)
Optional: 03 (Python automation)
Goal: Build SRE system, define SLOs, run blameless postmortems.
```

### I'm preparing for interviews
```
Go straight to: 12 (Interview Prep)
Review alongside: Core topics from 01, 05, 08
Practice: [devops-exercises](https://github.com/bregman-arie/devops-exercises)
```

---

## 📺 Top English Video Courses

Curated from personal experience. Al are highly recommended.

| # | Course | Platform | Instructor | Level |
|---|--------|----------|-----------|-------|
| 1 | [Linux Mastery](https://www.udemy.com/course/linux-mastery/) | Udemy | Jason Canon | Beginner |
| 2 | [Docker Mastery](https://www.udemy.com/course/docker-mastery/) | Udemy | Bret Fisher | Intermediate |
| 3 | [Kubernetes Mastery](https://www.udemy.com/course/kubernetes-mastery/) | Udemy | Bret Fisher | Advanced |
| 4 | [Terraform Associate Cert](https://www.udemy.com/course/terraform-associate/) | Udemy | Stephane Maarek | Intermediate |
| 5 | [Prometheus/Grafana](https://www.udemy.com/course/prometheus-grafana/) | Udemy | Alaeldin Abdo | Advanced |
| 6 | [AWS Solutions Architect](https://www.udemy.com/course/aws-certified-solutions-architect-associate/) | Udemy | Stephane Maarek | Intermediate |
| 7 | [SRE with Java Microservices](https://www.udemy.com/course/sre-java-microservices/) | Udemy | Vinoth Rathinam | Advanced |
| 8 | [Google SRE Book](https://sre.google/books/) | Free Online | Google SRE Team | Intermediate |
| 9 | [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way) | GitHub | Kelsey Hightower | Advanced |
| 10 | [CNCF Landscape](https://landscape.cncf.io/) | Interactive | CNCF | Reference |

---

## 🌐 Online Lab Platforms

No need to buy servers — practice online:

| Platform | Features | Cost |
|----------|----------|------|
| [Killercoda](https://killercoda.com/) | Free K8s, Linux, and DevOps labs | Free |
| [Play with Docker](https://labs.play-with-docker.com/) | Docker online lab | Free |
| [Play with K8s](https://labs.play-with-k8s.com/) | Kubernetes online lab | Free |
| [Qwiklabs](https://www.qwiklabs.com/) | GCP/AWS hands-on labs, high quality | Paid |
| [A Cloud Guru](https://acloudguru.com/) | Cloud certs + hands-on labs | Paid |
| [KodeKloud](https://kodekloud.com/) | DevOps hands-on labs, very practical | Paid |

---

## 💻 My Recommended Practice Environment

### Option A: Local VMs (Free)
- Software: VirtualBox (free) or VMware Workstation
- Setup: 3x CentOS 7/8 VMs, 2CPU/4GB each
- Practice: Linux basics, networking, Shell scripting, single-node Docker

### Option B: Cloud Servers (Recommended, ~$5/month)
- Provider: DigitalOcean / Linode / Vultr
- Setup: 3x 2CPU/4GB instances
- Advantage: Public IP — practice load balancing, Nginx reverse proxy, real-world scenarios

### Option C: Online Labs (Most Convenient)
- Killercoda + Play with Docker/K8s
- No environment setup — open browser and start practicing
- Best for碎片化时间学习

---

## 🔗 Related Resources

- [← Back to Home](../README.md)
- [中文版 (CN_Ops_Roadmap)](../CN_Ops_Roadmap/)
- [GitHub Trending Repos](../resources/trending.md)
- [My CSDN Blog (中文)](https://jiubana1.blog.csdn.net/)

---

<p align="right">
  <sub>vinson-lee · Cloud Ops Practitioner</sub>
</p>
