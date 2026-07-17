import asyncio

from .config import settings
from .session import MCPConnection
from .router import MCPRouter


async def main():
    document_client = MCPConnection(
        settings.DOCUMENT_SERVER_COMMAND, settings.DOCUMENT_SERVER_PATH
    )
    employee_client = MCPConnection(
        settings.EMPLOYEE_SERVER_COMMAND, settings.EMPLOYEE_SERVER_PATH
    )

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
