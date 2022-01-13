try:
    x, y = map(int, input("Введите два числа через пробел: ").split())
    res = x / y
except ValueError:
    print("Ошибка типа данных")
# except ZeroDivisionError:
#     print("Деление на ноль недопустимо")

except ArithmeticError:
    print("Арифметическая ошибка")
print("Завершили")


