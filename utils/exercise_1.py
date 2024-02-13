import json


class Category:
    '''класс Category с атрибутами имя, описание, товары, общее количество категорий и общее количество уникальных продуктов'''
    name: list
    description: str
    products: list

    def __init__(self, name, description, products):
        global sum
        self.name = name
        self.description = description
        self.products = products
        self.total_quantity_category = len(self.name)
        self.total_quantity_product = [elem["quantity"] for elem in products]


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


def load_file():
    with open('product.json', "r", encoding="utf-8") as file:
        return json.load(file)


produc = load_file()

for i in produc:
    category_ = Category(i["name"], i["description"], i["products"])
    for elem in i["products"]:
        product = Product(elem['name'], elem['description'], elem['price'], elem['quantity'])


print(f"{category_.name}, {category_.description}, {category_.products}")
print(f"{product.name}, {product.description}, {product.price}, {product.quantity}")

