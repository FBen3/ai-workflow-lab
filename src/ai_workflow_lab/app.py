from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/version")
    def version():
        return jsonify(version="0.1.0")

    @app.get("/")
    def index():
        return "ai-workflow-lab: hello"

    return app

if __name__ == "__main__":
    create_app().run(debug=True, port=8000)

