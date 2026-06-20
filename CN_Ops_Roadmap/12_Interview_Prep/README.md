# 12 · 运维面试题汇总

> 面试是检验学习成果的最好方式。这个模块汇总了运维工程师高频面试题，附详细解答思路。
> 适用于：应届生面试、社招面试、晋升答辩、CKA/CKAD 认证考试。

---

## 📝 使用建议

- **不要死记硬背**：理解原理，能用自己的话解释
- **结合实战**：每个知识点都有对应的实验验证
- **持续更新**：面试回来补充被问到的新题
- **模拟面试**：找同事/朋友模拟，练习表达

---

## 🎯 按模块分类

### 一、Linux 基础（必问）

#### 1. 说说 Linux 启动流程（从按下电源到登录提示符）

**答案要点**：
```
1. BIOS/UEFI → 2. Bootloader (GRUB) → 3. Kernel 加载 → 4. initramfs (临时根文件系统)
5. 挂载真实根文件系统 → 6. systemd/init 启动 → 7. 启动各服务 → 8. 登录界面
```

**常见追问**：
- GRUB 的作用是什么？（引导加载程序，负责加载内核）
- initramfs 是什么？（临时根文件系统，包含驱动，用于挂载真实根文件系统）
- systemd 和 SysVinit 的区别？（systemd 并行启动，更快；SysVinit 串行）

#### 2. 如何排查 CPU 使用率高的进程？

**命令**：
```bash
top                          # 实时查看（按 P 按 CPU 排序）
htop                        # 更友好的界面
pidstat -u 1 5              # 查看每个 CPU 的使用率
perf top                    # 定位热点函数（性能分析神器）
```

**进阶**：如果 `kworker` 进程 CPU 高，可能是：
- 磁盘 I/O 高（用 `iotop` 确认）
- 网络设备中断（检查 `/proc/interrupts`）

#### 3. 如何排查内存占用高的进程？

**命令**：
```bash
free -h                      # 查看总内存使用
top                          # 按 M 按内存排序
ps aux --sort=-%mem | head   # 按内存排序
pmap -x <PID>               # 查看进程内存映射
```

**常见追问**：
- `buff/cache` 高正常吗？（正常，Linux 会利用空闲内存做缓存，可用 `echo 3 > /proc/sys/vm/drop_caches` 清理）
- OOM Killer 是什么？（内存不足时，内核杀掉内存占用最高的进程）

#### 4. 说说 `soft lockup` 和 `hard lockup` 的区别？

- **soft lockup**：内核代码长时间不调度（通常 >20s），但中断还能响应。原因：死循环、长时间禁用抢占。
- **hard lockup**：中断都不响应（通常 >10s）。原因：中断处理程序中死锁、硬件故障。

**排查**：查看 `/var/log/messages` 里的 `BUG: soft lockup` 日志。

---

### 二、网络（必问）

#### 5. 从浏览器输入 URL 到页面显示，中间发生了什么？

**标准答案**（逐层展开）：
```
1. DNS 解析（浏览器缓存 → 系统缓存 → 本地 DNS → 根 DNS → 顶级域 DNS → 权威 DNS）
2. 建立 TCP 连接（三次握手）
3. 发送 HTTP 请求
4. 服务器处理请求并返回 HTTP 响应
5. 浏览器解析响应并渲染页面
6. 关闭 TCP 连接（四次挥手）
```

**加分回答**：
- HTTPS 还要 TLS 握手（额外 2-3 个 RTT）
- HTTP/2 多路复用，HTTP/3 基于 UDP（QUIC）

#### 6. TCP 三次握手和四次挥手详细过程？

**三次握手**：
```
Client → SYN=1, seq=x          → Server  (SYN_SENT)
Client ← SYN=1, ACK=1, seq=y, ack=x+1 ← Server  (ESTABLISHED)
Client → ACK=1, seq=x+1, ack=y+1 → Server  (ESTABLISHED)
```

**为什么不是两次？**（防止旧连接请求延迟到达，服务器误建立连接）

**四次挥手**：
```
Client → FIN=1, seq=u → Server  (FIN_WAIT_1)
Client ← ACK=1, ack=u+1         ← Server  (CLOSE_WAIT)
(服务器继续发送剩余数据...)
Client ← FIN=1, seq=w, ack=u+1 ← Server  (LAST_ACK)
Client → ACK=1, ack=w+1         → Server  (TIME_WAIT)
```

**为什么是四次？**（因为服务器收到 FIN 后，可能还有数据要发送，所以先 ACK，等数据发完再 FIN）

#### 7. HTTP 和 HTTPS 的区别？TLS 握手过程？

**区别**：
- HTTP：明文传输，端口 80
- HTTPS：加密传输（TLS/SSL），端口 443，需要证书

**TLS 1.2 握手**：
```
1. Client Hello（支持的加密套件、随机数 C）
2. Server Hello（选定的加密套件、随机数 S、证书）
3. Client 验证证书 → 用服务器公钥加密「预主密钥」发送
4. 双方用 C + S + 预主密钥 → 生成会话密钥
5. 后续通信用会话密钥对称加密
```

