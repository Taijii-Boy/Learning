from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'House Blend Coffee'

    def cost(self):
        return 0.89


class CondimentDecorator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class Milk(CondimentDecorator):
    def cost(self):
        return 0.1

    def get_description(self):
        return 
