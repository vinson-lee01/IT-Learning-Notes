# 02 · 计算机网络

> **不懂网络的运维，排起障来就是抓瞎。**
>
> 我刚入行那会儿，遇到过一个问题：用户反馈访问网站慢，我查了 CPU、内存、磁盘，都没问题，最后才发现是 DNS 解析慢导致的。从那以后我就明白：TCP/IP、DNS、HTTP、负载均衡——这是运维的基本功，不把这关过了，后面学再多容器、K8s 都是空中楼阁。
>
> 这个模块我会从实战角度出发，少讲理论，多给你看抓包、多给你看生产环境的配置。学完这个模块，你能独立排查 80% 的网络问题，能独立配置四层和七层负载均衡。
>
> 本模块定位 **网络基础 → 生产级网络故障排查**，适合有一定 Linux 基础的同学。

---

## 🎯 学习目标

学完这个模块，你应该能够：

- [ ] 理解 TCP/IP 协议栈各层的职责，能画出数据包在网络中的封装与解封装过程
- [ ] 掌握 TCP 三次握手和四次挥手，能说清楚为什么是三次而不是两次
- [ ] 理解 TCP 可靠传输机制（滑动窗口、拥塞控制、重传机制）
- [ ] 熟练掌握子网划分（CIDR），能给一个企业设计合理的 IP 地址规划方案
- [ ] 独立配置 DNS 服务（Bind）或排查 DNS 解析问题
- [ ] 理解 HTTP/1.1、HTTP/2、HTTP/3 的差异，能说清楚 HTTPS/TLS 握手过程
- [ ] 掌握四层负载均衡（L4，如 LVS、Nginx Stream）和七层负载均衡（L7，如 Nginx、HAProxy）的原理和配置
- [ ] 熟练使用网络排查命令（ping、traceroute、nslookup、tcpdump、Wireshark）
- [ ] 理解网络存储相关协议（NFS、iSCSI、Ceph RBD）的基础原理
- [ ] 掌握防火墙和 NAT 的配置（iptables、firewalld）
- [ ] 了解软件定义网络（SDN）和基础网络架构（VXLAN、Overlay）
- [ ] 能独立设计一个中型企业的网络架构（DMZ、内网、运维管理网）

---

## 📺 推荐视频教程

计算机网络这块，B 站上有不少优质的课程。我按难度排序推荐给大家。

