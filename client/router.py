class MCPRouter:

    def __init__(self):
        self.routes = {}

    def register(self, name, client):
        self.routes[name] = client

    async def list_tools(self):
        result = {}

        for name, client in self.routes.items():
            result[name] = await client.tools()

        return result
