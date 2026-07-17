from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

from .config import settings
from .schemas import (
    DocumentMetadata,
    DocumentContent,
)


class BlobStorage:
    """
    Azure Blob Storage service layer.
    """

    def __init__(self):
        if not settings.AZURE_STORAGE_ACCOUNT_URL:
            raise ValueError("AZURE_STORAGE_ACCOUNT_URL is missing")

        if settings.AZURE_STORAGE_ACCOUNT_KEY:
            self.client = BlobServiceClient(
                account_url=settings.AZURE_STORAGE_ACCOUNT_URL,
                credential=settings.AZURE_STORAGE_ACCOUNT_KEY,
            )
        else:
            self.client = BlobServiceClient(
                account_url=settings.AZURE_STORAGE_ACCOUNT_URL,
                credential=DefaultAzureCredential(),
            )

    def _container(self, container_name=None):
        return self.client.get_container_client(
            container_name or settings.AZURE_STORAGE_CONTAINER_NAME
        )

    def list_documents(self, container_name=None) -> list[DocumentMetadata]:
        container = self._container(container_name)
        documents = []

        for blob in container.list_blobs():
            documents.append(
                DocumentMetadata(
                    name=blob.name,
                    size=blob.size,
                    content_type=(
                        blob.content_settings.content_type
                        if blob.content_settings
                        else None
                    ),
                    last_modified=str(blob.last_modified),
                    url=(
                        f"{settings.AZURE_STORAGE_ACCOUNT_URL}"
                        f"/{container.container_name}"
                        f"/{blob.name}"
                    ),
                )
            )

        return documents

    def search_documents(
        self, query: str, container_name=None
    ) -> list[DocumentMetadata]:
        documents = self.list_documents(container_name)
        query = query.lower()
        return [doc for doc in documents if query in doc.name.lower()]

    def get_document(self, name: str, container_name=None) -> DocumentContent:
        container = self._container(container_name)
        blob = container.get_blob_client(name)
        data = blob.download_blob()
        content = data.readall().decode("utf-8", errors="ignore")
        return DocumentContent(name=name, content=content)
