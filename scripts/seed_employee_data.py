from sqlalchemy.orm import sessionmaker

from employee_server.database import EmployeeDatabase
from employee_server.models import EmployeeModel

database = EmployeeDatabase()

Session = sessionmaker(bind=database.engine)


employees = [
    EmployeeModel(
        name="Amit Sharma",
        department="Engineering",
        email="amit@company.com",
        location="Noida",
    ),
    EmployeeModel(
        name="Priya Singh", department="HR", email="priya@company.com", location="Delhi"
    ),
    EmployeeModel(
        name="Rahul Verma",
        department="Finance",
        email="rahul@company.com",
        location="Mumbai",
    ),
]


with Session() as db:

    db.add_all(employees)

    db.commit()


print("Employee data inserted")
