# class MyArray(list):
#     def __init__(self, value: list, max_items: int):
#         super().__init__()
#         self.value = value
#         self.max_items = max_items
#
#     def __iter__(self):
#         return super().__iter__
#
#     def append(self, __object) -> None:
#         if len(self.value) == self.max_items:
#             return
#         self.value.append(__object)
#
#     def __str__(self):
#         return str(self.value)


class MenuItem:
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def is_vegetarian(self):
        return self._vegetarian


class PancakeHouseMenu:
    def __init__(self):
        self._items: list[MenuItem] = []
        self.add_item('K&B Pancake Breakfast', 'Pancake with scrambled eggs and toast', True, 2.99)
        self.add_item('Regular Pancake Breakfast', 'Pancake with fried eggs and sausage', False, 2.99)
        self.add_item('Blueberry Pancake', 'Pancake made with fresh blueberries', True, 3.49)
        self.add_item('Waffles with your choice of blueberries or strawberries',
                      'Pancake with scrambled eggs and toast', True, 3.59)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float):
        item = MenuItem(name, description, vegetarian, price)
        self._items.append(item)

    def get_menu_items(self) -> list:
        return self._items


class DinerMenu:
    def __init__(self):
        self._items = []
        self.max_items = 6
        self.add_item('Vegetarian BLT', '(Fakin") Bakon with lettuce & tomato on whole wheat', True, 2.99)
        self.add_item('BLT', 'Bakon with lettuce & tomato on whole wheat', False, 2.99)
        self.add_item('Soup of the day', 'Soup of the day with a side of potato salad', False, 3.29)
        self.add_item('Hotdog', 'A hot dog with saurkraut, relish, onions, topped with cheese', True, 3.59)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float):
        item = MenuItem(name, description, vegetarian, price)
        if len(self._items) >= self.max_items:
            raise Exception(f'Максимальное количество должно быть не больше {self.max_items}')
        self._items.append(item)

    def get_menu_items(self) -> list:
        return self._items


if __name__ == '__main__':
    menu = PancakeHouseMenu()
    print(menu.get_menu_items())
    