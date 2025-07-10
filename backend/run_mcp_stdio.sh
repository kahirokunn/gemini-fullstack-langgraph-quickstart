#!/bin/bash

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the backend directory
cd "$DIR"

# Set PYTHONPATH to ensure modules can be found
export PYTHONPATH="$DIR:$PYTHONPATH"

# Run the MCP server in stdio mode
exec python -m src.agent.mcp_server --stdio
