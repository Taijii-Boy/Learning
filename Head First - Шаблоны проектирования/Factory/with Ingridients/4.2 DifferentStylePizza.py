from abc import ABC, abstractmethod

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
            pizza = CheesePizza(NYPizzaIngredientFactory())
            pizza.name = 'Нью-йоркская сырная пицца'
        elif pizza_type == 'clam':
            pizza = ClamPizza(NYPizzaIngredientFactory())
            pizza.name = 'Нью-йоркская пицца c мидиями'
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(NYPizzaIngredientFactory())
            pizza.name = 'Нью-йоркская пицца пепперони'
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(NYPizzaIngredientFactory())
            pizza.name = 'Нью-йоркская вегетарианская пицца'
        else:
            pizza = CheesePizza(NYPizzaIngredientFactory())
            pizza.name = 'Нью-йоркская сырная пицца'
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            pizza = CheesePizza(ChicagoIngredientFactory())
            pizza.name = 'Чикагская сырная пицца'
        elif pizza_type == 'clam':
            pizza = ClamPizza(ChicagoIngredientFactory())
            pizza.name = 'Чикагская пицца c мидиями'
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(ChicagoIngredientFactory())
            pizza.name = 'Чикагская пицца пепперони'
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(ChicagoIngredientFactory())
            pizza.name = 'Чикагская вегетарианская пицца'
        else:
            pizza = CheesePizza(ChicagoIngredientFactory())
            pizza.name = 'Чикагская сырная пицца'
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
