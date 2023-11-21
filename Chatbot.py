from Usuario import Usuario


class Chatbot(Usuario):
    def __init__(self, username, name, password, type_user, chats):
        super().__init(username, name, password, type_user)
        self.input_text = chats[0]
        self.output_text = chats[1]

    def get_input_text(self):
        return self.input_text

    def get_output_text(self):
        return self.output_text
