# a_list = [1, 0, True]
# print(all(a_list)) # Если все элементы - True, то вернет True
# print(any(a_list)) # Если хотя бы один элемент True - вернёт True

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a_list = []
# print(bool(a_list))  # Для пустого списка bool возвращает False
# print(all(a_list))  # All для пустого списка возвращает True, т.к. в цикле ищет False. Если находит - возвращает)
# print(any(a_list))  # Any для пустого списка возвращает False, т.к. ищет в цикле True и не находит

# # Для проверки пустотности списка как раз удобно использовать any:
# if any(a_list):
#     pass

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Фильтр
# Лучше использовать listcomp, но иногда можно использовать filter. Например, в том же примере
# мы хотим распечатать ненулевые элементы
#
# a_list = [0, 0, 0, "Tom", False, 0.0, True]
# if any(a_list):
#     print(list(filter(None, a_list)))
# # Можно не указывать лямбду, а указать None - фильтр поймёт, что ему в этом случае
# # нужно возвращать только True элементы
#
#     print([e for e in a_list if e])  # Можно использовать listcomp для того же самого

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # MIN и MAX
# a_list = ['aaa', 'bbz', 'cc', 'd', ]
# print(max(a_list))  # Сравнивает по порядку в алфавите первой буквы
# print(max(a_list, key=len)) #  Сравнивает количество символов

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name =}, {self.age=}'


cats = [Cat('Tom', 3), Cat('Angela', 2), Cat('Boba', 5)]
# print(max(cats, key=lambda cat: cat.name))  # Max для имени по алфавиту
# print(max(cats, key=lambda cat: len(cat.name)))  # Max по длине имени
# print(max(cats, key=lambda cat: cat.age))  # Max для возраста


# # Использование итератора
# for cat in cats:
#     print(cat)
#
# # Этот цикл то же самое, что и такой:
# for cat in iter(cats):
#     print(cat)
#
# # Такая форма будет использовать функцию func до тех пор, пока в переборе не встретит второй аргумент - None
# for cat in iter(func, None):
#     pass

# # Вводим значения до тех пор, пока не введём end
# for line in iter(input, 'end'):
#     print(line.upper())

# То же самое для формирования списка
ints = [int(e) for e in iter(input, '')]
print(ints)




