# 04 · Docker 容器化

> Docker 是现代运维的必修课。不懂容器，K8s 也学不好。
> 这个模块从安装到生产实践，一步一步来。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 理解容器和虚拟机的区别
- [ ] 安装和配置 Docker（ daemon.json 调优）
- [ ] 熟练使用 Docker 基础命令（run/exec/logs/rm 等）
- [ ] 编写生产级 Dockerfile（多阶段构建、安全最佳实践）
- [ ] 使用 Docker Compose 编排多容器应用
- [ ] 配置 Docker 网络（bridge/host/overlay）
- [ ] 配置 Docker 存储（volume/bind mount/tmpfs）
- [ ] 搭建和使用私有镜像仓库（Harbor）
- [ ] 掌握 Docker 安全加固（非 root 用户、镜像扫描）
- [ ] 能排查容器常见故障

**学完这个模块，你能把任何应用装进容器跑起来。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| Docker 从入门到实战 | 狂神说 | [B站 BV1og4y1q7M4](https://www.bilibili.com/video/BV1og4y1q7M4) | 300万+ | ⭐⭐⭐⭐⭐ |
| Docker 容器化技术 | 尚硅谷 | [B站](https://www.bilibili.com/video/BV1sK4y1C7T5) | 80万+ | ⭐⭐⭐⭐ |
| Docker Compose 实战 | IT 老齐 | [B站](https://space.bilibili.com/383016053) | 20万+ | ⭐⭐⭐⭐ |
| Harbor 私有仓库 | 马哥 | [B站](https://space.bilibili.com/387633139) | 10万+ | ⭐⭐⭐⭐ |

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《Docker 进阶与实战》 | 华为 Docker 团队 | 高级 | 华为团队写的，有内部实践经验 |
| 《Docker 从入门到实践》 | 异步社区 | 入门 | 中文，跟着做一遍就能上手 |
| 《Docker in Action（第2版）》 | O'Reilly | 中级 | 最好的 Docker 英文书，有中文版 |
| 《Docker 全栈实践》 | 奇虎360 | 高级 | 360 内部实践，安全专题讲得好 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| Docker 官方文档（中文） | https://docs.docker.com/ | 最权威，必看 |
| Docker 中文社区 | https://www.docker8.com/ | 中文翻译，入门友好 |
| Play with Docker | https://labs.play-with-docker.com/ | 在线实验，免费 |
| harbor/harbor | https://github.com/goharbor/harbor | ⭐15k，企业级私有仓库 |
| awesome-docker | https://github.com/veggiemonk/awesome-docker | Docker 资源合集 |

---

## 📝 核心知识点清单

### 第一阶段：Docker 基础和安装（3-5 天）

#### 容器 vs 虚拟机

```
虚拟机：
  硬件 → Hypervisor → Guest OS × N → App × N
  特点：隔离性好，但重（每个 VM 都有完整 OS）

容器：
  硬件 → Host OS → Docker Engine → Container × N
  特点：轻量（共享 Host OS 内核），秒级启动
```

#### 安装 Docker（CentOS 7/8）

```bash
# 1. 卸载旧版本
yum remove -y docker docker-common docker-selinux docker-engine

# 2. 安装依赖
yum install -y yum-utils device-mapper-persistent-data lvm2

# 3. 添加 Docker 仓库（用阿里云镜像加速）
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 4. 安装 Docker
yum install -y docker-ce docker-ce-cli containerd.io

# 5. 配置镜像加速（必做，不然拉镜像很慢）
mkdir -p /etc/docker
cat > /etc/docker/daemon.json << EOF
{
  "registry-mirrors": [
    "https://mirror.ccs.tencentyun.com",
    "https://registry.docker-cn.com"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  },
  "storage-driver": "overlay2"
}
EOF

# 6. 启动 Docker
systemctl enable docker
systemctl start docker

# 7. 验证
docker version
docker info
```

#### Docker 基础命令

```bash
# 镜像操作
docker search nginx              # 搜索镜像
docker pull nginx:1.25            # 拉取镜像
docker images                      # 列出本地镜像
docker rmi nginx:1.25            # 删除镜像
docker build -t my-app:v1 .      # 构建镜像（当前目录的 Dockerfile）

# 容器操作
docker run -d --name my-nginx -p 8080:80 nginx:1.25
                                # 启动容器（-d 后台运行，--name 指定名字，-p 端口映射）
docker ps                          # 列出运行中的容器
docker ps -a                       # 列出所有容器（包括停止的）
docker exec -it my-nginx /bin/bash   # 进入容器
docker logs my-nginx              # 查看容器日志
docker logs -f --tail 100 my-nginx   # 实时查看最后 100 行日志
docker stop my-nginx              # 停止容器
docker start my-nginx             # 启动已停止的容器
docker rm my-nginx               # 删除容器（需先停止）
docker rm -f my-nginx             # 强制删除（不需先停止）

# 清理（慎用！）
docker system prune -a               # 删除所有未使用的镜像、容器、网络
```

### 第二阶段：Dockerfile 编写（1 周）

#### 最简单的 Dockerfile

```dockerfile
# Dockerfile
FROM nginx:1.25
LABEL maintainer="vinson-lee"
COPY index.html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### 生产级 Dockerfile（多阶段构建）

```dockerfile
# 阶段 1：构建
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 阶段 2：运行（最终镜像只有构建产物，很小）
FROM nginx:1.25-alpine
COPY --from=builder /app/dist /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### Dockerfile 最佳实践

```dockerfile
# ✅ 推荐
FROM python:3.11-slim           # 用 slim/alpine 版本，镜像更小
WORKDIR /app                    # 用 WORKDIR，不用 RUN cd
COPY requirements.txt .          # 分开 COPY，利用缓存
RUN pip install -r requirements.txt
COPY . .                          # 最后 COPY 代码（改动频繁）
RUN useradd -m app && chown -R app:app /app
USER app                          # 用非 root 用户运行
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1   # 健康检查
EXPOSE 8080
CMD ["python", "app.py"]
```

### 第三阶段：Docker Compose（1 周）

#### 用 Compose 部署 LNMP

```yaml
# docker-compose.yml
version: '3.8'

services:
  nginx:
    image: nginx:1.25
    container_name: lnmp-nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - ./html:/usr/share/nginx/html
    depends_on:
      - php
    networks:
      - lnmp-net

  php:
    image: php:8.2-fpm
    container_name: lnmp-php
    volumes:
      - ./html:/var/www/html
    networks:
      - lnmp-net

  mysql:
    image: mysql:8.0
    container_name: lnmp-mysql
    environment:
      MYSQL_ROOT_PASSWORD: "Root@123456"
      MYSQL_DATABASE: "wordpress"
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - lnmp-net

  redis:
    image: redis:7-alpine
    container_name: lnmp-redis
    volumes:
      - redis-data:/data
    networks:
      - lnmp-net

networks:
  lnmp-net:
    driver: bridge

volumes:
  mysql-data:
  redis-data:
```

```bash
# 启动
docker compose up -d

# 查看状态
docker compose ps

# 查看日志
docker compose logs -f

# 停止并删除容器
docker compose down

# 停止并删除容器 + 删除卷（慎用！）
docker compose down -v
```

### 第四阶段：Docker 网络（1 周）

#### 四种网络模式

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| bridge（默认） | 容器连接到 docker0 网桥 | 单机容器通信 |
| host | 容器共享宿主机网络栈 | 性能敏感场景（不用 NAT） |
| none | 容器没有网络接口 | 安全敏感场景 |
| overlay | 跨主机容器通信 | Swarm/K8s 集群 |

```bash
# 创建自定义网络（推荐，容器间用服务名通信）
docker network create my-net
docker run -d --name app1 --network my-net my-app
docker run -d --name app2 --network my-net my-app
# 现在 app1 可以直接 ping app2（Docker 内置 DNS）

# 查看网络详情
docker network inspect my-net
```

### 第五阶段：私有镜像仓库（3-5 天）

#### 搭建 Harbor（企业级）

```bash
# 1. 下载 Harbor 安装包
wget https://github.com/goharbor/harbor/releases/download/v2.9.0/harbor-offline-installer-v2.9.0.tgz
tar -xf harbor-offline-installer-v2.9.0.tgz
cd harbor

# 2. 修改配置文件
cp harbor.yml.tmpl harbor.yml
# 编辑 harbor.yml：配置 hostname、https 证书、admin 密码

# 3. 安装
./install.sh

# 4. 访问
# https://your-harbor-domain.com
# 默认账号：admin / 密码：见 harbor.yml 配置

# 5. 推送镜像到 Harbor
docker login your-harbor-domain.com
docker tag my-app:1.0 your-harbor-domain.com/library/my-app:1.0
docker push your-harbor-domain.com/library/my-app:1.0
```

---

## 💻 实战命令示例

### 排查容器故障常用命令

```bash
# 1. 容器起不来，查看原因
docker logs <container-name>
docker inspect <container-name>      # 查看容器详细配置

# 2. 容器网络不通
docker exec -it <container-name> ping 8.8.8.8
docker exec -it <container-name> nslookup google.com
docker network inspect <network-name>

# 3. 容器磁盘占满
docker exec -it <container-name> df -h
# 找到大文件后清理，或者扩展 volume

# 4. 查看容器资源占用
docker stats <container-name>
docker top <container-name>              # 查看容器内运行的进程

# 5. 拷贝文件（容器 ↔ 宿主机）
docker cp <container-name>:/var/log/app.log ./
docker cp ./config.conf <container-name>:/etc/app/
```

### 清理 Docker 资源（运维常用）

```bash
# 清理停止的容器
docker container prune -f

# 清理未被使用的镜像
docker image prune -a -f

# 清理未被使用的 volume（⚠️ 会删除数据！）
docker volume prune -f

# 一键清理所有（⚠️ 慎用！）
docker system prune -a --volumes -f
```

---

## 🧪 实战项目

### 项目 1：用 Docker Compose 部署 WordPress

**目标**：不用手动装 LNMP，一条命令起来。

**步骤**：
1. 创建 `docker-compose.yml`（参考上面的 LNMP 示例，加上 WordPress）
2. `docker compose up -d`
3. 浏览器访问 `http://服务器IP`，完成 WordPress 初始化
4. 验证 MySQL 数据持久化（删除容器，数据还在）

### 项目 2：编写多阶段构建的 Dockerfile

**目标**：把一个 Node.js 应用打包成最小镜像。

**要求**：
1. 用多阶段构建（构建阶段用 `node:18`，运行阶段用 `nginx:alpine`）
2. 最终镜像不超过 50MB
3. 用非 root 用户运行
4. 加上健康检查
5. 推送到阿里云镜像仓库

---

## 🔧 常见故障排查

### 故障 1：容器无法访问外网

**排查步骤**：
```bash
# 1. 检查宿主机网络
ping -c 3 8.8.8.8

# 2. 检查 Docker DNS 配置
cat /etc/docker/daemon.json
# 如果没有配置 DNS，加上：
# "dns": ["8.8.8.8", "114.114.114.114"]

# 3. 重启 Docker
systemctl restart docker
```

### 故障 2：端口被占用，容器起不来

```bash
# 查看端口占用
netstat -tlnp | grep :8080
# 或者
lsof -i :8080

# 杀掉占用进程，或者改容器的映射端口
docker run -d -p 8081:80 nginx   # 改用 8081
```

### 故障 3：镜像拉取很慢

**解决**：配置镜像加速器（见上面安装 Docker 时的 `daemon.json` 配置）

---

## 💼 面试高频题

1. **Docker 和虚拟机的区别？**
   - 虚拟机：硬件虚拟化，每个 VM 有独立 OS，重但隔离性好
   - 容器：OS 级虚拟化，共享宿主机内核，轻量但隔离性弱

2. **Dockerfile 中 COPY 和 ADD 的区别？**
   - `COPY`：单纯复制文件
   - `ADD`：复制文件 + 自动解压压缩包 + 支持 URL（不推荐用，行为不透明）

3. **为什么推荐用非 root 用户运行容器？**
   - 容器被突破后，攻击者获得的是容器内用户的权限，不是宿主机 root

4. **Docker 网络模式中 bridge 和 host 的区别？**
   - `bridge`：容器有独立 IP，通过 NAT 访问外网，安全性好
   - `host`：容器共享宿主机网络，性能更好但失去网络隔离

---

## 📈 进阶学习路径

- **Docker 安全**：学镜像扫描（Trivy）、签名（Docker Content Trust）
- **容器编排**：学 Kubernetes（Docker 的单机能力有限，K8s 才是终点）
- **容器运行时**：了解 containerd、CRI-O（K8s 1.24+ 不再用 Docker 作为运行时）
- **Service Mesh**：学 Istio（容器网络的高级玩法）

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 03 Shell 脚本](../03_Shell_Scripting/)
- [CN 05 Kubernetes](../05_Kubernetes/)
- [实时发现：Docker 相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · 容器化是第一步，K8s 才是目的地</sub>
</p>
