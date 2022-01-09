# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)
# finally:
#     print('Блок finally выполняется всегда')


def get_values():
    try:
        x, y = map(int, input().split())
        return x, y

    except ValueError as z: 
        print(z)
        return (0, 0)
    finally:
        print('Блок finally выполняется до return')


x, y = get_values()
print(x, y)