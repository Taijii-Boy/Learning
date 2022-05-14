from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print('Я лечуууу!')


class FlyNoWay(FlyBehavior):
    def fly(self):
        print('Я не умею летать!')


class QuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('Квааа!')


class Squeak(QuackBehavior):
    def quack(self):
        print('Пии!')


class MuteQuack(QuackBehavior):
    def quack(self):
        print('Я с вами не разговариваю!')


class Duck(ABC):
    def __init__(self):
        self._fly_behavior = FlyBehavior()
        self._quack_behavior = QuackBehavior()

    def swim(self):
        print('Уточка плавает!')

    @abstractmethod
    def display(self):
        pass

    def quack(self):
        self.quack_behavior.quack()

    def fly(self):
        self.fly_behavior.fly()

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, new_behavior):
        self._fly_behavior = new_behavior

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, new_behavior):
        self._quack_behavior = new_behavior


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print('Я кряква!')


class RedheadDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Squeak()

    def display(self):
        print('Я красноголовая утка!')


class RubberDuck(Duck):
    def display(self):
        print('Я резиновая уточка!')


class DecoyDuck(Duck):
    def display(self):
        print('Я манок!')


mal_duck = MallardDuck()
mal_duck.display()
mal_duck.quack()
mal_duck.fly()

mal_duck.fly_behavior = FlyNoWay()
mal_duck.fly()
