#!/usr/bin/env python
"""
Mock deployment script for template project.
"""
import argparse
import os
import sys
import time


def deploy(environment):
    """
    Simulate deployment to the specified environment without requiring actual endpoints.

    Args:
        environment: The environment to deploy to (staging or production)

    Returns:
        True if dummy deployment was successful, False otherwise
    """
    if environment not in ["staging", "production"]:
        print(f"Invalid environment: {environment}")
        return False

    # For template purposes, we'll consider DEPLOY_TOKEN optional
    token = os.getenv("DEPLOY_TOKEN", "dummy-token-for-demo")
    if token == "dummy-token-for-demo":
        print("Note: Using dummy deployment token")

    # Use a dummy URL for demonstration
    deploy_url = os.getenv(
        f"{environment.upper()}_URL", f"https://{environment}-example.com"
    )
    print(f"[DUMMY] Deploying to {environment} at {deploy_url}...")

    # Simulate deployment steps with delays
    steps = [
        "Preparing build artifacts...",
        "Running pre-deployment checks...",
        "Uploading package...",
        "Updating service...",
        "Restarting application...",
        "Verifying deployment...",
    ]

    for step in steps:
        print(f"[DUMMY] {step}")
        # Simulate work happening
        time.sleep(1)

    # Create a mock deployment artifact
    try:
        os.makedirs("dist", exist_ok=True)
        with open(os.path.join("dist", f"{environment}_deployment.log"), "w") as f:
            f.write(
                f"Dummy deployment to {environment} completed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            f.write(f"Deployment URL: {deploy_url}\n")
            for step in steps:
                f.write(f"✓ {step}\n")
    except Exception as e:
        print(f"Warning: Could not create mock deployment artifact: {e}")

    print(f"[DUMMY] Application successfully deployed to {environment}!")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Dummy deployment for template project"
    )
    parser.add_argument(
        "--environment",
        "-e",
        choices=["staging", "production"],
        default="staging",
        help="Environment to deploy to",
    )

    args = parser.parse_args()

    if not deploy(args.environment):
        sys.exit(1)

    sys.exit(0)
