import json
from exercise_1 import Category, Product

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