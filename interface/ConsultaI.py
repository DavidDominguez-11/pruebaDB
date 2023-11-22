from abc import abstractmethod
from abc import ABCMeta


class ConsultaI(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass
