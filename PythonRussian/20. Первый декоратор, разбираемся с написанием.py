# Функция - полноправный объект
# Внутренняя функция может захватывать переменные из внешней

# def summ(a, b):
#     return a + b


# def example(func):
#     print(f'{func.__name__}')


# function = summ
# print(summ)
# print(function)
# example(summ)

# ------------------------------------------------------
# Внутренняя функция может захватывать переменные из внешней


# def example(a):
#     def inner(b):
#         print(a + b)
#
#     inner(3)
#
#
# example(5)


# ------------------------------------------------------

def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b): # В этот меомент summ = wrapper
    return a + b

print(summ(1, 2))
# function = logger(summ)
# print(function(1, 2))

# То же самое, что и function(logger)(1,2)
# или summ = logger(summ)
