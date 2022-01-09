
class Point:
    '''Класс создает точки по заданным координатам'''

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y


    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


    def get_Coords(self):
        return self.__x, self.__y


    def set_Coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")


pt = Point(2, 5)
pt.set_Coords(3, 7)
print(pt.get_Coords())


    