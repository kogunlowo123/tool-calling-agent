# Tool Calling Agent

[![CI](https://github.com/kogunlowo123/tool-calling-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/tool-calling-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Tool-use orchestration agent that manages function calling, tool selection, parameter validation, error handling, and result integration for LLM-powered agents interacting with external APIs and services.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `register_tool` | Register a new tool with schema, description, and access controls |
| `select_tools` | Select optimal tools for a given user intent |
| `validate_call` | Validate tool call parameters against the tool schema |
| `execute_tool` | Execute a validated tool call and return structured results |
| `compose_tools` | Compose multiple tool calls into a pipeline |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/tools/register` | Register a tool |
| `POST` | `/api/v1/tools/select` | Select tools for intent |
| `POST` | `/api/v1/tools/validate` | Validate tool call |
| `POST` | `/api/v1/tools/execute` | Execute tool call |
| `POST` | `/api/v1/tools/compose` | Compose tool pipeline |

## Features

- Tool Selection
- Parameter Validation
- Error Handling
- Result Integration
- Tool Registry

## Integrations

- Openai Api
- Anthropic Api
- Langchain
- Mcp Server
- Api Gateway

## Architecture

```
tool-calling-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── tool_calling_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**OpenAI Function Calling + Anthropic Tool Use + LangChain Tools**

---

Built as part of the Enterprise AI Agent Platform.
