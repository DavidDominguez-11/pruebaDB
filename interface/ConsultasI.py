from abc import abstractmethod, ABCMeta
from controllers import Database


class ConsultasI(metaclass=ABCMeta):
    def __init__(self):
        self.db = Database('localhost', 'root', '', 'proyecto_2')

    @abstractmethod
    def obtener_traducciones(self, usuario_actual):
        pass

    @abstractmethod   
    def guardar_traducciones(self, usuario_actual, texto_idioma1, texto_idioma2):
        pass

