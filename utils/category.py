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
        self.total_quantity_product = sum(Product.quantity)

    @property
    def products(self):
        return self.__products

    def append_product(self, name, description, price, quantity):
        """Добавление продукта"""
        new_product = {"name": name, "description": description, "price": float(price),"quantity": int(quantity)}
        self.__products.append(new_product)
        return self.__products

    @property
    def products_dispaly(self):
        """Конструктор вывода"""
        products = self.__products
        for product in products:
            return f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт."

    def examination_products(self, new_products):
        '''Проверка продукта есть ли он в списке'''
        for i in self.__products:
            if new_products.name == i['name']:
                i['quantity'] += new_products.quantity
                if new_products.price > i['price']:
                    i['price'] = new_products.price
                    return self.__products
                else:
                    return self.__products
            else:
                return new_products.name, new_products.description, new_products.price, new_products.quantity


