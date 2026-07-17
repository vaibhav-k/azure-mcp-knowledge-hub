import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    DB_SERVER = os.getenv("DB_SERVER", "")
    DB_DATABASE = os.getenv("DB_DATABASE", "")
    DB_USERNAME = os.getenv("DB_USERNAME", "")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")


settings = Settings()
