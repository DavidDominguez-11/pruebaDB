from abc import abstractmethod, ABCMeta


class ConsultasI(metaclass=ABCMeta):
    @abstractmethod
    def obtener_data(self, usuario_actual):
        pass

    @abstractmethod
    def guardar_data(self, usuario_actual, texto1, texto2):
        pass
