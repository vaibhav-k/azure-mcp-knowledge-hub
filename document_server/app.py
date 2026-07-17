from fastmcp import FastMCP
from tools import register_tools

mcp = FastMCP("Document Server")

register_tools(mcp)


if __name__ == "__main__":
    mcp.run()
