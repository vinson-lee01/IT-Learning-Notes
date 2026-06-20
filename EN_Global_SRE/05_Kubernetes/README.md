# 05 · Kubernetes Orchestration

> K8s is the operating system of cloud native. Master K8s, and you master the universal language of modern infrastructure.
> This is the most important module — K8s is the core competency for DevOps/SRE roles.

---

## 🎯 Learning Objectives

After completing this module, you should be able to:

- [ ] Understand K8s architecture (Control Plane / Data Plane, etcd, API Server, Scheduler, Controllers)
- [ ] Proficiently operate core resources: Pod / Deployment / Service / Ingress
- [ ] Write and debug YAML manifests by hand (not generate from code)
- [ ] Manage config and secrets with ConfigMap / Secret
- [ ] Master Helm package manager (add repos, install, customize values.yaml)
- [ ] Understand advanced controllers: StatefulSet / DaemonSet / Job / CronJob
- [ ] Configure PersistentVolume and PersistentVolumeClaim
- [ ] Implement service discovery and load balancing
- [ ] Master Ingress controllers (Nginx Ingress / Traefik / Istio)
- [ ] Understand RBAC authorization
- [ ] Perform cluster maintenance: upgrades, backup (etcd), node management
- [ ] Troubleshoot common issues: Pod not starting, network unreachable, storage mount failures
- [ ] Understand networking: CNI plugins, Service IP, Pod IP, Ingress routing
- [ ] Configure ResourceQuota and LimitRange
- [ ] Understand K8s security: Pod Security Standards, Network Policy

**After this module, you're worth 25K+ CNY / $40K+ USD.**

---

## 📺 Recommended Video Tutorials

