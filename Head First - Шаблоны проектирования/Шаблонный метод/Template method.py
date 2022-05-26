from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print('Кипятим воду')

    def pour_in_cup(self):
        print('Выливаем в кружку')


class Coffee(CaffeineBeverage):

    def brew(self):
        print('Добавляем зёрна кофе')

    def add_condiments(self):
        print('Добавляем сахар и молоко')


class Tea(CaffeineBeverage):

    def brew(self):
        print('Добавляем чайный пакетик')

    def add_condiments(self):
        print('Добавляем лимон')


class CaffeineBeverageWithHook(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print('Кипятим воду')

    def pour_in_cup(self):
        print('Выливаем в кружку')

    def customer_wants_condiments(self):
        return True


class CoffeeWithHook(CaffeineBeverageWithHook):

    def brew(self):
        print('Добавляем зёрна кофе')

    def add_condiments(self):
        print('Добавляем сахар и молоко')

    def customer_wants_condiments(self):
        answer = input('Вы хотите добавить приправы? : ')
        if answer.lower() in ['y', 'yes', 'да', 'д']:
            return True
        else:
            return False


if __name__ == '__main__':
    t = Tea()
    c = CoffeeWithHook()
    c.prepare_recipe()
