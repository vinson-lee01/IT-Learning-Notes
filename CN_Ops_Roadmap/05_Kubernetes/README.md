# 05 · Kubernetes 容器编排

> K8s 是云原生的操作系统。学会 K8s，你就掌握了现代基础设施的通用语言。
> 这个模块是我花时间最多的，因为 K8s 是现在运维工程师的核心竞争力。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 理解 K8s 整体架构（Master/Worker、etcd、API Server、Scheduler、Controller）
- [ ] 熟练操作 Pod/Deployment/Service/Ingress 等核心资源
- [ ] 编写和调试 YAML 配置文件
- [ ] 使用 ConfigMap/Secret 管理配置和敏感信息
- [ ] 掌握 Helm 包管理工具（添加仓库、安装、自定义 values）
- [ ] 了解 StatefulSet/DaemonSet/Job/CronJob 等高级控制器
- [ ] 配置 PersistentVolume 和 PersistentVolumeClaim
- [ ] 理解并实现服务发现和负载均衡
- [ ] 掌握 Ingress 控制器（Nginx Ingress / Traefik）
- [ ] 了解 RBAC 权限控制机制
- [ ] 会做集群维护：升级、备份（etcd）、节点管理
- [ ] 能排查常见故障：Pod 起不来、网络不通、存储挂载失败

