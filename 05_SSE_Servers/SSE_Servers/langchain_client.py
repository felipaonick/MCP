from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import asyncio
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

async def main():
    # dobbiamo dirli a quali mcp server vogliamo connetterci e come runnarli
    client = MultiServerMCPClient({
        "math": {
            "command": "python",
            "args": ["C:/Users/felip/Desktop/import-pc/MCP/05_SSE_Servers/SSE_Servers/servers/math_server.py"],
            "transport": "stdio"
        },
        "weather": {
            "url": "http://localhost:8000/sse",
            "transport": "sse"
        }
    })

    tools = await client.get_tools()

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    #result = await agent.ainvoke({
    #    "messages": [{"role": "user", "content": "What is 2 + 2 ?"}]
    #})

    result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]})

    print(result['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
