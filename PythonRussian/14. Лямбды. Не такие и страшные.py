# аналог def
# можно писать все, что допустимо после return в def
# lambda не выполянется до вызова!!!
# Можно писать без лямбд!

from operator import attrgetter, itemgetter


def square(x):
    return x ** 2

# square2 = lambda x: x**2
even_odd = lambda x: 'EVEN' if x%2 == 0 else 'ODD'


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Cat {self.name} age is {self.age}'


if __name__ == '__main__':
    # четное , не четное
    # print(even_odd(1))
    # print(even_odd(2))

    # Возможная ошибка:
    # x = 2
    # result = lambda: x**2
    # x = 3
    # result2 = lambda: x**2
    # print(result())
    # print(result2())

    # Чтобы избежать ошибку:
    # x = 2
    # result = lambda n=x: n**2
    # x = 3
    # result2 = lambda n=x: n**2
    # print(result())
    # print(result2())


    # Фильтрация и сортировка - самое частое использование лямбд:
    # Фильтрация

    # ints = list(range(10))
    # print(list(map(lambda y: y**2, filter(lambda x: x%2 == 0, ints))))
    # # это все можно заменить на более читаемый вариант без лямбд:
    # print([x**2 for x in ints if x%2 ==0])

    # # Сортировка словарей
    # a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4} # items - ('a', 3)
    # print(sorted(a_dict.items(), key = lambda x:x[0]))
    # print(sorted(a_dict.items(), key = lambda x:x[1]))
    # ## Можно использовать itemgetter из библиотеки operator для упрощения:
    # print(sorted(a_dict.items(), key = itemgetter(0)))
    # print(sorted(a_dict.items(), key = itemgetter(1)))


    # Фильтрация классов
    cats = [Cat('Tom', 2), Cat('Angela', 3)] 
    print(sorted(cats, key = lambda cat: cat.name))
    print(sorted(cats, key = lambda cat: cat.age))
    
    # Можно использовать attrgetter из библиотеки operator для упрощения:
    print(sorted(cats, key = attrgetter('name')))
    print(sorted(cats, key = attrgetter('age')))
