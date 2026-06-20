# 02 · Networking for SRE

> **Why this matters**: Every outage is a networking problem until proven otherwise. Whether it's a misconfigured security group, a saturated uplink, a DNS TTL that's too long, or a TLS handshake that's timing out — networking knowledge is what lets you debug across the OSI stack instead of guessing. I've lost count of how many "application bugs" turned out to be MTU mismatches or misconfigured load balancer health checks. Master networking, and you'll solve outages faster than your entire team combined.

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- [ ] Explain the OSI model and TCP/IP stack with concrete examples at each layer
- [ ] Capture and analyze packets with `tcpdump` and Wireshark like a network engineer
- [ ] Design IP addressing schemes: subnetting, CIDR, VLANs, and VPC peering
- [ ] Debug DNS: resolution path, record types, TTL strategy, DNS over HTTPS/TLS
- [ ] Understand HTTP/1.1, HTTP/2 (multiplexing, HPACK), and HTTP/3 (QUIC)
- [ ] Configure and troubleshoot TLS 1.2/1.3: certificates, chains, OCSP, cipher suites
- [ ] Design and operate load balancers: L4 (transport) vs L7 (application), algorithms, health checks
- [ ] Use `iptables` / `nftables` for traffic control, NAT, and security policy
- [ ] Diagnose connectivity with `traceroute`, `mtr`, `ping`, `ss`, `netstat` (legacy)
- [ ] Understand BGP fundamentals: ASNs, prefix announcements, BGP hijacking
- [ ] Configure and tune TCP: congestion control (cubic, bbr), window scaling, keepalive
- [ ] Monitor network performance: bandwidth, latency, jitter, packet loss, retransmits
- [ ] Secure network infrastructure: DDoS mitigation, WAF, network segmentation

---

## 📺 Recommended Video Courses

