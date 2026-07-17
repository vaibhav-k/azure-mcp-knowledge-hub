from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

from config import settings
from schemas import DocumentMetadata


class BlobStorage:
    """
    Azure Blob Storage abstraction.
    """

    def __init__(self):

        if not settings.AZURE_STORAGE_ACCOUNT_URL:
            raise ValueError("AZURE_STORAGE_ACCOUNT_URL is missing")

        self.client = BlobServiceClient(
            account_url=settings.AZURE_STORAGE_ACCOUNT_URL,
            credential=DefaultAzureCredential(),
        )

    def list_documents(
        self, container_name: str | None = None
    ) -> list[DocumentMetadata]:
        """
        List documents from Azure Blob Storage.
        """

        container_name = container_name or settings.AZURE_STORAGE_CONTAINER_NAME

        container = self.client.get_container_client(container_name)

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
                        f"/{container_name}/{blob.name}"
                    ),
                )
            )

        return documents
