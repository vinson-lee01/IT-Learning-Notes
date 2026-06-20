# 01 · Linux 基础

> **Linux 是运维工程师的立身之本。**
>
> 我常跟新人说：无论容器、K8s、云原生如何演进，Linux 基础不牢，一切都无从谈起。你在 K8s 里排障，最终还是要回到节点上敲命令；你写 Ansible Playbook，底层还是 SSH 到 Linux 执行。
>
> 这个模块我花了最大力气整理，因为我自己就是从这里一路走过来的。2015 年我第一次装 CentOS 6，连 vim 都不会退出，到现在能徒手写内核参数调优方案——Linux 这条路，没有捷径，就是多敲命令、多踩坑。
>
> 本模块定位 **零基础 → 生产级系统管理员**，学完你能独立维护 50 台以上的服务器集群。

---

## 🎯 学习目标

学完这个模块，你应该能够：

- [ ] 独立完成 CentOS Stream / Rocky Linux / Ubuntu 的系统安装与基础配置（分区方案、网络配置、软件源）
- [ ] 精通 Linux 目录结构（FHS 标准），知道 `/etc`、`/var`、`/proc`、`/sys` 各自干什么用
- [ ] 熟练使用 vim 编辑器（我推荐直接用 vim，别用 nano，生产环境不一定有 nano）
- [ ] 掌握文件权限体系（rwx、SUID/SGID/Sticky Bit、ACL），能排查权限导致的各种诡异问题
- [ ] 熟练使用 grep / sed / awk 文本三剑客，这是我日常运维最高频的工具
- [ ] 掌握用户与用户组管理，理解 `/etc/passwd`、`/etc/shadow`、`/etc/group` 每一列的含义
- [ ] 精通进程管理（ps、top、htop、pidstat），能快速定位 CPU 100% 的罪魁祸首
- [ ] 掌握内存管理（free、vmstat、slabtop），理解 buffer / cache / available 的区别
- [ ] 熟练使用磁盘管理工具（df、du、fdisk、lsblk、LVM），能独立完成在线扩容
- [ ] 掌握日志管理（journalctl、rsyslog、logrotate），能配置自动化日志轮转
- [ ] 理解 systemd 体系（unit 文件、target、service 编写），这是现代 Linux 的标配
- [ ] 掌握网络基础命令（ip、ss、netstat、tcpdump），能独立排查网络连通性问题
- [ ] 熟悉软件包管理（yum/dnf/apt），能搭建本地 yum 仓库
- [ ] 掌握基础的安全加固（防火墙 firewalld/iptables、SELinux、ssh 安全配置）
- [ ] 具备独立排查系统故障的能力（OOM、磁盘满、inode 耗尽、中病毒等真实场景）

---

## 📺 推荐视频教程

我筛选了 B 站上质量最高的 Linux 教程，都是我自己看过或者团队里推荐过的。

