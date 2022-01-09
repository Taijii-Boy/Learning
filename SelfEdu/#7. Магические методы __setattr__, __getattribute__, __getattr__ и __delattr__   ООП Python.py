
class Point:
    '''Класс создает точки по заданным координатам'''

    MAX_COORD = 100
    MIN_COORD = 0

    # __slots__ = ['__x', '__y'] # Разрешенные свойства экземпляров класса в коллекции __slots__ (В самом классе могут быть любые)
  
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # def set_Coords(self, x, y):
    #     if self.MIN_COORD <= x <= self.MAX_COORD:
    #         self.x = x
    #         self.y = y


    # def __getattribute__(self, item):
    #     '''Автоматически вызывается при получении свойства через экземпляр класса с именем item'''

    #     print("Вызван магический метод __getattribute__")
    #     if item == "x":
    #         raise ValueError("Доступ запрещен")
    #     else:  
    #         return object.__getattribute__(self, item) 

    
    def __setattr__(self, key, value):
        ''' Автоматически вызывается при изменении свойства key класса'''
        if key == "x":
            raise AttributeError("недопустимое имя атрибута")
        else:
            self.__dict__[key] = value
        print("Вызван магический метод __setattr__")


    def __getattr__(self, item):
        '''Автоматически вызывается при получении несуществующего свойства класса с именем item'''
        print("Я перегруженный метод __getattr__, переменная - ", item) 


    def __delattr__(self, item):
        '''Автоматически вызывается при удалении свойства item (не важно - существует оно или нет)'''
        print("Я перегруженный метод __delattr__, переменная - ", item)

    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left


pt = Point(1, 2)
a = pt.x
print(a)
# pt.set_bound(22)