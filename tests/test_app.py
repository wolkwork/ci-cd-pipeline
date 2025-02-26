"""
Tests for app module.
"""

import os
from unittest import mock

import pytest

from src.app import get_config, hello


def test_hello_default():
    """Test hello function with default argument."""
    result = hello()
    pytest.assume(result == "Hello, World!")


def test_hello_custom_name():
    """Test hello function with custom name."""
    result = hello("GitHub")
    pytest.assume(result == "Hello, GitHub!")


def test_hello_empty_name():
    """Test hello function raises ValueError with empty name."""
    with pytest.raises(ValueError, match="Name cannot be empty"):
        hello("")


def test_get_config_default():
    """Test get_config with default environment."""
    with mock.patch.dict(os.environ, {}, clear=True):
        config = get_config()
        pytest.assume(config["environment"] == "development")
        pytest.assume(config["version"] == "0.1.0")


def test_get_config_custom_env():
    """Test get_config with custom environment."""
    with mock.patch.dict(os.environ, {"APP_ENV": "staging"}, clear=True):
        config = get_config()
        pytest.assume(config["environment"] == "staging")
