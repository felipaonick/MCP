import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get("OPENAI_API_KEY"))

async def main():
    print("Hello from langchain-mcp-adapters-project!")


if __name__ == "__main__":
    asyncio.run(main())
