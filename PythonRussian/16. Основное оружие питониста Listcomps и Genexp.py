# import pprint
from time import sleep

# list comprehension = listcomps
# Generator expressions = genexp
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# Переменные в listcomps - локальные, они недоступны снаружи
# Читается слева направо
# для словаря обязательно указывается КЛЮЧ: ЗНАЧЕНИЕ
# Генератор вернет объект, а не коллекцию
# Генератор ленивый. Не выполняет действий и не занимает память, пока не потребуется
# Генератор проверяет источник при создании!!! Если источник - большая функция - аккуратно! Он её выполнит
# генератор одноразовый. Если исчерпан, то бросает StopIteration
# Цикл For перехватывает StopIteration(мы не увидим исключение)

# Фильтр + преобразование
squares = [x ** 2 for x in range(10) if x % 2 == 0]

# Преобразование
text = 'hello world'
words = [word.capitalize() for word in text.split()]

# Фильтр
ints = [-1, -2, 0, 3, -4]
positives = [x for x in ints if x > 0]

# Обычный цикл выглядел бы так
squares2 = []
for e in range(10):
    if e > 0:
        squares2.append(e * e)

# Двойной цикл:
letters = [letter for word in text.split() for letter in word if letter < 'l']

# Матрица
matrix = [list(range(x, x + 3)) for x in range(3)]

# Set-comp. Множество
unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

# Словарь
alphabet = {index: letter for index, letter in enumerate('abcdefghijklmopqrstuvyxwz', 1)}

# Поменять местами КЛЮЧ: ЗНАЧЕНИЕ
alphabet_reversed = {value: key for key, value in alphabet.items()}

# Genexp
big_gen = (x for x in range(10_000_000_000_000) if x % 2 == 0)


# Генератор выполняет функцию!!! проверяет источник!
def some_source():
    print('!!!')
    sleep(3)
    return [1, 2, 3]


# Генератор иссякает! После того как выдаст все значения, его нужно создавать заново
positives_gen = (e for e in ints if e > 0)

if __name__ == '__main__':
    # pprint.pprint(matrix, indent=1, width=15)
    # gen = [e for e in some_source()]
    print()
