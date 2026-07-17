from pydantic import BaseModel


class DocumentResult(BaseModel):
    filename: str
    blob_url: str
    snippet: str
