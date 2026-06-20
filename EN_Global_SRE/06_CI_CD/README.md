# 06 · CI/CD Pipelines

> Ship software safely, frequently, and automatically. From commit to production in minutes, not weeks.

---

## 🎯 Learning Objectives

- [ ] Build Jenkins pipelines (Declarative + Scripted)
- [ ] Configure GitLab CI with .gitlab-ci.yml
- [ ] Use GitHub Actions for cloud-native CI
- [ ] Implement deployment strategies (blue-green, canary, rolling)

---

## 🌐 Key Resources

| Resource | Link | Notes |
|----------|------|-------|
| Jenkins Pipeline Docs | https://www.jenkins.io/doc/book/pipeline | Official |
| GitLab CI Docs | https://docs.gitlab.com/ee/ci | Official |
| GitHub Actions Docs | https://docs.github.com/en/actions | Official |
| ArgoCD | https://argo-cd.readthedocs.io | GitOps CD |
| Tekton | https://tekton.dev | Cloud-native CI/CD |

---

## 📝 Deployment Strategies

```
BLUE-GREEN              CANARY                  ROLLING
────────────           ────────────            ────────────
  ┌─────┐                ┌─────┐                ┌─┐┌─┐┌─┐
  │ BLUE │ ──switch──▶   │     │  5% traffic    │ ││ ││ │
  └─────┘                │     │    ┌─┐          └─┘└─┘└─┘
  ┌──────┐               │     │────│ │ 95%      ┌─┐
  │GREEN │               │     │    └─┘          │ │ new
  └──────┘               └─────┘    new          └─┘ batch
 Instant switch         Gradual rollout        One-by-one
```

### Jenkins Pipeline (Declarative)
```groovy
pipeline {
    agent any
    stages {
        stage('Build')  { steps { sh 'docker build -t app .' } }
        stage('Test')   { steps { sh 'npm test' } }
        stage('Deploy') {
            when { branch 'main' }
            steps { sh 'kubectl apply -f k8s/' }
        }
    }
}
```

### GitHub Actions
```yaml
name: CI/CD
on: push
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/build-push-action@v5
        with: { push: true, tags: app:latest }
```

---

[← Back to English Home](../README.md)