| Tutorial | Instructor | Link | Views | Rating |
|----------|-------------|------|-------|--------|
| Kubernetes Full Course | TechWorld with Nana | [YouTube](https://www.youtube.com/watch?v=X48VxPB4Pm) | 4M+ | ⭐⭐⭐⭐⭐ |
| K8s in 3 Hours | TechWorld with Nana | [YouTube](https://www.youtube.com/watch?v=s_o8SX20-Y) | 2M+ | ⭐⭐⭐⭐⭐ |
| Helm Simplified | Nana | [YouTube](https://www.youtube.com/watch?v=Z60EyhGWJg) | 500K+ | ⭐⭐⭐⭐ |
| CKA Preparation | Killer Shell | [YouTube](https://www.youtube.com/watch?v=9pUd9Qncao) | 300K+ | ⭐⭐⭐⭐⭐ |
| Istio Service Mesh | Traefik Labs | [YouTube](https://www.youtube.com/watch?v=rxih-PeBIc) | 100K+ | ⭐⭐⭐⭐ |

**Recommended order**: Nana (foundation) → Killer Shell (practice) → Helm (package management)

---

## 📖 Recommended Books

| Book | Author | Level | Comment |
|------|--------|-------|---------|
| *Kubernetes in Action (2nd Ed.)* | Marko Lukša | Advanced | Best K8s book, period. |
| *Kubernetes: Up & Running (3rd Ed.)* | Brendan Burns et al. | Advanced | From K8s co-creator. |
| *Kubernetes Patterns* | Bilgin Ibryam | Advanced | Design patterns for K8s apps. |
| *Helm Book* | Matt Butcher et al. | Intermediate | Definitive Helm guide. |
| *CKA Study Guide* | Benjamin Muschko | Intermediate | Best prep for CKA cert. |
| *Istio in Action* | Christian Posta | Advanced | Service mesh deep dive. |

---

## 🌐 Online Resources

| Resource | Link | Features |
|----------|------|----------|
| K8s Official Docs | https://kubernetes.io/docs/ | Most authoritative, must-read |
| K8s Official Docs (CN) | https://kubernetes.io/zh-cn/docs/ | Chinese translation |
| Kubernetes/minikube | https://github.com/kubernetes/minikube | Local dev environment |
| helm/helm | https://github.com/helm/helm | Helm official repo |
| CNCF Landscape | https://landscape.cncf.io/ | All cloud native projects |
| Play with K8s | https://labs.play-with-k8s.com/ | Online lab platform |
| K8s The Hard Way | https://github.com/kelseyhightower/kubernetes-the-hard-way | ⭐32k, manual setup from scratch |
| CNI Comparison | https://www.cni.dev/ | Network plugin selection guide |
| Istio Docs | https://istio.io/latest/docs/ | Service mesh learning |
| Awesome Kubernetes | https://github.com/ramitsurana/awesome-kubernetes | ⭐4k, curated list |

---

## 📝 Core Knowledge Checklist

### Phase 1: K8s Architecture & Basics (1-2 weeks)

- What K8s is and what problems it solves (container orchestration, self-healing, autoscaling)
- Architecture overview:
  - **Control Plane**: API Server (gateway), etcd (state store), Scheduler (scheduling), Controller Manager (control loops)
  - **Data Plane (Worker)**: kubelet (Pod manager), kube-proxy (network proxy), Container Runtime (container runtime)
- Installation methods:
  - `kubeadm init`: Official recommendation, suitable for production
  - Binary deployment: Most educational, but time-consuming
  - Managed (EKS / GKE / AKS / ACK): Production首选, hassle-free
  - minikube / kind: Local dev & testing
- Set up local environment with minikube:
  ```bash
  minikube start --cpus=4 --memory=8192 --driver=docker
  kubectl get nodes
  ```
- kubectl essential commands:
  ```bash
  kubectl get pods -A                                 # View all Pods in all namespaces
  kubectl get pods -n kube-system                   # View Pods in specific namespace
  kubectl describe pod <name>                       # View Pod details (critical for debugging)
  kubectl logs <pod-name>                           # View logs
  kubectl logs <pod-name> -c <container-name>      # Multi-container Pod: view specific container logs
  kubectl exec -it <pod-name> -- /bin/bash          # Enter container
  kubectl apply -f xxx.yaml                        # Declarative deployment
  kubectl delete -f xxx.yaml                       # Delete resources
  kubectl edit deployment <name>                   # Edit live resource
  kubectl scale deployment <name> --replicas=5   # Scale up/down
  kubectl rollout status deployment <name>          # View rolling update status
  kubectl rollout undo deployment <name>           # Rollback
  kubectl port-forward <pod-name> 8080:80         # Port forwarding (debugging magic)
  kubectl get events --sort-by=.metadata.creationTimestamp  # View cluster events
  ```

### Phase 2: Core Resource Objects (2-3 weeks)

#### Pod — K8s smallest scheduling unit
- Pod definition: one or more containers sharing network/storage
- Why Pod (vs running container directly): co-scheduling, shared volumes, sidecar pattern
- Image pull policy: `Always` / `IfNotPresent` / `Never`
- Restart policy: `Always` / `OnFailure` / `Never`
- Resource constraints: `requests` (scheduling basis) vs `limits` (hard ceiling)
  ```yaml
  resources:
    requests:
      memory: "64Mi"
      cpu: "250m"
    limits:
      memory: "128Mi"
      cpu: "500m"
  ```
- Health checks:
  - `livenessProbe`: Alive probe (restart container on failure)
  - `readinessProbe`: Ready probe (remove from Service on failure)
  - `startupProbe`: Startup probe (protect slow-starting apps)
- InitContainers: Run before main containers, ideal for initialization tasks

#### Deployment — Stateless application deployment
- Deployment purpose: declarative updates, rolling updates, rollbacks, replica control
- Replica control (`replicas`)
- Update strategies:
  - `RollingUpdate`: Rolling update (default, maxSurge/maxUnavailable control pace)
  - `Recreate`: Delete then recreate (for legacy apps that can't run in parallel)
- Rollback operations:
  ```bash
  kubectl rollout history deployment <name>     # View revision history
  kubectl rollout undo deployment <name>      # Rollback to previous version
  kubectl rollout undo deployment <name> --to-revision=2  # Rollback to specific version
  ```
- Pause/resume rolling update:
  ```bash
  kubectl rollout pause deployment <name>      # Pause (for debugging)
  kubectl rollout resume deployment <name>     # Resume
  ```

#### Service — Service discovery & load balancing
- Four Service types:
  - `ClusterIP`: Default, in-cluster access only
  - `NodePort`: Each node opens a fixed port
  - `LoadBalancer`: Cloud provider load balancer
  - `ExternalName`: DNS CNAME mapping
- Service-to-Pod association: via `selector` label matching
- Headless Service (`clusterIP: None`): for StatefulSet or when direct Pod IP access is needed
- DNS resolution rule: `<service>.<namespace>.svc.cluster.local`

#### Ingress — HTTP/HTTPS routing
- Ingress purpose: L7 load balancing, domain-based routing, TLS termination
- Ingress Controller vs Ingress Resource:
  - Ingress Controller: The actual reverse proxy doing the work (Nginx/Traefik/Istio)
  - Ingress Resource: Routing rules definition
- Nginx Ingress installation:
  ```bash
  helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
  helm install ingress-nginx ingress-nginx/ingress-nginx
  ```
- Ingress example:
  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: example-ingress
    annotations:
      nginx.ingress.kubernetes.io/rewrite-target: /
  spec:
    tls:
    - hosts:
      - example.com
      secretName: example-tls
    rules:
    - host: example.com
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: web-service
              port:
                number: 80
  ```

#### ConfigMap & Secret — Configuration management
```yaml
# ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgres://db:5432/mydb"
  log_level: "info"

---
# Using ConfigMap in Pod
spec:
  containers:
  - name: app
    env:
    - name: DATABASE_URL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database_url
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config

---
# Secret (base64-encoded)
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=   # echo -n "password123" | base64
```

---

## 🔧 Hands-On: Deploy a Complete App (Nginx + Redis + Config)

```yaml
# 1. ConfigMap (Nginx config)
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-conf
data:
  nginx.conf: |
    server {
        listen 80;
        location / {
            root /usr/share/nginx/html;
            index index.html;
        }
        location /api {
            proxy_pass http://redis-service:6379;
        }
    }

---
# 2. Deployment (Nginx)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
        volumeMounts:
        - name: conf
          mountPath: /etc/nginx/conf.d
        - name: html
          mountPath: /usr/share/nginx/html
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 5
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
      volumes:
      - name: conf
        configMap:
          name: nginx-conf
      - name: html
        configMap:
          name: nginx-html

---
# 3. Service (Nginx)
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
  type: ClusterIP

---
# 4. Redis Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        ports:
        - containerPort: 6379
        volumeMounts:
        - name: data
          mountPath: /data
      volumes:
      - name: data
        emptyDir: {}

---
# 5. Redis Service
apiVersion: v1
kind: Service
metadata:
  name: redis-service
spec:
  selector:
    app: redis
  ports:
  - port: 6379
    targetPort: 6379
  type: ClusterIP
```

Apply:
```bash
kubectl apply -f nginx-redis.yaml
kubectl get all
kubectl port-forward svc/nginx-service 8080:80
# Visit localhost:8080 in browser
```

---

## 🚨 Common Troubleshooting Guide

### Pod won't start (Pending / CrashLoopBackOff / ImagePullBackOff)

```bash
# 1. Check Pod status and events
kubectl describe pod <pod-name> -n <namespace>
# Focus on Events section

# 2. Common Pending causes
# - Insufficient resources (nodes have insufficient...)
# - Node selector mismatch
# - PVC mount failure

# 3. Common ImagePullBackOff causes
# - Wrong image name
# - Private registry without imagePullSecrets
# - Network unreachable (node can't access registry)

# 4. Check container logs
kubectl logs <pod-name> -n <namespace>
kubectl logs <pod-name> -c <container-name> -n <namespace>  # multi-container
```

### Network unreachable (Service can't reach Pod / Pod can't reach internet)

```bash
# 1. Check Service Endpoints (MOST IMPORTANT!)
kubectl get endpoints <service-name> -n <namespace>
# If Endpoints is empty, Service selector and Pod labels don't match

# 2. Test network from inside a Pod
kubectl exec -it <pod-name> -- nslookup kubernetes.default.svc.cluster.local
kubectl exec -it <pod-name> -- ping <service-ip>
kubectl exec -it <pod-name> -- curl <service-name>:<port>

# 3. Check NetworkPolicy (is traffic blocked?)
kubectl get networkpolicy -n <namespace>

# 4. Check CNI plugin status
kubectl get pods -n kube-system | grep -E "calico|flannel|weave|cilium"
```

### Storage mount failure (PVC Pending)

```bash
# 1. Check if StorageClass exists
kubectl get sc

# 2. Check PVC status
kubectl get pvc -n <namespace>
# Pending = no available PV or StorageClass misconfigured

# 3. View PVC events
kubectl describe pvc <pvc-name> -n <namespace>
```

---

## 🏭 Production Best Practices

### Resource Quotas & Limits
```yaml
# ResourceQuota: namespace-level total resource limits
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.cpu: "20"
    limits.memory: 40Gi
    pods: "50"
    services: "20"

---
# LimitRange: default resource limits per container
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
spec:
  limits:
  - default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "100m"
      memory: "128Mi"
    type: Container
```

### Pod Disruption Budget (PDB) — Ensure service availability during rolling updates
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  minAvailable: 2        # Keep at least 2 Pods available
  selector:
    matchLabels:
      app: nginx
```

### Security Hardening
```yaml
# 1. Don't run as root
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  readOnlyRootFilesystem: true

# 2. Network Policy (allow only specific Pods to access)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-allow
spec:
  podSelector:
    matchLabels:
      app: api
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
```

---

## 🎓 Certification Guide (CKA / CKAD)

| Cert | Focus | Preparation Tips |
|------|-------|-------------------|
| CKA (Certified Kubernetes Administrator) | Cluster ops, troubleshooting, networking, storage | Practice `kubectl` speed, hand-write YAML fast |
| CKAD (Certified Kubernetes Application Developer) | App deployment, ConfigMap/Secret, Ingress, HPA | Practice Helm, label selectors, health checks |
| CKS (Certified Kubernetes Security Specialist) | Security hardening, network policies, image security | Practice Pod Security Standards, RBAC, Network Policy |

**Prep Resources**:
- [Killer Shell](https://killer.sh/) — Simulated exam environment (HIGHLY推荐)
- [CKA Prep Notes](https://github.com/stefanprodan/Kubernetes-CKA) — ⭐14k
- [CKAD Exercises](https://github.com/dgkanatsio/Kubernetes-CKAD) — ⭐8k

---

## 📊 Advanced Roadmap

```
K8s Basics
  └── K8s Networking (CNI, Service, Ingress, Istio)
        └── K8s Storage (PV/PVC/StorageClass/CSI)
              └── Helm Package Management
                    └── GitOps (Argo CD / Flux)
                          └── Service Mesh (Istio / Linkerd)
                                └── Observability (Prometheus + Grafana + Jaeger)
```

**Recommended next module**: [06_CI_CD](../06_CI_CD/) — Learn to automate deployments to K8s with GitHub Actions / GitLab CI.

---

## ✅ Self-Check Quiz

After learning, try to answer these:

- [ ] Explain K8s architecture — what does each component do?
- [ ] What's the difference between `requests` and `limits`?
- [ ] How does Deployment rolling update work? How to rollback?
- [ ] What's the difference between `ClusterIP` / `NodePort` / `LoadBalancer`?
- [ ] What's the relationship between Ingress and Service?
- [ ] Difference between `livenessProbe` and `readinessProbe`?
- [ ] How does PVC binding to PV work?
- [ ] What's the difference between StatefulSet and Deployment?
- [ ] What's the relationship between Role / ClusterRole / RoleBinding / ClusterRoleBinding in RBAC?
- [ ] How do you troubleshoot Pod network connectivity issues?

---

> After this module, go get a CKA certification. Put "Proficient in K8s architecture & operations" on your resume — your salary will jump.
> Next recommended: [06_CI_CD](../06_CI_CD/) — Automate code deployment to K8s clusters.
