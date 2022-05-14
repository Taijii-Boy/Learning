class Integer:
    def __set_name__(self, owner, name):
        self.name = '_' + name
        print(f'owner переменной {name} - {owner}')

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        print(f'instance - {instance}, owner - {owner}, name - {self.name}')
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)
        print(f'instance - {instance}, name - {self.name}, value - {value}')


class Point:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    p1 = Point(1, 2, 3)
    print(p1.__dict__)
    p1.z = 5
    print(p1.__dict__)
    print(p1.y)