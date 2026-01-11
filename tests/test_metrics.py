import time

from ai_workflow_lab.app import create_app


def test_metrics_response_structure():
    app = create_app()
    client = app.test_client()
    resp = client.get("/metrics")

    assert resp.status_code == 200
    assert "uptime" in resp.json
    assert "requests" in resp.json


def test_metrics_uptime():
    app = create_app()
    client = app.test_client()

    # First request
    resp = client.get("/metrics")
    uptime1 = resp.json["uptime"]

    # Wait a moment
    time.sleep(1)

    # Second request
    resp = client.get("/metrics")
    uptime2 = resp.json["uptime"]

    # Uptime should have increased
    assert uptime2 >= uptime1
    assert isinstance(uptime1, int)
    assert isinstance(uptime2, int)


def test_metrics_request_count():
    app = create_app()
    client = app.test_client()

    # First request to /metrics
    resp = client.get("/metrics")
    count1 = resp.json["requests"]

    # Make some additional requests
    client.get("/health")
    client.get("/version")

    # Check metrics again
    resp = client.get("/metrics")
    count2 = resp.json["requests"]

    # Request count should have increased
    # count1 is 1 (the first /metrics call)
    # Then we make /health, /version, and another /metrics
    # So count2 should be count1 + 3
    assert count2 > count1
    assert count2 == count1 + 3
