import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DOCUMENT_SERVER_COMMAND = os.getenv("DOCUMENT_SERVER_COMMAND", "python")
    DOCUMENT_SERVER_PATH = os.getenv(
        "DOCUMENT_SERVER_PATH", ".\\document_server\\app.py"
    )

    EMPLOYEE_SERVER_COMMAND = os.getenv("EMPLOYEE_SERVER_COMMAND", "python")
    EMPLOYEE_SERVER_PATH = os.getenv(
        "EMPLOYEE_SERVER_PATH", ".\\employee_server\\app.py"
    )


settings = Settings()
