# 11 · SRE Handbook

> SRE (Site Reliability Engineering) is not a job title — it's a way of running production systems.
> This module covers the SRE philosophy, practices, and tools. Based on Google's SRE books.

---

## 🎯 What is SRE?

SRE is what happens when you ask a software engineer to design an operations team.

| Traditional Ops | SRE |
|---------------|-----|
| "Run the service however you can" | Engineering approach to operations |
| Manual, reactive | Automated, proactive |
| No error budget | Error budget = explicit agreement |
| "Feature velocity vs reliability" is a fight | SLOs make it a shared goal |
| Human intervention for everything | Eliminate toil |

**Core insight**: SRE is 50% engineering work (writing code to automate operations) and 50% operational work (on-call, incident response, postmortems).

---

## 📝 Core Concepts (MUST memorize)

### SLO / SLI / SLA — Know the difference!

| Term | Full name | What it means | Example |
|------|------------|-------------|----------|
| **SLI** | Service Level Indicator | The metric you measure | "99.9% of requests return 200 in <200ms" |
| **SLO** | Service Level Objective | The target you set | "We aim for 99.9% availability per month" |
| **SLA** | Service Level Agreement | The contract with users | "If we miss 99.5%, users get refund" |

**Key SLIs to track**:
- **Availability**: `% of requests that return 200`
- **Latency**: `p99 latency < 200ms`
- **Throughput**: requests per second
- **Error rate**: `% of 5xx responses`
- **Durability**: `% of writes that survive disk failure`

### Error Budget

The most powerful SRE concept:

```
Error Budget = 1 - SLO
If SLO = 99.9%, then Error Budget = 0.1% = ~43 min/month

If you've "spent" your error budget (43 min of downtime this month):
  → Feature freeze! No new releases until next month.
  → Focus on reliability work.

If you have error budget remaining:
  → Release freely! Take risks!
```

This aligns engineering and product: both want to "spend" the error budget wisely.

---

## 🔥 Incident Response

### What is an incident?

An incident is an event that disrupts normal service and requires human intervention.

### Incident Command System (ICS)

Don't wing it. Use roles:

| Role | Responsibility | Who |
|------|-----------------|------|
| **IC (Incident Commander)** | Overall coordination, decision making | Most senior person |
| **Scribe** | Document everything in the incident doc | Rotate every 30 min |
| **SME (Subject Matter Expert)** | Deep technical knowledge | On-call engineer |
| **Comms** | User-facing communication | Product/Support |

### Incident Severity Levels

| Severity | Impact | Response time | Example |
|----------|---------|----------------|----------|
| **SEV-1** | Full outage, revenue impact | 15 min | All users can't log in |
| **SEV-2** | Partial outage, degraded service | 30 min | Search is slow but works |
| **SEV-3** | Minor impact, workaround exists | 4 hours | One feature broken for some users |
| **SEV-4** | Bug, no user impact | Next business day | Typo in docs |

### Incident Template (use this every time)

```
## SEV-1: [Brief description]

**Status**: Investigating | Identified | Monitoring | Resolved
**Impact**: [Which users/services affected]
**Start time**: 2026-01-15 14:30 UTC
**Responders**: @alice, @bob

### Timeline
- 14:30 — Alert fired: API 5xx rate > 10%
- 14:35 — Iidentifed: database primary is down
- 14:40 — Action: failover to replica
- 14:50 — Verified: service recovered
- 15:00 — Monitoring: no further alerts

### Root Cause
[What actually caused this]

### Action Items
- [ ] Fix the root cause
- [ ] Update runbook
- [ ] Add alert for this scenario
```

---

## 📄 Postmortem (BLAMELESS!)

**Rule #1: Postmortems are blameless.** If you blame people, they won't be honest next time.

### Postmortem Template

```markdown
## Postmortem: SEV-1 API Outage 2026-01-15

**Authors**: @alice, @bob
**Reviewers**: @sre-team
**Status**: Draft | Review | Final

### Summary
[2-3 sentences: what happened, impact, root cause]

### Impact
- Duration: 30 minutes (14:30 - 15:00 UTC)
- Affected users: 100% (all API requests failing)
- Revenue impact: $[estimate]

### Root Cause
[Detailed technical explanation of what went wrong]

### Timeline
(Must match incident doc timeline)

### Contributing Factors
- [ ] No alert on database primary health
- [ ] Runbook was outdated
- [ ] Failover took 10 minutes (should be < 2 min)

### Lessons Learned
**What went well**:
- Alert fired quickly
- Team responded within SLA
- Communication to users was clear

**What went wrong**:
- Database failover was slow
- Runbook had wrong command syntax
- No monitoring on replica lag

### Action Items
| Action | Owner | Deadline | Status |
|--------|--------|----------|--------|
| Update database failover runbook | @alice | 2026-01-20 | Open |
| Add alert for DB primary health | @bob | 2026-01-18 | Open |
| Test failover in staging (monthly) | @charlie | 2026-02-01 | Open |
```

**Key rule**: Every SEV-1 and SEV-2 incident MUST have a postmortem. Action items must have owners and deadlines.

---

## 📊 Monitoring & Observability

### Three Pillars of Observability

