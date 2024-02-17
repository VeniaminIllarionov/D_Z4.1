class Product:
    '''класс Product с атрибутами имя, описание, ценой, количества'''
    name: str
    description: list
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product=list):
        """Добавление товара"""
        cls.name = new_product[0]
        cls.description = new_product[1]
        cls.price = new_product[2]
        cls.quantity = new_product[3]
        return Product(cls.name, cls.description, cls.price, cls.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не корректная")
            return
        self.__price = value


house = Product("dddd", 'ffff', price=50000.0, quantity=96)

print(house.price)
# 50000.0

house.price = -50  # обновили значение
print(house.price)
# 45000.0
