from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings
from .models import Base, EmployeeModel
from .schemas import Employee


class EmployeeDatabase:

    def __init__(self):

        if not all(
            [
                settings.DB_SERVER,
                settings.DB_DATABASE,
                settings.DB_USERNAME,
                settings.DB_PASSWORD,
            ]
        ):
            raise ValueError("Database configuration is missing")

        connection_string = (
            "DRIVER={ODBC Driver 18 for SQL Server};"
            f"SERVER=tcp:{settings.DB_SERVER},1433;"
            f"DATABASE={settings.DB_DATABASE};"
            f"UID={settings.DB_USERNAME};"
            f"PWD={settings.DB_PASSWORD};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
        )

        connection_url = "mssql+pyodbc:///?odbc_connect=" + quote_plus(
            connection_string
        )

        print("Initializing Employee Database")

        self.engine = create_engine(
            connection_url,
            pool_pre_ping=True,
            pool_recycle=1800,
        )

        # Consider removing this in production.
        # Use migrations (Alembic) instead.
        Base.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)

    def get_all(self):

        with self.session() as db:

            employees = db.query(EmployeeModel).all()
            return [
                Employee(
                    id=e.id,
                    name=e.name,
                    department=e.department,
                    email=e.email,
                    location=e.location,
                )
                for e in employees
            ]

    def get_by_id(self, employee_id: int):

        with self.session() as db:

            employee = (
                db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
            )

            if not employee:
                return None

            return Employee(
                id=employee.id,
                name=employee.name,
                department=employee.department,
                email=employee.email,
                location=employee.location,
            )

    def search(self, query: str):

        with self.session() as db:

            employees = (
                db.query(EmployeeModel).filter(EmployeeModel.name.contains(query)).all()
            )

            return [
                Employee(
                    id=e.id,
                    name=e.name,
                    department=e.department,
                    email=e.email,
                    location=e.location,
                )
                for e in employees
            ]
