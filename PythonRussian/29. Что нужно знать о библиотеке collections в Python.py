# OrderedDict нужен для действий сло словарем, где необходим порядок элементов, например, сравнение с учетом
# порядка, перестановки элементов с сохранением порядка. Платим памятью!

# ChainMap нужен для логического объединения словарей. Например, для поиска информации.
# Копирования словарей не происходит. Но при изменениях меняется первый словарь!

# Counter считает количество встречающихся элементов в последовательности. Работает с hashable объектами. Часто
# используется для частотного анализа в текстах

# Defaultdict нужен для создания словаря со значением по умолчанию. Значение подставляется при обращении к
# несуществующему ключу

# Dequa работает как словарь, но она потокобезопасна, оперирует элементами с двух сторон (добавление и изъятие). Быстра

# namedtuple - именованный кортеж. Нужен для создания структуры данных, нечто среднее между стандартными типами
# и классом, быстрее классов. Неизменяем. Позволяет обращаться по имени атрибута, индексам


from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple
import csv
# --------------------------------------------------------------------------------

# first = {1: 1, 2: 2, 3: 3}  # С версии 3.7 Словарь хранит порядок, если он задан таким образом
# second = {2: 2, 1: 1}  # Но при сравнении встроенный словарь не проверяет порядок элементов
#
# order1 = OrderedDict(first)
# order2 = OrderedDict(second)
#
# # print(first)
# # print(first.popitem())
# # print(first)
# print(first == second)
# print(order1 == order2)  # Упорядоченный словарь учитывает порядок в сравнении
# # print(order1.popitem(last=False))  # Берем элемент с конца
# order1.move_to_end(1)  # Элемент с ключом 1 в конец словаря
# order1.move_to_end(3, last=False)  # В начало
# print(order1)
# --------------------------------------------------------------------------------
# first = {1: 1, 2: 2, 3: 3}
# second = {4: 4, 5: 5}
# chain = ChainMap(first, second)
# print(chain)
# print(1 in chain)
# print(5 in chain)
# chain[1] = 200  # Меняет в 1 словаре
# print(chain)
# chain[5] = 200  # Создаем новый объект (!) в первом словаре
# print(chain)
# --------------------------------------------------------------------------------

# counter = Counter('hello')
# print(counter)
# counter.update('world')
# print(counter)
# print(counter.most_common(3))
# --------------------------------------------------------------------------------
# a_dict = defaultdict(int)
# for char in 'hello':
#     a_dict[char] += 1
#
# print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))  # - То же самое, что и counter
# # --------------------------------------------------------------------------------
# a_dict = defaultdict(list)
# for char in 'hello':
#     a_dict[char].append(char)
#
# print(a_dict)


# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# a_deque = deque()
# a_deque.append(1)
# print(a_deque)
# a_deque.appendleft(2)
# print(a_deque)
# a_deque.append(3)
# print(a_deque)
# a_deque.popleft()
# print(a_deque)
# --------------------------------------------------------------------------------
# a_deque = deque([1, 2, 3], maxlen=3)
# print(a_deque)
# a_deque.append(4)
# print(a_deque)
# --------------------------------------------------------------------------------
# Выведем последние 2 строки в файле:

# with open('point.csv') as file:
#     a_deque = deque(file, maxlen=2)
#
# for line in a_deque:
#     print(line.rstrip())
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# tom = ('Tom', 4, 'yellow')
# Cat = namedtuple('Cat', 'name age color')
# tom = Cat('Tom', 4, 'yellow')
# print(tom)
# print(tom[0])
# print(tom.color)
# --------------------------------------------------------------------------------

Point = namedtuple('Point', 'x y')
with open('point.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)