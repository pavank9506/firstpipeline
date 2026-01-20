# python - CI/CD with GitHub Actions

A comprehensive CI/CD pipeline project demonstrating Flask application deployment with security scanning, image signing, and Kubernetes orchestration.

## 📋 Overview

This project implements a complete DevOps pipeline including:
- ✅ Unit & Integration Testing
- ✅ Code Coverage Analysis (80% minimum)
- ✅ Docker Image Building & Signing (Cosign)
- ✅ SBOM Generation (Syft)
- ✅ Vulnerability Scanning (Trivy)
- ✅ Kubernetes Deployment
- ✅ Image Signature Verification (OPA/Gatekeeper)

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker
- Git
- kubectl (for Kubernetes deployment)

### Local Setup

```bash
# Clone repository
git clone <repo-url>
cd firstpipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
pip install coverage pytest

# Run tests
python -m unittest discover -s . -p "test_*.py" -v

# Run with coverage
coverage run -m unittest test_app.py
coverage report -m --fail-under=80
```

## 📦 Project Structure

```
firstpipeline/
├── .github/
│   └── workflows/
│       └── deploy.yml           # CI/CD workflow
├── app.py                        # Flask application
├── test_app.py                   # Unit & Integration tests
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker image definition
├── kyverno-policy.yaml          # Kyverno image verification
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🔄 CI/CD Pipeline

### Jobs

#### 1. Test Job
- Checkout code
- Setup Python 3.9
- Install dependencies
- Generate SBOM (source)
- Run unit tests (80% coverage minimum)
- Run integration tests
- Deploy Flask app locally

#### 2. Docker Build Job
- Build Docker image
- Push to Docker Hub
- Generate SBOM (Docker image)
- Scan with Trivy for vulnerabilities
- Sign image with Cosign
- Upload artifacts

#### 3. Kubernetes Deploy Job
- Install OPA/Gatekeeper
- Apply image verification policies
- Deploy to production cluster
- Verify deployment

## 🧪 Testing

### Unit Tests
```bash
python -m unittest test_app.py
```

### Integration Tests
```bash
python -m unittest discover -s . -p "test_*.py" -v
```

### Coverage Report
```bash
coverage run -m unittest test_app.py
coverage report -m --fail-under=80
coverage html  # Generates htmlcov/index.html
```

## 🐳 Docker

### Build Image
```bash
docker build -t pavan095/github_action_docker:latest .
```

### Run Container
```bash
docker run -d -p 5000:5000 pavan095/github_action_docker:latest
curl http://localhost:5000/
```

## 🔐 Security

### Image Signing (Cosign)
- Keyless signing via Sigstore
- Signature verification in Kubernetes
- OPA/Gatekeeper enforces signed images only

### Vulnerability Scanning (Trivy)
- Scans Docker images for CVEs
- Generates SARIF reports
- Uploads to GitHub Security tab

### SBOM Generation (Syft)
- Creates Software Bill of Materials
- SPDX-JSON format
- Tracks dependencies

## ☸️ Kubernetes Deployment

### OPA Policy
Blocks unsigned images from deployment:
```bash
kubectl apply -f opa-policy.yaml
```

### Deploy Application
```bash
kubectl set image deployment/firstpipeline firstpipeline=pavan095/github_action_docker:latest -n production
kubectl rollout status deployment/firstpipeline -n production
```

### Verify Deployment
```bash
kubectl get pods -n production
kubectl get svc -n production
```

## 📊 Artifacts

Generated artifacts in each workflow run:
- `sbom-source` — Source code SBOM
- `sbom` — Docker image SBOM
- `coverage-report` — HTML coverage report
- `trivy-results.sarif` — Vulnerability scan results

## 🔑 Required GitHub Secrets

```
DOCKER_USERNAME      — Docker Hub username
DOCKER_PASSWORD      — Docker Hub access token
KUBE_CONFIG          — Base64-encoded kubeconfig file
```

### Add Secrets
```bash
# Encode kubeconfig
cat ~/.kube/config | base64 -w 0

# Add to GitHub → Settings → Secrets and variables → Actions
```

## 📝 Configuration Files

### requirements.txt
```
Flask==2.3.0
```

### Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🚨 Troubleshooting

### Coverage < 80%
Ensure all code paths are tested:
```bash
coverage report -m  # Shows uncovered lines
```

### Cosign Signing Fails
Clear cache and retry:
```bash
rm -rf ~/.sigstore ~/.cache/sigstore
```

### Kubernetes Deploy Fails
Verify kubeconfig:
```bash
kubectl cluster-info
kubectl get nodes
```

## 📚 References

- [GitHub Actions](https://docs.github.com/actions)
- [Cosign Documentation](https://docs.sigstore.dev/cosign/overview/)
- [Trivy Scanner](https://github.com/aquasecurity/trivy)
- [OPA/Gatekeeper](https://open-policy-agent.github.io/gatekeeper/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 👤 Author

 (pavan095)

## 📄 License

This project is open source and available under the MIT License.

---

**Last Updated:** January 20, 2026
