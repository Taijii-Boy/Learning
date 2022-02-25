# Строитель предоставляет лаконичный API для поэтапного
# конструирования сложного объекта

class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None

        #employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.street_address}, {self.postcode}, {self.city}' +\
                f'Employed at {self.company_name} as a {self.position} earning {self.annual_income}'

class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self