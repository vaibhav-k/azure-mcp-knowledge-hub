import os

from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

load_dotenv()


class BlobStorage:
    """
    Azure Blob Storage service wrapper.
    """

    def __init__(self):

        account_url = os.getenv("AZURE_STORAGE_ACCOUNT_URL")

        if not account_url:
            raise ValueError("AZURE_STORAGE_ACCOUNT_URL is not configured")

        self.client = BlobServiceClient(
            account_url=account_url, credential=DefaultAzureCredential()
        )

    def list_documents(self, container_name: str) -> list[str]:
        """
        Returns document names from a blob container.
        """

        container = self.client.get_container_client(container_name)

        return [blob.name for blob in container.list_blobs()]
