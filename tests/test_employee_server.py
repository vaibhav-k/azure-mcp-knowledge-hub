import asyncio

from fastmcp import Client
from fastmcp.client.transports import StdioTransport


async def test_employee_tools():
    transport = StdioTransport(command="python", args=[".\\employee_server\\app.py"])
    client = Client(transport)

    async with client:
        tools = await client.list_tools()
        print("Available Employee tools:")

        for tool in tools:
            print("-", tool.name)


if __name__ == "__main__":
    asyncio.run(test_employee_tools())
