# 04 · Container Docker#

> Docker is the foundation of modern Ops. Master it, and K8s becomes approachable.
> This module takes you from installation to production practices.

---

## 🎯 Learning Objectives#

By completing this module, you should be able to:

- [ ] Understand the difference between containers and VMs
- [ ] Install and configure Docker (demon.json tuning)
- [ ] Master Docker basics (run/exec/logs/rm etc.)
- [ ] Write production-grade Dockerfiles (multi-stage, security best practices)
- [ ] Use Docker Compose for multi-container apps
- [ ] Configure Docker networking (bridge/host/overlay)
- [ ] Configure Docker storage (volume/bind mount/tmpfs)
- [ ] Set up a private registry (Harbor)
- [ ] Master Docker security hardening (non-root, image scanning)
- [ ] Troubleshoot common container issues

**After this module, you can containerize any app.**

---

## 📺 Recommended Video Courses#

| Course | Instructor | Link | Views | Rating |
|--------|-------------|------|-------|--------|
| Docker Mastery | Bret Fisher | [Udemy](https://www.udemy.com/course/docker-mastery/) | Paid | ⭐⭐⭐⭐⭐ |
| Docker Full Course | FreeCodeCamp | [YouTube](https://youtube.com/watch?v=rXC861N P58) | 2M+ | ⭐⭐⭐⭐ |
| Docker Compose | Bret Fisher | [YouTube](https://youtube.com/watch?v=HG6yWln4e08) | 500K+ | ⭐⭐⭐⭐ |
| Harbor Private Registry | IBM | [YouTube](https://youtube.com/watch?v=pk3V0lb９) | 100K+ | ⭐⭐⭐⭐ |

---

## 📖 Recommended Books#

| Book | Author | Level | Comment |
|------|--------|-------|---------|
| **Docker in Action (2nd Ed.)** | O'Reilly | Intermediate | Best Docker book bar none. |
| **Docker: Up & Running (2nd Ed.)** | O'Reilly | Intermediate | Practical, good for Ops. |
| **Docker Deep Dive** | Nigel Poulton | Beginner→Intermediate | Very clear explanations. |

---

## 🌐 Online Resources#

| Resource | Link | Features |
|----------|------|----------|
| Docker Official Docs | https://docs.docker.com/ | Authoritative. |
| Play with Docker | https://labs.play-with-docker.com/ | Free online lab. |
| docker/library | https://github.com/docker-library/official-images | Official image source. |
| awesome-docker | https://github.com/veggiemonk/awesome-docker | Docker resources. |

---

## 📝 Core Knowledge Checklist#

### Phase 1: Docker Basics & Installation (3-5 days)#

#### Containers vs VMs#

```
VM:
  Hardware → Hypervisor → Guest OS × N → App × N
  Pros: Strong isolation.
  Cons: Heavy (each VM has full OS).

Container:
  Hardware → Host OS → Docker Engine → Container × N
  Pros: Lightweight (share Host OS kernel),秒级启动.
  Cons: Weaker isolation than VMs.
```

#### Installation (CentOS 7/8)#

```bash
# 1. Remove old versions
sudo yum remove -y docker docker-common docker-selinux docker-engine

# 2. Install dependencies
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

# 3. Add Docker repository (use Aliyun mirror for China)
sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 4. Install Docker
sudo yum install -y docker-ce docker-ce-cli containerd.io

# 5. Configure mirror acceleration (MUST do for China)
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "https://mirror.ccs.tencentyun.com",
    "https://registry.docker-cn.com"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  }
}
EOF

# 6. Start Docker
sudo systemctl enable docker
sudo systemctl start docker

# 7. Verify
docker version
docker info
```

#### Docker Basic Commands#

```bash
# Image operations
docker search nginx                 # Search images
docker pull nginx:1.25                # Pull image
docker images                         # List local images
docker rmi nginx:1.25               # Remove image
docker build -t my-app:v1 .       # Build image (Dockerfile in current dir)

# Container operations
docker run -d --name my-nginx -p 8080:80 nginx:1.25
                                 # Start container (-d=background, --name, -p=port mapping)
docker ps                               # List running containers
docker ps -a                            # List all containers (including stopped)
docker exec -it my-nginx /bin/bash    # Enter container
docker logs my-nginx                   # View container logs
docker logs -f --tail 100 my-nginx  # Follow last 100 lines of logs
docker stop my-nginx                 # Stop container
docker start my-nginx                # Start a stopped container
docker rm my-nginx                  # Remove container (must stop first)
docker rm -f my-nginx                # Force remove (no need to stop first)

# Cleanup (use with caution!)
docker system prune -a                  # Remove unused images, containers, networks
```

### Phase 2: Dockerfile Writing (1 week)#

#### Minimal Dockerfile#

```dockerfile
# Dockerfile
FROM nginx:1.25
LABEL maintainer="vinson-lee"
COPY index.html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### Production-grade Dockerfile (Multi-stage Build)#

```dockerfile
# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Run (final image only has build artifacts, very small)
FROM nginx:1.25-alpine
COPY --from=builder /app/dist /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### Dockerfile Best Practices#

```dockerfile
# ✅ Recommended
FROM python:3.11-slim            # Use slim/alpine versions for smaller images
WORKDIR /app                     # Use WORKDIR, not RUN cd
COPY requirements.txt .           # Copy dependencies first (leverage cache)
RUN pip install -r requirements.txt
COPY . .                         # Copy code last (changes frequently)
RUN useradd -m app && chown -R app:app /app
USER app                           # Run as non-root user
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1   # Health check
EXPOSE 8080
CMD ["python", "app.py"]
```

### Phase 3: Docker Compose (1 week)#

#### Deploy LNMP with Compose#

```yaml
# docker-compose.yml
version: '3.8'

services:
  nginx:
    image: nginx:1.25
    container_name: lnmp-nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - ./html:/usr/share/nginx/html
    depends_on:
      - php
    networks:
      - lnmp-net:

  php:
    image: php:8.2-fpm
    container_name: lnmp-php
    volumes:
      - ./html:/var/www/html
    networks:
      - lnmp-net:

  mysql:
    image: mysql:8.0
    container_name: lnmp-mysql
    environment:
      MYSQL_ROOT_PASSWORD: "Root@123456"
      MYSQL_DATABASE: "wordpress"
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - lnmp-net:

  redis:
    image: redis:7-alpine
    container_name: lnmp-redis
    volumes:
      - redis-data:/data
    networks:
      - lnmp-net:

networks:
  lnmp-net:
    driver: bridge

volumes:
  mysql-data:
  redis-data:
```

```bash
# Start
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f

# Stop and remove containers
docker compose down

# Stop and remove containers + volumes (⚠️ Data loss!)
docker compose down -v
```

### Phase 4: Docker Networking (1 week)#

#### Four Network Modes#

| Mode | Description | Use Case |
|------|-------------|----------|
| bridge (default) | Container connects to docker0 bridge | Single-host container communication |
| host | Container shares Host network stack | Performance-critical (no NAT) |
| none | Container has no network interface | Security-sensitive scenarios |
| overlay | Cross-host container communication | Swarm/K8s clusters |

```bash
# Create custom network (recommended — containers communicate by service name)
docker network create my-net
docker run -d --name app1 --network my-net my-app
docker run -d --name app2 --network my-net my-app
# Now app1 can ping app2 directly (Docker built-in DNS)

# Inspect network
docker network inspect my-net
```

### Phase 5: Private Registry (3-5 days)#

#### Set up Harbor (Enterprise-grade)#

```bash
# 1. Download Harbor installer
wget https://github.com/goharbor/harbor/releases/download/v2.9.0/harbor-offline-installer-v2.9.0.tgz
tar -xf harbor-offline-installer-v2.9.0.tgz
cd harbor

# 2. Modify config
cp harbor.yml.tmpl harbor.yml
# Edit harbor.yml: configure hostname, https certs, admin password

# 3. Install
./install.sh

# 4. Access
# https://your-harbor-domain.com
# Default: admin / password from harbor.yml

# 5. Push image to Harbor
docker login your-harbor-domain.com
docker tag my-app:1.0 your-harbor-domain.com/library/my-app:1.0
docker push your-harbor-domain.com/library/my-app:1.0
```

---

## 💻 Practical Command Examples#

### Container Troubleshooting#

```bash
# 1. Container won't start — check why
docker logs <container-name>
docker inspect <container-name>       # View detailed container config

# 2. Container has no network access
docker exec -it <container-name> ping 8.8.8.8
docker exec -it <container-name> nslookup google.com
docker network inspect <network-name>

# 3. Container disk full
docker exec -it <container-name> df -h
# After finding large files, clean up or expand volume

# 4. View container resource usage
docker stats <container-name>
docker top <container-name>               # View processes inside container

# 5. Copy files (container ↔ host)
docker cp <container-name>:/var/log/app.log ./
docker cp ./config.conf <container-name>:/etc/app/
```

### Docker Cleanup (Ops Frequently Used)#

```bash
# Remove stopped containers
docker container prune -f

# Remove unused images
docker image prune -a -f

# Remove unused volumes (⚠️ Data loss!)
docker volume prune -f

# Nuclear option: remove EVERYTHING unused (⚠️⚠️⚠️)
docker system prune -a --volumes -f
```

---

## 🧪 Hands-on Projects#

### Project 1: Deploy WordPress with Docker Compose#

**Goal**: One command brings up the entire LNMP stack.

**Steps**:
1. Create `docker-compose.yml` (reference the LNMP example above, add WordPress)
2. `docker compose up -d`
3. Browser access `http://server-ip`, complete WordPress setup
4. Verify MySQL data persistence (delete container, data remains)

### Project 2: Write a Multi-stage Dockerfile#

**Goal**: Package a Node.js app into a minimal image.

**Requirements**:
1. Use multi-stage build (build stage: `node:18`, run stage: `nginx:alpine`)
2. Final image under 50MB
3. Run as non-root user
4. Add health check
5. Push to Aliyun Container Registry

---

## 🔧 Common Troubleshooting#

### Issue 1: Container Can't Access External Network#

**Troubleshooting**:
```bash
# 1. Check host network
ping -c 3 8.8.8.8

# 2. Check Docker DNS config
cat /etc/docker/daemon.json
# If no DNS configured, add:
# "dns": ["8.8.8.8", "114.114.114.114"]

# 3. Restart Docker
sudo systemctl restart docker
```

### Issue 2: Port Already in Use#

```bash
# Find process using the port
netstat -tlnp | grep :8080
# Or
lsof -i :8080

# Kill the process, or use a different host port
docker run -d -p 8081:80 nginx    # Use 8081 instead
```

### Issue 3: Image Pull is Too Slow#

**Fix**: Configure mirror acceleration (see Installation section above for `daemon.json` config).

---

## 💼 Interview Questions#

1. **Difference between Docker and VMs?**
   - See "Containers vs VMs" explanation above.

2. **Difference between `COPY` and `ADD` in Dockerfile?**
   - `COPY`: Just copies files.
   - `ADD`: Copies files + auto-extracts archives + supports URL (not recommended, behavior is opaque).

3. **Why run containers as non-root?**
   - If container is compromised, attacker only gets container user privileges, not Host root.

4. **Bridge vs Host network mode?**
   - `bridge`: Container has independent IP, accesses external network via NAT. Good isolation.
   - `host`: Container shares Host network. Better performance but no network isolation.

---

## 📈 Advanced Learning Path#

- **Docker Security**: Image scanning (Trivy), signing (Docker Content Trust)
- **Container Orchestration**: Learn Kubernetes (single-host Docker is limited)
- **Container Runtime**: Understand containerd, CRI-O (K8s 1.24+ no longer uses Docker as runtime)
- **Service Mesh**: Learn Istio (advanced container networking)

---

## 🔗 Related Resources#

- [← Back to EN Home](../README.md)
- [EN 03 Shell & Automation](../03_Shell_Automation/)
- [EN 05 Kubernetes](../05_Kubernetes/)
- [GitHub Trending: Docker Repos](../../resources/trending.md)

---

<p align="right">
  <sub>vinson-lee · Containerization is step one, K8s is the destination</sub>
</p>
