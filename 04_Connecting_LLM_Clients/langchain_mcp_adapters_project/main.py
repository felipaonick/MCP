import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python", # dato che il nostro server è un file Python
    args=["C:/Users/felip/Desktop/import-pc/MCP/04_Connecting_LLM_Clients/langchain_mcp_adapters_project/servers/math_server.py"] # mettiamo il path assoluto al file del server
)




async def main():
    print("Hello from langchain-mcp-adapters-project!")


if __name__ == "__main__":
    asyncio.run(main())