| # | 教程标题 | UP 主 | 链接 | 播放量 | 难度 | 推荐理由 |
|---|---------|-------|------|--------|------|---------|
| 1 | 《一周学会 Linux》 | 韩顺平 | [BV1Sv411r7vd](https://www.bilibili.com/video/BV1Sv411r7vd) | 1200万+ | ⭐ 入门 | 韩老师讲课风格亲切，适合零基础，我推荐给很多转行的小伙伴 |
| 2 | 《Linux 教程-尚硅谷》 | 尚硅谷 | [BV1mW411i7Qf](https://www.bilibili.com/video/BV1mW411i7Qf) | 600万+ | ⭐⭐ 系统 | 体系完整，从安装到 Shell 全覆盖，适合系统学习 |
| 3 | 《老男孩 Linux 运维》 | 老男孩教育 | [BV1tV411o7Cm](https://www.bilibili.com/video/BV1tV411o7Cm) | 200万+ | ⭐⭐ 实战 | 贴近生产，有很多企业级案例 |
| 4 | 《Linux 性能优化实战》 | 倪鹏飞（极客时间） | [BV1KQ4y1W7ских](https://www.bilibili.com/video/BV1KQ4y1W7ских) | 80万+ | ⭐⭐⭐ 进阶 | 性能调优专著，适合有一定基础后深入 |
| 5 | 《RHCE8 认证课程》 | 课堂唐工 | [BV1Xy4y1a7Wz](https://www.bilibili.com/video/BV1Xy4y1a7Wz) | 50万+ | ⭐⭐⭐ 认证 | 红帽认证体系，企业认可度高 |
| 6 | 《Linux 内核原理》 | 斯坦福公开课翻译 | [BV1z7411U7aA](https://www.bilibili.com/video/BV1z7411U7aA) | 30万+ | ⭐⭐⭐⭐ 深入 | 想深入理解内核机制的看这个 |
| 7 | 《sed 和 awk 神器》 | 马哥 Linux | [BV1Tt411x7ey](https://www.bilibili.com/video/BV1Tt411x7ey) | 40万+ | ⭐⭐ 工具 | 文本处理三剑客专项突破 |
| 8 | 《Linux 系统安全加固》 | 安全牛课堂 | [BV1gK4y1a71W](https://www.bilibili.com/video/BV1gK4y1a71W) | 15万+ | ⭐⭐⭐ 安全 | 等保合规、安全加固实战 |

> **我的建议**：零基础先看韩顺平，有基础直接上尚硅谷，工作后遇到性能问题再看倪鹏飞的优化实战。

---

## 📖 推荐书籍

这些书都是我书架上有的，有些已经翻烂了。

| # | 书名 | 作者 | 豆瓣评分 | 适合阶段 | 我的推荐理由 |
|---|------|------|----------|---------|-------------|
| 1 | 《鸟哥的 Linux 私房菜——基础篇》 | 鸟哥 | **9.1** | 零基础入门 | 这本书不用多说，Linux 入门圣经。我 2015 年就是看这个学会的，现在还经常翻。最新版基于 CentOS 7/8，内容非常接地气。 |
| 2 | 《Linux 命令行与 Shell 脚本编程大全（第4版）》 | Richard Blum | **8.8** | 入门→进阶 | 这本书把 Linux 命令和 Shell 脚本结合在一起讲，非常适合想往自动化方向发展的同学。我推荐买纸质书，随时查阅。 |
| 3 | 《Linux 运维之道（第2版）》 | 丁明一 | **8.5** | 生产实战 | 这本书最大的特点是贴近实战，作者把多年运维经验融进去了。我特别喜欢里面关于系统调优和故障排查的章节。 |
| 4 | 《Linux 就该这么学》 | 刘遄 | **8.3** | RHCE 认证 | 这本书是RHCE 认证导向的，如果你想考红帽认证，这本是必备的。内容编排很合理，每章有习题。 |
| 5 | 《UNIX/Linux 系统管理技术手册（第5版）》 | Evi Nemeth | **9.3** | 进阶→专家 | 这本书被很多人称为"系统管理员百科全书"，内容极其全面。缺点是比较厚，建议作为工具书查阅，不用一口气读完。 |
| 6 | 《深入理解 Linux 内核（第3版）》 | Daniel P. Bovet | **9.2** | 内核深入 | 想深入理解 Linux 底层的同学必读。我是在遇到一些诡异的内核 bug 后才下定决心啃这本的，收获很大。 |
| 7 | 《Linux 高性能服务器构建实战》 | 高俊峰 | **8.7** | 生产实战 | 高老师是运维圈的老前辈了，这本书里有大量生产环境的真实案例，特别是性能调优部分，非常实用。 |

> **购书建议**：鸟哥的书必买，其他根据需求选。我个人的书架上，鸟哥 + 运维之道 + 系统管理技术手册 这三本是最常用的。

---

## 🌐 在线参考资源

这些是我日常工作中经常查阅的网站和仓库。

| # | 资源名称 | 链接 | 类型 | 说明 |
|---|---------|------|------|------|
| 1 | Linux 命令大全（中文） | [github.com/jaywcjlove/linux-command](https://github.com/jaywcjlove/linux-command) ⭐36k | GitHub 仓库 | 中文最全的 Linux 命令速查，每个命令都有中文示例，我每天都会用到 |
| 2 | linux-tutorial | [github.com/dunwu/linux-tutorial](https://github.com/dunwu/linux-tutorial) ⭐6.8k | GitHub 仓库 | dunwu 大佬的系统化 Linux 教程，涵盖基础到进阶，质量很高 |
| 3 | 红帽官方文档 | [access.redhat.com/documentation](https://access.redhat.com/documentation) | 官方文档 | 企业级权威文档，虽然是基于 RHEL 的，但对所有 Linux 发行版都有参考价值 |
| 4 | tldr（命令简洁版 man） | [tldr.sh](https://tldr.sh/) | 工具网站 | 比 man 页面友好太多，直接给你最常用的命令示例。我推荐安装 tldr 客户端：`npm install -g tldr` |
| 5 | Linux 中国 | [linux.cn](https://linux.cn/) | 中文社区 | 国内最活跃的 Linux 中文社区，有很多优质的翻译教程和原创文章 |
| 6 | 掘金 Linux 标签 | [juejin.cn/tag/Linux](https://juejin.cn/tag/Linux) | 中文社区 | 很多一线运维工程师分享实战经验，我经常在通勤路上刷 |
| 7 | The Linux Documentation Project | [tldp.org](https://tldp.org/) | 官方文档 | 最古老的 Linux 文档项目，HOWTO 系列非常经典 |
| 8 | Linux Kernel Documentation | [kernel.org/doc](https://kernel.org/doc/) | 官方文档 | 内核官方文档，想深入研究内核的必看 |
| 9 | 腾讯云 Linux 运维文档 | [cloud.tencent.com/document/product/213](https://cloud.tencent.com/document/product/213) | 云厂商文档 | 国内云厂商的 Linux 最佳实践，很多可以直接用到生产环境 |
| 10 | explainshell.com | [explainshell.com](https://explainshell.com/) | 工具网站 | 输入任何 Linux 命令，它帮你逐段解释含义。我教新人时经常让他们先用这个理解命令 |

> **我的使用习惯**：查命令用 tldr 和 linux-command；学新东西看 dunwu 的教程；遇到诡异问题翻红帽官方文档；给团队培训时参考鸟哥的体系。

---

## 📝 核心知识点清单

这是本模块最核心的部分。我把它分成 5 个阶段，每个阶段 10-12 个知识点，共 50+ 条。建议你打印出来，一条一条过。

### 第一阶段：系统安装与基础操作（1-2周）

这个阶段的目标是：能独立安装系统，能在命令行里活下来。

1. **Linux 发行版选择** —— CentOS Stream / Rocky Linux / AlmaLinux / Ubuntu / Debian 的区别与选型建议。生产环境我推荐 Rocky 或 Ubuntu LTS。
2. **虚拟化环境搭建** —— VMware Workstation / VirtualBox 安装与配置，快照管理（这个很重要，做实验随时回滚）
3. **系统安装全流程** —— 分区方案设计（/boot、/、/home、swap 的推荐大小）、网络配置、软件源配置
4. **第一次启动后的基础配置** —— 主机名修改、sudo 配置、SSH 服务配置、防火墙初始化
5. **Linux 目录结构（FHS 标准）** —— 理解 `/bin`、`/sbin`、`/etc`、`/var`、`/usr`、`/proc`、`/sys`、`/dev` 各自的职责
6. **绝对路径与相对路径** —— 这是新手最容易混淆的概念，必须搞清楚
7. **vim 编辑器入门** —— 我强烈推荐直接用 vim，别用 nano。掌握普通模式、插入模式、命令模式的切换，以及保存退出（:wq）
8. **文件操作基础命令** —— `ls`（重点掌握 -l、-a、-h 参数）、`cp`、`mv`、`rm`（慎用 -rf）、`touch`、`mkdir`（-p 参数很有用）
9. **查看文件内容** —— `cat`、`less`（比 more 好用）、`head`、`tail`（-f 参数实时追踪日志，我每天用）
10. **文件搜索** —— `find`（重点掌握 -name、-type、-mtime 参数）、`locate`、`which`、`whereis`
11. **软链接与硬链接** —— 理解 inode，知道 `ln -s` 和 `ln` 的区别。我面试必问这个。
12. **压缩与解压** —— `tar -czvf` / `tar -xzvf`（最常用）、`zip` / `unzip`、`gzip` / `gunzip`

### 第二阶段：用户、权限与软件管理（2-3周）

这个阶段的目标是：能管理多用户环境，能控制权限，能安装软件。

1. **用户管理** —— `/etc/passwd` 和 `/etc/shadow` 文件详解（每一列的含义都必须背下来）、`useradd`（理解 -m、-s、-G 参数）、`usermod`、`userdel`、`passwd`
2. **用户组管理** —— `/etc/group` 文件详解、`groupadd`、`groupmod`、`groupdel`、将用户加入附加组
3. **文件权限基础** —— rwx 权限的含义（读=4、写=2、执行=1）、`chmod`（数字模式和符号模式都要掌握）、`chown`（递归修改 -R）
4. **特殊权限位** —— SUID（让普通用户临时获得 root 权限，如 passwd 命令）、SGID（目录继承）、Sticky Bit（/tmp 目录的权限）
5. **ACL 访问控制列表** —— 当基础权限不够用时，`setfacl` 和 `getfacl` 可以精细化控制权限
6. **sudo 配置** —— `/etc/sudoers` 文件配置（建议用 `visudo` 编辑，有语法检查）、配置免密 sudo、配置 sudo 命令白名单
7. **软件包管理（RPM 系）** —— `rpm` 命令基础（查询、安装、卸载）、`yum` / `dnf` 的工作原理、配置国内 yum 源（阿里云、清华源）
8. **软件包管理（Debian 系）** —— `dpkg` 命令基础、`apt` / `apt-get` 的使用、配置国内 apt 源
9. **搭建本地 yum 仓库** —— 生产环境很多服务器不能连外网，需要搭建本地仓库。用 `createrepo` 命令。
10. **源码编译安装** —— `./configure` && `make` && `make install` 三部曲，理解每个步骤在干什么
11. **PAM 认证模块基础** —— 了解 `/etc/pam.d/` 目录，知道如何配置密码策略和登录限制
12. **登录日志审计** —— `/var/log/secure`、`last`、`lastb`、`who`、`w` 命令，排查非法登录

### 第三阶段：进程、内存与磁盘管理（2-3周）

这个阶段的目标是：能监控服务器资源，能定位性能瓶颈。

1. **进程基础概念** —— PID、PPID、守护进程（daemon）、孤儿进程、僵尸进程（zombie）
2. **进程查看命令** —— `ps aux`（我最常用的进程查看命令）、`ps -ef`、`top`（重点理解每列含义）、`htop`（比 top 更友好）
3. **进程控制** —— `kill`（理解 -1、-9、-15 信号的区别）、`pkill`、`killall`、`nice` / `renice`（调整进程优先级）
4. **系统负载（Load Average）** —— 理解 1分钟、5分钟、15分钟负载的含义，负载多少算高？这个公式要记住：负载 / CPU核数
5. **内存管理命令** —— `free -h`（重点理解 available 列，不是 free 列）、`vmstat`（我排查内存问题必用）、`slabtop`（内核缓存分析）
6. **buffer 与 cache 的区别** —— 这是面试高频题。buffer 是缓冲（写操作），cache 是缓存（读操作）
7. **磁盘使用查看** —— `df -h`（看文件系统级别）、`du -sh *`（看目录级别，找大文件神器）
8. **磁盘分区工具** —— `fdisk`（MBR 分区表，支持最大 2TB）、`gdisk`（GPT 分区表，支持更大磁盘）、`parted`（更强大的分区工具）
9. **LVM 逻辑卷管理** —— 这是生产环境必用的。`pvcreate` → `vgcreate` → `lvcreate`，以及在线扩容 `lvextend` + `resize2fs`
10. **磁盘挂载与卸载** —— `/etc/fstab` 文件详解（每一列都要理解）、`mount`、`umount`、查看 UUID（`blkid`）
11. **inode 概念与排查** —— 理解 inode，知道 `df -i` 查看 inode 使用情况。我遇到过 inode 耗尽导致无法创建文件的问题。
12. **系统监控工具合集** —— `iostat`（磁盘 IO）、`iftop`（网络流量）、`nethogs`（按进程查看网络）、`dstat`（综合监控）

### 第四阶段：系统服务与启动管理（2周）

这个阶段的目标是：理解 Linux 的启动流程，能管理 systemd 服务。

1. **Linux 启动流程详解** —— BIOS → MBR → GRUB → kernel → initramfs → systemd → 登录提示符。我建议画一张图把它记住。
2. **GRUB 引导加载器** —— `/etc/default/grub` 配置、内核启动参数修改、单用户模式进入（破解 root 密码）
3. **systemd 体系架构** —— 为什么 systemd 取代了 SysVinit？理解 unit 的概念（service、target、socket、timer 等）
4. **systemd 服务管理** —— `systemctl start/stop/restart/status/reload`、`systemctl enable/disable`、`systemctl list-units`
5. **编写 systemd service 文件** —— 这是我经常要做的事。掌握 `[Unit]`、`[Service]`（ExecStart、Restart、User）、`[Install]` 各字段含义
6. **target 运行级别** —— 理解 `multi-user.target`（命令行模式）和 `graphical.target`（图形模式），以及 `systemctl set-default`
7. **journalctl 日志管理** —— systemd 的日志系统，比传统 syslog 更强大。`journalctl -u 服务名`、`journalctl -f`、`journalctl --since`
8. **rsyslog 传统日志系统** —— `/etc/rsyslog.conf` 配置、日志设施（facility）和优先级（priority）、远程日志配置
9. **logrotate 日志轮转** —— 这个太重要了，不配置日志轮转，磁盘很快被撑满。`/etc/logrotate.conf` 和 `/etc/logrotate.d/` 目录
10. **crontab 定时任务** —— `/etc/crontab` 和系统 crontab 的区别、`crontab -e`（用户级）、`crontab -l`、cron 表达式（秒级要用 systemd timer）
11. **systemd timer** —— cron 的现代替代品，支持更灵活的调度（如"每次启动后1小时执行"）
12. **内核参数调优** —— `sysctl` 命令、`/etc/sysctl.conf` 配置。我常用的调优参数：`net.ipv4.ip_forward`、`vm.swappiness`、`fs.file-max`

### 第五阶段：网络基础与故障排查（2-3周）

这个阶段的目标是：能配置网络，能排查常见的网络问题。

1. **网络接口配置** —— `ip addr`（取代 ifconfig）、`ip link`、`nmcli`（NetworkManager 命令行工具）、网卡配置文件（`/etc/sysconfig/network-scripts/` 或 `/etc/netplan/`）
2. **路由配置** —— `ip route` 查看和配置路由表、默认网关配置、`traceroute` / `mtr`（网络连通性排查神器）
3. **DNS 配置与排查** —— `/etc/resolv.conf`、`nslookup`、`dig`（我推荐用 dig，比 nslookup 信息更全）、`host` 命令
4. **网络连通性测试** —— `ping`（基础）、`telnet`（测试端口连通性，虽然过时但很实用）、`nc`（netcat，网络排查瑞士军刀）
5. **网络连接查看** —— `ss`（取代 netstat，速度更快）、`netstat -tulnp`（查看监听端口）、`lsof -i :端口号`
6. **网络抓包分析** —— `tcpdump` 基础用法（我常用的：`tcpdump -i eth0 port 80 -nn -c 100`）、Wireshark 简介
7. **防火墙管理（firewalld）** —— `firewall-cmd` 命令、`zone` 概念、开放端口、端口转发配置
8. **防火墙管理（iptables）** —— 虽然 firewalld 是主流，但很多老系统还在用 iptables。理解表（filter、nat、mangle）和链（INPUT、OUTPUT、FORWARD）
9. **SSH 服务深度配置** —— `/etc/ssh/sshd_config` 关键参数（Port、PermitRootLogin、PasswordAuthentication、PubkeyAuthentication）、密钥登录配置
10. **SCP 与 rsync 文件传输** —— `scp` 基础用法、`rsync -avz`（增量同步，我每天用来做备份）、`rsync` 通过 SSH 传输
11. **网络绑定（Bonding）与桥接（Bridge）** —— 生产环境高可用必备，了解几种 bonding 模式（mode=0~6）
12. **网络性能调优基础** —— 理解 MTU、TCP 拥塞控制算法（cubic、bbr）、`ethtool` 查看网卡参数

---

## 💻 实战命令 / 配置示例

下面这些命令都是我日常工作中真实在用的，不是教科书上的伪代码。建议你在自己的实验环境里逐条敲一遍。

### 1. 查看系统信息和资源使用

```bash
# 查看系统版本（比 cat /etc/redhat-release 更通用）
cat /etc/os-release

# 查看 CPU 信息
lscpu
# 或者
cat /proc/cpuinfo | grep "model name" | head -1

# 查看内存使用情况（我每天用的命令）
free -h
# 重点关注 available 列，这才是真正可用的内存

# 查看磁盘使用情况
df -h
# 找出大文件（找出 /var 下大于 100M 的文件）
find /var -type f -size +100M -exec ls -lh {} \;

# 查看系统负载和进程
top
# 或者更友好的 htop（需要安装）
htop
```

### 2. 用户和权限管理

```bash
# 创建用户并设置密码（自动创建家目录，指定 shell）
useradd -m -s /bin/bash zhangsan
passwd zhangsan

# 将用户加入 sudo 组（Ubuntu）或 wheel 组（CentOS）
usermod -aG sudo zhangsan    # Ubuntu
usermod -aG wheel zhangsan   # CentOS

# 配置 sudo 免密（编辑 /etc/sudoers，建议用 visudo）
# 添加这一行：zhangsan ALL=(ALL) NOPASSWD: ALL

# 修改文件权限（递归修改目录权限）
chmod -R 755 /path/to/dir
# 修改文件属主（递归）
chown -R nginx:nginx /var/www/html

# 设置特殊权限位（SUID，让普通用户能执行需要 root 权限的命令）
chmod u+s /usr/bin/passwd
# Sticky Bit（只有文件所有者能删除自己的文件，/tmp 目录默认有这个权限）
chmod +t /shared/dir
```

### 3. 文本处理三剑客实战

```bash
# grep：过滤日志中的 ERROR 信息（我很常用的命令）
grep "ERROR" /var/log/app.log
# 显示行号
grep -n "ERROR" /var/log/app.log
# 统计出现次数
grep -c "ERROR" /var/log/app.log
# 排除某个关键词
grep -v "INFO" /var/log/app.log

# sed：替换文件中的字符串（直接修改文件用 -i 参数）
sed -i 's/old_string/new_string/g' /path/to/file
# 删除空行
sed -i '/^$/d' /path/to/file
# 在匹配行后插入新行
sed -i '/pattern/a\new line content' /path/to/file

# awk：处理结构化文本（如日志分析）
# 打印 /etc/passwd 的用户名和 shell
awk -F: '{print $1, $7}' /etc/passwd
# 统计 nginx 访问日志的 IP 访问量 TOP 10
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10
```

### 4. 进程管理和故障排查

```bash
# 查看某个进程的详细信息
ps aux | grep nginx
# 以树状结构显示进程
pstree -p
# 查看某个进程打开的文件（排查文件句柄泄露很有用）
lsof -p <PID>

# 找出 CPU 使用率最高的进程（我排查性能问题的第一步）
ps aux --sort=-%cpu | head -10
# 找出内存使用率最高的进程
ps aux --sort=-%mem | head -10

# 杀死进程（优先用 -15，不行再用 -9）
kill -15 <PID>
# 强制杀死（慎用，可能导致数据丢失）
kill -9 <PID>

# 实时查看系统资源（每 2 秒刷新一次）
vmstat 2
# 查看磁盘 IO 使用情况
iostat -x 2
```

### 5. 网络配置和排查

```bash
# 查看网卡配置（推荐使用 ip 命令，ifconfig 已过时）
ip addr show
# 简写
ip a

# 查看路由表
ip route show
# 添加默认网关
ip route add default via 192.168.1.1

# 查看监听端口（推荐使用 ss，比 netstat 快）
ss -tulnp
# 查看已建立的 TCP 连接
ss -tan | grep ESTAB

# 测试端口连通性（telnet 虽然老但很实用）
telnet 192.168.1.100 80
# 更现代的替代工具
nc -zv 192.168.1.100 80

# DNS 解析测试（推荐用 dig）
dig www.baidu.com
# 反向解析
dig -x 8.8.8.8
```

### 6. 磁盘管理和 LVM 操作

```bash
# 查看磁盘分区情况
lsblk
fdisk -l

# 创建 LVM 物理卷
pvcreate /dev/sdb
# 创建卷组
vgcreate vg_data /dev/sdb
# 创建逻辑卷（使用全部空间）
lvcreate -l 100%FREE -n lv_data vg_data
# 格式化为 ext4
mkfs.ext4 /dev/vg_data/lv_data
# 挂载
mount /dev/vg_data/lv_data /data

# LVM 在线扩容（这是生产环境最常用的操作）
lvextend -L +10G /dev/vg_data/lv_data
# 调整文件系统大小（ext4）
resize2fs /dev/vg_data/lv_data
# 如果是 xfs 文件系统
xfs_growfs /data
```

### 7. 日志管理和分析

```bash
# 查看系统日志（systemd 系统）
journalctl -xe
# 查看某个服务的日志
journalctl -u nginx.service -f
# 查看今天以来的日志
journalctl --since today

# 查看传统日志
tail -f /var/log/messages    # CentOS
tail -f /var/log/syslog      # Ubuntu
# 查看安全日志（登录记录）
tail -f /var/log/secure      # CentOS
tail -f /var/log/auth.log    # Ubuntu

# 日志搜索（在大量日志中快速定位问题）
grep -i "error" /var/log/messages | tail -50
# 查看某个时间段的日志
sed -n '/2024-01-01 10:00/,/2024-01-01 11:00/p' /var/log/app.log
```

### 8. 定时任务和自动化

```bash
# 编辑当前用户的 crontab
crontab -e
# 示例：每天凌晨 2 点执行备份脚本
0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1
# 示例：每 5 分钟检查一次服务状态
*/5 * * * * /opt/scripts/check_service.sh

# 系统级 crontab（需要 root 权限）
vim /etc/crontab
# 格式：分 时 日 月 周 用户 命令
0 * * * * root /usr/local/bin/cleanup.sh

# 创建 systemd timer（比 cron 更灵活）
# 1. 创建服务文件 /etc/systemd/system/backup.service
# 2. 创建定时器文件 /etc/systemd/system/backup.timer
# 3. 启用定时器
systemctl enable --now backup.timer
```

### 9. 系统服务管理（systemd）

```bash
# 编写一个简单的 systemd 服务（以 nginx 为例）
cat > /etc/systemd/system/myapp.service <<EOF
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=nginx
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/bin/start.sh
Restart=always
RestartSec=10s

[Install]
WantedBy=multi-user.target
EOF

# 重新加载 systemd 配置
systemctl daemon-reload
# 启动服务
systemctl start myapp
# 设置开机自启
systemctl enable myapp
# 查看服务状态
systemctl status myapp
```

### 10. 安全加固常用命令

```bash
# 禁用 root 远程登录（修改 SSH 配置）
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl restart sshd

# 修改 SSH 默认端口
sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# 配置防火墙（firewalld）
firewall-cmd --permanent --add-port=2222/tcp
firewall-cmd --permanent --remove-service=ssh
firewall-cmd --reload

# 查看登录失败记录（防暴力破解）
lastb | head -20
# 用 fail2ban 自动封禁暴力破解 IP（推荐安装）
yum install -y fail2ban
```

### 11. 软件包管理和仓库搭建

```bash
# 配置阿里云 yum 源（CentOS 8/Rocky Linux）
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=https://mirrors.aliyun.com|g' /etc/yum.repos.d/CentOS-*

# 清理 yum 缓存并重建
yum clean all
yum makecache

# 查看某个命令属于哪个软件包
yum provides */ifconfig
# 或者（更现代的命令）
dnf provides */ifconfig

# 搭建本地 yum 仓库（内网环境必备）
# 1. 安装 createrepo
yum install -y createrepo
# 2. 把所有 rpm 包放到一个目录
mkdir -p /opt/local_repo
# 3. 创建仓库元数据
createrepo /opt/local_repo
# 4. 创建 repo 文件
cat > /etc/yum.repos.d/local.repo <<EOF
[local]
name=Local Repository
baseurl=file:///opt/local_repo
enabled=1
gpgcheck=0
EOF
```

### 12. 系统性能基准测试

```bash
# CPU 性能测试（计算圆周率）
time echo "scale=5000; 4*a(1)" | bc -l

# 内存性能测试（用 dd 命令）
dd if=/dev/zero of=/tmp/test bs=1M count=1024 conv=fdatasync

# 磁盘 IO 性能测试（用 fio，需要安装）
# 随机读测试
fio --name=randread --ioengine=libaio --rw=randread --bs=4k --numjobs=4 --iodepth=32 --size=1G --runtime=60 --group_reporting --filename=/data/testfile

# 网络性能测试（需要在两台机器上运行 iperf3）
# 服务端
iperf3 -s
# 客户端
iperf3 -c 192.168.1.100 -t 30
```

---

## 🧪 实战项目

理论学完一定要做项目，不然很快就会忘。下面这 3 个项目都是我精心设计的，难度递进。

### 项目一：搭建 Linux 实验环境 + 基础配置

**项目目标**：搭建一套完整的 Linux 学习实验环境，并完成基础安全配置。

**步骤**：

1. 安装 VirtualBox 或 VMware Workstation（我推荐 VMware，快照功能更强大）
2. 创建 3 台虚拟机：
   - 主机名：linux-master，IP：192.168.56.10，配置：2CPU/4GB/40GB
   - 主机名：linux-node1，IP：192.168.56.11，配置：2CPU/2GB/20GB
   - 主机名：linux-node2，IP：192.168.56.12，配置：2CPU/2GB/20GB
3. 操作系统选择：Rocky Linux 8.8 或 Ubuntu 22.04 LTS
4. 完成基础配置：
   - 配置静态 IP（用 nmcli 或 netplan）
   - 修改主机名（`hostnamectl set-hostname`）
   - 配置 `/etc/hosts` 文件（三台机器能互相解析主机名）
   - 关闭 SELinux（或者配置成 permissive 模式）
   - 配置防火墙规则（开放 SSH 端口，其他端口按需开放）
   - 配置国内 yum/apt 源
   - 安装常用工具：`vim`、`wget`、`curl`、`net-tools`、`bind-utils`
5. 配置 SSH 密钥登录（在三台机器之间实现免密登录）
6. 编写系统初始化脚本（把所有上述步骤写成一个 Shell 脚本）

**验收标准**：三台机器能互相 SSH 免密登录，系统基础配置符合要求。

### 项目二：系统监控和日志管理方案

**项目目标**：搭建一套基础的系统监控和日志收集方案。

**步骤**：

1. 在 linux-master 上安装 Prometheus + Node Exporter：
   ```bash
   # 下载 Node Exporter
   wget https://github.com/prometheus/node_exporter/releases/download/v1.6.0/node_exporter-1.6.0.linux-amd64.tar.gz
   # 解压并安装为系统服务
   ```
2. 编写 systemd service 文件，让 Node Exporter 开机自启
3. 在 linux-master 上安装 Prometheus，配置抓取 Node Exporter 指标
4. 在三台机器上都部署 Node Exporter，统一被 Prometheus 监控
5. 配置日志集中收集：
   - 安装 rsyslog，配置 linux-node1 和 linux-node2 的日志发送到 linux-master
   - 在 linux-master 上配置 rsyslog 接收远程日志
6. 编写日志分析脚本：
   - 统计每天的错误日志数量
   - 分析 SSH 登录失败 IP，自动加入黑名单（用 firewalld 封禁）
7. 配置 logrotate，让日志自动轮转，避免磁盘被撑满

**验收标准**：Prometheus 能正常采集三台机器的指标，日志能集中收集到 master 节点。

### 项目三：自动化运维脚本集

**项目目标**：编写一套生产级运维脚本，实现常见的自动化运维任务。

**步骤**：

1. 编写服务器批量操作脚本（`batch_op.sh`）：
   - 从配置文件读取主机列表
   - 支持批量执行命令、批量分发文件
   - 增加错误处理和日志记录
2. 编写系统资源监控脚本（`monitor.sh`）：
   - 监控 CPU、内存、磁盘使用率
   - 超过阈值发送告警（邮件或企业微信）
   - 加入 crontab，每 5 分钟执行一次
3. 编写应用健康检查脚本（`health_check.sh`）：
   - 检查 Nginx/MySQL/Redis 等服务是否正常运行
   - 如果服务挂了，自动重启（用 systemctl）
   - 记录每次检查和恢复操作到日志文件
4. 编写系统初始化检查脚本（`system_check.sh`）：
   - 检查系统基础配置（主机名、DNS、时间同步等）
   - 检查安全配置（root 登录、防火墙、SELinux）
   - 检查资源使用情况和系统负载
   - 生成系统状态报告（发送到运维群）
5. 把所有脚本加入 Git 版本管理，编写 README 说明文档

**验收标准**：脚本能在实际环境中正常运行，实现预期的自动化功能。

---

## 🔧 常见故障排查

我在生产环境中遇到过各种各样的问题，下面这 5 个是最常见的故障场景。

### 故障一：服务器 CPU 使用率 100%

**故障现象**：服务器响应缓慢，登录卡顿，`top` 命令看到 CPU 使用率接近 100%。

**诊断步骤**：

```bash
# 1. 找出 CPU 使用率最高的进程
ps aux --sort=-%cpu | head -10

# 2. 查看该进程的线程情况（可能是一个多线程程序的某个线程出了问题）
top -H -p <PID>

# 3. 查看进程在干什么（用 strace 跟踪系统调用）
strace -p <PID>

# 4. 如果是 Java 程序，用 jstack 导出线程栈
jstack <PID> > /tmp/thread_dump.txt

# 5. 查看系统负载（判断是 CPU 密集型还是 IO 等待导致）
vmstat 2 5
# 如果 wa（IO 等待）很高，说明是磁盘 IO 问题
```

**解决方案**：

- 如果是业务程序死循环，联系开发修复代码
- 如果是被恶意挖矿程序入侵（我很常见），用 `ps -ef` 找到可疑进程，删除相关文件，检查定时任务
- 如果是 IO 等待导致，优化磁盘 IO（换 SSD、优化数据库查询）
- 临时方案：重启相关服务或限制 CPU 使用率（`cpulimit` 命令）

### 故障二：服务器磁盘空间满（Disk Full）

**故障现象**：无法写入文件，日志报错 "No space left on device"。

**诊断步骤**：

```bash
# 1. 查看磁盘使用情况
df -h
# 找到使用率 100% 的分区

# 2. 找出该分区下的大文件
du -sh /* | sort -rh | head -10
# 逐层深入，找到占用空间最大的目录

# 3. 常见的大文件位置
ls -lh /var/log/        # 日志文件
ls -lh /tmp/            # 临时文件
find / -type f -size +500M -exec ls -lh {} \; 2>/dev/null  # 找出大于 500M 的文件

# 4. 检查是否是 inode 耗尽（这种情况 df -h 看起来还有空间）
df -i
# 如果 IUsed 接近 IUse%，说明是 inode 耗尽
```

**解决方案**：

- 删除不必要的大文件（优先删日志、临时文件）
- 配置 logrotate，让日志自动轮转
- 如果是 inode 耗尽，找出大量小文件的目录（通常是缓存或日志），清理或归档
- 长期方案：扩容磁盘或迁移数据到新磁盘

### 故障三：SSH 无法登录服务器

**故障现象**：SSH 连接超时或拒绝连接。

**诊断步骤**：

```bash
# 1. 检查网络连通性
ping <服务器IP>

# 2. 检查 SSH 端口是否开放
telnet <服务器IP> 22
# 或者
nc -zv <服务器IP> 22

# 3. 如果网络通但端口不通，可能是防火墙问题
# 在服务器上检查防火墙规则
firewall-cmd --list-all
# 或者 iptables -L -n

# 4. 检查 SSH 服务是否运行
systemctl status sshd

# 5. 查看 SSH 日志（看看有没有拒绝登录的记录）
tail -f /var/log/secure      # CentOS
tail -f /var/log/auth.log    # Ubuntu
```

**解决方案**：

- 如果是防火墙问题，添加防火墙规则开放 SSH 端口
- 如果是 SSH 服务挂了，重启 sshd 服务
- 如果是 IP 被拉黑（fail2ban），将 IP 从黑名单中移除
- 如果是因为 root 登录被禁用，用普通用户登录后 `su - root`
- 最坏情况：通过 IPMI/iDRAC/KVM 控制台登录服务器

### 故障四：Linux 系统时间不同步

**故障现象**：服务器时间不准确，导致日志时间错乱、证书验证失败等问题。

**诊断步骤**：

```bash
# 1. 查看当前系统时间
date

# 2. 查看硬件时间（BIOS 时间）
hwclock

# 3. 检查时间同步服务是否运行
systemctl status chronyd    # CentOS 8/Rocky Linux
systemctl status systemd-timesyncd    # Ubuntu

# 4. 查看时间同步源
chronyc sources -v    # 如果用 chrony
```

**解决方案**：

```bash
# 安装并配置 chrony（现代 Linux 推荐用 chrony，比 ntp 更好）
yum install -y chrony    # CentOS
apt install -y chrony     # Ubuntu

# 配置国内 NTP 服务器（编辑 /etc/chrony.conf）
# 添加：
# server ntp.aliyun.com iburst
# server ntp.tuna.tsinghua.edu.cn iburst

# 启动 chrony 服务
systemctl enable --now chronyd

# 手动同步一次
chronyc -a makestep

# 设置时区（中国市场用 Asia/Shanghai）
timedatectl set-timezone Asia/Shanghai
```

### 故障五：Linux 系统假死（Load Average 很高但 CPU 使用率不高）

**故障现象**：服务器响应极慢，load average 很高（超过 CPU 核数的 5 倍），但 `top` 显示 CPU 使用率不高。

**诊断步骤**：

```bash
# 1. 查看系统负载
uptime
# 或者
top
# 关注 load average 和 CPU 使用率的 wa（IO 等待）值

# 2. 查看 IO 等待情况
vmstat 2 5
# 如果 wa 列很高（超过 30%），说明是磁盘 IO 瓶颈

# 3. 找出导致 IO 等待的进程
iotop
# 如果没有 iotop，用 pidstat
pidstat -d 2

# 4. 查看磁盘 IO 性能
iostat -x 2 5
# 关注 %util 列（磁盘利用率）和 await 列（IO 等待时间）
```

**解决方案**：

- 如果是备份任务或大数据处理导致的 IO 高峰，调整任务执行时间（放到凌晨）
- 如果是数据库 IO 瓶颈，优化 SQL 查询或加索引
- 如果是磁盘性能不足，考虑升级到 SSD
- 临时方案：用 `ionice` 调整进程的 IO 优先级

---

## 💼 面试高频题

这些题都是我面试别人或者被别人面试时真实遇到的。

### 1. 说一下 Linux 启动流程（从按下电源键到登录提示符）

**参考答案**：

1. **BIOS/UEFI**：加电自检（POST），检测硬件，从启动设备加载引导程序
2. **GRUB**：加载 GRUB 引导加载器，显示启动菜单，加载内核镜像和 initramfs
3. **内核初始化**：解压内核，检测硬件，加载驱动（initramfs 里的临时驱动），挂载真正的根文件系统
4. **systemd 启动**：内核启动 systemd（PID 1），systemd 根据 default.target 启动各个 unit
5. **用户登录**：启动 getty 或显示登录管理器，等待用户登录

**加分回答**：能画出流程图，能说清楚 initramfs 的作用，知道如何进入单用户模式重置 root 密码。

### 2. 软链接和硬链接的区别是什么？

**参考答案**：

- **硬链接**（hard link）：多个文件名指向同一个 inode。特点：不能跨文件系统；不能对目录创建硬链接；删除源文件不影响硬链接文件；`ls -l` 第 2 列是硬链接计数
- **软链接**（soft link / symbolic link）：类似于 Windows 的快捷方式，是一个特殊的文件，内容是目标文件的路径。特点：可以跨文件系统；可以对目录创建软链接；删除源文件，软链接失效（ dangling link）；`ls -l` 显示 `->` 指向目标

**验证命令**：

```bash
# 创建硬链接
ln source.txt hard_link.txt
# 创建软链接
ln -s source.txt soft_link.txt
# 查看 inode 号（硬链接的 inode 相同，软链接不同）
ls -i source.txt hard_link.txt soft_link.txt
```

### 3. 说一下 Linux 的文件权限体系（rwx、SUID、SGID、Sticky Bit）

**参考答案**：

- **基础权限**（rwx）：读（4）、写（2）、执行（1）。分为用户（u）、用户组（g）、其他（o）三个维度
- **SUID**（Set UID，4）：让普通用户在执行该程序时临时获得文件所有者的权限。典型例子：`/usr/bin/passwd`（属于 root，普通用户执行时能修改 `/etc/shadow`）
- **SGID**（Set GID，2）：对文件来说，执行时获得文件用户组的权限；对目录来说，新建的文件自动继承目录的用户组
- **Sticky Bit**（1）：只对目录有效，用户只能删除自己创建的文件。典型例子：`/tmp` 目录

**查看命令**：

```bash
# 查看 passwd 命令的权限（有 SUID 位）
ls -l /usr/bin/passwd
# 输出：-rwsr-xr-x，s 表示 SUID 位已设置

# 查看 /tmp 目录的权限（有 Sticky Bit）
ls -ld /tmp
# 输出：drwxrwxrwt，t 表示 Sticky Bit 已设置
```

### 4. 如何查看系统的 CPU 使用率、内存使用率、磁盘 IO？

**参考答案**：

- **CPU**：`top`（实时）、`vmstat`（周期性统计）、`pidstat`（按进程统计）
- **内存**：`free -h`（概览）、`vmstat`（详细统计）、`slabtop`（内核缓存）
- **磁盘 IO**：`iostat -x`（整体 IO 统计）、`iotop`（按进程统计）、`pidstat -d`（按进程统计）

**加分回答**：能说清楚 `free -h` 输出中 `available` 和 `free` 的区别（available 才是真正可用的内存，包含了可以回收的 cache/buffer）。

### 5. 说一下 Linux 的 LVM 是什么，有什么好处？

**参考答案**：

LVM（Logical Volume Manager）是 Linux 的逻辑卷管理器，它介于文件系统和物理磁盘之间，提供了一层抽象。

**核心概念**：

- **PV**（Physical Volume）：物理卷，可以是整个磁盘或磁盘分区
- **VG**（Volume Group）：卷组，由多个 PV 组成，相当于一个存储池
- **LV**（Logical Volume）：逻辑卷，从 VG 中划分出来，相当于传统意义上的"分区"

**好处**：

1. **在线扩容**：不用停机就能扩展文件系统（这是最大的好处）
2. **灵活分配**：可以跨多个物理磁盘创建逻辑卷
3. **快照功能**：可以做 LVM 快照，用于备份
4. **动态调整**：可以动态调整 LV 的大小

**常用命令**：

```bash
# 创建 LVM
pvcreate /dev/sdb
vgcreate vg_data /dev/sdb
lvcreate -L 10G -n lv_data vg_data

# 在线扩容
lvextend -L +5G /dev/vg_data/lv_data
resize2fs /dev/vg_data/lv_data    # ext4
xfs_growfs /data                   # xfs
```

### 6. 说一下 systemd 和传统 SysVinit 的区别

**参考答案**：

- **并行启动**：systemd 可以并行启动服务，启动速度更快；SysVinit 是串行启动
- **依赖管理**：systemd 通过 unit 文件管理依赖关系；SysVinit 通过脚本顺序控制
- **日志管理**：systemd 有统一的 journald 日志系统；SysVinit 日志分散在各个文件中
- **功能更全面**：systemd 集成了日志、定时任务（timer）、挂载管理等功能；SysVinit 只负责启动

**加分回答**：能说一下 systemd 的争议（有人认为它违反了 Unix 哲学"一个程序只做一件事"）。

### 7. 如何排查 Linux 服务器无法访问外网的问题？

**参考答案**：

按网络层级从底向上排查：

1. **物理层**：检查网线是否插好、网卡指示灯是否正常（`ip link` 看状态是不是 UP）
2. **网络层**：
   - 检查 IP 地址配置（`ip addr`）
   - 检查路由表（`ip route`）
   - 检查能否 ping 通网关（`ping 网关IP`）
3. **传输层**：检查防火墙是否阻挡（`firewall-cmd --list-all` 或 `iptables -L`）
4. **应用层**：
   - 检查 DNS 配置（`cat /etc/resolv.conf`）
   - 用 `nslookup` 或 `dig` 测试 DNS 解析
   - 检查代理配置（`env | grep -i proxy`）

### 8. 说一下 /proc 和 /sys 目录的作用

**参考答案**：

- **/proc**：proc 文件系统，是一个虚拟文件系统，不占用磁盘空间。它提供了内核和进程的实时信息。
  - `/proc/cpuinfo`：CPU 信息
  - `/proc/meminfo`：内存信息
  - `/proc/loadavg`：系统负载
  - `/proc/<PID>/`：每个进程的信息
  - `/proc/sys/`：内核参数（可以用 `sysctl` 命令修改）
- **/sys**：sysfs 文件系统，也是虚拟文件系统，提供内核对象的接口（主要是设备驱动信息）。
  - `/sys/block/`：块设备信息
  - `/sys/class/net/`：网络接口信息
  - 很多内核参数可以通过写 `/sys/` 下的文件来动态调整

**加分回答**：能举出实际使用的例子，如 `echo 1 > /proc/sys/net/ipv4/ip_forward` 开启 IP 转发。

---

## 📈 进阶学习路径

学完 Linux 基础，你应该根据自己的发展方向选择进阶路线：

### 路线一：运维工程师（传统运维 → 云计算运维）

1. **Linux 进阶**：内核参数调优、系统性能基准测试、大规模服务器集群管理
2. **网络进阶**：TCP/IP 协议深入、网络抓包分析（Wireshark）、SDN/NFV 基础
3. **脚本自动化**：Shell 脚本编程（本路线图 03 模块）、Python 运维开发
4. **监控体系**：Prometheus + Grafana、Zabbix、ELK 日志分析
5. **云计算**：AWS EC2、阿里云 ECS、腾讯云 CVM、OpenStack
6. **容器技术**：Docker（本路线图 04 模块）、Kubernetes（本路线图 05 模块）

### 路线二：SRE（Site Reliability Engineering）

1. **Linux 性能优化**：深入理解 CPU、内存、IO、网络性能瓶颈定位
2. **可观测性**：指标（Metrics）、日志（Logs）、链路追踪（Tracing）
3. **自动化运维**：Infrastructure as Code（Terraform、Ansible）
4. **混沌工程**：故障注入、韧性测试
5. **SLO/SLI/SLA**：服务水平目标、指标、协议的设计与落地

### 路线三：DevOps 工程师

1. **CI/CD 流水线**：Jenkins、GitLab CI、GitHub Actions（本路线图 06 模块）
2. **容器编排**：Kubernetes 深入、Helm、Operator 开发
3. **GitOps**：ArgoCD、FluxCD
4. **云原生技术栈**：Istio（服务网格）、Knative（Serverless）、Prometheus（监控）

### 推荐的学习资源（进阶）

- **书籍**：《性能之巅（第2版）》（Brendan Gregg 著，豆瓣 9.5）、《Site Reliability Engineering》（Google SRE Book）
- **在线课程**：极客时间《Linux 性能优化实战》（倪鹏飞）、《SRE 实战手册》
- **认证**：红帽 RHCE（系统管理）、CKA（Kubernetes 管理）、AWS Solutions Architect

---

[← 返回中文版首页](../README.md)
