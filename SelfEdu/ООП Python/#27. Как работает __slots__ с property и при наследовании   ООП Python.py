# class Point2D:
#     __slots__ = ['x', 'y', '__length']

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__length = (x * x + y * y) ** 0.5


#     @property
#     def length(self):
#         return self.__length

    
#     @length.setter
#     def length(self, value):
#         self.__length = value


# pt = Point2D(1, 2)
# print(pt.length)


class Point2D:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        
pt = Point3D(1, 2)
pt.z = 30
print(pt.z)