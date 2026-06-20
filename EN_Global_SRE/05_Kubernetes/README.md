# 05 · Kubernetes Orchestration

> Kubernetes is the operating system of cloud-native infrastructure. Master K8s and you master the universal language of modern ops.
> This module is the heart of the entire roadmap — spend time here, it directly impacts your salary.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- [ ] Understand K8s architecture (Control Plane / Node components, etcd, API Server, Scheduler, Controllers)
- [ ] Confidently work with Pods, Deployments, Services, Ingress
- [ ] Write and debug YAML manifests fluently
- [ ] Manage config and secrets with ConfigMap / Secret
- [ ] Use Helm for package management (add repos, install, customize values)
- [ ] Understand StatefulSet, DaemonSet, Job, CronJob
- [ ] Configure PersistentVolume and PersistentVolumeClaim
- [ ] Implement service discovery and load balancing
- [ ] Set up Ingress controllers (Nginx Ingress / Traefik)
- [ ] Understand RBAC authorization
- [ ] Perform cluster maintenance: upgrades, etcd backup, node management
- [ ] Troubleshoot: Pod not starting, network issues, storage mount failures

**Master this module and you're worth 25K+ RMB (or $50K+ USD).**

---

## 📺 Recommended Video Courses

### English

| Course | Instructor | Platform | Duration | Rating |
|--------|-----------|----------|----------|--------|
| **Kubernetes for Beginners** | TechWorld with Nana | YouTube | 3h | ⭐⭐⭐⭐⭐ |
| **Kubernetes Full Course** | FreeCodeCamp | YouTube | 8h | ⭐⭐⭐⭐⭐ |
| **CKA Course** | KillerCoda | Interactive | Self-paced | ⭐⭐⭐⭐⭐ |
| **Kubernetes Deployment Architectures** | Sander van Vugt | O'Reilly | 6h | ⭐⭐⭐⭐ |

