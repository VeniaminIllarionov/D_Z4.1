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
    assert category.products == [{'description': '256GB, Серый цвет, 200MP камера', 'name': 'Samsung Galaxy C23 Ultra',
                                  'price': 180000.0,'quantity': 5},{'description': '512GB, Gray space',
                                    'name': 'Iphone 15', 'price': 210000.0, 'quantity': 8}, {'description': '1024GB, Синий',
                                    'name': 'Xiaomi Redmi Note 11', 'price': 31000.0, 'quantity': 14}]
    assert category.total_quantity_category == 1
    sum = 0
    for i in category.products:
        sum += i["quantity"]
    assert sum == 27
    assert len(category.products) == 3
    assert category.products_dispaly == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    new_product = Product.new_product('Samsung Galaxy C23 Ultra', 'ffff', 300_000.0, 200)
    assert category.examination_products(new_product) == [
        {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера',
         'price': 300000.0, 'quantity': 205}, {'name': 'Iphone 15', 'description': '512GB, Gray space',
                                               'price': 210000.0, 'quantity': 8},
        {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий',
         'price': 31000.0, 'quantity': 14}]
    assert category.append_product('Xiaomi', '2548gb 520 MPx', 500000, 10) == [
        {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 300000.0,
         'quantity': 205}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8},
        {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14},
        {'name': 'Xiaomi', 'description': '2548gb 520 MPx', 'price': 500000, 'quantity': 10}]

