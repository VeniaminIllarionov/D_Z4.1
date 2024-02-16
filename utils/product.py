class Product:
    '''класс Product с атрибутами имя, описание, ценой, количества'''
    name: str
    description: list
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @staticmethod
    def new_product(name, description, price, quantity):
        """Добавление товара"""
        product_dict = {"name": None, "description": None,
                        "price": None, "quantity": None}
        name_input = name
        description_input = description
        price_input = price
        quantity_input = quantity
        product_dict["name"] = name_input
        product_dict["description"] = description_input
        product_dict["price"] = float(price_input)
        product_dict["quantity"] = int(quantity_input)
        return product_dict

    @property
    def price_(self):
        if self._price <= 0:
            print("Цена не корректная")

    @price_.setter
    def price(self, price):
        self._price = price



