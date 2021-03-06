# позиционные аргументы всегда идут в начале
# def example(a, b, /, c):  - все что слева от / - позиционные аргументы
# def example(a, b, /, c, *, d):  - все что справа от * - только ключевые аргументы
# *args собирает все позиционные аргументы в кортеж
# **kwargs собирает все ключевые аргументы в словарь


# a, b, c = [1, 2, 3]
# a, b, c = 'abc'
# a, b, c = [1, 2]  # Недостаточно элементов для распаковки
# a, *b, c = [1, 2]
# a, *b = [1, 2, 3]  # Первое значение в a, * - Всё остальное
# a, *b = 'abcd'  # Распаковка возвращает в b список, а не строку
# *a, b = 'abcd'  # Всё кроме последнего
# a, *_, c = 'abcd'  # Только первый и последний
#
# print(f'{a=}')
# print(f'{b=}')
# print(f'{c=}')

# print(*[1, 2, 3])  # Возьмёт по одному элементу и выведет на экран. Та же распаковка

# --------------------------------------------------------------------
# def example(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# example(1, 2, 3)  # позиционные аргументы
# example(a=1, b=2, c=3)  # ключевые аргументы
# --------------------------------------------------------------------
def my_print(*args, **kwargs):
    print(f'Got keywords: {kwargs}')
    for arg in args:
        print(str(arg), **kwargs)


# my_print(1, 2, 3, 4, 5, sep=':', end='-')
print(1, 2, **{'sep': ':', 'end': '-'})
