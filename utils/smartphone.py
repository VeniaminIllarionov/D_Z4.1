from utils.abs_class import AbsClass
from utils.mixin_log import MixinLog
from utils.product import Product


class SmartPhone(Product, AbsClass, MixinLog):
    """
    Класс наследние от класса Product
    """
    performance: str
    model: str
    amount_memory: float

    def __init__(self, name, description, price, quantity, performance, model, amount_memory, color):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory



