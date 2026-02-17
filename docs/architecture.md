# EKS GitOps Platform

## Architecture

- Developer pushes code → GitHub
- ArgoCD detects changes
- Syncs Kubernetes manifests
- Deploys container automatically
- Health checks and self-healing

## Architecture Diagram

```mermaid
flowchart TB

%% ===== LAYER: SOURCE CONTROL =====
subgraph L1[Source Control / CI Trigger]
  direction TB
  Dev[Developer Laptop] -->|git push| GH[(GitHub Repo)]
end

%% ===== LAYER: GITOPS CONTROLLER =====
subgraph L2[GitOps Control Plane]
  direction TB
  Argo[Argo CD]
end

GH -->|webhook / polling| Argo

%% ===== LAYER: CLUSTER =====
subgraph L3[Kubernetes Cluster (Kind now → EKS later)]
  direction TB

  subgraph NS1[Namespace: argocd]
    direction TB
    ArgoSvc[Argo CD Services]
  end

  subgraph NS2[Namespace: default]
    direction TB
    Kustomize[Kustomize Manifests] --> Deploy[Deployment: sample-api]
    Deploy --> RS[ReplicaSet]
    RS --> Pods[(Pods)]
    Pods --> Svc[Service: ClusterIP :80 → 8000]
  end
end

Argo -->|sync manifests| Kustomize
Argo -->|health checks + self-heal| Pods

%% ===== LAYER: ACCESS / TESTING =====
subgraph L4[Access / Testing]
  direction TB
  User[User / Tester]
  PF[kubectl port-forward :18080 → svc/sample-api:80]
  Curl[curl http://localhost:18080/healthz]
end

User --> PF --> Svc
User --> Curl --> PF
```
