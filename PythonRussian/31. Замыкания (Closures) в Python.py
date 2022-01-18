# Closure Замыкания
# Замыкание - это внутренняя функция, которая возвращается из внешней и использует переменные из внешнего скоупа
# Каждое замыкание хранит свое состояние, они не пересекаются
# Получается, что замыкание - это некий объект, хранящий состояние(данные) и предоставляет интерфейс для
# работы с данными. "Скрывает" данные.
# Может использоваться вместо глобальных переменных

def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner

# def average():
#     values = []
#
#     def inner(value: int) -> float:
#         values.append(value)
#         return sum(values)/len(values)
#
#     return inner
# --------------------------------------------------------------------

# def counter():
#     count = 0
#
#     def inner(value: int) -> int:
#         nonlocal count
#         count += value
#         return count
#
#     return inner
# --------------------------------------------------------------------

# def pow_(base):
#
#     def inner(value):
#         return value ** base
#
#     return inner
# --------------------------------------------------------------------

def pow_(base):
    return lambda value: value ** base  # - Замыкание через lambda-функцию





if __name__ == '__main__':
    # boys = names()
    # girls = names()
    # print(boys('Vasia'))
    # print(boys('Petya'))
    # print(boys('Dima'))
    # print(girls('Olga'))
    # print(girls('Ira'))
    # print(girls('Larisa'))
    # avg = average()
    # print(avg(10))
    # print(avg(20))
    # print(avg(30))

    # -----------------------------------------------
    # count = counter()
    # print(count(1))
    # print(count(1))
    # print(count(1))
    # print(count(-3))
    # -----------------------------------------------
    # p1 = pow_(2)
    # p2 = pow_(2)
    # print(p1(4))
    # print(p2(5))
    # -----------------------------------------------
    boys = names()
    boys('Vasia')
    print(boys.__closure__[0].cell_contents)  # - Чтобы дотянуться до содержания замыкания
