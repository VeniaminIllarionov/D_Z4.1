import pytest
from utils.category import Category
from utils.product import Product


@pytest.fixture
def category():
    Product.name = "Samsung Galaxy C23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"
    Product.description = "256GB, Серый цвет, 200MP камера", "512GB, Gray space", "1024GB, Синий"
    price = 180_000.0, 210_000.0, 31_000.0
    Product.quantity = 5, 8, 14
    return Category(["Смартфоны"], "Смартфон облегчают жизнь",
                    [{"name": Product.name[0], "description": Product.description[0], "price": price[0],
                      "quantity": Product.quantity[0]},{"name": Product.name[1], "description": Product.description[1],
                     "price": price[1],"quantity": Product.quantity[1]},{"name": Product.name[2],
                     "description": Product.description[2], "price": price[2],"quantity": Product.quantity[2]}])


def test_init(category):
    assert category.name == ["Смартфоны"]
    assert category.description == "Смартфон облегчают жизнь"
    assert category.products == [{'name': 'Samsung Galaxy C23 Ultra',
                                  'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5},
                                 {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8},
                                 {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]
    assert category.total_quantity_category == 1
    assert category.total_quantity_product == 27
    assert len(category.products) == 3
    assert category.append_product("Honor", "1024GB, Белый", 151000.0,154) ==[
        {'description': '256GB, Серый цвет, 200MP камера', 'name': 'Samsung Galaxy C23 Ultra', 'price': 180000.0,
              'quantity': 5}, {'description': '512GB, Gray space', 'name': 'Iphone 15', 'price': 210000.0, 'quantity': 8},
             {'description': '1024GB, Синий', 'name': 'Xiaomi Redmi Note 11', 'price': 31000.0, 'quantity': 14},
             {'description': '1024GB, Белый', 'name': 'Honor', 'price': 151000.0, 'quantity': 154}]
    assert category.products_dispaly == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    new_product = Product.new_product('Samsung Galaxy C23 Ultra', 'ffff', 300_000.0, 200)
    assert category.examination_products(new_product) == [
        {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера',
         'price': 300000.0, 'quantity': 205}, {'name': 'Iphone 15', 'description': '512GB, Gray space',
         'price': 210000.0, 'quantity': 8}, {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий',
         'price': 31000.0, 'quantity': 14}, {'name': 'Honor', 'description': '1024GB, Белый',
                                             'price': 151000.0, 'quantity': 154}]


