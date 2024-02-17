import pytest
from utils.category import Category


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
    assert category.append_product({
        "name": "Samsung A51",
        "description": "1024GB, Белый",
        "price": 51000.0,
        "quantity": 14}) == [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера',
                              'price': 180000.0, 'quantity': 5},
                             {'name': 'Iphone 15', 'description': '512GB, Gray space',
                              'price': 210000.0, 'quantity': 8},
                             {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0,
                              'quantity': 14},
                             {'name': 'Samsung A51', 'description': '1024GB, Белый', 'price': 51000.0, 'quantity': 14}]
    assert category.products_dispaly == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert category.examination_products(
        ["Samsung Galaxy C23 Ultra", '256GB, Серый цвет, 200MP камер', 200000, 10]) == [
               {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 200000.0,
                'quantity': 15},
               {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8},
               {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14},
               {'name': 'Samsung A51', 'description': '1024GB, Белый', 'price': 51000.0, 'quantity': 14}]
