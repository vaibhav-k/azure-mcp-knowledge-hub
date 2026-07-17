from database import EmployeeDatabase

_database = None


def get_database():

    global _database

    if _database is None:
        _database = EmployeeDatabase()

    return _database


def register_tools(mcp):

    @mcp.tool()
    def list_employees():
        """
        Return all employees.
        """

        return get_database().get_all()

    @mcp.tool()
    def get_employee(employee_id: int):
        """
        Get employee by ID.
        """

        return get_database().get_by_id(employee_id)

    @mcp.tool()
    def search_employees(query: str):
        """
        Search employees.
        """

        return get_database().search(query)
