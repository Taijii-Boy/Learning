from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    def __init__(self, name: str, dough: str, sauce: str):
        self.__name: str = name
        self.__dough: str = dough
        self.__sauce: str = sauce
        self.__topping: List[str] = []

    def prepare(self):
        print(f'Готовим пиццу {self.__name}')
        print(f'Месим {self.__dough}')
        print(f'Добавляем {self.__sauce}')
        print('Добавляем топинг:')
        for topping in self.__topping:
            print(topping)

    def bake(self):
        print(f'Печем пиццу 25 минут при 350 градусах')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки клиньями')

    def box(self):
        print(f'Упаковываем пиццу {self.__name}')

    @property
    def name(self) -> str:
        return self.__name

    def add_toppings(self, top: str):
        self.__topping.append(top)


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(name='NY Style Sauce and Cheese Pizza',
                         dough='Тонкая основа с корочкой',
                         sauce='Соус Маринара'
                         )
        self.add_toppings('Сыр "Реджано"')


class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super().__init__(name='Chicago Style Deep Dish Cheese Pizza',
                         dough='Ультра толстая основа с корочкой',
                         sauce='Соус томатный'
                         )
        self.add_toppings('Сыр "Моцарелла"')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки квадратами')


class NYStylePepperoniPizza(Pizza):
    pass


class ChicagoPepperoniPizza(Pizza):
    pass


class NYStyleClamPizza(Pizza):
    pass


class ChicagoClamPizza(Pizza):
    pass


class NYStyleVeggiePizza(Pizza):
    pass


class ChicagoVeggiePizza(Pizza):
    pass


class NYPizzaFactory:
    ...


class ChicagoPizzaFactory:
    ...


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
        # elif pizza_type == 'clam':
        #     pizza = NYStyleClamPizza()
        # elif pizza_type == 'pepperoni':
        #     pizza = NYStylePepperoniPizza()
        # elif pizza_type == 'veggie':
        #     pizza = NYStyleVeggiePizza()
        # else:
        #     pizza = NYStyleCheesePizza('cheese')
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            pizza = ChicagoCheesePizza()
        # elif pizza_type == 'clam':
        #     pizza = ChicagoClamPizza()
        # elif pizza_type == 'pepperoni':
        #     pizza = ChicagoPepperoniPizza()
        # elif pizza_type == 'veggie':
        #     pizza = ChicagoVeggiePizza()
        # else:
        #     pizza = ChicagoCheesePizza()
        return pizza


class PizzaTestDrive:
    def main(self):
        ny_pizza_store = NYPizzaStore()
        chicago_pizza_store = ChicagoPizzaStore()

        pizza = ny_pizza_store.order_pizza('cheese')
        print(f'Ethan ordered a {pizza.name}\n')

        pizza = chicago_pizza_store.order_pizza('cheese')
        print(f'Joel ordered a {pizza.name}\n')


if __name__ == '__main__':
    test = PizzaTestDrive()
    test.main()
