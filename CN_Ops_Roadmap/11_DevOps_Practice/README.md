# 11 · DevOps 实践

> DevOps 不只是工具，是文化和合作方式。
> 这个模块讲 SRE 指标、GitOps、ChatOps、安全加固，是从"会工具"到"会做工程"的跨越。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 理解 DevOps 的核心文化和价值观
- [ ] 掌握 DORA 四大指标（部署频率、变更前置时间、变更失败率、恢复服务时间）
- [ ] 用 GitOps（ArgoCD）实现 K8s 的声明式部署
- [ ] 了解 ChatOps（用 IM 机器人操作运维）
- [ ] 配置安全加固（镜像扫描、网络策略、RBAC）
- [ ] 建立运维规范和 Review 流程
- [ ] 设计故障复盘（Blameless Postmortem）
- [ ] 能带领团队做 DevOps 转型

**学完这个模块，你能做 DevOps 负责人/团队 Lead。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| DevOps 从理念到实践 | 狂神说 | [B站](https://space.bilibili.com/423272454) | 20万+ | ⭐⭐⭐⭐ |
| GitOps with ArgoCD | 阳阳羊 | [B站](https://space.bilibili.com/391793870) | 10万+ | ⭐⭐⭐⭐ |
| SRE 实践 | 马哥 | [B站](https://space.bilibili.com/387633139) | 15万+ | ⭐⭐⭐⭐ |
| DORA 指标详解 | 阿里云 | [阿里云开发者社区](https://developer.aliyun.com/) | 官方 | ⭐⭐⭐⭐ |

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《DevOps 实践指南》 | Gene Kim 等 | 进阶 | DevOps 文化入门，讲为什么要做 DevOps |
| 《持续交付》 | Jez Humble | 高级 | CI/CD 理论基础，做流水线必读 |
| 《Accelerate》 | Nicole Forsgren 等 | 高级 | DORA 指标的来源，数据驱动 DevOps |
| 《SRE with Java》 | Vinoth Rathinam | 高级 | SRE 实战案例，Java 技术栈 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| Google SRE Books（免费） | https://sre.google/books/ | SRE 圣经，有中文翻译 |
| DORA Metrics 官方 | https://dora.dev/research/ | 四大指标定义和基准 |
| ArgoCD 文档 | https://argo-cd.readthedocs.io/ | GitOps 实践指南 |
| Open Guide to DevOps | https://github.com/open-guides/og-aws | AWS 运维开源指南 |

---

## 📝 核心知识点清单

### 第一阶段：DevOps 文化（1 周）

#### DevOps 是什么？

- **不是工具**：Jenkins ≠ DevOps
- **是一种文化**：开发和运维合作，共同对软件交付负责
- **核心原则**：
  1. 合作（打破部门墙）
  2. 自动化（重复的事让机器做）
  3. 持续反馈（快速失败、快速修复）
  4. 持续改进（测量 → 改进 → 再测量）

#### DORA 四大指标（衡量 DevOps 水平的金标准）

| 指标 | 定义 | 精英级 | 高水平 | 中水平 | 低水平 |
|------|------|---------|--------|--------|--------|
| 部署频率 | 代码部署到生产的频率 | 按需（每天多次） | 每天 - 每周 | 每月 - 每季 | 每季 - 每年 |
| 变更前置时间 | 从代码提交到部署的时间 | < 1 小时 | 1 天 - 1 周 | 1 月 - 6 月 | > 6 月 |
| 变更失败率 | 部署导致生产故障的比例 | 0-15% | 16-30% | 31-45% | > 45% |
| 恢复服务时间 | 故障后恢复服务的时间 | < 1 小时 | 1 小时 - 1 天 | 1 天 - 1 周 | > 1 周 |

---

### 第二阶段：GitOps 实践（2 周）

#### 为什么需要 GitOps？

传统 CI/CD 的问题：
- 部署状态不透明（不知道生产跑的是什么版本）
- 回滚慢（要重新构建）
- 配置漂移（手动改了生产，代码里没记录）

GitOps 解决思路：
- **Git 是唯一的真相来源**（所有配置都在 Git 里）
- **自动同步**（Git 变更 → 自动部署到 K8s）
- **一键回滚**（Git revert → 自动回滚）

#### ArgoCD 实战

```bash
# 1. 安装 ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# 2. 获取 Admin 密码
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

# 3. 访问 ArgoCD UI
kubectl port-forward -n argocd svc/argocd-server 8080:443

# 4. 创建 Application（声明式定义"要部署什么"）
```

```yaml
# app-of-apps.yaml — ArgoCD Application
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoUrl: https://github.com/your-org/your-repo.git
    targetRevision: main
    path: k8s/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: prod
  syncPolicy:
    automated:
      prune: true        # 自动删除 Git 里删掉的资源
      selfHeal: true    # K8s 里手动改了，自动改回来
```

#### GitOps 工作流

```
开发人员提交代码到 feature 分支
              ↓
       创建 PR（Pull Request）
              ↓
     CI 自动跑测试（必须全部通过）
              ↓
      Review 通过后合并到 main
              ↓
  ArgoCD 检测到 Git 变更（每 3 分钟轮询）
              ↓
    自动同步到 K8s 生产环境
              ↓
    发送通知到企业微信/Slack
```

---

### 第三阶段：SRE 实践（2 周）

#### SLI / SLO / SLA

| 概念 | 全称 | 定义 | 示例 |
|------|------|------|------|
| SLI | Service Level Indicator | 指标（实际测量值） | 可用率 = 99.9% |
| SLO | Service Level Objective | 目标（内部承诺） | 本月可用率目标 99.95% |
| SLA | Service Level Agreement | 协议（对客户承诺） | 对客户承诺 99.9%，不达标要赔偿 |

#### 错误预算（Error Budget）

- **定义**：100% - SLO = 允许不可用的时间
  - SLO 99.9% → 错误预算 = 0.1% = 每月约 43 分钟
- **用法**：
  - 错误预算充足 → 可以放开发布（快速迭代）
  - 错误预算耗尽 → 冻结发布（只修 Bug）
- **意义**：平衡「快速迭代」和「稳定性」

#### 故障复盘（Blameless Postmortem）

**原则**：对事不对人，目标是改进系统，不是找替罪羊。

**模板**：
```markdown
# 故障复盘：2024-06-15 支付服务中断

## 摘要
- 时间：2024-06-15 14:32 - 15:07（共 35 分钟）
- 影响：支付请求 100% 失败，约 1200 个订单受影响
- 严重等级：P0

## 时间线
- 14:32 — 发布 v2.3.1（含新支付接口）
- 14:33 — 监控告警：支付接口 HTTP 500 激增
- 14:35 — 值班工程师确认故障
- 14:40 — 决策：回滚到 v2.3.0
- 14:45 — 执行回滚
- 15:07 — 服务恢复正常

## 根因
新版本支付接口的连接池配置错误（maxConnections 设为 10，实际并发 100+）

## 影响面
- 总订单损失：约 ¥50,000
- 用户投诉：23 条

## 改进措施
- [ ] 立即：在测试环境模拟高并发，验证连接池配置（责任人：张三，截止：2024-06-20）
- [ ] 短期：CI/CD 加入压力测试步骤（责任人：李四，截止：2024-06-25）
- [ ] 长期：建立支付接口的 SLO（可用率 99.95%）和告警规则（责任人：王五，截止：2024-06-30）
```

---

### 第四阶段：ChatOps 实践（1 周）

#### 什么是 ChatOps？

- 在即时通讯工具（企业微信、钉钉、Slack）里用机器人操作运维
- 示例：
  - `@机器人 部署 my-app 到生产环境`
  - `@机器人 查看生产集群状态`
  - `@机器人 重启 payment-service`

#### 常见 ChatOps 工具

| 工具 | 适合场景 |
|------|---------|
| Slack + Hubot | 外企、配合 GitHub 好用 |
| 企业微信 + 自研机器人 | 国内企业 |
| 钉钉 + 自研机器人 | 阿里系企业 |
| Mattermost + Hubot | 私有化部署 |

---

### 第五阶段：安全加固（1 周）

#### 镜像安全

```bash
# 1. 镜像扫描（Trivy）
trivy image nginx:1.25
# 输出：CVE 漏洞列表、严重程度

# 2. 镜像签名（Docker Content Trust）
export DOCKER_CONTENT_TRUST=1
docker build -t my-app:v1 .
docker push my-app:v1
# 现在镜像必须用密钥签名，否则 push 失败

# 3. 用非 root 用户运行容器
# 在 Dockerfile 里：
RUN useradd -m app && chown -R app:app /app
USER app
CMD ["python", "app.py"]
```

#### K8s 安全

```yaml
# NetworkPolicy — 限制 Pod 间通信
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
# 效果：这个命名空间里的 Pod 完全不能通信（默认拒绝）

---
# 只允许前端访问后端
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
```

---

## 💻 实战命令/配置示例

### 用 ArgoCD 做金丝雀发布

```yaml
# rollouts-demo.yaml — 用 Argo Rollouts 实现金丝雀
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: my-app
spec:
  replicas: 10
  strategy:
    canary:
      steps:
      - setWeight: 10      # 先 10% 流量到新版本
      - pause: {duration: 5m}  # 观察 5 分钟
      - setWeight: 50
      - pause: {duration: 10m}
      - setWeight: 100
```

### 配置 Prometheus SLO 告警

```yaml
# slo-alert.yaml
groups:
- name: slo-alerts
  rules:
  - alert: LowAvailability
    expr: |
      (
        1 - (
          sum(rate(http_requests_total{code=~"5.."}[5m]))
          / sum(rate(http_requests_total[5m]))
        )
      ) < 0.999  # 可用率 < 99.9%
    for: 10m
    labels:
      severity: critical
    annotations:
      summary: "可用率低于 SLO 目标（当前：{{ $value | printf \"%.3f\" }}）"
```

---

## 🧪 实战项目

### 项目 1：搭建完整的 GitOps 流水线

**目标**：代码合并到 main 后，自动部署到 K8s，且在 ArgoCD UI 可观测。

**步骤**：
1. 安装 ArgoCD
2. 创建 Git 仓库，存放 K8s YAML 文件
3. 在 ArgoCD 里创建 Application，指向 Git 仓库
4. 修改 Git 里的 YAML（改镜像版本），观察 ArgoCD 自动同步
5. 配置 ArgoCD 通知（发送到企业微信）

### 项目 2：建立团队的 SRE 指标体系

**目标**：为你的服务定义 SLI/SLO，并配置告警。

**步骤**：
1. 选取核心服务的 3 个关键指标（可用率、延迟、错误率）
2. 在 Prometheus 里计算 SLI
3. 定义 SLO（比如：可用率 99.95%）
4. 配置错误预算告警（剩余预算 < 20% 时告警）
5. 写一份 SLO 文档，和团队对齐

---

## 🔧 常见故障排查

### 故障 1：ArgoCD 同步失败

**排查步骤**：
```bash
# 1. 查看 Application 状态
argocd app get my-app

# 2. 查看同步失败原因
argocd app logs my-app

# 3. 常见原因：
# - Git 仓库访问失败（检查凭证）
# - K8s 集群权限不足（检查 RBAC）
# - YAML 语法错误（用 kubectl apply --dry-run=client 预检查）
```

### 故障 2：SLO 告警太敏感（频繁误报）

**解决**：调整时间窗口和容忍度
```yaml
# 改为：15 分钟内错误率 > 1% 才告警（避免短暂波动触发）
expr: |
  (
    sum(rate(http_requests_total{code=~"5.."}[15m]))
    / sum(rate(http_requests_total[15m]))
  ) > 0.01
for: 15m
```

---

## 💼 面试高频题

1. **DORA 四大指标是什么？你们团队达到了什么水平？**
   - 按记忆回答四大指标
   - 真实数据：部署频率（我们每周 3 次）、变更前置时间（2 小时左右）

2. **SLO 和 SLA 的区别？**
   - SLO 是内部目标（激励团队）
   - SLA 是对外承诺（法律效力）

3. **如何推动团队从「传统运维」转向 DevOps？**
   - 先建立共识（为什么要变）
   - 选一个试点项目（别一上来就全公司推）
   - 建立指标（DORA 四大指标，定期回顾）
   - 庆祝小胜利（第一次自动部署成功，要宣传）

4. **ChatOps 在实际工作中有哪些坑？**
   - 权限控制（不能让所有人都能操作生产）
   - 操作审计（所有通过机器人的操作必须记录）
   - 误操作和回滚机制

---

## 📈 进阶学习路径

- **可观测性**：学 OpenTelemetry（统一 Trace/Metric/Log）
- **平台工程**：学 Backstage（开发者自助平台）
- **混沌工程**：学 Chaos Mesh（主动注入故障，验证系统韧性）
- **DevSecOps**：把安全扫描集成到 CI/CD（在流水线里扫漏洞）

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 05 Kubernetes](../05_Kubernetes/)
- [CN 06 CI/CD](../06_CI_CD/)
- [CN 08 监控告警](../08_Monitoring/)
- [实时发现：DevOps 相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · DevOps 的核心是人，不是工具</sub>
</p>
