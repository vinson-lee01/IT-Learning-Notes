# 01 · Linux Fundamentals

> **Why this matters**: Linux runs the internet. Every major cloud provider, every Kubernetes node, every container — they all run on Linux. If you master Linux, you understand how the cloud actually works under the hood. I've seen too many engineers who can deploy to EKS but can't debug why a node is thrashing — don't be that person. This module gives you the deep, practical Linux knowledge that separates junior ops from senior SRE.

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- [ ] Install and harden a Linux server (RHEL/Rocky/Ubuntu) for production use
- [ ] Navigate and explain the entire Linux filesystem hierarchy (FHS) from `/bin` to `/var`
- [ ] Manage users, groups, permissions, ACLs, and sudoers with confidence
- [ ]Master systemd: units, targets, timers, journald, and custom service files
- [ ] Debug any performance problem using the USE Method (Utilization, Saturation, Errors)
- [ ] Use `strace`, `perf`, `bpftrace`, and `eBPF` tools to trace system calls and kernel events
- [ ] Capture and analyze network traffic with `tcpdump`, `tshark`, and `ss`
- [ ] Tune kernel parameters via `sysctl`, `/proc`, and `/sys` for production workloads
- [ ] Diagnose and resolve OOM situations, memory leaks, and CPU saturation
- [ ] Master text processing pipelines: `grep` → `sed` → `awk` → `jq`
- [ ] Write robust Bash scripts with proper error handling, traps, and idempotency
- [ ] Understand the Linux boot process: BIOS/UEFI → GRUB → initramfs → systemd
- [ ] Manage storage: partitioning, LVM, RAID, filesystem tuning (`ext4`, `xfs`, `btrfs`)
- [ ] Configure and troubleshoot SELinux/AppArmor in enforcing mode

---

## 📺 Recommended Video Courses

