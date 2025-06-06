import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python", # dato che il nostro server è un file Python
    args=["C:/Users/felip/Desktop/import-pc/MCP/04_Connecting_LLM_Clients/langchain_mcp_adapters_project/servers/math_server.py"] # mettiamo il path assoluto al file del server
)


async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Sessione inizializzata")
            tools = await load_mcp_tools(session)
            print(tools)

            agent = create_react_agent(model=llm, tools=tools)

            response = await agent.ainvoke({
                "messages": [HumanMessage(content="What is 2 plus 2?")]
            })
            print(response['messages'][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
