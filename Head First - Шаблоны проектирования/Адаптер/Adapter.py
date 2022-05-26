from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):

    def quack(self):
        print('Кряяяя!')

    def fly(self):
        print('Я лечу!')


class WildTurkey(Turkey):

    def gobble(self):
        print('Курлы!')

    def fly(self):
        print('Я летаю на короткие дистанции')


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()

class DuckAdapter(Turkey):
    def __init__(self, duck: Duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        self.duck.fly()

class DuckTestDrive:
    def main(self):
        duck = MallardDuck()
        turkey = WildTurkey()
        turkey_adapter = TurkeyAdapter(turkey)
        print('Индюшка говорит:')
        turkey.gobble()
        turkey.fly()
        print('Утка говорит:')
        duck.quack()
        duck.fly()
        print('Индутка говорит:')
        turkey_adapter.quack()
        turkey_adapter.fly()

    def test_duck(self, duck: Duck):
        duck.quack()
        duck.fly()


if __name__ == '__main__':
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)
    test = DuckTestDrive()
    test.test_duck(turkey_adapter)
