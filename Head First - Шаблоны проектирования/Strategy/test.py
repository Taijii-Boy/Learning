class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = Address()

class Address:
    def __init__(self, address='Lenina, 5'):
        self.address = address

    def get_address(self):
        return self.address

p = Person('Vasia', 30)
print(p.name)
print(p.get_address())
