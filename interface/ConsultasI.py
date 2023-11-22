from abc import ABC, abstractmethod

class ConsultasI(ABC):
    @abstractmethod
    def obtener_traducciones(self, usuario_actual):
        pass

    @abstractmethod
    def guardar_traducciones(self, usuario_actual, texto_idioma1, texto_idioma2):
        pass
