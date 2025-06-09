from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_westher(location: str) -> str:
    """Get the weather for location."""
    print("This is a log from the SSE server")
    return "Hot as hell"


if __name__ == "__main__":
    mcp.run(transport="sse")