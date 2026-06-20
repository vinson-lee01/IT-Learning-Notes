# 09 · 数据库管理

> 数据是企业的生命线。懂数据库的运维，比只懂系统的运维值钱得多。
> 这个模块以 MySQL 为主（国内用得最多），兼顾 Redis 和其他数据库。

---

## 🎯 学习目标

完成本模块后，你应该能够：

- [ ] 安装和初始化 MySQL 8.0
- [ ] 熟练使用 MySQL 基础命令（DDL/DML/DQL）
- [ ] 配置 MySQL 主从复制（一主两从）
- [ ] 会做 MySQL 备份和恢复（mysqldump / xtrabackup）
- [ ] 掌握 MySQL 性能调优基础（索引、慢查询分析）
- [ ] 安装和配置 Redis，理解内存淘汰策略
- [ ] 配置 Redis 主从 + Sentinel 高可用
- [ ] 了解 MongoDB 基础操作和副本集
- [ ] 能排查数据库常见故障

**学完这个模块，你能胜任「数据库运维」专职方向。**

---

## 📺 推荐视频教程

| 教程 | 讲师 | 链接 | 播放量 | 推荐度 |
|------|------|------|--------|---------|
| MySQL 基础到精通 | 尚硅谷 | [B站 BV1xW5y1M7QC](https://www.bilibili.com/video/BV1xW5y1M7QC) | 80万+ | ⭐⭐⭐⭐⭐ |
| MySQL 高级（主从/优化） | 黑马程序员 | [B站](https://www.bilibili.com/video/BV1xJ411w7cx) | 40万+ | ⭐⭐⭐⭐ |
| Redis 从入门到精通 | 狂神说 | [B站 BV1FZ4y1D7fw](https://www.bilibili.com/video/BV1FZ4y1D7fw) | 100万+ | ⭐⭐⭐⭐⭐ |
| MongoDB 实战 | IT 老齐 | [B站](https://space.bilibili.com/383016053) | 15万+ | ⭐⭐⭐⭐ |
| MySQL 性能调优 | 极客时间 | [B站](https://www.bilibili.com/video/BV1YJ411y7M7) | 20万+ | ⭐⭐⭐⭐ |

---

## 📖 推荐书籍

| 书名 | 作者 | 适合阶段 | 一句话评价 |
|------|------|---------|-------------|
| 《高性能 MySQL（第3版）》 | Baron Schwartz 等 | 高级 | MySQL 调优圣经，必读 |
| 《MySQL 必知必会》 | Ben Forta | 入门 | 薄，但核心概念讲得清楚 |
| 《Redis 设计与实现》 | 黄健宏 | 高级 | 最好 Redis 书，原理 + 源码 |
| 《Redis 实战》 | O'Reilly | 进阶 | Redis 应用场景，有中文版 |
| 《MongoDB 权威指南》 | O'Reilly | 进阶 | MongoDB 官方推荐 |

---

## 🌐 在线参考资源

| 资源 | 链接 | 特点 |
|------|------|------|
| MySQL 8.0 官方文档（中文） | https://dev.mysql.com/doc/ | 最权威 |
| MySQL 性能调优博客 | https://www.jianshu.com/p/9b9f9e8b9a0a | 实战案例多 |
| Redis 官方文档（中文） | https://redis.io/docs/ | 官方文档很清楚 |
| MongoDB 官方文档（中文） | https://www.mongodb.org.cn/ | 中文社区翻译 |
| percona/percona-server | https://github.com/percona/percona-server | ⭐6k，MySQL 增强版 |

---

## 📝 核心知识点清单

### 第一阶段：MySQL 安装和基础（1 周）

#### 安装 MySQL 8.0（CentOS 7/8）

```bash
# 1. 卸载系统自带的 MariaDB
yum remove -y mariadb*

# 2. 添加 MySQL 官方仓库
wget https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm
rpm -ivh mysql80-community-release-el7-5.noarch.rpm

# 3. 安装 MySQL
yum install -y mysql-community-server

# 4. 启动并设置开机自启
systemctl enable mysqld
systemctl start mysqld

# 5. 获取初始密码
grep 'temporary password' /var/log/mysqld.log

# 6. 安全初始化
mysql_secure_installation
# 按提示操作：改密码、删匿名用户、禁 root 远程登录

# 7. 登录验证
mysql -uroot -p
```

#### MySQL 基础命令

```sql
-- 查看所有数据库
SHOW DATABASES;

-- 创建数据库
CREATE DATABASE my_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 使用数据库
USE my_app;

-- 创建表
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入数据
INSERT INTO users (username, password) VALUES ('admin', MD5('password123'));

-- 查询数据
SELECT * FROM users WHERE id = 1;

-- 创建索引（调优关键！）
CREATE INDEX idx_username ON users(username);
-- 或者建表时加
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    amount DECIMAL(10,2),
    INDEX idx_user_id (user_id)   -- 建表时创建索引
) ENGINE=InnoDB;
```

### 第二阶段：MySQL 主从复制（1 周）

#### 为什么需要主从？

- **读写分离**：主库写，从库读，提升性能
- **数据备份**：从库是主库的实时备份
- **高可用**：主库挂了，从库顶上

#### 配置主从复制

```bash
# ========== 主库配置（192.168.56.101）==========

# 1. 修改 /etc/my.cnf
cat >> /etc/my.cnf << EOF
[mysqld]
server-id = 1
log-bin = mysql-bin
binlog_format = ROW
expire_logs_days = 7
max_binlog_size = 256M
EOF

# 2. 重启 MySQL
systemctl restart mysqld

# 3. 创建复制用户
mysql -uroot -p
CREATE USER 'repl'@'192.168.56.%' IDENTIFIED BY 'Repl@123456';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'192.168.56.%';
FLUSH PRIVILEGES;

# 4. 查看主库状态（记录 File 和 Position）
SHOW MASTER STATUS;
-- 输出示例：
-- File: mysql-bin.000003
-- Position: 856


# ========== 从库配置（192.168.56.102）==========

# 1. 修改 /etc/my.cnf
cat >> /etc/my.cnf << EOF
[mysqld]
server-id = 2
relay-log = relay-bin
read-only = 1
EOF

# 2. 重启 MySQL
systemctl restart mysqld

# 3. 配置复制到主库
mysql -uroot -p
CHANGE MASTER TO
  MASTER_HOST='192.168.56.101',
  MASTER_USER='repl',
  MASTER_PASSWORD='Repl@123456',
  MASTER_LOG_FILE='mysql-bin.000003',
  MASTER_LOG_POS=856;

# 4. 启动复制
START SLAVE;

# 5. 查看复制状态（关键！）
SHOW SLAVE STATUS\G
-- 看到 Slave_IO_Running: Yes
--      Slave_SQL_Running: Yes
-- 才算成功！
```

#### 验证主从同步

```sql
-- 在主库插入数据
USE my_app;
INSERT INTO users (username, password) VALUES ('test', '123456');

-- 在从库查询（应该能看到刚插入的数据）
SELECT * FROM my_app.users;
```

### 第三阶段：MySQL 备份和恢复（1 周）

#### 逻辑备份（mysqldump）

```bash
# 备份单个数据库
mysqldump -uroot -p my_app > my_app_$(date +%Y%m%d).sql

# 备份所有数据库
mysqldump -uroot -p --all-databases > all_db_$(date +%Y%m%d).sql

# 备份时锁表（MyISAM 需要，InnoDB 不需要）
mysqldump -uroot -p --single-transaction my_app > my_app.sql
# --single-transaction：对 InnoDB 做一致性备份，不锁表

# 压缩备份
mysqldump -uroot -p my_app | gzip > my_app_$(date +%Y%m%d).sql.gz

# 恢复备份
mysql -uroot -p my_app < my_app_20240620.sql
# 或者进入 mysql 后：source /backup/my_app_20240620.sql
```

#### 物理备份（xtrabackup，生产推荐）

```bash
# 安装 xtrabackup
yum install -y https://repo.percona.com/yum/percona-release-latest.noarch.rpm
yum install -y percona-xtrabackup-80

# 全量备份
xtrabackup --backup --target-dir=/backup/full-20240620 --user=root --password=xxx

# 准备备份（让数据一致）
xtrabackup --prepare --target-dir=/backup/full-20240620

# 恢复（需要先停 MySQL，清空数据目录）
systemctl stop mysqld
rm -rf /var/lib/mysql/*
xtrabackup --move-back --target-dir=/backup/full-20240620
chown -R mysql:mysql /var/lib/mysql
systemctl start mysqld
```

#### 自动化备份脚本

```bash
#!/bin/bash
# mysql-backup.sh — MySQL 自动备份脚本

BACKUP_DIR="/backup/mysql"
DATE=$(date +%Y%m%d_%H%M%S)
MYSQL_USER="backup_user"
MYSQL_PASS="Backup@123"
RETENTION_DAYS=7

# 创建备份目录
mkdir -p "$BACKUP_DIR/$DATE"

# 全量备份
echo "[$(date)] 开始备份..."
mysqldump -u$MYSQL_USER -p$MYSQL_PASS \
  --single-transaction \
  --routines --triggers --events \
  --all-databases | gzip > "$BACKUP_DIR/$DATE/all-db.sql.gz"

if [ $? -eq 0 ]; then
    echo "[$(date)] ✅ 备份成功：$BACKUP_DIR/$DATE/all-db.sql.gz"
    # 删除 7 天前的备份
    find "$BACKUP_DIR" -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete
else
    echo "[$(date)] ❌ 备份失败！"
    exit 1
fi
```

### 第四阶段：MySQL 性能调优（1-2 周）

#### 慢查询分析

```sql
-- 开启慢查询日志
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;  -- 超过 2 秒的记录
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';

-- 分析慢查询（在命令行）
# mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
# -s t：按查询时间排序
# -t 10：显示前 10 条
```

#### 索引优化

```sql
-- 查看表的索引
SHOW INDEX FROM users;

-- 用 EXPLAIN 分析查询（调优最重要的命令！）
EXPLAIN SELECT * FROM users WHERE username = 'admin';
-- 看 key 列：实际用了哪个索引
-- 看 rows 列：扫描了多少行（越少越好）
-- 看 type 列：ALL（全表扫描，最差）→ index → range → ref → eq_ref → const（最好）

-- 创建复合索引（注意顺序！）
CREATE INDEX idx_user_status ON orders(user_id, status);
-- 生效的查询：WHERE user_id = 1 AND status = 'paid'
-- 不生效的查询：WHERE status = 'paid'（不符合最左前缀）

-- 删除冗余索引
-- 用 pt-duplicate-key-checker 工具检查
```

#### 常用调优参数（/etc/my.cnf）

```ini
[mysqld]
# 内存分配（服务器 4GB 内存的参考配置）
innodb_buffer_pool_size = 2G    # 最重要！InnoDB 缓存池，建议设为物理内存的 50-70%
max_connections = 500                  # 最大连接数
query_cache_size = 0                  # MySQL 8.0 已移除查询缓存，设为 0

# 日志
slow_query_log = 1
long_query_time = 2
log-error = /var/log/mysql/error.log

# InnoDB 设置
innodb_flush_log_at_trx_commit = 1  # 事务提交时刷盘（最安全）
innodb_log_file_size = 512M              #  redo log 大小
```

### 第五阶段：Redis 实战（1 周）

#### 安装和配置

```bash
# 安装 Redis
yum install -y epel-release
yum install -y redis

# 修改配置 /etc/redis.conf
cat >> /etc/redis.conf << EOF
bind 0.0.0.0                  # 允许远程访问（生产要配密码）
requirepass Redis@123456          # 设置密码
maxmemory 1gb                   # 最大内存
maxmemory-policy allkeys-lru     # 内存满时淘汰策略
appendonly yes                   # 开启 AOF 持久化
EOF

# 启动
systemctl enable redis
systemctl start redis

# 验证
redis-cli -a Redis@123456 ping
# 返回 PONG 说明正常
```

#### Redis 常用命令

```bash
# 字符串（最常用，缓存场景）
SET user:1 "{'name':'vinson','age':30}"
GET user:1
EXPIRE user:1 3600         # 1 小时后过期
SETEX user:1 3600 "..."    # 等价于 SET + EXPIRE

# 哈希（存储对象）
HSET user:1 name "vinson" age 30
HGET user:1 name
HGETALL user:1

# 列表（消息队列）
LPUSH queue "task1"
RPUSH queue "task2"
RPOP queue                    # 取出任务（阻塞版本：BRPOP）

# 集合（去重、共同好友）
SADD tags "linux" "docker" "k8s"
SMEMBERS tags
SINTER tags1 tags2           # 交集

# 有序集合（排行榜）
ZADD leaderboard 100 "user1"
ZADD leaderboard 95 "user2"
ZREVRANGE leaderboard 0 9 WITHSCORES  # 前 10 名
```

#### Redis 主从 + Sentinel（高可用）

```bash
# ========== 主库（6379）==========
# 不需要特殊配置，正常运行即可

# ========== 从库（6380）==========
# 修改 /etc/redis-slave.conf
cat > /etc/redis-slave.conf << EOF
bind 0.0.0.0
port 6380
requirepass Redis@123456
masterauth Redis@123456
replicaof 127.0.0.1 6379     # 指定主库
EOF
redis-server /etc/redis-slave.conf

# ========== Sentinel（26379）==========
# 修改 /etc/redis-sentinel.conf
cat > /etc/redis-sentinel.conf << EOF
bind 0.0.0.0
port 26379
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel auth-pass mymaster Redis@123456
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 10000
EOF
redis-sentinel /etc/redis-sentinel.conf
```

---

## 🧪 实战项目

### 项目 1：部署 MySQL 主从 + 配置备份告警

**目标**：搭建一套生产可用的 MySQL 高可用方案。

**步骤**：
1. 准备 3 台服务器（1 主 2 从）
2. 安装 MySQL 8.0，配置主从复制
3. 部署 Prometheus + Grafana，监控 MySQL 状态
4. 编写备份脚本，crontab 每天凌晨 3 点执行
5. 备份失败时发邮件告警

### 项目 2：用 Redis 做 Web 应用缓存

**目标**：给 WordPress 加 Redis 缓存，提升响应速度。

**步骤**：
1. 安装 Redis
2. 安装 WordPress Redis 插件（Redis Object Cache）
3. 配置插件连接到 Redis
4. 用 `ab` 压测工具对比缓存前后的 QPS

---

## 🔧 常见故障排查

### 故障 1：MySQL 主从复制延迟大

**排查步骤**：
```sql
-- 在从库执行，查看延迟秒数
SHOW SLAVE STATUS\G
-- 看 Seconds_Behind_Master 字段

-- 常见原因：
-- 1. 主库写入量大，从库单线程复制跟不上
--   解决：启用并行复制（MySQL 5.7+）
--   在从库 my.cnf 加：
--   slave_parallel_workers = 8
--   slave_parallel_type = LOGICAL_CLOCK

-- 2. 从库硬件差
--   解决：提升从库配置，或用中间件（如 ProxySQL）做读写分离

-- 3. 大事务导致延迟
--   解决：避免一次性 DELETE 大量数据，分批删除
```

### 故障 2：Redis 内存满了

**排查**：
```bash
redis-cli -a Redis@123456 INFO memory
# 看 used_memory_human 和 maxmemory

# 解决 1：扩大 maxmemory（如果服务器还有内存）
# 解决 2：检查是否有大 Key
redis-cli -a Redis@123456 --bigkeys

# 解决 3：检查内存淘汰策略是否合适
redis-cli -a Redis@123456 CONFIG GET maxmemory-policy
```

### 故障 3：MySQL 连接数爆满

**排查**：
```sql
-- 查看当前连接数
SHOW STATUS LIKE 'Threads_connected';

-- 查看所有连接（看看是谁在连）
SHOW PROCESSLIST;

-- 杀掉空闲连接
KILL <connection_id>;

-- 永久解决：调大 max_connections，并检查应用是否用了连接池
```

---

## 💼 面试高频题

1. **MySQL 的 InnoDB 和 MyISAM 有什么区别？**
   - InnoDB：支持事务、行锁、外键，崩溃后安全（有 redo log）
   - MyISAM：不支持事务、表锁、崩溃后可能丢数据，但读性能好
   - **现在默认存储引擎是 InnoDB，MyISAM 基本不用了**

2. **什么是 MVCC？**
   - 多版本并发控制，InnoDB 实现读写不阻塞的机制
   - 每行记录有隐藏的 trx_id 和 roll_pointer，读操作读快照

3. **Redis 的持久化方式有哪些？**
   - RDB：定时快照，恢复快但会丢数据
   - AOF：记录每条写命令，安全但文件大
   - 推荐：同时开启（Redis 4.0+ 支持混合持久化）

4. **什么情况下数据库索引会失效？**
   - 对索引列做函数操作（`WHERE MD5(name) = ...`）
   - 隐式类型转换（`WHERE phone = 13800138000`，phone 是 VARCHAR）
   - 最左前缀原则不匹配
   - `LIKE '%keyword%'`（左模糊匹配）

---

## 📈 进阶学习路径

- **MySQL 深入**：学事务隔离级别、锁机制（Next-Key Lock）、执行计划深度优化
- **分布式数据库**：学 TiDB（国产 NewSQL，兼容 MySQL 协议）
- **Redis 深入**：学内存淘汰策略、哨兵机制原理、Redis Cluster
- **数据库中间件**：学 ProxySQL、ShardingSphere（分库分表）

---

## 🔗 相关资源

- [← 返回中文版首页](../README.md)
- [CN 05 Kubernetes](../05_Kubernetes/)
- [CN 08 监控告警](../08_Monitoring/)
- [实时发现：数据库相关热门仓库](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · 数据不丢，比什么都重要</sub>
</p>
