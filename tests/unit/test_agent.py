"""Tool Calling Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_register_tool():
    """Test Register a new tool with schema, description, and access controls."""
    tools = AgentTools()
    result = await tools.register_tool(name="test", schema="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_select_tools():
    """Test Select optimal tools for a given user intent."""
    tools = AgentTools()
    result = await tools.select_tools(user_intent="test", available_tools="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_validate_call():
    """Test Validate tool call parameters against the tool schema."""
    tools = AgentTools()
    result = await tools.validate_call(tool_name="test", parameters="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_execute_tool():
    """Test Execute a validated tool call and return structured results."""
    tools = AgentTools()
    result = await tools.execute_tool(tool_name="test", parameters="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.tool_calling_agent_agent import ToolCallingAgentAgent
    agent = ToolCallingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
