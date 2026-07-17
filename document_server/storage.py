import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

load_dotenv()


class BlobStorage:

    def __init__(self):

        account_url = os.getenv("AZURE_STORAGE_ACCOUNT_URL")

        if not account_url:
            raise ValueError(
                "AZURE_STORAGE_ACCOUNT_URL is missing. " "Set it in .env file."
            )

        credential = DefaultAzureCredential()

        self.client = BlobServiceClient(account_url=account_url, credential=credential)

    def list_documents(self, container_name: str) -> list[str]:

        container_client = self.client.get_container_client(container_name)

        return [blob.name for blob in container_client.list_blobs()]
