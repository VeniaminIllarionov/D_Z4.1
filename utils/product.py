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

    @property
    def price_(self):
        return self.__price



    @price_.setter
    def price_(self):
        if self.__price <= 0:
            print("Цена не корректная")
            return





