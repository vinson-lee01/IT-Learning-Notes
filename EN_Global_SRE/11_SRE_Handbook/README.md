# 11 · SRE Handbook

> Site Reliability Engineering — how Google runs production systems at planetary scale. SRE is what happens when you treat operations as a software engineering problem.

---

## 🎯 Learning Objectives

- [ ] Understand SRE principles (SLI/SLO/SLA, error budgets)
- [ ] Apply toil reduction and automation patterns
- [ ] Design incident management and postmortem processes
- [ ] Implement observability and alerting best practices

---

## 📖 The Canon: Google SRE Books (Free)

| Book | Link | Focus |
|------|------|-------|
| Site Reliability Engineering | https://sre.google/sre-book/table-of-contents | Theory & principles |
| The SRE Workbook | https://sre.google/workbook/table-of-contents | Practical implementation |
| Building Secure & Reliable Systems | https://sre.google/books | Security focus |

---

## 📝 Core Concepts

### SLI / SLO / SLA — The Holy Trinity

```
┌──────────────────────────────────────────┐
│  SLA: Business contract with customers    │
│  "99.9% uptime or service credits"        │
│        ┌────────────────────────┐         │
│        │  SLO: Internal target   │         │
│        │  "99.95% availability"  │         │
│        │    ┌──────────────┐     │         │
│        │    │  SLI: Metric  │     │         │
│        │    │  "request     │     │         │
│        │    │   latency     │     │         │
│        │    │   p99 < 200ms"│     │         │
│        │    └──────────────┘     │         │
│        └────────────────────────┘         │
└──────────────────────────────────────────┘
```

### Error Budget

```
Error Budget = 1 - SLO

Example: 99.95% availability → 0.05% error budget
         = 21.6 minutes/month of acceptable downtime

Use it to:
✓ Allow calculated risk-taking in releases
✓ Freeze releases when budget is exhausted
✓ Justify reliability investments
```

### Key Principles

- **Embrace Risk**: 100% reliability is neither possible nor desirable
- **Service Level Objectives**: Define what "good enough" means
- **Eliminate Toil**: Automate repetitive operational work
- **Monitoring**: Alert on symptoms, not causes
- **Postmortems**: Blameless, actionable, widely shared

---

## 🌐 Key Resources

| Resource | Link | Stars |
|----------|------|-------|
| awesome-sre | https://github.com/dastergon/awesome-sre | ⭐13k |
| devops-exercises | https://github.com/bregman-arie/devops-exercises | ⭐82k |
| Postmortem Templates | https://github.com/dastergon/postmortem-templates | - |
| SRE Weekly | https://sreweekly.com | Newsletter |
| How They SRE | https://github.com/upgundecha/howtheysre | Case studies |

---

## 📖 Recommended Reading

| Title | Author |
|-------|--------|
| The Phoenix Project | Gene Kim |
| The DevOps Handbook | Gene Kim, Jez Humble |
| Database Reliability Engineering | Laine Campbell |
| Seeking SRE | David Blank-Edelman |
| Observability Engineering | Charity Majors |

---

[← Back to English Home](../README.md)
