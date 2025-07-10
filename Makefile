.PHONY: help dev-backend dev-mcp test install

help:
	@echo "Available commands:"
	@echo "  make dev-backend     - Starts the backend development server (LangGraph)"
	@echo "  make dev-mcp         - Starts the MCP server for development"
	@echo "  make test            - Runs the test suite"
	@echo "  make install         - Installs dependencies"

dev-backend:
	@echo "Starting backend development server..."
	@cd backend && langgraph dev

dev-mcp:
	@echo "Starting MCP server..."
	@cd backend && python -m src.agent.mcp_server

test:
	@echo "Running tests..."
	@cd backend && python -m pytest

install:
	@echo "Installing dependencies..."
	@cd backend && uv pip install -e .

# Default target
dev: dev-mcp
