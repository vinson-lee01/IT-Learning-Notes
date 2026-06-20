# 06 · CI/CD 持续集成与持续交付

> CI/CD 是 DevOps 的核心实践。自动化的构建、测试、部署流水线是现代软件交付的标配。
> 学会这个，你就能把「发版要看天」变成「点一下就上线」。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 理解 CI/CD 的基本概念和价值
- [ ] 搭建 Jenkins 并编写 Jenkinsfile（Pipeline as Code）
- [ ] 配置 GitLab CI/CD（`.gitlab-ci.yml`）
- [ ] 使用 GitHub Actions 实现开源项目的 CI
- [ ] 理解并实践蓝绿部署、金丝雀发布、滚动更新
- [ ] 配置构建制品管理（Docker 镜像仓库）
- [ ] 集成代码质量扫描（SonarQube）
- [ ] 实现自动化回滚机制
- [ ] 管理 CI/CD 中的敏感信息（凭证、Token）
- [ ] 排查流水线故障

**学完这个模块，你能主导团队的 CI/CD 建设。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| Jenkins 从入门到精通 | 黑马程序员 | [B站 BV1kJ411p7mV](https://www.bilibili.com/video/BV1kJ411p7mV) | 80万+ | ⭐⭐⭐⭐⭐ |
| GitLab CI/CD 实战 | 尚硅谷 | [B站](https://www.bilibili.com/video/BV1Kv4y1Z7Rf) | 30万+ | ⭐⭐⭐⭐ |
| GitHub Actions 实战 | 狂神说 | [B站](https://www.bilibili.com/video/BV1Sv411r7vd) | 50万+ | ⭐⭐⭐⭐ |
| ArgoCD GitOps | 阳阳羊 | [B站](https://space.bilibili.com/391793870) | 10万+ | ⭐⭐⭐⭐ |
| Jenkins + K8s 集成 | 马哥 | [B站](https://space.bilibili.com/387633139) | 20万+ | ⭐⭐⭐⭐ |

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《Jenkins 2 权威指南》 | 清华大学出版社 | 高级 | Jenkins 专题，Jenkinsfile 讲得细 |
| 《持续交付》 | Jez Humble | 高级 | CI/CD 理论基础，做流水线必读 |
| 《Accelerate》 | Nicole Forsgren | 高级 | DORA 指标的来源，数据驱动 DevOps |
| 《GitLab CI/CD 实战》 | 电子工业出版社 | 中级 | .gitlab-ci.yml 配置详解 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| Jenkins 官方文档 | https://www.jenkins.io/doc/ | 最权威，插件文档全 |
| GitLab CI/CD 文档 | https://docs.gitlab.com/ee/ci/ | .gitlab-ci.yml 配置参考 |
| GitHub Actions 文档 | https://docs.github.com/en/actions | 官方示例丰富 |
| ArgoCD 文档 | https://argo-cd.readthedocs.io/ | GitOps 实践指南 |
| jenkinsci/pipeline-examples | https://github.com/jenkinsci/pipeline-examples | ⭐2.1k，Jenkinsfile 示例集 |

---

## 📝 核心知识点清单

### 第一阶段：CI/CD 基础（1 周）

#### 什么是 CI/CD？

- **CI（持续集成）**：代码合并到主干后自动构建、测试
- **CD（持续交付）**：代码通过测试后自动部署到预发布环境
- **CD（持续部署）**：代码通过测试后自动部署到生产环境（无人工干预）
- 价值：减少人工操作、快速反馈、降低发布风险

#### 经典 CI/CD 流程

```
开发人员提交代码
        ↓
    触发 CI 流水线
        ↓
    自动构建（编译/打包）
        ↓
    自动测试（单元/集成/接口）
        ↓
    构建失败 → 通知开发人员
        ↓（构建成功）
    打包 Docker 镜像
        ↓
    推送到镜像仓库
        ↓
    自动部署到测试环境
        ↓
    自动化验收测试
        ↓
    人工确认（持续交付）或自动部署（持续部署）
        ↓
    部署到生产环境
        ↓
    健康检查 + 监控告警
```

### 第二阶段：Jenkins 实战（2 周）

#### Jenkins 安装与配置

```bash
# Docker 方式安装（推荐，最快）
docker run -d \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

# 获取初始管理员密码
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

#### Jenkinsfile（Pipeline as Code）

```groovy
// Jenkinsfile — 声明式流水线
pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'registry.cn-hangzhou.aliyuncs.com/my-repo'
        APP_NAME = 'my-app'
        BUILD_VERSION = "${BUILD_NUMBER}"
    }

    stages {
        stage('1. 拉取代码') {
            steps {
                git branch: 'main', url: 'https://github.com/xxx/my-app.git'
            }
        }

        stage('2. 单元测试') {
            steps {
                sh 'npm test'
            }
            post {
                failure {
                    mail to: 'dev-team@company.com',
                         subject: '单元测试失败',
                         body: "构建 ${BUILD_NUMBER} 失败，请及时处理"
                }
            }
        }

        stage('3. 构建 Docker 镜像') {
            steps {
                sh "docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_VERSION} ."
            }
        }

        stage('4. 推送镜像') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aliyun-docker-registry',
                    usernameVariable: 'REGISTRY_USER',
                    passwordVariable: 'REGISTRY_PASS'
                )]) {
                    sh "docker login -u ${REGISTRY_USER} -p ${REGISTRY_PASS} ${DOCKER_REGISTRY}"
                    sh "docker push ${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_VERSION}"
                }
            }
        }

        stage('5. 部署到测试环境') {
            steps {
                sh "kubectl set image deployment/my-app my-app=${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_VERSION} -n test"
                sh "kubectl rollout status deployment/my-app -n test"
            }
        }
    }

    post {
        success {
            echo '流水线执行成功！'
        }
        failure {
            echo '流水线执行失败，请排查！'
        }
    }
}
```

### 第三阶段：GitLab CI/CD（1 周）

#### `.gitlab-ci.yml` 配置

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

# 单元测试
unit_test:
  stage: test
  image: node:18
  script:
    - npm install
    - npm test
  only:
    - merge_requests
    - main

# 构建 Docker 镜像
build_image:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_TAG .
    - docker push $IMAGE_TAG
  only:
    - main

# 部署到生产环境
deploy_prod:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context $KUBE_CONTEXT
    - kubectl set image deployment/app app=$IMAGE_TAG -n prod
    - kubectl rollout status deployment/app -n prod
  only:
    - main
  when: manual  # 需要人工点击确认
```

