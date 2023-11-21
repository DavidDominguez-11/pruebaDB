from users import Usuario
from users import Chatbot
from users import TraductorU


class SuperUser(Usuario):
    def __init__(self, id_, username, password, type_user):
        super().__init__(id_, username, password, type_user)
        self.chatbot = Chatbot(id_, username, password, type_user)
        self.traductor = TraductorU(id_, username, password, type_user)

    def set_input_text(self, text):
        self.chatbot.set_input_text(text)

    def set_output_text(self, text):
        self.chatbot.set_output_text(text)

    def get_input_text(self):
        return self.chatbot.get_input_text()

    def get_output_text(self):
        return self.chatbot.get_output_text()

    # Métodos para interactuar con Traductor
    def set_idioma_original(self, idioma):
        self.traductor.set_idioma_original(idioma)

    def set_idioma_final(self, idioma):
        self.traductor.set_idioma_final(idioma)

    def get_idioma_original(self):
        return self.traductor.get_idioma_original()

    def get_idioma_final(self):
        return self.traductor.get_idioma_final()
