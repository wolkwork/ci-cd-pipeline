"""
Simple application module.
"""

import os
from typing import Dict


def get_config() -> Dict[str, str]:
    """
    Get application configuration.

    Returns:
        Dict containing configuration values
    """
    return {"environment": os.getenv("APP_ENV", "development"), "version": "0.1.0"}


def hello(name: str = "World") -> str:
    """
    Return a greeting message.

    Args:
        name: Name to greet

    Returns:
        Greeting message
    """
    if not name:
        raise ValueError("Name cannot be empty")

    return f"Hello, {name}!"


def main() -> None:
    """Main function."""
    config = get_config()
    print(f"Starting application in {config['environment']} mode")
    print(hello())


if __name__ == "__main__":
    main()