### 第四阶段：GitHub Actions（1 周）

#### 工作流配置

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm test

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          push: true
          tags: my-app:${{ github.sha }}

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to K8s
        uses: azure/k8s-deploy@v1
        with:
          namespace: prod
          manifests: |
            k8s/deployment.yaml
            k8s/service.yaml
```

### 第五阶段：发布策略（1 周）

#### 蓝绿部署（Blue-Green Deployment）

- 同时运行两套环境：蓝（当前版本）和绿（新版本）
- 切换流量从蓝到绿
- 优点：瞬间切换、容易回滚
- 缺点：资源消耗翻倍

```bash
# 示例：用 Service selector 切换
# 蓝环境：version: blue
# 绿环境：version: green

kubectl patch svc my-app -p '{"spec":{"selector":{"version":"green"}}}'
# 切换完成，绿环境接收所有流量
```

#### 金丝雀发布（Canary Release）

- 先让小部分用户（比如 5%）访问新版本
- 观察指标（错误率、延迟）
- 逐步扩大比例，直到 100%
- 优点：风险可控，能真实测试新版本
- 工具：Nginx/Ingress、Istio、Flagger

```yaml
# Ingress 金丝雀配置示例
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-canary
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "10"  # 10% 流量
spec:
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-canary
            port:
              number: 80
```

#### 滚动更新（Rolling Update）

- K8s Deployment 默认策略
- 逐步用新版本 Pod 替换旧版本 Pod
- 优点：资源消耗少
- 缺点：新旧版本共存期间可能有兼容性问题

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # 最多比期望副本多几个
      maxUnavailable: 0  # 更新期间最少保持几个可用副本
```

---

## 💻 实战项目

