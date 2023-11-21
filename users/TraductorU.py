from users import Usuario


class TraductorU(Usuario):
    def __init__(self, username, id_, password, type_user):
        super().__init__(id_, username, password, type_user)
        self.idioma1 = None
        self.idioma2 = None

    def set_idioma_original(self, text):
        self.idioma1 = text

    def set_idioma_final(self, text):
        self.idioma2 = text

    def get_idioma_original(self):
        return self.idioma1

    def get_idioma_final(self):
        return self.idioma2
