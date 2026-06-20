# 09 · Database Administration

> Data is the most valuable asset of any company. As an ops engineer, database reliability, backup, and performance are your responsibility.
> This module covers MySQL/PostgreSQL — the two most common Ops-managed databases.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- [ ] Install and configure MySQL/PostgreSQL
- [ ] Understand storage engines (InnoDB vs MyISAM)
- [ ] Set up master-slave replication
- [ ] Configure primary-primary (Galera) cluster
- [ ] Perform backup and restore (mysqldump, xtrabackup, pg_dump)
- [ ] Tune database performance: indexes, query optimization, buffer pool
- [ ] Monitor database health (slow query log, Prometheus mysqld_exporter)
- [ ] Handle common failures: replication lag, deadlock, disk full
- [ ] Implement connection pooling (HikariCP, PgBouncer)
- [ ] Secure the database: least privilege, network isolation, encryption at rest

---

## 📺 Recommended Video Courses

| Course | Platform | Duration | Rating |
|--------|----------|----------|--------|
| **MySQL for DevOps** | Udemy | 6h | ⭐⭐⭐⭐ |
| **PostgreSQL Administration** | LinkedIn Learning | 4h | ⭐⭐⭐⭐ |
| **Database Performance Tuning** | Conferences (YouTube) | Various | ⭐⭐⭐⭐⭐ |

### Chinese

