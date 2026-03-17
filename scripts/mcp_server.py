#!/usr/bin/env python3
"""MCP server exposing ai-workflow-lab project metadata tools."""

import tomllib
from pathlib import Path

from mcp.server.fastmcp import FastMCP

PROJECT_ROOT = Path(__file__).parent.parent

mcp = FastMCP("ai-workflow-lab")


@mcp.tool()
def get_project_meta() -> dict:
    """Return project name, version, and Python version requirement from pyproject.toml."""
    with open(PROJECT_ROOT / "pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    project = data["project"]
    return {
        "name": project["name"],
        "version": project["version"],
        "requires_python": project["requires-python"],
    }


@mcp.tool()
def list_routes() -> list[dict]:
    """Return the Flask routes exposed by this application."""
    return [
        {
            "path": "/health",
            "methods": ["GET"],
            "description": "Health check endpoint — returns service status",
        },
        {
            "path": "/version",
            "methods": ["GET"],
            "description": "Returns the application version from pyproject.toml",
        },
        {
            "path": "/",
            "methods": ["GET"],
            "description": "Root endpoint — returns a greeting message",
        },
    ]


if __name__ == "__main__":
    mcp.run(transport="stdio")

