# 12 · Interview Prep

> This module helps you get the job — and negotiate the offer.
> Covers: technical questions, system design, behavioral questions, and salary negotiation.

---

## 🎯 Who is this for?

| Target | Focus |
|--------|-------|
| **Junior Ops (< 2 years)** | Linux basics, Shell scripting, basic Docker |
| **Mid-level (2-5 years)** | K8s, CI/CD, monitoring, incident response |
| **Senior (5+ years)** | System design, SRE practices, team leadership |
| **SRE-specific** | SLO/SLI, postmortems, toil reduction, capacity planning |

---

## 📋 Resume Tips (Before the Interview)

### What to include
- **Quantified impact**: "Reduced deployment time from 2 hours to 15 minutes" > "Set up CI/CD"
- **Technologies**: list specific tools (K8s, Terraform, Prometheus), not just "DevOps tools"
- **Incident examples**: "Led incident response for SEV-1 outage, reduced MTTR by 40%"
- **Projects**: link to GitHub (this repo counts!)

### Resume template (ops-specific)
```
[NAME]
[EMAIL] | [PHONE] | [LINKEDIN] | [GITHUB]

SKILLS
Linux · Docker · Kubernetes · CI/CD (Jenkins/GitHub Actions) · Prometheus/Grafana · Terraform

EXPERIENCE
[Company] — [Job Title]                                          [Dates]
• Reduced deployment frequency from weekly to daily by implementing CI/CD pipeline
• Migrated 50+ services to Kubernetes, improved resource utilization by 30%
• Set up Prometheus monitoring stack, created 20+ dashboards, reduced MTTR by 50%
• Led incident response for 5+ SEV-1 outages, wrote blameless postmortems

PROJECTS
• Personal lab: 3-node K8s cluster at home, running 15+ services
• Contributing to [this repo](https://github.com/vinson-lee01/ops-engineering-roadmap)
```

---

## 🔧 Technical Questions

### Linux (Almost Every Interview)

| Question | What they want to hear |
|----------|----------------------|
| Explain `ps aux` output | `VSZ` = virtual memory, `RSS` = physical memory, `STAT` = process state (R=running, S=sleeping, Z=zombie) |
| What is a zombie process? | Child process that finished but parent hasn't read exit status. Fix: `wait()` in parent or kill parent. |
| `soft link` vs `hard link` | Soft = pointer to filename (breaks if target moved), Hard = pointer to inode (survives target deletion) |
| How to troubleshoot high load? | `top` → which process? → `strace` → `lsof` → check logs |
| `tcpdump` example | `tcpdump -i eth0 port 80 -w capture.pcap` |
| What is `OOM_killer`? | Linux kills processes when memory is full. Check: `dmesg \| grep -i oom` |

### Docker

| Question | Answer |
|----------|--------|
| What is the difference between `CMD` and `ENTRYPOINT`? | `CMD` can be overridden, `ENTRYPOINT` is fixed. `CMD` = default args for `ENTRYPOINT`. |
| Multi-stage build — why? | Reduces image size (build deps not in final image), improves security (no build tools in runtime) |
| `COPY` vs `ADD` | `COPY` = copy local files. `ADD` = copy + auto-extract archives + accept URLs. Prefer `COPY`. |
| How to reduce image size? | Multi-stage build, `alpine` base, `.dockerignore`, one `RUN` per layer (chain with `&&`) |

### Kubernetes (The Big One)

| Question | Answer |
|----------|--------|
| What happens when you run `kubectl apply`? | 1. Client sends YAML to API Server → 2. Authentication/Authorization → 3. Validation → 4. Store in etcd → 5. Scheduler assigns node → 6. Kubelet on node creates containers |
| Pod vs Deployment vs ReplicaSet? | Pod = one or more containers. ReplicaSet = maintains replica count. Deployment = manages ReplicaSets (rolling updates, rollbacks). |
| How to debug a CrashLoopBackOff? | `kubectl logs <pod> --previous` (crash logs), `kubectl describe pod <pod>` (events), check image/command/health checks |
| What is a Namespace? | Logical isolation within a cluster. Resources (Pods, Services) are namespaced; some are not (Nodes, PVs) |
| How to expose a service externally? | `NodePort` (port on every node), `LoadBalancer` (cloud LB), `Ingress` (HTTP/HTTPS routing) |

### CI/CD

| Question | Answer |
|----------|--------|
| CI vs CD? | CI = build + test automatically. CD = deploy automatically (Delivery = manual prod, Deployment = automated prod) |
| How to secure secrets in CI? | Never commit. Use Vault, AWS Secrets Manager, or CI platform's secret store. Rotate regularly. |
| Blue-green vs canary deployment? | Blue-green = two environments, instant switch. Canary = gradual rollout (5% → 25% → 100%) |

### SRE / System Design

| Question | What to cover |
|----------|----------------|
| Design a URL shortener | Consistent hashing, database sharding, caching (Redis), read replicas, monitoring |
| How to design a 99.99% available system? | Redundancy (N+1), auto-failover, geographic distribution, chaos engineering |
| Explain CAP theorem | Consistency, Availability, Partition tolerance — pick 2 (really: P is always there, pick C or A) |
| How to handle cascading failures? | Circuit breaker, bulkhead, timeout, retry with backoff, rate limiting |

---

## 🧩 System Design — How to Answer

### Framework (use this every time)

1. **Clarify requirements** (5 min)
   - "How many users?" "Read-heavy or write-heavy?" "Latency requirements?"
2. **Estmate scale** (5 min)
   - "10M users × 10 req/day = 100M req/day = ~1200 RPS"
