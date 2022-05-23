from abc import ABC, abstractmethod
from typing import List
from Factory import NYPizzaIngredientFactory, ChicagoIngredientFactory, PizzaIngredientFactory


class Pizza(ABC):
    def __init__(self, name: str):
        self.__name: str = name

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print(f'Печем пиццу 25 минут при 350 градусах')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки клиньями')

    def box(self):
        print(f'Упаковываем пиццу {self.__name}')
        print('_' * 50)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value



class CheesePizza(Pizza):
    def __init__(self, factory: PizzaIngredientFactory):
        self.__factory = factory

    def prepare(self):
        print('_'*12, f'{self.name}', '_'*12)
        print('Готовим')
        dough = self.__factory.create_dough()
        sauce = self.__factory.create_sauce()
        cheese = self.__factory.create_cheese()
        veggies = self.__factory.create_veggies()


class ClamPizza(Pizza):
    def __init__(self, factory: PizzaIngredientFactory):
        self.__factory = factory

    def prepare(self):
        print(f'Готовим {self.name}')
        dough = self.__factory.create_dough()
        sauce = self.__factory.create_sauce()
        cheese = self.__factory.create_cheese()
        clam = self.__factory.create_clam()
        veggies = self.__factory.create_veggies()


class VeggiePizza(Pizza):
    def __init__(self, factory: PizzaIngredientFactory):
        self.__factory = factory

    def prepare(self):
        print(f'Готовим {self.name}')
        dough = self.__factory.create_dough()
        sauce = self.__factory.create_sauce()
        cheese = self.__factory.create_cheese()
        veggies = self.__factory.create_veggies()


class PepperoniPizza(Pizza):
    def __init__(self, factory: PizzaIngredientFactory):
        self.__factory = factory

    def prepare(self):
        print(f'Готовим {self.name}')
        dough = self.__factory.create_dough()
        sauce = self.__factory.create_sauce()
        cheese = self.__factory.create_cheese()
        pepperoni = self.__factory.create_pepperoni()
        veggies = self.__factory.create_veggies()

