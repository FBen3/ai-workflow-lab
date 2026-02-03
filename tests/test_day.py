from ai_workflow_lab.app import create_app


def test_day():
    app = create_app()
    client = app.test_client()
    resp = client.get("/day")

    assert resp.status_code == 200
    assert "day" in resp.json
    assert resp.json["day"] in {
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    }
