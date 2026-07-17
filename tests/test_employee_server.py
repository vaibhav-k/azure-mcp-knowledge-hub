import asyncio

from fastmcp import Client
from fastmcp.client.transports import StdioTransport


async def test_employee_tools():

    transport = StdioTransport(command="python", args=["-m", "employee_server.app"])
    client = Client(transport)

    async with client:
        tools = await client.list_tools()
        print("Available Employee tools:")
        for tool in tools:
            print("-", tool.name)
        print("\nTesting list_employees...")
        employees = await client.call_tool("list_employees", {})
        print(employees)
        print("\nTesting search_employees...")
        results = await client.call_tool("search_employees", {"query": "John"})
        print(results)
        print("\nTesting get_employee...")
        employee = await client.call_tool("get_employee", {"employee_id": 1})
        print(employee)


if __name__ == "__main__":
    asyncio.run(test_employee_tools())
