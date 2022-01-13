 

class Vector:

    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD


    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y): # Можно использовать Vector.validate, но Python поймет и через self, так более универсально, т.к. имя класса может меняться   
            self.x = x
            self.y = y
        
        print(self.norm2(self.x, self.y))

    
    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(15, 30)
res = Vector.get_coord(v)
# print(v.get_coord())
# print(Vector.validate(5))
# print(res)