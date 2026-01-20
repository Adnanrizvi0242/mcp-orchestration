# MCP Orchestration Framework (Langflow + Python)

This project demonstrates a custom MCP (Model Context Protocol) server
integrated with Langflow for tool orchestration.

## Features
- Calculator (BODMAS)
- Simple Interest (SI)
- Compound Interest (CI)
- EMI Calculator
- Weather tool (Weatherstack API)
- Deterministic tool routing

## Tech Stack
- Python 3.11
- Langflow
- MCP (FastMCP)
- Weatherstack API
- AST-based safe math evaluation

## Setup Instructions

```bash
git clone <repo-url>
cd mcp-orchestration
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Create .env:
    WEATHERSTACK_API_KEY=your_api_key_here


Run Langflow:
    langflow run


Import the flow from:

langflow/mcp_orchestration_flow.json

Import the flow from:

langflow/mcp_orchestration_flow.json



Example Prompts

2+2

SI 10000 5 2

CI 10000 5 2

EMI 500000 8 20

jamshedpur weather