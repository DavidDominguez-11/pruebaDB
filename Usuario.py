import database


class Usuario:
    def __init__(self, username, name, password, type_user):
        self.db = database.Database('localhost', 'root', '', 'proyecto_2')
        self.username = username
        self.name = name
        self.password = password
        self.type = type_user

    def get_username(self):
        return self.username

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_type_user(self):
        return self.type_user
