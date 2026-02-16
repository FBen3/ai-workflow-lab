from importlib.metadata import PackageNotFoundError, distribution
from datetime import datetime
from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/")
    def index():
        return "ai-workflow-lab: hello"

    @app.get("/version")
    def version():
        try:
            dist = distribution("ai-workflow-lab")
        except PackageNotFoundError:
            return jsonify(name=None, version=None)

        return jsonify(name=dist.metadata.get("Name"), version=dist.version)

    @app.get("/day")
    def day():
        return jsonify(day=datetime.now().strftime("%Y-%m-%d"))

    return app

if __name__ == "__main__":
    create_app().run(debug=True, port=8000)

