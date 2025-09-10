# K8s-Assignment

---

# Commands for `flask-app`

### 1. Build Docker Image

```
docker build -t lokeshbnr/flask-app:1.0 .
```

### 2. Push Image to Docker Hub

```
docker push lokeshbnr/flask-app:1.0
```

---

### 3. Apply Kubernetes Resources


```
kubectl apply -f namespace.yaml
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

### 4. Check Deployment

```
kubectl get pods -n flask-namespace
kubectl get svc -n flask-namespace
kubectl get deployments -n flask-namespace
```

---

### 5. Access App in Browser


```
kubectl port-forward svc/flask-service 8080:80 -n flask-namespace
```

[http://localhost:8080](http://localhost:8080)

