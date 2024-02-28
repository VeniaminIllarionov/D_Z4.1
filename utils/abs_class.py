from abc import ABC, abstractmethod


class AbsClass(ABC):
    @abstractmethod
    def __str__(self):
        pass
