from fastmcp import Client
from fastmcp.client.transports import StdioTransport


class MCPConnection:

    def __init__(self, command: str, args: list[str]):
        self.transport = StdioTransport(command=command, args=args)
        self.client = Client(self.transport)
        self.context = None

    async def connect(self):
        self.context = await self.client.__aenter__()

    async def close(self):
        await self.client.__aexit__(None, None, None)

    async def tools(self):
        return await self.client.list_tools()
