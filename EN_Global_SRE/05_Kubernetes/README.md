# 05 · Kubernetes

> Kubernetes is the de facto operating system of the cloud. Master it, and you command fleets of containers at planetary scale.

---

## 🎯 Learning Objectives

- [ ] Understand K8s architecture deeply (etcd, API server, scheduler, controllers)
- [ ] Design and deploy workloads (Deployment, StatefulSet, DaemonSet, Job)
- [ ] Implement networking (Services, Ingress, NetworkPolicy)
- [ ] Manage configuration (ConfigMap, Secret) and storage (PV/PVC)
- [ ] Operate with Helm, RBAC, HPA, and pod scheduling policies

---

## 🌐 Key Resources

| Resource | Link | Notes |
|----------|------|-------|
| K8s Official Docs | https://kubernetes.io/docs | The source of truth |
| k8s-tutorials | https://github.com/guangzhengli/k8s-tutorials | ⭐5.8k — Chinese tutorial |
| K8s the Hard Way | https://github.com/kelseyhightower/kubernetes-the-hard-way | ⭐43k — Learn by building |
| Play with K8s | https://labs.play-with-k8s.com | Free online cluster |
| K9s | https://github.com/derailed/k9s | Terminal UI for K8s |
| kubectx/kubens | https://github.com/ahmetb/kubectx | Switch contexts fast |

---

## 📖 Essential Books

| Title | Author | Level |
|-------|--------|-------|
| Kubernetes in Action (2nd Ed.) | Marko Lukša | Intermediate |
| Production Kubernetes | Josh Rosso et al. | Advanced |
| Kubernetes Best Practices | Brendan Burns | Intermediate |

---

## 📝 Core Architecture

```
┌──────────────────────────────────────────────┐
│                  Control Plane                │
│  ┌─────────┐ ┌──────────┐ ┌───────────────┐  │
│  │   etcd  │ │API Server│ │ Scheduler     │  │
│  └─────────┘ └──────────┘ └───────────────┘  │
│  ┌───────────────┐ ┌──────────────────────┐  │
│  │ Controller Mgr│ │ Cloud Controller Mgr │  │
│  └───────────────┘ └──────────────────────┘  │
└──────────────────────────────────────────────┘
          │                    │
    ┌─────▼─────┐        ┌────▼──────┐
    │  Worker 1 │  ...   │  Worker N │
    │ kubelet   │        │ kubelet   │
    │ kube-proxy│        │ kube-proxy│
    └───────────┘        └───────────┘
```

## 🏆 Certifications

| Cert | Focus | Time | Cost |
|------|-------|------|------|
| CKA | Admin | 2h | $395 |
| CKAD | Developer | 2h | $395 |
| CKS | Security | 2h | $395 |
| KCNA | Fundamentals | 1.5h | $250 |

**Pro tip**: CKA + CKS is the golden combo for SRE roles.

---

[← Back to English Home](../README.md)
