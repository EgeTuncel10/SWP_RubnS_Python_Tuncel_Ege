#from .Person import Person
#from .Role import Role
#from .Position import Position
import Person, Role, Position
class Employee(Person):
    def __init__(self, person_id, firstname, lastname, birthdate, gender, role: Role, position: Position):
        super().__init__(person_id, firstname, lastname, birthdate, gender)
        self.role = role
        self.position = position

    def __str__(self) -> str:
        return f"{super().__str__()}\n{self.role} {self.position}"
