# EKS GitOps Platform

## Architecture

- Developer pushes code → GitHub
- ArgoCD detects changes
- Syncs Kubernetes manifests
- Deploys container automatically
- Health checks and self-healing

## Architecture Diagram

```mermaid
flowchart LR
  Dev[Developer] -->|git push| GH[(GitHub Repo)]
  GH -->|webhook / polling| Argo[Argo CD]

  subgraph K8S[Kubernetes Cluster (Kind now → EKS later)]
    direction TB
    Argo --> Kustomize[Kustomize Manifests]
    Kustomize --> Deploy[Deployment: sample-api]
    Deploy --> Pods[(Pods)]
    Pods --> Svc[Service: ClusterIP]
    Argo -->|health checks + self-heal| Pods
  end

  User[User / Tester] -->|kubectl port-forward| Svc
  User -->|GET /healthz| Pods
```