#### 8. 如何排查网络不通的问题？

**排查流程**（分层排查）：
```bash
# 1. 物理层：网线/网卡灯亮吗？
ip link show                   # 查看网卡状态

# 2. 网络层：IP 配置正确吗？
ip addr show                  # 查看 IP 地址
ip route show                 # 查看路由表

# 3. 连通性：能 ping 通网关吗？
ping 192.168.1.1             # ping 网关
ping 8.8.8.8                  # ping 外网 IP

# 4. DNS：能解析域名吗？
nslookup google.com           # 测试 DNS
cat /etc/resolv.conf         # 查看 DNS 配置

# 5. 端口：服务端口在监听吗？
ss -tlnp | grep :80           # 查看端口监听

# 6. 防火墙：被 iptables 拦截了吗？
sudo iptables -L -n           # 查看规则
```

---

### 三、Shell 脚本（常问）

#### 9. 如何批量重命名文件（把 `.txt` 改成 `.md`）？

```bash
# 方法 1：for 循环
for f in *.txt; do
    mv "$f" "${f%.txt}.md"
done

# 方法 2：rename 命令
rename 's/\.txt$/.md/' *.txt

# 方法 3：find + xargs
find . -name "*.txt" | while read f; do
    mv "$f" "${f%.txt}.md"
done
```

#### 10. 如何找出大文件（>100MB）并删除？

```bash
# 找出大文件
find / -type f -size +100M 2>/dev/null

# 找出大文件并删除（谨慎！）
find /var/log -type f -size +100M -mtime +30 -delete
```

#### 11. 如何监控某个进程的内存和 CPU 使用率，超过阈值就重启？

```bash
#!/bin/bash
PID=$1
CPU_THRESHOLD=80
MEM_THRESHOLD=80

while true; do
    CPU=$(ps -p $PID -o %cpu | tail -1 | awk '{print $1}')
    MEM=$(ps -p $PID -o %mem | tail -1 | awk '{print $1}')
    
    if (( $(echo "$CPU > $CPU_THRESHOLD" | bc -l) )) || \
       (( $(echo "$MEM > $MEM_THRESHOLD" | bc -l) )); then
        echo "$(date): High resource usage detected, restarting..."
        systemctl restart myapp
        sleep 60   # 等 60 秒再检查
    fi
    sleep 30
done
```

---

### 四、Docker & Kubernetes（高频）

#### 12. 说说 Docker 的网络模式？

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| `bridge` | 默认，容器通过虚拟网桥通信 | 单主机容器通信 |
| `host` | 容器共享宿主机网络栈 | 性能敏感应用 |
| `none` | 无网络 | 离线处理 |
| `overlay` | 跨主机容器通信 | Docker Swarm / K8s |
| `macvlan` | 容器有独立 MAC 地址 | 遗留应用 |

#### 13. K8s 中 Pod 的 `requests` 和 `limits` 有什么区别？

- **requests**：调度依据（调度器保证节点有足够资源）
- **limits**：硬上限（容器内存超过 limits 会被 OOM Kill）

**示例**：
```yaml
resources:
  requests:
    memory: "64Mi"   # 调度时保证有 64MB 可用
    cpu: "250m"      # 调度时保证有 0.25 核可用
  limits:
    memory: "128Mi"  # 内存超过 128MB 会被 OOM Kill
    cpu: "500m"       # CPU 最多用 0.5 核
```

#### 14. K8s 中 Service 的 `ClusterIP` / `NodePort` / `LoadBalancer` 区别？

| 类型 | 访问范围 | 适用场景 |
|------|---------|---------|
| `ClusterIP` | 集群内 | 内部服务通信（默认） |
| `NodePort` | 集群外（通过 `<NodeIP>:<NodePort>`） | 测试/临时暴露 |
| `LoadBalancer` | 公网（云厂商负载均衡器） | 生产环境对外服务 |
| `ExternalName` | DNS CNAME 映射 | 访问外部服务 |

#### 15. 如何排查 K8s 中 Pod 网络不通？

**排查流程**：
```bash
# 1. 检查 Pod 是否 Running
kubectl get pods -n <namespace>

# 2. 检查 Pod 日志
kubectl logs <pod-name> -n <namespace>

# 3. 检查 Service 的 Endpoints（最关键！）
kubectl get endpoints <service-name> -n <namespace>
# 如果 Endpoints 为空 → Service selector 和 Pod labels 不匹配

# 4. 在 Pod 里测试 DNS
kubectl exec -it <pod-name> -- nslookup kubernetes.default.svc.cluster.local

# 5. 检查 NetworkPolicy
kubectl get networkpolicy -n <namespace>

# 6. 检查 CNI 插件状态
kubectl get pods -n kube-system | grep -E "calico|flannel|weave|cilium"
```

---

