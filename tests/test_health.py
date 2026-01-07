from ai_workflow_lab.app import create_app


def test_health():
    app = create_app()
    client = app.test_client()
    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json == {"status": "ok"}

