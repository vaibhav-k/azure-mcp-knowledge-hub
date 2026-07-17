from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings
from .models import Base, EmployeeModel
from .schemas import Employee


class EmployeeDatabase:

    def __init__(self):

        if not settings.DATABASE_URL:
            raise ValueError("DATABASE_URL is missing")

        self.engine = create_engine(settings.DATABASE_URL)

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