**学完这个模块，你值 25K+。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| K8s 教程由浅入深 | 尚硅谷 | [B站 BV1Qv41167ck](https://www.bilibili.com/video/BV1Qv41167ck) | 100万+ | ⭐⭐⭐⭐⭐ |
| K8s 入门到精通 | 黑马程序员 | [B站 BV1cK4y1L7Tb](https://www.bilibili.com/video/BV1cK4y1L7Tb) | 50万+ | ⭐⭐⭐⭐ |
| K8s 实战 | 马哥 | [B站](https://space.bilibili.com/387633139) | 30万+ | ⭐⭐⭐⭐ |
| 狂神说 K8s | 狂神 | [B站 BV1GT4y1A756](https://www.bilibili.com/video/BV1GT4y1A756) | 200万+ | ⭐⭐⭐⭐ |
| Helm 包管理 | 阳阳羊 | [B站](https://www.bilibili.com/video/BV1SAR7Y7oj) | 10万+ | ⭐⭐⭐ |

**学习顺序建议**：先看完「尚硅谷」打基础，再跟「狂神」做实战，最后用「Helm」学包管理。

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《Kubernetes 权威指南》 | 龚正等 | 高级 | 国内 K8s 最系统的书，配合官网文档一起看 |
| 《Kubernetes in Action（第2版）》 | Marko Lukša | 高级 | 最好的 K8s 英文书，有中文版 |
| 《深入解析 Kubernetes》 | 张磊 | 高级 | 阿里云 K8s 团队出品，原理讲得深 |
| 《Helm 学习指南》 | O'Reilly | 高级 | Helm 专题，够用 |
| 《Kubernetes 网络权威指南》 | 杜军 | 专家 | 网络专题，CNI/Service/Ingress 讲得细 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| K8s 官方文档（中文） | https://kubernetes.io/zh-cn/docs/ | 最权威，必看 |
| K8s 中文社区 | https://kubernetes.org.cn/ | 中文翻译，更新及时 |
| guangzhengli/k8s-tutorials | https://github.com/guangzhengli/k8s-tutorials | ⭐5.8k，最好的中文教程 |
| kubernetes/minikube | https://github.com/kubernetes/minikube | 本地实验环境 |
| helm/helm | https://github.com/helm/helm | Helm 官方仓库 |
| 阿里云 K8s 最佳实践 | https://help.aliyun.com/product/85222.html | 国内云厂商实战经验 |
| Play with K8s | https://labs.play-with-k8s.com/ | 在线实验平台 |

---

## 📝 核心知识点清单

### 第一阶段：K8s 架构和基础（1-2 周）

- K8s 是什么，解决什么问题
- 整体架构：Master 节点组件 vs Worker 节点组件
  - Master：API Server、etcd、Scheduler、Controller Manager
  - Worker：kubelet、kube-proxy、Container Runtime
- 安装方式对比：kubeadm vs 二进制 vs 云厂商托管
- 使用 minikube 搭建本地实验环境
- kubectl 基础命令：
  ```
  kubectl get pods
  kubectl describe pod <name>
  kubectl logs <pod-name>
  kubectl exec -it <pod-name> -- /bin/bash
  kubectl apply -f xxx.yaml
  kubectl delete -f xxx.yaml
  ```

### 第二阶段：核心资源对象（2-3 周）

#### Pod — K8s 的最小调度单元
- Pod 的定义：一个或多个容器的集合
- 为什么需要 Pod（vs 直接跑容器）
- 镜像拉取策略：`Always` / `IfNotPresent` / `Never`
- 重启策略：`Always` / `OnFailure` / `Never`
- 资源限制：`requests` vs `limits`
- 健康检查：livenessProbe / readinessProbe / startupProbe
- 初始化容器（initContainers）

#### Deployment — 无状态应用部署
- Deployment 的作用：声明式更新、滚动升级、回滚
- 副本数控制（replicas）
- 更新策略：RollingUpdate vs Recreate
- 回滚操作：`kubectl rollout undo`
- 暂停和恢复更新：`kubectl rollout pause`

#### Service — 服务发现和负载均衡
- Service 的几种类型：
  - `ClusterIP`：集群内访问（默认）
  - `NodePort`：通过节点 IP + 端口访问
  - `LoadBalancer`：云厂商负载均衡器
  - `ExternalName`：DNS CNAME 映射
- Service 和 Pod 的关联：Labels 和 Selectors
- Headless Service（`clusterIP: None`）

#### Ingress — HTTP/HTTPS 路由
- 为什么需要 Ingress（vs Service NodePort）
- Ingress 控制器：Nginx Ingress / Traefik / HAProxy
- Ingress 规则配置：域名路由、路径匹配、TLS 终止
- 实战：用 Ingress 暴露多个 Web 服务

### 第三阶段：配置管理和存储（1 周）

#### ConfigMap & Secret
- ConfigMap：键值对配置，挂载为环境变量或文件
- Secret：Base64 编码的敏感信息（密码、Token）
- 使用场景对比：何时用 ConfigMap，何时用 Secret
- 实战：把 MySQL 密码存到 Secret，挂载到 Pod

#### 存储（Volume / PV / PVC）
- Volume 类型：emptyDir、hostPath、nfs、persistentVolumeClaim
- PV（PersistentVolume）：集群级别的存储资源
- PVC（PersistentVolumeClaim）：用户对存储的请求
- StorageClass：动态供应存储
- 实战：给 MySQL 挂载持久化存储

### 第四阶段：高级控制器（1-2 周）

#### StatefulSet — 有状态应用
- 和 Deployment 的区别：稳定的网络标识、稳定的存储
- 适用场景：MySQL 主从、Redis Cluster、Kafka
- Headless Service + StatefulSet 组合使用

#### DaemonSet — 守护进程
- 每个节点运行一个 Pod
- 适用场景：日志收集（Filebeat）、监控代理（Node Exporter）

#### Job & CronJob — 批处理
- Job：一次性任务
- CronJob：定时任务（类似 crontab）

### 第五阶段：Helm 包管理（1 周）

- Helm 是什么，解决什么问题（K8s 的 yum/apt）
- Helm v3 架构（去掉了 Tiller）
- 常用命令：
  ```
  helm repo add bitnami https://charts.bitnami.com/
  helm search repo mysql
  helm install my-mysql bitnami/mysql
  helm list
  helm upgrade my-mysql bitnami/mysql --set auth.rootPassword=xxx
  helm uninstall my-mysql
  ```
- 自定义 values.yaml
- 编写自己的 Helm Chart

### 第六阶段：安全和维护（1 周）

#### RBAC 权限控制
- Role / ClusterRole / RoleBinding / ClusterRoleBinding
- ServiceAccount：Pod 的身份
- 实战：创建一个只能读取 Pod 的 ServiceAccount

#### 集群维护
- 备份 etcd：`ETCDCTL_API=3 etcdctl snapshot save`
- 恢复 etcd：`etcdctl snapshot restore`
- 升级 K8s 版本（kubeadm 方式）
- 节点维护：cordon / drain / uncordon

---

## 💻 实战 YAML 示例

### 示例 1：最简单的 Pod

```yaml
# basic-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.25
    ports:
    - containerPort: 80
```

### 示例 2：Deployment + Service

```yaml
# nginx-deployment.yaml
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
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
  type: ClusterIP
```

### 示例 3：ConfigMap 挂载配置文件

```yaml
# nginx-configmap.yaml
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
    }
---
# 在 Pod 中挂载
spec:
  containers:
  - name: nginx
    image: nginx
    volumeMounts:
    - name: conf
      mountPath: /etc/nginx/conf.d
  volumes:
  - name: conf
    configMap:
      name: nginx-conf
```

### 示例 4：Ingress 路由规则

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-svc
            port:
              number: 80
```

---

## 🧪 实战项目

### 项目 1：部署 WordPress（LNMP on K8s）

**目标**：把传统 LNMP 应用迁移到 K8s

**步骤**：
1. 创建 MySQL Deployment + PVC（数据持久化）
2. 把 MySQL 密码存到 Secret
3. 创建 WordPress Deployment，连接 MySQL
4. 创建 WordPress Service（ClusterIP）
5. 配置 Ingress，通过域名访问
6. 用 Helm 重新部署（用 bitnami 的 Chart）

**验收标准**：浏览器访问 `wordpress.example.com`，能完成初始化并登录后台。

### 项目 2：CI/CD 流水线（Jenkins + K8s）

**目标**：代码提交后自动构建镜像、推送到仓库、部署到 K8s

**步骤**：
1. Jenkins 安装 K8s 插件
2. 配置 Docker 仓库凭证
3. 编写 Jenkinsfile：
   - 拉取代码
   - 构建 Docker 镜像
   - 推送镜像到阿里云镜像仓库
   - 部署到 K8s（kubectl apply）
4. 配置 Webhook，实现自动触发

---

## 🔧 常见故障排查

### 故障 1：Pod 一直 ContainerCreating

**排查步骤**：
```bash
kubectl describe pod <pod-name>
# 查看 Events 部分，常见原因：
# - 镜像拉取失败（网络问题、镜像名写错）
# - PV 挂载失败（PVC 没绑定）
# - 节点资源不足（Insufficient cpu/memory）
```

**解决**：根据 Events 提示逐一排查。

### 故障 2：Service 无法访问 Pod

**排查步骤**：
```bash
# 1. 检查 Endpoints（Service 是否正确发现 Pod）
kubectl get endpoints <service-name>

# 2. 如果没有 Endpoints，检查 Label Selector 是否匹配
kubectl get pods --show-labels
kubectl get svc <name> -o yaml

# 3. 进入 Pod 测试网络
kubectl exec -it <pod-name> -- curl <service-ip>:<port>
```

### 故障 3：Ingress 返回 502

**常见原因**：
- 后端 Service 的 Port 名称和 Ingress 配置不匹配
- Pod 没就绪（readinessProbe 失败）
- 域名 DNS 没解析到 Ingress 控制器

---

## 💼 面试高频题

1. **K8s 的 Service 和 Ingress 有什么区别？**
   - Service：L4（TCP/UDP）负载均衡，集群内访问
   - Ingress：L7（HTTP/HTTPS）路由，支持域名和路径匹配，对外暴露

2. **Deployment 的滚动更新过程是怎样的？**
   - 创建新 ReplicaSet → 逐步扩容新版本 Pod → 逐步缩容旧版本 Pod

3. **PV 和 PVC 的关系是什么？**
   - PV：集群的存储资源（管理员创建）
   - PVC：用户对存储的请求（用户创建）
   - 绑定后，Pod 通过 PVC 使用存储

4. **livenessProbe 和 readinessProbe 的区别？**
   - livenessProbe：容器是否"活着"，失败会重启 Pod
   - readinessProbe：容器是否"准备好接收流量"，失败会从 Service Endpoints 移除

5. **K8s 网络模型（CNI）了解吗？**
   - 三层网络模型：Container ↔ Pod ↔ Service ↔ External
   - 常用 CNI：Flannel（简单）、Calico（高性能、支持网络策略）

---

## 📈 进阶学习路径

K8s 学完基础后，进阶方向：

- **深入原理**：读 K8s 源码（Go 语言）、《深入解析 Kubernetes》
- **服务网格**：学 Istio（流量管理、熔断、灰度发布）
- **GitOps**：学 ArgoCD（K8s 的 CD 工具）
- **运维实战**：多集群管理（Rancher / KubeFed）
- **认证**：考 CKA（Certified Kubernetes Administrator）

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 04 Docker 容器](../04_Container_Docker/)
- [CN 06 CI/CD](../06_CI_CD/)
- [CN 08 监控告警](../08_Monitoring/)
- [实时发现：K8s 相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · K8s 是绕不开的坎，但迈过去就值钱了</sub>
</p>
