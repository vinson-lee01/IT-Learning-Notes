# 10 · Cloud Native & IaC

> Infrastructure as Code means: no manual changes, versioned config, reproducible environments.
> Cloud Native means: design for the cloud from day one, not migrate later.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- [ ] Understand IaC philosophy and why it matters
- [ ] Write Terraform configurations (HCL syntax)
- [ ] Manage Terraform state (local, remote, locking)
- [ ] Use Terraform modules (create and consume)
- [ ] Use Ansible for configuration management
- [ ] Understand Cloud Native patterns (12-factor app, microservices)
- [ ] Containerize apps properly (multi-stage Dockerfile)
- [ ] Use Helm for Kubernetes package management
- [ ] Implement GitOps (ArgoCD / Flux)
- [ ] Design for failure (circuit breaker, retry, timeout)

---

## 📺 Recommended Video Courses

| Course | Platform | Duration | Rating |
|--------|----------|----------|--------|
| **Terraform for Beginners** | TechWorld with Nana | YouTube | 2h | ⭐⭐⭐⭐⭐ |
| **Ansible Full Course** | FreeCodeCamp | YouTube | 3h | ⭐⭐⭐⭐ |
| **Terraform in Depth** | A Cloud Guru | Paid | 8h | ⭐⭐⭐⭐⭐ |
| **GitOps with ArgoCD** | Codefresh | YouTube | 1.5h | ⭐⭐⭐⭐ |

---

## 📖 Recommended Books

| Book | Author | Stage | Comment |
|------|--------|-------|---------|
| **Terraform: Up and Running (3rd ed)** | Yevgeniy Brikman | Advanced | The Terraform bible. Must-read. |
| **Ansible for DevOps** | Jeff Geerling | Intermediate | Free sample, great practical examples. |
| **Cloud Native Paterns** | Cornelia Davis | Advanced | Design paterns for cloud-native apps. |
| **The Twelve-Factor App** | Adam Wiggins | All | Short, foundational. Read it at https://12factor.net/ |
| **Production Kubernetes** | O'Reilly | Advanced | Running K8s in production, IaC included. |

---

## 🌐 Online Resources

| Resource | Link | Features |
|----------|------|----------|
| **Terraform Official Docs** | https://developer.hashicorp.com/terraform/docs | Authoritative |
| **Terraform Best Practices** | https://www.terraform-best-practices.com/ | Do's and don'ts |
| **Ansible Docs** | https://docs.ansible.com/ | Comprehensive |
| **ArgoCD Docs** | https://argo-cd.readthedocs.io/ | GitOps deployment |
| **12-Factor App** | https://12factor.net/ | Must-read, 15 min |
| **CNCF Landscape** | https://landscape.cncf.io/ | See the whole cloud-native ecosystem |
| **Terraform AWS Modules** | https://registry.terraform.io/modules/aws | Reusable modules |

---

## 📝 Core Knowledge Checklist

### Phase 1: IaC Fundamentals (1 week)

- What problem IaC solves: manual config drift, no versioning, unreproducible environments
- IaC tools comparison:

| Tool | Type | State | Use case |
|------|------|-------|----------|
| **Terraform** | Declarative | Yes (local/remote) | Provision infrastructure |
| **Ansible** | Imperative/Declarative | No | Configure OS/apps |
| **Pulumi** | Declarative (real code) | Yes | Same as Terraform, but with Python/TS |
| **CloudFormation** | Declarative | Yes | AWS-only |
| **ARM/Bicep** | Declarative | Yes | Azure-only |

- Immutable vs mutable infrastructure
- Idempotency: running the same code twice produces the same result

### Phase 2: Terraform — The Industry Standard (3 weeks)

#### Basic Terraform workflow
```bash
# Initialize (download providers)
terraform init

# Check what will be created/changed
terraform plan

# Apply changes
terraform apply  # type 'yes' to confirm

# Destroy infrastructure
terraform destroy
```

#### Basic `main.tf` structure
```hcl
# Specify provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure provider
provider "aws" {
  region = "us-east-1"
}

# Create a resource
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"  # Ubuntu 22.04
  instance_type = "t2.micro"

  tags = {
    Name = "web-server"
    Env  = "prod"
  }
}

# Output values
output "web_public_ip" {
  value = aws_instance.web.public_ip
}
```

#### Terraform state — the most important concept
- State file (`terraform.tfstate`) maps real-world resources to your config
- **Never** commit `terraform.tfstate` to Git
- Use remote state for team collaboration:

```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    dynamodb_table = "terraform-locks"  # state locking
  }
}
```

#### Variables and outputs
```hcl
# variables.tf
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

# Use it
resource "aws_instance" "web" {
  instance_type = var.instance_type
}

# outputs.tf
output "web_url" {
  value       = "http://${aws_instance.web.public_ip}"
  description = "Public URL of the web server"
}
```

#### Modules — reusable Terraform code
```hcl
# Call a module from registry
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my-vpc"
  cidr = "10.0.0.0/16"
}

# Create your own module
# File structure:
# my-module/
#   ├── main.tf
#   ├── variables.tf
#   ├── outputs.tf
#   └── versions.tf
```

