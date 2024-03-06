import pytest
from utils.category import Category
from utils.product import Product


@pytest.fixture
def category():
    cat_list = Category("Смартфоны", "Смартфон облегчают жизнь", [])
    prod_1 = Product.new_product('Samsung Galaxy C23 Ultra', '256GB, 200MP камера',
                                 180_000.0, 5, 'Серый цвет')
    cat_list.append_product(prod_1)
    cat_list.append_product(Product('Iphone 15', '512GB', 210_000.0, 8, 'Gray space'))
    cat_list.append_product(Product('Xiaomi Redmi Note 11', '1024GB', 31_000.0, 14, 'Синий'))

    return cat_list


def test_init(category):
    assert category.name == 'Смартфоны'
    assert category.description == "Смартфон облегчают жизнь"
    assert category.products_dispaly == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                         'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                         'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']
    category.append_product(Product('Iphone 15', '512GB', 250_000.0, 222, 'Gray space'))
    assert category.products_dispaly == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                         'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                         'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.',
                                         'Iphone 15, 250000.0 руб. Остаток: 222 шт.']
    assert category.total_quantity_category == 1
    assert category.total_quantity_product == 4
    category.examination_products('Samsung Galaxy C23 Ultra', '256GB, 200MP камера',
                                  250000.0, 25, 'Серый цвет')
    assert category.products_dispaly == ['Samsung Galaxy C23 Ultra, 250000.0 руб. Остаток: 30 шт.',
                                         'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                         'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.',
                                         'Iphone 15, 250000.0 руб. Остаток: 222 шт.']
    assert str(category) == 'Название категории Смартфоны, количество продуктов: 274 шт.'
    assert category.average_price() == 2704.38
