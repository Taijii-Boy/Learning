from contextlib import contextmanager

class Resource:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f'Resource was opened with args {args}')
        self.opened = True

    def close(self):
        print('Resource was closed!')
        self.opened = False

    def __del__(self):
        if self.opened:
            print('Memory leak detection! Resource was not closed')

    def action(self):
        print('Do something with resource')


# 1 способ написания контекстного менеджера:

@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource
    except Exception:
        raise
    finally:
        if resource:
            resource.close()


# 2 способ написания через класс:

class ResourceWorker:
    def __init__(self, *args):
        self.args = args
        self.resource = None

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()
            # return True  # если вернуть True - не будет выброшено исключение, если произойдёт


if __name__ == '__main__':
    # 1 способ:

    # with open_resource(1, 2, 3) as res:
    #     res.action()
    #     raise ValueError('Stop')

    # 2 способ:
    with ResourceWorker(1, 2, 3) as res:
        res.action()



