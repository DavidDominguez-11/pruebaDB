from Usuario import Usuario
from Chatbot import Chatbot
from Traductor import Traductor


class SuperUsuario(Usuario):
    def __init__(self, username, name, password, type_user):
        super().__init__(username, name, password, type_user)
        self.chatbot = Chatbot(username, name, password, type_user)
        self.traductor = Traductor(username, name, password, type_user)

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
