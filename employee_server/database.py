from schemas import Employee


class EmployeeDatabase:
    """
    Employee database abstraction.

    This can later be replaced with Azure SQL.
    """

    def __init__(self):

        self.employees = [
            Employee(
                id=1,
                name="Amit Sharma",
                department="Engineering",
                email="amit@example.com",
                location="Noida",
            ),
            Employee(
                id=2,
                name="Priya Singh",
                department="HR",
                email="priya@example.com",
                location="Delhi",
            ),
            Employee(
                id=3,
                name="Rahul Verma",
                department="Finance",
                email="rahul@example.com",
                location="Mumbai",
            ),
        ]

    def get_all(self):

        return self.employees

    def get_by_id(self, employee_id: int):

        for employee in self.employees:

            if employee.id == employee_id:
                return employee

        return None

    def search(self, query: str):

        query = query.lower()

        return [
            employee
            for employee in self.employees
            if query in employee.name.lower() or query in employee.department.lower()
        ]
