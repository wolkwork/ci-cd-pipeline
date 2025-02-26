"""
Mock smoke tests for template project.
"""

import os
import time

import pytest


def test_mock_service_health():
    """Dummy test that always passes for CI/CD demonstration."""
    # Get staging URL or use a mock URL
    url = os.getenv("STAGING_URL", "https://staging-api.example.com/health")

    # Simulate checking the service
    print(f"[DUMMY] Checking service health at {url}")
    time.sleep(1)

    # This test will always pass for demonstration purposes
    pytest.assume(True, "Dummy health check passed")


def test_mock_api_endpoints():
    """Dummy test for API endpoints that always passes."""
    # Simulate checking API endpoints
    print("[DUMMY] Verifying API endpoints...")
    time.sleep(1)

    # Simulate checking specific endpoints
    endpoints = ["users", "auth", "health", "status", "config", "metrics"]
    for endpoint in endpoints:
        print(f"[DUMMY] Checking endpoint: {endpoint}")
        time.sleep(0.5)

    # This test will always pass for demonstration purposes
    pytest.assume(True, "Dummy API endpoint check passed")


def test_mock_response_time():
    """Dummy test for service response time that always passes."""
    print("[DUMMY] Measuring service response time...")
    time.sleep(1)

    # Simulate a response time measurement
    mock_response_time = 0.123  # seconds
    print(f"[DUMMY] Response time: {mock_response_time}s")

    # This test will always pass for demonstration purposes
    pytest.assume(mock_response_time < 1.0, "Dummy response time check passed")
