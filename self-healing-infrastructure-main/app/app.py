from flask import Flask, jsonify, render_template
import os
import time
import socket

app = Flask(__name__)

START_TIME = time.time()
REQUEST_COUNT = 0


@app.before_request
def count_request():
    global REQUEST_COUNT
    REQUEST_COUNT += 1


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        hostname=socket.gethostname(),
        uptime=int(time.time() - START_TIME),
        requests=REQUEST_COUNT
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "self-healing-app",
        "hostname": socket.gethostname()
    })


@app.route("/api/status")
def status():
    uptime = int(time.time() - START_TIME)

    return jsonify({
        "service": "self-healing-app",
        "status": "healthy",
        "hostname": socket.gethostname(),
        "uptime_seconds": uptime,
        "requests": REQUEST_COUNT,
        "auto_healing": True
    })


@app.route("/api/metrics")
def metrics():
    return jsonify({
        "requests": REQUEST_COUNT,
        "uptime_seconds": int(time.time() - START_TIME),
        "hostname": socket.gethostname()
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
