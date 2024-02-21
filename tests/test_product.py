import pytest

from utils.product import Product


@pytest.fixture
def product():
    return Product.new_product("Iphone15", "512GB, Gray space", 31_000.0, 8)


def test_init_1(product):
    assert product.name == "Iphone15"
    assert product.description == "512GB, Gray space"
    assert product.price == 31000.0
    assert product.quantity == 8
    assert str(product) == "Iphone15, 31000.0 руб. Остаток: 8 шт."
    product2 = Product.new_product("Iphone15", "512GB, Gray space", 10_000.0, 20)
    assert product + product2 == 448000.0

