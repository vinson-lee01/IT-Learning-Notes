# 03 · Shell 脚本自动化

> 脚本能力是运维的必备技能。重复的操作写成脚本，效率提升 10 倍不止。
> 这个模块我从零开始讲，假设你只会 `ls` 和 `cd`。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 熟练使用 Bash 基础语法（变量、条件、循环、函数）
- [ ] 读懂并修改现有的 Shell 脚本
- [ ] 用 `awk`/`sed`/`grep` 处理文本（日志分析必备）
- [ ] 编写实用的运维脚本（备份、日志清理、健康检查）
- [ ] 用 `crontab` 配置定时任务
- [ ] 掌握 Shell 脚本调试技巧（`set -x`、`echo` 断点）
- [ ] 了解 Python 在运维自动化中的使用场景
- [ ] 能写 100 行以上的复杂脚本

**学完这个模块，你就能把重复工作自动化。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| Shell 脚本从入门到实战 | 尚硅谷 | [B站 BV1hW5y1F7J](https://www.bilibili.com/video/BV1hW5y1F7J) | 60万+ | ⭐⭐⭐⭐⭐ |
| Bash 脚本编程 | 黑马程序员 | [B站](https://www.bilibili.com/video/BV1WY41147iP) | 30万+ | ⭐⭐⭐⭐ |
| awk/sed 实战 | IT 老齐 | [B站](https://space.bilibili.com/383016053) | 10万+ | ⭐⭐⭐⭐ |
| Python 自动化运维 | 修炼之路 | [B站 BV1gW41137qf](https://www.bilibili.com/video/BV1gW41137qf) | 50万+ | ⭐⭐⭐⭐ |

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《Shell 脚本学习指南》 | O'Reilly | 入门→进阶 | 中文版翻译不错，Bash 编程必读 |
| 《sed 与 awk（第二版）》 | O'Reilly | 进阶 | 文本处理神器，运维绕不开的两本书 |
| 《Linux 命令行与 Shell 脚本编程大全》 | Richard Blum | 入门 | 厚但全面，适合当工具书 |
| 《Python 自动化运维》 | 刘天斯 | 进阶 | 国内少有的 Python 运维实战书 |
| 《Automate the Boring Stuff with Python》 | Al Sweigart | 入门 | 免费在线，Python 自动化入门最佳 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| GNU Bash 手册（中文） | https://wfr.github.io/bash-guide/ | 最权威的 Bash 参考 |
| 菜鸟教程 — Shell | https://www.runoob.com/linux/linux-shell.html | 中文，入门友好 |
| explainshel.com | https://explainshel.com/ | 交互式 Bash 解释 |
| jaywcjlove/linux-command | https://github.com/jaywcjlove/linux-command | ⭐36k，命令速查 |
| awesome-shell | https://github.com/alebcay/awesome-shell | Shell 工具和资源合集 |

---

## 📝 核心知识点清单

### 第一阶段：Bash 基础语法（1 周）

#### 变量和基础

```bash
# 变量赋值（注意：等号两边不能有空格）
name="vinson"
age=30

# 使用变量
echo $name
echo "我的名字是 ${name}"  # 推荐用 ${} 形式

# 环境变量
echo $HOME
echo $PATH
export MY_VAR="hello"  # 导出为环境变量

# 特殊变量
echo $0   # 脚本名
echo $1   # 第一个参数
echo $@   # 所有参数
echo $#   # 参数个数
echo $?   # 上一条命令的退出码（0=成功）
```

#### 条件判断

```bash
# 文件判断
if [ -f "/etc/passwd" ]; then
    echo "文件存在"
fi

if [ -d "/tmp" ]; then
    echo "/tmp 是目录"
fi

# 字符串判断
if [ "$name" = "vinson" ]; then
    echo "名字匹配"
fi

if [ -z "$name" ]; then
    echo "字符串为空"
fi

# 数字判断
if [ $age -gt 18 ]; then
    echo "已成年"
fi

# -eq 等于  -ne 不等于  -gt 大于  -lt 小于  -ge 大于等于  -le 小于等于

# 逻辑运算
if [ -f "/etc/passwd" ] && [ -r "/etc/passwd" ]; then
    echo "文件存在且可读"
fi
```

#### 循环

```bash
# for 循环
for i in 1 2 3 4 5; do
    echo "数字：$i"
done

# 遍历文件
for file in /var/log/*.log; do
    echo "日志文件：$file"
done

# while 循环
count=0
while [ $count -lt 5 ]; do
    echo "计数：$count"
    count=$((count + 1))
done

# 逐行读取文件
cat /etc/passwd | while read line; do
    echo "行内容：$line"
done

# 更高效的写法
while IFS= read -r line; do
    echo "$line"
done < /etc/passwd
```

#### 函数

```bash
# 定义函数
backup() {
    local src="$1"
    local dest="$2"
    echo "开始备份：$src → $dest"
    cp -r "$src" "$dest"
    if [ $? -eq 0 ]; then
        echo "备份成功"
    else
        echo "备份失败"
        return 1
    fi
}

# 调用函数
backup "/var/log" "/backup/log_$(date +%Y%m%d)"
```

### 第二阶段：文本处理三剑客（1 周）

#### `grep` — 文本搜索

```bash
# 基础搜索
grep "error" /var/log/app.log

# 显示行号
grep -n "error" /var/log/app.log

# 反向匹配（显示不包含的行）
grep -v "info" /var/log/app.log

# 递归搜索目录
grep -r "TODO" /home/user/projects/

# 使用正则
grep -E "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}" access.log  # 提取 IP
```

#### `sed` — 流编辑器

```bash
# 替换（不改变原文件，只输出到 stdout）
sed 's/old/new/' file.txt

# 直接修改文件（-i）
sed -i 's/old/new/g' file.txt

# 删除含 "error" 的行
sed '/error/d' file.txt

# 在匹配行后插入新行
sed '/pattern/a\新的一行' file.txt

# 运维实战：批量修改配置文件
sed -i 's/Port 22/Port 2222/' /etc/ssh/sshd_config
```

#### `awk` — 文本分析（最强）

```bash
# 打印某列
awk '{print $1}' access.log          # 第一列（IP）
awk '{print $1, $7}' access.log     # 第一列和第七列

# 条件过滤
awk '$9 >= 400 {print $1, $7, $9}' access.log  # 状态码 >= 400

# 统计（类似 SQL）
awk '{count[$1]++} END {for (ip in count) print ip, count[ip]}' access.log | sort -k2 -nr | head -10
# 解释：统计每个 IP 的访问次数，按次数倒序，显示前 10

# 实战：分析 Nginx 访问日志，找出访问量最大的 IP
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -10

# 实战：统计每分钟请求数
awk '{print substr($4, 2, 17)}' /var/log/nginx/access.log | uniq -c
```

### 第三阶段：实用运维脚本（1 周）

#### 脚本 1：自动备份 `/var/log`

```bash
#!/bin/bash
# log-backup.sh — 自动备份日志文件

set -e  # 遇到错误立即退出
set -u  # 使用未定义变量时报错

BACKUP_DIR="/backup/logs"
SOURCE_DIR="/var/log"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/log-backup-$DATE.tar.gz"

# 检查备份目录是否存在
if [ ! -d "$BACKUP_DIR" ]; then
    echo "备份目录不存在，创建：$BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
fi

# 打包并压缩
echo "开始备份..."
tar -czf "$BACKUP_FILE" "$SOURCE_DIR" 2>/dev/null

# 检查备份结果
if [ -f "$BACKUP_FILE" ]; then
    BACKUP_SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "✅ 备份成功：$BACKUP_FILE（大小：$BACKUP_SIZE）"
else
    echo "❌ 备份失败"
    exit 1
fi

# 删除 7 天前的备份
find "$BACKUP_DIR" -name "log-backup-*.tar.gz" -mtime +7 -delete
echo "清理完成：7 天前的备份已删除"
```

#### 脚本 2：磁盘空间告警

```bash
#!/bin/bash
# disk-alert.sh — 磁盘使用率超过阈值时发告警

THRESHOLD=80
ALERT_LOG="/var/log/disk-alert.log"

df -h | grep -v "Filesystem" | while read line; do
    usage=$(echo $line | awk '{print $5}' | sed 's/%//')
    partition=$(echo $line | awk '{print $1}')
    mounted=$(echo $line | awk '{print $6}')

    if [ $usage -ge $THRESHOLD ]; then
        MSG="$(date '+%Y-%m-%d %H:%M:%S') [告警] 分区 $partition（$mounted）使用率 ${usage}%"
        echo "$MSG" | tee -a "$ALERT_LOG"
        # 生产环境这里应该发邮件或调用告警 API
        # mail -s "磁盘告警" admin@company.com < "$ALERT_LOG"
    fi
done
```

#### 脚本 3：检查服务器健康检查

```bash
#!/bin/bash
# health-check.sh — 检查服务器基本健康状况

echo "===== 服务器健康检查报告 ====="
echo "检查时间：$(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 1. 检查 CPU 负载
load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | sed 's/,//')
echo "📊 CPU 负载（1分钟）：$load"

# 2. 检查内存使用
mem_total=$(free -m | awk '/Mem:/ {print $2}')
mem_used=$(free -m | awk '/Mem:/ {print $3}')
mem_percent=$((mem_used * 100 / mem_total))
echo "💾 内存使用率：${mem_percent}%（${mem_used}MB / ${mem_total}MB）"

# 3. 检查磁盘使用
echo "💿 磁盘使用率："
df -h | grep -v "Filesystem" | awk '{print "   " $1 " → " $5 "（挂载点：" $6 "）"}'

# 4. 检查关键进程
echo "🔄 关键进程检查："
for proc in nginx mysql redis-server docker; do
    if pgrep -x "$proc" > /dev/null; then
        echo "   ✅ $proc 运行中"
    else
        echo "   ❌ $proc 未运行"
    fi
done

echo ""
echo "===== 检查完成 ====="
```

### 第四阶段：crontab 定时任务（3 天）

```bash
# 查看当前用户的定时任务
crontab -l

# 编辑定时任务
crontab -e

# 格式：分 时 日 月 周 命令
#       ┬  ┬  ┬  ┬  ┬
#       │  │  │  │  │
#       │  │  │  │  └─ 星期几（0-7，0和7都是周日）
#       │  │  │  └──── 月份（1-12）
#       │  │  └─────── 日期（1-31）
#       │  └────────── 小时（0-23）
#       └───────────── 分钟（0-59）

# 示例：
0 3 * * * /scripts/log-backup.sh          # 每天凌晨 3 点执行备份
*/10 * * * * /scripts/health-check.sh   # 每 10 分钟执行一次健康检查
0 0 * * 0 /scripts/cleanup.sh          # 每周日凌晨执行清理
0 9-18 * * 1-5 /scripts/monitor.sh  # 工作日 9 点到 18 点，每小时执行

# 特殊符号：
# *   任意值
# ,   列表分隔（如：1,3,5）
# -   范围（如：1-10）
# /   步长（如：*/10 表示每 10 分钟）
```

### 第五阶段：Python 运维脚本入门（1 周）

为什么学 Python？Shell 适合简单任务，复杂逻辑用 Python 更高效。

```python
#!/usr/bin/env python3
# check-ports.py — 检查服务器端口是否可达

import socket
import sys

def check_port(host, port, timeout=3):
    """检查指定主机的端口是否开放"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"检查失败：{e}")
        return False

if __name__ == "__main__":
    targets = [
        ("127.0.0.1", 22, "SSH"),
        ("127.0.0.1", 80, "HTTP"),
        ("127.0.0.1", 3306, "MySQL"),
    ]
    print("===== 端口检查 =====")
    for host, port, name in targets:
        if check_port(host, port):
            print(f"✅ {name}（{host}:{port}）— 端口开放")
        else:
            print(f"❌ {name}（{host}:{port}）— 端口不可达")
```

---

## 💻 实战命令示例

### 日志分析三板斧

```bash
# 1. 查看实时日志
tail -f /var/log/nginx/access.log

# 2. 统计访问量最大的 IP（前 10）
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -10

# 3. 统计指定时间段的访问量
awk '/21\/Jun\/2024:10/,/21\/Jun\/2024:11/' /var/log/nginx/access.log | wc -l

# 4. 找出 404 最多的的是哪些 URL
awk '$9 == 404 {print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -20

# 5. 统计每小时请求数
awk '{print substr($4, 2, 15)}' /var/log/nginx/access.log | uniq -c
```

### 系统巡检脚本常用命令

```bash
# CPU 核数
nproc

# 内存详情
free -h

# 磁盘 IO 统计
iostat -x 1 5

# 网络连接数统计
netstat -an | awk '/^tcp/ {print $6}' | sort | uniq -c | sort -nr

# 查看某个进程占用的文件句柄数
lsof -n | awk '{print $1}' | sort | uniq -c | sort -nr | head

# 找出占用磁盘空间最大的前 10 个文件/目录
du -ah / | sort -rh | head -10
```

---

## 🧪 实战项目

### 项目 1：自动化日志清理系统

**目标**：写一个脚本，自动清理 30 天前的日志，并保留清理记录。

**要求**：
1. 可配置要清理的目录和保留天数
2. 清理前先打印要删除的文件列表（预览模式）
3. 真正删除时写日志
4. 配置到 crontab，每天凌晨 2 点执行

### 项目 2：服务器巡检报告（自动生成）

**目标**：每天自动生成服务器健康状况报告，发送到运维群。

**步骤**：
1. 用上面写的 `health-check.sh` 为基础
2. 把输出保存到 `/var/report/health-$(date +%Y%m%d).txt`
3. 用 `mail` 或调用企业微信 API 发送报告
4. 配置 crontab 每天早 9 点执行

---

## 🔧 常见故障排查

### 故障 1：Shell 脚本执行报错 `Permission denied`

**原因**：脚本没有执行权限

**解决**：
```bash
chmod +x script.sh
# 或者用 bash 直接执行（不需要 +x）
bash script.sh
```

### 故障 2：脚本在 crontab 中不执行

**常见原因**：
1. 路径问题：crontab 的 `PATH` 很有限，命令要用绝对路径
2. 环境变量：crontab 不会加载 `.bashrc`，需要在脚本开头 `source ~/.bashrc`
3. 输出重定向：crontab 没有终端，输出默认发邮件（通常没配置）

**解决**：
```bash
# 在脚本开头加上：
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# 或者命令用绝对路径：/usr/bin/awk 而不是 awk
```

### 故障 3：awk 处理大文件很慢

**优化技巧**：
```bash
# 不好的写法（每行都调用外部命令）
awk '{system("date -d @" $1)}' file.log

# 好的写法（awk 内置函数）
awk '{print strftime("%Y-%m-%d", $1)}' file.log
```

---

## 💼 面试高频题

1. **`$@` 和 `$*` 的区别？**
   - `$@`：每个参数独立引用（推荐），`"$@"` 保留参数中的空格
   - `$*`：所有参数合并为一个字符串

2. **如何用 `awk` 统计日志中 500 错误的数量？**
   ```bash
   awk '$9 == 500 {count++} END {print count}' access.log
   ```

3. **Shell 脚本中如何捕获 Ctrl+C 信号？**
   ```bash
   trap "echo '收到中断信号，清理临时文件...'; exit 1" INT TERM
   ```

4. **如何写一个防止重复运行的脚本？**
   ```bash
   LOCK_FILE="/tmp/my-script.lock"
   if [ -f "$LOCK_FILE" ]; then
       echo "脚本正在运行中，退出"
       exit 1
   fi
   touch "$LOCK_FILE"
   trap "rm -f $LOCK_FILE" EXIT  # 脚本退出时自动删除锁文件
   ```

---

## 📈 进阶学习路径

- **高级 Bash**：学数组、关联数组、正则表达式、进程替换
- **Python 运维**：学 `paramiko`（SSH）、`psutil`（系统监控）、`requests`（API 调用）
- **配置管理**：学 Ansible（基于 YAML 和 Python，不需要 Agent）
- **Go 运维工具开发**：学 Go，可以写高性能的运维工具（如 `kubectl`、`terraform` 都是 Go 写的）

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 02 计算机网络](../02_Networking/)
- [CN 04 Docker 容器](../04_Container_Docker/)
- [CN 11 DevOps 实践](../11_DevOps_Practice/)
- [实时发现：Shell/自动化相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · 脚本写得好，下班回家早</sub>
</p>
