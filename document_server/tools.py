from .storage import BlobStorage

_storage = None


def get_storage():

    global _storage

    if _storage is None:
        _storage = BlobStorage()

    return _storage


def register_tools(mcp):

    @mcp.tool()
    def list_documents(container_name: str | None = None):
        """
        List available documents.
        """
        return get_storage().list_documents(container_name)

    @mcp.tool()
    def search_documents(query: str, container_name: str | None = None):
        """
        Search documents by name.
        """
        return get_storage().search_documents(query, container_name)

    @mcp.tool()
    def get_document(name: str, container_name: str | None = None):
        """
        Retrieve document content.
        """
        return get_storage().get_document(name, container_name)
