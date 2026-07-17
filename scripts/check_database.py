from sqlalchemy import text

from employee_server.database import EmployeeDatabase

database = EmployeeDatabase()


with database.engine.connect() as connection:

    result = connection.execute(text("SELECT * FROM employees"))

    for row in result:
        print(row)
