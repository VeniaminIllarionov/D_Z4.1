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

    def examination_products(self):
        """Проверка продукта есть ли он в списке"""
        new_product = [Product.name, Product.description, Product.price, Product.quantity]
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


sss = Product('Samsung', "222", 52000, 25)
aaa = Category(["Смартфоны"], "Смартфон облегчают жизнь", [
    {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    },
    {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    },
    {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }])
sss.new_product(["Ione15", "52GB, Gray space", 10000, 80])
print(sss.name)
print(sss.description)
print(sss.price)
print(sss.quantity)
