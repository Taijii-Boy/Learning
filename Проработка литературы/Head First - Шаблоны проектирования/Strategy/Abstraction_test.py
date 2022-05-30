from abc import abstractmethod, ABC


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print('Гав-гав!')


class Cat(Animal):

    def make_sound(self):
        print('Мяяяу!')

