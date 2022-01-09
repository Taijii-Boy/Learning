
class Clock:
    __DAY = 86400 # Число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        
        self.seconds = seconds % self.__DAY

    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    
    def __add__(self, other): # self - объект слева от "+", other - справа
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other  # Для случая 100 + c1, когда экземпляр класса справа от числа


    def __iadd__(self, other): # для случая c1 += 100
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds

        self.seconds += sc
        return self  # В этом случае мы не создаем нового экземпляра класса
        

c1 = Clock(1000)
c2 = Clock(2000)
c1 = 100 + c1
c3 = c1 + c2
print(c1.get_time())
print(c3.get_time())