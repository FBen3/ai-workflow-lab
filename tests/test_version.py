from ai_workflow_lab.app import create_app


def test_version():
    app = create_app()
    client = app.test_client()
    resp = client.get("/version")

    assert resp.status_code == 200
    assert set(resp.json.keys()) == {"name", "version"}

