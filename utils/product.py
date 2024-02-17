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



new_product = Product.new_product('samsung', 'ffsafdf', 520000, 52)
print(new_product.name)
print(new_product.description)
print(new_product.price)
print(new_product.quantity)

