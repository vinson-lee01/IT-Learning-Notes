# 12 · Interview Preparation

> Ace your DevOps/SRE interviews with these battle-tested questions and scenario walkthroughs.

---

## 📝 Top Topic Questions

### Linux
- Explain the Linux boot process (BIOS → GRUB → kernel → init)
- What happens when you type `ls -la` in a terminal?
- How does Linux manage memory (virtual memory, page cache, swapping)?
- Explain `strace`, `lsof`, `tcpdump` use cases
- How to troubleshoot a server with 100% CPU?

### Docker
- Docker image layers — how do they work?
- Difference between `CMD`, `ENTRYPOINT`, and `RUN`?
- How would you reduce a Docker image from 2GB to 100MB?
- Explain Docker networking modes (bridge, host, none, overlay)

### Kubernetes
- Walk through what happens when you `kubectl create deployment`
- How does a Service discover its Pods? (Endpoints + kube-proxy)
- How to troubleshoot a Pod stuck in `CrashLoopBackOff`?
- Explain RBAC: Roles, ClusterRoles, RoleBindings
- How does HPA (Horizontal Pod Autoscaler) work?

### Networking
- Detail a TCP three-way handshake and four-way teardown
- How does DNS resolution work end-to-end?
- What happens when you type `google.com` in your browser?
- Explain TLS 1.3 handshake

### System Design Scenarios
1. Design a system handling 1M requests/second
2. How to migrate a production database with zero downtime?
3. Design a global CDN infrastructure
4. How to scale a monolithic application to microservices?
5. Design a centralized logging platform for 1000+ servers

---

## 🌐 Top Interview Repos

| Resource | Link | Stars |
|----------|------|-------|
| devops-exercises | https://github.com/bregman-arie/devops-exercises | ⭐82k |
| System Design Primer | https://github.com/donnemartin/system-design-primer | ⭐275k |
| Coding Interview University | https://github.com/jwasham/coding-interview-university | ⭐305k |

---

## 💡 Pro Tips

- **STAR method**: Situation, Task, Action, Result — for behavioral questions
- **Draw diagrams**: System design questions need visuals
- **Ask clarifying questions**: Shows you think before building
- **Admit what you don't know**: Then explain how you'd find out

---

[← Back to English Home](../README.md)
