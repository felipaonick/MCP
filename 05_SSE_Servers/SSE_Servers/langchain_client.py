from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import asyncio
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

async def main():
    print("Hello langchain MCP!")



if __name__ == "__main__":
    asyncio.run(main())
