from abc import ABC, abstractmethod
from typing import List

from Factory import NYPizzaIngredientFactory, ChicagoIngredientFactory
from Pizza import *


class PizzaStore(ABC):

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        ...


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif pizza_type == 'clam':
            pizza = NYStyleClamPizza()
        elif pizza_type == 'pepperoni':
            pizza = NYStylePepperoniPizza()
        elif pizza_type == 'veggie':
            pizza = NYStyleVeggiePizza()
        else:
            pizza = NYStyleCheesePizza()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            pizza = ChicagoCheesePizza()
        elif pizza_type == 'clam':
            pizza = ChicagoClamPizza()
        elif pizza_type == 'pepperoni':
            pizza = ChicagoPepperoniPizza()
        elif pizza_type == 'veggie':
            pizza = ChicagoVeggiePizza()
        else:
            pizza = ChicagoCheesePizza()
        return pizza


class PizzaTestDrive:
    def main(self):
        ny_pizza_store = NYPizzaStore()
        chicago_pizza_store = ChicagoPizzaStore()

        pizza = ny_pizza_store.order_pizza('cheese')
        print(f'Доставляем {pizza.name} для Итэна\n')

        pizza = chicago_pizza_store.order_pizza('veggie')
        print(f'Доставляем {pizza.name} для Джулии\n')


if __name__ == '__main__':
    test = PizzaTestDrive()
    test.main()
