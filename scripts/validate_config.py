#!/usr/bin/env python
"""
Mock configuration validation script for ci/cd pipeline template project.
Normally this would include actual pre-deployment validations.
"""
import os
import sys
import time


def validate_environment():
    """
    Dummy validation of environment configuration.
    For template purposes, this will always succeed but show informative messages.

    Returns:
        Always returns True for template demonstration
    """
    print("Validating environment for deployment...")

    # List environment variables that would normally be required
    required_vars = ["DEPLOY_TOKEN", "STAGING_URL"]

    # Check which variables are actually set
    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        print(
            f"Note: The following variables would normally be required: {', '.join(missing)}"
        )
        print("For this template project, dummy values will be used.")
    else:
        print("All required environment variables are set.")

    # Simulate validations that could normally be done in a real deployment
    print("Running configuration validation checks...")
    time.sleep(1)
    print("Checking API access...")
    time.sleep(1)
    print("Validating permissions...")
    time.sleep(1)

    print("Environment validation passed!")
    return True


if __name__ == "__main__":
    # For template purposes, this will always succeed
    validate_environment()

    print("Configuration valid, ready for deployment!")
    sys.exit(0)
