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
    