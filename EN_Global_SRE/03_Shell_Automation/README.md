# 03 · Shell & Automation

> The command line is a force multiplier. A good script replaces hours of clicking with milliseconds of execution.
> This module starts from zero — assumes you only know `ls` and `cd`.

---

## 🎯 Learning Objectives

By completing this module, you should be able to:

- [ ] Master Bash syntax (variables, conditionals, loops, functions)
- [ ] Read and modify existing Shell scripts
- [ ] Process text with `awk`/`sed`/`grep` (log analysis essential)
- [ ] Write practical Ops scripts (backup, log cleanup, health check)
- [ ] Configure cron jobs for scheduled tasks
- [ ] Debug Shell scripts (`set -x`, echo breakpoints)
- [ ] Understand when to use Python vs Bash for Ops tasks
- [ ] Write 100+ line complex scripts

**After this module, you can automate repetitive work.**

---

## 📺 Recommended Video Courses

| Course | Instructor | Link | Views | Rating |
|--------|-------------|------|-------|--------|
| Linux Shell Scripting | Udemy | [Link](https://www.udemy.com/course/linux-shell-scripting/) | Paid | ⭐⭐⭐⭐ |
| Bash Scripting Full Course | FreeCodeCamp | [YouTube](https://youtube.com/watch?v=oxuR. | 2M+ | ⭐⭐⭐⭐⭐ |
| awk/sed Mastery | O'Reilly | [O'Reilly](https://oreilly.com/) | Books | ⭐⭐⭐⭐ |
| Python for DevOps | Noah Gift | [O'Reilly](https://oreilly.com/) | Book | ⭐⭐⭐⭐ |

---

## 📖 Recommended Books

| Book | Author | Level | Comment |
|------|--------|-------|---------|
| **Learning the bash Shell (3rd Ed.)** | O'Reilly | Beginner→Intermediate | The Bash bible. Clear and practical. |
| **sed & awk (2nd Ed.)** | O'Reilly | Intermediate | Text processing masters. Must-read for Ops. |
| **The Linux Command Line** | William Shotts | Beginner | Free online, best Linux CLI intro. |
| **Automate the Boring Stuff with Python** | Al Sweigart | Beginner | Free online. Python for non-programmers. |
| **Python for DevOps** | Noah Gift et al. | Intermediate | Python speciically for Ops tasks. |

---

## 🌐 Online Resources

| Resource | Link | Features |
|----------|------|----------|
| GNU Bash Manual | https://www.gnu.org/s/bash/manual/ | Authoritative reference |
| ShellCheck | https://www.shellcheck.net/ | Static analysis for Shell scripts |
| Explainshel.com | https://explainshel.com/ | Interactive Bash explanation |
| awesome-shell | https://github.com/aleksandrilyin/awesome-shell | Shell tools and resources |
| Google Style Guide | https://google.github.io/stypeguide/sh/ | Best practices for writing scripts |

---

## 📝 Core Knowledge Checklist

### Phase 1: Bash Fundamentals (1 week)

#### Variables & Basics

```bash
# Variable assignment (NO spaces around =)
name="vinson"
age=30

# Using variables
echo $name
echo "My name is ${name}"  # Recommended: always use ${}

# Environment variables
echo $HOME
echo $PATH
export MY_VAR="hello"  # Export as environment variable

# Special variables
echo $0   # Script name
echo $1   # First argument
echo $@   # All arguments
echo $#   # Number of arguments
echo $?   # Exit code of last command (0=success)
```

#### Conditionals

```bash
# File tests
if [ -f "/etc/passwd" ]; then
    echo "File exists"
fi

if [ -d "/tmp" ]; then
    echo "/tmp is a directory"
fi

# String tests
if [ "$name" = "vinson" ]; then
    echo "Name matches"
fi

if [ -z "$name" ]; then
    echo "String is empty"
fi

# Numeric tests
if [ $age -gt 18 ]; then
    echo "Adult"
fi

# -eq equal  -ne not equal  -gt greater  -lt less  -ge greater-or-equal  -le less-or-equal

# Logical operators
if [ -f "/etc/passwd" ] && [ -r "/etc/passwd" ]; then
    echo "File exists and is readable"
fi
```

#### Loops

```bash
# for loop
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

# Iterate over files
for file in /var/log/*.log; do
    echo "Log file: $file"
done

# while loop
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done

# Read file line by line
while IFS= read -r line; do
    echo "Line: $line"
done < /etc/passwd
```

#### Functions

```bash
# Define function
backup() {
    local src="$1"
    local dest="$2"
    echo "Starting backup: $src → $dest"
    cp -r "$src" "$dest"
    if [ $? -eq 0 ]; then
        echo "Backup successful"
    else
        echo "Backup failed"
        return 1
    fi
}

# Call function
backup "/var/log" "/backup/log_$(date +%Y%m%d)"
```

### Phase 2: Text Processing Trio (1 week)

#### `grep` — Text Search

```bash
# Basic search
grep "error" /var/log/app.log

# Show line numbers
grep -n "error" /var/log/app.log

# Invert match (show non-matching lines)
grep -v "info" /var/log/app.log

# Recursive search
grep -r "TODO" /home/user/projects/

# Regex search
grep -E "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}" access.log  # Extract IPs
```

#### `sed` — Stream Editor

```bash
# Substitute (output only, doesn't modify file)
sed 's/old/new/' file.txt

# In-place modification (-i)
sed -i 's/old/new/g' file.txt

# Delete lines containing pattern
sed '/error/d' file.txt

# Append after matching line
sed '/pattern/a\New line' file.txt
```

#### `awk` — Text Analysis (Most Powerful)

```bash
# Print column 1
awk '{print $1}' access.log          # Column 1 (IP)
awk '{print $1, $7}' access.log     # Column 1 and 7

# Conditional filter
awk '$9 >= 400 {print $1, $7, $9}' access.log  # Status >= 400

# Statistics (like SQL)
awk '{count[$1]++} END {for (ip in count) print ip, count[ip]}' access.log | sort -k2 -nr | head -10
# Explanation: count visits per IP, sort by count descending, show top 10

# Real-world: find top 10 IPs by access count
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -10

# Real-world: count requests per minute
awk '{print substr($4, 2, 17)}' /var/log/nginx/access.log | uniq -c
```

### Phase 3: Practical Ops Scripts (1 week)

#### Script 1: Auto Backup `/var/log`

```bash
#!/bin/bash
# log-backup.sh — automated log backup

set -e  # Exit immediately on error
set -u  # Treat unset variables as an error

BACKUP_DIR="/backup/logs"
SOURCE_DIR="/var/log"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/log-backup-$DATE.tar.gz"

# Check if backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Backup directory doesn't exist, creating: $BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
fi

# Archive and compress
echo "Starting backup..."
tar -czf "$BACKUP_FILE" "$SOURCE_DIR" 2>/dev/null

# Check backup result
if [ -f "$BACKUP_FILE" ]; then
    BACKUP_SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "✅ Backup successful: $BACKUP_FILE (Size: $BACKUP_SIZE)"
else
    echo "❌ Backup failed"
    exit 1
fi

# Delete 7-day-old backups
find "$BACKUP_DIR" -name "log-backup-*.tar.gz" -mtime +7 -delete
echo "Cleanup complete: 7-day-old backups deleted"
```

#### Script 2: Disk Usage Alert

```bash
#!/bin/bash
# disk-alert.sh — alert when disk usage exceeds threshold

THRESHOLD=80
ALERT_LOG="/var/log/disk-alert.log"

df -h | grep -v "Filesystem" | while read line; do
    usage=$(echo $line | awk '{print $5}' | sed 's/%//')
    partition=$(echo $line | awk '{print $1}')
    mounted=$(echo $line | awk '{print $6}')

    if [ $usage -ge $THRESHOLD ]; then
        MSG="$(date '+%Y-%m-%d %H:%M:%S') [ALERT] Partition $partition ($mounted) usage ${usage}%"
        echo "$MSG" | tee -a "$ALERT_LOG"
        # In production: send email or call alert API
        # mail -s "Disk Alert" admin@company.com < "$ALERT_LOG"
    fi
done
```

#### Script 3: Server Health Check

```bash
#!/bin/bash
# health-check.sh — check server health

echo "===== Server Health Check Report ====="
echo "Check time: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 1. CPU load
load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | sed 's/,//')
echo "📊 CPU Load (1-min): $load"

# 2. Memory usage
mem_total=$(free -m | awk '/Mem:/ {print $2}')
mem_used=$(free -m | awk '/Mem:/ {print $3}')
mem_percent=$((mem_used * 100 / mem_total))
echo "💾 Memory Usage: ${mem_percent}% (${mem_used}MB / ${mem_total}MB)"

# 3. Disk usage
echo "💿 Disk Usage:"
df -h | grep -v "Filesystem" | awk '{print "   " $1 " → " $5 " (Mount: " $6 ")"}'

# 4. Critical processes
echo "🔧 Critical Process Check:"
for proc in nginx mysql redis-server docker; do
    if pgrep -x "$proc" > /dev/null; then
        echo "   ✅ $proc is running"
    else
        echo "   ❌ $proc is NOT running"
    fi
done

echo ""
echo "===== Check Complete ====="
```

### Phase 4: crontab Scheduled Tasks (3 days)

```bash
# View current user's cron jobs
crontab -l

# Edit cron jobs
crontab -e

# Format: minute hour day month weekday command
#          ┬  ┬  ┬  ┬  ┬
#          │  │  │  │  │
#          │  │  │  │  └─ Weekday (0-7, 0 and 7 = Sunday)
#          │  │  │  └──── Month (1-12)
#          │  │  └─────── Day (1-31)
#          │  └──────────── Hour (0-23)
#          └───────────────── Minute (0-59)

# Examples:
0 3 * * * /scripts/log-backup.sh           # Run at 3:00 AM daily
*/10 * * * * /scripts/health-check.sh    # Run every 10 minutes
0 0 * * 0 /scripts/cleanup.sh           # Run at midnight on Sundays
0 9-18 * * 1-5 /scripts/monitor.sh  # Run hourly 9AM-6PM on weekdays

# Special strings:
# *   any value
# ,   list separator (e.g., 1,3,5)
# -   range (e.g., 1-10)
# /   step (e.g., */10 = every 10 minutes)
```

### Phase 5: Python for Ops (1 week)

Why learn Python? Bash is great for simple tasks. Python is better for complex logic.

```python
#!/usr/bin/env python3
# check-ports.py — check if server ports are reachable

import socket
import sys

def check_port(host, port, timeout=3):
    """Check if a port is open on target host"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Check failed: {e}")
        return False

if __name__ == "__main__":
    targets = [
        ("127.0.0.1", 22, "SSH"),
        ("127.0.0.1", 80, "HTTP"),
        ("127.0.0.1", 3306, "MySQL"),
    ]
    print("===== Port Check =====")
    for host, port, name in targets:
        if check_port(host, port):
            print(f"✅ {name} ({host}:{port}) — Port open")
        else:
            print(f"❌ {name} ({host}:{port}) — Port unreachable")
```

---

## 💻 Practical Command Examples

### Log Analysis Essential Trio

```bash
# 1. Watch real-time logs
tail -f /var/log/nginx/access.log

# 2. Top 10 IPs by access count
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -10

# 3. Count requests in a time range
awk '/21\/Jun\/2024:10/,/21\/Jun\/2024:11/' /var/log/nginx/access.log | wc -l

# 4. Find URLs with most 404s
awk '$9 == 404 {print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -20

# 5. Count requests per hour
awk '{print substr($4, 2, 15)}' /var/log/nginx/access.log | uniq -c
```

### System Inspection Commands (Frequently Used)

```bash
# CPU cores
nproc

# Memory details
free -h

# Disk IO stats
iostat -x 1 5

# Network connection count by state
netstat -an | awk '/^tcp/ {print $6}' | sort | uniq -c | sort -nr

# Find which process is using lots of file descriptors
lsof -n | awk '{print $1}' | sort | uniq -c | sort -nr | head

# Find top 10 largest files/directories
du -ah / | sort -rh | head -10
```

---

## 🧪 Hands-on Projects

### Project 1: Automated Log Cleanup System

**Goal**: Write a script that automatically cleans up logs older than 30 days, with a preview mode.

**Requirements**:
1. Configurable target directory and retention days
2. Preview mode (list files to be deleted, don't actually delete)
3. Logging of cleanup actions
4. Cron job: run daily at 2:00 AM

### Project 2: Daily Server Report (Auto-generated)

**Goal**: Generate a daily server health report and send it to Ops team channel.

**Steps**:
1. Use the `health-check.sh` template above
2. Save output to `/var/report/health-$(date +%Y%m%d).txt`
3. Send via email or enterprise WeChat API
4. Cron: run daily at 9:00 AM

---

## 🔧 Common Troubleshooting

### Issue 1: `Permission denied` when running a script

**Cause**: Script doesn't have execute permission.

**Fix**:
```bash
chmod +x script.sh
# Or run with bash directly (no +x needed)
bash script.sh
```

### Issue 2: Script works in terminal but not in crontab

**Common causes**:
1. PATH issue: crontab's `PATH` is limited; use absolute paths for commands
2. Environment variables: crontab doesn't load `.bashrc`; source it at script start
3. Output redirection: crontab has no terminal; output defaults to email (usually not configured)

**Fix**:
```bash
# Add at script start:
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# Or use absolute paths: /usr/bin/awk instead of awk
```

### Issue 3: `awk` is slow on large files

**Optimization**:
```bash
# Bad (calls external command for each line)
awk '{system("date -d @" $1)}' file.log

# Good (uses awk built-in functions)
awk '{print strftime("%Y-%m-%d", $1)}' file.log
```

---

## 💼 Interview Questions

1. **Difference between `$@` and `$*`?**
   - `$@`: Each argument stays separate ("$@" preserves spaces in arguments)
   - `$*`: All arguments merged into one string

2. **How to count 500 errors in a log file using `awk`?**
   ```bash
   awk '$9 == 500 {count++} END {print count}' access.log
   ```

3. **How to trap Ctrl+C in a Shell script?**
   ```bash
   trap "echo 'Interrupted! Cleaning up...'; exit 1" INT TERM
   ```

4. **How to write a script that prevents double execution?**
   ```bash
   LOCK_FILE="/tmp/my-script.lock"
   if [ -f "$LOCK_FILE" ]; then
       echo "Script is already running, exiting"
       exit 1
   fi
   touch "$LOCK_FILE"
   trap "rm -f $LOCK_FILE" EXIT  # Auto-remove lock on exit
   ```

---

## 📈 Advanced Learning Path

- **Advanced Bash**: Arrays, associative arrays, regex, process substitution
- **Python for Ops**: Learn `paramiko` (SSH), `psutil` (system monitoring), `requests` (API calls)
- **Configuration Management**: Learn Ansible (YAML + Python, no agent needed)
- **Go for Ops Tool Dev**: Learn Go to write high-performance Ops tools (like `kubectl`, `terraform`)

---

## 🔗 Related Resources

- [← Back to EN Home](../README.md)
- [EN 02 Networking](../02_Networking/)
- [EN 04 Containers](../04_Container_Docker/)
- [EN 11 SRE Handbook](../11_SRE_Handbook/)
- [GitHub Trending: Shell/Automation](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · Good scripts = early leave</sub>
</p>
