from Usuario import Usuario


class Traductor(Usuario):
    def __init__(self, username, name, password, type_user, traducciones):
        super().__init(username, name, password, type_user)
        self.idioma1 = traducciones[0]
        self.idioma2 = traducciones[1]

    def get_idioma_original(self):
        return self.idioma1

    def get_idioma_final(self):
        return self.idioma2
