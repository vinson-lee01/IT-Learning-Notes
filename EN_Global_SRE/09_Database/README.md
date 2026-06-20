# 09 · Database Administration

> Data is the business. MySQL, PostgreSQL, Redis — every ops engineer must know how to run, backup, and recover databases.

---

## 🎯 Learning Objectives

- [ ] Deploy and tune MySQL/PostgreSQL for production
- [ ] Implement backup strategies (full + incremental)
- [ ] Set up replication for high availability
- [ ] Manage Redis as a caching layer

---

## 🌐 Key Resources

| Resource | Link | Notes |
|----------|------|-------|
| MySQL Docs | https://dev.mysql.com/doc/refman/8.0/en | Official |
| PostgreSQL Docs | https://www.postgresql.org/docs | Best DB docs ever |
| Redis Docs | https://redis.io/docs | Official |
| Percona Toolkit | https://www.percona.com/software | Advanced MySQL tools |
| Use The Index, Luke | https://use-the-index-luke.com | SQL indexing masterclass |

---

## 📝 Key Topics

### MySQL
- InnoDB architecture (buffer pool, redo/undo logs)
- Backup: `mysqldump` vs `xtrabackup` vs binary logs
- Replication: async, semi-sync, GTID
- Slow query analysis (`EXPLAIN`, `pt-query-digest`)
- Connection pooling (ProxySQL)

### PostgreSQL
- MVCC and VACUUM
- Streaming replication
- `pg_dump` / `pg_basebackup` / WAL archiving
- Extensions: `pg_stat_statements`, PostGIS

### Redis
- Data structures and use cases
- Persistence: RDB snapshots vs AOF
- Sentinel for HA, Cluster for sharding
- Eviction policies (`allkeys-lru`, `volatile-ttl`)

---

[← Back to English Home](../README.md)
