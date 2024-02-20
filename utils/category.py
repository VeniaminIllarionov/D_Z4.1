from utils.product import Product


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
        # self.total_quantity_category = Category.
        self.total_quantity_product = [elm['quantity'] for elm in products]

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
