from abc import ABC


class Beverage(ABC):
    def get_description(self):
        return ''


class Tea(Beverage):
    def __init__(self):
        self.cost = 0.89
        self.description = 'Вкусный чай'

    def get_description(self):
        return self.description


class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage
        self.description = None

    def get_description(self):
        return f'{self.beverage.get_description()} + {self.description}'


class Chocolate(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.cost = 0.1
        self.description = 'Шоколад'



if __name__ == '__main__':
    t = Tea()
    bever = Chocolate(t)
    print(bever.get_description())
