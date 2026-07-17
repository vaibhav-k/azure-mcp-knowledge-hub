from pydantic import BaseModel


class Employee(BaseModel):
    """
    Employee record.
    """

    id: int
    name: str
    department: str
    email: str
    location: str
