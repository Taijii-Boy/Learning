class PropertyObservable:
    """Наблюдатель свойств. Информирует об изменениях свойств. Подмешиваем в функции"""
    def __init__(self):
        self.property_changed = Event()


class MyClass(PropertyObservable):

    def __init__(self):
        super().__init__()
        self.__flag = True

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, value):
        if self.__flag == value:
            return
        self.__flag = value
        self.property_changed('flag', value)


class Event(list):
    """Список функций, которые необходимо вызывать всякий раз, когда происходит событие"""
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


if __name__ == '__main__':

    def param_changed(name, value):
        """Что нужно делать при изменении параметра"""
        if name == 'flag':
            print(f'Param has changed to {value}')


    my = MyClass()
    my.property_changed.append(param_changed) # связываем экземпляр класса с функцией

    my.flag = False


