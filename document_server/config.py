import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Application configuration.
    """

    AZURE_STORAGE_ACCOUNT_URL: str = os.getenv("AZURE_STORAGE_ACCOUNT_URL", "")
    AZURE_STORAGE_CONTAINER_NAME: str = os.getenv(
        "AZURE_STORAGE_CONTAINER_NAME", "documents"
    )


settings = Settings()
