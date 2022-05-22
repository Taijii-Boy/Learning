from abc import ABC


class Pizza(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def prepare(self):
        print(f'Готовим пиццу {self.__name}')

    def bake(self):
        print(f'Печем пиццу {self.__name}')

    def cut(self):
        print(f'Нарезаем пиццу {self.__name}')

    def box(self):
        print(f'Упаковываем пиццу {self.__name}')


class CheesePizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class VeggiePizza(Pizza):
    pass


class SimplePizzaFactory:

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            pizza = CheesePizza(pizza_type)
        elif pizza_type == 'clam':
            pizza = ClamPizza(pizza_type)
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(pizza_type)
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(pizza_type)
        else:
            pizza = CheesePizza('cheese')
        return pizza


class PizzaStore:
    def __init__(self, factory):
        self.__factory = factory

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.__factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


if __name__ == '__main__':

    store = PizzaStore(SimplePizzaFactory())
    pizza = store.order_pizza('cheese')
