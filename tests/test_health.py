# test_health.py
import pytest
from app import create_app

@pytest.fixture
def client():
    """
    A Pytest fixture that sets up a test client for a Flask application.

    This fixture creates a test client for a Flask application created by `create_app()` and configures
    it for testing purposes. It sets the application context and yields the test client for use in
    test cases.

    Usage:
    ```
    def test_example(client):
        # Use the `client` fixture to make test requests to the Flask application.
        response = client.get('/example-route')
        assert response.status_code == 200
    ```
    """
    app = create_app()
    app.app.testing = True
    with app.app.app_context():
        with app.test_client() as client:
            yield client

def test_health_check(client):
    """ Test the health check endpoint. """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}