from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

password = "V@ibhav23"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=tcp:azure-mcp-knowledgehub-sql.database.windows.net,1433;"
    "DATABASE=knowledgehub;"
    "UID=sqladmin;"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

connection_url = "mssql+pyodbc:///?odbc_connect=" + quote_plus(connection_string)

engine = create_engine(connection_url)

with engine.connect() as conn:
    print(conn.execute(text("SELECT 1")).fetchone())