### Chinese (for reference)

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| K8s 教程由浅入深 | 尚硅谷 | [B站](https://www.bilibili.com/video/BV1Qv41167ck) | 100万+ | ⭐⭐⭐⭐⭐ |
| K8s 入门到精通 | 黑马程序员 | [B站](https://www.bilibili.com/video/BV1cK4y1L7Tb) | 50万+ | ⭐⭐⭐⭐ |
| 狂神说 K8s | 狂神 | [B站](https://www.bilibili.com/video/BV1GT4y1A756) | 200万+ | ⭐⭐⭐⭐ |

**Suggested order**: Watch Nana's beginner course first → practice on KillerCoda → read Kubernetes in Action → take CKA exam.

---

## 📖 Recommended Books

| Book | Author | Stage | Comment |
|------|--------|-------|---------|
| **Kubernetes in Action (2nd ed)** | Marko Lukša | Advanced | The best K8s book, period. Must-read. |
| **Kubernetes: Up and Running (2nd ed)** | Brendan Burns | Advanced | From K8s co-founders, great context. |
| **The Kubernetes Book** | Nigel Poulton | Intermediate | Thin, clear, great for quick start. |
| **Kubernetes Patterns** | Bilgin Ibryam | Advanced | Design patterns for K8s apps. |
| **Managing Kubernetes** | Josh Rosso | Advanced | Operations-focused, troubleshooting. |

**Chinese**: 《Kubernetes 权威指南》+《深入解析 Kubernetes》(张磊) are excellent Chinese references.

---

## 🌐 Online Resources

| Resource | Link | Features |
|----------|------|----------|
| **Kubernetes Official Docs** | https://kubernetes.io/docs/ | Authoritative, has Chinese version |
| **Kubernetes by Example** | https://k8sbyexample.com/ | Quick reference for YAML snippets |
| **Awesome Kubernetes** | https://github.com/ramitsurana/awesome-kubernetes | Curated list of K8s resources |
| **KillerCoda K8s Scenarios** | https://killercoda.com/kubernetes | Free interactive K8s labs |
| **Play with Kubernetes** | https://labs.play-with-k8s.com/ | Free browser-based K8s cluster |
| **Helm Official Docs** | https://helm.sh/docs/ | Package management |
| **CNCF Landscape** | https://landscape.cncf.io/ | See the whole ecosystem |
| **K8s Production Best Practices** | https://learnk8s.io/production-best-practices | Practical production tips |

---

## 📝 Core Knowledge Checklist

### Phase 1: Architecture & Basics (1-2 weeks)

- What K8s solves and why it exists
- Architecture overview:
  - **Control Plane**: API Server, etcd, Scheduler, Controller Manager
  - **Node components**: kubelet, kube-proxy, Container Runtime
- Installation methods: kubeadm vs binary vs managed (EKS/GKE/AKS)
- Set up local lab with minikube or kind
- Essential kubectl commands:
  ```bash
  kubectl get pods -A
  kubectl describe pod <name> -n <namespace>
  kubectl logs <pod-name> -f
  kubectl exec -it <pod-name> -- /bin/bash
  kubectl apply -f manifest.yaml
  kubectl delete -f manifest.yaml
  kubectl get events --sort-by=.metadata.creationTimestamp
  ```

### Phase 2: Core Resource Objects (2-3 weeks)

#### Pod — The smallest deployable unit
- What a Pod is: one or more containers sharing network/storage
- Why Pods exist (vs running containers directly)
- Image pull policy: `Always` / `IfNotPresent` / `Never`
- Restart policy: `Always` / `OnFailure` / `Never`
- Resource requests vs limits (QoS classes)
- Health checks: livenessProbe / readinessProbe / startupProbe
- Init containers

#### Deployment — Declarative updates for Pods
- What Deployments provide: declarative updates, rolling updates, rollbacks
- Replica management
- Update strategies: RollingUpdate vs Recreate
- Rollback: `kubectl rollout undo deployment/<name>`
- Scaling: `kubectl scale deployment/<name> --replicas=5`
- Pause and resume rollouts

#### Service — Stable network endpoint for Pods
- Why Services exist (Pod IPs are ephemeral)
- Service types:
  - `ClusterIP`: internal-only (default)
  - `NodePort`: exposes on each Node's IP at a static port
  - `LoadBalancer`: provisions cloud load balancer
  - `ExternalName`: DNS CNAME mapping
- Service discovery via DNS
- Headless Services (`clusterIP: None`) for StatefulSets

#### ConfigMap & Secret — Configuration management
- Creating ConfigMaps from literals, files, directories
- Consuming in containers: env vars, envFrom, volume mount
- Secrets: Opaque, docker-registry, tls
- Best practice: don't commit Secrets to Git → use Sealed Secrets or Vault

### Phase 3: Advanced Workloads (2 weeks)

#### StatefulSet — Stateful applications
- When to use StatefulSet vs Deployment
- Stable network identity (Pod hostname persists across reschedules)
- Ordered deployment and scaling
- Persistent storage per Pod
- Example use cases: databases, message queues, clustered apps

#### DaemonSet — One Pod per Node
- Use cases: log collectors, monitoring agents, networking
- Updating DaemonSets

#### Job & CronJob — Batch processing
- Job: one-off task, retry logic
- CronJob: scheduled tasks, concurrency policies
- `startingDeadlineSeconds` and why it matters

### Phase 4: Storage (1-2 weeks)

- Container filesystem is ephemeral — why PV/PVC exists
- PV (PersistentVolume): provisioned manually or dynamically
- PVC (PersistentVolumeClaim): what the Pod actually requests
- StorageClasses: dynamic provisioning
- Access modes: RWO, ROX, RWX
- Common pitfalls:
  - PVC not binding (no matching PV or StorageClass)
  - Pod stuck `Pending` because PVC can't mount
  - File permissions on mounted volumes

### Phase 5: Ingress & Networking (2 weeks)

- Why Ingress exists (avoid exposing each Service via LoadBalancer)
- Ingress controllers: Nginx, Traefik, HAProxy, Istio
- Ingress resource YAML structure
- Path-based vs host-based routing
- TLS termination at Ingress
- NetworkPolicies: control traffic between Pods
- CNI plugins: Calico, Flannel, Cilium (comparison)

### Phase 6: Helm & Package Management (1 week)

- Why Helm exists (YAML sprawl, no versioning, no rollback)
- Helm architecture: Chart = package, Release = installed instance
- Essential commands:
  ```bash
  helm repo add bitnami https://charts.bitnami.com/bitnami
  helm search repo nginx
  helm install my-nginx bitnami/nginx
  helm upgrade my-nginx bitnami/nginx --values custom-values.yaml
  helm rollback my-nginx 1
  helm uninstall my-nginx
  ```
- Creating your own Chart: `helm create my-chart`
- Template syntax: `{{ .Values.xxx }}`, conditionals, ranges
- Helm best practices: use existing Charts, don't reinvent

### Phase 7: RBAC & Security (1 week)

- Why RBAC matters (least privilege)
- Core concepts: User/Group → Role/ClusterRole → RoleBinding/ClusterRoleBinding
- Default ServiceAccount and why you should't use it for everything
- Pod Security Standards: Privileged / Baseline / Restricted
- Network segmentation with NetworkPolicies
- Secrets encryption at rest (etcd encryption)

### Phase 8: Cluster Administration (ongoing)

- Upgrading control plane nodes (one at a time)
- Upgrading worker nodes (drain → upgrade → uncordon)
- etcd backup and restore:
  ```bash
  etcdctl snapshot save snapshot.db
  etcdctl snapshot restore snapshot.db
  ```
- Node management: taints, tolerations, node affinity
- Resource quotas and limit ranges
- Monitoring cluster health: control plane components

---

## 🔬 Hands-on Projects

| Project | Difficulty | What you'll learn |
|---------|-------------|-------------------|
| **Deploy a 3-tier app** | ⭐⭐ | Deployments, Services, Ingress, PVC |
| **Set up Nginx Ingress** | ⭐⭐ | Ingress controller installation and configuration |
| **Helmify an app** | ⭐⭐⭐ | Create a Helm Chart from scratch |
| **Set up Prometheus monitoring** | ⭐⭐⭐⭐ | K8s monitoring stack |
| **CKA practice exam** | ⭐⭐⭐⭐ | Exam-style troubleshooting |
| **Multi-stage deployment** | ⭐⭐⭐⭐⭐ | Staging → production with Helm |

---

## ⚠️ Common Pitfalls

| Pitfall | Why it happens | How to avoid |
|---------|----------------|---------------|
| Images pulled from public registries | Rate limits, reliability | Use a private registry or pull-through cache |
| No resource requests/limits | Node runs out of memory | Always set requests and limits |
| Using `latest` tag | Can't reproduce or roll back | Pin image tags to specific versions |
| Storing Secrets in Git | Security breach | Use Sealed Secrets, Vault, or SOPS |
| Not using health checks | K8s sends traffic to broken Pods | Always configure liveness/readiness probes |
| One big monolithic manifest | Hard to maintain | Split into separate files, use Kustomize or Helm |
| Ignoring RBAC | Security risk | Set up proper Roles and RoleBindings |

---

## ✅ Self-Check: Can you...

- [ ] Explain what happens when you run `kubectl apply -f deployment.yaml`?
- [ ] Manually debug a Pod that's in `CrashLoopBackOff`?
- [ ] Set up an Ingress that routes `api.example.com` to one Service and `web.example.com` to another?
- [ ] Create a Helm Chart with configurable replica count and resource limits?
- [ ] Back up etcd and restore it on a new cluster?
- [ ] Explain the difference between a Deployment and a StatefulSet?

> 💡 **Next step**: After this module, move on to **08 · CI/CD Pipelines** to learn how to automate deployments to your K8s cluster.
