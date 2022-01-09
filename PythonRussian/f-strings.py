from datetime import datetime
a = 'Hello'
b = 'World'

today = datetime.now()
result = 200
c = f'{a} {b}'
pi = 3.141592
big_number = 12328193797289
real = 86.25
full = 100

# Для быстрого логирования:
# print(f'result = {result} - вариант "в лоб" ')
# print(f'{result = }')


# Перевод в другие системы счисления
# print(f'{result} - десятичная')
# print(f'{result:b} - двоичная')
# print(f'{result:o} - восьмеричная')
# print(f'{result:x} - шестнадцатеричная')

# Число точек после запятой
# print(f'{pi:.2f}')
# print(f'{pi:.5f}')

# Количество знаков в выводе
# print(f'{result:6}')
# print(f'{result:4}')
# print(f'{result:07} - добавляем нули перед')
# print(f'{result:^12} - в серединку')
# print(f'{result:<12} - слева')
# print(f'{result:>12} - справа')
# print(f'{result:0>12} - справа с нулями')
# print(f'{result:=>12} - справа с символами равно')

# Разделение запятой по разрядам
# print(f'{big_number:,}')

# # Вычисление функций
# print(f'{min(big_number, pi)}')

# Форматирование времени
# print(today, '- не читабельно')
# print(f'{today:%d-%m-%y %H:%M}')
# print(f'{today:%d.%m.%y, %H:%M:%S}')

# Считаем проценты
# print(f'{real/full:%}')
# print(f'{real/full:.2%}')
# print(f'{real/full:.0%}')