from models.Person.Gender import Gender

class Person:
    def __init__(self, person_id, firstname, lastname, birthdate, gender: Gender):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.gender = gender

    def __str__(self) -> str:
        return f"{self.person_id} {self.firstname} {self.lastname} {self.birthdate} {self.gender}"
