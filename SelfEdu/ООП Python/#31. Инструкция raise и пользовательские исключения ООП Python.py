class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""


class ExceptionPrintData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.message}'


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"Печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintData("Принтер не отвечает")

    def send_to_print(self, data):
        return False
        # return True


p = PrintData()
# p.print("Hello world")
try:
    p.print("Hello world")
except ExceptionPrintData:
    print("Принтер не отвечает")
except ExceptionPrint:
    print("Общая ошибка печати")
