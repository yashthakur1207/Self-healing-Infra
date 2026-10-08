# 🔧 Self-Healing Infrastructure

### Automated Service Monitoring, Alerting and Recovery using Prometheus, Alertmanager, Ansible and Docker

![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker\&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus\&logoColor=white)
![Alertmanager](https://img.shields.io/badge/Alertmanager-Alerting-orange)
![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?logo=ansible\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-000000?logo=flask\&logoColor=white)
![Nginx](https://img.shields.io/badge/NGINX-Reverse%20Proxy-009639?logo=nginx\&logoColor=white)

---

## 📌 Project Overview

The **Self-Healing Infrastructure** project is an automated monitoring and recovery system designed to detect service failures and automatically restore affected services.

The project combines:

* **Docker** for containerization
* **Flask** for the application
* **NGINX** as a reverse proxy
* **Prometheus** for monitoring
* **Blackbox Exporter** for HTTP health checks
* **Alertmanager** for alert management
* **Webhook** for receiving alerts
* **Ansible** for automated recovery

The system follows a monitoring → alerting → automation → recovery workflow.

---

## 🎯 Objectives

The main objectives of this project are:

1. Monitor application and infrastructure services.
2. Detect service failures automatically.
3. Generate alerts when a monitored service becomes unavailable.
4. Forward alerts to an automation webhook.
5. Execute Ansible recovery playbooks automatically.
6. Restart failed Docker containers.
7. Verify that the service has recovered.
8. Maintain logs of the self-healing process.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │     Flask App       │
                    │      Port 5000      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       NGINX         │
                    │      Port 8081      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Blackbox Exporter  │
                    │      Port 9115      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Prometheus      │
                    │      Port 9090      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Alertmanager     │
                    │      Port 9094      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Healing Webhook   │
                    │      Port 5001      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Ansible       │
                    │   Recovery Playbook │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Docker Restart    │
                    │   Failed Service    │
                    └─────────────────────┘
```

---

## 🔄 Self-Healing Workflow

```text
Service Running
      │
      ▼
Health Check
      │
      ▼
Prometheus Monitoring
      │
      ├── Healthy ──────────────► Continue Monitoring
      │
      ▼
Service Failure
      │
      ▼
Prometheus Detects Failure
      │
      ▼
Alertmanager
      │
      ▼
Webhook
      │
      ▼
Ansible Playbook
      │
      ▼
Docker Container Restart
      │
      ▼
Health Check
      │
      ▼
Service Recovered
```

---

## 🛠️ Technologies Used

| Technology        | Purpose                                 |
| ----------------- | --------------------------------------- |
| Docker            | Containerization and service management |
| Docker Compose    | Multi-container orchestration           |
| Python            | Application and webhook development     |
| Flask             | Web application framework               |
| NGINX             | Reverse proxy                           |
| Prometheus        | Monitoring and alert evaluation         |
| Blackbox Exporter | HTTP endpoint health monitoring         |
| Alertmanager      | Alert routing                           |
| Ansible           | Automated service recovery              |
| Bash              | Utility and management scripts          |
| Git               | Version control                         |
| GitHub            | Source code hosting                     |

---

## 📁 Project Structure

```text
self-healing-infrastructure/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   │
│   ├── static/
│   │   └── style.css
│   │
│   └── templates/
│       └── dashboard.html
│
├── automation/
│   ├── ansible/
│   │   ├── heal.yml
│   │   └── inventory.ini
│   │
│   └── webhook/
│       ├── webhook.py
│       ├── requirements.txt
│       └── Dockerfile
│
├── docker/
│   ├── docker-compose.yml
│   └── nginx.conf
│
├── monitoring/
│   ├── alertmanager/
│   │   └── alertmanager.yml
│   │
│   ├── blackbox/
│   │   └── blackbox.yml
│   │
│   └── prometheus/
│       ├── prometheus.yml
│       └── alerts.yml
│
├── scripts/
│   ├── health-check.sh
│   ├── start.sh
│   └── stop-service.sh
│
├── logs/
│   ├── ansible-healing.log
│   └── self-healing.log
│
└── README.md
```

---

# 🚀 Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/RajveerMistri/self-healing-infrastructure.git
```

Move into the project:

```bash
cd self-healing-infrastructure
```

---

## 2. Verify Docker

Check Docker:

```bash
docker --version
```

Check Docker Compose:

```bash
docker compose version
```

---

## 3. Validate Docker Compose Configuration

Run:

```bash
docker compose -f docker/docker-compose.yml config
```

A valid configuration should complete without YAML or Compose errors.

---

## 4. Start the Infrastructure

Run:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

Check running containers:

```bash
docker ps
```

The main services are:

```text
self-healing-app
self-healing-nginx
self-healing-prometheus
self-healing-blackbox
self-healing-alertmanager
self-healing-webhook
```

---

# 🌐 Service Endpoints

When running locally:

| Service           | URL                   |
| ----------------- | --------------------- |
| Flask Application | http://localhost:8081 |
| Prometheus        | http://localhost:9090 |
| Blackbox Exporter | http://localhost:9115 |
| Alertmanager      | http://localhost:9094 |
| Webhook           | http://localhost:5001 |

Application API endpoints:

```text
/
 /health
 /api/status
 /api/metrics
```

---

# 📊 Monitoring

Prometheus monitors the infrastructure using **Blackbox Exporter**.

The monitored HTTP endpoints are:

```text
http://nginx/health
http://app:5000/health
http://webhook:5001/health
```

Prometheus periodically checks these endpoints and evaluates alert rules.

---

# 🚨 Alert Rules

The project currently uses three primary alerts.

### ApplicationUnhealthy

Triggered when the Flask application's health endpoint becomes unavailable.

```yaml
alert: ApplicationUnhealthy
```

Severity:

```text
critical
```

---

### NginxDown

Triggered when NGINX becomes unavailable.

```yaml
alert: NginxDown
```

Severity:

```text
critical
```

This is the primary self-healing demonstration.

---

### WebhookDown

Triggered when the healing webhook becomes unavailable.

```yaml
alert: WebhookDown
```

Severity:

```text
warning
```

---

# 🤖 Automated Recovery

When an alert enters the firing state:

```text
Prometheus
     ↓
Alertmanager
     ↓
Webhook
     ↓
Ansible
     ↓
Docker Restart
```

The webhook extracts the alert name and executes:

```bash
ansible-playbook \
-i /ansible/inventory.ini \
/ansible/heal.yml \
--extra-vars "alert_name=<ALERT_NAME>"
```

For an NGINX failure, Ansible executes:

```bash
docker restart self-healing-nginx
```

The service is then checked again by Prometheus.

---

# 🧪 Self-Healing Test

A basic NGINX failure can be simulated with:

```bash
docker stop self-healing-nginx
```

Check the container:

```bash
docker ps
```

Prometheus detects the failed health check.

After the alert enters the firing state:

```text
Prometheus
    ↓
NginxDown
    ↓
Alertmanager
    ↓
Webhook
    ↓
Ansible
    ↓
docker restart self-healing-nginx
```

Check recovery:

```bash
docker ps
```

The NGINX container should be running again.

---

# 📝 Logs

The project maintains logs for the healing workflow.

### Webhook Log

```text
logs/self-healing.log
```

Example:

```text
[2026-09-20 17:36:30] ALERT RECEIVED | alert_count=1
[2026-09-20 17:36:30] ALERT | name=NginxDown | severity=critical | status=firing
[2026-09-20 17:36:30] ACTION | Starting Ansible healing for NginxDown
[2026-09-20 17:36:32] ANSIBLE | return_code=0
```

### Ansible Log

```text
logs/ansible-healing.log
```

Example:

```text
[HEALING] 2026-09-20 17:36:30 | Alert=NginxDown | Starting recovery
[HEALING] 2026-09-20 17:36:32 | Alert=NginxDown | Recovery completed
```

These logs provide evidence of automated recovery.

---

# 🔍 Useful Commands

### View all containers

```bash
docker ps
```

### View all containers including stopped containers

```bash
docker ps -a
```

### View project logs

```bash
docker compose -f docker/docker-compose.yml logs
```

### View a specific service

```bash
docker logs self-healing-nginx
```

```bash
docker logs self-healing-prometheus
```

```bash
docker logs self-healing-webhook
```

### Stop the complete infrastructure

```bash
docker compose -f docker/docker-compose.yml down
```

### Restart the infrastructure

```bash
docker compose -f docker/docker-compose.yml up -d
```

---

# 🩺 Health Check Script

The project includes:

```bash
scripts/health-check.sh
```

Make scripts executable if required:

```bash
chmod +x scripts/*.sh
```

Run:

```bash
./scripts/health-check.sh
```

The script checks the availability of the main infrastructure services.

---

# 🔐 Security Considerations

For a production deployment, the following improvements should be implemented:

* Use HTTPS/TLS.
* Secure the webhook endpoint.
* Avoid exposing Docker socket directly.
* Use restricted Docker permissions.
* Store credentials using secure secret management.
* Use authentication for monitoring dashboards.
* Restrict network access using firewall rules.
* Use pinned container image versions.

This project is intended as an educational demonstration of automated infrastructure recovery.

---

# 📈 Benefits

The self-healing approach can help reduce:

* Manual intervention
* Service downtime
* Recovery time
* Repetitive operational tasks

It demonstrates how monitoring and automation can work together to create an automated recovery workflow.

---

# 🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Containerization
* Docker Compose
* Infrastructure monitoring
* Health checks
* Alert-based automation
* Prometheus alert rules
* Alertmanager routing
* Webhook development
* Ansible automation
* Automated Docker recovery
* Bash scripting
* Git and GitHub
* DevOps monitoring and recovery concepts

---

# 🔮 Future Enhancements

Possible future improvements include:

* Kubernetes-based deployment
* Cloud deployment
* Grafana dashboards
* Slack/Email notifications
* Secure authentication
* More advanced service recovery
* Infrastructure-as-Code integration
* Centralized logging
* High-availability monitoring

---

# 👨‍💻 Author

**Rajveer Mistri**

GitHub:

https://github.com/RajveerMistri

Project Repository:

https://github.com/RajveerMistri/self-healing-infrastructure

---

# 📜 License

This project was developed for educational and academic purposes.

---

## ⭐ Project Summary

The project demonstrates a complete automated self-healing workflow:

```text
       ┌──────────────┐
       │    Service   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │  Monitoring  │
       │  Prometheus  │
       └──────┬───────┘
              │
         Failure Detected
              │
              ▼
       ┌──────────────┐
       │ Alertmanager │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │    Webhook   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │    Ansible   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ Docker Restart│
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │   Recovery   │
       └──────────────┘
```

**Detect → Alert → Automate → Recover → Verify**
