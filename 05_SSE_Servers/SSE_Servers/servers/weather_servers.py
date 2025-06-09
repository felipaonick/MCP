from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_westher(location: str) -> str:
    """Get the weather for location."""
    return "Hot as hell"


if __name__ == "__main__":
    mcp.run(transport="sse")