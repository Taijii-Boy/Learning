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

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен быть int или Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other): # для != тоже работает __eq__, если в c1 не переопределен метод !=(__ne__): с1 != с2  => not(c1 == c2)
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __ne__(self, other): # !=
        sc = self.__verify_data(other)
        return self.seconds != sc
 
    def __lt__(self, other): # Сравнение на <
        sc = self.__verify_data(other)  # Для > тоже работает, если оператор >(__gt__) не реализован в c1 : c1 > c2 => c2 < c1
        return self.seconds < sc

    def __gt__(self, other): # Сравнение на >
        sc = self.__verify_data(other)  
        return self.seconds > sc

    def __le__(self, other): # Сравнение на <=
        sc = self.__verify_data(other)  # Для >= тоже работает, если оператор >=(__le__) не реализован в c1 : c1 >= c2 => c2 <= c1
        return self.seconds <= sc

    def __ge__(self, other): # Сравнение на <=
        sc = self.__verify_data(other)  
        return self.seconds >= sc   


c1 = Clock(1000)
c2 = Clock(1000) 
print(c1 == 1000)