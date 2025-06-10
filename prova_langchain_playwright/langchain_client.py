from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START
from langchain_core.messages import HumanMessage
#from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import asyncio

load_dotenv()

# LLM da usare (puoi anche usare GPT-4o o altri)
#llm = ChatOllama(model="qwen2.5:14b", temperature=0, base_url="http://localhost:11434/")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

async def main():
    client = MultiServerMCPClient({
        "playwright": {
            "command": "docker",
            "args": [
                "run", "-i", "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "playwright-mcp-server"
            ],
            "transport": "stdio"
        }
    })

    tools = await client.get_tools()
    print(f"✅ Tools disponibili: {[t.name for t in tools]}")

    agent = create_react_agent(model=llm, tools=tools)

    async def call_model(state: MessagesState):
        response = await agent.ainvoke(state)
        return {"messages": response['messages'][-1]}

    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_edge(START, "call_model")

    graph = builder.compile()

    site_response = await graph.ainvoke({'messages': [HumanMessage(content="apri il sito www.bbc.com e dimmi il titolo principale")]})
    print(site_response['messages'][-1].content)

# async def main():
#     # Inizializza la sessione e carica i tool MCP
#     async with client.session("playwright") as session:
#         tools = await load_mcp_tools(session)
#         print(f"✅ Tools disponibili: {[t.name for t in tools]}")
#
#         # Crea agente LangChain/LangGraph con i tool ottenuti
#         agent = create_react_agent(model=llm, tools=tools)
#
#         # Esegui una query (esempio generico)
#         response = await agent.ainvoke({
#             "messages": {"role": "user", "content": "apri il sito www.bbc.com e dimmi il titolo principale"}
#         })
#         print(response['messages'][-1].content)


if __name__ == "__main__":
    asyncio.run(main())

    
