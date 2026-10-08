#!/bin/bash

echo "======================================"
echo " Self-Healing Infrastructure Check"
echo "======================================"

echo
echo "[1] Application"
curl -fsS http://localhost:8081/health

echo
echo
echo "[2] Prometheus"
curl -fsS http://localhost:9090/-/healthy

echo
echo
echo "[3] Alertmanager"
curl -fsS http://localhost:9094/-/healthy

echo
echo
echo "[4] Blackbox Exporter"
curl -fsS http://localhost:9115/-/healthy

echo
echo
echo "[5] Webhook"
curl -fsS http://localhost:5001/health

echo
echo
echo "======================================"
echo " Health checks completed"
echo "======================================"
