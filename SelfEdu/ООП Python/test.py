class Point:

    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        print('__getattribute__')
        object.__getattribute__(self, item)


    def __setattr__(self, key, value):
        print('__setattr__')
        return object.__setattr__(self, key, value)

pt = Point(10, 20)
a = pt.x

