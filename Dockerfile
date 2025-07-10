# MCP Research Agent Server Dockerfile
FROM mirror.gcr.io/python:3.11-slim

# Install UV package manager
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend/ .

# Set Python path
ENV PYTHONPATH=/app

# Install dependencies with UV
RUN uv sync --no-dev

# Expose port for MCP server
EXPOSE 8000

# Default command to run the MCP server
CMD ["uv", "run", "python", "-m", "src.agent.mcp_server"]
