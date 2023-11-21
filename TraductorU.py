from Usuario import Usuario
import ConsultasI


class Traductor(Usuario):
    def __init__(self, username, name, password, type_user):
        super().__init()