3. **High-level design** (10 min)
   - Draw boxes: Load Balancer → API → Service → Database
   - Label data flow
4. **Deep dive** (10 min)
   - Pick 2-3 components to detail (caching, database schema, API design)
5. **Scale the design** (5 min)
   - "What breaks at 100× scale?" → sharding, CDN, read replicas

### Common Ops-Specific Design Questions

| Question | Key points |
|----------|------------|
| Design a log aggregation system | ELK stack, log shippers (Fluentd), retention policy, index lifecycle |
| Design a CI/CD pipeline | Build → test → scan → package → deploy, rollback strategy, secrets management |
| Design a monitoring system | Metrics (Prometheus), logs (Loki), traces (Tempo), alerting (Alertmanager), dashboards (Grafana) |
| Design a multi-region K8s cluster | Federation vs multi-cluster, data locality, global load balancing, DR |

---

## 🗣️ Behavioral Questions (STAR Method)

**STAR** = Situation → Task → Action → Result

### Common Questions

| Question | How to answer |
|----------|----------------|
| Tell me about a time you fixed a critical outage | **S**: SEV-1, API down. **T**: Investigate + fix within SLA. **A**: Checked logs, identified DB connection leak, restarted + connection pool tuning. **R**: Service restored in 20 min, added monitoring to prevent recurrence. |
| How do you handle on-call stress? | **S**: Frequent false alarms. **T**: Reduce alert fatigue. **A**: Reviewed all alerts, increased thresholds, added runbooks. **R**: Alerts reduced by 60%, sleep improved. |
| Tell me about a time you improved a process | **S**: Manual, error-prone deployment. **T**: Automate. **A**: Wrote Jenkins pipeline, added automated rollback. **R**: Deployment time 2h → 15 min, error rate reduced to 0. |
| Why do you want to leave your current job? | Focus on growth, not complaining. "Want to work on larger-scale systems" > "My boss is bad." |

---

## 💰 Salary Negotiation (Don't Skip This!)

### Before the Offer

1. **Research market rate**:
   - Levels.fyi (for big tech)
   - TeamBlind (anonymous salary data)
   - 拉勾 / Boss 直聘 (for China market)
2. **Know your number**: Have a target, not just "whatever they offer"
3. **Don't give first number**: "What's the budget for this role?"

### After the Offer

| Rule | Why |
|------|-----|
| **Never accept immediately** | "I need 2-3 days to review" — this gets you 10-20% more |
| **Negotiate total package**, not just base | RSU, bonus, relocation, sign-on bonus all count |
| **Get it in writing** | Verbal offer ≠ real offer |
| **It's not personal** | Companies expect you to negotiate. You're leaving money on the table if you don't. |

### Sample negotiation script
```
"Thank you for the offer! I'm excited about the role. 
Based on my research and experience, I was expecting [target]. 
Is there flexibility on the base salary / equity?"
```

---

## 📝 Coding Questions (For SRE Roles)

SRE interviews often include coding (usually easier than SWE, but still matters).

### What to practice

| Topic | Where to practice |
|--------|-----------------|
| Bash scripting | [HackerRank - Bash](https://www.hackerrank.com/domains/tutorials/10-days-of-bash) |
| Python (most common) | [LeetCode - Easy](https://leetcode.com/problemset/) |
| System design (coding) | Design LRU cache, consistent hash, rate limiter |
| Regular expressions | Text processing is 80% of SRE coding tasks |

### Sample SRE coding question
```
# Write a Bash script that:
# 1. Takes a log file as argument
# 2. Prints top 10 IPs by request count
# 3. Prints top 10 URLs by 5xx errors

# Answer:
#!/bin/bash
LOG_FILE=$1

echo "=== Top 10 IPs ==="
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -10

echo "=== Top 10 URLs with 5xx ==="
awk '$9 ~ /^5/ {print $7}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -10
```

---

## 🔗 Useful Resources

| Resource | Link | Type |
|----------|------|------|
| **Levels.fyi** | https://levels.fyi/ | Salary data |
| **TeamBlind** | https://teamblind.com/ | Anonymous tech community |
| **System Design Primer** | https://github.com/donnemartin/system-design-primer | GitHub repo |
| **SRE Interview Questions** | https://github.com/mxssl/sre-interview | GitHub repo |
| **DevOps Interview Questions** | https://github.com/bregman-arie/devops-interview-questions | GitHub repo |
| **STAR Method Guide** | https://www.themuse.com/advice/star-interview-method | Article |

---

## ✅ Pre-Interview Checklist

- [ ] Resume updated with quantified achievements
- [ ] GitHub profile has at least 2-3 projects (this repo counts!)
- [ ] Reviewed this roadmap's modules relevant to the job description
- [ ] Prepared 3-5 STAR stories (outage, improvement, conflict, leadership, failure)
- [ ] Practiced 10-20 common technical questions
- [ ] Prepared 3-5 questions to ask the interviewer (shows interest!)
- [ ] Salary range researched
- [ ] Internet + webcam tested (for remote interviews)

### Questions to ask the interviewer (impresses them!)
1. "What does the on-call rotation look like? How many SEV-1s per month?"
2. "What's the deployment frequency? How long does a rollback take?"
3. "What's the biggest reliability challenge the team is facing right now?"
4. "How does the team handle postmortems? Is it blameless?"
5. "What tools does the team use for monitoring/alerting?"

> 💡 **Final tip**: After the interview, send a thank-you email within 24 hours. Short, genuine, mentions something specific from the conversation.
