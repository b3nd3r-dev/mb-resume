# Kubernetes Setup

A secret key needs to be set up in production. Create a secret to be injested in the deployment and set to `SECRET_KEY`

```
kubectl create secret generic secretkey \
  --from-literal=key=XXXXXXX
```