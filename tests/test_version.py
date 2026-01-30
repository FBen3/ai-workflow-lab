from importlib import metadata

from ai_workflow_lab.app import create_app


def test_version():
    dist_names = metadata.packages_distributions().get("ai_workflow_lab", [])
    dist_name = dist_names[0]
    dist = metadata.distribution(dist_name)

    app = create_app()
    client = app.test_client()
    resp = client.get("/version")

    assert resp.status_code == 200
    assert resp.json == {"name": dist.metadata["Name"], "version": dist.version}
