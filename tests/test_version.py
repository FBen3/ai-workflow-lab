from ai_workflow_lab.app import create_app


def test_version():
    app = create_app()
    client = app.test_client()
    resp = client.get("/version")

    assert resp.status_code == 200
    assert resp.json == {"version": "0.1.0"}
