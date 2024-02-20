import pytest

from utils.category import Category
from utils.product import Product



@pytest.fixture
def product():
    return Product.new_product("Iphone15", "512GB, Gray space", 31_000.0, 8)


def test_init_1(product):
    assert product.name == "Iphone15"
    assert product.description == "512GB, Gray space"
    assert product.price == 31000.0
    assert product.quantity == 8
    products = [{'name': "Iphone15", 'price': 301_000.0, 'quantity': 8}, {'name': "Samsung",
                'price': 3_000.0, 'quantity': 8}, {'name': "Xiaomi", 'price': 32_000.0, 'quantity': 7}]
    assert product.examination_products(products) == [{'name': 'Iphone15', 'price': 301000.0, 'quantity': 16},
            {'name': 'Samsung', 'price': 3000.0, 'quantity': 8}, {'name': 'Xiaomi', 'price': 32000.0, 'quantity': 7}]
    products_1 = [{'name': "Samsung", 'price': 3_000.0, 'quantity': 8},
                {'name': "Xiaomi", 'price': 32_000.0, 'quantity': 7}]
    assert product.examination_products(products_1) == ('Iphone15', '512GB, Gray space', 31000.0, 8)



