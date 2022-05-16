from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self._description = 'Unknown Beverage'

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage):
