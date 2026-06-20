# 12 · 面试突击

> 面试是门手艺，既要懂技术，也要懂表达。
> 这个模块整理了我面试别人和被人面试的经验，都是真实场景。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 流畅回答 Linux 基础面试题（20 道高频）
- [ ] 流畅回答 Docker/K8s 面试题（20 道高频）
- [ ] 做现场故障排查题（Troubleshooting）
- [ ] 回答系统设计题（设计高可用架构）
- [ ] 讲清楚自己的项目经验（STAR 法则）
- [ ] 反问面试官有水平的问题
- [ ] 谈薪资（了解市场行情）

**学完这个模块，面试成功率提升 50%。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| Linux 面试高频题 | 黑马程序员 | [B站](https://www.bilibili.com/video/BV1W54y1k7o) | 30万+ | ⭐⭐⭐⭐⭐ |
| Docker/K8s 面试题 | 马哥 | [B站](https://space.bilibili.com/387633139) | 20万+ | ⭐⭐⭐⭐ |
| 运维面试实战 | IT 老齐 | [B站](https://space.bilibili.com/383016053) | 10万+ | ⭐⭐⭐⭐ |
| 系统设计面试题 | 尚硅谷 | [B站](https://www.bilibili.com/video/BV1xK4y1P7ZF) | 50万+ | ⭐⭐⭐⭐⭐ |

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《DevOps 面试宝典》 | 电子工业出版社 | 面试 | 国内少有的 DevOps 面试专项书 |
| 《SRE with Java》 | Vinoth Rathinam | 高级 | 有面试场景题和答案 |
| 《System Design Interview (Vol 1 & 2)》 | Alex Xu | 高级 | 系统设计面试圣经，有中文版 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| bregman-arie/devops-exercises | https://github.com/bregman-arie/devops-exercises | ⭐82k，2600+ 面试题 |
| bregman-arie/awesome-sre | https://github.com/bregman-arie/awesome-sre | SRE 面试资源 |
| 牛客网 — 运维面试题 | https://www.nowcoder.com/ | 国内面试经验分享 |
| 拉勾 — 运维岗位 JD | https://www.lagou.com/ | 了解市场需求 |

---

## 📝 核心知识点清单

### 第一部分：Linux 高频面试题（20 道）

#### 基础命令篇

**Q1：如何查看某个进程占用的端口？**
```bash
# 方法 1：lsof
lsof -i :80          # 查看 80 端口被谁占用
lsof -p 1234          # 查看 PID 1234 打开的所有端口

# 方法 2：netstat
netstat -tlnp | grep :80

# 方法 3：ss（推荐，比 netstat 快）
ss -tlnp | grep :80
```

**Q2：`$*` 和 `$@` 的区别？（Shell 脚本必问）**
```bash
# 区别在双引号里才体现
set -- a b "c d"   # 设置 3 个参数

for i in "$*"; do echo "[$i]"; done
# 输出（只有 1 次循环）：
# [a b c d]

for i in "$@"; do echo "[$i]"; done
# 输出（3 次循环，每个参数独立）：
# [a]
# [b]
# [c d]
```

**Q3：如何排查 CPU 使用率高的进程？**
```bash
# 1. 用 top 找出 CPU 最高的进程
top -c             # -c 显示完整命令
# 按 P 按 CPU 排序，按 M 按内存排序

# 2. 查看该进程的线程（可能某个线程死循环）
top -Hp <PID>     # 查看进程内的线程

# 3. 用 perf 分析（高级）
perf top -p <PID>

# 4. 用 jstack（如果是 Java 进程）
jstack <PID> > thread_dump.txt
```

**Q4：`soft limit` 和 `hard limit` 的区别？**
```bash
# soft limit：用户可以自己改，但不能超过 hard limit
# hard limit：只有 root 能改

ulimit -S -n   # 查看 soft limit（默认 1024）
ulimit -H -n   # 查看 hard limit（默认 4096）

# 修改（临时）
ulimit -S -n 65535

# 修改（永久，写入 /etc/security/limits.conf）
* soft nofile 65535
* hard nofile 131072
```

#### 网络篇

**Q5：TCP 三次握手和四次挥手？**
```
三次握手（建立连接）：
  客户端 → SYN=1, seq=x         → 服务端
  客户端 ← SYN=1, ACK=1, seq=y, ack=x+1 ← 服务端
  客户端 → ACK=1, seq=x+1, ack=y+1 → 服务端

四次挥手（断开连接）：
  客户端 → FIN=1, seq=u         → 服务端
  客户端 ← ACK=1, ack=u+1       ← 服务端（此时服务端还能发数据）
  客户端 ← FIN=1, ACK=1, seq=w ← 服务端
  客户端 → ACK=1, ack=w+1       → 服务端
```

**Q6：`TIME_WAIT` 状态大量存在怎么办？**
```bash
# 查看 TIME_WAIT 数量
netstat -ant | grep TIME_WAIT | wc -l

# 原因：主动关闭连接的一方会进入 TIME_WAIT（默认 60 秒）
# 解决：
# 1. 让客户端主动关闭（服务端不主动 close）
# 2. 调整内核参数
cat >> /etc/sysctl.conf << EOF
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1  # 4.1+ 内核已移除这个参数
net.ipv4.tcp_fin_timeout = 30
EOF
sysctl -p
```

#### 进阶篇

**Q7：Ext4 和 XFS 文件系统选哪个？**
- **Ext4**：成熟稳定，适合 `/boot`、小文件系统
- **XFS**：性能好，适合大文件系统（> 10TB）、高并发写入
- **生产推荐**：`/boot` 用 Ext4，数据盘用 XFS

**Q8：如何在线扩容分区（不重启、不丢数据）？**
```bash
# 1. 扩容物理盘（云厂商控制台操作）
# 2. 让内核重新读取分区表
partprobe /dev/sda

# 3. 删除并重建分区（危险！但数据不丢，因为重建分区时指定相同的起始扇区）
fdisk /dev/sda
# d 删除分区
# n 新建分区（起始扇区要和原来一样！）
# w 保存

# 4. 扩容文件系统
resize2fs /dev/sda1         # Ext 系列
xfs_growfs /mount/point     # XFS
```

---

### 第二部分：Docker/K8s 高频面试题（20 道）

**Q9：K8s 的 Service 和 Ingress 有什么区别？**
- **Service**：L4（TCP/UDP）负载均衡，集群内访问
- **Ingress**：L7（HTTP/HTTPS）路由，支持域名和路径匹配，对外暴露

**Q10：Deployment 的滚动更新过程是怎样的？**
1. 创建新 ReplicaSet
2. 逐步扩容新版本 Pod（按 `maxSurge` 配置）
3. 逐步缩容旧版本 Pod（按 `maxUnavailable` 配置）
4. 所有旧 Pod 删除后，滚动更新完成

**Q11：PV 和 PVC 的关系？**
- **PV**（PersistentVolume）：集群级别的存储资源（管理员创建）
- **PVC**（PersistentVolumeClaim）：用户对存储的请求（用户创建）
- 绑定后，Pod 通过 PVC 使用存储
- **生命周期**：PVC 删除 → PV 根据 `reclaimPolicy` 决定是保留（Retain）、删除（Delete）还是清除数据（Recycle，已废弃）

**Q12：livenessProbe 和 readinessProbe 的区别？**
- **livenessProbe**：容器是否"活着"，失败会重启 Pod
- **readinessProbe**：容器是否"准备好接收流量"，失败会从 Service Endpoints 移除

---

### 第三部分：故障排查场景题

#### 场景 1：服务器负载很高，但 CPU 使用率不高

**排查思路**：
```bash
# 1. 查看负载组成（load average）
uptime
# 负载高但 CPU 不高 → 通常是 IO 等待（iowait）或进程 D 状态（不可中断睡眠）

# 2. 查看 IO 等待
top
# 看 %wa 列（iowait）

# 3. 找出 IO 高的进程
iotop

# 4. 找出哪个文件在狂写
lsof -p <PID> | grep REG
# 或者用 iostat 看哪个磁盘忙
iostat -x 1
```

**常见原因**：
- 数据库没索引，全表扫描 → 加索引
- 日志写入太频繁，没轮转 → 配置 `logrotate`
- 内存不够，开始用 swap → 加内存或优化应用

#### 场景 2：K8s Pod 一直 CrashLoopBackOff

**排查步骤**：
```bash
# 1. 查看 Pod 状态
kubectl get pods
kubectl describe pod <pod-name>   # 看 Events

# 2. 查看容器日志（当前实例的日志）
kubectl logs <pod-name>

# 3. 查看上一个实例的日志（如果一直重启）
kubectl logs <pod-name> --previous

# 4. 常见原因：
# - 镜像里没有指定正确的 CMD/ENTRYPOINT
# - 配置文件挂载失败（ConfigMap/Secret 不存在）
# - 健康检查配置太严格（livenessProbe 初始延迟太短）
# - 资源不足（没到调度器，或者 OOMKilled）
```

---

### 第四部分：系统设计题

#### 题目：设计一个 1000 万用户的短视频平台架构

**回答框架**（STAR 法则的变体）：

```
1. 需求分析（先问清楚再答）
   - 日活多少？读多写多还是读多写少？
   - 视频文件存哪里？CDN 要不要？
   - 是否需要推荐算法？

2. 整体架构（从上往下画）
   ┌──────────────────────────────────┐
   │         用户（APP/Web）                │
   └──────────────┬───────────────────┘
                      ↓
   ┌──────────────────────────────────┐
   │     CDN（静态资源加速）          │
   └──────────────┬───────────────────┘
                      ↓
   ┌──────────────────────────────────┐
   │     API Gateway（Nginx/Kong）    │
   │     - 认证、限流、路由            │
   └──────────────┬───────────────────┘
                      ↓
   ┌──────────────────────────────────┐
   │     服务层（微服务）              │
   │     - 用户服务（User Svc）      │
   │     - 视频服务（Video Svc）     │
   │     - 评论服务（Comment Svc）   │
   └──────────────┬───────────────────┘
                      ↓
   ┌──────────────────────────────────┐
   │     存储层                      │
   │     - MySQL（元数据）           │
   │     - Redis（缓存）            │
   │     - OSS（视频文件）          │
   │     - ES（搜索）               │
   └──────────────────────────────────┘

3. 数据库设计（重点！）
   - 用户表：id, username, password_hash, ...
   - 视频表：id, user_id, video_url, title, ...
   - 分表策略：按 user_id 哈希分 16 张表

4. 高可用设计
   - 多可用区部署（云厂商）
   - 数据库主从 + 读写分离
   - Redis 主从 + Sentinel
   - 服务无状态化（K8s Deployment）

5. 性能优化
   - CDN 加速视频播放
   - Redis 缓存热点数据
   - 数据库加索引
   - 用消息队列（Kafka）异步处理耗时任務
```

---

### 第五部分：反问面试官（加分项）

**好问题**（显示你有思考）：
1. "团队现在最大的技术挑战是什么？"
2. "运维和开发的协作模式是怎样的？"
3. "这个岗位的 On-call 机制是怎样的？"
4. "团队的技术栈是偏保守还是愿意尝试新技术？"

**避免的问题**：
- ❌ "加班多吗？"（可以问，但换成"团队的工作节奏怎样？"）
- ❌ "薪资多少？"（等对方先提）
- ❌ "有加班费吗？"（太急着谈钱）

---

## 💻 实战模拟

### 模拟面试 1：Linux 基础岗（3 年经验，目标 15-20K）

**面试官**："说说你们现在怎么管理服务器？"
**回答模板**（STAR）：
```
我们目前管 200+ 台服务器（Situation）
我主导把原来的手动运维改成了自动化（Task）
具体做法是：写 Shell 脚本 + Ansible Playbook，
把软件安装、配置同步、日志清理都自动化了（Action）
效果是：部署一台新服务器从 2 小时降到 10 分钟，
而且不会有人为失误（Result）
```

### 模拟面试 2：K8s 高级岗（5 年经验，目标 30-40K）

**面试官**："说说你们 K8s 集群的高可用方案"
**回答要点**：
1. 多 Master 节点（3 或 5 个，etcd 也部署在里面）
2. 工作节点分布在多个可用区
3. Ingress 控制器多副本 + 云厂商 SLB 做负载均衡
4. 用 Prometheus + Grafana 监控集群状态
5. 定期做 etcd 备份（我们每天自动备份到 OSS）

---

## 💼 薪资谈判

### 市场行情参考（2024 年，国内）

| 经验年限 | Linux 基础岗 | 运维开发 | K8s/DevOps | SRE |
|-----------|--------------|----------|---------------|-----|
| 1-3 年 | 10-18K | 15-25K | 18-30K | 25-35K |
| 3-5 年 | 15-25K | 20-35K | 25-40K | 35-50K |
| 5-10 年 | 20-35K | 30-50K | 35-60K | 50K+ |

### 谈薪资技巧

1. **先让对方出价**（别先报期望薪资）
2. **用数据说话**："我上一份工作是 25K，主导了 K8s 迁移项目，节省服务器成本 30%"
3. **不仅要 base**：期权、年终奖、加班费、培训预算都要问
4. **表达意愿但要底线**："这个岗位我很感兴趣，但低于 30K 我可能要考虑一下"

---

## 📈 进阶学习路径

- **高级岗**：学架构设计、容量规划、多集群治理
- **管理岗**：学团队管理、项目排期、跨部门协作
- **专家岗**：学内核调优、分布式系统、大规模集群治理

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 01 Linux 基础](../01_Linux_Basics/)
- [CN 05 Kubernetes](../05_Kubernetes/)
- [CN 08 监控告警](../08_Monitoring/)
- [实时发现：面试相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · 面试是门手艺，既要懂技术，也要懂表达</sub>
</p>
