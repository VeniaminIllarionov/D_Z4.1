from utils.product import Product


class Category:
    """класс Category с атрибутами имя, описание, товары, общее количество категорий и общее количество уникальных
    продуктов"""
    name: str
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

    def append_product(self, new_product):
        """Добавление продукта"""
        if not isinstance(new_product, Product):
            raise TypeError('Добавлять можно только объекты Product или его наследников')
        elif not issubclass(type(new_product), Product):
            raise TypeError('Добавлять можно только объекты Product или его наследников')
        elif new_product.quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else:
            self.products.append(new_product)
            Category.total_quantity_product += 1
            return self.products

    @property
    def products_dispaly(self):
        """Конструктор вывода"""

        prod_list = []
        for product in self.__products:
            prod = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            prod_list.append(prod)
        return prod_list

    def examination_products(self, name, description, price, quantity, color):
        """Проверка продукта есть ли он в списке"""
        new_products = Product.new_product(name, description, price, quantity, color)
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

    def __str__(self):
        return f'Название категории {self.name}, количество продуктов: {self.__len__()} шт.'

    def __len__(self):
        sum_product = 0
        for i in self.__products:
            sum_product += i.quantity
        return sum_product

    def average_price(self):
        """Подсчет средней цены продуктов"""
        total_price = []
        average_price = []
        try:
            for i in self.__products:
                total_price.append(i.price * i.quantity)
        except ZeroDivisionError:
            average_price = 0
        average_price = round(sum(total_price) / self.__len__(), 2)
        return average_price



