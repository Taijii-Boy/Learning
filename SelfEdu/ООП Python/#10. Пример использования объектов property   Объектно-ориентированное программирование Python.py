from string import ascii_letters
from typing import Type

class Person:
    S_RUS = 'абвгдеёжзиийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split() # сеттера нет, используем __fio
        self.old = old          # Используем не __old потому что для old у нас есть setter с дополнительной проверкой
        self.passport = ps
        self.weight = weight


    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы 1 сивол")
            if len(s.strip(letters)) != 0: #Все символы, не входящие в letters удаляются
                raise TypeError("В ФИО используются только буквенные символы и дефис")


    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом от 14 до 120") 


    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("Возраст должен быть вещественным числом от 20 и выше")

    
    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Серия и номер паспорта должны быть строкой")

        s = ps.split()
        if len(s) != 2  or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")


    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter   
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter   
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight



p = Person("Сорокин Алексндр Игоревич", 32, "1234 111111", 78.0)
p2 = Person("Васькин Василий Васильевич", 23, "1233 333333", 65.2)