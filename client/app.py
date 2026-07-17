import asyncio

from .config import settings
from .session import MCPConnection
from .router import MCPRouter


async def main():
    document_client = MCPConnection("python", ["-m", "document_server.app"])
    employee_client = MCPConnection("python", ["-m", "employee_server.app"])

    await document_client.connect()
    await employee_client.connect()

    router = MCPRouter()
    router.register("documents", document_client)
    router.register("employees", employee_client)
    tools = await router.list_tools()

    for server, server_tools in tools.items():
        print(f"\n{server}:")

        for tool in server_tools:
            print("-", tool.name)

    await document_client.close()
    await employee_client.close()


if __name__ == "__main__":
    asyncio.run(main())
