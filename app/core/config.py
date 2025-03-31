import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FastAPI")
    VERSION: str = os.getenv("VERSION", "1.0.0")
    DB_SERVER: str = os.getenv("DB_SERVER", "localhost")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "")
    DB_DRIVER: str = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER.replace(' ', '+')}"
    )

    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ALLOWED_HOSTS: list = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else []