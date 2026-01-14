FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/wilfoa/pybugger-mcp"
LABEL org.opencontainers.image.description="Python Debugger MCP Server"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

# Install the package from PyPI
RUN pip install --no-cache-dir pybugger-mcp

# Run the MCP server
ENTRYPOINT ["python", "-m", "pybugger_mcp.mcp_server"]
