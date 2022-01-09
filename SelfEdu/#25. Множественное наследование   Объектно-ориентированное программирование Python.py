class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("Goods __init__")
        self.name = name
        self.weight = weight
        self.price = price


    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print("MixinLog __init__")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: товар был продан в 00:00')


class MixinLog2:

    def __init__(self):
        print("MixinLog2 __init__")



class NoteBook(Goods, MixinLog, MixinLog2):
    pass

 
n = NoteBook('Acer', 1.5, 30000)
n.print_info()
n.save_sell_log()
print(NoteBook.__mro__)