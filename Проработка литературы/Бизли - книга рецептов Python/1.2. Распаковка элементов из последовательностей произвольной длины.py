# 1.2. Распаковка элементов из последовательностей произвольной длины
# Задача
# Вам нужно распаковать N элементов из итерируемого объекта, но этот объект может содержать больше N элементов,
# что вызывает исключение «too many values to unpack» («слишком много значений для распаковки»).
#  --------------------------------------------

# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)
#  --------------------------------------------

# record = ('Dave', 'dave@example.com', '773-555-1212', '873-782-1212')
# name, mail, *phone_numbers = record
# print(name)
# print(phone_numbers)

#  --------------------------------------------
# sales_record = [1, 2, 3, 4, 55, 62, 11, 323, 51, 12, 2, 34]
#
#
# def avg_comparison(record):
#     *trailing, current = record
#     trailing_avg = sum(trailing)/len(trailing)
#     print(trailing)
#     print(current)
#     return trailing_avg
#
#
# print(avg_comparison(sales_record))
#  --------------------------------------------
# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]
#
#
# def do_foo(x, y):
#     print('foo', x, y)
#
#
# def do_bar(s):
#     print('bar', s)
#
#
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
#  --------------------------------------------
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname)
# print(homedir)
# print(sh)
# ----------------------------------------------
# record = ('ACME', 50, 123.45, (12, 18, 2012))
# name, *_, (*_, year) = record
# print(name)
# print(year)
# ----------------------------------------------


def sum_(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum_([1, 2, 3, 4, 5, 6, 7, 8]))