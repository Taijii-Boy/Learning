from abc import ABC


class Beverage(ABC):
    def __init__(self):
        self.description = None
        self.cost = None

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class HouseBlend(Beverage):
    def __init__(self):
        self.cost = 0.89
        self.description = 'Домашняя смесь'


class DarkRoast(Beverage):
    def __init__(self):
        self.cost = 0.99
        self.description = 'Темная обжарка'


class Espresso(Beverage):
    def __init__(self):
        self.cost = 1.99
        self.description = 'Эспрессо'


class Decaf(Beverage):
    def __init__(self):
        self.cost = 1.05
        self.description = 'Без кофеина'


class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        self.description = f'{self.beverage.get_description()} + {self.description}'
        print(f'Напиток: {self.description}')
        print(f'Цена напитка: {self.get_cost()}')

    def get_cost(self):
        return self.beverage.get_cost() + self.cost


class Milk(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.cost = 0.1
        self.description = 'Молочная пена'


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.cost = 0.2
        self.description = 'Шоколад'


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.cost = 0.15
        self.description = 'Соя'


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.cost = 0.1
        self.description = 'Взбитые сливки'


if __name__ == '__main__':
    beverage = Whip(Espresso())
    beverage.get_description()
    print(beverage.cost)
