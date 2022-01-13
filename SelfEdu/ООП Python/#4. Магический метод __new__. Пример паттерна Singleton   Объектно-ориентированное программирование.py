
## Пример реализации магического метода __new__
# class Point:

#     def __new__(cls, *args, **kwargs):
#         print('Вызов __new__ для ' + str(cls))
#         return super().__new__(cls)


#     def __init__(self, x=0, y=0):
#         print('Вызов __init__ для ' + str(self))
#         self.x = x
#         self.y = y


# pt = Point(1, 2)
# print(pt.__dict__)


# Нам нужен только 1 экземпляр БД. Для создания только 1 экземпляра используется Singleton
class DataBase: 
    
    __instance = None # Для хранения ссылки на экземпляр класса. Если экземпляра класса нет, то ссылка = None

    def __init__(self, user, passwd, port):
        self.user = user
        self.passwd = passwd
        self.port = port

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

   
    def __del__(self):
        DataBase.__instance = None 


    def connect(self):
        print(f'Соединение с БД пользователя {self.user}, пароль: {self.passwd}, порт: {self.port}')


    def close(self):
        print('Закрытие БД')


    def read(self):
        return 'Чтение с БД'


    def write(self, data):
        print(f'Запись в БД: {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('user', '8765', 40)
# print(id(db), id(db2))
db.connect()
db2.connect()