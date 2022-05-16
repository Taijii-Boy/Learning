# def summ(a, b):
#     return a + b
#
#
# def logger(func):
#     def wrapper(*args):
#         print(f'{func.__name__} started')
#         result = func(*args)
#         print(f'{func.__name__} end')
#         return result
#
#     return wrapper

def typed(type_):
    def real_decorator(function):
        def wrapped(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Тип должен быть {type_.__name__}')
            return function(*args)
        return wrapped
    return real_decorator


@typed(int)
def calculate(a, b, c):
    # Logic
    return a + b + c


@typed(str)
def convert(a, b):
    # Logic
    return a + b


if __name__ == '__main__':
    # # summ = logger(summ)
    # # print(summ(2, 3))
    #
    # # print(logger(summ)(2, 3))
    # wrapper = logger(summ)

    # calculate = typed_int(calculate)
    print(calculate(1, 2, 3))
    print(convert('1', ' Biba'))