| Course | Creator / Platform | Views / Info | Difficulty |
|--------|---------------------|--------------|------------|
| **TCP/IP Deep Dive** | David Bombal (YouTube) | 500k+ views | ⭐⭐ Intermediate |
| **Computer Networking Crash Course** | Crash Course (YouTube) | 2M+ views | ⭐ Beginner |
| **Networking for DevOps Engineers** | Nexus (YouTube) | 80k+ views | ⭐⭐ Intermediate |
| **Wireshark Tutorial for Beginners** | NetworkChuck (YouTube) | 400k+ views | ⭐ Beginner |
| **HTTP/2 and HTTP/3 Explained** | HPBN (Ilya Grigorik, YouTube) | 100k+ views | ⭐⭐⭐ Advanced |
| **BGP for Everyone** | Ivan Pepelnjak (ipSpace) | 30k+ students | ⭐⭐⭐ Advanced |
| **Linux Networking Masterclass** | Sander van Vugt (O'Reilly) | 10k+ students | ⭐⭐ Intermediate |
| **AWS Networking Deep Dive** | Adrian Cantrill (Udemy) | 50k+ students | ⭐⭐ Intermediate |

---

## 📖 Recommended Books

| Title | Author | Rating | One-line Recommendation |
|-------|--------|--------|--------------------------|
| **TCP/IP Illustrated, Volume 1 (2nd Ed.)** | Kevin Fall, W. Richard Stevens | ★★★★★ | The definitive TCP/IP reference — every protocol explained with packet captures |
| **Computer Networking: A Top-Down Approach (8th Ed.)** | Kurose & Ross | ★★★★☆ | Best textbook — top-down from HTTP down to physical layer |
| **High Performance Browser Networking** | Ilya Grigorik | ★★★★★ | Free online — the performance bible for web-facing services |
| **HTTP/2 in Action** | Barry Pollard | ★★★★☆ | Clear explanation of multiplexing, server push, and HPACK |
| **BGP (2nd Ed.)** | Iljitsch van Beijnum | ★★★★☆ | Understanding BGP is understanding the internet — essential for cloud networking |
| **The Linux Command Line — Networking Chapters** | William Shotts | ★★★☆☆ | Good practical intro to Linux networking CLI |
| **Network Security Assessment (3rd Ed.)** | Chris McNab | ★★★★☆ | Teaches you to think like an attacker — great for defense |

---

## 🌐 Online Resources

| Resource | Link | Stars / Notes |
|----------|------|---------------|
| **High Performance Browser Networking** | https://hpbn.co | Free book — performance deep dive |
| **Cloudflare Learning Center** | https://www.cloudflare.com/learning | Best conceptual articles on DNS, TLS, DDoS |
| **Beej's Guide to Network Programming** | https://beej.us/guide/bgnet | Classic C socket programming guide |
| **DNS Viz** | https://dnsviz.net | Visual DNS delegation chain debugger |
| **TCP/IP Guide** | https://tcpipguide.com | Free, comprehensive protocol reference |
| **nginx Reverse Proxy Guide** | https://nginx.org/en/docs/http/ngx_http_proxy_module.html | Official — best proxy module docs |
| **Awesome Networking** | https://github.com/luckrnc/awesome-networking | ⭐2.8k — Curated networking resources |
| **WireGuard Documentation** | https://www.wireguard.com | Modern VPN — simpler than IPsec |
| **Let's Encrypt Documentation** | https://letsencrypt.org/docs | TLS certificate automation |
| **ipcalc / cidr.xyz** | https://cidr.xyz | Visual CIDR/subnet calculator |

---

## 📝 Core Knowledge Checklist

Networking is vast. Focus on what SREs actually use day-to-day: TCP, DNS, HTTP, load balancing, and Linux networking. Spend 4–5 weeks on this module.

### Phase 1: Networking Foundations (Week 1)

**1.1 OSI Model vs TCP/IP Model — Know Both**
- [ ] OSI 7 layers vs TCP/IP 4 layers — mapping real protocols to each layer
- [ ] Encapsulation: how an HTTP request becomes an Ethernet frame (with headers at each layer)
- [ ] Why the OSI model still matters for troubleshooting (layer-by-layer isolation)

**1.2 IP Addressing and Subnetting**
- [ ] IPv4 address classes (historical), CIDR notation — `/24`, `/16`, `/8`
- [ ] Subnet mask math: given `10.0.1.0/24`, what's the broadcast address? How many hosts?
- [ ] Private vs public IP ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`
- [ ] IPv6 basics: `2001:db8::/32` (documentation range), SLAAC, NAT64/DNS64

**1.3 Ethernet and ARP**
- [ ] MAC addresses: OUI (vendor), unicast vs multicast vs broadcast
- [ ] ARP: resolution, cache, gratuitous ARP, ARP spoofing (security risk)
- [ ] Switch vs hub vs router — and why you probably haven't seen a hub in 15 years
- [ ] VLANs: 802.1Q tagging, trunk ports, access ports — foundation of network segmentation

**1.4 ICMP — More Than Just Ping**
- [ ] ICMP message types: Echo Request/Reply (ping), Destination Unreachable, TTL Exceeded (traceroute)
- [ ] `ping`: `-c` count, `-i` interval, `-s` size, `-M do` (don't fragment — MTU discovery)
- [ ] `traceroute` / `mtr`: how they work (UDP/ICMP/TCP probes), reading the output
- [ ] PMTU Discovery: why `ping -M do -s 1472` fails on some networks (hint: 1500 MTU - 28 bytes header = 1472)

---

### Phase 2: TCP Deep Dive (Week 2)

**2.1 TCP Connection Lifecycle**
- [ ] 3-way handshake: `SYN` → `SYN-ACK` → `ACK` — and what happens if the last ACK is lost
- [ ] 4-way teardown: `FIN` → `ACK`, `FIN` → `ACK` — vs `RST` (abort)
- [ ] `TIME_WAIT` state: why it exists (2MSL), why it's on the closing side, how to handle high `TIME_WAIT` counts
- [ ] TCP states diagram: memorize `LISTEN`, `SYN_SENT`, `ESTABLISHED`, `CLOSE_WAIT`, `FIN_WAIT_1/2`, `TIME_WAIT`

**2.2 TCP Reliability Mechanisms**
- [ ] Sequence numbers and acknowledgments — how TCP reassembles out-of-order segments
- [ ] Sliding window: sender window vs receiver window, zero-window probing
- [ ] Retransmission: timeout-based (RTO) vs fast retransmit (3 duplicate ACKs)
- [ ] Selective Acknowledgment (SACK) — why it matters for high-latency, high-bandwidth links

**2.3 TCP Congestion Control**
- [ ] Slow start, congestion avoidance, fast recovery — the Reno/NewReno state machine
- [ ] Modern algorithms: `cubic` (default on Linux), `bbr` (Google's BBR — game changer for satellite/high-BDP links)
- [ ] Bufferbloat: why big buffers are bad, and how `fq_codel` / `cake` QoS helps
- [ ] Checking and changing TCP congestion control: `sysctl net.ipv4.tcp_congestion_control`

**2.4 TCP Performance Tuning for SRE**
- [ ] `net.ipv4.tcp_tw_reuse = 1` — reuse `TIME_WAIT` sockets for new outbound connections (safe for clients)
- [ ] `net.ipv4.tcp_fin_timeout = 15` — reduce `FIN_WAIT_2` timeout (default 60s is too long)
- [ ] `net.core.somaxconn = 4096` — backlog for `listen()` syscall
- [ ] `net.ipv4.tcp_max_syn_backlog = 8192` — SYN queue size (protects against SYN flood)
- [ ] TCP keepalive: `tcp_keepalive_time`, `tcp_keepalive_probes`, `tcp_keepalive_intvl` — and why application-level heartbeats are better

**2.5 UDP — When and Why**
- [ ] Connectionless, no reliability, no ordering — why DNS, DHCP, streaming use it
- [ ] UDP checksum: optional in IPv4, mandatory in IPv6
- [ ] QUIC: Google's UDP-based protocol that replaces TCP + TLS + HTTP/2 (HTTP/3 runs on QUIC)

---

### Phase 3: DNS, HTTP, and TLS (Week 3)

**3.1 DNS — The Internet's Phonebook**
- [ ] DNS hierarchy: root → TLD → authoritative → recursive resolver
- [ ] Record types: `A`, `AAAA`, `CNAME`, `MX`, `TXT`, `NS`, `SOA`, `SRV`, `CAA`, `CNAME` (flat — no chaining)
- [ ] `CNAME` at apex (naked domain) — why it's forbidden and how `ALIAS` / `ANAME` records solve it
- [ ] TTL strategy: short TTL (60s) for active-active failover, long TTL (3600s+) for stable records
- [ ] DNS resolution in Linux: `/etc/resolv.conf`, `options ndots:5` (Kubernetes!), `systemd-resolved`
- [ ] DNS over HTTPS (DoH) and DNS over TLS (DoT) — privacy, but breaks internal DNS split-horizon

**3.2 HTTP/1.1 → HTTP/2 → HTTP/3**
- [ ] HTTP/1.1: persistent connections (`Connection: keep-alive`), pipelining (broken in practice), chunked transfer
- [ ] HTTP/2: binary framing, multiplexing (multiple streams over one TCP connection), HPACK header compression, server push (deprecated in practice)
- [ ] HTTP/3: runs on QUIC (UDP), no head-of-line blocking, 0-RTT connection establishment
- [ ] ALPN (Application-Layer Protocol Negotiation) — how TLS handshake negotiates HTTP/2 vs HTTP/1.1

**3.3 TLS — Transport Layer Security**
- [ ] TLS 1.2 handshake: `ClientHello` → `ServerHello` → Certificate → Key Exchange → `Finished`
- [ ] TLS 1.3 handshake: reduced to 1-RTT (sometimes 0-RTT), removed obsolete cipher suites
- [ ] Certificate chains: leaf → intermediate → root — and why a missing intermediate breaks clients
- [ ] OCSP vs OCSP Stapling: real-time revocation checking without phoning home to CA
- [ ] Cipher suites: what `ECDHE-RSA-AES256-GCM-SHA384` actually means (key exchange─authentication─bulk encryption─MAC)
- [ ] Let's Encrypt: `certbot`, ACME protocol, wildcard certificates (`*.example.com`), 90-day renewal

**3.4 HTTP Headers Every SRE Should Know**
- [ ] `X-Forwarded-For`, `X-Real-IP` — and why you must trust them only from known proxies
- [ ] `Strict-Transport-Security` (HSTS) — force HTTPS, prevent downgrade attacks
- [ ] `Content-Security-Policy` — mitigate XSS (not strictly networking, but relevant for edge/SRE)
- [ ] `Connection: close` vs `Keep-Alive` — and why `Keep-Alive` is default in HTTP/1.1
- [ ] `Transfer-Encoding: chunked` — streaming response bodies

---

### Phase 4: Load Balancing and Network Design (Week 4–5)

**4.1 Load Balancer Fundamentals**
- [ ] L4 (transport layer) vs L7 (application layer) — what each sees, what each can do
- [ ] L4: operates on IP + port, cannot read HTTP headers, extremely fast, no SSL termination
- [ ] L7: terminates SSL, reads HTTP headers, can do path-based routing (`/api/*` → api pool), cookie-based session affinity
- [ ] Load balancing algorithms: round-robin, least connections, IP hash, weighted, least time (NGINX Plus)

**4.2 Health Checks — The Most Misconfigured Feature**
- [ ] Active health checks: LB sends periodic probes (HTTP GET `/health`, TCP connect)
- [ ] Passive health checks: mark node unhealthy after N consecutive failures
- [ ] What makes a good health check endpoint: check dependencies (DB, cache), respond within 1s, return 200 only when healthy
- [ ] Common mistake: health check endpoint that always returns 200 (defeats the purpose)

**4.3 High Availability Patterns**
- [ ] Active-Active: both LB nodes handle traffic, DNS round-robin or anycast
- [ ] Active-Passive: floating IP (VIP) via VRRP / keepalived / cloud LB
- [ ] Anycast: same IP advertised from multiple locations, BGP routes to nearest — how Cloudflare works
- [ ] Connection draining (graceful removal): stop sending new connections, let existing ones finish

**4.4 Cloud Networking (AWS/GCP/Azure — concepts apply everywhere)**
- [ ] VPC: private IP space, subnets (each AZ gets a subnet), route tables
- [ ] Security Groups (stateful) vs NACLs (stateless) — security groups are per-ENI, NACLs are per-subnet
- [ ] NAT Gateway vs NAT Instance — why you need NAT for private-subnet internet access
- [ ] VPC Peering vs Transit Gateway — scaling mesh networking
- [ ] Cloud load balancers: Classic ELB (legacy), ALB (L7, target groups), NLB (L4, ultra-fast)

**4.5 iptables / nftables — Linux Firewalling**
- [ ] iptables tables: `filter` (default), `nat`, `mangle`, `raw`
- [ ] iptables chains: `INPUT`, `OUTPUT`, `FORWARD`, `PREROUTING`, `POSTROUTING`
- [ ] Rule processing order: tables in order (raw → mangle → nat → filter), chains in order (rules are evaluated top-to-bottom)
- [ ] Common recipes: block an IP, port forwarding (`DNAT`), masquerading (`SNAT` for outbound)
- [ ] `nftables`: the modern replacement for iptables — simpler syntax, better performance

---

## 💻 Hands-on Commands / Config Examples

**1. Packet Capture — `tcpdump` Essentials**
```bash
# Capture HTTP requests (port 80) on any interface, show ASCII payload
sudo tcpdump -i any -A -s 0 'port 80'
# Capture DNS queries, write to file for Wireshark analysis
sudo tcpdump -i any port 53 -w /tmp/dns.pcap
# Capture only SYN packets (connection attempts) — great for DoS detection
sudo tcpdump -i any 'tcp[tcpflags] & (tcp-syn) != 0 and not port 22'
#Capture traffic between two specific hosts
sudo tcpdump -i any host 10.0.0.5 and host 10.0.0.20 -nn
# Capture with size limit (useful on prod — don't fill the disk!)
sudo tcpdump -i any -C 100 -W 10 -w /tmp/capture.pcap  # 100MB per file, rotate 10 files
```

**2. Network Diagnostics**
```bash
# Check which processes are listening on which ports
sudo ss -tlnp  # TCP, listening, numeric, show process
sudo ss -ulnp   # UDP equivalent
# Check active connections, with TCP state
ss -tan state established '( dport = :443 or sport = :443 )' | wc -l
# TCP retransmit rate — if > 1%, something is wrong
nstat -az TcpRetransSegs TcpOutSegs | awk 'NR>2 {print $2}' | paste - - | awk '{printf "Retransmit rate: %.2f%%\n", ($1/$2)*100}'
# MTU discovery — if this fails, you have a PMTU blackhole
ping -M do -s 1472 -c 3 8.8.8.8  # should succeed for 1500 MTU
ping -M do -s 8972 -c 3 8.8.8.8  # for jumbo frames (9000 MTU)
```

**3. DNS Debugging**
```bash
# dig: the SRE's best friend — verbose output shows the full resolution path
dig +trace example.com  # shows root → TLD → authoritative
dig +short example.com  # just the answer
dig -x 8.8.8.8  # reverse DNS (PTR record)
dig @8.8.8.8 example.com +stats  # use specific resolver, show timing
# Check all NS records and their response consistency
for ns in $(dig +short example.com NS); do echo "=== $ns ==="; dig @$ns example.com +short A; done
# DNS over HTTPS test
curl -H "accept: application/dns-json" "https://cloudflare-dns.com/dns-query?name=example.com&type=A"
```

**4. HTTP/2 and TLS Testing**
```bash
# Test HTTP/2 support (requires openssl 1.1.1+)
openssl s_client -connect example.com:443 -alpn h2,http/1.1 </dev/null 2>&1 | grep ALPN
# Check TLS certificate expiration (expires within 30 days?)
echo | openssl s_client -servername example.com -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
# Scan for supported cipher suites (use testssl.sh for comprehensive scan)
testssl.sh example.com
# curl with HTTP/2
curl -v --http2 https://example.com
# Check OCSP stapling
openssl s_client -connect example.com:443 -status </dev/null 2>&1 | grep -A 10 "OCSP Response"
```

**5. iptables Rules (common patterns)**
```bash
# Allow established/related connections (ALWAYS do this first)
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
# Allow SSH from specific IP only
iptables -A INPUT -p tcp -s 203.0.113.50 --dport 22 -j ACCEPT
# Rate-limit SSH attempts (prevent brute force)
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m limit --limit 3/min -j ACCEPT
# Port forwarding: forward external 80 → internal 8080
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 127.0.0.1:8080
iptables -t nat -A POSTROUTING -j MASQUERADE
# Block an IP
iptables -A INPUT -s 198.51.100.0/24 -j DROP
# List rules with line numbers (for deletion)
iptables -L INPUT --line-numbers
```

**6. Network Interface and Routing**
```bash
# Show all interfaces with IPs
ip addr show
# Add a secondary IP to an interface (useful for migrations)
ip addr add 10.0.0.100/24 dev eth0
# Show routing table
ip route show
# Add a static route
ip route add 172.16.0.0/16 via 10.0.0.1
# Policy-based routing: use a specific table for specific source
ip rule add from 10.0.0.100 lookup 100
ip route add default via 10.0.0.254 table 100
# Check ARP table
ip neigh show
```

**7. Performance Testing**
```bash
# iperf3: TCP bandwidth test
# On server: iperf3 -s
# On client: iperf3 -c <server-ip> -t 30 -P 4  # 4 parallel streams, 30 seconds
# UDP test (to find packet loss)
iperf3 -c <server-ip> -u -b 100M  # 100Mbps UDP
# Simulate network conditions with tc (netem)
sudo tc qdisc add dev eth0 root netem delay 100ms loss 0.5%  # add 100ms delay + 0.5% packet loss
sudo tc qdisc del dev eth0 root  # remove the emulation
# ab (Apache Bench) — quick HTTP load test
ab -n 10000 -c 100 https://example.com/  # 10k requests, 100 concurrency
```

**8. BBR Congestion Control (enable on Linux)**
```bash
# Check current congestion control
sysctl net.ipv4.tcp_congestion_control
# Enable BBR (requires kernel 4.9+)
echo "net.core.default_qdisc = fq" | sudo tee -a /etc/sysctl.d/99-bbr.conf
echo "net.ipv4.tcp_congestion_control = bbr" | sudo tee -a /etc/sysctl.d/99-bbr.conf
sudo sysctl --system
# Verify BBR is active
lsmod | grep bbr
```

---

## 🧪 Hands-on Projects

### Project 1: Build a Mini Load Balancer with `nginx`

**Goal**: Configure `nginx` as an L7 load balancer with health checks, SSL termination, and path-based routing.

**Steps**:
1. Launch 3 VMs (or Docker containers): 1 LB + 2 backend web servers
2. Install `nginx` on all three
3. On the LB, configure:
   - Upstream block with 2 backend servers, health check (`max_fails=3 fail_timeout=10s`)
   - SSL termination with a self-signed cert (or Let's Encrypt staging)
   - Path-based routing: `/api/*` → API servers, `/` → static servers
   - Rate limiting: `limit_req_zone` — 10 req/s per IP
4. On backends, configure a simple health check endpoint (`/health`) that checks a fake "database" (a file)
5. Simulate a backend failure (`systemctl stop nginx` on one), watch the LB remove it from rotation
6. Test with `ab` or `hey` (HTTP load testing tool)
7. **Deliverable**: `nginx.conf`, a diagram of your setup, and a screenshot of the load balancing in action

### Project 2: Packet Analysis — Debug a Slow Application

**Goal**: Use `tcpdump` + Wireshark to diagnose a real performance problem.

**Steps**:
1. Set up a simple client-server app (e.g., Python `http.server` or `nginx`)
2. Introduce an artificial delay (via `tc netem` on the server)
3. Capture traffic: `tcpdump -i any -w /tmp/slow.pcap port 80`
4. Open the `.pcap` in Wireshark
5. Use Wireshark's **TCP Stream Graph** → **Time-Sequence Graph** to visualize
6. Look for: retransmissions (black packets), duplicate ACKs, zero window (receiver overwhelmed)
7. Identify the bottleneck: is it the server (slow response) or the network (packet loss)?
8. Write a postmortem report: what you found, which Wireshark filters you used, the root cause
9. **Deliverable**: The `.pcap` file (anonymized), Wireshark screenshots, and your analysis report

---

## 🔧 Common Troubleshooting

### Scenario 1: "Connection timeout" but the server is up

**Symptoms**: `curl http://internal-api:8080` hangs and eventually times out. The server process is running, CPU is low.

**Diagnosis**:
```bash
# Is the process listening?
sudo ss -tlnp | grep 8080  # if empty, process isn't listening
# Can you reach it locally on the server?
curl http://127.0.0.1:8080  # if this works, it's a network/firewall issue
# Check firewall rules
sudo iptables -L INPUT -n -v  # look for DROP rules
# Check security groups (if on cloud)
# Check routing: does the client have a route to the server's subnet?
ip route get <server-ip>  # run this on the client
# tcpdump on both ends to see if SYN packets arrive
sudo tcpdump -i any 'port 8080' -nn  # on server — do you see SYN?
```

**Solution**: Most common: security group / firewall blocking the port. Second most common: wrong bind address (app binds to `127.0.0.1` instead of `0.0.0.0`). Third: route table missing or wrong.

---

### Scenario 2: "DNS resolution is intermittently slow"

**Symptoms**: Application logs show occasional 5-second delays on outbound HTTP calls. `dig` is fast when you test manually.

**Diagnosis**:
```bash
# Check the DNS resolver configuration
cat /etc/resolv.conf
# If it has multiple nameservers, Linux uses the first one; if it times out (5s default), it tries the second
# Check resolution time with detailed output
dig example.com +stats
# If using systemd-resolved, check its cache and upstream config
systemd-resolve --statistics
systemd-resolve --status
# Check for DNS race conditions in containers (Kubernetes sets ndots:5 by default!)
cat /etc/resolv.conf | grep ndots  # if ndots:5, every DNS query tries the search domain first = slow
```

**Solution**: If `ndots:5`, this is a Kubernetes "feature" — every DNS query for a name without 5 dots gets tried with the search domain suffix first. Fix: set `options ndots:2` in `/etc/resolv.conf`, or use `dnsConfig` in the Pod spec. If using external DNS, add a local DNS cache ( `systemd-resolved` or `dnsmasq`).

---

### Scenario 3: "High retransmit rate on production database connections"

**Symptoms**: Application performance degrades. `nstat -az | grep Retrans` shows high `TcpRetransSegs`.

**Diagnosis**:
```bash
# Confirm retransmit rate
nstat -az TcpRetransSegs TcpOutSegs | awk 'NR>2 {print $2}' | paste - - | awk '{printf "Rate: %.2f%%\n", ($1/$2)*100}'
# Capture traffic to/from the database
sudo tcpdump -i any host <db-ip> and port 5432 -w /tmp/db.pcap
# Open in Wireshark — look for black (retransmitted) packets
# Check for packet loss along the path
mtr -r -c 100 <db-ip>  # report mode, 100 packets — shows loss at each hop
# Check interface error counters
ip -s link show eth0  # look at "RX errors", "TX errors"
```

**Solution**: Packet loss between app and DB. Could be: (1) oversubscribed network link, (2) faulty switch port (check `ethtool -S eth0 | grep error`), (3) MTU mismatch (PMTU blackhole — TCP segments get silently dropped). Fix: find the loss point with `mtr`, then fix the underlying network issue. As a temporary workaround, enable TCP BBR which handles loss better.

---

### Scenario 4: "TLS handshake timeout in the load balancer"

**Symptoms**: HTTPS requests through the LB occasionally fail with `SSL handshake timeout`.

**Diagnosis**:
```bash
# Test TLS handshake time
time echo | openssl s_client -connect example.com:443 -servername example.com 2>&1 | head -20
# If it takes > 5s, something is wrong
# Check if the LB's certificate chain is complete
openssl s_client -connect example.com:443 -CAfile /etc/ssl/certs/ca-certificates.crt
# If you see "Verify return code: 21 (unable to verify the first certificate)" — incomplete chain
# Check OCSP responder reachability (from the LB)
openssl ocsp -issuer intermediate.crt -cert example.com.crt -url http://ocsp.ca.com -header "HOST" "ocsp.ca.com"
```

**Solution**: Incomplete certificate chain — the server isn't sending the intermediate certificate. Fix: concatenate the intermediate cert to your cert: `cat example.com.crt intermediate.crt > fullchain.crt`. For OCSP stapling timeout: disable OCSP must-staple or ensure the LB can reach the OCSP responder (may need outbound 80 allowed in firewall).

---

### Scenario 5: "`TIME_WAIT` socket exhaustion"

**Symptoms**: Application can't make outbound connections. `ss -tan state time-wait | wc -l` shows tens of thousands.

**Diagnosis**:
```bash
# Check time_wait count
ss -tan state time-wait | wc -l
# Check if kernel is recycling TIME_WAIT
sysctl net.ipv4.tcp_tw_reuse  # should be 1 for clients
sysctl net.ipv4.ip_local_port_range  # is the port range big enough?
# Calculate: if you have 30k TIME_WAIT sockets and a port range of 32768-60999 (28k ports), you're stuck
```

**Solution**: Enable `net.ipv4.tcp_tw_reuse = 1` (allows reusing TIME_WAIT sockets for new outbound connections — safe for clients, NEVER for servers). Expand `net.ipv4.ip_local_port_range`. As a last resort, reduce `net.ipv4.tcp_fin_timeout = 15` (default 60s). Real fix: use connection pooling (HTTP keep-alive, database connection pools) — don't open a new TCP connection for every request.

---

## 💼 Interview Questions

**Q1: Explain what happens when you type `https://www.example.com` in your browser.**
A: (1) DNS resolution: browser checks cache → OS cache → `/etc/hosts` → DNS resolver → authoritative NS. (2) TCP connection: 3-way handshake to resolved IP on port 443. (3) TLS handshake: ClientHello (with SNI + ALPN) → ServerHello (certificate + chosen cipher) → key exchange → Finished. (4) HTTP request sent over TLS. (5) Server responds with HTTP response. (6) Browser renders. Follow-up: what's SNI? (Server Name Indication — lets the server present the correct certificate when hosting multiple HTTPS sites on one IP.)

**Q2: What's the difference between L4 and L7 load balancing?**
A: L4 (transport layer) load balancing operates on IP + port only. It doesn't understand the application protocol — can't read HTTP headers, can't do SSL termination. It's extremely fast and works for any TCP/UDP protocol. L7 (application layer) terminates the connection, reads the application protocol (usually HTTP), and can make routing decisions based on headers, cookies, URL paths. L7 can do SSL termination, HTTP/2, and more sophisticated health checks. Trade-off: L7 is slower (more processing per packet) and more complex.

**Q3: Why do we need `TIME_WAIT` state, and why does it last 2MSL?**
A: `TIME_WAIT` ensures (1) the remote end receives the ACK to its FIN (if the ACK is lost, remote re-sends FIN, and we need to still be in a state that can ACK it), and (2) old duplicated packets from the connection don't arrive at a later connection that happens to reuse the same 4-tuple (src IP, src port, dst IP, dst port). 2MSL (Maximum Segment Lifetime, typically 60s) ensures all packets from the old connection have died in the network.

**Q4: Explain BGP in one paragraph.**
A: BGP (Border Gateway Protocol) is the routing protocol that holds the internet together. It allows autonomous systems (ASNs — each ISP, cloud provider, large enterprise has one) to announce which IP prefixes they own. When you announce `198.51.100.0/24` via BGP, the world routes traffic for that prefix to you. BGP is path-vector (not distance-vector) — it carries the full AS path, which prevents loops and lets network operators set policy (prefer this upstream, don't announce to that peer). BGP hijacking happens when a malicious ASN announces someone else's prefix — traffic gets routed to the attacker.

**Q5: What is `tcp_tw_reuse` and is it safe?**
A: `tcp_tw_reuse` allows the kernel to reuse `TIME_WAIT` sockets for new outbound connections. It's safe for clients (outbound connections) because the kernel verifies that the new connection uses a fresh timestamp (via TCP timestamp option) and that the sequence number is increasing. It is NOT safe for servers (inbound connections) — never enable it on a server. The safer alternative for servers is connection reuse (HTTP keep-alive).

**Q6: How does HTTP/2 multiplexing work, and why is it faster than HTTP/1.1?**
A: HTTP/1.1 opens multiple TCP connections (usually 6 per domain) to parallelize requests. But each connection can only handle one response at a time (head-of-line blocking). HTTP/2 uses a single TCP connection and breaks requests/responses into small frames, each tagged with a stream ID. Frames from multiple streams are interleaved on the single connection. This eliminates head-of-line blocking at the HTTP level (though not at the TCP level — that's what HTTP/3/QUIC solves). It also uses HPACK header compression to reduce overhead.

**Q7: What is PMTU Discovery, and what is a PMTU blackhole?**
A: PMTU (Path MTU) Discovery figures out the maximum packet size that can traverse the entire path without fragmentation. It works by sending packets with the "Don't Fragment" (DF) bit set; if any link along the path has a smaller MTU, that link's router sends back an ICMP "Fragmentation Needed" message, and the sender reduces its packet size. A PMTU blackhole happens when firewalls block those ICMP messages — the sender never finds out it needs to reduce packet size, and large packets silently get dropped. Symptoms: small requests work, large requests hang. Fix: `ping -M do -s 1472` to find the actual MTU, then set `ip link set eth0 mtu <size>`.

**Q8: Explain the difference between `iptables` and `nftables`.**
A: `iptables` is the classic Linux firewall, with separate tools for each protocol family (`iptables` for IPv4, `ip6tables` for IPv6, `arptables` for ARP). It has a locked-in, hard-to-read syntax. `nftables` is the modern replacement (kernel 3.13+) that unifies all protocol families into one tool with a cleaner syntax, atomic rule updates (no race conditions), and better performance. Most distributions now default to `nftables` (Debian 10+, RHEL 8+), though `iptables` commands are often translated to `nftables` under the hood via a compatibility layer.

---

## 📈 Advanced Learning Path

**Network Programming**
- Read **UNIX Network Programming, Volume 1 (Stevens)** — the bible of sockets programming
- Write a simple HTTP server in C (or Go) using `socket()`, `bind()`, `listen()`, `accept()` — understand blocking vs non-blocking, `epoll` vs `select`

**Advanced TCP**
- **BBR v2** — the next version of Google's congestion control (fairer than v1)
- **TCP Fast Open** — 0-RTT data in the SYN packet (requires `net.ipv4.tcp_fastopen = 3`)
- **MPTCP** (Multipath TCP) — using multiple interfaces (Wi-Fi + cellular) simultaneously

**Cloud Networking Specialization**
- AWS Advanced Networking — Direct Connect, Transit Gateway, VPC sharing
- GCP — Andromeda (their networking stack), global load balancing
- Kubernetes Networking (CNI deep dive) — covered in Module 5, but understanding Linux networking first is essential

**Security**
- **Wireshark Certified Network Analyst (WCNA)** — if you want to prove packet analysis skills
- **SANS SEC503: Intrusion Detection and Analysis** — network security monitoring
- **MITM (Man-in-the-Middle) attack lab** — understand how ARP spoofing, DNS poisoning, and SSL stripping work (so you can defend against them)

---

[← Back to English Home](../README.md)
