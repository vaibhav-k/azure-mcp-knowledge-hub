import logging
import signal
import sys

from fastmcp import FastMCP

from .tools import register_tools

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


logger = logging.getLogger("document-server")


mcp = FastMCP("Document Server")


register_tools(mcp)


def shutdown_handler(signum, frame):
    """
    Graceful shutdown handler.
    """
    logger.info("Stopping Document MCP Server...")
    sys.exit(0)


signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)


if __name__ == "__main__":

    try:
        logger.info("Starting Document MCP Server")
        mcp.run()

    except KeyboardInterrupt:
        logger.info("Document MCP Server stopped")

    finally:
        logger.info("Shutdown complete")
