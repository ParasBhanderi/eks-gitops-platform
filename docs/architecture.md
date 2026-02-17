# EKS GitOps Platform

## Architecture

- Developer pushes code → GitHub
- ArgoCD detects changes
- Syncs Kubernetes manifests
- Deploys container automatically
- Health checks and self-healing

## Stack

- Docker
- Kubernetes (Kind → later EKS)
- ArgoCD
- GitOps
- FastAPI
