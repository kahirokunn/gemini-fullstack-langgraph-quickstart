#!/usr/bin/env python
"""
MCP Server Wrapper for Claude Desktop
This wrapper ensures proper stdio communication between Claude Desktop and the FastMCP server.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Now import and run the MCP server
from src.agent.mcp_server import mcp

if __name__ == "__main__":
    # Run in stdio mode for Claude Desktop
    mcp.run(transport="stdio")
