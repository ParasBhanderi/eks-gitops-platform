# EKS GitOps Platform

## Architecture

- Developer pushes code → GitHub
- ArgoCD detects changes
- Syncs Kubernetes manifests
- Deploys container automatically
- Health checks and self-healing

## Architecture Diagram

flowchart TB

subgraph L1[Source Control]
direction TB
Dev[Developer Laptop] -->|git push| GH[(GitHub Repo)]
end

subgraph L2[GitOps Control Plane]
direction TB
Argo[Argo CD]
end

GH -->|webhook or polling| Argo

subgraph L3[Kubernetes Cluster - Kind now, EKS later]
direction TB

subgraph NS1[Namespace argocd]
direction TB
ArgoSvc[Argo CD Services]
end

subgraph NS2[Namespace default]
direction TB
Kustomize[Kustomize Manifests] --> Deploy[Deployment sample-api]
Deploy --> RS[ReplicaSet]
RS --> Pods[(Pods)]
Pods --> Svc[Service ClusterIP port 80 to 8000]
end
end

Argo -->|sync manifests| Kustomize
Argo -->|health checks and self-heal| Pods

subgraph L4[Access and Testing]
direction TB
User[User or Tester]
PF[kubectl port-forward 18080 to service port 80]
Curl[curl localhost:18080/healthz]
end

User --> PF --> Svc
User --> Curl --> PF
