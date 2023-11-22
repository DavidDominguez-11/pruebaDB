class Usuario:
    def __init__(self, id_, username, password, type_user):
        self.username = username
        self.id_ = id_
        self.password = password
        self.type_user = type_user

    def get_username(self):
        return self.username

    def get_id(self):
        return self.id_

    def get_password(self):
        return self.password

    def get_type_user(self):
        return self.type_user
