"""Test configuration for Tool Calling Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "tool-calling-agent", "category": "AI Engineering"}
