from utils.abs_class import AbsClass
from utils.mixin_log import MixinLog


class Product(MixinLog, AbsClass):
    '''класс Product с атрибутами имя, описание, ценой, количества'''
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color, *args, **kwargs):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @classmethod
    def new_product(cls, name, description, price, quantity, color):
        """Добавление товара"""
        return cls(name, description, price, quantity, color)

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
        return f'{self.name}, {self.price} руб. Остаток: {self.__len__()} шт.'

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise ValueError('Сложение возможно только двух одинковых категорий')

    def __len__(self):
        return self.quantity
