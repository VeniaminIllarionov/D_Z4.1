import pytest
from utils.category import Category
from utils.product import Product


@pytest.fixture
def category():
    return Category(["Смартфоны"], "Смартфон облегчают жизнь", [
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


def test_init(category):
    assert category.name == ["Смартфоны"]
    assert category.description == "Смартфон облегчают жизнь"
    assert category.products == [
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
        }]
    assert category.total_quantity_category == 1
    sum = 0
    for i in category.products:
        sum += i["quantity"]
    assert sum == 27
    assert len(category.products) == 3
    assert category.append_product("Honor", "1024GB, Белый", 151000.0,154) == [
        {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
         'quantity': 5}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8},
        {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14},
        {'name': "Honor", 'description': '1024GB, Белый', 'price': 151000.0, 'quantity': 154}]
    assert category.products_dispaly == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    new_product = Product('Samsung Galaxy C23 Ultra', 'ffff', 300000, 200)
    assert category.examination_products(new_product) == [
               {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 300000.0,
                'quantity': 205},
               {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8},
               {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14},
               {'name': "Honor", 'description': '1024GB, Белый', 'price': 151000.0, 'quantity': 154}]

