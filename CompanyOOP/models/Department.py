from models.Person.DepartmentHead import DepartmentHead
from models.Person.Employee import Employee
from models.DepartmentName import DepartmentName
from models.Person.Position import Position

from typing import List

class Department:
    def __init__(self, department_name: DepartmentName, department_head: DepartmentHead, employees: List[Employee]):
        self.department_name = department_name
        self.department_head = department_head
        self.employees = employees

    def __str__(self) -> str:
        return f"{self.department_name} {self.department_head} {self.employees}"
    
    def amount_of_employees(self):
        return len(self.employees)
    
    def employees_strength(self):
        employees_strength = 0
        for i in self.employees:
            if (i.position == Position.High) or (i.position == Position.Middle):
                employees_strength += 1

        return employees_strength
        
    