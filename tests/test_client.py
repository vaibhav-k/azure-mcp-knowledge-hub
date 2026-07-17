import asyncio

from fastmcp import Client
from fastmcp.client.transports import StdioTransport


async def create_client(server_path: str):
    transport = StdioTransport(command="python", args=[server_path])
    return Client(transport)


async def test_client_router():
    document_client = await create_client(".\\document_server\\app.py")
    employee_client = await create_client(".\\employee_server\\app.py")

    async with document_client, employee_client:
        document_tools = await document_client.list_tools()
        employee_tools = await employee_client.list_tools()
        document_tool_names = [tool.name for tool in document_tools]
        employee_tool_names = [tool.name for tool in employee_tools]

        print("\nDocument MCP Server tools:")

        for tool in document_tool_names:
            print("-", tool)

        print("\nEmployee MCP Server tools:")

        for tool in employee_tool_names:
            print("-", tool)

        assert "list_documents" in document_tool_names
        assert "search_documents" in document_tool_names
        assert "get_document" in document_tool_names
        assert "list_employees" in employee_tool_names
        assert "get_employee" in employee_tool_names
        assert "search_employees" in employee_tool_names


if __name__ == "__main__":
    asyncio.run(test_client_router())
