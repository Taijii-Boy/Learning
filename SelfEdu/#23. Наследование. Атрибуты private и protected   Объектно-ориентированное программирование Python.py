class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Geom класса {self.__class__}')
        self.__verify_coord(x1)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def get_coords(self):
        return (self._x2, self._y2)

    def __verify_coord(self, coord):
        return 0 <= coord < 100

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill = 'red'):
        super().__init__(x1, y1, x2, y2)
        print('Инициализатор класса Rect')
        self._fill = fill




r = Rect(0, 0, 10, 20)
print(r.get_coords())
print(r.__dict__)