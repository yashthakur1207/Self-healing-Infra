from flask import Flask, request, jsonify
import subprocess
import datetime
import os

app = Flask(__name__)

LOG_FILE = "/logs/self-healing.log"


def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    os.makedirs("/logs", exist_ok=True)

    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "self-healing-webhook"
    })


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json(silent=True) or {}

    alerts = data.get("alerts", [])

    write_log(
        f"ALERT RECEIVED | alert_count={len(alerts)}"
    )

    for alert in alerts:

        status = alert.get("status", "unknown")

        labels = alert.get("labels", {})

        annotations = alert.get("annotations", {})

        alert_name = labels.get(
            "alertname",
            "UnknownAlert"
        )

        severity = labels.get(
            "severity",
            "unknown"
        )

        summary = annotations.get(
            "summary",
            "No summary provided"
        )

        write_log(
            f"ALERT | name={alert_name} | "
            f"severity={severity} | "
            f"status={status} | "
            f"summary={summary}"
        )

        if status == "firing":

            write_log(
                f"ACTION | Starting Ansible healing "
                f"for {alert_name}"
            )

            try:

                result = subprocess.run(
                    [
                        "ansible-playbook",
                        "-i",
                        "/ansible/inventory.ini",
                        "/ansible/heal.yml",
                        "--extra-vars",
                        f"alert_name={alert_name}"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=120
                )

                write_log(
                    f"ANSIBLE | return_code={result.returncode}"
                )

                if result.stdout:
                    write_log(
                        f"ANSIBLE_OUTPUT | {result.stdout.strip()}"
                    )

                if result.stderr:
                    write_log(
                        f"ANSIBLE_ERROR | {result.stderr.strip()}"
                    )

            except Exception as error:

                write_log(
                    f"HEALING_ERROR | {str(error)}"
                )

    return jsonify({
        "status": "received",
        "alerts_processed": len(alerts)
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001
    )
