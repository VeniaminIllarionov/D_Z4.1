from abc import ABC, abstractmethod


class AbsClass(ABC):
    '''Abstract class'''
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def new_product(self, name, description, price, quantity, color):
        pass