| # | 教程标题 | UP 主 | 链接 | 播放量 | 难度 | 推荐理由 |
|---|---------|-------|------|--------|------|---------|
| 1 | 《计算机网络微课堂》 | 湖科大教书匠 | [BV1c4411d7jb](https://www.bilibili.com/video/BV1c4411d7jb) | 800万+ | ⭐ 入门 | 被称为"最好的中文计网视频"，通俗易懂，适合零基础。我推荐所有转行的同学先看这个。 |
| 2 | 《TCP/IP 协议详解》 | 韩立刚 | [BV1Kb411G7uS](https://www.bilibili.com/video/BV1Kb411G7uS) | 300万+ | ⭐⭐ 系统 | 韩老师讲课风格幽默，对 TCP/IP 协议栈讲得很细。适合有一定基础后系统学习。 |
| 3 | 《HTTP 协议详解》 | 尚硅谷 | [BV1xs411Q7Bf](https://www.bilibili.com/video/BV1xs411Q7Bf) | 150万+ | ⭐⭐ 专项 | HTTP 协议专项突破，对理解 Web 运维非常有帮助。 |
| 4 | 《Nginx 入门到实战》 | 狂神说 | [BV1F54y1k7XR](https://www.bilibili.com/video/BV1F54y1k7XR) | 200万+ | ⭐⭐ 实战 | Nginx 是运维必备技能，这个教程从安装到配置都讲得很清楚。 |
| 5 | 《Wireshark 网络分析》 | 安全牛课堂 | [BV1Yx411K7V7](https://www.bilibili.com/video/BV1Yx411K7V7) | 50万+ | ⭐⭐⭐ 进阶 | 网络故障排查利器，学会用 Wireshark 抓包分析，你就能看透网络问题的本质。 |
| 6 | 《负载均衡技术详解》 | 马哥 Linux | [BV1xT4y1j7mK](https://www.bilibili.com/video/BV1xT4y1j7mK) | 30万+ | ⭐⭐⭐ 专项 | LVS、Nginx、HAProxy 的负载均衡原理和配置，生产环境必用。 |
| 7 | 《DNS 原理与实践》 | 课堂唐工 | [BV1tK4y1a7Wx](https://www.bilibili.com/video/BV1tK4y1a7Wx) | 20万+ | ⭐⭐ 专项 | DNS 是互联网的基础，这个视频讲清楚了递归查询、迭代查询、DNS 劫持等核心概念。 |
| 8 | 《网络安全基础》 | 无线通信课堂 | [BV1x7411x7Vz](https://www.bilibili.com/video/BV1x7411x7Vz) | 100万+ | ⭐⭐⭐ 安全 | 防火墙、VPN、IPS/IDS 等网络安全技术基础，想往安全方向发展的同学必看。 |

> **我的建议**：零基础先看湖科大的计网微课堂，然后看韩立刚的 TCP/IP，工作后遇到 HTTP 或负载均衡问题再针对性地看专项视频。

---

## 📖 推荐书籍

网络这块的书籍，我推荐"经典 + 实战"的组合。

| # | 书名 | 作者 | 豆瓣评分 | 适合阶段 | 我的推荐理由 |
|---|------|------|----------|---------|-------------|
| 1 | 《TCP/IP 详解 卷1：协议》 | W. Richard Stevens | **9.2** | 进阶→深入 | 网络领域的圣经，Stevens 的书不用多说。我建议作为工具书查阅，不用一口气读完。想深入理解 TCP 状态的同学必读。 |
| 2 | 《计算机网络：自顶向下方法（第7版）》 | James F. Kurose | **9.0** | 零基础→系统 | 这本是很多大学的教材，讲解方式是从应用层往下讲，比较符合人的认知习惯。我推荐英文好的同学看英文原版。 |
| 3 | 《HTTP 权威指南》 | David Gourley | **8.6** | Web 运维 | 做 Web 运维的同学必读。虽然书有点老（2012 年），但 HTTP 基础部分依然是经典。 |
| 4 | 《图解 TCP/IP（第5版）》 | 竹下隆史 | **8.5** | 零基础入门 | 日本人的书，最大的特点是图解多，适合不喜欢看大段文字的同学。我入门时看过，通俗易懂。 |
| 5 | 《图解 HTTP》 | 上野宣 | **8.7** | 零基础入门 | 和《图解 TCP/IP》是同一个系列，HTTP 部分讲得很清楚，200 多页，很快就能读完。 |
| 6 | 《Nginx 高性能 Web 服务器详解》 | 苗泽 | **8.4** | 实战 | 国内作者写的 Nginx 实战书，有很多生产环境的配置案例，我日常配置 Nginx 经常翻。 |
| 7 | 《Web 性能权威指南》 | Ilya Grigorik | **8.8** | 性能优化 | Google 工程师写的，从 TCP、TLS、HTTP 到浏览器渲染，全面讲解 Web 性能优化。想深入 HTTP/2、HTTP/3 的同学必读。 |
| 8 | 《计算机网络实验教程》 | 王文帅 | **7.9** | 实战 | 这本书有很多网络实验，适合边学边练。我推荐配合 GNS3 或 Packet Tracer 一起用。 |

> **购书建议**：《TCP/IP 详解》和《图解 HTTP》是我书架上最常用的两本。如果预算有限，优先买这两本。

---

## 🌐 在线参考资源

这些是我日常工作中经常查阅的网站和仓库。

| # | 资源名称 | 链接 | 类型 | 说明 |
|---|---------|------|------|------|
| 1 | 小林 coding 图解网络 | [xiaolincoding.com/network](https://xiaolincoding.com/network/) | 中文教程 | 用大量图解讲解网络知识，非常直观。我经常在面试前刷一遍。 |
| 2 | MDN Web Docs - HTTP | [developer.mozilla.org/zh-CN/docs/Web/HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP) | 官方文档 | Mozilla 的 HTTP 文档，权威且易懂，比看书效率高。 |
| 3 | Cloudflare 学习中心 | [www.cloudflare.com/zh-cn/learning](https://www.cloudflare.com/zh-cn/learning/) | 厂商文档 | Cloudflare 出的网络基础教程，涵盖 DNS、HTTP、SSL/TLS 等，质量很高。 |
| 4 | TCP 的那些事儿 | [coolshell.cn/articles/11564.html](https://coolshell.cn/articles/11564.html) | 技术博客 | 陈皓（左耳朵耗子）写的 TCP 系列，深入浅出，我强烈推荐。 |
| 5 | Nginx 官方文档（中文） | [nginx.org/en/docs](https://nginx.org/en/docs/) | 官方文档 | Nginx 的官方文档非常详细，我配置 Nginx 首先查这里。 |
| 6 | Wireshark 官方文档 | [wiki.wireshark.org](https://wiki.wireshark.org/) | 官方文档 | Wireshark 的显示过滤器和抓包技巧，这里有最全的说明。 |
| 7 | 计算机网络面试题 | [github.com/CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) ⭐167k | GitHub 仓库 | 计算机科学笔记，网络部分整理得非常好，适合面试复习。 |
| 8 | HTTP 协议字段详解 | [datatracker.ietf.org/doc/html/rfc7231](https://datatracker.ietf.org/doc/html/rfc7231) | RFC 文档 | HTTP/1.1 的 RFC 文档，想深入理解 HTTP 协议的必看原版。 |
| 9 | 腾讯云网络产品文档 | [cloud.tencent.com/document/product/215](https://cloud.tencent.com/document/product/215) | 云厂商文档 | 国内云厂商的网络产品文档，理解 VPC、子网、路由表、安全组的好材料。 |
| 10 | 阿里云网络最佳实践 | [help.aliyun.com/document_detail/27721.html](https://help.aliyun.com/document_detail/27721.html) | 云厂商文档 | 阿里云的网络架构最佳实践，很多设计思路可以直接借鉴。 |

> **我的使用习惯**：学新概念看小林 coding 的图解；查 HTTP 头字段看 MDN；配置 Nginx 看官方文档；面试复习刷 CS-Notes。

---

## 📝 核心知识点清单

这部分是网络模块的核心，我把它分成 5 个阶段，每个阶段 10-12 个知识点。

### 第一阶段：网络基础与 OSI 模型（1-2周）

1. **OSI 七层模型 vs TCP/IP 四层模型** —— 理解每一层的职责，知道数据在各层叫什么名字（PDU：物理层=比特，数据链路层=帧，网络层=包，传输层=段，应用层=报文）
2. **网络拓扑结构** —— 星型、环型、总线型、树型、网状型，以及现代数据中心常用的叶脊（Leaf-Spine）架构
3. **IP 地址基础** —— IPv4 地址结构（32位，点分十进制）、IP 地址分类（A/B/C/D/E 类）、私有地址和公有地址
4. **子网掩码与 CIDR** —— 子网掩码的作用、CIDR 表示法（如 192.168.1.0/24）、如何计算网络地址和广播地址
5. **子网划分实战** —— 给定一个大网段，划分成多个小网段（这是企业 IP 地址规划的必备技能）
6. **ARP 协议** —— 地址解析协议，IP 地址到 MAC 地址的映射，ARP 缓存、ARP 欺骗（安全问题）
7. **RARP 和 Gratuitous ARP** —— 反向地址解析、免费 ARP（用于检测 IP 冲突）
8. **ICMP 协议** —— Internet 控制消息协议，ping 和 traceroute 背后的原理
9. **MAC 地址** —— 48 位硬件地址，OUI（组织唯一标识符），MAC 地址表（交换机学习）
10. **以太网帧结构** —— 前导码、目的 MAC、源 MAC、类型/长度、数据、FCS（帧校验序列）
11. **网络传输介质** —— 双绞线（Cat5e/Cat6/Cat6a）、光纤（单模/多模）、同轴电缆
12. **网络设备基础** —— 集线器（Hub）、交换机（Switch）、路由器（Router）的区别和工作原理

### 第二阶段：TCP/IP 协议栈深入（2-3周）

1. **IP 协议** —— IP 头部结构（版本、TTL、协议号、源/目的 IP）、IP 分片与重组、TTL 的作用
2. **TCP 协议基础** —— TCP 头部结构（源/目的端口、序列号、确认号、窗口大小、标志位）、TCP 可靠传输的基础
3. **TCP 三次握手** —— 详细过程（SYN → SYN-ACK → ACK）、为什么是三次而不是两次或四次、SYN Flood 攻击
4. **TCP 四次挥手** —— 详细过程（FIN → ACK → FIN → ACK）、TIME_WAIT 状态的作用和优化
5. **TCP 滑动窗口** —— 发送窗口、接收窗口、零窗口探测，理解流量控制原理
6. **TCP 拥塞控制** —— 慢启动、拥塞避免、快速重传、快速恢复（这四个算法是 TCP 的核心）
7. **TCP 重传机制** —— 超时重传、快速重传、SACK（选择性确认）、D-SACK
8. **UDP 协议** —— UDP 头部结构、UDP 的优缺点、适用场景（视频流、DNS、QUIC）
9. **端口号** —— 知名端口（0-1023）、注册端口（1024-49151）、动态端口（49152-65535）、`/etc/services` 文件
10. **DNS 协议** —— DNS 的层级结构（根域、顶级域、二级域）、递归查询 vs 迭代查询、DNS 记录类型（A、AAAA、CNAME、MX、NS、TXT、PTR）
11. **DHCP 协议** —— 动态主机配置协议，DHCP 工作流程（Discovery → Offer → Request → ACK）
12. **NAT 网络地址转换** —— SNAT（源地址转换）、DNAT（目的地址转换）、PAT（端口地址转换）

### 第三阶段：应用层协议（2周）

1. **HTTP/1.1 协议** —— 请求方法（GET/POST/PUT/DELETE 等）、状态码（1xx/2xx/3xx/4xx/5xx）、头部字段（Host、User-Agent、Content-Type、Cookie 等）
2. **HTTP 连接管理** —— 短连接（HTTP/1.0）、持久连接（Keep-Alive，HTTP/1.1 默认）、管道化（Pipelining）
3. **HTTPS/TLS 协议** —— TLS 握手过程（Client Hello → Server Hello → 证书验证 → 密钥交换 → 加密通信）、对称加密 vs 非对称加密、CA 证书体系
4. **HTTP/2 协议** —— 二进制分帧、多路复用、头部压缩（HPACK）、服务器推送（Server Push）
5. **HTTP/3 和 QUIC** —— 基于 UDP 的 HTTP、0-RTT 握手、解决队头阻塞问题
6. **WebSocket 协议** —— 全双工通信、握手过程（Upgrade 头部）、适用场景（实时聊天、股票行情）
7. **RESTful API 设计** —— 资源导向、HTTP 方法语义、状态码使用、版本管理
8. **gRPC 和 Protobuf** —— 高性能 RPC 框架、Protocol Buffers 序列化、HTTP/2 多路复用
9. **SMTP 和邮件传输** —— 简单邮件传输协议、MUA/MTA/MDA 角色、邮件路由
10. **FTP 和 SFTP** —— 文件传输协议（控制连接 + 数据连接）、SFTP（基于 SSH 的安全文件传输）
11. **SSH 协议** —— 安全 Shell，SSH 握手过程、公钥认证原理、SSH 隧道（端口转发）
12. **网络抓包分析基础** —— 用 tcpdump 抓包、用 Wireshark 分析（我会专门讲这个，因为太重要了）

### 第四阶段：负载均衡与网络架构（2周）

1. **负载均衡基础概念** —— 为什么需要负载均衡、负载均衡的层级（L4 vs L7）、常见算法（轮询、加权轮询、最少连接、IP Hash）
2. **LVS（Linux Virtual Server）** —— LVS 的三种模式（NAT、DR、TUN）、LVS 的调度算法、LVS + Keepalived 高可用方案
3. **Nginx 四层负载均衡** —— `stream` 模块配置、TCP/UDP 负载均衡、健康检查配置
4. **Nginx 七层负载均衡** —— `http` 模块配置、upstream 定义、负载均衡算法配置、会话保持（ip_hash、sticky cookie）
5. **HAProxy** —— 高性能 TCP/HTTP 负载均衡器、HAProxy 配置语法、统计页面配置、与 Nginx 的对比
6. **Keepalived 高可用** —— VRRP 协议原理、Keepalived 配置（vrrp_instance、virtual_ipaddress）、脑裂问题及解决方案
7. **DNS 负载均衡** —— 通过 DNS 轮询实现负载均衡、GSLB（全局负载均衡）、智能 DNS（按地域解析）
8. **CDN（内容分发网络）** —— CDN 工作原理（边缘节点、回源）、CDN 的缓存策略、CDN 的适用场景
9. **网络架构设计** —— 三层网络架构（核心层、汇聚层、接入层）、叶脊（Leaf-Spine）架构、VPC（虚拟私有云）设计
10. **安全组与网络 ACL** —— 云环境下的虚拟防火墙、安全组（实例级别）、网络 ACL（子网级别）、应用场景
11. **NAT 网关与 VPN** —— NAT 网关的配置、IPsec VPN、SSL VPN、GRE 隧道
12. **网络性能优化** —— TCP 优化（调整内核参数）、启用 TCP BBR 拥塞控制算法、连接池、HTTP 长连接

### 第五阶段：网络故障排查与实战（2周）

1. **网络故障排查方法论** —— 从底层到高层逐层排查（物理层 → 数据链路层 → 网络层 → 传输层 → 应用层）
2. **物理层故障排查** —— 网线、光纤、网卡、交换机端口故障，`ethtool` 查看网卡状态
3. **网络层故障排查** —— IP 地址配置错误、路由错误、防火墙阻挡，`ping`、`traceroute`、`mtr` 的使用
4. **传输层故障排查** —— 端口未监听、防火墙阻挡、TCP 连接超时，`ss`、`netstat`、`telnet`、`nc` 的使用
5. **应用层故障排查** —— HTTP 状态码异常、DNS 解析失败、SSL 证书过期，`curl`、`openssl`、`dig` 的使用
6. **tcpdump 高级用法** —— 过滤表达式（host、port、tcp、udp）、捕获 HTTP 请求、捕获 DNS 查询
7. **Wireshark 使用技巧** —— 抓包过滤器（Capture Filter） vs 显示过滤器（Display Filter）、常见协议分析（TCP、HTTP、DNS）
8. **网络性能测试** —— `iperf3` 测试带宽、`ping` 测试延迟和丢包率、`mtr` 持续监控网络质量
9. **DNS 故障排查** —— `dig` 命令详解（追踪 DNS 解析过程）、DNS 缓存清理、DNS 劫持排查
10. **SSL/TLS 故障排查** —— `openssl s_client` 测试 SSL 握手、`curl -v` 查看 HTTPS 详细过程、证书链验证
11. **网络攻击与防御** —— DDoS 攻击（SYN Flood、UDP Flood）、MITM（中间人攻击）、ARP 欺骗、防御措施
12. **云网络故障排查** —— VPC 路由表配置、安全组规则、弹性网卡、弹性公网 IP，这些是云运维的必备技能

---

## 💻 实战命令 / 配置示例

下面这些命令和配置都是我日常工作中真实在用的。

### 1. 网络基础配置和查看

```bash
# 查看网卡配置（推荐使用 ip 命令，ifconfig 已过时）
ip addr show
# 简写
ip a

# 查看网卡统计信息（看有没有丢包、错误）
ip -s link

# 启用/禁用网卡
ip link set eth0 up
ip link set eth0 down

# 配置 IP 地址（临时配置，重启后失效）
ip addr add 192.168.1.100/24 dev eth0
# 删除 IP 地址
ip addr del 192.168.1.100/24 dev eth0

# 查看路由表
ip route show
# 添加默认网关
ip route add default via 192.168.1.1
# 添加静态路由
ip route add 10.0.0.0/8 via 192.168.1.1

# 查看 ARP 缓存
ip neigh show
# 清除 ARP 缓存
ip neigh flush all
```

### 2. 网络连通性测试

```bash
# ping 测试（发送 4 个包后停止）
ping -c 4 www.baidu.com
# ping 大包测试（测试 MTU 问题）
ping -s 1472 -M do www.baidu.com

# traceroute 追踪路由（看到每个跳的延迟）
traceroute www.baidu.com
# 用 TCP 方式追踪（能绕过防火墙对 UDP 的屏蔽）
traceroute -T -p 80 www.baidu.com

# mtr 持续监控网络质量（结合 ping 和 traceroute 的功能）
mtr -r -c 100 www.baidu.com
# 实时模式（类似 top）
mtr www.baidu.com

# 测试端口连通性
telnet 192.168.1.100 80
# 更现代的替代工具
nc -zv 192.168.1.100 80
```

### 3. DNS 解析测试和配置

```bash
# 查看 DNS 配置
cat /etc/resolv.conf

# nslookup 测试 DNS 解析（交互模式）
nslookup www.baidu.com
# 非交互模式
nslookup www.baidu.com 8.8.8.8

# dig 命令（我推荐用 dig，信息更全）
dig www.baidu.com
# 只看答案部分
dig www.baidu.com +short
# 追踪 DNS 解析过程（看每一级 DNS 服务器）
dig +trace www.baidu.com
# 反向解析（IP 到域名）
dig -x 8.8.8.8

# 查询特定类型的 DNS 记录
dig www.baidu.com A      # IPv4 地址
dig www.baidu.com AAAA   # IPv6 地址
dig www.baidu.com MX     # 邮件交换记录
dig www.baidu.com CNAME  # 别名记录
dig www.baidu.com NS     # 权威 DNS 服务器
```

### 4. 网络连接查看和故障排查

```bash
# 查看监听端口（推荐使用 ss，比 netstat 快）
ss -tulnp
# 查看已建立的 TCP 连接
ss -tan | grep ESTAB
# 查看 TCP 连接状态统计
ss -tan | awk '{print $1}' | sort | uniq -c

# 查看某个进程的网络连接
netstat -tulnp | grep nginx
# 或者（更现代的命令）
ss -tulnp | grep nginx

# 查看某个端口被哪个进程占用
lsof -i :80
# 或者
fuser -n tcp 80

# 抓包分析（tcpdump 是必备技能）
# 抓取 eth0 网卡上端口 80 的流量
tcpdump -i eth0 port 80 -nn -c 100
# 抓取特定主机的流量
tcpdump -i eth0 host 192.168.1.100 -nn
# 抓取 HTTP GET 请求（终端显示）
tcpdump -i eth0 -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
# 保存抓包结果到文件（用 Wireshark 分析）
tcpdump -i eth0 -w /tmp/capture.pcap
```

### 5. iptables 防火墙配置

```bash
# 查看当前 iptables 规则
iptables -L -n -v
# 查看 NAT 表
iptables -t nat -L -n -v

# 允许 SSH 连接（开放 22 端口）
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 允许已建立和相关的连接（这条很重要，放后面会被屏蔽）
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 允许本地回环接口
iptables -A INPUT -i lo -j ACCEPT

# 允许 ping
iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT

# 拒绝其他所有入站流量（默认策略）
iptables -P INPUT DROP

# SNAT（源地址转换，用于内网机器上网）
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE

# DNAT（目的地址转换，端口映射）
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 192.168.1.100:80

# 保存 iptables 规则（CentOS 6）
service iptables save
# 保存 iptables 规则（通用方法）
iptables-save > /etc/sysconfig/iptables
```

### 6. firewalld 防火墙配置（CentOS 8+/Rocky Linux）

```bash
# 查看防火墙状态
firewall-cmd --state

# 查看当前活动区域
firewall-cmd --get-active-zones

# 查看某个区域的规则
firewall-cmd --zone=public --list-all

# 开放端口
firewall-cmd --permanent --zone=public --add-port=80/tcp
# 开放服务（预定义的服务）
firewall-cmd --permanent --zone=public --add-service=http

# 端口转发（将 8080 转发到 80）
firewall-cmd --permanent --zone=public --add-forward-port=port=8080:proto=tcp:toport=80:toaddr=192.168.1.100

# 富规则（更复杂的规则）
# 允许特定 IP 访问 SSH
firewall-cmd --permanent --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="ssh" accept'

# 重新加载防火墙配置（让永久配置生效）
firewall-cmd --reload

# 禁用防火墙（不推荐，仅测试环境）
systemctl stop firewalld
systemctl disable firewalld
```

### 7. Nginx 负载均衡配置

```nginx
# /etc/nginx/nginx.conf 或 /etc/nginx/conf.d/loadbalancer.conf

# 定义上游服务器组（负载均衡后端）
upstream backend {
    # 负载均衡算法：轮询（默认）
    # least_conn;    # 最少连接数
    # ip_hash;        # 根据客户端 IP 哈希（会话保持）

    # 后端服务器列表
    server 192.168.1.101:80 weight=5;    # weight 表示权重
    server 192.168.1.102:80 weight=3;
    server 192.168.1.103:80 weight=2 backup;    # backup 表示备份服务器

    # 健康检查（需要 nginx_plus 或第三方模块，开源版用 max_fails）
    # max_fails=3 fail_timeout=30s 表示 30 秒内失败 3 次则标记为不可用
}

# HTTP 负载均衡配置
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://backend;
        # 传递真实客户端 IP
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;

        # 超时配置
        proxy_connect_timeout 5s;
        proxy_read_timeout 60s;
        proxy_send_timeout 60s;
    }
}

# TCP/UDP 四层负载均衡（需要 stream 模块）
stream {
    upstream mysql_backend {
        server 192.168.1.101:3306;
        server 192.168.1.102:3306;
    }

    server {
        listen 3306;
        proxy_pass mysql_backend;
        proxy_timeout 600s;
        proxy_responses 1;
    }
}
```

### 8. 网络性能测试和调优

```bash
# 安装 iperf3（需要在两台机器上运行）
yum install -y iperf3

# 在一台机器上启动 iperf3 服务端
iperf3 -s

# 在另一台机器上测试 TCP 带宽
iperf3 -c 192.168.1.100 -t 30
# 测试 UDP 带宽
iperf3 -c 192.168.1.100 -u -b 1G -t 30

# 查看网络接口统计（有没有丢包、错误）
ip -s link show eth0
# 查看网卡参数（速率、双工模式）
ethtool eth0

# 调整 TCP 拥塞控制算法为 BBR（Google 开发的，效果很好）
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p
# 验证
sysctl net.ipv4.tcp_congestion_control

# 调整 TCP 参数优化高并发（生产环境常用配置）
cat >> /etc/sysctl.conf <<EOF
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 0    # Linux 4.12+ 已移除这个参数
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_synack_retries = 2
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65535
EOF
sysctl -p
```

### 9. SSL/TLS 证书管理

```bash
# 生成 RSA 私钥（2048 位）
openssl genrsa -out server.key 2048

# 生成证书签名请求（CSR）
openssl req -new -key server.key -out server.csr
# 交互式填写信息（国家、省、市、组织、域名等）

# 查看 CSR 内容
openssl req -text -noout -verify -in server.csr

# 自签名证书（测试环境用）
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

# 查看证书内容
openssl x509 -text -noout -in server.crt

# 测试 SSL/TLS 握手
openssl s_client -connect www.baidu.com:443
# 只看证书
openssl s_client -connect www.baidu.com:443 </dev/null 2>/dev/null | openssl x509 -noout -text

# 用 Let's Encrypt 获取免费证书（需要安装 certbot）
yum install -y certbot
certbot certonly --standalone -d example.com -d www.example.com
```

### 10. HTTP/HTTPS 测试（curl 高级用法）

```bash
# 发送 GET 请求
curl http://example.com

# 发送 POST 请求（提交表单）
curl -X POST -d "username=admin&password=123456" http://example.com/login

# 发送 JSON 数据
curl -X POST -H "Content-Type: application/json" -d '{"name":"zhangsan","age":25}' http://example.com/api

# 查看 HTTP 响应头
curl -I http://example.com

# 查看请求和响应的详细信息（调试必备）
curl -v http://example.com
# 只看响应头（包括重定向）
curl -LI http://example.com

# 测试 HTTPS（忽略证书验证，测试环境用）
curl -k https://example.com

# 使用客户端证书
curl --cert client.crt --key client.key https://example.com

# 测试 HTTP/2
curl -I --http2 https://example.com

# 下载文件（显示进度条）
curl -# -O http://example.com/file.tar.gz
# 断点续传
curl -C - -O http://example.com/bigfile.iso
```

### 11. 配置 Bind DNS 服务器（简单示例）

```bash
# 安装 Bind
yum install -y bind bind-utils

# 编辑主配置文件 /etc/named.conf
# 允许查询的 IP 段
# allow-query     { any; };
# 允许递归查询
# recursion yes;

# 配置区域文件 /etc/named.rfc1912.zones
zone "example.com" IN {
    type master;
    file "example.com.zone";
    allow-update { none; };
};

# 创建区域文件 /var/named/example.com.zone
$TTL 86400
@   IN  SOA ns1.example.com. admin.example.com. (
            2024010101  ; Serial
            3600        ; Refresh
            1800        ; Retry
            604800      ; Expire
            86400 )     ; Minimum TTL

@       IN  NS      ns1.example.com.
@       IN  A       192.168.1.100
ns1     IN  A       192.168.1.100
www     IN  A       192.168.1.101
mail    IN  A       192.168.1.102
@       IN  MX 10   mail.example.com.
```

### 12. 网络配置持久化（不同发行版）

```bash
# CentOS 7/8, Rocky Linux: 用 nmcli 或编辑 /etc/sysconfig/network-scripts/
# 方法1: nmcli（推荐）
nmcli con add type ethernet con-name eth0 ifname eth0
nmcli con modify eth0 ipv4.addresses 192.168.1.100/24
nmcli con modify eth0 ipv4.gateway 192.168.1.1
nmcli con modify eth0 ipv4.dns "8.8.8.8 114.114.114.114"
nmcli con modify eth0 ipv4.method manual
nmcli con up eth0

# 方法2: 编辑配置文件 /etc/sysconfig/network-scripts/ifcfg-eth0
TYPE=Ethernet
BOOTPROTO=static
NAME=eth0
DEVICE=eth0
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
DNS2=114.114.114.114

# Ubuntu 18.04+: 编辑 /etc/netplan/*.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses: [192.168.1.100/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 114.114.114.114]
# 应用配置
netplan apply
```

---

## 🧪 实战项目

下面这 3 个项目覆盖了网络模块的核心技能点。

### 项目一：搭建 DNS 服务器和内部域名解析系统

**项目目标**：在企业内部搭建一套 DNS 系统，实现内部域名解析和公网域名缓存。

**步骤**：

1. 准备两台服务器（master 和 slave，实现高可用）
2. 安装 Bind9 DNS 服务器：`yum install -y bind bind-utils`
3. 配置主 DNS 服务器：
   - 编辑 `/etc/named.conf`，配置允许查询的 IP 段
   - 创建正向解析区域（example.com）
   - 创建反向解析区域（1.168.192.in-addr.arpa）
4. 配置从 DNS 服务器（区域传输）
5. 配置公网域名缓存（forwarders 配置，转发到 8.8.8.8 或 114.114.114.114）
6. 配置 DNS 安全（DNSSEC、限制递归查询）
7. 在客户端配置 DNS 指向你的 DNS 服务器
8. 用 `dig` 命令测试解析是否正常

**验收标准**：内部域名能正常解析，公网域名能通过你的 DNS 服务器解析。

### 项目二：搭建 Nginx 负载均衡集群

**项目目标**：用 Nginx 搭建一套高可用的负载均衡集群，实现 Web 服务的负载均衡和故障自动切换。

**步骤**：

1. 准备 4 台服务器：
   - 2 台负载均衡器（LB1、LB2，用 Keepalived 实现高可用）
   - 2 台 Web 服务器（Web1、Web2，运行 Nginx 或 Apache）
2. 在 Web 服务器上部署测试网站
3. 在 LB1 和 LB2 上安装 Nginx 和 Keepalived
4. 配置 Nginx 负载均衡（upstream 模块，配置后端服务器列表）
5. 配置 Keepalived（VRRP 协议，虚拟 IP 飘移）
6. 配置健康检查（Nginx 主动健康检查或利用 max_fails）
7. 测试负载均衡效果（访问虚拟 IP，看请求是否分发到不同后端）
8. 测试高可用（关闭 LB1，看虚拟 IP 是否漂移到 LB2）
9. 配置 Nginx 状态监控（stub_status 模块）

**验收标准**：负载均衡正常工作，后端服务器故障能自动摘除，负载均衡器故障能自动切换。

### 项目三：企业网络架构设计和实现

**项目目标**：用 GNS3 或 EVE-NG 网络模拟器，设计一套中型企业的网络架构。

**步骤**：

1. 网络需求分析：
   - 员工 200 人，分财务部、人事部、技术部、访客区
   - 需要 DMZ 区放置对外服务器（Web、Mail）
   - 需要运维管理网（带外管理）
2. 用 GNS3 搭建网络拓扑：
   - 核心交换机（三层交换机，做 VLAN 间路由）
   - 接入交换机（二层交换机，接终端设备）
   - 路由器（连接公网）
   - 防火墙（分隔内网和 DMZ）
3. 配置 VLAN（虚拟局域网）：
   - VLAN 10：财务部（192.168.10.0/24）
   - VLAN 20：人事部（192.168.20.0/24）
   - VLAN 30：技术部（192.168.30.0/24）
   - VLAN 99：访客区（192.168.99.0/24，限制只能访问公网）
4. 配置 ACL（访问控制列表）：
   - 访客区不能访问内网
   - 财务部只能特定 IP 访问
5. 配置 NAT（内网用户访问公网）
6. 配置 DHCP 服务器（自动分配 IP 地址）
7. 测试网络连通性（用 ping、traceroute）

**验收标准**：网络拓扑符合设计，VLAN 隔离生效，ACL 规则生效，内网能访问公网。

---

## 🔧 常见故障排查

### 故障一：网站访问慢，用户反馈打开页面要 10 多秒

**故障现象**：用户访问网站响应慢，但服务器 CPU、内存、磁盘使用率都不高。

**诊断步骤**：

```bash
# 1. 测试网络延迟和丢包率
ping -c 100 www.example.com
mtr -r -c 100 www.example.com

# 2. 用 curl 测试各阶段耗时（DNS 解析、TCP 连接、TLS 握手、数据传输）
curl -w "@curl-format.txt" -o /dev/null -s http://example.com
# curl-format.txt 内容：
#      time_namelookup:  %{time_namelookup}\n
#         time_connect:  %{time_connect}\n
#      time_appconnect:  %{time_appconnect}\n
#     time_pretransfer:  %{time_pretransfer}\n
#        time_redirect:  %{time_redirect}\n
#   time_starttransfer:  %{time_starttransfer}\n
#                     ----------\n
#          time_total:  %{time_total}\n

# 3. 如果 DNS 解析慢，检查 DNS 配置
dig www.example.com +trace
# 看看是哪一级 DNS 慢

# 4. 如果 TCP 连接慢，抓包分析
tcpdump -i eth0 -w /tmp/tcp.pcap port 80
# 用 Wireshark 分析 TCP 握手时间

# 5. 如果 TLS 握手慢，检查证书链是否完整
openssl s_client -connect www.example.com:443 -servername www.example.com

# 6. 检查是否有过多的 TCP 连接
ss -tan | grep ESTAB | wc -l
# 如果连接数太多，可能是 Keep-Alive 配置不合理
```

**解决方案**：

- 如果是 DNS 解析慢，更换更快的 DNS 服务器（如 8.8.8.8、119.29.29.29）
- 如果是 TCP 连接慢，启用 TCP Fast Open、调整 `tcp_syn_retries`
- 如果是 TLS 握手慢，优化证书链（减少证书链长度）、启用 TLS 1.3、开启 OCSP Stapling
- 如果是数据传输慢，启用 Gzip 压缩、启用 HTTP/2、优化图片等静态资源
- 长期方案：上 CDN

### 故障二：服务器无法访问外网，但内网正常

**故障现象**：服务器能 ping 通同网段的其他机器，但 ping 不通公网 IP（如 8.8.8.8）。

**诊断步骤**：

```bash
# 1. 检查 IP 配置
ip addr show
# 看 IP 地址、子网掩码是否正确

# 2. 检查路由表
ip route show
# 看有没有默认路由（default 或 0.0.0.0/0）

# 3. 如果有默认路由，测试到达网关的连通性
ping <网关IP>

# 4. 如果网关通，测试公网 IP
ping 8.8.8.8

# 5. 如果公网 IP 不通，可能是防火墙或 ISP 的问题
traceroute 8.8.8.8
# 看路由在哪里断了

# 6. 如果域名 ping 不通但 IP 能 ping 通，是 DNS 问题
cat /etc/resolv.conf
# 检查 DNS 配置
dig www.baidu.com
```

**解决方案**：

- 如果没有默认路由，添加：`ip route add default via <网关IP>`
- 如果 DNS 配置错误，修改 `/etc/resolv.conf` 或 NetworkManager 配置
- 如果是防火墙阻挡，检查 `iptables -L` 或 `firewall-cmd --list-all`
- 如果是 ISP 问题，联系网络运营商

### 故障三：Nginx 负载均衡后端频繁摘除

**故障现象**：Nginx 负载均衡的后端服务器频繁被标记为不可用，用户访问不稳定。

**诊断步骤**：

```bash
# 1. 查看 Nginx 错误日志
tail -f /var/log/nginx/error.log

# 2. 查看后端服务器健康状态
curl http://backend-server/health

# 3. 检查网络连接数
ss -tan | grep ESTAB | wc -l

# 4. 检查后端服务器的资源使用
ssh backend-server "top"
ssh backend-server "free -h"

# 5. 用 tcpdump 抓包，看 Nginx 和后端的通信
tcpdump -i eth0 host <backend-ip> -w /tmp/nginx-backend.pcap
```

**解决方案**：

- 调整 Nginx 的 `max_fails` 和 `fail_timeout` 参数（默认可能太严格）
- 配置更合理的健康检查（用 `nginx_upstream_check_module` 第三方模块）
- 优化后端服务器的性能（数据库慢查询、代码性能问题）
- 增加后端服务器数量，降低单台压力

### 故障四：DNS 解析失败或解析到错误 IP

**故障现象**：访问某个域名，解析到的 IP 不是预期的，或者解析失败。

**诊断步骤**：

```bash
# 1. 用 dig 追踪解析过程
dig +trace www.example.com

# 2. 查看本地 DNS 缓存（如果用 systemd-resolved）
systemd-resolve --statistics
# 清除缓存
systemd-resolve --flush-caches

# 3. 检查 /etc/hosts 文件（可能被恶意修改）
cat /etc/hosts

# 4. 检查是否被 DNS 劫持（用不同 DNS 服务器解析，看结果是否一致）
dig @8.8.8.8 www.example.com
dig @114.114.114.114 www.example.com
# 如果结果不同，可能被运营商 DNS 劫持

# 5. 检查 DNS 服务器配置
cat /etc/resolv.conf
```

**解决方案**：

- 如果是 `/etc/hosts` 被恶意修改，恢复并加固服务器安全
- 如果是 DNS 劫持，更换 DNS 服务器（用 8.8.8.8 或 119.29.29.29）
- 如果是 DNS 记录配置错误，登录域名管理平台修改 DNS 记录
- 配置 DNSSEC（防止 DNS 欺骗）

### 故障五：网络丢包严重，导致应用超时

**故障现象**：网络延迟正常，但丢包率很高（超过 1%），导致 TCP 重传、应用超时。

**诊断步骤**：

```bash
# 1. 用 mtr 持续监控网络质量（看每一跳的丢包率）
mtr -r -c 100 <目标IP>

# 2. 查看网卡统计（看有没有丢包、错误）
ip -s link show eth0
# 关注 tx/rx 的 errors、dropped、overruns

# 3. 查看网络拥塞情况
netstat -s | grep -i "segments retransmited"
# 如果重传数很高，说明网络有丢包

# 4. 用 tcpdump 抓包分析（看是不是只有特定类型的包丢失）
tcpdump -i eth0 -w /tmp/capture.pcap host <目标IP>

# 5. 检查是不是 MTU 问题（ICMP 分片Needed 但 DF 位被设置）
ping -s 1472 -M do <目标IP>
# 如果不通，说明 MTU 有问题，需要调整 MTU 或开启 MSS Clamping
```

**解决方案**：

- 如果是网卡问题，更换网卡或网线
- 如果是交换机端口问题，更换端口
- 如果是 MTU 不匹配，调整 MTU（如改成 1450 或开启 MSS Clamping）
- 如果是网络拥塞，联系运营商扩容链路
- 临时方案：调整 TCP 拥塞控制算法（如换成 BBR）

---

## 💼 面试高频题

### 1. 说一下 TCP 三次握手的过程，为什么是三次而不是两次？

**参考答案**：

**三次握手过程**：

1. 客户端发送 SYN（同步序列编号）包到服务器，进入 SYN_SENT 状态
2. 服务器收到 SYN 包，返回 SYN+ACK 包，进入 SYN_RCVD 状态
3. 客户端收到 SYN+ACK 包，返回 ACK 包，双方进入 ESTABLISHED 状态

**为什么是三次**：

- **两次不安全**：如果只有两次握手，服务器无法确认客户端的接收能力。假设客户端发送的第一个 SYN 包因为网络延迟很久才到达服务器，客户端以为丢失就重发了，第二次成功连接并关闭后，第一次的 SYN 包才到，服务器会误以为客户端又要建立连接，造成资源浪费。
- **两次无法同步序列号**：TCP 是用序列号来做可靠传输的，三次握手可以让双方都确认对方的初始序列号（ISN）。
- **防止旧连接干扰**：网络中可能存在的旧 SYN 包到达服务器，如果是两次握手，服务器会误以为是新连接请求。

**加分回答**：能说一下 SYN Flood 攻击的原理和防御方法（SYN Cookie、限制 SYN 半连接队列）。

### 2. 说一下 TCP 四次挥手的过程，为什么是四次而不是三次？

**参考答案**：

**四次挥手过程**：

1. 客户端发送 FIN 包（表示不再发送数据），进入 FIN_WAIT_1 状态
2. 服务器收到 FIN，返回 ACK 包，进入 CLOSE_WAIT 状态（此时服务器可能还有数据要发送）
3. 服务器数据发送完毕后，发送 FIN 包，进入 LAST_ACK 状态
4. 客户端收到 FIN，返回 ACK 包，进入 TIME_WAIT 状态，等待 2MSL 后关闭

**为什么是四次**：

- 因为 TCP 是全双工的，数据可以在两个方向同时传输。关闭连接时，每个方向必须单独关闭。
- 客户端发送 FIN 只是表示客户端不再发送数据，但还可以接收数据（半关闭状态）。
- 服务器可能还有数据要发送给客户端，所以不能马上发 FIN，只能先 ACK，等数据发完再发 FIN。
- 如果服务器没有数据要发送，可以合并 ACK 和 FIN，变成三次挥手（但并不常见）。

**TIME_WAIT 的作用**：

- 确保最后一个 ACK 能到达服务器（如果丢失，服务器会重传 FIN）
- 等待足够长的时间，让本连接持续时间内产生的所有报文都从网络中消失，避免影响新连接。

### 3. HTTP 和 HTTPS 的区别是什么？HTTPS 的握手过程是怎样的？

**参考答案**：

**HTTP vs HTTPS**：

- HTTP 是明文传输，不安全；HTTPS 是加密传输，安全
- HTTP 默认端口 80；HTTPS 默认端口 443
- HTTPS 需要申请 SSL/TLS 证书
- HTTPS 有 TLS 握手过程，会增加延迟（但 TLS 1.3 已经大幅优化）

**HTTPS/TLS 握手过程（以 TLS 1.2 为例）**：

1. **Client Hello**：客户端发送支持的 TLS 版本、加密套件列表、随机数（Client Random）
2. **Server Hello**：服务器选择 TLS 版本和加密套件，发送随机数（Server Random）、证书
3. **证书验证**：客户端验证服务器证书（是否可信、是否过期、域名是否匹配）
4. **密钥交换**：
   - 如果是 RSA 密钥交换：客户端生成预主密钥（Pre-Master Secret），用服务器公钥加密后发送
   - 如果是 DH 密钥交换：双方各自生成 DH 参数，交换后计算出相同的预主密钥
5. **生成会话密钥**：双方用 Client Random + Server Random + Pre-Master Secret 生成会话密钥
6. **Finished**：双方用会话密钥加密通信，握手完成

**加分回答**：能说一下 TLS 1.3 的改进（减少握手往返次数，支持 0-RTT）。

### 4. 说一下 DNS 的递归查询和迭代查询的区别

**参考答案**：

- **递归查询**（Recursive Query）：DNS 服务器必须向客户端返回一个确定的答案（要么解析成功，要么返回错误）。如果 DNS 服务器不知道答案，它会代替客户端向其他 DNS 服务器查询，直到得到答案。
  - 典型场景：客户端向本地 DNS 服务器发起的是递归查询。
- **迭代查询**（Iterative Query）：DNS 服务器返回它能给的最佳答案（可能是下一级 DNS 服务器的地址），让客户端自己去查询。
  - 典型场景：本地 DNS 服务器向根 DNS、顶级域 DNS、权威 DNS 发起的是迭代查询。

**DNS 解析完整过程**（以访问 www.example.com 为例）：

1. 客户端向本地 DNS 服务器发起递归查询
2. 本地 DNS 服务器向根 DNS 服务器发起迭代查询，根 DNS 返回 .com 顶级域 DNS 地址
3. 本地 DNS 向 .com 顶级域 DNS 发起迭代查询，返回 example.com 权威 DNS 地址
4. 本地 DNS 向 example.com 权威 DNS 发起迭代查询，返回 www.example.com 的 IP 地址
5. 本地 DNS 将结果返回给客户端（同时缓存这个结果）

### 5. 负载均衡的算法有哪些？各自适用什么场景？

**参考答案**：

1. **轮询（Round Robin）**：按顺序将请求分发到每台服务器。
   - 适用场景：每台服务器性能相近，请求处理时间相近。
2. **加权轮询（Weighted Round Robin）**：给性能好的服务器分配更高的权重。
   - 适用场景：服务器性能不一致。
3. **最少连接（Least Connections）**：将请求分发到当前连接数最少的服务器。
   - 适用场景：请求处理时间差异较大（避免某台服务器堆积太多长连接）。
4. **加权最少连接（Weighted Least Connections）**：结合权重和连接数。
5. **IP Hash**：根据客户端 IP 计算哈希值，分发到固定服务器。
   - 适用场景：需要会话保持（Session Persistence），但不想用 Cookie。
6. **URL Hash**：根据请求的 URL 计算哈希值。
   - 适用场景：实现缓存定向（同一 URL 总是到同一台服务器，提高缓存命中率）。
7. **随机（Random）**：随机分发请求。
   - 适用场景：服务器性能相近，简单场景。

### 6. 说一下 Nginx 和 LVS 的区别，各自适用什么场景？

**参考答案**：

| 维度 | Nginx | LVS |
|------|-------|-----|
| 工作层级 | 七层（应用层），也能做四层 | 四层（传输层） |
| 性能 | 较高（但比 LVS 低） | 极高（基于内核，性能接近硬件负载均衡） |
| 功能 | 支持 HTTP 路由、URL 重写、缓存等 | 只做包转发，功能简单 |
| 配置复杂度 | 简单，灵活 | 较复杂 |
| 健康检查 | 支持（需要第三方模块或自己实现） | 支持 |
| 适用场景 | Web 应用负载均衡、需要七层路由的场景 | 对性能要求极高的场景、TCP/UDP 负载均衡 |

**我的建议**：如果是 Web 应用，用 Nginx；如果是数据库、消息队列等 TCP 服务，用 LVS 或 HAProxy。

### 7. 说一下 TCP 的拥塞控制机制

**参考答案**：

TCP 拥塞控制有四种算法：

1. **慢启动**（Slow Start）：初始拥塞窗口（cwnd）很小（通常是 1 个 MSS），每收到一个 ACK，cwnd 翻倍。指数增长，快速探测带宽。
2. **拥塞避免**（Congestion Avoidance）：当 cwnd 超过慢启动阈值（ssthresh）后，进入拥塞避免阶段。每 RTT 只增加 1 个 MSS，线性增长。
3. **快速重传**（Fast Retransmit）：收到 3 个重复 ACK，立即重传丢失的包，不用等超时。
4. **快速恢复**（Fast Recovery）：快速重传后，ssthresh 减半，cwnd 设为 ssthresh + 3，进入快速恢复阶段（而不是回到慢启动）。

**加分回答**：能说一下 TCP BBR 算法（Google 开发的，不基于丢包，而是基于带宽和延迟估算，效果很好）。

### 8. 如何排查网络延迟高的问题？

**参考答案**：

按网络层级逐层排查：

1. **物理层**：检查网线、光纤、网卡有没有问题（`ethtool eth0` 看网卡状态）
2. **网络层**：
   - 用 `ping` 测试延迟
   - 用 `traceroute` 或 `mtr` 找出延迟高的跳
   - 如果是局域网延迟高，检查交换机性能、网线质量
   - 如果是广域网延迟高，联系运营商
3. **传输层**：
   - 用 `ss -tan` 查看 TCP 连接状态（有没有大量 TIME_WAIT、SYN_RECV）
   - 抓包分析（用 Wireshark 看 TCP 握手时间、重传情况）
4. **应用层**：
   - 用 `curl -w` 测试 DNS 解析时间、TCP 连接时间、TLS 握手时间、服务端响应时间
   - 如果是服务端响应慢，排查应用性能（数据库慢查询、代码性能问题）

---

## 📈 进阶学习路径

学完网络基础，你可以根据自己的发展方向选择进阶路线：

### 路线一：网络工程师（传统网络 → 云网络）

1. **网络协议深入**：BGP、OSPF、IS-IS 等路由协议，VLAN、STP、VXLAN 等二层技术
2. **网络设备管理**：Cisco、华为、H3C 交换机和路由器配置
3. **网络设计**：企业网络架构设计、数据中心网络设计、SD-WAN
4. **网络安全**：防火墙、VPN、IPS/IDS、DDoS 防御
5. **云网络**：VPC、弹性网卡、负载均衡器、NAT 网关（AWS VPC、阿里云 VPC）

### 路线二：运维工程师（网络 + 系统 + 自动化）

1. **网络自动化**：用 Python 操作网络设备（Netmiko、Napalm）、Ansible 网络自动化
2. **容器网络**：Docker 网络模型（bridge、host、overlay）、Kubernetes 网络（CNI、Flannel、Calico）
3. **服务网格**：Istio、Linkerd（七层网络治理）
4. **网络可观测性**：网络流量监控（ntopng）、网络抓包分析平台（Arkime）

### 路线三：SRE（网络性能优化 + 故障排查）

1. **网络性能调优**：TCP 参数调优、内核网络栈调优、网卡队列调优
2. **网络故障演练**：混沌工程（模拟网络延迟、丢包、分区）
3. **网络可观测性**：指标（网络流量、丢包率、错误率）、分布式追踪（Jaeger、Zipkin）

### 推荐的学习资源（进阶）

- **书籍**：《TCP/IP 详解 卷2：实现》（看 TCP 协议栈源码）、《计算机网络：系统方法》（侧重网络系统架构）
- **在线实验**：GNS3（网络模拟器）、容器网络实验（用 Docker 搭建各种网络拓扑）
- **认证**：Cisco CCNA/CCNP（网络工程师认证）、AWS Advanced Networking（云网络认证）

---

[← 返回中文版首页](../README.md)
