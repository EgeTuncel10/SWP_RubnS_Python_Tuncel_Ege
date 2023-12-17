from models.Person.Employee import Employee
from .Title import Title

class DepartmentHead(Employee):
    def __init__(self, person_id, firstname, lastname, birthdate, gender, role, position, responsibilities, title: Title, email, phone):
        super().__init__(person_id, firstname, lastname, birthdate, gender, role, position)
        self.responsibilities = responsibilities
        self.title = title
        self.email = email
        self.phone = phone

    def __str__(self) -> str:
        return f"{super().__str__()}\n{self.responsibilities} {self.title} {self.email} {self.phone}"
