class Category:
    '''класс Category с атрибутами имя, описание, товары, общее количество категорий и общее количество уникальных
    продуктов'''
    name: list
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.total_quantity_category = len(self.name)
        self.total_quantity_product = [elem["quantity"] for elem in products]

    @property
    def products(self):
        return self.__products

    def append_product(self, new_product=dict):
        self.__products.append(new_product)
        return self.__products

    @property
    def products_dispaly(self):
        products = self.__products
        for product in products:
            return f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт."

    def examination_products(self, name, descreption, price, quantity):
        new_product = Product.add_product(name, descreption, price, quantity)
        for i in self.__products:
            if new_product['name'] == i['name']:
                i['quantity'] += new_product['quantity']
                if new_product['price'] > i['price']:
                    i['price'] = new_product['price']
                    return self.__products
                else:
                    return self.__products
            else:
                self.__products.append(new_product)
                return self.__products


class Product:
    '''класс Product с атрибутами имя, описание, ценой, количества'''
    name: str
    description: list
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @staticmethod
    def add_product(name, description, price, quantity):
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



    # @classmethod
    # def append_product(cls, new_product):
    # for i in cls.products:
    # if new_product['name'] in i['name']:
    # i['quantity'] += new_product['quantity']
    # elif new_product['name'] not in i['name']:

    # cls.products.append(new_product)
