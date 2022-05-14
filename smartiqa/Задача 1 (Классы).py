"""
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
 (отвечающий за добавку к выбираемому лимонаду).
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
а иначе отобразится следующая фраза: «Обычная газировка».
При решении задания можно дополнительно проверить тип передаваемого аргумента: принимается только строка."""


class Soda:

    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')


my_drink_1 = Soda('Малина')
my_drink_1.show_my_drink()

my_drink_2 = Soda(123)
my_drink_2.show_my_drink()
