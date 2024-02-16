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
        self.total_quantity_category = len(self.name)
        self.total_quantity_product = [elem["quantity"] for elem in products]

    @property
    def products(self):
        return self.__products

    def append_product(self, new_product):
        """Добавление продукта"""
        self.__products.append(new_product)
        return self.__products

    @property
    def products_dispaly(self):
        """Конструктор вывода"""
        products = self.__products
        for product in products:
            return f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт."

    def examination_products(self, new_product=list):
        """Проверка продукта есть ли он в списке"""
        new_product = Product.new_product(new_product)
        for i in self.products:
            if Product.name == i['name']:
                i['quantity'] += Product.quantity
                if Product.price > i['price']:
                    i['price'] = Product.price
                    return self.products
                else:
                    return self.products
            else:
                return new_product
