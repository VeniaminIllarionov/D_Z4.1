from utils.product import Product


class Lawn_Grass(Product):
    """
    Класс наследние от класса Product
    """
    manuf_country: str
    germ_period: int

    def __init__(self, name, description, price, quantity, manuf_country, germ_period, color):
        super().__init__(name, description, price, quantity, color)
        self.manuf_country = manuf_country
        self.germ_period = germ_period
