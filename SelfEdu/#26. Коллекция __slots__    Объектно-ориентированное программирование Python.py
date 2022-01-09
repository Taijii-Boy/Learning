import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:

    __slots__ = ('x', 'y') #  Какие локальные свойства разрешены в объектах класса Point2D

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


# pt = Point(1, 2)
# pt.z = 3
# print(pt.__dict__)

# pt2 = Point2D(1, 2)
# pt.x = 4
# print(pt2.__dict__) # При наличии __slots__ коллекция __dict__ удаляется (иначе мы могли бы в неё что-нибудь добавить)

p = Point(1, 2)
p2 = Point2D(10, 20)

t1 = timeit.timeit(p.calc)
t2 = timeit.timeit(p2.calc)
print(t1, t2)