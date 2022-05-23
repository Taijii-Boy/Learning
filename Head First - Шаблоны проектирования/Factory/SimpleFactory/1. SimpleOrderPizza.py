from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def prepare(self):
        print('Готовим пиццу')

    def bake(self):
        print('Печем пиццу')

    def cut(self):
        print('Нарезаем пиццу')

    def box(self):
        print('Упаковываем пиццу')


class CheesePizza(Pizza):
    pass


class GreekPizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class OrderPizza:
    def __init__(self, pizza_type: str):
        self.__pizza_type = pizza_type
        if self.__pizza_type == 'cheese':
            pizza = CheesePizza(self.__pizza_type)
        elif self.__pizza_type == 'greek':
            pizza = GreekPizza(self.__pizza_type)
        elif self.__pizza_type == 'pepperoni':
            pizza = PepperoniPizza(self.__pizza_type)
        self.make_pizza(pizza)

    def make_pizza(self, pizza: Pizza) -> Pizza:
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

if __name__ == '__main__':
    pizza = OrderPizza('cheese')

