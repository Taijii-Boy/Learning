# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x # Есть сеттер, поэтому обращаемся к property x, а не к self._x
#         self.y = y
#         self.z = z

#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise TypeError("Координата должна быть целывм числом")

#     @property
#     def x(self):
#         return self._x

#     @x.setter
#     def x(self, x):
#         self.verify_coord(x)
#         self._x = x

#     @property
#     def y(self):
#         return self._y

#     @y.setter
#     def y(self, y):
#         self.verify_coord(y)
#         self._y = y

#     @property
#     def z(self):
#         return self._z

#     @x.setter
#     def z(self, z):
#         self.verify_coord(z)
#         self._z = z



################ ДЕСКРИПТОРЫ ###################

class ReadIntX:
    '''Дескриптор не данных'''

    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    # def __set__(self, instance, value):
    #     setattr(instance, self.name, value)


class Integer:
    '''Дескриптор данных для координат'''

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целывм числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX() # Приоритет дескриптора не данных такой же, как и у локальной переменной

    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
# p.xr = 5
print(p.xr, p.__dict__)