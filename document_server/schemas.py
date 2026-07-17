from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    """
    Azure Blob document metadata.
    """

    name: str
    size: int | None = None
    content_type: str | None = None
    last_modified: str | None = None
    url: str | None = None


class DocumentContent(BaseModel):
    """
    Document content response.
    """

    name: str
    content: str
