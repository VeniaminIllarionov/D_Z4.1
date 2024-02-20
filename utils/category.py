from utils.product import Product


class Category:
    '''класс Category с атрибутами имя, описание, товары, общее количество категорий и общее количество уникальных
    продуктов'''
    name: list
    description: str
    products: list
    total_quantity_category = 0
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_quantity_category += 1
        self.total_quantity_product = 0

    @property
    def products(self):
        return self.__products

    def append_product(self, name, description, price, quantity):
        """Добавление продукта"""
        new_product = Product(name, description, price, quantity)
        self.__products.append(new_product)
        return self.__products

    @property
    def products_dispaly(self):
        """Конструктор вывода"""
        prod_list = []
        for product in self.__products:
            prod = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            prod_list.append(prod)
        return prod_list
