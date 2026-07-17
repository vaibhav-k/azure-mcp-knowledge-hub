from storage import BlobStorage

_storage = None


def get_storage():

    global _storage

    if _storage is None:
        _storage = BlobStorage()

    return _storage


def register_tools(mcp):

    @mcp.tool()
    def list_documents(container_name: str) -> list[str]:
        """
        List documents from Azure Blob Storage.
        """

        storage = get_storage()

        return storage.list_documents(container_name)
