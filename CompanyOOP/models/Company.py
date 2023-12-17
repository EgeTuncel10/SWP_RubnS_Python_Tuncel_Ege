from typing import List

from models.Person.Person import Person
from models.Department import Department
from models.Person.Gender import Gender

class Company:
    def __init__(self, company_id, additional_persons: List[Person], departments: List[Department]):
        self.company_id = company_id
        self.additional_persons = additional_persons
        self.departments = departments

    def __str__(self) -> str:
        return f"{self.company_id} {self.additional_persons} {self.departments}"
    
    def amount_of_employees(self):
        amount = 0
        for i in self.departments:
            amount += i.amount_of_employees()

        return amount
    
    def amount_of_departments(self):
        return len(self.departments)
    
    def percentage_of_female_and_male(self):
        amount = {'female': 0, 'male': 0}
        for i in self.departments:
            for e in i.employees:
                if e.gender == Gender.Female:
                    amount['female'] += 1
                else:
                    amount['male'] += 1
        
        percentages = {'female': 0, 'male': 0}
        percentages['female'] = (amount['female']/(amount['female']+amount['male'])) * 100
        percentages['male'] = (amount['male']/(amount['female']+amount['male'])) * 100

        return percentages
    
    def department_employees_strength(self):
        dep_employees_stength = {}
        for i in self.departments:
            dep_name = i.department_name.name
            dep_strength = i.employees_strength()
            dep_employees_stength[dep_name] = dep_strength
        
        return dep_employees_stength
        

