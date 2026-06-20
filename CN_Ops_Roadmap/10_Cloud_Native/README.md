# 10 · 云原生实践

> 云原生不只是"上云"，是一套架构思想和工程实践。
> 这个模块涵盖国内主流云厂商实战、Terraform、Ansible、Service Mesh。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 理解云原生的核心理念（容器、微服务、DevOps、持续交付）
- [ ] 熟练使用阿里云/腾讯云核心产品（ECS、SLB、RDS、OSS）
- [ ] 用 Terraform 管理云基础设施（IaC）
- [ ] 用 Ansible 做配置管理和应用部署
- [ ] 理解并部署 Service Mesh（Istio）
- [ ] 配置多集群管理（Rancher / KubeFed）
- [ ] 了解 FinOps（云成本优化）
- [ ] 能设计云原生架构方案

**学完这个模块，你能做云架构师方向。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| 阿里云 ACE 认证课程 | 阿里云 | [阿里云开发者社区](https://developer.aliyun.com/) | 官方 | ⭐⭐⭐⭐⭐ |
| 腾讯云 TCP 认证 | 腾讯云 | [腾讯云学堂](https://cloud.tencent.com/edu) | 官方 | ⭐⭐⭐⭐⭐ |
| Terraform 从入门到实战 | 阳阳羊 | [B站](https://space.bilibili.com/391793870) | 15万+ | ⭐⭐⭐⭐ |
| Istio 服务网格 | 马哥 | [B站](https://space.bilibili.com/387633139) | 10万+ | ⭐⭐⭐⭐ |
| 多云管理 Rancher | 狂神说 | [B站](https://www.bilibili.com/video/BV1Sv411r7vd) | 20万+ | ⭐⭐⭐⭐ |

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《云原生应用架构实践》 | 程序员DD | 高级 | Spring Cloud 和 K8s 结合，微服务方向 |
| 《Terraform 实战（第2版）》 | O'Reilly | 高级 | IaC 圣经，有中文版 |
| 《Istio 实战》 | 机械工业出版社 | 专家 | Service Mesh 入门，中文案例多 |
| 《Cloud Native Patterns》 | Cornelia Davis | 高级 | 云原生设计模式，英文原版更好 |
| 《FinOps 云成本管理》 | J.R. Storment | 专家 | 降本增效，大厂都在做 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| 阿里云文档中心 | https://help.aliyun.com/ | 中文最全，实战案例多 |
| 腾讯云文档中心 | https://cloud.tencent.com/document/ | 国内第二大云厂商文档 |
| Terraform 官方文档（中文） | https://www.terraform.io/language | HasiCorp 官方 |
| Istio 官方文档（中文） | https://istio.io/latest/docs/ | Service Mesh 权威指南 |
| Rancher 文档 | https://docs.rancher.cn/ | 多集群管理平台 |
| CNCF Landscape | https://landscape.cncf.io/ | 云原生全家桶，选型参考 |

---

## 📝 核心知识点清单

### 第一阶段：云原生基础（1 周）

#### 什么是云原生？

CNCF（云原生计算基金会）定义：

1. **容器化**：所有服务跑在容器中
2. **微服务**：把单体应用拆成小服务
3. **DevOps**：开发和运维协作，自动化交付
4. **持续交付**：代码提交后自动发布

#### 国内主流云产品对照

| 产品类型 | 阿里云 | 腾讯云 | 华为云 | AWS |
|-----------|--------|--------|--------|-----|
| 云服务器 | ECS | CVM | ECS | EC2 |
| 对象存储 | OSS | COS | OBS | S3 |
| 关系型数据库 | RDS | TencentDB | RDS | RDS |
| 负载均衡 | SLB | CLB | ELB | ALB |
| 容器服务 | ACK | TKE | CCE | EKS |
| 函数计算 | FC | SCF | FunctionGraph | Lambda |

### 第二阶段：Terraform IaC（2 周）

#### 为什么需要 IaC？

- **可重现**：代码定义基础设施，随时重建
- **版本控制**：Infra 代码提交到 Git，可追溯
- **自动化**：`terraform apply` 一条命令部署全套环境

#### Terraform 基础

```hcl
# main.tf — 在阿里云创建一台 ECS

terraform {
  required_providers {
    aliyun = {
      source  = "aliyun/aliyun"
      version = "~> 1.200.0"
    }
  }
}

provider "aliyun" {
  region = "cn-hangzhou"
}

resource "aliyun_instance" "web" {
  instance_name = "web-server"
  image_id      = "centos_7_9_x64_20G_alibase_20230601.vhd"
  instance_type = "ecs.t5-lc1m1.small"
  security_groups = [aliyun_security_group.default.id]
  vswitch_id     = aliyun_vswitch.default.id

  tags = {
    Name    = "web-server"
    Env     = "prod"
    ManagedBy = "terraform"
  }
}

resource "aliyun_security_group" "default" {
  name = "web-sg"
}

resource "aliyun_security_group_rule" "ssh" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "intranet"
  policy            = "accept"
  port_range        = "22/22"
  security_group_id = aliyun_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}
```

```bash
# 初始化（下载 Provider 插件）
terraform init

# 检查配置是否有语法错误
terraform validate

# 预览要创建的资源（不实际执行）
terraform plan

# 应用配置（创建资源）
terraform apply

# 销毁资源
terraform destroy
```

#### 模块化 Terraform

```hcl
# modules/ecs/main.tf
variable "instance_name" {}
variable "instance_type" { default = "ecs.t5-lc1m1.small" }

resource "aliyun_instance" "this" {
  instance_name = var.instance_name
  instance_type = var.instance_type
  # ...
}

output "private_ip" {
  value = aliyun_instance.this.private_ip
}

# 使用模块
module "web" {
  source         = "./modules/ecs"
  instance_name = "web-server"
  instance_type = "ecs.c6.large"
}
```

### 第三阶段：Ansible 配置管理（1-2 周）

#### Ansible vs Terraform

| | Terraform | Ansible |
|--|------------|----------|
| 定位 | 基础设施编排（创建资源） | 配置管理（软件安装、配置） |
| 状态 | 有状态文件（记录已创建资源） | 无状态（每次都重新执行） |
| 语言 | HCL | YAML |
| Agent | 不需要 | 不需要（用 SSH） |

#### Ansible Playbook 示例

```yaml
# deploy-web.yml — 部署 Nginx

- name: Deploy Nginx on web servers
  hosts: webservers
  become: yes  # sudo
  vars:
    nginx_port: 80

  tasks:
    - name: Install Nginx
      yum:
        name: nginx
        state: present

    - name: Copy Nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart Nginx  # 配置文件变了就重启

    - name: Start Nginx
      service:
        name: nginx
        state: started
        enabled: yes

  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

```bash
# 执行 Playbook
ansible-playbook -i inventory.ini deploy-web.yml

# inventory.ini 示例
[webservers]
192.168.56.101
192.168.56.102
192.168.56.103
```

### 第四阶段：Service Mesh（2 周）

#### 为什么需要 Service Mesh？

K8s 原生的服务通信能力有限：
- 没有流量管理（熔断、限流、超时）
- 没有安全策略（mTLS、服务间认证）
- 没有可观测性（调用链追踪、指标）

Istio 解决这些问题，且对业务代码无侵入。

#### Istio 核心概念

```
Istio 架构：
┌─────────────────────────────────────────────┐
│              Control Plane（istiod）          │
│  - 服务发现                                        │
│  - 配置分发                                       │
│  - 证书管理                                       │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│           Data Plane（Envoy Sidecar）         │
│  每个 Pod 注入一个 Envoy 代理              │
│  所有流量都经过 Sidecar                │
└─────────────────────────────────────────────┘
```

#### Istio 安装和实战

```bash
# 安装 Istio
curl -L https://istio.io/downloadIstio | sh -
cd istio-*.* && export PATH=$PWD/bin:$PATH
istioctl install --set profile=demo -y

# 注入 Sidecar（两种方式）
# 方式 1：命名空间级别自动注入
kubectl label namespace default istio-injection=enabled

# 方式 2：Pod 级别手动注入
istioctl kube-inject -f deployment.yaml | kubectl apply -f -
```

```yaml
# 配置流量规则：熔断
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: web-circuit-breaker
spec:
  host: web-svc
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 10
      consecutiveErrors: 3
```

### 第五阶段：FinOps 云成本优化（1 周）

#### 常见的浪费

1. **资源闲置**：服务器上周利用率 < 10%
2. ** over-provisioning**：申请 8 核 16GB，实际只用 2 核 4GB
3. **未删除的测试环境**：开发测试完忘了删
4. **存储浪费**：OSS/COS 里有很多不再访问的文件

#### 优化策略

```bash
# 1. 查看资源利用率（Prometheus + Grafana）
# 找出 CPU 利用率 < 10% 的 Pod

# 2. 用 K8s VPA（Vertical Pod Autoscaler）自动调整资源
kubectl apply -f - <<EOF
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: web-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  updatePolicy:
    updateMode: "Auto"
EOF

# 3. 用 HPA（Horizontal Pod Autoscaler）自动扩缩容
kubectl autoscale deployment web --min=2 --max=10 --cpu-percent=50

# 4. 定时扩缩容（CronHPA）
# 白天扩容、晚上缩容，节省成本
```

---

## 💻 实战命令/配置示例

### Terraform 管理 K8s 集群（阿里云 ACK）

```hcl
resource "aliyun_cs_kubernetes" "ack" {
  name               = "my-ack-cluster"
  cluster_spec       = "ack.standard"
  version            = "1.28.0-aliyun.1"
  worker_instance_types = ["ecs.c6.large"]
  worker_number      = 3
  pod_cidr             = "172.20.0.0/16"
  service_cidr         = "172.21.0.0/20"
  enable_ssh          = true
  load_balancer_spec = "slb.s1.small"

  tags = {
    Environment = "prod"
  }
}

output "cluster_endpoint" {
  value = aliyun_cs_kubernetes.ack.connections[0].api_server_endpoint
}
```

### Ansible 批量部署 K8s 集群

```yaml
# 用 Ansible 初始化 K8s Master 节点
- name: Initialize K8s Master
  hosts: masters
  become: yes
  tasks:
    - name: Disable swap
      shell: swapoff -a

    - name: Add Kubernetes repository
      yum_repository:
        name: kubernetes
        description: Kubernetes repo
        baseurl: https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
        enabled: yes

    - name: Install K8s components
      yum:
        name:
          - kubelet-1.28.0
          - kubeadm-1.28.0
          - kubectl-1.28.0
        state: present

    - name: Initialize K8s cluster
      shell: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
```

---

## 🧪 实战项目

### 项目 1：用 Terraform + Ansible 部署完整 Web 架构

**目标**：代码化整个基础设施和应用部署。

**步骤**：
1. Terraform 创建 VPC、交换机、安全组、ECS（3 台）
2. Terraform 输出 ECS IP 到 Ansible Inventory
3. Ansible 在 ECS 上安装 Docker、K8s
4. Ansible 部署 Nginx（K8s Deployment）
5. Terraform 创建 SLB（负载均衡），绑定 ECS
6. 验证：访问 SLB IP，看到 Nginx 欢迎页

**成果**：一条命令重建整个架构 `terraform destroy && terraform apply`

### 项目 2：灰度发布系统（Istio）

**目标**：实现基于权重的灰度发布。

**步骤**：
1. 部署 v1 和 v2 两个版本的应用
2. 配置 VirtualService，v1 权重 90%，v2 权重 10%
3. 观察 v2 的错误率和延迟
4. 如果正常，逐步调整权重到 100%
5. 如果异常，立即回滚（权重改回 100%/0%）

---

## 🔧 常见故障排查

### 故障 1：Terraform state 文件冲突

**场景**：团队多人协作，state 文件被覆盖。

**解决**：用远程 Backend（OSS/COS/S3）存储 state
```hcl
terraform {
  backend "oss" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    endpoint = "oss-cn-hangzhou.aliyuncs.com"
    acl    = "private"
  }
}
```

### 故障 2：Istio Sidecar 注入失败

**排查**：
```bash
# 检查命名空间是否启用了注入
kubectl get namespace default -o yaml | grep istio-injection

# 检查 Pod 是否有 istio-proxy 容器
kubectl describe pod <pod-name>
# 看 Containers 部分，应该有 2 个容器（业务容器 + istio-proxy）

# 查看 Sidecar 注入日志
kubectl logs -l app=web -c istio-proxy
```

### 故障 3：云服务器费用超标

**排查**：
```bash
# 用阿里云费用中心 API 拉取账单
# 找出费用最高的资源类型

# 常见原因：
# 1. 按量付费的 ECS 没有释放
# 2. OSS 存储了大量不再访问的文件
# 3. SLB（负载均衡）闲置

# 设置费用告警（阿里云支持）
# 费用 > ¥500/月 → 发短信告警
```

---

## 💼 面试高频题

1. **Terraform 的 state 文件是做什么的？**
   - 记录当前基础设施的实际状态
   - Terraform 用 state 和实际资源对比，决定要创建/修改/删除什么
   - **不能删除 state 文件**，删了 Terraform 就"失忆"了

2. **Istio 和 Nginx Ingress 的区别？**
   - Nginx Ingress：L7 路由，适合简单的入口流量管理
   - Istio：服务网格，管理服务间所有通信（东西向 + 南北向），功能强得多

3. **云原生和传统架构的核心区别？**
   - 传统：单体应用、手动部署、垂直扩容
   - 云原生：微服务、自动部署、水平扩容、容器化

4. **如何设计一个高可用云架构？**
   - 多可用区部署（防单机房故障）
   - 负载均衡（SLB/ALB）
   - 数据库主从 + 自动故障切换
   - 对象存储（OSS/COS）存静态文件
   - CDN 加速静态资源

---

## 📈 进阶学习路径

- **Certification**：考阿里云 ACE / 腾讯云 TCP 高级认证
- **多云管理**：学 Crossplane（Terraform 的 K8s 原生替代）
- **平台工程**：学 Backstage（开发者自助平台）
- **FinOps**：深入分析云账单，做成本优化项目

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 05 Kubernetes](../05_Kubernetes/)
- [CN 06 CI/CD](../06_CI_CD/)
- [CN 11 DevOps 实践](../11_DevOps_Practice/)
- [实时发现：云原生相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · 云原生的核心是"可观测 + 可控制"，不是"上云"</sub>
</p>
