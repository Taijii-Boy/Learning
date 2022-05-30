from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    def __init__(self, name: str, dough: str, sauce: str):
        self.__name: str = name
        self.__dough: str = dough
        self.__sauce: str = sauce
        self.__topping: List[str] = []

    def prepare(self):
        print('_'*50)
        print(f'Готовим пиццу {self.__name}')
        print(f'Месим {self.__dough}')
        print(f'Добавляем {self.__sauce}')
        print('==================')
        print('Добавляем топинг:')
        for topping in self.__topping:
            print(topping)
        print('==================')

    def bake(self):
        print(f'Печем пиццу 25 минут при 350 градусах')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки клиньями')

    def box(self):
        print(f'Упаковываем пиццу {self.__name}')
        print('_'*50)

    @property
    def name(self) -> str:
        return self.__name

    def add_toppings(self, top: str):
        self.__topping.append(top)


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(name='Нью-Йоркская сырная пицца',
                         dough='тонкая основа с корочкой',
                         sauce='соус Маринара'
                         )
        self.add_toppings('реджано')
        self.add_toppings('чеснок')


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__(name='Нью-Йоркская пицца Пепперони',
                         dough='тонкая основа с корочкой',
                         sauce='соус Маринара'
                         )
        self.add_toppings('реджано')
        self.add_toppings('грибы')
        self.add_toppings('лук')
        self.add_toppings('красный перец')
        self.add_toppings('пепперони')


class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__(name='Нью-Йоркская пицца с мидиями',
                         dough='тонкая основа с корочкой',
                         sauce='соус Маринара'
                         )
        self.add_toppings('реджано')
        self.add_toppings('свежие мидии')


class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__(name='Нью-Йоркская вегетарианская пицца',
                         dough='Тонкая основа с корочкой',
                         sauce='соус Маринара'
                         )
        self.add_toppings('реджано')
        self.add_toppings('грибы')
        self.add_toppings('лук')
        self.add_toppings('красный перец')


class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super().__init__(name='Чикагская сырная пицца',
                         dough='ультра толстая основа с корочкой',
                         sauce='соус томатный'
                         )
        self.add_toppings('моцарелла')
        self.add_toppings('пармезан')
        self.add_toppings('орегано')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки квадратами')


class ChicagoPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__(name='Чикагская пицца Пепперони',
                         dough='ультра толстая основа с корочкой',
                         sauce='соус томатный'
                         )
        self.add_toppings('моцарелла')
        self.add_toppings('пармезан')
        self.add_toppings('орегано')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки квадратами')


class ChicagoClamPizza(Pizza):
    def __init__(self):
        super().__init__(name='Чикагская пицца с мидиями',
                         dough='ультра толстая основа с корочкой',
                         sauce='соус томатный'
                         )
        self.add_toppings('моцарелла')
        self.add_toppings('пармезан')
        self.add_toppings('мидии')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки квадратами')


class ChicagoVeggiePizza(Pizza):
    def __init__(self):
        super().__init__(name='Чикагская вегетарианская пицца',
                         dough='ультра толстая основа с корочкой',
                         sauce='соус томатный'
                         )
        self.add_toppings('моцарелла')
        self.add_toppings('пармезан')
        self.add_toppings('мидии')
        self.add_toppings('баклажан')
        self.add_toppings('шпинат')
        self.add_toppings('оливки')

    def cut(self):
        print(f'Нарезаем пиццу на кусочки квадратами')


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
