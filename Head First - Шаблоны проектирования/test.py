from abc import ABC, abstractmethod


class IPizzaBase(ABC):
    """Интерфейс декорируемого объекта"""
    @abstractmethod
    def cost(self) -> float:
        pass


class PizzaBase(IPizzaBase):
    """Декорируемый класс"""
    def __init__(self, base_cost):
        self.__cost = base_cost

    def cost(self) -> float:
        return self.__cost


class IDecorator(IPizzaBase):
    """Интерфейс декоратора"""

    @abstractmethod
    def name(self) -> str:
        pass


class PizzaMargarita(IDecorator):
    """На основе PizzaBase получаем
    пиццу Маргарита"""

    def __init__(self, wrapped: IPizzaBase, cost: float):
        self.__wrapped = wrapped
        self.__cost = cost
        self.__name = 'Маргарита'

    def name(self) -> str:
        return self.__name

    def cost(self) -> float:
        return self.__cost + self.__wrapped.cost()


class PizzaSalami(IDecorator):
    """На основе PizzaBase получаем
    пиццу Салями"""

    def __init__(self, wrapped: IPizzaBase, cost: float):
        self.__wrapped = wrapped
        self.__cost = cost
        self.__name = 'Салями'

    def name(self) -> str:
        return self.__name

    def cost(self) -> float:
        return (self.__cost + self.__wrapped.cost())*2


if __name__ == '__main__':
    pizza_base = PizzaBase(3.5)
    margarita = PizzaMargarita(pizza_base, 4)
    print(f'Имя пиццы: {margarita.name()}\nСтоимость: {margarita.cost()}')
