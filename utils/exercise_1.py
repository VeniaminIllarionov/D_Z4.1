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




