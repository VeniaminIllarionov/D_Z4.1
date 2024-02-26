import pytest

from utils.lawn_grass import Lawn_Grass
from utils.smartphone import SmartPhone


@pytest.fixture
def smartphone():
    return SmartPhone("Samsung", "200MP камера",
                      180000.0, 10, 24, 'Galaxy C23 Ultra', 256, 'Серый цвет')


def test_init(smartphone):
    assert smartphone.name == "Samsung"
    assert str(smartphone) == 'Samsung, 180000.0 руб. Остаток: 10 шт.'
    prod_1 = SmartPhone("Iphone ", "Идеальый телефон-смартфон",
                        150000.0, 2, 32, '15', 512, 'Серый цвет')
    assert smartphone + prod_1 == 2100000.0
    assert str(prod_1) == 'Iphone , 150000.0 руб. Остаток: 2 шт.'