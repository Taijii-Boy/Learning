"""Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она реализовала
методы set_kg() - для задания нового значения килограммов, get_kg() - для вывода текущего значения кг.
Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений.
Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже."""

# class KgToPounds:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def set_kg(self, new_kg):
#         if isinstance(new_kg, (float, int)):
#             self.__kg = new_kg
#         else:
#             raise ValueError('Килограммы должны быть числами!')
#
#     def get_kg(self):
#         return self.__kg


# class KgToPounds:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def __set_kg(self, new_kg):
#         if isinstance(new_kg, (float, int)):
#             self.__kg = new_kg
#         else:
#             raise ValueError('Килограммы должны быть числами!')
#
#     def __get_kg(self):
#         return self.__kg
#
#     kg = property(__get_kg, __set_kg)



class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (float, int)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы должны быть числами!')



amount = KgToPounds(200)
print(amount.to_pounds())
amount.kg = 100
print(amount.to_pounds())

