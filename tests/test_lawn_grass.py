import pytest

from utils.lawn_grass import Lawn_Grass


@pytest.fixture
def lawn_grass():
    return Lawn_Grass("Стандартный", "Умеренное устойчивость к механическим нагрузкам", 175.0,
                      1000, 'Russia', 24, "привлекательный ярко-зеленый")


def test_init(lawn_grass):
    assert lawn_grass.name == "Стандартный"
    assert str(lawn_grass) == 'Стандартный, 175.0 руб. Остаток: 1000 шт.'
    prod_1 = Lawn_Grass("Премиум", "Приспособлен к различным почвенным условиям", 200.0,
                        500, 'Italy', 12, "изумрудно-зеленый цвет")
    assert lawn_grass + prod_1 == 275000.0
    assert str(prod_1) == 'Премиум, 200.0 руб. Остаток: 500 шт.'
    assert lawn_grass.__repr__() == ("Lawn_Grass(dict_items([('name', 'Стандартный'), ('description', 'Умеренное "
                                     "устойчивость к механическим нагрузкам'), ('_Product__price', 175.0), "
                                     "('quantity', 1000), ('color', 'привлекательный ярко-зеленый'), "
                                     "('manuf_country', 'Russia'), ('germ_period', 24)]))")
