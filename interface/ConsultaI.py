from abc import abstractmethod
from abc import ABCMeta


class ConsultaI(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self, username):
        pass

    @abstractmethod
    def save_data(self, username, data1, data2):
        pass
