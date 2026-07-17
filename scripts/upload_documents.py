import os

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

ACCOUNT_URL = os.getenv("AZURE_STORAGE_ACCOUNT_URL")
CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER_NAME", "documents")


def upload_file(path):
    client = BlobServiceClient(ACCOUNT_URL, credential=DefaultAzureCredential())
    blob = client.get_blob_client(container=CONTAINER, blob=os.path.basename(path))
    with open(path, "rb") as data:
        blob.upload_blob(data, overwrite=True)
    print(f"Uploaded {path}")


if __name__ == "__main__":
    upload_file("sample.pdf")