### 五、CI/CD & 监控（进阶）

#### 16. 说说 Blue-Green 部署和 Canary 部署的区别？

- **Blue-Green**：两套环境（蓝 + 绿），流量切换瞬间完成（零停机）
  - 优点：回滚快
  - 缺点：需要双倍资源
  
- **Canary**：新版本先给小部分用户（比如 5%），逐步扩大
  - 优点：风险可控
  - 缺点：需要流量分割能力（Istio / Nginx）

#### 17. Prometheus 的 PromQL 常用查询？

```promql
# CPU 使用率（所有容器）
sum(rate(container_cpu_usage_seconds_total{image!=""}[5m])) by (pod)

# 内存使用量（所有容器）
sum(container_memory_usage_bytes{image!=""}) by (pod)

# 磁盘 I/O（读取速率）
rate(container_fs_reads_bytes_total[5m])

# 网络接收速率
rate(container_network_receive_bytes_total[5m])

# 健康检查（up 状态）
up

# 预测磁盘 24 小时后满（prometheus 2.2+）
predict_linear(disk_free_bytes[1h], 24 * 3600)
```

---

### 六、场景题（开放思维）

#### 18. 生产环境服务器突然变慢，如何排查？

**标准排查流程**（从上到下）：
```
1. 确认现象（是所有人慢，还是部分人慢？）
2. 查看监控（Grafana → 找异常指标）
3. 检查服务器资源（top / free / df -h）
4. 检查网络（ping / traceroute / ss -tlnp）
5. 检查日志（/var/log/messages / 应用日志）
6. 检查最近变更（部署？配置修改？）
7. 回滚最近变更（如果确认是变更引起的）
```

**常见原因**：
- 流量突增（用 `ss -tln` 查看连接数）
- 数据库慢查询（检查慢查询日志）
- 磁盘满了（用 `df -h` 检查）
- 内存泄漏（用 `ps aux --sort=-%mem` 找异常进程）

#### 19. 如何设计一个高可用架构？

**要点**（分层设计）：
```
1. DNS 层：智能 DNS（根据地理位置返回最近IP）
2. 接入层：负载均衡（Nginx / HAProxy / 云负载均衡）
3. 应用层：无状态应用（多实例 + 负载均衡）
4. 缓存层：Redis 集群（主从 + 哨兵）
5. 数据库层：主从复制 + 读写分离
6. 存储层：分布式存储（Ceph / 云盘）
7. 监控层：Prometheus + Grafana + Alertmanager
8. 备份层：定期备份 + 异地容灾
```

#### 20. 如果有 1000 台服务器需要管理，你会怎么做？

**答案要点**：
```
1. 自动化运维工具（Ansible / SaltStack / Puppet）
2. 配置管理（所有配置版本化，用 Git 管理）
3. 监控告警（Prometheus + Grafana，覆盖所有指标）
4. 日志集中（ELK / Loki，所有日志统一查询）
5. CI/CD（所有变更通过流水线，禁止手动登录服务器）
6. 堡垒机（所有服务器访问通过堡垒机，有审计）
7. 标准化（OS、软件版本、目录结构统一）
```

---

## 📚 推荐刷题资源

| 资源 | 链接 | 特点 |
|------|------|------|
| 腾讯云运维工程师认证 | https://cloud.tencent.com/edu/cert | 国内云厂商认证 |
| CKA 真题 | https://github.com/stefanprodan/Kubernetes-CKA | ⭐14k，必刷 |
| DevOps 面试题 | https://github.com/bregman-arie/devops-interview-questions | ⭐8k，英文 |
| Linux 面试题 | https://github.com/linuxiac/linux-interview-questions | 中文整理 |
| 我自己的面经 | 见下节 | 真实面试记录 |

---

## ✅ 模拟面试自测

找一个朋友，让他随机问你这些问题（计时回答）：

- [ ] 说说 Linux 启动流程
- [ ] 如何排查 CPU 使用率高的问题？
- [ ] 从浏览器输入 URL 到页面显示，中间发生了什么？
- [ ] TCP 为什么要三次握手？
- [ ] Docker 的 `COPY` 和 `ADD` 指令有什么区别？
- [ ] K8s 中 Pod 的 `requests` 和 `limits` 有什么区别？
- [ ] 如何排查 K8s 中 Pod 网络不通的问题？
- [ ] 说说 Blue-Green 部署和 Canary 部署的区别？
- [ ] 生产环境服务器突然变慢，如何排查？
- [ ] 如果有 1000 台服务器需要管理，你会怎么做？

**评分标准**：
- 能说清楚原理 → ⭐⭐⭐（通过）
- 能结合实战经验 → ⭐⭐⭐⭐（优秀）
- 能画图辅助解释 → ⭐⭐⭐⭐⭐（满分）

---

> 面试题只是检验工具，真正的能力是在实际工作中积累的。
> 把每个知识点都实操一遍，比背 100 道面试题更有用。
> 祝面试顺利！🎉
