import pytest
from utils.exercise_1 import Category, Product


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


@pytest.fixture
def product():
    return Product("Iphone15", "512GB, Gray space", 31_000.0, 8)


def test_init_1(product):
    assert product.name == "Iphone15"
    assert product.description == "512GB, Gray space"
    assert product.price == 31000.0
    assert product.quantity == 8
    assert product.add_product("Samsung", "1024 Gb blue", 100000, 20) == {'name': 'Samsung',
                                                                          'description': '1024 Gb blue',
                                                                          'price': 100000.0, 'quantity': 20}
    print(product.examination_products)
