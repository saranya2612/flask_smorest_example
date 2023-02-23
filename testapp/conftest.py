import pytest
from sample_app.bin.create_app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True})
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_request_example(client):
    response = client.get("/")
    assert b"<h1>Home Page</h1><p>This is the home page of test application</p>" in response.data