| Pillar | What it captures | Tool |
|---------|-----------------|-------|
| **Metrics** | Numeric time-series data | Prometheus, Datadog |
| **Logs** | Discrete events (timestamp + message) | ELK, Loki |
| **Traces** | Request flow across services | Jaeger, Tempo |

#### Metrics — the foundation
```
# Four golden signals (Google SRE book)
1. Latency: How long it takes to serve a request
2. Traffic: How much demand is being served (RPS)
3. Errors: Rate of failed requests
4. Saturation: How "full" the service is (CPU, memory, disk)
```

Prometheus Query Language (PromQL) basics:
```promql
# HTTP request rate
rate(http_requests_total[5m])

# 95th percentile latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# CPU usage > 80%
(node_cpu_seconds_total / node_cpu_seconds_total) * 100 > 80

# Alert: error rate too high
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
```

#### Logs — structured, not text
```
# Bad
log.info("User logged in")

# Good (structured JSON)
log.info("user_login", user_id=1234, ip="1.2.3.4", duration_ms=45)
```

ELK stack: Elasticsearch + Logstash + Kibana
- Logstash: collect and parse logs
- Elasticsearch: store and index
- Kibana: search and visualize

#### Traces — understand request flow
When a user request hits your API and calls 5 microservices, a trace shows you:
- Which service is slow?
- Where are the errors?
- What's the critical path?

OpenTelemetry is the standard (replaces OpenTracing + OpenCensus).

---

## 🔧 Toil — The Silent Killer

**Toil** = operational work that is:
- Manual
- Repetitive
- Automatable
- Tactical (not strategic)
- No enduring value

**Why toil is bad**:
- Scales linearly with service growth (more users = more toil)
- Prevents strategic work (engineering improvements)
- Burns people out

**SRE toil target**: < 50% of SRE time should be on-call/toil. Remaining 50% for engineering projects.

**How to reduce toil**:
1. Automate runbooks (don't document, automate!)
2. Self-healing systems (auto-restart, auto-failover)
3. Better alerting (only page for things that need human judgment)
4. Eliminate recurring issues (fix root cause, not symptoms)

---

## 🚀 Capacity Planning

- **Why it matters**: running out of capacity = outage
- **Lead time**: how long to provision new capacity? (Hours? Days? Weeks?)
- **Growth rate**: how fast is traffic growing? (Linear? Exponential?)
- **Headroom**: always have N+1 redundancy

**Simple capacity formula**:
```
Required capacity = (current traffic × growth factor) / (average RPS per instance) × (1 + headroom)
```

Example:
- Current: 1000 RPS
- Growth: 50% next quarter
- Per-instance: 50 RPS
- Headroom: 30%
- Required: (1000 × 1.5) / 50 × 1.3 = 39 instances

---

## 📖 Essential Reading

| Book | Author | Must-read? | Free? |
|------|--------|-----------|-------|
| **Site Reliability Engineering** | Google SRE | ⭐⭐⭐⭐⭐ | ✅ https://sre.google/books/ |
| **The Site Reliability Workbook** | Google SRE | ⭐⭐⭐⭐⭐ | ✅ https://sre.google/workbook/table-of-contents/ |
| **Seeking SRE** | Google SRE | ⭐⭐⭐⭐ | ✅ https://sre.google/seeking-sre/table-of-contents/ |
| **Implementing Service Level Objectives** | O'Reilly | ⭐⭐⭐⭐ | ❌ |
| **The Art of Monitoring** | James Turnbull | ⭐⭐⭐ | ❌ |

**Read the free Google SRE books first.** They are the foundation of everything SRE.

---

## 🔬 Hands-on Projects

| Project | Difficulty | What you'll learn |
|---------|-------------|-------------------|
| **Set up Prometheus + Grafana** | ⭐⭐ | Metrics, dashboards, alerting |
| **Define SLOs for a service** | ⭐⭐⭐ | SLI/SLO design, error budget |
| **Write a postmortem for a past incident** | ⭐⭐⭐ | Blameless culture, root cause analysis |
| **Set up ELK stack** | ⭐⭐⭐ | Log aggregation, search, visualization |
| **Implement circuit breaker** | ⭐⭐⭐⭐ | Resilience patterns |
| **Run a game day** | ⭐⭐⭐⭐ | Chaos engineering, team preparedness |

---

## ⚠️ Common Mistakes

| Mistake | Why it happens | How to avoid |
|----------|----------------|---------------|
| Setting SLOs too strict | "We want 100% uptime!" | 100% is the wrong target. It's too expensive. |
| No error budget enforcement | "We'll just release anyway" | Then SLOs are meaningless. Enforce the freeze. |
| Blameful postmortems | "This was John's mistake" | You get silence. Blameless = honesty. |
| Alerting on everything | "I want to know everything" | Alert fatigue. Only alert on things needing human judgment. |
| No runbooks | "I'll remember how to fix it" | You won't. Write it down AND automate it. |

---

## ✅ Self-Check: Can you...

- [ ] Explain the difference between SLO, SLI, and SLA?
- [ ] Calculate error budget for 99.9% SLO?
- [ ] Write a good postmortem (blameless, actionable)?
- [ ] Set up a Prometheus alert for high error rate?
- [ ] Explain why 100% availability is the wrong target?
- [ ] Define the four golden signals and what they measure?

> 💡 **Next step**: After this module, move on to **12 · Interview Prep** to consolidate everything before job hunting.
