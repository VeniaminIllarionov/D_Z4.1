

class Product:
    '''класс Product с атрибутами имя, описание, ценой, количества'''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        """Добавление товара"""
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не корректная")
            return
        self.__price = value

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.quantity}'


