class ChocolateBoiler:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        ChocolateBoiler.__instance = None

    def __init__(self):
        self.__empty = True
        self.__boiled = False

    def fill(self):
        if self.is_empty:
            self.__empty = False
            self.__boiled = False
            print('Заполнение нагревателя молочно-шоколадной смесью')

    def drain(self):
        if not self.is_empty and self.is_boiled:
            self.__empty = True
            print('Сливаем нагретое молоко и шоколад')

    def boil(self):
        if not self.is_empty and not self.is_boiled:
            self.__boiled = True
            print('Кипятим содержимое')

    @property
    def is_empty(self):
        return self.__empty

    @property
    def is_boiled(self):
        return self.__boiled
