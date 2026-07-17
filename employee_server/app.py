import logging
import signal
import sys

from fastmcp import FastMCP

from .tools import register_tools

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


logger = logging.getLogger("employee-server")


mcp = FastMCP("Employee Server")


register_tools(mcp)


def shutdown_handler(signum, frame):
    logger.info("Stopping Employee MCP Server...")
    sys.exit(0)


signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)


if __name__ == "__main__":

    try:
        logger.info("Starting Employee MCP Server")
        mcp.run()

    except KeyboardInterrupt:
        logger.info("Employee MCP Server stopped")

    finally:
        logger.info("Shutdown complete")