#### Terraform best practices
- Use **remote state** with locking (S3 + DynamoDB for AWS)
- **Never** `terraform apply` in CI/CD without `plan` first
- Use **modules** for reusable logic (don't repeat yourself)
- Pin provider versions: `~> 5.0` not `">= 5.0"`
- Use **workspaces** for env separation (or better: separate state files per env)
- Review `terraform plan` output carefully before applying
- Use `terraform import` to bring existing resources under Terraform management

### Phase 3: Ansible — Configuration Management (2 weeks)

#### Basic Ansible playbook
```yaml
# site.yml
- name: Configure web servers
  hosts: webservers
  become: yes  # sudo
  
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
    
    - name: Start Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copy config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart Nginx
  
  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

#### Inventory file (`hosts.ini`)
```ini
[webservers]
10.0.1.10
10.0.1.11

[databases]
10.0.2.10

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/id_rsa
```

#### Running Ansible
```bash
# Check connectivity
ansible all -i hosts.ini -m ping

# Run a playbook
ansible-playbook -i hosts.ini site.yml

# Run only specific tags
ansible-playbook -i hosts.ini site.yml --tags "nginx,config"
```

#### Ansible best practices
- Use **roles** for organization (not flat playbooks)
- Store secrets in **Ansible Vault**, not plaintext
- Use **ansible-lint** in CI to catch errors early
- Prefer `apt`/`yum` modules over `command`/`shell`

### Phase 4: Cloud Native Design Paterns (2 weeks)

#### The 12-Factor App (read it!)
1. **Codebase**: One codebase, many deploys
2. **Dependencies**: Explicitly declare deps (no system-level deps)
3. **Config**: Store config in environment variables (not code!)
4. **Backing services**: Treat DB, cache as attached resources
5. **Build/Release/Run**: Strictly separate build and run stages
6. **Processes**: Execute as stateless processes
7. **Port binding**: Export services via port binding
8. **Concurrency**: Scale via process model
9. **Disposability**: Fast startup, graceful shutdown
10. **Dev/Prod parity**: Keep dev and prod as similar as possible
11. **Logs**: Treat logs as event streams (write to stdout)
12. **Admin processes**: Run admin tasks as one-off processes

#### Container best practices
- Use **multi-stage builds** to keep images small:
  ```dockerfile
  # Build stage
  FROM golang:1.21 AS builder
  WORKDIR /app
  COPY . .
  RUN go build -o myapp
  
  # Final stage (small!)
  FROM alpine:3.19
  COPY --from=builder /app/myapp /usr/local/bin/
  CMD ["myapp"]
  ```
- **Don't run as root** in containers
- **Always pin image tags** (not `latest`)
- **Scan images** for vulnerabilities (Trivy)

#### Designing for failure
- **Circuit breaker**: stop calling a failing service
- **Retry with exponential backoff**: `retry = base * 2^attempt`
- **Timeout**: never wait forever
- **Bulkhead**: isolate failures (one slow service shouldn't block others)
- **Health checks**: liveness (restart if stuck) vs readiness (receive traffic or not)

### Phase 5: GitOps — Git as the single source of truth (1 week)

#### What is GitOps?
- Git repo holds desired state
- Automated process syncs desired state → actual state
- Git commit = deployment (no manual `kubectl apply`)

#### ArgoCD — the most popular GitOps tool
```yaml
# Application manifest
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/myapp-manifests.git
    targetRevision: main
    path: overlays/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: prod
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Key ArgoCD features:
- **Auto-sync**: automatically apply changes from Git
- **Rollback**: one-click rollback to any previous version
- **App-of-Apps**: use ArgoCD to manage ArgoCD (bootstrap pattern)
- **Health status**: visual indicator of app health

---

## 🔬 Hands-on Projects

| Project | Difficulty | What you'll learn |
|---------|-------------|-------------------|
| **Provision AWS VPC + EC2 with Terraform** | ⭐⭐ | VPC, subnets, security groups, state management |
| **Configure EC2 with Ansible** | ⭐⭐ | Playbooks, inventory, roles |
| **Multi-stage Dockerfile + push to ECR** | ⭐⭐⭐ | Optimized images, registry auth |
| **Set up ArgoCD on K8s** | ⭐⭐⭐ | GitOps workflow end-to-end |
| **Terraform + Helm to deploy app to K8s** | ⭐⭐⭐⭐ | Best practice: Terraform manages infra, Helm manages apps |
| **Implement circuit breaker with Istio** | ⭐⭐⭐⭐⭐ | Service mesh, failure handling |

---

## ⚠️ Common Pitfalls

| Pitfall | Why it happens | How to avoid |
|---------|----------------|---------------|
| Committing Terraform state to Git | Forgot `.gitignore` | Always `.gitignore terraform.tfstate*` |
| Hardcoding secrets in Terraform | Convenient, wrong | Use AWS Secrets Manager, SSM Parameter Store |
| `terraform apply` without `plan` | In a hurry | Always CI/CD: plan → review → apply |
| No state locking | Multiple people running Terraform | Use DynamoDB table for locking |
| Ansible Vault password in Git | "I'll remove it later" | Never. Use CI/CD variable for vault password |
| Over-complicated Terraform modules | Trying to make them "universal" | Keep modules simple, compose them |

---

## ✅ Self-Check: Can you...

- [ ] Write a Terraform config that creates a VPC, subnet, and EC2 instance?
- [ ] Explain the difference between Terraform and Ansible?
- [ ] Set up remote state with locking?
- [ ] Write an Ansible playbook that installs and configures Nginx?
- [ ] Explain what GitOps is and why it's better than `kubectl apply`?
- [ ] List at least 5 of the 12-factor app principles?

> 💡 **Next step**: After this module, move on to **11 · SRE Handbook** to learn the SRE philosophy and practices.
