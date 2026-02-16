from ai_workflow_lab.app import create_app
from datetime import datetime


def test_day():
    app = create_app()
    client = app.test_client()
    resp = client.get("/day")

    assert resp.status_code == 200
    assert resp.json == {"day": datetime.now().strftime("%Y-%m-%d")}
