import pytest
from sample_app.bin.create_app import create_app
import psycopg2

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

# https://medium.com/@mariusz.raczynski2/pytest-mock-how-to-mock-your-database-connection-5c84a5a0bfc3
# FILE: tests/unit/conftest.py
#requires pytest-mock, pytest-docker plugins

@pytest.fixture(scope='session')
def db_connection(docker_services, docker_ip):
    """
    :param docker_services: pytest-docker plugin fixture
    :param docker_ip: pytest-docker plugin fixture
    :return: psycopg2 connection class
    """
    db_settings = {
        'database'        : 'test_database',
        'user'            : 'postgres',
        'host'            : docker_ip,
        'password'        : '',
        'port'            : docker_services.port_for('database', 5432),
        'application_name': 'your-app'
    }
    dbc = psycopg2.connect(**db_settings)
    dbc.autocommit = True
    return dbc


@pytest.fixture(autouse=True)
def _mock_db_connection(mocker, db_connection):
    """
    This will alter application database connection settings, once and for all the tests
    in unit tests module.
    :param mocker: pytest-mock plugin fixture
    :param db_connection: connection class
    :return: True upon successful monkey-patching
    """
    mocker.patch('db.database.dbc', db_connection)
    return True

