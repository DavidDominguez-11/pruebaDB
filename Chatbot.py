from Usuario import Usuario


class Chatbot(Usuario):
    def __init__(self, username, name, password, type_user):
        super().__init(username, name, password, type_user)
        self.input_text = None
        self.output_text = None

    def set_input_text(self, text):
        self.input_text = text

    def set_output_text(self, text):
        self.output_text = text

    def get_input_text(self):
        return self.input_text

    def get_output_text(self):
        return self.output_text
