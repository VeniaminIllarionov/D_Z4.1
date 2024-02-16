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

    def append_product(self, new_product=dict):
        """Добавление продукта"""
        self.__products.append(new_product)
        return self.__products

    @property
    def products_dispaly(self):
        """Конструктор вывода"""
        products = self.__products
        for product in products:
            return f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт."

    def examination_products(self, name, descreption, price, quantity):
        """Проверка продукта есть ли он в списке"""
        new_product = Product.new_product(name, descreption, price, quantity)
        for i in self.__products:
            if new_product['name'] == i['name']:
                i['quantity'] += new_product['quantity']
                if new_product['price'] > i['price']:
                    i['price'] = new_product['price']
                    return self.__products
                else:
                    return self.__products
            else:
                return new_product
