import os
import threading
import time
from importlib import metadata

from flask import Flask, jsonify, request

PACKAGE_DISTRIBUTION = "ai-workflow-lab"


def get_package_info() -> dict[str, str]:
    distribution = metadata.distribution(PACKAGE_DISTRIBUTION)
    return {"name": distribution.metadata["Name"], "version": distribution.version}


def create_app() -> Flask:
    app = Flask(__name__)

    app_start_time = time.monotonic()
    request_count = 0
    count_lock = threading.Lock()

    @app.before_request
    def count_request():
        nonlocal request_count
        if request.path != "/metrics":
            with count_lock:
                request_count += 1

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/")
    def index():
        return "ai-workflow-lab: hello"

    @app.get("/version")
    def version():
        return jsonify(get_package_info())

    @app.get("/metrics")
    def metrics():
        uptime = int(time.monotonic() - app_start_time)
        return jsonify(uptime=uptime, requests=request_count)

    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    create_app().run(debug=True, port=port)