| Course | Creator / Platform | Views / Info | Difficulty |
|--------|---------------------|--------------|------------|
| **Linux Administration Bootcamp** | Jason Cannon (Udemy) | 100k+ students | ⭐ Beginner |
| **LFCS (Linux Foundation Certified Sysadmin)** | Andrew Mallett (Udemy) | 40k+ students | ⭐⭐ Intermediate |
| **Red Hat Enterprise Linux Technical Overview** | Red Hat (YouTube) | 200k+ views | ⭐ Beginner |
| **Brendan Gregg — Linux Performance Tools** | Brendan Gregg (YouTube) | 300k+ views | ⭐⭐⭐ Advanced |
| **How Linux Works (Talk Python)** | Brian Ward (YouTube) | 50k+ views | ⭐⭐ Intermediate |
| **Advanced Linux Debugging with eBPF** | Liz Rice (YouTube) | 80k+ views | ⭐⭐⭐ Advanced |
| **Linux Troubleshooting Masterclass** | Sander van Vugt (O'Reilly) | 15k+ students | ⭐⭐ Intermediate |
| **TCP/IP Deep Dive** | David Bombal (YouTube) | 500k+ views | ⭐⭐ Intermediate |

---

## 📖 Recommended Books

| Title | Author | Rating | One-line Recommendation |
|-------|--------|--------|--------------------------|
| **Linux Performance (2nd Ed.)** | Brendan Gregg | ★★★★★ | The definitive guide to Linux performance analysis — every SRE should own this |
| **UNIX and Linux System Administration Handbook (5th Ed.)** | Evi Nemeth et al. | ★★★★★ | The sysadmin encyclopedia — covers everything from boot to security |
| **How Linux Works (3rd Ed.)** | Brian Ward | ★★★★☆ | Best "mental model" book — explains what happens under the hood |
| **The Linux Command Line (2nd Ed.)** | William Shotts | ★★★★☆ | The best CLI introduction — free online from the author |
| **Linux Kernel Development (3rd Ed.)** | Robert Love | ★★★★☆ | Understand the kernel itself — useful when tuning `sysctl` |
| **Advanced Programming in the UNIX Environment (3rd Ed.)** | W. Richard Stevens | ★★★★★ | The bible of UNIX programming — essential for writing robust scripts |
| **SELinux Cookbook** | Sven Vermeulen | ★★★★☆ | Demystifies SELinux — includes real policy writing examples |

---

## 🌐 Online Resources

| Resource | Link | Stars / Notes |
|----------|------|---------------|
| **linux-command** | https://github.com/jaywcjlove/linux-command | ⭐36k — Chinese/English command cheatsheet |
| **linux-tutorial** | https://github.com/dunwu/linux-tutorial | ⭐6.8k — Comprehensive tutorial repo |
| **RHEL System Admin Docs** | https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux | Official enterprise-grade docs |
| **Linux Journey** | https://linuxjourney.com | Interactive, gamified learning — excellent for beginners |
| **tldr pages** | https://tldr.sh | Simplified man pages — what I actually use day-to-day |
| **Brendan Gregg's Site** | https://www.brendangregg.com | USE Method, perf examples, eBPF guides |
| **Linux Audit** | https://linux-audit.com | Hardening guides, Lynis security scanner docs |
| **The Linux Documentation Project** | https://tldp.org | Classic HOWTOs — still relevant for deep topics |
| **Kernel.org sysctl docs** | https://www.kernel.org/doc/html/latest/admin-guide/sysctl | Official kernel parameter reference |
| **ExplainShell** | https://explainshell.com | Visual breakdown of any Linux command |

---

## 📝 Core Knowledge Checklist

This is the biggest section — work through it phase by phase. I recommend spending 4–6 weeks on this module if you're starting from scratch.

### Phase 1: Linux Foundations (Week 1–2)

**1.1 Distribution Landscape**
- [ ] RHEL / Rocky / Alma vs Ubuntu / Debian — package managers (`dnf`/`yum` vs `apt`), release cycles, support lifecycles
- [ ] When to choose what: enterprise production → RHEL/Rocky; rapid prototyping → Ubuntu; embedded → Alpine/BusyBox
- [ ] Understanding `.rpm` vs `.deb`, and how to inspect packages with `rpm -qi` or `dpkg -s`

**1.2 The Boot Process (understand this cold — it's interview gold)**
- [ ] BIOS/UEFI → Bootloader (GRUB2) → kernel (vmlinuz) → initramfs → init/systemd
- [ ] GRUB2 configuration: `/etc/default/grub`, `grub.cfg`, and how to rescue a broken boot
- [ ] `dracut` / `initramfs` — what's inside, how to rebuild, rescue mode

**1.3 Filesystem Hierarchy Standard (FHS)**
- [ ] `/bin`, `/sbin`, `/usr/bin`, `/usr/sbin` — why the split exists (and why it's disappearing)
- [ ] `/etc` (config), `/var` (variable data), `/tmp` (tmpfs?), `/proc` (kernel interface), `/sys` (device interface)
- [ ] `/dev` — udev, block devices, character devices, `major:minor` numbers

**1.4 Package Management Mastery**
- [ ] `dnf` / `yum`: repos, GPG keys, `dnf history`, rollback, `dnf module`
- [ ] `apt`: `sources.list`, PPAs, `apt-cache`, `apt-get` vs `apt`, pinning
- [ ] Building from source: `./configure`, `make`, `make install`, and why you should avoid it on prod

**1.5 Basic Administration**
- [ ] `sudo` configuration: `/etc/sudoers`, `visudo`, alias specs, logging
- [ ] Time sync: `chronyd` vs `ntpd`, `timedatectl`, timezone files
- [ ] Locale and keyboard: `localectl`, `locale.conf`

---

### Phase 2: Advanced Administration (Week 3–4)

**2.1 User and Group Management (deep dive)**
- [ ] `/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/gshadow` — field-by-field breakdown
- [ ] `useradd` defaults in `/etc/default/useradd` and `/etc/login.defs`
- [ ] PAM (Pluggable Authentication Modules): `/etc/pam.d/`, stack-based config, common modules
- [ ] `passwd` aging policies, `chage`, locked accounts, password quality (`pwquality.conf`)

**2.2 File Permissions and ACLs**
- [ ] Classical permissions: `rwx` (owner/group/other), octal math, `umask`
- [ ] Special bits: `setuid` (04755), `setgid` (02755), sticky bit (01777) — and when each is dangerous
- [ ] ACLs: `setfacl`, `getfacl`, default ACLs, and how they interact with `cp`/`mv`
- [ ] `chattr` / `lsattr` — immutable files, append-only, and why they confuse backup tools

**2.3 Process Management**
- [ ] Process lifecycle: fork, exec, wait, zombie, orphan
- [ ] `ps`: every flag combo (`aux`, `ef`, `-eo`, `tree`), understanding `STAT` codes (R, S, D, Z, T)
- [ ] `top` / `htop` / `btop` — what each column means (VIRT, RES, SHR, %CPU — it's not what you think)
- [ ] `nice` / `renice` / `cgroups` — process priority and why `nice` alone is weak on modern systems
- [ ] `systemd-run` — running ad-hoc commands in a transient scope/slice

**2.4 systemd — The Init System You Need to Know**
- [ ] Unit types: `.service`, `.socket`, `.timer`, `.target`, `.mount`, `.device`
- [ ] Unit file anatomy: `[Unit]`, `[Service]`, `[Install]` sections
- [ ] `systemctl`: `status`, `cat`, `show`, `list-units`, `list-unit-files`, `daemon-reload`
- [ ] `journalctl`: filtering by unit, priority, time range; persistent journals; log size limits
- [ ] systemd timers vs cron: why timers are better (dependencies, accuracy, logging)
- [ ] `systemd-analyze`: boot time breakdown, blame, plot

**2.5 Disk and Storage**
- [ ] Partition tables: MBR vs GPT, `fdisk` vs `gdisk`, partition types
- [ ] LVM: PV → VG → LV, `lvextend` + `resize2fs`, snapshots, thin provisioning
- [ ] Filesystem choices: `ext4` (reliable), `xfs` (scales), `btrfs` (snapshots), `zfs` (enterprise)
- [ ] Mount options: `noatime`, `nodiratime`, `data=writeback`, `barrier=0` (and why you probably shouldn't)
- [ ] `fstab` — UUID vs LABEL vs device name, `fs_passno`, `mount -a` dry-run

---

### Phase 3: Performance and Troubleshooting (Week 5–6)

**3.1 The USE Method (Brendan Gregg's superpower)**
- [ ] For every resource (CPU, memory, disk, network), check: Utilization, Saturation, Errors
- [ ] CPU USE: `mpstat -P ALL`, `pidstat`, `perf stat`
- [ ] Memory USE: `vmstat`, `free -h`, `/proc/meminfo` (what "available" actually means)
- [ ] Disk USE: `iostat -xz`, `iotop`, `sar -d`
- [ ] Network USE: `sar -n DEV`, `ip -s link`, `ethtool`

**3.2 CPU Performance Deep Dive**
- [ ] CPU modes: user vs system vs idle vs wait — and why high `%wa` is killing your database
- [ ] `perf`: `perf top`, `perf record` + `perf report`, `perf stat`, flame graphs
- [ ] `strace`: tracing system calls, `-c` summary, `-f` follow forks, `-e` filter
- [ ] `bpftrace` / `bcc` tools: `execsnoop`, `opensnoop`, `ext4slower`, `biolatency`
- [ ] CPU affinities: `taskset`, `numactl`, and why NUMA matters for databases

**3.3 Memory Performance Deep Dive**
- [ ] Page cache vs buffer cache — how Linux uses "free" memory (it's not wasted!)
- [ ] `slabtop`, `/proc/slabinfo` — kernel memory leaks often show here
- [ ] OOM Killer: how it chooses, `/proc/<pid>/oom_score_adj`, how to protect critical processes
- [ ] `valgrind` — `memcheck` for user-space leaks (dev only, high overhead)
- [ ] Huge pages: transparent vs explicit, when to enable, Oracle/DB tuning

**3.4 Disk I/O Performance**
- [ ] I/O schedulers: `mq-deadline`, `bfq`, `none` — and why NVMe changed everything
- [ ] `blktrace` + `blkparse` — the full I/O path from syscall to hardware
- [ ] `fio` — the gold standard for benchmarking storage (learn it before you buy SAN)
- [ ] `ionice` — I/O priority, and why it doesn't work on CFQ anymore

**3.5 Network Performance**
- [ ] `ss` vs `netstat` (use `ss` — `netstat` is deprecated)
- [ ] `tcpdump` mastery: filters (`host`, `port`, `tcp[tcpflags]`), `-w` for Wireshark analysis
- [ ] `ethtool`: ring buffers, offloading (`gro`, `lro`, `tso`), and why offloading breaks some packet captures
- [ ] `nstat` / `ip -s link` — interface-level error counters (CRC errors = bad cable, not software)
- [ ] `iperf3` — TCP/UDP bandwidth testing, `-R` reverse, `-P` parallel streams

---

### Phase 4: Kernel Tuning and Hardening (Week 7–8)

**4.1 sysctl — The Kernel Tuning Interface**
- [ ] `sysctl -a`, `/etc/sysctl.conf`, `/etc/sysctl.d/*.conf`
- [ ] Networking tuning: `net.core.somaxconn`, `net.ipv4.tcp_tw_reuse`, `net.ipv4.ip_local_port_range`
- [ ] Memory tuning: `vm.swappiness`, `vm.overcommit_memory`, `vm.dirty_ratio`
- [ ] Filesystem tuning: `fs.file-max`, `fs.inotify.max_user_watches`
- [ ] `kernel.pid_max`, `kernel.threads-max` — running out of PIDs on a busy node

**4.2 eBPF and Modern Observability**
- [ ] What eBPF is (and isn't) — safely running sandboxed programs in the kernel
- [ ] BCC tools: `biosnoop`, `tcpconnect`, `tcpaccept`, `cachestat`, `memleak`
- [ ] bpftrace one-liners: `bpftrace -e 'tracepoint:syscalls:sys_enter_open { @[comm] = count(); }'`
- [ ] Cilium — eBPF-based networking (skim this; it's covered more in K8s module)

**4.3 Security Hardening**
- [ ] SELinux: `getenforce`, `setenforce`, `ausearch`, `sealert`, writing custom policy modules
- [ ] AppArmor: profiles, `aa-status`, `aa-logprof`
- [ ] `firewalld` / `iptables` / `nftables` — the evolution of Linux firewalling
- [ ] SSH hardening: `PermitRootLogin`, `MaxAuthTries`, `AllowUsers`, key-only auth, `sshd -T`
- [ ] `fail2ban` — automated ban based on auth logs
- [ ] `auditd`: writing audit rules, searching logs, compliance (PCI-DSS, SOC2)

**4.4 Container-Aware Linux (Preview)**
- [ ] `namespaces`: PID, NET, MNT, UTS, IPC, USER — the isolation primitives
- [ ] `cgroups v1` vs `cgroups v2` — resource limits, the unified hierarchy
- [ ] `runc` — the OCI runtime that actually creates containers
- [ ] How Docker/containerd/Kubernetes use these primitives (you'll dive deeper in modules 4 & 5)

---

## 💻 Hands-on Commands / Config Examples

Below are real commands I use in production. Copy them, run them, modify them.

**1. System Information & Hardware**
```bash
# CPU info — model, cores, sockets, NUMA nodes
lscpu
# Memory info — total, available, buffers/cache breakdown
free -h && cat /proc/meminfo | grep -E "MemTotal|MemAvailable|Buffers|Cached"
# Block devices — model, size, type (SSD/HDD), rotational
lsblk -o NAME,SIZE,TYPE,ROTA,MOUNTPOINT,MODEL
# PCI devices — useful for driver debugging
lspci -v | less
```

**2. Process Analysis**
```bash
# Find the top CPU-consuming processes, sorted, with threads
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -20
# Same thing, but with full command line and tree view
ps -eo pid,ppid,user,cmd --forest | grep -v grep | head -30
# Real-time process viewer with customizable fields
top -b -n 1 | head -20  # batch mode, one snapshot
# Thread-level CPU usage (great for Java apps with many threads)
ps -eLf | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9}' | sort -k9 -rn | head -20
```

**3. systemd Service File (production template)**
```ini
# /etc/systemd/system/my-app.service
[Unit]
Description=My Application
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=notify
User=appuser
Group=appuser
WorkingDirectory=/opt/my-app
ExecStart=/opt/my-app/bin/server --config /etc/my-app/config.yaml
ExecReload=/bin/kill -USR2 $MAINPID
Restart=on-failure
RestartSec=5s
# Security hardening
PrivateTmp=true
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/log/my-app /var/run/my-app

[Install]
WantedBy=multi-user.target
```
```bash
# After writing the file:
sudo systemctl daemon-reload
sudo systemctl enable --now my-app
sudo journalctl -u my-app -f  # follow logs
```

**4. Performance: `strace` in Production**
```bash
# Trace all system calls of a running process (high overhead — use wisely)
sudo strace -p <PID> -c  # summary by syscall count/time
sudo strace -p <PID> -e trace=open,read,write -f  # specific syscalls, follow children
# Trace a new command from start
strace -f -e trace=network -o /tmp/strace-output.txt curl https://example.com
```

**5. Performance: `perf` Quick Start**
```bash
# Live CPU profiling (like top but showing which function)
sudo perf top
# Record workload, then analyze
sudo perf record -g -- python3 my_script.py  # -g = call graph
sudo perf report  # navigate interactively
# Generate a flame graph (clone Brendan Gregg's FlameGraph repo)
perf record -F 99 -g -- sleep 30
perf script | ./FlameGraph/stackcollapse-perf.pl | ./FlameGraph/flamegraph.pl > out.svg
```

**6. Network: `tcpdump` Filters**
```bash
# Capture all traffic on port 443 (HTTPS), write to file for Wireshark
sudo tcpdump -i any port 443 -w /tmp/https.pcap
# Capture only SYN packets (connection attempts) — great for DoS analysis
sudo tcpdump -i any 'tcp[tcpflags] & (tcp-syn) != 0'
# Capture traffic between two hosts
sudo tcpdump -i any host 10.0.0.5 and host 10.0.0.20
# DNS queries (UDP port 53)
sudo tcpdump -i any -vvv port 53
```

**7. Disk I/O Analysis**
```bash
# Extended I/O statistics, every 1 second, 10 times
iostat -xz 1 10
# Top processes by disk I/O
iotop -oPa  # only show processes doing I/O, accumulate
# Trace block device I/O (needs root, BCC installed)
sudo /usr/share/bcc/tools/biolatency -d /dev/nvme0n1 1 10
# Filesystem latency — which files are slow?
sudo /usr/share/bcc/tools/ext4slower 10  # trace ext4 ops > 10ms
```

**8. Memory Analysis**
```bash
# Detailed memory per process
ps aux --sort=-%mem | head -20
# Slab memory (kernel object cache)
sudo slabtop -o  # once, sorted by usage
# NUMA statistics — are processes on the right NUMA node?
numastat
numactl --hardware  # show NUMA topology
# Check if OOM killer has been active
dmesg | grep -i "out of memory\|oom"
```

**9. Kernel Tuning for High-Throughput Servers**
```bash
# File descriptors (apply in /etc/sysctl.d/99-ops.conf)
cat > /etc/sysctl.d/99-ops.conf << 'EOF'
# Network
net.core.somaxconn = 4096
net.ipv4.tcp_tw_reuse = 1
net.ipv4.ip_local_port_range = 1024 65535
net.ipv4.tcp_max_syn_backlog = 8192
net.core.netdev_max_backlog = 16384

# Memory
vm.swappiness = 1
vm.overcommit_memory = 1  # for Redis; understand the risk!
vm.dirty_ratio = 15
vm.dirty_background_ratio = 5

# Filesystem
fs.file-max = 1000000
fs.inotify.max_user_watches = 524288
EOF
sysctl --system  # reload all sysctl configs
```

**10. LVM Expansion (common production task)**
```bash
# Check current LVM layout
lsblk
sudo pvs  # physical volumes
sudo vgs  # volume groups
sudo lvs  # logical volumes
# Add a new disk and extend
sudo pvcreate /dev/sdb
sudo vgextend vg00 /dev/sdb
sudo lvextend -l +100%FREE /dev/vg00/root_lv
sudo resize2fs /dev/vg00/root_lv  # for ext4
# For xfs:
sudo xfs_growfs /
```

**11. Text Processing Pipeline (the SRE power move)**
```bash
# Parse nginx access log: top 10 IPs by request count
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10
# Find slow requests (>2s response time) in combined log format
awk '$NF > 2 {print $0}' /var/log/nginx/access.log | wc -l
# Extract JSON fields from mixed log file
grep '{' /var/log/app.log | jq -r '.user_id + " " + .action' | sort | uniq -c
# Replace all occurrences across multiple files (safely)
find /etc/nginx/conf.d -name "*.conf" -exec sed -i 's/old-domain.com/new-domain.com/g' {} \;
```

**12. Bash Script Template (production-ready)**
```bash
#!/usr/bin/env bash
# Strict mode — always use this
set -euo pipefail
IFS=$'\n\t'

# Constants
readonly SCRIPT_NAME="$(basename "$0")"
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"
readonly LOCK_FILE="/var/run/${SCRIPT_NAME}.lock"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')] $*" | tee -a "$LOG_FILE"
}

# Cleanup on exit
cleanup() {
    rm -f "$LOCK_FILE"
    log "Script exited"
}
trap cleanup EXIT

# Prevent parallel runs
if [ -f "$LOCK_FILE" ]; then
    log "ERROR: Another instance is running"
    exit 1
fi
touch "$LOCK_FILE"

# Main logic
main() {
    log "Starting backup..."
    # Your code here
    log "Done."
}

main "$@"
```

---

## 🧪 Hands-on Projects

### Project 1: Build a Linux Performance Troubleshooting "War Story"

**Goal**: Intentionally create and then diagnose 5 different performance problems.

**Steps**:
1. Launch a VM (Vagrant or cloud instance) with 2 vCPU, 4GB RAM
2. Install `stress-ng`, `bcc`, `sysstat`, `strace`, `perf`
3. Create these scenarios one by one and document your diagnosis:
   - **CPU saturation**: Run `stress-ng --cpu 4` and use `top` → `pidstat` → `perf top` to identify
   - **Memory pressure**: Run `stress-ng --vm 2 --vm-bytes 3G` and watch OOM killer via `dmesg`
   - **Disk I/O bottleneck**: Run `stress-ng --hdd 4` and use `iostat -xz 1` to see await/util
   - **Network saturation**: Use `iperf3 -s` / `iperf3 -c` and `ss -tin` to see TCP state
   - **Stale file descriptors**: Write a Python script that leaks FDs, then use `lsof -p <PID> | wc -l`
4. Write a 2-page postmortem-style document for each scenario
5. **Deliverable**: A GitHub repo with your notes, screenshots, and the exact commands you used

### Project 2: Write a systemd-based Service with Full Observability

**Goal**: Package a simple app as a production-grade systemd service.

**Steps**:
1. Write a simple Python/Go app that listens on a port and logs requests
2. Create a dedicated user (`useradd -r -s /bin/false myapp`)
3. Write a systemd unit file with: `Type=notify`, security hardening, restart policy
4. Configure `journald` to forward logs to a file via `ForwardToSyslog=yes`
5. Add a `systemd-timer` that runs a health-check script every 5 minutes
6. Simulate a crash (kill -9) and verify `Restart=on-failure` works
7. Use `systemd-analyze security my-app.service` to audit your security settings
8. **Deliverable**: The unit file, timer file, and a README explaining each setting

---

## 🔧 Common Troubleshooting

### Scenario 1: "Server is unresponsive but ping works"

**Symptoms**: SSH hangs, services don't respond, but ICMP ping succeeds.

**Diagnosis**:
```bash
# If you have an out-of-band console:
# Check for OOM killer
dmesg | tail -50
# Check load average vs CPU count
cat /proc/loadavg
nproc
# If load >> CPU count, you have a wait-queue problem (likely disk or lock contention)
# Check for D-state (uninterruptible sleep) processes
ps aux | awk '$8 ~ /D/ { print }'
```

**Solution**: D-state processes usually mean waiting on disk I/O (bad storage, NFS hang). If it's NFS, restart the NFS client mount. If local disk, check `iostat` for `%util = 100%`. Add I/O capacity or tune the I/O scheduler.

---

### Scenario 2: "Application starts but crashes silently"

**Symptoms**: `systemctl start my-app` succeeds, but the service is not running 5 seconds later.

**Diagnosis**:
```bash
# Check the journal for this specific unit
journalctl -u my-app.service --no-pager -n 100
# Check if the process is exiting with a signal
systemctl status my-app.service
# Run the binary manually to see stderr
sudo -u appuser /opt/my-app/bin/server --config /etc/my-app/config.yaml
# Use strace to see the last syscall before exit
strace -e trace=exit_group,write /opt/my-app/bin/server 2>&1 | tail -20
```

**Solution**: Common causes: config file permissions (app can't read it), port already in use (`ss -tlnp | grep <port>`), missing environment variables, or `Type=notify` without the app actually calling `sd_notify()`.

---

### Scenario 3: "DNS resolution is slow or failing intermittently"

**Symptoms**: `curl https://api.example.com` sometimes takes 30s, then works fine.

**Diagnosis**:
```bash
# Check which DNS resolver is configured
cat /etc/resolv.conf
# Test resolution time
time dig api.example.com @8.8.8.8
time dig api.example.com @<internal-dns>
# Check for DNS round-trip amplification (too many lookups)
tcpdump -i any -w /tmp/dns.pcap port 53 &
# then make the request, stop tcpdump, open in Wireshark
# Check systemd-resolved if in use
systemd-resolve --status
```

**Solution**: If using `systemd-resolved`, check `nsswitch.conf` — `hosts: files dns` vs `hosts: files resolve dns`. If internal DNS is slow, add caching via `dnsmasq` or `systemd-resolved`'s built-in cache. If it's a container environment, DNS is covered in Module 4.

---

### Scenario 4: "Disk is full but `du` and `df` show different numbers"

**Symptoms**: `df -h` shows 100% used, but `du -sh /*` totals far less.

**Diagnosis**:
```bash
# A deleted file that's still held open by a process
sudo lsof +L1
# This shows files that are deleted but have a non-zero size and an open FD
# The space will be freed when the process closes the file (or when the process restarts)
```

**Solution**: Identify the process from `lsof` output and restart it gracefully. If you can't restart, you can sometimes truncate the file via `/proc/<PID>/fd/<FD>`:
```bash
# WARNING: Only do this if you understand the consequences
: > /proc/<PID>/fd/<FD>
```
Or just restart the service. This is why you should always configure `logrotate` with `copytruncate` or a post-rotate restart signal.

---

### Scenario 5: "High `%iowait` in `top` — system is slow"

**Symptoms**: `%wa` (I/O wait) is consistently above 30% in `top`. Applications are sluggish.

**Diagnosis**:
```bash
# Identify which processes are waiting on I/O
iotop -oPa
# Check disk utilization and latency
iostat -xz 1 5
# Look for: %util near 100%, avgqu-sz high, await > 50ms
# Which files are being written?
sudo /usr/share/bcc/tools/fileslower 10  # trace file reads/writes > 10ms
```

**Solution**: If `%util` = 100%, your disk is the bottleneck. Options: upgrade to SSD/NVMe, spread I/O across multiple disks, tune `vm.dirty_ratio` to flush more aggressively, or move heavy write workloads to a separate mount point with its own I/O scheduler.

---

## 💼 Interview Questions

**Q1: Explain the Linux boot process from power-on to login prompt.**
A: BIOS/UEFI → GRUB2 (loads kernel + initramfs) → kernel initializes hardware → kernel mounts root FS → kernel starts `systemd` (PID 1) → `systemd` reaches `multi-user.target` (or `graphical.target`) → `getty` presents login. Key interview follow-up: what's in initramfs and why do you need it? (Answer: drivers needed to mount the real root filesystem.)

**Q2: What happens when you run `ls -l` in Linux? (System call deep dive)**
A: Shell `fork()`s (or `clone()`s) a child process → child `execve("/bin/ls", argv, envp)` → kernel loads `/bin/ls` into memory → `ls` calls `openat()` on `.`, `getdents()` to read directory entries, `lstat()` on each file, `write()` to stdout. The `ls` binary itself is loaded via the `execve` syscall which the kernel handles by reading ELF headers, mapping segments, and jumping to `_start`.

**Q3: What is the difference between a process and a thread in Linux?**
A: In Linux, both are `task_struct` in the kernel. The difference is sharing: threads within a process share `mm` (memory), `files` (file descriptors), and `fs` (root/cwd). Processes don't. `clone()` syscall with `CLONE_VM | CLONE_FS | CLONE_FILES` creates a thread; without those flags, it's a process. This is why `ps -eLf` shows both PIDs and TIDs.

**Q4: How does `tcpdump` capture packets? What's the performance impact?**
A: `tcpdump` uses `libpcap`, which uses the `AF_PACKET` socket (or `PF_RING` / `eBPF` on modern systems) to capture at the kernel level before the packet hits the application. Performance impact: minimal for low packet rates; at 10Gbps line rate, `tcpdump -w` can drop packets (use `-n` to avoid DNS resolution, and write to a fast disk or `/dev/shm`).

**Q5: Explain the OOM Killer — how does it choose which process to kill?**
A: When the kernel can't allocate more memory, it invokes OOM Killer. It scores each process using `/proc/<pid>/oom_score` (0–1000), calculated from: process memory usage (bigger = higher score), `oom_score_adj` (-1000 to +1000, set via `echo -900 > /proc/<pid>/oom_score_adj` to protect critical processes). The process with the highest score dies. System-critical processes should have `oom_score_adj = -1000` (never kill).

**Q6: What does `vm.swappiness = 1` actually do?**
A: It controls how aggressively the kernel swaps out process memory. `swappiness = 0` (kernel 3.5+) means avoid swapping as long as possible (only swap to avoid OOM). `swappiness = 100` means swap aggressively. `vm.swappiness = 1` is what I recommend for most database servers — it keeps the page cache but avoids swapping application memory unless absolutely necessary. Note: this doesn't disable swap; it just changes the preference.

**Q7: `setuid` bit — what is it, and why is it a security risk?**
A: `setuid` (04000) makes a program run with the file owner's permissions, not the running user's. Example: `/usr/bin/passwd` is owned by `root` with `setuid` — lets normal users change their own password by writing to `/etc/shadow` (which they can't normally write to). Security risk: if a `setuid` program has a buffer overflow, an attacker can gain root. Never make your own scripts `setuid` — use `sudo` instead, which logs and controls precisely.

**Q8: How do you troubleshoot a server that has high load but low CPU utilization?**
A: High load with low CPU means processes are waiting on something (load average = runnable + waiting). Check: (1) `ps aux | awk '$8 ~ /D/'` for D-state (disk wait), (2) `iostat -xz 1` for I/O wait, (3) `sar -n DEV 1 5` for network saturation, (4) `free -h` for memory pressure (swapping causes high load). Most common cause: a slow storage backend (NFS, cloud EBS with burst balance exhausted).

---

## 📈 Advanced Learning Path

Once you've mastered the core material, here's where to go next:

**Kernel Development**
- Read **Linux Kernel Development (Robert Love)** — understand scheduling, memory management, syscalls
- Subscribe to the **LKML (Linux Kernel Mailing List)** — see how kernel decisions are made
- Try compiling your own kernel: `make menuconfig` → `make -j$(nproc)` → `make modules_install`

**eBPF and Extended Observability**
- **Brendan Gregg's BPF Performance Tools** book — the definitive eBPF reference
- **Cilium** — eBPF-based networking and security (prepares you for K8s networking)
- **Pixie**, **Grafana Pyroscope** — eBPF-based observability tools

**Linux Security**
- **SELinux Coloring Book** (Red Hat) — conceptual introduction
- **Lynis** — open-source security auditing tool, read its reports to learn hardening
- **Linux Server Hardening** checklist from the CIS Benchmarks

**From Linux to Cloud-Native**
- Now that you understand Linux, Module 4 (Docker) and Module 5 (Kubernetes) will click
- The container primitives (namespaces, cgroups) are just Linux features exposed by Docker
- eBPF is the bridge between Linux kernel observability and Kubernetes observability (Cilium, Falco)

---

[← Back to English Home](../README.md)
