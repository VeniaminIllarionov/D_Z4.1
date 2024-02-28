from abc import ABC, abstractmethod


class AbsClass(ABC):
    '''Abstract class'''
    @abstractmethod
    def __str__(self):
        pass
