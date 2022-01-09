class ThreadData:
    __shared_attrs = {
        'name': 'thread1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


td = ThreadData()
td2 = ThreadData()
td2.name = 'Вова'
td2.new_attr = 'Петя'

print(td.__dict__)
print(td2.__dict__)