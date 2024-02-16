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
    Product.new_product(["Ione15", "52GB, Gray space", 10000, 80])
    assert Product.name == "Ione15"
    assert Product.price == 10000
    assert Product.description == "52GB, Gray space"
    assert Product.quantity == 80



