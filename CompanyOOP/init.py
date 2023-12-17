from models.DepartmentName import DepartmentName
from models.Person.Gender import Gender
from models.Person.Role import Role
from models.Person.Title import Title
from models.Person.Position import Position
from models.Company import Company
from models.Department import Department
from models.Person.DepartmentHead import DepartmentHead
from models.Person.Employee import Employee
from models.Person.Person import Person

from datetime import date

def init():
    company = Company(
        company_id = 1,
        additional_persons = [
            Person(
                person_id=1,
                firstname="Michael",
                lastname="Immergut",
                birthdate=date(1999, 12, 1),
                gender=Gender.Male
            )
        ],
        departments = [
            Department(
                department_name = DepartmentName.SearchAndDevelopment,
                department_head = DepartmentHead(
                    person_id=1,
                    firstname="Jane",
                    lastname="Doe",
                    birthdate="1995-02-15",
                    gender=Gender.Female,
                    role=Role.DepartmentHead,
                    position=Position.High,
                    responsibilities="Manage department activities",
                    title=Title.Prof,
                    email="jane.doe@example.com",
                    phone="09786379833"
                ),
                employees = [
                    Employee(
                        person_id=1,
                        firstname="Kabi",
                        lastname="Lane",
                        birthdate="1995-01-15",
                        gender=Gender.Male,
                        role=Role.SoftwareEngineer,
                        position=Position.Middle,
                    ),
                    Employee(
                        person_id=2,
                        firstname="Kabi",
                        lastname="bAne",
                        birthdate="1995-01-15",
                        gender=Gender.Female,
                        role=Role.SoftwareEngineer,
                        position=Position.Middle,
                    ),
                    Employee(
                        person_id=3,
                        firstname="Kabi",
                        lastname="Shame",
                        birthdate="1995-01-15",
                        gender=Gender.Female,
                        role=Role.SoftwareEngineer,
                        position=Position.Middle,
                    )
                ]
            ),
            Department(
                department_name = DepartmentName.MarketingAndAccountance,
                department_head = DepartmentHead(
                    person_id=1,
                    firstname="Dame",
                    lastname="Shame",
                    birthdate="1995-02-15",
                    gender=Gender.Male,
                    role=Role.DepartmentHead,
                    position=Position.High,
                    responsibilities="Manage department activities",
                    title=Title.Mag,
                    email="dame.shame@example.com",
                    phone="09733339833"
                ),
                employees = [
                    Employee(
                        person_id=4,
                        firstname="Didi",
                        lastname="Zime",
                        birthdate="1995-01-15",
                        gender=Gender.Female,
                        role=Role.Accountant,
                        position=Position.Low,
                    ),
                    Employee(
                        person_id=5,
                        firstname="Bin",
                        lastname="Bin",
                        birthdate="1995-01-15",
                        gender=Gender.Female,
                        role=Role.MachineWorker,
                        position=Position.Middle,
                    ),
                    Employee(
                        person_id=6,
                        firstname="Lime",
                        lastname="Shin",
                        birthdate="1995-01-15",
                        gender=Gender.Female,
                        role=Role.MachineWorker,
                        position=Position.Middle,
                    )
                ]
            )
        ]
    )

    return company

def main():
    company = init()
    print(company.amount_of_employees())
    print(company.amount_of_departments())
    print(company.percentage_of_female_and_male())
    print(company.department_employees_strength())
