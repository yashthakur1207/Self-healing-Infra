#!/bin/bash

set -e

SERVICE="${1:-nginx}"

echo "======================================"
echo " Self-Healing Failure Simulation"
echo "======================================"

echo
echo "Stopping service: $SERVICE"
echo

case "$SERVICE" in

    nginx)
        docker stop self-healing-nginx
        ;;

    app)
        docker stop self-healing-app
        ;;

    webhook)
        docker stop self-healing-webhook
        ;;

    *)
        echo "Unknown service: $SERVICE"
        echo
        echo "Usage:"
        echo "  ./scripts/stop-service.sh nginx"
        echo "  ./scripts/stop-service.sh app"
        echo "  ./scripts/stop-service.sh webhook"
        exit 1
        ;;

esac

echo
echo "Failure simulation completed."
echo "The monitoring system should detect the failure."
