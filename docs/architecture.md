# EKS GitOps Platform

## Architecture

- Developer pushes code → GitHub
- ArgoCD detects changes
- Syncs Kubernetes manifests
- Deploys container automatically
- Health checks and self-healing

## Architecture Diagram

```mermaid
flowchart TD
  Dev[Developer] -->|git push| GH[(GitHub Repo)]
  GH -->|webhook / polling| Argo[Argo CD]

  subgraph Cluster[Kubernetes Cluster (Kind now → EKS later)]
    Argo -->|sync| K8s[Kubernetes Manifests (Kustomize)]
    K8s --> Deploy[Deployment: sample-api]
    Deploy --> Pods[Pods]
    Pods --> SVC[Service (ClusterIP)]
    Argo -->|health + self-heal| Pods
  end

  User[User / Tester] -->|kubectl port-forward| SVC
  User -->|GET /healthz| Pods



## Stack

- Docker
- Kubernetes (Kind → later EKS)
- ArgoCD
- GitOps
- FastAPI
```
