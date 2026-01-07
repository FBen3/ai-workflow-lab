from importlib import metadata

from flask import Flask, jsonify

PACKAGE_DISTRIBUTION = "ai-workflow-lab"


def get_package_info() -> dict[str, str]:
    distribution = metadata.distribution(PACKAGE_DISTRIBUTION)
    return {"name": distribution.metadata["Name"], "version": distribution.version}


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
        return jsonify(get_package_info())

    return app

if __name__ == "__main__":
    print("Ben")
    create_app().run(debug=True, port=8000)
