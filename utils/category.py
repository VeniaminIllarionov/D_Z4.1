from utils.product import Product


class Category:
    '''класс Category с атрибутами имя, описание, товары, общее количество категорий и общее количество уникальных
    продуктов'''
    name: list
    description: str
    products: list
    total_quantity_category = 0
    total_quantity_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_quantity_category += 1


    @property
    def products(self):
        return self.__products

    def append_product(self, name, description, price, quantity):
        """Добавление продукта"""
        new_product = Product(name, description, price, quantity)
        self.__products.append(new_product)
        Category.total_quantity_product += 1
        return self.__products

    @property
    def products_dispaly(self):
        """Конструктор вывода"""
        prod_list = []
        for product in self.__products:
            prod = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            prod_list.append(prod)
        return prod_list

    def examination_products(self, name, description, price, quantity):
        '''Проверка продукта есть ли он в списке'''
        new_products = Product.new_product(name, description, price, quantity)
        for prod in self.__products:
            if new_products.name == prod.name:
                prod.quantity += new_products.quantity
                if new_products.price > prod.price:
                    prod.price = new_products.price
                    return self.__products
                else:
                    return self.__products
            else:
                return new_products
