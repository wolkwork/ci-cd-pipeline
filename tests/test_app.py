"""
Tests for app module.
"""

import os
from unittest import mock

import pytest

from src.app import get_config, hello


@pytest.mark.unit
@pytest.mark.parametrize(
    "name,expected",
    [
        (None, "Hello, World!"),
        ("GitHub", "Hello, GitHub!"),
    ],
)
def test_hello(name, expected):
    """Test hello function with various inputs."""
    result = hello(name)
    assert result == expected


@pytest.mark.unit
def test_hello_empty_name():
    """Test hello function raises ValueError with empty name."""
    with pytest.raises(ValueError, match="Name cannot be empty"):
        hello("")


@pytest.mark.config
def test_default_environment():
    """Test get_config with default environment."""
    with mock.patch.dict(os.environ, {}, clear=True):
        config = get_config()
        assert config["environment"] == "development"
        assert config["version"] == "0.1.0"


@pytest.mark.config
def test_custom_environment():
    """Test get_config with custom environment."""
    with mock.patch.dict(os.environ, {"ENVIRONMENT": "production"}, clear=True):
        config = get_config()
        assert config["environment"] == "production"
