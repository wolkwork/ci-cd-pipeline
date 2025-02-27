"""
Mock smoke tests for template project.
"""

import os
from unittest import mock

import pytest


@pytest.mark.smoke
def test_service_health():
    """Test service health endpoint."""
    # Mock the service URL
    url = os.getenv("STAGING_URL", "https://staging-api.example.com/health")

    # In a real test, we would make an actual request to the service
    # For demonstration, we'll use a mock response
    with mock.patch("requests.get") as mock_get:
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "healthy"}
        mock_get.return_value = mock_response

        # Here could be the actual code for a real test, e.g.:
        # response = requests.get(f"{url}")
        # assert response.status_code == 200
        # health_data = response.json()
        # assert health_data["status"] == "healthy"

        # For demonstration, we'll just assert our mock was configured correctly
        assert mock_response.status_code == 200
        assert mock_response.json()["status"] == "healthy"
        mock_get.assert_not_called()  # Since we're not actually making the request
        print(f"Example action: GET {url}")


@pytest.mark.smoke
@pytest.mark.parametrize(
    "endpoint", ["users", "auth", "health", "status", "config", "metrics"]
)
def test_api_endpoint_availability(endpoint):
    """Test that each API endpoint is available and returns expected status code."""
    base_url = os.getenv("STAGING_URL", "https://staging-api.example.com")

    # In a real test, we would make actual requests to endpoints
    with mock.patch("requests.get") as mock_get:
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Here could be the actual code for a real test, e.g.:
        # response = requests.get(f"{base_url}/{endpoint}")
        # assert response.status_code in (200, 201, 204)

        # For demonstration, we'll just assert our mock was configured correctly
        assert mock_response.status_code == 200
        mock_get.assert_not_called()  # Since we're not actually making the request
        print(f"Example action: GET {base_url}/{endpoint}")


@pytest.mark.smoke
@pytest.mark.performance
def test_response_time():
    """Test that service response time is within acceptable limits."""
    url = os.getenv("STAGING_URL", "https://staging-api.example.com/health")
    max_response_time = 1.0  # seconds

    # In a real test, we would measure actual response time
    with mock.patch("requests.get") as mock_get:
        mock_response = mock.MagicMock()
        mock_response.elapsed.total_seconds.return_value = 0.123
        mock_get.return_value = mock_response

        # Here could be the actual code for a real test, e.g.:
        # start_time = time.time()
        # response = requests.get(url)
        # response_time = time.time() - start_time

        # For demonstration, we'll use the mock's elapsed time
        response_time = mock_response.elapsed.total_seconds()

        assert (
            response_time < max_response_time
        ), f"Response time {response_time}s exceeds maximum allowed {max_response_time}s"
        mock_get.assert_not_called()  # Since we're not actually making the request
        print(f"Example action: GET {url}")
