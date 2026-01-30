from importlib import metadata

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    def _package_info() -> dict[str, str]:
        dist_names = metadata.packages_distributions().get("ai_workflow_lab", [])
        dist_name = dist_names[0]
        dist = metadata.distribution(dist_name)
        return {"name": dist.metadata["Name"], "version": dist.version}

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/")
    def index():
        return "ai-workflow-lab: hello"

    @app.get("/version")
    def version():
        return jsonify(_package_info())

    return app

if __name__ == "__main__":
    create_app().run(debug=True, port=8000)
