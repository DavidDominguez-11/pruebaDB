import database


class Usuario:
    def __init__(self):
        self.usuario_actual = None
        self.db = database.Database('localhost', 'root', '', 'proyecto_2')

    def iniciar_sesion(self, nombre, contrasena):
        flag = self.db.verificar_usuario(nombre, contrasena)
        if flag:
            self.usuario_actual = nombre
            return True
        return False

    def cerrar_sesion(self):
        self.usuario_actual = None
