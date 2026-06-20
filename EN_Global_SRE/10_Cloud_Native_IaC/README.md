# 10 · Cloud Native & IaC

> Infrastructure as Code is the foundation of cloud-native operations. Terraform provisions, Ansible configures, and Kubernetes runs.

---

## 🎯 Learning Objectives

- [ ] Provision cloud resources with Terraform
- [ ] Automate server configuration with Ansible
- [ ] Understand GitOps and declarative infrastructure
- [ ] Explore service mesh patterns with Istio

---

## 🌐 Key Resources

| Resource | Link | Notes |
|----------|------|-------|
| Terraform Docs | https://developer.hashicorp.com/terraform | Official |
| Terraform Registry | https://registry.terraform.io | Modules & providers |
| Ansible Docs | https://docs.ansible.com | Official |
| Ansible Galaxy | https://galaxy.ansible.com | Roles |
| Istio Docs | https://istio.io/latest/docs | Service mesh |
| AWS Well-Architected | https://aws.amazon.com/architecture/well-architected | Best practices |

---

## 📝 Terraform: Core Concepts

```hcl
# Provider
provider "aws" {
  region = "us-east-1"
}

# Resource
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}

# Module
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
  cidr    = "10.0.0.0/16"
}

# State: NEVER commit terraform.tfstate to git!
# Use remote backends: S3 + DynamoDB, Terraform Cloud, etc.
```

### State Management
- `terraform plan` — dry-run changes
- `terraform apply` — provision
- `terraform destroy` — tear down
- Remote state with locking (S3 + DynamoDB)
- Workspaces for multi-environment

### Ansible: Key Concepts
- **Idempotency** — run once or 100 times, same result
- **Inventory** — static or dynamic (cloud plugins)
- **Playbooks** — YAML-based automation
- **Roles** — reusable, opinionated structure
- **Vault** — encrypt secrets

---

## 📖 Books

| Title | Author |
|-------|--------|
| Terraform: Up & Running (3rd Ed.) | Yevgeniy Brikman |
| Ansible for DevOps | Jeff Geerling |
| Infrastructure as Code (2nd Ed.) | Kief Morris |
| Cloud Native DevOps with Kubernetes | John Arundel |

---

[← Back to English Home](../README.md)
