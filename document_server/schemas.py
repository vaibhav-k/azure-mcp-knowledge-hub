from pydantic import BaseModel


class DocumentResult(BaseModel):
    """
    Represents a document stored in Azure Blob Storage.
    """

    filename: str
    blob_url: str | None = None
    snippet: str | None = None
