#!/bin/bash

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "======================================"
echo " Starting Self-Healing Infrastructure"
echo "======================================"

docker compose -f docker/docker-compose.yml up -d --build

echo
echo "Infrastructure started successfully."
echo
echo "Application : http://localhost:8081"
echo "Prometheus  : http://localhost:9090"
echo "Alertmanager: http://localhost:9093"
echo "Blackbox    : http://localhost:9115"
echo "Webhook     : http://localhost:5001"
