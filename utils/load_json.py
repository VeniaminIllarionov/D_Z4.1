import json
from Category import Category, Product


def load_file():
    with open('product.json', "r", encoding="utf-8") as file:
        return json.load(file)


produc = load_file()

for i in produc:
    category_ = Category(i["name"], i["description"], i["products"])
    print(f"Категория:{category_.name},\n"
          f"Описание:{category_.description}")
    for elem in i["products"]:
        product = Product(elem['name'], elem['description'], elem['price'], elem['quantity'])
        print(f"Наименование:{product.name},\nОписание:{product.description},\n"
              f"Цена:{product.price},\nКоличество:{product.quantity}")


