from storage import BlobStorage

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
        List documents from Azure Blob Storage.

        Returns document metadata.
        """

        storage = get_storage()

        return storage.list_documents(container_name)
