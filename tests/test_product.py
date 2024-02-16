import pytest
from utils.product import Product


@pytest.fixture
def product():
    return Product("Iphone15", "512GB, Gray space", 31_000.0, 8)


def test_init_1(product):
    assert product.name == "Iphone15"
    assert product.description == "512GB, Gray space"
    assert product.price == 31000.0
    assert product.quantity == 8
    assert product.new_product("Samsung", "1024 Gb blue", 100000, 20) == {'name': 'Samsung',
                                                                          'description': '1024 Gb blue',
                                                                          'price': 100000.0, 'quantity': 20}


@pytest.fixture
def price():
    return Product("Iphone15", "512GB, Gray space", 10000, 8)


def test_price(price):
    assert price.price_ == 10000
    price.price_ = 0
    assert price.price_ == None
