from abc import ABC, abstractmethod
from typing import List

from Ingridients import *


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self) -> List:
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaSouce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FleshClams()


class ChicagoIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSouce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        veggies = [Spinach(), BlackOlives(), EggPlant()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()