### 项目 1：搭建完整的 Jenkins CI/CD 流水线

**目标**：实现代码提交 → 自动构建 → 自动测试 → 自动部署

**步骤**：
1. Docker 安装 Jenkins，安装必要插件（Git、Docker、Kubernetes）
2. 配置 JDK、Node.js、Docker 环境
3. 创建多分支流水线项目
4. 编写 Jenkinsfile（参考上面示例）
5. 配置 Webhook（GitHub → Jenkins）
6. 模拟提交代码，观察流水线自动执行
7. 加入 SonarQube 代码质量扫描

**验收标准**：往 `main` 分支提交代码，5 分钟内自动完成构建、测试、部署。

### 项目 2：用 GitHub Actions 做开源项目的 CI

**目标**：给自己的开源项目配置 CI，提升专业度

**步骤**：
1. 在 GitHub 仓库创建 `.github/workflows/ci.yml`
2. 配置代码检查（ESLint/Prettier）
3. 配置单元测试（Jest）
4. 配置自动构建 Docker 镜像
5. 配置自动发布到 Docker Hub
6. 配置 PR 合并前必须通过 CI

---

## 🔧 常见故障排查

### 故障 1：Jenkins 流水线卡住不动

**排查步骤**：
```bash
# 1. 检查 Jenkins 日志
docker logs jenkins

# 2. 检查节点状态（是否被禁用了）
# Jenkins → 系统管理 → 节点管理

# 3. 检查流水线是否等待人工输入
# 在 Blue Ocean 页面查看，是否有暂停的步骤
```

### 故障 2：kubectl 在 Jenkins 中执行失败（权限问题）

**解决**：配置 RBAC，给 Jenkins ServiceAccount 授权
```yaml
# jenkins-rbac.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: jenkins-admin
subjects:
- kind: ServiceAccount
  name: jenkins
  namespace: jenkins
roleRef:
  kind: ClusterRole
  name: cluster-admin  # 生产环境应该用更精细的权限
  apiGroup: rbac.authorization.k8s.io
```

### 故障 3：Docker 镜像拉取失败（dind 问题）

**常见原因**：Jenkins 运行在容器中，Docker 命令需要访问宿主机的 Docker daemon

**解决**：挂载宿主机的 Docker socket
```bash
docker run -d \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(which docker):/usr/bin/docker \
  jenkins/jenkins:lts
```

---

## 💼 面试高频题

1. **Jenkinsfile 的声明式和脚本式有什么区别？**
   - 声明式：结构清晰、有固定的 `pipeline`/`stages`/`steps` 结构，更易读
   - 脚本式：更灵活，用 `node` 和自由 Groovy 代码，适合复杂逻辑

2. **蓝绿部署和金丝雀发布怎么选？**
   - 蓝绿：适合对资源不敏感、要求瞬间切换的场景
   - 金丝雀：适合对风险敏感、希望逐步验证新版本的场景

3. **CI/CD 流水线中的敏感信息（密码、Token）怎么管理？**
   - Jenkins：用 Credentials 绑定，在 Jenkinsfile 中用 `withCredentials` 引用
   - GitLab CI：用 CI/CD Variables（Settings → CI/CD → Variables）
   - GitHub Actions：用 Secrets（Settings → Secrets and variables → Actions）

4. **如何保证部署的幂等性？**
   - K8s：`kubectl apply` 天然幂等
   - Terraform：`terraform apply` 会检测实际状态和期望状态的差异

---

## 📈 进阶学习路径

- **GitOps**：学 ArgoCD / FluxCD（K8s 原生的 CD 工具）
- **高级发布策略**：学 Istio 流量管理（熔断、限流、灰度）
- **CI/CD 安全**：学 DevSecOps（在流水线中集成安全扫描）
- **大模型辅助**：用 GitHub Copilot 生成 Jenkinsfile / .gitlab-ci.yml

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 05 Kubernetes](../05_Kubernetes/)
- [CN 07 Web 服务器](../07_Web_Servers/)
- [CN 11 DevOps 实践](../11_DevOps_Practice/)
- [实时发现：CI/CD 相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · 发版不用熬到凌晨，是 CI/CD 给的底气</sub>
</p>
