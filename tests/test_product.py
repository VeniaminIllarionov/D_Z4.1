import pytest

from utils.product import Product


@pytest.fixture
def product():
    return Product.new_product("Iphone15", "512GB", 31_000.0, 8, 'Gray space')


def test_init_1(product):
    assert product.name == "Iphone15"
    assert product.description == "512GB"
    assert product.price == 31000.0
    assert product.quantity == 8
    assert product.color == "Gray space"
    assert str(product) == "Iphone15, 31000.0 руб. Остаток: 8 шт."
    product2 = Product.new_product("Iphone15", "512GB", 10_000.0, 20, 'Blue')
    assert product + product2 == 448000.0
    assert product.__repr__() == ('Создан объект со свойствами name: Iphone15,description: '
                                  '512GB,_Product__price: 31000.0,quantity: 8,color: Gray space,)')
