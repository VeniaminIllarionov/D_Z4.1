import pytest
from utils.category import Category
from utils.product import Product


@pytest.fixture
def category():
    cat_list = Category(["Смартфоны"], "Смартфон облегчают жизнь", [])
    cat_list.append_product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера',
                            180000.0, 5)
    cat_list.append_product('Iphone 15', '512GB, Gray space', 210000.0, 8)
    cat_list.append_product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
    return cat_list


def test_init(category):
    assert category.name == ["Смартфоны"]
    assert category.description == "Смартфон облегчают жизнь"
    assert category.products_dispaly == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                         'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                         'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']
    category.append_product('Iphone 15', '512GB', 1555555, 222)
    assert category.products_dispaly == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                         'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                         'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.',
                                         'Iphone 15, 1555555 руб. Остаток: 222 шт.']






