"""MCP Server implementation for the LangGraph research agent."""

import os
import asyncio
from typing import Dict, Any, List
from fastmcp import FastMCP
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from agent.graph import graph
from agent.configuration import Configuration
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("Research Agent")

# Helper function to perform research
def _perform_research(question: str, max_research_loops: int = 2, initial_search_query_count: int = 3) -> str:
    """
    Internal helper function to perform research on a given question.
    """
    # Create the initial state
    state = {
        "messages": [HumanMessage(content=question)],
        "initial_search_query_count": initial_search_query_count,
        "max_research_loops": max_research_loops,
        "search_query": [],
        "web_research_result": [],
        "sources_gathered": [],
        "research_loop_count": 0,
    }

    # Run the graph
    result = graph.invoke(state)

    # Extract the final answer from the messages
    messages = result.get("messages", [])
    if messages:
        final_message = messages[-1]
        if isinstance(final_message, AIMessage):
            return final_message.content

    return "No research results available."

@mcp.tool
def research_query(question: str, max_research_loops: int = 2, initial_search_query_count: int = 3) -> str:
    """
    Perform comprehensive research on a given question using web search and analysis.

    Args:
        question: The research question to investigate
        max_research_loops: Maximum number of research loops to perform (default: 2)
        initial_search_query_count: Number of initial search queries to generate (default: 3)

    Returns:
        A comprehensive research report with citations
    """
    return _perform_research(question, max_research_loops, initial_search_query_count)

# Helper function to get research sources
def _get_research_sources(question: str, max_research_loops: int = 2, initial_search_query_count: int = 3) -> List[Dict[str, Any]]:
    """
    Internal helper function to get sources used during research.
    """
    # Create the initial state
    state = {
        "messages": [HumanMessage(content=question)],
        "initial_search_query_count": initial_search_query_count,
        "max_research_loops": max_research_loops,
        "search_query": [],
        "web_research_result": [],
        "sources_gathered": [],
        "research_loop_count": 0,
    }

    # Run the graph
    result = graph.invoke(state)

    # Return the sources gathered
    return result.get("sources_gathered", [])

@mcp.tool
def get_research_sources(question: str, max_research_loops: int = 2, initial_search_query_count: int = 3) -> List[Dict[str, Any]]:
    """
    Get the sources used during research for a given question.

    Args:
        question: The research question to investigate
        max_research_loops: Maximum number of research loops to perform (default: 2)
        initial_search_query_count: Number of initial search queries to generate (default: 3)

    Returns:
        List of sources with metadata used during research
    """
    return _get_research_sources(question, max_research_loops, initial_search_query_count)

@mcp.tool
def quick_research(question: str) -> str:
    """
    Perform quick research with minimal loops for faster results.

    Args:
        question: The research question to investigate

    Returns:
        A quick research summary
    """
    return _perform_research(question, max_research_loops=1, initial_search_query_count=2)

# Tools are already registered with @mcp.tool decorators above

if __name__ == "__main__":
    import sys
    import traceback

    # Check if we should run in stdio mode
    if "--stdio" in sys.argv:
        try:
            # Add debug output
            print("Starting MCP server in stdio mode...", file=sys.stderr)
            # Run the MCP server with stdio transport
            mcp.run(transport="stdio")
        except Exception as e:
            print(f"Error running MCP server: {e}", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            sys.exit(1)
    else:
        # Run the MCP server with SSE transport
        print("Starting MCP Research Agent Server...")
        print("Available tools:")
        print("- research_query: Comprehensive research with citations")
        print("- get_research_sources: Get sources used in research")
        print("- quick_research: Fast research with minimal loops")
        mcp.run(transport="sse", host="0.0.0.0", port=8000)