| 教程 | 讲师 | 链接 | 推荐度 |
|------|------|------|---------|
| MySQL 高级实战 | 尚硅谷 | [B站](https://www.bilibili.com/) | ⭐⭐⭐⭐⭐ |
| PostgreSQL 从入门到精通 | 黑马程序员 | [B站](https://www.bilibili.com/) | ⭐⭐⭐⭐ |

---

## 📖 Recommended Books

| Book | Author | For | Comment |
|------|--------|-----|---------|
| **High Performance MySQL (4th ed)** | Baron Schwartz | Advanced | The MySQL bible. Must-read. |
| **PostgreSQL: Up and Running (3rd ed)** | Regina Obe | Intermediate | Best PostgreSQL intro. |
| **MySQL Troubleshooting** | O'Reilly | Advanced | Real-world failure cases. |
| **The Art of PostgreSQL** | Dimitri Fontaine | Advanced | Deep dive into PG internals. |
| **Designing Data-Intensive Applications** | Martin Kleppmann | All levels | Not ops-specific but every senior should read. |

---

## 🌐 Online Resources

| Resource | Link | Features |
|----------|------|----------|
| **MySQL 8.0 Reference Manual** | https://dev.mysql.com/doc/refman/8.0/en/ | Official, comprehensive |
| **PostgreSQL Documentation** | https://www.postgresql.org/docs/ | Excellent official docs |
| **Percona Blog** | https://www.percona.com/blog | High-performance MySQL/PG tips |
| **MySQL Explain Analyzer** | https://mariadb.com/kb/en/explain-analyze/ | Understand query execution plans |
| **Awesome MySQL** | https://github.com/shaluwali/awesome-mysql | Curated tools list |
| **Awesome PostgreSQL** | https://github.com/dhamaniasad/awesome-postgres | Curated PG tools |

---

## 📝 Core Knowledge Checklist

### Phase 1: Installation & Basic Administration (1 week)

#### MySQL installation (the right way)
```bash
# Use official repo (not OS package — it's often outdated)
wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb
sudo apt update
sudo apt install mysql-server-8.0
sudo mysql_secure_installation
```

Key `my.cnf` settings to check:
```ini
[mysqld]
datadir=/var/lib/mysql
socket=/var/run/mysqld/mysqld.sock
log-error=/var/log/mysqld.log

# InnoDB settings (most important)
innodb_buffer_pool_size = 4G  # ~70-80% of RAM for dedicated DB server
innodb_log_file_size = 512M
innodb_flush_log_at_trx_commit = 2  # 1 = ACID, 2 = performance

# Connection settings
max_connections = 500
wait_timeout = 300
interactive_timeout = 300

# Logging
slow_query_log = 1
long_query_time = 2
log_queries_not_using_indexes = 1
```

#### PostgreSQL installation
```bash
# Use official repo
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt install postgresql-16
```

Key `postgresql.conf` settings:
```ini
shared_buffers = 4GB              # ~25% of RAM
effective_cache_size = 12GB        # ~75% of RAM
maintenance_work_mem = 1GB
wal_buffers = 16MB
checkpoint_timeout = 15min
```

### Phase 2: Backup & Restore (1 week)

#### MySQL backup strategies

| Method | Speed | Lock | Granularity | Use case |
|--------|-------|------|------------|----------|
| `mysqldump` | Slow | Yes (InnoDB=no) | Logical | Small DBs (<50GB) |
| `xtrabackup` | Fast | No | Physical | Large DBs, hot backup |
| Replication | N/A | No | N/A | DR, read scaling |

**mysqldump (correct way)**:
```bash
# Full backup
mysqldump -u root -p --single-transaction --routines --triggers --all-databases > backup_$(date +%F).sql

# Restore
mysql -u root -p < backup_2026-01-15.sql

# Single database
mysqldump -u root -p --single-transaction myapp > myapp.sql
```

**xtrabackup (for large databases)**:
```bash
# Install percona-xtrabackup
xtrabackup --backup --target-dir=/data/backups/full

# Prepare (make it consistent)
xtrabackup --prepare --target-dir=/data/backups/full

# Restore
systemctl stop mysqld
rm -rf /var/lib/mysql/*
xtrabackup --move-back --target-dir=/data/backups/full
chown -R mysql:mysql /var/lib/mysql
systemctl start mysqld
```

#### PostgreSQL backup
```bash
# Logical backup
pg_dump -U postgres myapp > myapp_$(date +%F).sql
pg_dumpall -U postgres > all_databases_$(date +%F).sql

# Physical backup (WAL archiving)
# Requires archive_mode = on in postgresql.conf
pg_basebackup -D /data/backups/base -Ft -Xs -P

# Restore
systemctl stop postgresql
rm -rf /var/lib/postgresql/16/main/*
tar -xvf /data/backups/base/base.tar -C /var/lib/postgresql/16/main/
systemctl start postgresql
```

### Phase 3: Replication & High Availability (2 weeks)

#### MySQL master-slave replication
```sql
-- On master
CREATE USER 'repl'@'%' IDENTIFIED BY 'secure_password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
FLUSH PRIVILEGES;
SHOW MASTER STATUS;  -- Note File and Position

-- On slave
CHANGE MASTER TO
  MASTER_HOST='master_host',
  MASTER_USER='repl',
  MASTER_PASSWORD='secure_password',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=154;
START SLAVE;
SHOW SLAVE STATUS\G
```

**Check replication health**:
```sql
SHOW SLAVE STATUS\G
-- Look for:
--   Slave_IO_Running: Yes
--   Slave_SQL_Running: Yes
--   Seconds_Behind_Master: 0  (or small number)
```

**Common replication issues**:
| Problem | Cause | Fix |
|----------|-------|-----|
| `Seconds_Behind_Master` growing | Slow SQL on slave | Optimize queries, upgrade slave hardware |
| Duplicate key error | Data drift | Rebuild slave from fresh backup |
| `Got fatal error 1236` | Binlog purged on master | Rebuild slave from fresh backup |

#### MySQL MGR (MySQL Group Replication) / Galera Cluster
- Multi-primary or single-primary
- Synchronous replication (certification-based)
- Automatic failover
- Use: Percona XtraDB Cluster (PXC) or MySQL InnoDB Cluster

### Phase 4: Performance Tuning (2 weeks)

#### Identify slow queries
```sql
-- Enable slow query log
SET GLOBAL slow_query_log = 1;
SET GLOBAL long_query_time = 2;

-- Analyze slow queries
SELECT * FROM mysql.slow_log ORDER BY start_time DESC LIMIT 10;

-- Use EXPLAIN to understand query execution
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
-- Look for: type=ALL (full table scan), rows=large number
```

#### Index strategy
```sql
-- Add index (the most impactful optimization)
ALTER TABLE users ADD INDEX idx_email (email);

-- Composite index (order matters!)
ALTER TABLE orders ADD INDEX idx_user_status (user_id, status);

-- Check index usage
SELECT * FROM sys.schema_unused_indexes;  -- MySQL 8.0
```

#### Key performance metrics to monitor
| Metric | Good | Bad | What to do |
|---------|------|-----|-------------|
| Buffer pool hit rate | > 99% | < 95% | Increase `innodb_buffer_pool_size` |
| Query cache hit rate | N/A (removed in 8.0) | - | Use app-level cache (Redis) |
| Replication lag | < 1s | > 10s | Optimize slow queries, upgrade slave |
| Connection usage | < 70% | > 85% | Increase `max_connections` |
| Disk IOPS | < provisioned | Saturated | Upgrade storage, tune `innodb_flush_log_at_trx_commit` |

### Phase 5: Monitoring (1 week)

#### Prometheus + Grafana for MySQL
```bash
# Install mysqld_exporter
wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.15.1/mysqld_exporter-0.15.1.linux-amd64.tar.gz
tar -xzf mysqld_exporter-*.tar.gz
cd mysqld_exporter

# Create exporter user in MySQL
mysql -u root -p -e "CREATE USER 'exporter'@'localhost' IDENTIFIED BY 'password'; GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'localhost';"

# Run exporter
export DATA_SOURCE_NAME="exporter:password@(localhost:3306)/"
./mysqld_exporter
```

Import MySQL dashboard in Grafana (ID: `7362`).

---

## 🔬 Hands-on Projects

| Project | Difficulty | What you'll learn |
|---------|-------------|-------------------|
| **Set up master-slave replication** | ⭐⭐ | Binlog, replication lag debugging |
| **Automated backup with cron + S3** | ⭐⭐⭐ | `xtrabackup`, `aws s3 cp`, recovery testing |
| **Tune a slow query from 10s to 0.1s** | ⭐⭐⭐ | `EXPLAIN`, index design, query rewriting |
| **Set up PostgreSQL streaming replication** | ⭐⭐⭐ | WAL archiving, `pg_basebackup` |
| **MySQL MGR / PXC cluster** | ⭐⭐⭐⭐ | Multi-primary, conflict detection |
| **Database connection pool tuning** | ⭐⭐⭐ | HikariCP config, `SHOW PROCESSLIST` |

---

## ⚠️ Common Pitfalls

| Pitfall | Why it happens | How to avoid |
|---------|----------------|---------------|
| No backup tested | "We have backups" but never tested restore | **Test restore monthly**. It's not backed up if you can't restore it. |
| Binary log purged too early | `expire_logs_days` too short | Set to at least 7 days; use `xtrabackup` for longer retention |
| No monitoring | "Database is fine" until it's not | Set up Prometheus + Grafana **before** you need it |
| Over-indexing | Adding indexes for every query | Each index slows down `INSERT`/`UPDATE`. Only index what's needed. |
| Ignoring connection limits | App connection leak | Set `wait_timeout`, use connection pool (HikariCP) |
| Mixing storage engines | MyISAM tables in InnoDB database | MyISAM doesn't support transactions. Use InnoDB only. |

---

## ✅ Self-Check: Can you...

- [ ] Restore a 50GB MySQL database from `xtrabackup` in under 30 minutes?
- [ ] Explain why `SELECT * FROM users WHERE email = 'x'` is slow even with an index on `email`?
- [ ] Set up a read replica and route read-only queries to it?
- [ ] Troubleshoot `Seconds_Behind_Master` growing from 0 to 300?
- [ ] Configure PostgreSQL WAL archiving for point-in-time recovery?

> 💡 **Next step**: After this module, move on to **10 · Cloud Native & IaC** to learn how to manage infrastructure as code.
