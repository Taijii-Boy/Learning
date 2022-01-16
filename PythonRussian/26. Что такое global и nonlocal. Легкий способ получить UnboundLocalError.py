# global и nonlocal нужны только для изменения значений. Print работает и без них
# global создает (!) переменную в глобальном скопе. Даже если не задать counter = 1, он её создаст
# global - "Ищи сразу в глобальной области видимости, а не в локальной"
# nonlocal - "Не ищи глобально и не ищи локально. Ищи в области Enclosed (LEGB - rules), т.е. в ту функцию, куда вложен"
# nonlocal работает во множнственном вложении до первого вложения, но не дальше
# nonlocal в отличие от global не создает (!) переменную
# Нужно стараться не использовать global и nonlocal

# counter = 1

# Без global:
# def increment():
#     # counter += 1 # Будет ошибка без global
#     print(counter)


# Использование global. Мы говорим "Ищи сразу в глобальной области видимости, а не в локальной"

# def increment():
#     global counter
#     counter += 1
#     print(counter)
# ---------------------------------------------------

# def increment():
#     global counter
#     counter = 100
#     print(counter)
# ---------------------------------------------------
# counter = 100
#
#
# def increment():
#     counter = 0
#
#     def inner():
#         # global counter
#         nonlocal counter
#         counter += 1
#         print(counter)
#
#     inner()
#
#
# if __name__ == '__main__':
#     increment()

# ---------------------------------------------------
# Как избежать global:

counter = 100


def increment(value):
    return value + 1


if __name__ == '__main__':
    counter = increment(counter)
    print(counter)
